# Grafana SCIM Setup Tutorial: Sync Teams Easily | Grafana 12 | Grafana Labs

In this demo, Sarah, a product manager at Grafana, walks you through how SCIM (System for Cross-domain Identity Management) ...

Published on 2025-05-07T10:01:06Z

URL: https://www.youtube.com/watch?v=dJSjoLawamk

Transcript: I'm Sarah, a product manager at Grafana,
and today I'm going to talk about SCIM. Previously, to get a
team set up in Grafana, you'd have to provision users
from your identity provider, and then you'd have to create the
team and sync the users into the team. And then a user would have to log
in to actually exist in the team. So this was pretty complicated.
If it was done using pipelines, maintenance was required and
setup was a bit tough too. And then onboarding teams could be slowed
down just by the fact that they need to log in to get stuff going. So
let's talk about SCIM. Here I am in the instance at the moment, there's
only one team existing in the instance. If I head over to Okta and look at groups, this is the group that
I want to sync into the instance: Collaborators@Company and
it's got two users in it. If I head over to applications, we've already
set up SCIM with this instance. And now if I had to push
groups and choose to create the group: Collaborators@Company
in the instance, you can see that it's pushing
and now it says it's active. So if I head back to the
instance and refresh, now we see that this group has
already been created as a Grafana team in the instance. No extra
work required. At the moment, it doesn't have any members in it, and that's because I have to also
set up the assignment of users in the Okta group to be synced to the
Grafana team that we've just pushed over there. So I head to assignments,
I can assign to groups, I can see the Collaborators@Company
group and click assign. It's assigned now. So there you go. I've set up the assignment and the
two folks that were in that group now also have been shown here. So if I head back to the
instance and refresh, so now we can see that those members
have been synced to this team. And this is really
powerful for apps like IRM, because without the users
ever having to log in, you can get them set up in the
instance and add them to things like schedules. You could here, you could assign that team, you
could add 'em, things like schedules, and then you could add them to
things like escalation chains. Again, you could start
picking people from that team. And that means that you can avoid waiting
for users to log in before you can set 'em up to be on call for
a particular application.

