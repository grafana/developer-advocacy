# Interactive Learning in Grafana: Context-Aware Help and Tutorials in the Grafana UI

Published on 2025-11-19T21:06:41Z

## Description

Grafana's new Interactive Learning brings context-aware help, step-by-step tutorials, and full in-product docs right into the UI—so ...

URL: https://www.youtube.com/watch?v=ZB_T2yQMR20

## Summary

In this video, Jay Clifford and Tom, both senior developer advocates at Grafana Labs, introduce a new interactive learning experience designed to enhance the help menu within Grafana. They discuss challenges related to accessing documentation while using the platform, explaining how the new feature allows users to access context-aware documentation and guided learning directly within Grafana. The interactive learning side panel, accessible via the help button, provides personalized help based on the user's current activities, with features like tutorials that include "show me" and "do it" buttons for a hands-on learning approach. Future plans include custom runbooks, integration with Grafana Assistant, and a workshop mode for live training sessions. The interactive learning feature is currently in public preview for version 12.3, and community contributions are encouraged to shape its development.

## Chapters

00:00:00 Introductions of presenters Jay and Tom  
00:01:30 Overview of the challenges with current documentation  
00:02:45 Introduction of the new interactive learning feature  
00:03:30 Accessing the interactive learning experience in Grafana  
00:04:15 Context-aware help and documentation rendering  
00:05:00 Explanation of interactive tutorials  
00:06:20 Demonstration of the Prometheus 101 tutorial  
00:07:45 Details on the recommender service for personalized learning  
00:08:30 Offline mode privacy considerations  
00:09:15 Future plans for custom runbooks and workshop mode

# Interactive Learning Experience at Grafana Labs

Hi, my name is **Jay Clifford**, a senior developer advocate here at Grafana Labs. 

And I'm **Tom**, also a senior developer advocate here at Grafana Labs. We've been developing a brand new, interactive learning experience—a feature that makes the help menu a little bit more helpful within Grafana. 

## Background

Tom, do you want to take us back to where it all began?

Thanks, Jay. One of the challenges we've always had is that our documentation lives outside of Grafana. Now, don't get me wrong, it's fantastic, highly detailed, and well-maintained, but when you're in the middle of using Grafana and you hit a problem, you have to stop what you're doing, leave the product, and search through the docs site to find the right solution. 

We wanted to make that easier by bringing help closer to where it's needed most—directly inside of Grafana. That’s where it hit us: we are rendering documentation directly in Grafana. This means we have the ability to interact with components within your Grafana instance. Documentation no longer has to stay static; it becomes a wizard-like experience to teach concepts to new users directly from within your instance. More on that in a bit.

## Accessing the New Experience

So, where can you find this new magical experience, you might be asking? You'll find the new interactive learning experience by clicking the **question mark icon** in the top right of Grafana. That's the same help button that’s always been there. 

Previously, it showed a few links out to places like our Docs and Community Forum. Now, it opens a whole new side panel that gives you contextual help in product docs and even guided learning journeys—all without leaving Grafana.

When you open the new interactive learning side panel, what you'll see depends on where you are inside of Grafana. The content is completely context-aware. Whether you're looking at a dashboard, editing a data source, or performing an action like creating a bar chart visualization, it automatically surfaces documentation and learning material that's relevant to what you are doing at that moment.

And this isn't just plain text either. You're actually seeing the full documentation rendered right inside of Grafana—complete with images, videos, and step-by-step examples. There’s no need to jump out to a browser tab or go searching for what you need.

## Interactive Tutorials

Jay's going to show us how we've taken that even further with the new interactive tutorials. 

**Interactive tutorials** are a new component found within our documentation. They provide a series of interactive steps that you can follow within the Grafana UI. It’s probably easier to show you with the **Prometheus 101 tutorial**. In this tutorial, we’ll guide you through setting up your first Prometheus data source and dashboard in Grafana.

Each step can either have a **show me** or a **do it** button. Clicking the **show me** button highlights the desired UI element and can also provide some further contextual information, while the **do it** button executes the action the step is asking you to complete. This could be clicking a button, filling in a form, or asking you to carry out a series of steps yourself. 

You can also take this a step further and run an entire section. This will run all steps sequentially so you can watch the process unfold. Of course, you can cancel this action at any time.

## Underlying Technology

Interactive Learning is made possible by two services: the **frontend plugin** and the **recommendation service**. Think of the recommender as a knowledgeable Grafana sidekick that can provide highly personalized documentation and interactive learning journey recommendations based on where and what you are doing in Grafana. 

It uses information such as your current path in Grafana, what data source types you are using, your user role, and your current intent—like creating a dashboard or editing a data source. 

We want to make it clear from the beginning that we respect our OSS users' privacy. That’s why we will always have an **offline mode**, which is enabled by default. This mode provides you with a great base set of recommendations based on your location in Grafana but does not need to connect to our recommender service. 

If you feel comfortable enough to enable the recommender, this will provide further documentation suggestions based on your actions within Grafana.

## Future Plans

This is only the start for interactive learning within Grafana. Tom, can you take us through some of our future plans for the new help bar in Grafana?

First up, **custom runbooks**. We want to let you create your own interactive learning experiences right inside of Grafana. This could be anything from onboarding new team members to walking people through your own workflows or internal processes. 

We’re also exploring ways to connect this with **Grafana Assistant**, our in-product AI experience that helps you analyze data and build dashboards. The idea is to combine the power of Assistant with guided learning, making it even easier to understand and explore your data, though that’s still something we’re experimenting with.

Finally, **workshop mode**. This is where things get really interesting. Imagine being able to host a live shared session where a presenter can guide a group through Grafana step-by-step in real time. It could be used for training sessions, team onboarding, or community workshops.

## Getting Started

So, Jay, how can people get started with the new interactive learning feature in Grafana?

We’re excited to be releasing the interactive learning experience under **public preview** for version 12.3. This means it sits underneath a feature flag, so you can enable it using the environment variable that you see on screen. Alternatively, you can install the plugin directly via the plugin catalog by searching for **interactive learning**. 

Like Grafana, the Interactive Learning plugin will be under an **AGPL license**, and you can find the repo by heading to this link. We’re always happy to accept contributions, whether that’s feedback, ideas, or improvements. This whole feature has been shaped by community input, and with your help, we can’t wait to see where it goes next.

## Raw YouTube Transcript

Hi, my name is Jay Clifford, a senior
developer advocate here at Grafana Labs. And I'm Tom, also a senior developer
advocate here at Grafana Labs. We've been developing a brand new,
interactive learning experience, a feature that makes
the help menu, well... a little bit more helpful
within Grafana. Tom, do you want to take us back
to where it's all began? Thanks, Jay. One of the challenges we've always had
is that our documentation lives outside of Grafana. Now, don't get
me wrong, it's fantastic, highly detailed and well-maintained, but when you're actually in the middle
of using Grafana and you hit a problem, you've got to stop what you're
doing, leave the product, and go digging through the docs
site to find the right solution. We wanted to make that easier by bringing
help closer to where it's needed most - directly inside of Grafana. And that's where it hit us. We are rendering documentation
directly in Grafana, meaning we have the ability to interact
with components within your Grafana instance. Documentation no
longer has to stay static, but becomes a wizard-like experience
to teach concepts to new users - directly from within your
instance. More on that in a bit. So where can you find this new magical
experience you might be asking? You'll find the new interactive learning
experience by clicking the question mark icon. In the top right of Grafana. That's the same help button
that's always been there. Before, it showed a few links out to places
like our Docs and Community Forum. Now it opens a whole new side panel that
gives you contextual help in product docs and even guided learning
journeys, all without leaving Grafana. So when you open the new
interactive learning side panel, what you'll see depends on
where you are inside of Grafana. The content is completely context aware. So whether you're looking at a
dashboard, editing a data source, or performing an action like
creating a bar chart visualization, it automatically surfaces documentation
and learning material that's relevant to what you are doing right there and then.
And this isn't just plain text either. You're actually seeing the
full documentation rendered
right inside of Grafana - complete with images, videos,
and step-by-step examples. So there's no need to jump out to a
browser tab or go searching for what you need. Jay's going to show us how we've
taken that even further with the new interactive tutorials. Interactive tutorials are a new
component found within our documentation. It provides a series of interactive steps
that you can follow within the Grafana UI. It's probably easier to show you
with the Prometheus 101 tutorial. In this tutorial, we'll guide you through setting up
your first Prometheus data source and dashboard in Grafana. Each step can either have a
show me or a do it button. Clicking the show me button highlights
the desired UI element and can also provide some further
contextual information. While the do it button executes the
action the step is asking you to complete. This could be clicking a
button, filling in a form, or asking you to carry out
a series of steps yourself. You can also take this a step
further and run an entire section. This will run all steps sequentially
so you can watch the process unfold. Of course, you can cancel this action at any time.
Interactive Learning is made possible by two services: the frontend plugin and
the recommendation service. Think of the recommender as the super
knowledgeable Grafana sidekick that can provide highly personalized documentation
and interactive learning journey recommendations based on where
and what you are doing in Grafana. It uses information such as
your current path in Grafana, what data source types you are using, your user role and your current intent. Like creating a dashboard
or editing a data source. We want to make it clear from the
beginning that we respect our OSS user's privacy. That's why we shall
always have an offline mode, which is enabled by default. This mode provides you with a great base
set of recommendations on where you are in Grafana, but does not need to
talk to our recommender service. If you feel comfortable enough
to enable the recommender, this will provide further documentation
suggestions based on your actions within Grafana. This is only the start for interactive
learning within Grafana. Tom, can you take us through some of our
future plans for the new help bar in Grafana? First up, custom run runbooks. We want to let you create
your own interactive learning
experiences right inside of Grafana. That could be anything from onboarding
new team members to walking people through your own workflows
or internal processes. We're also exploring ways to
connect this with Grafana Assistant, our in-product AI experience that helps
you analyze data and build dashboards. The idea is to combine the power
of Assistant with guided learning, making it even easier to
understand and explore your data, though that's still something we're
experimenting with. And finally, workshop mode. This is where
things get really interesting. Imagine being able to host a live shared
session where a presenter can guide a group through Grafana
step-by-step in real time. It could be used for training sessions,
team onboarding, or community workshops. So Jay, how can people get started with the new
interactive learning feature in Grafana? We're excited to be releasing
the interactive learning
experience under public preview for 12.3. This means it
sits underneath a feature flag, so you can enable it using
this environment variable
that you see on screen. Or you can install the plugin directly
via the plugin catalog by searching interactive learning. Like Grafana, the Interactive Learning plugging
will be under an AGPL license, and you can find the repo
by heading to this link. We're always happy to accept
contributions, whether
that's feedback, ideas, or improvements. This whole feature has been shaped by
community input and with your help, we can't wait to see where it goes next.

