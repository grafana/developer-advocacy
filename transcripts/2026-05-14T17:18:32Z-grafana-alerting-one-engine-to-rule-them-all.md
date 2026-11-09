# Grafana Alerting: One Engine to Rule Them All

Published on 2026-05-14T17:18:32Z

## Description

Grafana Alerting is now the single alerting engine you need — covering everything Prometheus, Mimir, and Loki could do, with a ...

URL: https://www.youtube.com/watch?v=6l6F687MSyI

## Summary

The show "Grafana Alerting: One Engine to Rule Them All" was published on May 14, 2026, featuring Sonia Aguilar and Alexander, both software engineers at Grafana Labs. The discussion focused on the evolution of Grafana Alerting, which now serves as a unified alerting engine for Prometheus, Mimir, and Loki, addressing challenges such as scaling and managing multiple teams. Key features highlighted include the new import tool for migrating existing alerts, multi-policy trees for better team management, and enhanced alert activity tracking for improved visibility into alert performance and notification history. The presenters emphasized the importance of Grafana Alerting as a comprehensive solution for organizations of all sizes.

Topics: Grafana Alerting, scaling, import tool, multi-policy trees, alert activity tracking.

## Chapters

00:00:00 Introduction to Grafana Alerting and its evolution
00:06:13 Grafana Alerting features and improvements
00:12:22 Importing alert rules into Grafana Alerting
00:17:50 Overview of Grafana Alerting features

## Grafana Alerting: One Engine to Rule Them All

**Published:** 2026-05-14T17:18:32Z

---

**Sonia Aguilar:** Hi. Welcome to our talk. We are here to show you why Grafana Alerting is ready to be your single alerting engine and how easy it is to get started. I'm Sonia Aguilar, and I'm one of the software engineers here at Grafana Labs.

**Alexander:** And I'm Alexander, I'm also a software engineer at Grafana Labs. When Mat asked how many of you have been woken up by alerting, I'm glad that I was backstage and didn't see that. 

So here's what we have for you today. We're going to start with a quick recap of how Grafana Alerting got to where it is now, what challenges we had to solve to make it better, how to bring your existing alerts into Grafana from another system, understand what's happening with them, whether notifications went out or not, and we also have some live demos.

Let's just start with a quick recap. When Grafana started, everything was about dashboards and visualizations. Alerting? Alerting was living in external systems like Prometheus. Then, with Grafana 4, we created our first alerting engine. It was basic, one-dimensional, and focused on Graphite. Over time, Prometheus, Mimir, and Loki became popular, and we built unified alerting, where you could manage alert rules from different systems in a single place. We also added the ability to create multi-dimensional alerts.

However, we realized that having two types of alerts—Grafana-managed alerts and data source-managed alerts—was adding complexity and sometimes confusion for users. Internally at Grafana, we were using Prometheus, Mimir, and Loki, each with their own alerting system, which created a bit of everything. At the same time, teams like security were adopting Grafana Alerting, and more users were asking us, "Which system should I use?" The problem was that having two options was adding more confusion than clarity. This confusion told us we needed to make a decision, and we did. We decided to double down on Grafana Alerting.

The result is an alerting system that has the best of these systems. Grafana Alerting is now a mature, scalable, and fully featured alerting engine. It has everything you could expect from Prometheus and more. We can call it alerting in the big tent because you can query from almost any data source you need and notify through most of the integrations you need. We have over 50 different data sources and 22 types of integrations, and counting.

To get here, we had to solve some big challenges, and Alexander will show you how.

**Alexander:** One of the challenges we had to solve is scaling because Grafana Alerting runs everywhere, from small teams with just a few rules to large organizations with thousands of alerts. As Sonia mentioned, we use it internally too, so we've seen what happens when things grow. There are really two sides to it. First, your system gets bigger, you have more alert rules and increased load on your database and data sources. But also, your organization gets bigger. You have more teams, and each team needs their own space. It also gets harder to understand what's happening across hundreds of rules and notification policies.

Let's start with the system side. Imagine you have one Grafana instance. It runs your alerting, queries data sources like Mimir, Tempo, and Loki, and writes alert state to the database. It's simple and easy to manage, but if it goes down, your alerting goes down with it. So, what do you do? Well, you panic, of course, but then you add a second Grafana. Now you have two instances running in high availability mode. If one fails, the other keeps evaluating. So you've got redundancy. 

However, it also means that both of them evaluate all alert rules independently. Your data source cluster and your database are getting hit twice for the exact same rules, and it all compounds. If you start five Grafanas, you'll get five times the load. Grafana needs to save alert state after each evaluation, so that's often where we feel the pain first.

There are a few things that Grafana can do already to reduce the database pressure. For example, **compressed state** allows Grafana to save the state of the whole rule at once instead of saving every single alert instance independently, reducing the number of queries it needs to make. 

Another option is **evaluation jitter**. Without it, Grafana runs all alert rules on the same interval at once, creating a thundering herd that slams your database and data sources. Instead, it can calculate a deterministic offset and spread rule evaluations evenly across the interval. 

The third option is **periodic saves**. Grafana saves alert state to the database after each evaluation, but it can also buffer the state in memory and flash to the database periodically, let's say, every five minutes. Of course, there is a trade-off. If Grafana crashes during those five minutes, you lose unsaved transitions, and they recover on the next evaluation. 

All these options help with database pressure, but they don't fix the fundamental issue that every replica is still doing all the work. That's what we fixed in Grafana 13. Now you can have one replica evaluate alert rules while the others stand by. Your data source and database loads stay the same no matter how many replicas you run. It uses the same cluster membership that Grafana Alert Manager already has, deciding which replica is the primary, and if it goes down, another one takes over automatically. 

During this failover process, there is a brief gap in rule evaluations. So before enabling this new mode, you need to pick what matters to you more: zero-gap redundancy or constant load on your database and data sources. If you already use high availability in production, you can enable this new mode with just one single config flag. It's available in Grafana 13, as I mentioned, and it's open source.

But scaling isn't just about load; it's also about handling more teams as your organization grows. For that, we've had role-based access control for a while now. Teams can own rules in folders with fine-grained control over who can change their alerting, and contact points have access control too. However, one piece was missing: notification policies. 

The routing tree that decides where notifications go when something fires or resolves was a problem when everyone shared a single policy tree. At scale, it becomes a nightmare to manage when different teams change the same config, and there's always a risk of breaking someone else's routing by accident. 

I really like this image. It was generated by AI, but I think it represents a complicated notification policy tree really well. You see there are different shapes, different colors; nobody really knows why, but it looks important, and they can't really delete it. 

So we fixed that as well. Now you can have multiple notification policy trees, where each team gets their own routing, small config, and they can change it however they want. Changes to one tree don't affect anyone else, so you can't break someone else's alerting by accident. That's how Grafana now scales with both your infrastructure and your teams.

But what if you want to move your existing alerting from another system like Mimir, Loki, or some other system to Grafana? What do you do?

**Sonia Aguilar:** Exactly. Let's talk about how we get started with Grafana Alerting. There are two ways to get started. One is creating all rules from scratch. For this, you can use the UI or you can use provisioning—file provisioning, API provisioning, or Terraform. 

If you are already running your alerting system in Prometheus, Mimir, or Loki, and you want to onboard into Grafana Alerting, we have built an import tool that lets you bring your alerting system...

directly into Grafana. If you prefer creating all rules from scratch using the UI, in GrafanaCON last year, we already showed you how we made it easier than ever. We simplified the way you define the query and condition, and we also simplified the way you define how an alert rule is going to be routed with the simplified routing that allows you to select the contact point in the alert rule form.

But let's talk about the new import tool. We have built a Prometheus compatibility layer directly into Grafana. This means that now you can import your alert rules and your Alertmanager configuration into Grafana Alerting. With this import tool, you don't need to copy-paste anything. You don't need to rewrite expressions. Your alerts will work in Grafana.

How does this work? Do you remember the multi-policy tree feature that Alexander showed us? This is where this feature becomes crucial. When we are importing from Prometheus, Mimir, and Loki, we are creating a new policy tree in Grafana with the imported policies, and we assign this policy tree to each imported alert rule. Your existing policies in Grafana stay untouched.

There are two ways to import: one is using the API and the other is using the UI. Let's talk about the API. If you have everything in CI/CD or lots of data sources to import, your best option is using the API. This API is fully compatible with mimirtool and cortextool. This means that you can continue using the same workflows and commands. You only need to target the new import endpoint, and your alerting system will be automatically imported into Grafana.

If you prefer a guided experience and don't have many data sources to import, we have built a new wizard in the UI, which is a good option for you. 

Let's go to the demo. We are here in the alert list view. In this menu, we have a new item: **Import to Grafana Alerting**. Let's click on it. This is the new import wizard. As you can see on the left, it is a basic three-step process, and the order in this wizard is intentional. First, we need to import notification resources. 

The first thing we have to do is decide the import source. Where is this Alertmanager stored? You can use a YAML file or a data source. In my case, I want to import the Alertmanager that lives in a data source, in particular, this one. Let's select this one. Then, you need to decide the name for the new policy tree that is going to be created in Grafana with the imported policies. The UI automatically uses the same name as the data source we decided here. You can edit it, of course, but I'm going to go ahead with this name. The UI is also doing some validation, checking for any conflicts. For example, if we want to import a contact point with a name that already exists in Grafana, we do some deduplication and rename these imported resources.

Let's go to the next step. This step is about importing alert rules. The first thing we have to decide is which policy tree we want to use for these imported rules. The UI automatically selects the policy tree name that we decided in the previous step. You can select another one, but I'm going to go ahead with this one. Then, you have to decide the import source. Where are these alert rules stored? You can use a YAML file or a data source. In my case, I want to import all the alert rules that live in this data source, so I'm going to select this one. You can also filter by namespace and group, but I want to import all the alert rules that live in this data source, so I'm not going to use any filter here.

Next, you need to select the target folder in Grafana. This will be the folder where all the imported rules are going to be created. I'm going to select this one. You can see two checks that are enabled by default. This is very important because it means that all the imported rules, once they are imported, are going to stay paused. This means that they are not going to start being evaluated yet. This gives you some time to review that everything looks correct in Grafana, and once you see that everything is correct, that is the moment you can unpause them.

Let's go to the last step. The last step is about reviewing that everything you want to import is correct. You can review notification resources, in this case, the Alertmanager that we want to import. You can also review the 10 rules that we are going to import. All right. We are ready. Let's click the button, **Start Importing**, and confirm. We are done. The UI has redirected us to the alert list view, filtered by the target folder that we decided during the import. We can see here all the imported rules that are now Grafana managed rules, and all of them are paused.

Now, let's imagine that everything looks fine. We can come here to the folder level, and we have this new feature, these three bulk actions. The interesting one for us is the second one, **Resume All Rules**. That means that all the rules in this folder are going to be unpaused. 

Let's take a look at one of these imported rules. We can see the query expressions. The interesting part here is in the **Configure Notifications** section because now we have a new setting, the policy tree selector. You can see that we have this **alerting-demo-alertmanager** selected. All our imported rules are going to have this setting, so all of them are going to follow the logic in this policy tree.

Let's take a look at the policies view. This policies view is not a policy tree view; it's a list of policy trees. The first one is the original one, the Grafana default policy, the one that all the existing Grafana rules are following for routing. The second one is the new policy tree, the one that was created during the import with the imported policies. The good thing about this multi-policy tree feature is that this is not only for import; now any team can come here, click this button, and create their independent policy tree without breaking someone else's routing.

Now that we see that everything has been imported, because we can see here at the contact points page some contact points imported, I would like to know how these imported alert rules are behaving. What do you think, Alex? 

- Let's take a look. We have a new page in Grafana called **Alert Activity**. During the scaling part, I mentioned that when your organization gets bigger, you have more alert rules, and it gets harder to understand what's happening. That's where alert activity helps you. 

You see here alert rules that fired in the last 15 minutes. It's a list of alert rules, and to the right, you see the chart, which shows the alert volume over time. Here, you can spot patterns, for example, when a few alerts started firing at the same time, or if there are spikes, you will see it here. Of course, you can filter by state or any label if you need to regroup them. For example, if I want to see alerting team alerts, I can filter by team name and just see my team's alerts.

But let's also take a look at one of the alerts, like the **ServiceHealth** alert. You see that it's flapping all the time. We can click on **Instance Details**, and it opens the detailed view of this specific alert instance. At the top, that's the query, the actual query that Grafana runs to evaluate the alert rule. Below that is the history. 

What's interesting about the history timeline is that it combines both state transitions, like the alert going from alerting to normal, and also notifications. You can see that it sent a result notification to the Grafana on-call contact point, and it was successfully delivered. The same thing happened with the firing notification a few minutes earlier. If Grafana failed to send...

Notification: you would also see an error here. You can silence the alert or declare an incident if you'd like. 

But what if you want to see all notifications that Grafana sent? If you click on the contact point itself, there's a new button called **History**, which opens the notification history of this specific contact point. You can see all alerts that Grafana sent. If you remove the filter, you'll see all notifications that Grafana sent across all the alerting. You can filter by status or by outcome, and you can also expand any of these to see what exactly was sent.

If you're firing alerts, and as I mentioned, if Grafana failed to send a notification, you will also see an error here, so you don't need to guess whether it was delivered or not and why. This new page lives next to the state history that shows the same state transitions over time, even if it didn't send a notification. 

In our system, there are lots of alerts, so we can even analyze them with the system if you like. What it is doing right now is getting all the same alerts that we have on this page in the last hour and collecting information about them because it knows more about our system. You can also see we have some prompts here that ask it to analyze patterns, spot any issues, and provide insights. 

So let's see what it says. It's using all the data that you actually see on the page. It might take a few seconds, but here we are. You can see that we already have some alerts that require immediate attention. It suggested taking a look at a few of them in the same namespace, and there are even some patterns. It analyzes everything that alerting has and even suggests what our investigation priority should be, so you can make a decision on what to do next.

That's the workflow that we built in Grafana 13, so you can import your existing alerting, understand what's happening in the system, see whether notifications went out or not, and if needed, task the assistant to help you understand what to do next. 

And that's the end of our demo. Can we go back to the slides, please? 

We hope that after seeing everything today, you are convinced to switch to Grafana Alerting. Whether it's the import tool, the multi-policy tree, or the new triage features, we've been working hard to make Grafana Alerting the only alerting system you will ever need. 

Thank you. 

*(Attendees clapping)*

## Raw YouTube Transcript

- One.
- Hi. - Welcome to our talk. We are here to show you
why Grafana Alerting is ready to be your single alerting engine and how easy is to get started. I'm Sonia Aguilar, and I'm one of the software
engineers here at Grafana Labs. - And I'm Alexander, I'm also a software
engineer at Grafana Labs. And when Mat asked you how many of you have been
woken up by alerting, I'm glad that I was backstage
and I didn't see that. So here's what we have for you today. We're going to start with a quick recap of how Grafana Alerting
got to where it's now, what challenges we had to
solve to make it better, how to bring your existing alerts into Grafana from another system, understand what's happening with them, whether notifications went out or not, and we also have some live demos. - Let's just start with a quick recap. When Grafana started, everything was about
dashboards and visualizations. Alerting? Alerting was living in external
systems like Prometheus. Then with Grafana 4, we created our first alerting engine. It was basic, one-dimensional,
and focus on Graphite. Over time, Prometheus, Mimir,
and Loki became popular, and we built the unified alerting, where you could manage alert
rules from different systems in a single place. And we also added the ability to create multi-dimensional alerts. But over time, we realized that having
two types of alerts, Grafana-managed alerts,
data source-managed alerts, was adding complexity and
sometimes confusion for users. And this is what was happening
internally in Grafana. We were using Prometheus, Mimir, Loki, each with their own alerting system, a bit of everything. But at the same time, teams like security were
adopting Grafana Alerting. And more users were asking us,
"Which system should I use?" And the problem was
that having two options was adding more confusion than clarity. And this confusion told us we needed to make a decision, and we did it. We decided to double
down on Grafana Alerting. And the result is an alerting system that has the best of these systems. Grafana Alerting is
now a mature, scalable, and fully featured alerting engine, it has everything you could
expect from Prometheus and more. And we can call it
alerting in the big tent because you can query from
almost any data source you need and you can notify through most of the integrations you need. And we can call it the big tent because we have over 50
different data sources and 22 types of
integrations, and counting. But to get here, first, we have to solve some big challenges, and Alexander will show you how. - One of the challenges
we had to solve is scaling because Grafana Alerting runs everywhere, from small teams with just a few rules to large organizations
with thousands of alerts. And as Sonia mentioned,
we use it internally too, so we've seen what
happens when things grow. And there are really two sides to it. First, your system gets bigger, you have more alert rules and increased load on your
database and data sources. But also your organization gets bigger. You have more teams. Each team needs their own space. And it also gets harder to understand what's happening across hundreds of rules and notification policies. So let's start with the system side. Imagine you have one Grafana instance. It runs your alerting, queries data sources like Mimir, Tempo, and Loki, and others, and writes alert state to the database. It's simple and easy to manage, but if it goes down, your
alerting goes down with it. So, what do you do? Well, you panic, of course, but then you add a second Grafana. Now you have two instances running in high availability mode. If one fails, the other keeps evaluating. So you've got redundancy. But it also means that both of them evaluate all alert rules independently. So your data source cluster and your database are getting hit twice for the exact same rules, and it all compounds. If you start five Grafanas, you'll get five times the load. And Grafana needs to save alert
state after each evaluation, so that's often where
we feel the pain first. There are a few things
that Grafana can do already to reduce the database pressure. For example, compressed state, when instead of saving
every single alert instance to the database independently, it can compress the
state of the whole rule and save it to the database at once, reducing the number of
queries it needs to make. And the evaluation jitter, without which Grafana runs all alert rules on the same interval at once, and that creates a thundering herd that slams your database and data sources. So instead, it can calculate
a deterministic offset and spread rule evaluations
evenly across the interval. And the third thing it
can do is periodic saves. I mentioned that Grafana saves
a load state to the database after each evaluation, but it can also buffer the state in memory and flash to the database periodically, let's say, every five minutes. Of course, there is a trade-off. If Grafana crashes during
those five minutes, you lose unsaved transitions and they recover on next evaluation. So all these options, they
help the database pressure, but they don't fix the fundamental issue, that every replica is
still doing all the work. And that's what they fixed in Grafana 13. Now you can have one
replica evaluate alert rules while the others stand by. Your data source and
database loads stay the same no matter how many replicas you run. And it uses the same cluster membership that Grafana alert manager already has. So it decides which
replica is the primary, and if it goes down, another
one takes over automatically. During this failover process, there is a brief gap in rule evaluations. So before enabling this new mode, you need to pick what matters to you more, zero-gap redundancy or constant load on your database and data sources. But if you already use high
availability in production, you can enable this new mode with just one single config flag. It's available in Grafana
13, as I mentioned, and it's open source. But I also said in the beginning that scaling isn't just about load, it's also about handling more teams as your organization grows. And for that, we've had
role-based access control for a while now. Teams can own rules in folders with fine-grained control over who can change their alerting, and contact points have
access control too. But one piece was missing,
notification policies. The routing tree that decides
where notifications go when something fires or resolves. Up until now, but when everyone
shares a single policy tree, it's a problem because,
at scale, it becomes this, like a gen tree, which
is a nightmare to manage when different teams
change the same config, and there's always a risk of breaking someone else's
routing by accident. And I really like this image. It was generated by AI, but I think it represents a complicated notification
policy tree really well, because you see there
are different shapes, different colors, nobody really knows why, but it looks important, and
they can't really delete it. So we fixed that as well. And now you can have multiple
notification policy trees when each team gets their
own routing, small config, and they can change it however they want. So changes to one tree
don't affect anyone else. You can't break someone
else's alerting by accident. And that's how Grafana now scales with both your infrastructure
and your teams. But what if you want to
move your existing alerting from another system like Mimir, Loki, or some other system to Grafana? What do you do? - Yeah, exactly. Let's talk about how we get
started into Grafana Alerting, because there are two ways to get started. One is creating all rules from scratch. And for this, you can use the UI or you can use provisioning,
file provisioning, API provisioning, or Terraform. Or if you are already
running your alerting system in Prometheus, Mimir, or Loki, and you want to onboard
into Grafana Alerting, we have built an import tool that lets you bring your alerting system directly into Grafana. If you prefer creating
all rules from scratch using the UI, in GrafanaCON last year, we already showed you how
we made it easier than ever because we simplified the way you define the query and condition, and we also simplified the way you define how an alert rule is going to be routed with the simplified routing that is being able to
select the contact point in the alert rule form. But let's talk about the new import tool. Because we have built a
Prometheus compatibility layer directly into Grafana, this means that now you
can import your alert rules and your alert manager
configuration into Grafana Alerting. With this import tool, you don't need to copy-paste anything. You don't need to rewrite expressions. Your alerts will work in Grafana. But how does this work? Do you remember the
multi-policy tree feature that Alexander showed us? This is where this
feature becomes crucial, because when we are importing from Prometheus, Mimir, and Loki, we are creating a new
policy tree in Grafana with the imported policies, and we assign this policy tree to each imported alert rule. And your existing policies
in Grafana stay untouched. There are two ways to import. One is using the API and
the other is using the UI. Let's talk about the API. Because maybe you have everything in CI/CD or maybe you have lots of
data sources to import, in this case, your best
option is using the API. This API is fully compatible
with mimirtool and cortextool. This means that you can continue using the same workflows, same commands. You only need to target
to the new import endpoint and your alerting system will be automatically imported into Grafana. But maybe you prefer a guided experience and you don't have lots
of data sources to import. In this case, we have built
a new wizard in the UI, and it's a good option for you. Let's go to the demo. Let's switch to the demo. Okay. So, we are here in the alert list view. And here in this menu,
we have a new menu item, Import to Grafana Alerting. Let's click on it. This is the new import wizard. As you can see on the left is
a basic three-step process, and the order in this
wizard is intentional, because, first, we need to
import notification resources. The first thing we have to do
is to decide import source. Where is this alert manager stored? You can use YAML file
or use a data source. In my case, I want to
import the other manager that lives in a data source,
in particular, this one. Let's select this one. Then you need to decide the name for the new policy tree that is going to be created in Grafana with imported policies. The UI is automatically
using the same name as the data source we decided here. You can edit, of course, but I'm going to go ahead with this name. And the UI is also doing some validation, is checking if there is
any conflict, for example, let's imagine if we want
to import a contact point with a name that already
exists in Grafana. In this case, we do some deduplication and we rename this imported resources. Let's go to the next step. This step is about importing alert rules, and the first thing we have to decide is which policy tree we want to use for these I imported rules. The UI is automatically
selecting the policy tree name that we decided in the previous step. You can select another one, but I'm going to go ahead with this one. Then you have to decide the import source. Where are these alert rules stored? You can use a YAML file or a data source. In my case, I want to
import all the alert rules that live in this data source, so I'm going to select this one. You can also filter by
namespace and group, but in my case, I want to import all the alert rules that
live in this data source, so I'm not going to use any filter here. Then you need to select the
target folder in Grafana. This will be the folder
where all the imported rules are going to be created. I'm going to select this one. And then in here, you can see two checks that are enabled by default. This is very important because it means that
all the imported rules, once they are imported,
are going to stay paused. This means that they
are not going to start being evaluated yet. This gives you some time to review that everything
looks correct in Grafana, and once you see that
everything is correct is the moment you can unpause them. Let's go to the last step. And last step is about reviewing that everything that you
want to import is correct. You can review notification resources. In this case, the alert
manager that we want to import. And you can review also in this case the 10 rules that we are going to import. All right. So, we are ready. Let's click the button, start importing, and confirm. And we are done. The UI has redirected us
to the alert list view, with this filter, namespace, by the target folder that we
decided during the import. So we can see here all the imported rules that now all of them are
Grafana managed rules, and all of them are paused. Now let's imagine that
everything looks fine. We can come here to the folder level, and we have this new feature,
these three bulk actions. The interesting one for
us is the second one, Resume all rules. That means that all the
rules that are in this folder are going to be unpaused. But let's take a look to
one of these imported rules. We can see the query, expressions. But interesting part here is in the Configure notifications section, because now we have a new setting, the policy tree selector. And you can see that we have this
alerting-demo-alertmanager selected. All our imported rules are
going to have this setting. So all of them are going
to follow the logic in this policy tree. Let's take a look to the policies view. Because now this policies view
is not a policy tree view, it's a list of policy trees. And the first one is the original one, the Grafana default policy, the one that all the
existing Grafana rules are following for the routing. And the second one is the new policy tree, the one that was created during the import with the imported policies. And the good thing of this
multi-policy tree feature is that this is not only for import, now any team can come
here, click this button, and create their independent policy tree without breaking someone else's routing. And now that we see that
everything has been imported, because we can see here
at the contact points page some contact points imported, I would like to know how these imported alert
rules are behaving. What do you think, Alex? - Let's take a look. So we have a new page in
Grafana called Alert activity. And during the scaling part, I talked that when your
organization gets bigger, you have more alert rules and it gets harder to
understand what's happening, and that's where alert activity helps you. So you see here alert rules that fired in the last 15 minutes. It's the list of alert rules, and to the right you see the chart, that's the alert volume over time. So here you can see that you
can spot patterns, for example, when a few alerts started
firing at the same time, or if there are spikes,
you will see it here. Of course, you can filter
by state or any label if you need to regroup them. For example, if I want to
see alerting team alerts, I can filter by team name, and just see my team's alerts. But let's also take a
look at one of the alerts, like ServiceHealth alert. You see that it's flapping all the time. So we can click on Instance details and it opens the detailed view of this specific alert instance. At the top, that's the query, the actual query that Grafana runs to evaluate the alert rule. And below that is history. And what's interesting
about the history timeline is that it combines in itself
both state transitions, like alert went from alerting to normal, and also notifications. So you can see that it
sent a result notification to Grafana on-call contact point, and it was successfully delivered. Same thing with firing
notification a few minutes earlier. And if Grafana failed
to send notification, you would also see an error here. You can silence the alert or declare an incident if you'd like. But what if you want to see all notifications that Grafana sent? So if you click on the
contact point itself, there's a new button called History, and it opens the notification history of this specific contact point. So you can see all
alert that Grafana sent. And if we remove the filter, then you'll see all
notifications that Grafana sent across all the alerting. You can filter by status or by outcome. And you can also expand any of this to see what exactly was sent. If you're firing alerts. And as I mentioned, if Grafana failed to send a notification, you also see a error here, so you don't need to guess was
it delivered or not and why. This new page lives next
to the state history that shows same state
transitions over time, even if it didn't send a notification. And in our system, there
are lots of alerts, so we can even analyze them
with the system if you like. And what it actually is doing right now is getting all the same alerts that we have on this
page in the last hour. And it collects information about them because it knows more about our system. And you can see also we
have some prompt here that asks it to analyze patterns, spot any issues and insights. So let's see what it says us. And it's using all the data that you actually see on the page. So, it might take a few
seconds, but here we are. So you can see that we
already have some alerts that require immediate attention. So it suggested to take
a look at a few of them, in the same namespace, and there are some even patterns. So it analyzes everything
that alerting has. And even suggests us what our investigation priority should be so you can make a decision
on what to do next. And that's the workflow
that we built in Grafana 13 so that you can import
your existing alerting, you can understand what's
happening in the system, see whether notifications went out or not, and if needed task assistant to help you to understand what to do next. And that's the end of our demo. Can we go back to the slides please? - We hope that after
seeing everything today, you are convinced to
switch to Grafana Alerting. Either is the import tool,
the multi-policy tree, or the new triage features, we've been working hard
to make Grafana Alerting the only alerting system
you will ever need. Thank you. - Thank you. (attendees clapping)

