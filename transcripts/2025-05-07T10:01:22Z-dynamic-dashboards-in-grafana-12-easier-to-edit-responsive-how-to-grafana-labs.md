# Dynamic Dashboards in Grafana 12: Easier to Edit + Responsive | How to | Grafana Labs

Dynamic Dashboards bring a more intuitive and sleek dashboarding experience that's built on the robust foundation of the Scenes ...

Published on 2025-05-07T10:01:22Z

URL: https://www.youtube.com/watch?v=tH7dQWRMniM

Transcript: Hi. The dashboards are at the heart
of Grafana. Last year, in Grafana 11, we have taken a big step forward. We've moved our core dashboards
over to the new Scenes library. These unlocked features and flexibility
we just couldn't achieve with the old setup. I'm Thanos, a group product manager here
at the Grafana Labs and I
want to show you what we have been building over the past
few months. But before we dive in, let's look a few common challenges
with today's experience. Grafana dashboards can get big,
pulling data from any sources, serving different users and covering
complex systems. While they're powerful, most users, they find relevant only a small part
of the info in a day-to-day basis. Template variables. Collapsible rows help, but still can leave empty
panels, which can be confusing. Layouts also don't adapt
well to different screens, and navigation can be slow with too much
scrolling and expanding sections. Let's see what we have built to address
these challenges. Alright, let's take a look at how we can make this
dashboard a bit better. To start with, we have improved the way you switch
between editing and viewing a dashboard while preserving the ability to
share it from both states. Okay, we now have the option to choose between
a custom layout or an auto layout. The auto option is great. It lets
you set things like column width or row height, and it adjusts the layout automatically
based on screen size and other conditions. Next, we can organize panels into rows or tabs
to create a structure that works best for us. You can set things up with rows
inside tabs or the other way around, and if you need something more advanced, you can even nest layouts to
handle more complex setups. Let's try and group
these panels a bit more. So I'm going to create two more rows and I'm going to move
some of the panels here. Okay, this looks good, but I think
for the screen size that I have, these panels look a bit bigger,
so I'm going to change the layout and I'll make the row
height too short and I want a narrow width. That looks good. Let's move the rest of the panel
in another row. Looks good. Because these two metrics
have the main ones, I want to emphasize them a bit more, so I'm going to increase the row
height. I think that looks better. Even with a clean layout, not
every panel is always useful. Sometimes panels don't have data or
aren't relevant based on variable selections. Now we can set rules to hide or show
panels or rows based on those conditions. Keeping the dashboard cleaner and more
focused. Let's see how we can do that. In this dashboard, I can see that some panels return the
message of no data based on a specific variable value. I want to hide those
panels because they create noise. So having the panel selected, I see
a new option. Show height rules. I'm going to set the panel visibility
tool into height and I'm going to add the rule. Currently we support
three rule types, query result, template variable and
timeframes. In this case, I'm interested about the query result. We can see that we applied an overlay
over this panel to showcase that this panel is going to be hidden. And what this actually says
is that because we have set
a rule that when a query returns the data, hide
the panel. Of course, you can hide or show
panels based on your needs. I want to do the same for
the rest of the panels, but I don't want to do it in each
one of the panels separately. So I want to do it on a row level.
I'm going to select the row. And similarly under the row visibility
toggle I'm going to select height and other rows based on the template variable. I'm going to select template
variable that I'm interested at and I'm going to select
sqlite. So similarly, we can see that we applied this
overlay that showcases that our row is going to be hidden. And
finally, to make navigation easier, we're introducing something similar
to what you see in Explore - dashboard outline. It lets you jump straight to specific
panels or other items of a dashboard and even do quick actions like
collapse in the name section. Let's give this new tab a new name. We're really excited about
what we've built so far, but we're even more excited
because this is just the beginning. We have more ideas coming
and we'd love your feedback. So feel free to reach out to me directly
in the community or in our channels. Would love to hear from you.

