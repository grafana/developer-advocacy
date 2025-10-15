# Grafana 12 in Action: Git Sync, Observability as Code, Dynamic Dasbboards, New APIs, SCIM, and More

Published on 2025-06-08T04:51:19Z

## Description

Explore the biggest updates in Grafana 12, from Git-backed dashboards and observability as code to dynamic layouts, SQL ...

URL: https://www.youtube.com/watch?v=PcduxPJgeyI

## Summary

In this session from GrafanaCON, Mihaela Maior, Director of Engineering, and Mitch Seaman, Director of Product Management, introduced the latest features and improvements in Grafana 12. They discussed the evolution of Grafana, highlighting the new "Observability as Code" capabilities, which include a version API for dashboards and enhanced Git Sync functionalities. The presentation featured live demonstrations from various team members, including Dominik and Ryan, who showcased the new dashboard schema and tools like Grafana CTL and Foundation SDK. The session also addressed the migration to a new app platform architecture, which aims to standardize APIs and improve performance. Key highlights included dynamic dashboards with conditional rendering and tabs, SQL expressions for data manipulation, Grafana managed alerts, and SCIM integration for user management. The improvements are designed to enhance user experience and facilitate better observability across systems.

# GrafanaCON Session Transcript

**Good morning, everyone.** Wow, this room is more packed than I was expecting! That's great. I hope you're all caffeinated and ready for this; we've got a long session for you.

Now, before we dive in, let's introduce ourselves. I’m Mihaela Maior, Director of Engineering and one of the co-chairs for GrafanaCON. I lead what we call the Grafana front-end team, responsible for the core Grafana experience. If you've ever used Grafana to visualize your data or built a dashboard to share it with your team, then you've experienced our work. Let's be honest; you all have, that's why you're here at GrafanaCON.

When I first started using Grafana in 2016, I could not have imagined how far it would go, how much it would evolve and change, or that I would get yet another opportunity to join you here on stage to talk about the latest major release. It’s been an awesome journey, and we have an incredible team as well. I’m very excited to share it with you today, along with some awesome Grafan-istas, such as Mitch.

**Mitch:** I thought she was going to say "present company excluded." I'm Mitch Seaman, the Director of Product Management for Grafana. If you've used Grafana's front-end, you've interacted with Mihaela's team’s work. And if you've ever submitted a feature request and had it declined, then you've seen what my team can do. But in all seriousness, I've had a lot of great conversations already this week with many of the people here in the audience, and I get a ton of inspiration from the community at events just like GrafanaCON. It's very exciting to be here.

This session is going to be really packed, and the deep dive means we’re going to demo and go into the details of a lot of Grafana 12. The people who built these features will be presenting many of them, so please take a photo of this QR code and ask questions throughout. We will have a Q&A at the end.

Today, we’re excited to explore the next step in the evolution of observability. It’s bold, it’s powerful, and it redefines what's possible to do with Grafana. This is Grafana 12. We'll use the next 90 minutes to dive deeper into some of the most important developments of this past year.

This year, we're taking a major step forward with **observability as code**, and I know many of you are excited because we've spoken about this around the hallway track as well. We’re introducing a version API for dashboards, a new schema for dashboards, and powerful new clients like Git Sync to make managing dashboards as code easier and more reliable than ever. Ryan and Dominik will walk you through how it all comes together.

All of this is made possible by something fundamental—the app platform. This is something we introduced to you last year. It’s a complete revamp of our architecture, storage, and APIs, and it's evolving really fast. Stephanie and JP will join us on stage to talk through how it’s evolved recently and where it's going next.

So, we’re talking about foundational stuff: the app platform, new APIs, new schemas, and Scenes, which we announced last year. This matters a great deal to us, and we’re really excited that this year we get to watch some flowers bloom out of the soil of those foundational features. Afterward, Bogdan and Thanos will join us to talk about dynamic dashboards.

Of course, this is Grafana, and our mission has always been clear. We’re here to help you keep your systems healthy with the most powerful observability experience in the world. Mitch and I are excited to show you how we’re taking that even further with G12, including lots of live demos.

Before we dive in, I want to highlight these release stage labels on this slide. This is another good one to take a picture of when you’re figuring out what to test out when you go home. We’re going to lean a little bit over our skis here and talk about things that we’re actively working on because we really want your feedback as members of the community and people who are comfortable working with Grafana.

So just to keep things straight: 
- An **experimental feature** is under active development, and we recommend testing it out in development.
- A **preview feature** is ready for you to try out in pre-production, and we really want your feedback—it’s the most valuable part of that stage.
- **GA (Generally Available) features** are fully supported and ready for use in production.

With all that said, let’s get into it. I’m very excited to introduce you to Ryan and Dominik to talk about redemption—I mean, Observability as Code.

**Ryan:** Hey everyone, I’m Dominik, a software engineer at Grafana. I work on dashboards.

**Ryan:** Hi, I'm Ryan. Not sure if you are more nervous than I am, but we’ll see how this goes today. Let’s try demo time again. Can we switch over to my laptop? 

Looks like we’re almost there. So, we’re going to pick up where we were yesterday, and I’m going to show you how I would like to work with my dashboards synchronized in Git. 

We have this heat map dashboard; I'm going to edit it and change the size and maybe some colors. Let’s change the reds to spectral. Oops, yes! See, you can tell it's real. 

Let’s save that. We’re going to push to a new branch and click that off. What that actually did is Grafana went and wrote that value into a Git repository; it didn’t save it locally. So now we can open a pull request based on that where my value is changed. 

I will open a pull request. So, that's been committed into Git, and we’re listening for those changes locally. A webhook takes place and will render an image showing the before and after of what will happen if I merge that. So we can go ahead and merge it. 

Let’s go ahead and merge that guy. Now, when I return to my heat map, we see that this has been updated locally. That was great; that part worked yesterday. 

Now, I’m going to go straight back into Git. So I’ve got, let’s say, this heat map, and I'm going to edit it directly in Git. Most likely, you’re not actually going to use the GitHub editor to do this, but there are many options. 

You can edit the heat map from GitHub, and I will commit this change. So this is writing first to Git directly. If we look in our history, that’s there, and go back to my local host, heat map edited from GitHub.

What I’ve shown here is essentially two workflows. The initial one is here. I can’t help myself with unnecessary data sources to walk through a diagram, but what I’ve shown you is as a user writing through the UI into the API. The next thing that happens is that is then written first to Git and then into our database. 

Only after both requests are successful do we return a successful response to the user through the UI. Alternatively, we have a write path that your program people can directly write into Git and get a response from our API, where we then synchronize it into the database. 

The read path is always from our database, so you do not need to be connected to Git for that to work. It’s purely the illusion of bidirectional synchronization, but the read is always from our database, and write always goes to Git first. 

This strategy is great for me, but honestly, there are many workflows. Your CI/CD pipelines may not work with this. Dominik’s going to show us a new CLI tool that will help us work with that more.

**Dominik:** Yep, thanks, Ryan. I think we need to sync one more repository first, right? To get those slides up and running. So let’s see if this works because my slides are a dashboard, actually. 

Let’s configure the Git Sync first. This time, I’m going to use my repository. So he is adding a new location. Oops, why is our… 

**Ryan:** We lost the screen. Can we keep the screen on the computer? They’re having technical issues. These are not my technical issues today; I promise you.

**Dominik:** What we are doing now is syncing another GitHub repository to another folder, basically. Hopefully, that’s going to come up. We’ll keep this on demo time so you know what's happening here. 

Alright, looks like something's happening. So the piece we’re showing is what we did yesterday—an instance that was entirely managed by Git. Every dashboard that you’re dealing with was written into Git and then coming back. 

But there's an alternative form because I want to pull in dashboards that Dominik just wrote. I want a folder managed from my dashboards and another folder from a different upstream repository. 

Here we go. For this, Dominik’s configuring a second upstream remote that we’re going to pull in his dashboards. Let’s choose additional settings—yes, yes, yes. What could possibly go wrong? 

Now we’ve got two remotes. So within this, let’s open the one about the deployment. Which one? The deployment modes, right? 

**Dominik:** Yeah, there we go. 

What we just showed here is essentially multiple teams with different upstream repositories. That’s one model. But through this, we could clearly imagine we have a dev environment where you're writing into Git, then staging, and eventually production. 

Alternatively, you may have something where you have a central location with multiple satellite offices that all pull their dashboards and configuration. Again, the nice part of this is that you don’t always have to be online for it to work. It pulls it online when you need to and when it’s been approved through various processes.

**Ryan:** Perfect. Let’s get back to the tooling then. I’m going to talk about three tools that we’re… actually, two tools and a new dashboard schema. 

Let’s switch back to another dashboard that was just synced from Git, and I should be here. It should be here. 

So we’re going to talk about three things: the Grafana CTL, Foundation SDK, and the new dashboard schema. Let’s start with Grafana CTL. It’s a command line tool we developed to simplify interactions with Grafana and Grafana APIs. 

You can authenticate your users with Grafana CTL, manage multiple Grafana instances with it, and resources, obviously. It works from the terminal, so it’s fairly easy to integrate with your existing workflows, or you may have some automation like GitHub actions that you would like to integrate Grafana CTL with. 

For instance, with Grafana CTL, you can pull all of your resources to the local file system to do a backup, or you may want to pull just the dashboards, do some bulk edits of those dashboards, and deploy them back without touching the Grafana UI. 

You can also edit the resources using Grafana CTL. 

**Dominik:** Okay, I’m going to use it and let’s keep our fingers crossed that everything goes well. Grafana CTL, resources edit, and I’m going to provide it with the UID of the dashboard that I’m editing. So, in this case, it’s dashboard-schema. That’s correct. 

So what's happening now? The resource has been fetched, the editor opened, and I can start editing it. Okay, there is the problem. Let’s fix it and save it. 

**Dominik:** It’s edited, so let’s see what happened. Way better. Thank you. So this is the name of the tool that you should remember, not the one with the typo. 

But the interesting thing here is that this is the dashboard that we just synced from Git. Right? I can see the change on my local machine, but I can also see that change on Git. 

Let’s see if that’s true. Yeah, just now there’s this commit that I’ve made and the typo. But importantly, whether you're using Git or not, the same command line tools work. 

**Ryan:** Precisely. So apart from editing, you may also want to provision your resources from the terminal, right? I have a simple dashboard prepared for this demo. So I’m going to try to provision it and let’s see what happens. 

This time I’m going to use Grafana CTL, resources push, and I’m going to provide it with a path to my file. But oops, this didn’t work, right? 

**Dominik:** But no panic; this is actually expected. The dashboard that I’m trying to provision is invalid. So, why would I want to provision an invalid dashboard? 

So Grafana CTL, by using the APIs under the hood, is actually preventing me from doing something irresponsible. Now I can fix that problem. 

I think it’s this weirdly named dashboard; I can add the title. So this schema is requiring that we have a title set. When he tried to push, it failed. 

**Ryan:** There’s a… oh, what’s wrong? 

**Dominik:** You’re missing it.

**Ryan:** Yeah, up there, it’s saved, and let’s try pushing it again. 

Awesome, it’s pushed, and let’s see if it’s really in my instance. Dashboards. Yay, it works. Awesome. 

So this is Grafana CTL, right? I showed you how you would manage static files, but that’s not always what you want. Many times you would like to generate your resources programmatically. 

Let’s say you have an API that returns information about your infrastructure. Based on that information, you may want to implement a code that would generate data source connections or dashboards programmatically. 

And for that, we have **Foundation SDK**. Foundation SDK is a set of libraries aimed at the programmatic creation of Grafana resources. It’s available in Golang, TypeScript, PHP, Python, and Java. 

So you can really choose the language you feel most comfortable with. The interesting thing about Foundation SDK is that it’s not human-written. It’s automatically generated based on the schemas that Grafana provides. 

I’ve prepared a simple example that you’re looking at right now. I’m a front-end engineer, so I use TypeScript mainly. 

**Dominik:** So I use the Foundation SDK TypeScript SDK, and I can again use Grafana CTL to work on this dashboard. Let’s see how this works. 

I’m going to navigate to my demo directory, and I’m going to this time use Grafana CTL resources serve command. Okay, and I’m going to provide it with my TypeScript script that generates those dashboards from the code that I’ve just showed you. 

So what happens now is a local preview server has started on port 8080, so I can go to that URL and start working on my dashboard with real preview, right? 

Oh, the connection to the server is lost. I wonder why. We’ll figure this out later. So this preview allows me to work on this dashboard. 

Let’s fix the no-data problem. It’s probably a typo again, I suppose. 

**Dominik:** Yeah, let’s fix that query. By the time I’m back to my browser, this preview has been refreshed, and I don’t have to do anything. 

Grafana CTL watches my Foundation SDK program, basically, and refreshes whenever I make a change to my… 

**Ryan:** So importantly, you’re working on a piece of code that generates a dashboard. You don’t really want to push it every time. This is letting you see those changes more interactively. 

**Dominik:** Exactly. And this all happens locally, right? But the connection that you have, the data is actually the connection that is on the target instance that you want to deploy to. 

So let’s assume that I’m happy with this dashboard. I can now run my program pretty much. In my case, it’s going to be ARN DEV generate manifests. 

It generates the static files, and those static files are something that I can now push with the command that I’ve showed you earlier, which is push. 

I think it’s going to be this one. Awesome, and if we go to my local Grafana, I should have a new folder now. 

Oh, wrong link. This one. Yeah, Foundation SDK dashboards. And as you can see, this is now deployed. 

So this is Grafana CTL and Foundation SDK, and this is quite a powerful set of tools to work on your Observability as Code. 

But the elephant in the room here, as we keep saying schemas, and I’m sure you’re all wondering, wait, what are they talking about? And I’ve never seen a great schema from Grafana. 

We know that; we’ve worked with them too, so we struggle with them. It’s this challenge of writing dashboards whatever 12 years ago and then kind of adding more and more properties. 

They change over time, and we want to do new things. It started off as kind of an internal implementation but has become a really solid public contract that we all struggle with. 

So when looking at how to support this, we need to do a pretty major schema-first approach. 

**Ryan:** With the app platform and versioned APIs, we’re taking the opportunity to establish a new pattern. Can you show us?

**Dominik:** Absolutely, yeah. With G12, we are introducing V2 dashboards API, and what comes along is the new schema for dashboards. Internally, we call it dashboards V2. 

I’m going to walk you through four major changes that we’re introducing with this schema. 

1. **The Pattern:** It’s about how we express the building blocks of a dashboard. Each building block, name it a panel, has its own kind now and very precise spec. With this, we are not only organizing the schema better, but it also impacts the diffs produced by changes you make to your dashboards quite significantly. This is now even more important with Git Sync in the picture.

2. **Decoupling Complexity:** It has allowed us to decouple a lot of complexity that has grown organically into the existing dashboard schema. 

3. **Changes to Panels:** For those of you who have seen version one of the dashboard JSON, you have a panels property, which is an array of panels that mixed concerns of layout, queries, and visualization options. We are separating those concerns right now. We’re introducing two new properties: one is called **elements**, and the second one is **layout**. 

   - **Elements:** It’s still a collection of the panels that you use, but there’s no layout information. All layout information about the visual hierarchy of your dashboard is expressed through the kinds that live under the layout property.

4. **Queries:** The fourth thing is related to queries. Queries are expressed through the data query kind. There is a group and version property—group is the type of the query, a type of the data source you want to use. 

With this model, we are preparing Grafana for the future, but we also have some immediate benefits thanks to this change. In V2 dashboards, you don’t really need to provide explicit data source references for your queries. 

This has a significant impact because it makes dashboards way more portable. You can implement your dashboard once without thinking about the references and deploy it to different environments.

Let’s summarize those changes:
- Unified structure, better organization of the schema, more user-friendly, easier to reason about.
- Untangled complexity that has grown into the existing schema over the years.
- Introduced new layout property to express the visual hierarchy of the dashboard.
- More portable dashboards with data source references.

Now, let’s revisit the resources we imported earlier. Here’s one that we imported; this is just dashboard legacy, the candlestick panel, and this is the dashboard JSON you’ve seen for years. 

No top-level properties, just a dashboard. This will still work; you won’t have to change everything forever. But moving forward, we’re trying to add versioned APIs to everything. 

At the top of this, you’ll notice there’s an API version, dashboard's V1, there’s a spec element. That spec is identical to the dashboard JSON you’ve already worked with, with a schema around it. 

Moving forward, we have V2. Again, the real difference here is identified as part of the API version at the top. 

The spec in this case is driven by a much more robust schema-first approach, including all the features, all the new things we’re building. 

Legacy still works; the API you’ve already been writing against will continue to work, but we’re moving forward for a more versioned flavor of this.

Interestingly, all of these tools we’ve shown you, like the Git Sync and the CTL, work on this generic pattern of having a common metadata wrapper around everything. 

So in this case, we’ve provisioned a playlist through this model just based on it having these identifiers. You can see how this becomes a pretty dynamic system. 

The power of that is based on the app platform and we’re going to welcome Stephanie and JP.

**Stephanie:** Hello! I am Stephanie, and I’m an engineer on the app platform team. 

**Jean-Philippe:** Hi, I’m Jean-Philippe, and I’m an engineer on the unified storage team at Grafana. We’re going to walk you through what has been powering all of the awesome things that you saw from Dominik and Ryan.

As you know, the Big Tent philosophy has long been at the heart of Grafana, where you can bring your data no matter where it lives, all underneath the Big Tent. 

We’ve been working to make the Big Tent even more expandable and easier to build on by transforming Grafana into an observability app platform. This platform will make it so plugins can do a lot more with access to things like auth and storage, but will also make everything underneath the Big Tent much more consistent, resilient, and stable. 

In Grafana 12, we migrated some of our key resources—folders and dashboards—onto the app platform to power things like Git Sync and Grafana CTL. 

Let’s dig into what that means. So in Grafana 12, we introduced new APIs for both dashboards and folders. These APIs are standardized, which makes them more predictable and compatible for things like Git Sync and Grafana CTL. 

These API schemas are also added to API versions so you will know exactly when things are going to change in those APIs and when there are breaking changes from an API version bump.

But this is just the start. We’re going to continue to migrate more resources onto the app platform, and all of the APIs across the Grafana ecosystem will become standardized, schematized, and versioned. 

These versions are also tied to an API lifecycle. In this API lifecycle, all of our APIs will start out in alpha, where we’re still experimenting with things and that may be a bit unstable, but then they’ll go into beta, where they’ll be a lot more tested, though there may still be some minor changes going forward. 

Eventually, they’ll go into stable, where we’ll guarantee backwards compatibility, and any breaking change will be met with an API version bump. 

So you can start building on those APIs knowing that they aren’t going to suddenly change from underneath you. 

So, we talked about how dashboards and folders have been migrated onto the app platform in Grafana 12, but what does that really mean for you? 

The old API will still be working; you can still be using those. But we also launched the V1beta1 for both folders and dashboards. 

Like Ryan said, for V1 for dashboards, it’s still the same JSON that’s going to be stored in the spec. There is a bit of validation, but it is not schema-first. 

So for V2, we introduced that for dashboards, and that’s where you can see what Dominik showed, with more schema validation and just a more consistent, deterministic, and predictable dashboard spec. 

Here’s what the APIs look like. All of the APIs going forward will have the same structure. It will start out with /APIs, followed by the group, the version, the namespace, and then the resource. 

This is a core resource in Grafana that you want to interact with, whether that's dashboards or folders. As you can see, the CRUD endpoints will be much more consistent and deterministic, and we’re going to continue to migrate more resources onto this /APIs pattern so you can have these schematized, standardized, and versioned APIs.

But looking even further into the future, you will also be able to extend Grafana with these types of APIs and have the same as code support as Grafana CTL and Git Sync. 

Additionally, you’ll be able to watch for events throughout the ecosystem and see when things are changing. Your apps built on this will have access to everything that core Grafana has access to, like auth and storage. 

**Jean-Philippe:** Now, the app SDK is in early development, but the storage layer is already powering Git Sync, so let’s hear from JP about that.

**Jean-Philippe:** Unified Storage is basically the new layer that we built to power those new APIs Stephanie just showed and will become the default as we work hard to make it the default in the future. 

Why did we build this new storage layer? Why not just use what we already have? Everyone running Grafana has a database that we already store data into. 

Over the years, the database of Grafana grew; we got a lot of tables, and it became hard to maintain. Also, all the data in those tables is unversioned, so we don’t really have a schema for the data where we can migrate from one version to another. 

Grafana is something special; instances usually have around 50 megabytes of data in MySQL or SQL in general, and that makes it not a really good fit long-term for what we strategize. 

We’ve thought about how to move forward with an easier way to store things, especially how we can store what we now call Grafana apps inside of the Grafana storage. 

So we came up with Unified Storage. It’s like a new layer, and all of Grafana will eventually use it, and all your apps can eventually use it. You’ll never need to create a new table in your schema or bring your own storage.

Another cool thing about Unified Storage is that it makes Grafana more reactive. It allows your app to watch resources. For example, with the dashboard app, we can watch the folders app, and as soon as a folder gets created, Unified Storage will tell the dashboard app that the new folder was created. 

It allows you to have all the states you need in your app coming from Grafana. 

Now, let’s talk a bit about how we get there. What changes have we already made? A high overview of what we did is basically to go from having all those tables to a more key-value approach. 

Now we have one table that stores the current state of Grafana, called the resource table, which has the live snapshot of your Grafana state. We also have a second table called resource history, which has a history of all the resources that you save in resource. 

This already works with the infrastructure you have, so you won’t need to set up something new like a new database or update your database or set up a messaging queue. 

It also works for all kinds of setups; whether you run it on a Raspberry Pi or a big deployment, we’ve got you covered. 

What does this new storage architecture enable? What are the features we can build on top of this that perhaps weren’t possible before? 

Here are three big things we're really excited about:
1. **Git Sync:** As shown by Ryan and Dominik, you can synchronize any Git repository with your Grafana instance. This is powered by Unified Storage.
2. **Unified Search Experience:** Eventually, you will be able to search for anything in Grafana, even things coming from third-party apps.
3. **Global Trash:** You will have a global view of all the trash elements, and with the resource history table, you will be able to restore every resource from the last 20 versions.

**Stephanie:** So let’s recap what we’ve seen so far. We’ve seen really cool as code tooling with Git Sync, Grafana CTL, Foundation SDK, and all of that powered by the app platform. 

With the app platform, you're going to get standardized, schematized, and versioned APIs. Dominik showed you a bit about what that brings for dashboards specifically in V2, all of that backed by the storage layer, which has a lot of cool functionality we will be able to build on for apps. 

The reason this matters is because of the really powerful and cool dashboards you can create. In Grafana 12, that has become even better. 

Let’s welcome Bogdan and Thanos to the stage to see how that has improved.

**Bogdan:** Hello, everyone. I am Bogdan; you probably saw me yesterday on stage talking about Doomfana. I’m here with Thanos, the Destroyer of Worlds, and today we’re going to talk about dynamic dashboards.

**Thanos:** Thank you, Bogdan. Grafana dashboards have certainly evolved over time, but honestly, some features didn’t get as much love as they needed. 

Take rows, for example. We introduced them way back in version two or three, and they pretty much stayed the same ever since. Why? Partly because we have to keep things working across versions, and partly because the old rendering engine made it tough to improve them meaningfully. 

That’s why last year we introduced Grafana Scenes—dashboard scenes. We migrated the dashboards into that new architecture, and this year we have made two big improvements: a new dashboard schema and fresh new APIs on top of the app platform that Stephanie and Jean-Philippe took us through. 

These form the base of the iceberg—unseen, but they support everything we’re going to talk about today. 

Let’s take a pause. Why are we doing those changes? Grafana dashboards can get big, pulling data from many different data sources, serving different types of users, and covering complex and diverse systems. 

Template variables and collapsible rows help, but they often still have empty panels that can be confusing. Layouts don’t adapt well to different screen sizes, and navigation can be slow with too much scrolling.

So what we did here is introduce **tabs**. Now, dashboards support tabs in addition to rows. Tabs are powerful and necessary for a well-structured dashboard. 

But it’s not just that; we now support different and nested layouts between tabs and rows, providing you the freedom to structure your dashboards like never before in Grafana. 

The next thing is **conditional logic**. This is a very powerful feature. It lets you set conditions for panels, rows, or tabs to show or hide them based on a variable value or when there’s no data. 

The last one is **auto layout**. What makes conditional rendering and tabs possible is the powerful auto-grid layout. It lets you set things like column width or row height, adjusting the layout automatically based on screen size and other conditions.

**Bogdan:** Let’s switch to the demo! 

I'm going to look a little bit over some dashboards that I currently have in my local Grafana instance. There’s a folder called Integration Linux Node, created automatically whenever you use the Linux node integration. 

If we expand this folder, we see that there are a lot of dashboards. Even though this worked fine until now, navigation between these dashboards is a little cumbersome.

For example, if I want to see advanced memory information, I need to navigate back to my dashboard list and so on. Let’s see how we can leverage dynamic dashboards to minimize the interactions or reduce the number of steps users take when doing an investigation.

I’m going to navigate to this Linux node dashboard. This dashboard combines all seven dashboards into only one. That’s right, seven dashboards in only one. 

I can just scroll, and it’s the same fleet management overview dashboard we had previously. The panels are aligned the same, but there’s one small difference: whenever I select an instance, another tab appears.

This is achieved by combining the features of tabs and conditional rendering. 

**Bogdan:** Allow me to enter edit mode. The first thing you will notice is the side pane. We added this side pane to allow quicker editing of various UI elements. 

If I select my instance tab and look at the show/hide rules, this is where we added conditional rendering. We can show or hide a tab depending on set rules. 

For example, if the selected instance equals O, that means there’s no specific instance selected, and the tab will not be visible. If I click to add a rule, I can set conditions like the time range. 

We can switch between matching all or any rules. 

We also didn’t talk about rows. Rows were added in Grafana version two or three, and we didn’t do many changes to them since then. We are introducing a new type of rows that are not tied to what we used to call the custom grid. 

Now, each row can be either a custom grid or auto grid, and it can contain other rows or tabs. 

If I exit the edit mode, it seems like there’s only one grid, but there are actually two grids. 

**Thanos:** The auto grid allows us to focus on writing queries and not on aligning panels. I mentioned seven dashboards in one, which means a lot of panels. 

How can I navigate through my dashboard while editing to find my panels quickly? We added the **outline feature**, which allows us to navigate to dashboard elements super fast. 

Now, we’ve covered a lot of new features: auto grid, custom grid, tabs, rows, outline, edit pane, and much more to come. 

With this, I’m going to pass it back to Mihaela and Mitch.

**Mihaela:** Now, I know we spent a lot of time in this session, but this is not it. Raise your hand if you think you’re going to use dynamic dashboards after this. 

I see quite a few hands! That’s awesome. We hope you’re just as excited about what we will talk about next. 

Mitch and I are back to close off Grafana 12 with some of our favorite features and even going hands-on to show you how it all works. 

**Mitch:** I’ll play the role of a Grafana user. I love my two dogs, but I’m also an engineer at heart. This is a high-tech operation. I have automated my stock management, supplier connections, and packaging. 

I’m using Grafana to monitor my system. 

What you see here is the main dashboard I use to look at the most critical parts of my business. One of my supplier systems is flaky, and it always goes down. 

Thanks to the new Atlassian status page data source, I can keep an eye on it straight in my dashboard. 

Next, let’s talk about data visualizations and actions. Last year, I showed you a demo where I turned a server on and off. This year, we introduced supercharged actions. 

In this panel at the top is a list of my automated pickers. They’re awesome but can get stuck. Some of them are off, so let’s try turning one off and on again. 

**Mihaela:** That worked. Now, let’s see how we do this. 

**Mitch:** In my overrides, I’ve set up actions. It makes a PUT request to the defined endpoint with the picker ID. Now, these actions are safe to use in production and are fully supported. 

I can order more stock, move stock around, and really do a lot from my dashboard without switching to other systems.

Now, talking about stock, I did a stock take this month. I have these funky manual scanners that dump messy raw data. I used six transformations to clean it up. 

Could I use Grafana 12 to make it easier? Let’s add a new visualization. I’m going to use a query that I’ve saved previously. 

Now you can see the data. I have various bits missing. Let’s use SQL expressions to clean it up. 

I’m going to add an expression and remove the limit. Running it creates another frame of data. I can hide the first query if I don’t want to see it.

Let’s just get our product data so I can show you how we can tidy it up. 

**Mitch:** I expect most of us have played with SQL at some point in our careers. So, why not use this well-known language? 

I’ll use this pre-prepared query. Thanks to AI, I didn’t write this from scratch; someone can generate the query for me. 

So, this query cleans up products without names and accounts that are empty. 

**Mihaela:** This is a basic example of what SQL expressions can do. They are available in private preview now, and we’re working to get them out to general availability.

We invite you to try them in your dev environments and give us feedback. 

Now every year at GrafanaCON, we talk about new things, but it’s also about making things better. 

Yesterday, David spoke about performance improvements, and I get to show you another one. The Geomap panel has a performance improvement. 

With WebGL, loading a million styled markers is fast—so fast you can barely see it loading. 

**Mitch:** Super Pets is working great! I can keep an eye on my suppliers, order more stock, and monitor my pickers. 

Thanks to Grafana, I have a working observability platform at all times. 

**Mihaela:** The challenges we face as usage of Grafana grows within organizations can feel overwhelming. 

We want to help you tidy things up with some improvements. First, we’re excited about **Observability as Code** like Ryan and Dominik discussed. 

The first thing I would do is set up Git Sync for version control of dashboards. Next, let’s talk about alerting. 

We’re migrating from data source-managed alerting rules to Grafana-managed alerting rules. 

Grafana-managed alerts work with any data source, support fine-grained access control, and offer a simpler authoring experience. 

Let’s switch to demo mode. 

**Mitch:** Here’s my alert rules screen in Grafana 12. Grafana-managed alerts are organized into folders for better organization. 

When I click to view one of these alerts, I can see its status history, version history, and compare or restore versions as needed. 

When I edit these alert rules, I get quality of life improvements. I can preview these rules and iterate on the query. 

In Grafana-managed alerts, I can assign notifications easily without complex routing policies. 

Another thing I’m excited about is Grafana-managed recording rules that work with any data source. 

These recording rules allow queries that take a while to run to store a time series in Prometheus. 

Grafana-managed recording rules are a super set of data source-managed recording and alert rules. We recommend everyone use them right away; they’re generally available. 

To migrate existing Prometheus alert rules, we built an import tool to move them over easily. 

Now, let’s talk about managing data source plugins. 

**Mihaela:** Many new data sources were introduced. But managing plugins can be complicated. 

In Grafana 12, we’ve improved the way we test plugins against different versions of Grafana. 

In the connections page, I can install a plugin directly from within the Grafana UI and see which plugins need updates. 

I can even filter just for plugins that need an update, check version history, upgrade, or downgrade directly within the UI. 

This plugins page is now the Grand Central Station for managing plugins—it’s a much smoother experience. 

**Mitch:** I want to introduce the Grafana Advisor, which helps admins see any issues in their instances. 

We started with data source plugin issues but are expanding it out to other issues like auth or dashboard problems. 

The advisor shows issues with data sources failing their health checks or missing the relevant plugins. 

**Mihaela:** Lastly, let’s talk about SCIM, which allows you to push users and groups from your identity provider straight into Grafana. 

This makes it handy for onboarding new people and ensuring they have the right permissions. 

**Mitch:** So just a really handy feature and a quality of life improvement for onboarding new teams. 

**Mihaela:** Great! Now, we’re very excited. You might recognize this slide from last year, where we presented another incremental step. 

In Grafana 12, we’ve officially removed AngularJS code from our codebase. 

This is a great security upgrade and a significant step in a long process. 

**Mitch:** So, that was a lot! 

We covered Git Sync, Foundation SDK, Grafana CTL, dynamic dashboards, and landmark improvements this release, including new data sources, SQL expressions, Grafana-managed alerts, and SCIM. 

All this comes together in a release designed to help you onboard teams smoothly into a powerful observability platform that you can customize to your heart's content. Thank you all for joining us today!

## Raw YouTube Transcript

Good morning, everyone. Wow, this room is more 
packed than I was expecting, that's great. I hope you're all caffeinated and ready for this, we've 
got a long session for you. Now, before we dive in, let's introduce ourselves. So I'm Mihaela 
Maior, I'm a Director of Engineering and one of the co-chairs for GrafanaCON. I lead what we call 
the Grafana front-end team, and we're responsible for the core Grafana experience. So if you ever 
use Grafana to visualize your data or even built a dashboard to share it with your team, then you've 
experienced our work. And let's be honest, you all have, that's why you're here at GrafanaCON.
Now, when I first started using Grafana in 2016, I could not have imagined how far it would go, 
how much it would evolve and change or that I'd get yet another opportunity to join you here on 
stage to talk about the latest major release. It's been an awesome journey and we have 
an incredible team as well. So I'm very excited to get to share it with you today with 
some awesome Grafan-istas, such as Mitch. I thought she was going to say present 
company excluded. I'm Mitch Seaman, I'm the director of product management for 
Grafana. So if you've used Grafana's front-end, you've interacted with stuff that Mihaela's 
team works on, and if you've ever submitted a feature request and had it declined, 
then you've seen what my team can do. But in all seriousness, I've actually had a lot of 
really great conversations already this week with a lot of the people here in 
the audience, and I get a ton of inspiration from the community at events just 
like GrafanaCON. It's very exciting to be here. And this is going to be a really packed 
session, though the deep dive means we're actually going to sort of demo and go into the 
details of a lot of Grafana 12. The people who built these features are presenting a 
lot of them, so please take a photo of this QR code and ask questions throughout, 
we're going to have a Q&A at the end. Today, we're excited to explore the next step 
in the evolution of observability. It's bold, it's powerful, and it redefines what's possible to 
do with Grafana. This is Grafana 12. We'll use the next 90 minutes to dive deeper into some of the 
most important developments of this past year. This year, we're taking a major step forward with 
observability as code, and I know loads of you're excited because we've spoken about this around the 
hallway track as well. We're introducing a version API for dashboards, a new schema for dashboards, 
powerful new clients such as Git Sync to make managing dashboards as code easier and more 
reliable than ever. Ryan and Dominik will walk you through how it all comes together. And all of 
this is made possible by something fundamental, that's the app platform. This is something that 
we introduced to you last year. It's a complete revamp of our architecture, storage and APIs, and 
it's evolving really fast. So, Stephanie and JP will join us on stage to talk through how it's 
evolved recently and where it's going next. So yeah, you're hearing us talk about a ton of 
foundational stuff, the app platform, new APIs, new schemas, and Scenes, which we announced last 
year, which is our new front-end framework for dashboards. This obviously matters a great 
deal to us, but we're really excited that this year we get to sort of watch some flowers 
bloom out of the soil of those foundational features. So Bogdan and Thanos are going to join 
us afterwards to talk about dynamic dashboards. And of course, this is Grafana, as our mission 
has always been clear. We're here to help you keep your systems healthy with the most powerful 
observability experience in the world. So, Mitch and I are excited to show you how 
we're taking that even further with G 12. And lots of live demos. Before we dive in, 
I just want to highlight these release stage labels on this slide. This is another good one 
to take a picture of when you're figuring out what to test out when you go home. So we're 
going to lean a little bit over our skis here and talk about things that we're actively 
working on. That's because we really want your feedback as members of the community and 
people who are comfortable working with Grafana. So just to keep things straight, an experimental 
feature is one that's under active development, and we recommend testing it out in dev. A preview 
feature is ready for you to try out in pre-prod, and we really want your feedback, that's the most 
valuable part of that stage. And GA or generally available features are fully supported, 
and they're ready for use in production. So now with all that said, let's get into it. 
I'm very excited to introduce you to Ryan and Dominik to talk about redemption, 
I mean, Observability as Code. Hey, everyone, I'm Dominik. I'm a software 
engineer at Grafana. I work on dashboards. Hi, I'm Ryan. I'm not sure if you are more nervous 
than I am, but we'll see how this goes today. Let us try demo time again. Can we switch over to 
my laptop? And we'll... oh, that's not it. Almost there.
It is there. This part's not even me, I swear. Oh, there we go, great. So we're going 
to pick up where we were yesterday and I'm going to show you essentially how I would like to 
work with my dashboards synchronized in Git. So we have this heat map dashboard, I am going to 
edit it and let's change the size and maybe some colors. So we'll edit, I'll change, let's say reds 
we'll change to spectral. Oops, yes. See, you can tell it's real. Save. We're going to push to a new 
branch and click that off. So what that actually did is Grafana went and wrote that value into a 
Git repository. It didn't save it locally. So now we can open a pull request based on that where my 
value is changed and I will open a pull request. So that's been committed into, or been 
written into Git as a pull request, and we're listening for those changes locally. 
And a web hook takes place and will render an image showing the before and after of what will 
happen if I merge that. So we can go ahead and merge it. Let's go ahead and merge that guy. 
And now when I return to my heat map, which we'll just do local host, heat map, we see that 
this has been updated locally. That was great. That part worked yesterday. So, we'll show you 
another variation here where I am going to go straight back into Git, and from Git so I've got, 
let's say this heat map, and I'm going to edit it directly in Git. Most likely you're not actually 
going to use the GitHub editor to do this, but there's many options. You can do heat map 
edited from GitHub, and I will commit this change. So this is writing first to Git directly. 
And if we look in our history that's there, and go back to local host, heat map edited from 
GitHub. So what I've shown here is essentially two workflows. The initial one is here. I can't 
help myself with unnecessary data sources to walk through a diagram, but so what I've shown you is 
as a user writing through the UI into the API, and the next thing that happens is that... 
oops, is that is then written first to Git and then into our database. And only after 
both requests are successful do we return a successful response to the user through the UI.
Alternatively, we have a right path that your program people can directly write into 
Git, and get a response into our API, where we then synchronize it into the database. 
The read path is always from our database, so you do not need to be connected to Git for that 
to work. It's purely the illusion of bidirectional synchronization, but the read is always from our 
database, and write always goes to Git first. So this strategy is great for me, but honestly, 
there's many workflows. Your CICD pipelines may not, this may not be sufficient for that to 
work. So Dominik's going to show us a new CLI tool that will help us work with that more.
Yep. Thanks, Ryan. I think we need to sync one more repository first, right? To get those slides 
up and running. So let's see if this works, because my slides are a dashboard actually. So 
let's configure the Git Sync first. This time, I'm going to use my repository.
So he is adding a new location. Oops, why is our-
We lost the screen. Can we keep the screen on the computer? 
They're having technical issues. These are not my technical issues 
today, I'm just going to promise you. So what we are doing now is actually we're syncing 
another GitHub repository to another folder, basically. Hopefully that's going to come up.
See, we'll keep this on demo time so you know what's happening here.
All right. Looks like something's happening.
So the piece we're showing is what we did yesterday was an instance that was entirely 
managed by Git. So every dashboard that you're dealing with was written into Git and then 
coming back. But there's an alternative form, because I want to pull in dashboards that Dominik 
just wrote. And I want a folder that's managed from my dashboards and another folder that's 
managed from a different upstream repository. Here we go.
So for this, Dominik's configuring a second upstream remote that we're going to pull in 
his dashboards. Let's choose additional settings, just yes, yes, yes. What could possibly go wrong? 
And now we've got two remotes. So within this, let's open the one about the deployment.
Which one? The deployment modes, right? Yeah.
Okay, there we go. There we go. So what we just showed here is 
essentially multiple teams with different upstream repositories. So that's one model. But through 
this, we could clearly imagine we have a dev environment where you're writing into Git and then 
staging and eventually production. Alternatively, you may have something where you have a central 
location with multiple satellite offices that all pull their dashboards and configuration. 
Again, the nice part of this is that you don't always have to be online for that to work. It 
pulls it online when you need to and when it's been approved through the various processes.
Perfect. Let's get back to the tooling then. Perfect.
Yeah, I'm going to talk about three tools that we're... Actually, two tools and a new 
dashboard schema. So let's switch back to another dashboard that was just synced from Git, and I 
should be here. It should be here. There we go. So we're going to talk about three 
things, the Grafana CTL, Foundation SDK, and the new dashboard schema, and let's start with 
Grafana CTL. It's a common line tool that we have developed to simplify interactions with Grafana 
and Grafana APIs. You can authenticate your users with Grafana CTL, you can manage multiple Grafana 
instances with it, and resources, obviously. It works from the terminal so it's fairly easy to 
integrate it with your existing workflows, or you may have some automation like GitHub actions that 
you would like to integrate Grafana CTL with. So with Grafana CTL, you can, for instance, 
I don't know, pull all of your resources to the local file system to do a backup, or you 
may want to pull, let's say dashboards only, do some bulk edits of those dashboards, and deploy 
them back without touching Grafana UI. So you can also edit the resources using Grafana CTL, and 
yeah, this typo is bugging me because it's not Graffana. It is Grafana CTL, not Graffana CTL. 
Let's try and fix it with Grafana CTL. Okay, I'm going to use it and let's keep our fingers 
crossed that everything goes well. Grafana CTL, resources edit, and I'm going to provide 
it with the UID of the dashboard that I'm editing. So in this case, it's, let's see, 
dashboard-schema, that's correct. So what happens now? The resource has been fetched, 
editor opened, and I can start editing it. Okay, there is the problem. Let's fix it 
and save it. It's edited, so let's see what happened. Way better. Thank you. So this is 
the name of the tool that you should remember, not the one with the typo. But the interesting 
thing here is that this is the dashboard that we just synced from Git. Right? I can see the 
change on my local machine, but I also can see that change on Git. And let's see if that's true. 
I'm pretty sure it is. Yeah, just now there's this commit that I've made and the typo.
Yeah, but importantly, whether you're using Git or not, the same command line tools work. So 
the ecosystem is all working together here. Precisely. So apart from editing, you may also 
want to provision your resources from terminal, right? So I have a simple dashboard prepared 
for this demo. So I'm going to try to provision it and let's see what happens. This time 
I'm going to use, I made that typo now. I'm sorry, Grafana CTL, again resources, but this 
time resources. Push, and I'm going to provide it with a path to my file, and I think it's going 
to be this file. But oops, this didn't work, right? But no panic, this is actually expected. 
The dashboard that I'm trying to provision is invalid. So, why would I want to provision an 
invalid dashboard? So Grafana CTL, by using the APIs under the hood, is actually preventing me 
from doing something, let's say irresponsible. So now I can fix that problem. I think it's this 
weirdly named dashboard, I can add the title. So this schema is requiring that we have a title 
set. And so when he tried to push it failed. Okay, there's a, oh, what's wrong? Oh-
You're missing it. Yeah. Up there, it's saved and let's try pushing 
it again. Awesome, it's pushed and let's see if it's really in my instance. Dashboards. Yay, it 
works. Awesome. So this is Grafana CTL, right? I showed you an example how you would manage static 
files, but that's not always what you want. Many times you would like to generate your resources 
programmatically. Let's say you have an API that returns an information about your infrastructure. 
And based on that information, you may want to implement a code that would generate data source 
connections or dashboards programmatically. And for that, we have Foundation SDK.
Foundation SDK is a set of libraries that are basically aimed at programmatic creation 
of Grafana resources. It's available in Golang, TypeScript, PHP, Python, and Java. So you can 
really choose the language that you feel most comfortable with. And the interesting 
thing about Foundation SDK is that it's not human written. It's automatically 
generated based on the schema, schemas that Grafana provides. I've prepared a simple example 
that you're looking at right now over here, I'm a front-end engineer, so I use TypeScript 
mainly. So I use the Foundation SDK TypeScript SDK, and I can again use Grafana CTL to work 
on this dashboard. So let's see how this works. I'm going to navigate to my demo directory, 
and I'm going to at this time, use Grafana CTL resources serve command. Okay, and I'm 
going to provide it with my TypeScript script that generates those dashboards from 
the code that I've just showed you. So what happens now, a local preview server has 
started on port 8080, so I can go to that URL, I can start working on my dashboard with 
real preview, right? So oh, connection to the server is lost. I wonder why. We're going to 
figure this out later. So this preview, I can now work on this dashboard. So let's fix the no data 
problem. It's probably a typo again, I suppose. Yeah, let's fix that query. And by the time 
I'm back to my browser, this preview has been refreshed and I haven't to do anything. Grafana 
CTL watches my Foundation SDK program, basically, and refreshes whenever I make a change to my-
So importantly, you're working on a piece of code that generates dashboard. You don't really want 
to push it every time. So this is letting you see those changes more interactively. So minor 
changes, you can more quickly see the feedback. Exactly. And this all happens locally, 
right? But the connection that you have, the data is actually the connection that is on 
the target instance that you want to deploy to. So let's assume that I'm happy with this dashboard, 
I can now run my program pretty much. In my case, it's going to be ARN DEV generate manifests. It 
generates the static files, and those static files is something that I can now push with the comment 
that I've showed you earlier, which is push. And I think it's going to be this one. Awesome, and 
if we go to my local Grafana, I should have a new folder now. Oh, wrong link. This one. Yeah, 
Foundation SDK dashboards. And as you can see, this is now deployed. So this is Grafana CTL and 
Foundation SDK, and this is quite a powerful set of tools to work on your Observability as Code.
But the elephant in the room here, as we keep saying schemas, and I'm sure you're all 
wondering, wait, what are they talking about? And I've never seen a great schema from 
Grafana. We know that, we've worked with them too, so we struggle with them, but it's this challenge 
of we wrote dashboards, whatever 12 years ago, and then kind of have organically added more and more 
properties. They change over time, we want to do new things. It started off as kind of an internal 
implementation, but has become a really solid public contract that we all struggle with. So 
when looking at how to support this, it's pretty clear we need to do a pretty major schema-first 
approach. So with the app platform with versioned APIs, we're taking the opportunity to establish 
kind of a new pattern. Can you show us? Absolutely, yeah. So with G 12, we 
are introducing V2 dashboards API, and what comes along is the new schema for 
dashboards. Internally, we call it dashboards V2. And I am going to walk you through four major 
changes that we're introducing with this schema. So the first one is the pattern. It's about, 
how do we express the building blocks of, sorry, of a dashboard. So each building block, name it, a 
panel, has its own kind now and very precise spec. Right? With this, we are not only organizing the 
schema better, but it also impacts the diffs that are produced by the changes that you make to your 
dashboards quite significantly, and this is now even more important with the Git Sync in the 
picture. Right? It also allowed us to decouple a lot of complexity that was grown organically 
into the existing dashboard schema. And to give you an example, I'm going to talk about the 
changes that we are making to the panels. For those of you who have seen the version one of 
the dashboard JSON, you have a panels property, which is pretty much an array of panels and 
panels, mixed concerns of layout, of queries, of visualization options. We are separating those 
concerns right now. So we are introducing two new properties. One is called elements, and the 
second one is layout. Elements, it's still a collection of the panels that you use, but there 
is no layout information. All of this information about the visual hierarchy of your dashboard is 
expressed through the kinds that live under the layout property. This is quite an interesting 
change, and we're going to hear about it very soon from Thanos and Bogdan, because it allowed 
us to introduce new layout types, for instance, and some other fancy features like conditional 
rendering. But that's going to happen soon, Thanos and Bogdan are going to talk about that.
Before this, let's see the changes that we are introducing to the panels. Panel is now expressed 
through our kind. The spec is again, quite precise, very precise actually. We have top-level 
properties that are common to every single panel. Name it, transparency, configuration, description, 
title, etc. Then we have visualization configuration, which is this Viz Config property, 
and it has a kind that is a type of the plug-in that you want to use. So the specification of 
the Viz Config comes from the specifications of visualization plug-ins. It's going to be different 
for bar chart, it's going to be different for time series and text panel, etc. And then there 
is the third thing that we are changing here, it's the data property. Queries, query options, 
and transformations, they all live together under a single kind that is called query group.
And I wanted to focus on the fourth thing that is related to queries here, because with this is 
the model we are preparing Grafana for the future, but we also have some immediate benefits thanks 
to this change. So, queries are expressed through the data query kind, and as you can see, 
there is a group and version properties. Group is the type of the query, a type of the 
data source that you want to use. Name it, Influx, name it Prometheus. Right? So with the group 
and version are preparing Grafana to support queries validation in the future. It's going to 
complement the dashboard schema validation that we're introducing with the V2. But the immediate 
change that we're bringing with the V2 schema is about the data source references. So in 
the V2 dashboards, you don't really need to provide explicit data source references for your 
queries. This has quite a significant impact because it makes dashboards way more portable. 
You can implement your dashboard once without thinking about the references and deploy it to, 
let's say dev, staging, whatever environment. It's let's say that's one of the deployment 
models that you, Ryan, showed, right? Forget this becomes really important. 
Obviously, if you have multiple data sources, exporting dashboards with the explicit reference 
and then trying to pull them in makes it pretty hard. So currently, this is just pulling, if you 
have one, Loki can say, give me the Loki data source. There's more coming in this direction, 
but aiming to make these more portable. Yeah. So when you deploy such a dashboard, 
you don't really have to care whether the references across different environments 
are the same or you don't have to care about updating those prior to deployment. So yeah, 
that's the immediate benefit of this change. All right, so let's summarize those changes. 
We have four of those that I discussed. One is the unified structure, better organization of the 
schema, more user-friendly, more easier to reason about. Then we have untangled the complexity that 
has grown into the existing schema over the years. We introduce new layout property to express visual 
hierarchy of the dashboard. And with that, we are bringing new layout types and new features to the 
dashboards. And last but not least, is the data source references and more portable dashboards.
Awesome. So this all sounds a little abstract when talking about generic schemas, but to be 
kind of concrete, let's go back to some of the resources we imported earlier. So here's one 
that we imported, this is just dashboard legacy, this is the candlestick panel, and this is 
the dashboard JSON you've seen for years. No top-level properties, it's just a dashboard. 
This will still work, you're not going to have to change everything forever, so don't worry too much 
about that. But moving forward, we're trying to add versioned APIs to everything. So at the top 
of this, you'll notice there's an API version, dashboard's V1, there's a spec element. That spec 
is actually identical to the dashboard JSON that you've already worked with. There's a schema 
around it. It's essentially reverse engineered on top of it, but fundamentally it's just move 
what was the dashboard JSON now under a spec and have a common metadata wrapper around it.
And then moving forward, we have V2. Again, the real difference here identified there, 
identified as part of the API version at the top. And the spec in this case is driven by a 
much more robust schema first approach, including all the features, all these tabs you've seen, 
all of the new things we're building. So legacy still works. The API that you've already writing 
against will continue to work, but we're moving forward for a more versioned flavor of this.
Interestingly, all of these tools we've shown you like the Git Sync, the CTL, they really work on 
this generic pattern of having a common metadata wrapper around everything. So in this case, 
we've provisioned a playlist through this model just based on it having these identifiers. So you 
can see how this becomes a pretty dynamic system. The power of that is based on the app platform and 
we're going to welcome Stephanie and JP. Come on up. Oh, can we switch back to slides?
Yeah. Yeah.
Nice. They're going to get to the 
slides, I swear. I swear. Fingers crossed.
All right. Sweet. Hello, I am Stephanie and I'm an 
engineer on the app platform team. Hi, and I'm Jean-Philippe, I'm an engineer 
on the unified storage team at Grafana. And we're going to be walking you through 
what has been powering all of the awesome things that you saw from Dominik and Ryan.
As you know, the Big Tent philosophy has long been at the heart of Grafana, where you can 
bring your data no matter where it lives, all underneath the Big Tent. And we've 
been working to make the Big Tent even more expandable and easier to build on by transforming 
Grafana into an observability app platform. This platform will make it so plugins can do a lot 
more with access to things like auth and storage, but will also make everything underneath the Big 
Tent much more consistent, resilient and stable. And in Grafana 12, we migrated some of 
our key resources, folders and dashboards, onto app platform to power things like Git Sync 
and Grafana CTL. Let's dig into what that means. So in Grafana 12, we introduced new APIs for 
both dashboards and folders. And these APIs are standardized. So this not only makes it 
more predictable, but also makes it compatible for things like Git Sync and Grafana CTL. These 
APIs are also schematized, so they have defined structure which helps with that validation 
that you saw from Dominic on Grafana CTL, and will just help in general with better 
tooling in a more consistent experience. Also, these API schemas are added to API versions, and 
so you will know exactly when things are going to change in those APIs and when there are breaking 
changes from an API version bump. But this is just the start. We're going to continue to migrate more 
and more resources onto app platform, and then all of the APIs across the Grafana ecosystem will 
become standardized, schematized, and versioned. And these versions are also tied to an API 
lifecycle. So in this API lifecycle, all of our APIs will start out in alpha, and this is where 
we're going to still be experimenting with things and that may be a bit unstable, but then they're 
going to go into beta. And in beta is where they're a lot more tested, but there may still 
be some minor changes going forward. And then they'll go into stable. And then stable is where 
we're going to guarantee backwards compatibility and any breaking change will be met with an 
API version bump. So you can start building on those APIs knowing that they aren't just 
going to suddenly change from underneath you. So we talked about how dashboards and folders have 
been migrated onto app platform in Grafana 12, but what does that really mean for you? So the 
old API will still be working, you can still be using those, but we also launched the V1beta1, 
and that is for both folders and dashboards. But like Ryan said, for V1 for dashboards, it's 
still the same JSON that's going to be stored in the spec. There is a bit of validation, but it is 
not schema first. So for V2, we introduced that for dashboards and that's where you can see 
what Dominik showed where there's a lot more schema validation and just more consistent and 
deterministic and predictable dashboard specs. So this is what the APIs look like. So all 
of the APIs going forward will have the same structure. It'll start out with /APIs and 
then it'll be followed by the group. And the group is just a related functionality so 
that can be dashboards, folders, alerting, then it'll be followed by the version, followed 
by the namespace. And the namespace will either be your org ID or a stack ID if you are in cloud, 
and then that will be followed by the resource. So that's a core resource in Grafana that you want 
to interact with, whether that's dashboards or folders. And as you can see looking between the 
two, they're the same CRUD endpoints as well, so the APIs are going to be much more consistent 
and deterministic. And we're going to continue to migrate more and more resources onto this /APIs 
pattern so that you can have these schematized and standardized and versioned APIs.
But looking even further into the future, you will also be able to extend Grafana with 
these types of APIs and then have the same as code support as Grafana CTL and with Git Sync. And then 
additionally, you'll be able to watch for events throughout the ecosystem and see when things are 
changing. Also, your apps that you build on this will have access to everything that core Grafana 
has access to, like auth and like storage. And JP is going to talk about storage in a bit. But the 
key thing here is that you're going to be able to build really powerful apps within Grafana that 
are going to feel like first class citizens like dashboards and folders inside of Grafana.
Now the app SDK is in early development, but the storage layer is already powering Git 
Sync, so let's hear from JP about that. Cool, thank you. So Unified Storage. 
So Unified Storage is basically the new layer that we build to kind of power those new 
APIs that Stephanie just showed, and will become the default and we are working really hard on 
that to make it the default in the future. So, why did we build this new storage layer? 
Why did we not use what we already have, right? Everybody of use running Grafana, there's 
a database that we already store data into. So over the years, the database of Grafana grew, we 
got a lot of tables as you can see, and it became really hard to maintain. Also, all the data in 
those tables are unversioned, so we don't really have a schema for the data where we can say we can 
migrate from one version of the data to the other. And also, Grafana is something really special. The 
Grafana instance usually have around 50 megabytes of data in my SQL or in SQL in general, and 
that makes it kind of a bit of not a really good fit long-term, what we strategize for.
So we have thought about, how can we do this and how can we move forward with having an easier way 
to approach how we store things? And especially also, how can we store, for example, what we 
now call Grafana apps inside of the Grafana storage? So right now, if you write a Grafana 
app, you would have to bring your own storage, but we want to kind of have a unified 
storage experience for all the apps that you build on top of the Grafana platform.
So what we came up with is something that we call Unified Storage, it's like a new layer and all 
of Grafana will eventually use it and all your apps can eventually use it. And the good thing 
is, you will never need to kind of create a new table on your schema or bring your own storage. 
Another thing that's really cool about that is that Unified Storage makes Grafana more reactive. 
That means that with Unified Storage, your app can basically watch resources. For example, here 
in this example, we can, with the dashboard app, we can watch the folders app, and then as soon 
as a folder gets created, Unified Storage will basically tell the dashboard app that the new 
folder was created. And we can have basically the state of folders in the dashboard app, and that 
works for all the operations, not only for create, but also for update and delete, an example. So 
you can basically have all the states you need in your app coming from Grafana.
Now let's talk a bit about, how do we get there? So what do we need to 
change? What changes have we already made, and so forth and so on. So a high overview about 
what we did is basically you saw that we had all this tables on this one screenshot, and we 
basically went from having all those tables to more key values to our approach. So basically now 
we have one table that stores the current state of Grafana. So this table looks a bit like this as 
of today, it's still evolving, but that's like the first iteration. So we have a table that's called 
resource, and this resource table basically has the live snapshot of your Grafana state. And then 
we have a second table, which we call resource history. This one is pretty interesting because 
it will enable in long run a lot of things. So resource history basically has a history of 
all the resources that you save in resource. And this all already works with infrastructure 
that you have. So you will have no need to kind of set up something new like a new database or 
update your database or set up a messaging queue, and also works for all kinds of setups. So 
for example, if you run it on a Raspberry Pi or you run it on a big deployment, we got you 
covered there. It shouldn't be a big difference. So let's talk a bit about what does this 
new storage architecture enable? What are the features now that we can build on top of 
this that perhaps weren't possible before, right? That's just a short sneak peek, we've got 
more common, but these are the three big things we're really excited about. One is Git Sync. 
Basically what Ryan and Dominic showed you, where you can basically synchronize any Git 
repository with your Grafana instance. This completely built on top of Unified Storage, so 
Unified Storage is powering that. Another thing I'm personally really excited about is that we get 
eventually unified search experience, which means you will be able to search anything in Grafana, 
even things that are coming from third-party apps eventually, as we now control the full storage 
there. So that's what I'm really excited about. Another thing, the global trash. So you will 
have a global view of all the trash elements, and also with the resource history table, we 
would be able that you can restore every resource. The last 20 versions, that's the limit right now 
from an old state. So basically right now this exists for dashboards, but it's coming for all 
the resources that we are supporting in Grafana. So now, Stephanie will give us a recap.
Yeah, yeah. So we've covered a lot already with Dominik and Ryan and us, so let's recap what 
we've seen so far. So we've seen really cool as code tooling with Git Sync, with Grafana CTL, 
Foundation SDK, and all of that has been powered by app platform. With app platform, you're 
going to get these standardized, schematized and versioned APIs. And Dominik showed you a bit 
about what that brings for dashboards specifically in V2, all of that is going to be backed by the 
storage layer, and that storage layer has a lot of really cool functionality that we're going to be 
able to have, like global trash. And additionally, all of the storage is going to be able to have a 
lot of other things that we can build on for apps so that you can store your data for apps as well.
And the reason that all of this matters is because of the really powerful and cool dashboards that 
you can create. And in Grafana 12, that has become even better. So let's welcome Bogdan and Thanos 
to the stage to see how that has improved. Thank you. Okay, so hello, everyone. I am 
Bogdan, you probably saw me yesterday on stage talking about Doomfana, and today I came 
here on stage again to showcase everybody that Doomfana is not the only cool project I'm working 
on. I'm here with Thanos, the Destroyer of Worlds, and today we're going to talk about 
dynamic dashboards. Thanos? Thank you Bogdan. I'm Thanos, and instead of 
holding my Thanos gauntlet snapping out features, I was given this remote control, I felt 
inevitable, but let's get to the point. Grafana dashboards have certainly 
evolved over time, but honestly, some of the features, they didn't get as much 
love as they needed. Take rows for example, we have introduced them way back in version 
two or three and they pretty much stayed the same ever since. Why? Partly because we have to 
keep things working, working across versions, and partly because the old rendering engine made 
it tough to improve them meaningfully. That's why last year we introduced Grafana scenes, dashboard 
scenes. So we migrated the dashboards into that new architecture, and this year we have made 
these big two improvements. A new dashboard schema that Dominik and Ryan presented, and the 
fresh new APIs on top of the app platform that Stephanie and Jean-Philippe took us through. 
These form the base of the iceberg, unseen, but they support everything that we're 
going to talk with Bogdan today. But let's take a pause, why we're doing 
those changes. Grafana dashboards can get big, pulling data from many different data 
sources, serving different types of users, and covering complex and diverse systems. Template 
variables and collapsible rows help, yes, but they often still have empty panels that 
can be confusing. Layouts often don't adapt well to different screen sizes, and navigation 
can be slow with too much scrolling or... It's too much scrolling and yeah, that's it, really.
So what we actually did here, we want to introduce tabs. Now dashboards support tabs in addition to 
rows, tabs are so powerful and necessary for a well-structured dashboard. But it's not just that. 
We aren't introducing just tabs, we now support different and nested layouts between tabs and rows 
that provide you the freedom to imagine ways of structuring your dashboards like never before 
in Grafana. Next thing is conditional logic. Simply this is a very powerful feature. It lets 
you set conditions to panels or rows or tabs in order to show or hide them based on a variable 
value or when simply there is no data. And the last one is the auto layout. What makes 
conditional rendering and tabs possible is the powerful auto grid layout. It lets you set 
things like column width or row height, and it adjusts the layout automatically based on screen 
size and other conditions. Enough with the words, let's get with Bogdan for the demo.
Okay, let's switch to the demo. Okay, it should be switched anytime now. 
All righty, this. Oh, okay, there we go. So in order to showcase the infinity stones that 
Thanos just presented, I'm going to look a little bit over some dashboards that I currently have in 
my local Grafana instance. We can see that there is a folder called Integration Linux Node. Well, 
this folder is created automatically whenever you use the Linux node integration. This is one of 
our most powerful, most used and more complex integration that we provide. And if we expand 
this folder, we can see that there are a lot, and I mean a lot of dashboards. I can count seven, 
I think. So even though this worked fine until now, the navigation between these dashboards is a 
little bit cumbersome. If we go to fleet overview, and this is the first dashboard that users should 
look over when they go to the Linux integration folders, sorry, dashboards, I can select an 
instance and then I'm going to be taken to another dashboard and I'm going to see an overview of that 
instance. And then I'm going to go navigate back. And for example, if I want to see advanced 
memory information, I need to navigate back to my dashboard list and so on and so forth. 
Well, we do present some, we do add some links to those dashboards and they help a little 
bit, but that's not enough. So, let's see how we can actually leverage dynamic dashboards to 
minimize the interactions or to reduce the number of steps that users have to take whenever 
they actually want to do an investigation. So I'm going to navigate to this Linux node 
dashboard that I have right here. And I want to tell you that this dashboard combines all 
seven dashboards into only one. That's right, seven dashboards in only one. So I'm loading these 
dashboards and I can just scroll, and it's the same fleet management overview dashboard that we 
had previously. The column, the panels are aligned the same, but there is only one small difference, 
and that is this little thing right here. Well, for now it's just standalone because the other 
tabs are not visible. And what I mean by that is, whenever I select an instance, there is another 
tab appearing. So, this is achieved by combining the features of tabs and conditional rendering.
You may wonder, how does conditional rendering work? What's that? Well, allow me to actually 
enter the edit mode. We switch the little edit button to switch here. So, this is the new edit 
mode, and the first thing that you will notice, it's the side pane. We added this side pane to 
allow quicker editing of various UI elements. So if I select my instance tab and I look here 
over the show hide rules, this is where we added the conditional rendering. We can see that we 
have the possibility of either showing a tab or hiding the tab depending on some rules. My 
current rule is if selected instance equals O, that means that don't have a specific instance 
selected, we have all the instances selected. That means the tab will not be visible, 
this, it was not visible in the beginning. If I click on add rule, I can say, for example, 
another condition time range less than. What this means is that, for example, if my selected 
time range right now you can see last 30 minutes, it's for example, less than seven days. Don't 
show the panel or show the panel depending on what we have here. Now, we can see that when I 
added a second rule there is this match rules section added right here. What this is, it 
allows you to switch between either matching all the rules at once or matching any rule. 
So this panel would be hidden if template variable and time range less than rules are 
actually respected, or if I select match any, it's going to check if either template variable 
or the time range conditions are matched. Okay, we talk about tabs, we talked about 
conditional rendering. We didn't talk about rows. So rows is one of those features that 
have been added in Grafana, version two, three, something like that, and we didn't do a lot 
of changes to them since then. Okay, they're repeatable, you can, but they do have some quirks 
and that is, for example, if you want to move a row or if you're on a rearrange a row, you need 
to actually first collapse it and then move it, or if you want to add the panel, that row has to 
be expanded. So, because we are using the previous schema and because we wanted to maintain 
the cross, the backwards compatibility, we never did a lot of changes to those.
But right now we are introducing a new type of rows, and these rows are a little bit different 
from the previous ones. Okay, they kind of act the same, they encapsulate panels, but these rows 
are not tied to what we used to call the custom grid. So the initial grid in Grafana was called 
custom grid. Now, each row can be either a custom grid, it can be a auto grid, it can contain other 
rows, it can contain other tabs, like we see here. So rows can be extremely well-used to actually 
combine multiple types of layouts and organize my panels better. So this can be seen here if 
we look over row one, row two. These rows have their headers hidden, if we hover, we can see 
that those rows have their header hidden and one row organizes the panels three on a row, and 
the second one are only two panels on a row. Well, if I exit the edit modes, I can see that this 
section right here seems like there is only one grid, but there are actually two grids.
And this is what I want to present to you next, grids. Thanos mentioned the auto grid, I mentioned 
it as well. What is the auto grid and how does it differ from the custom grid? Well, we all know, 
Grafana, you create a dashboard, you go there, and you just place your panels, you resize them. 
But that process sometimes can be extremely cumbersome. That is because, well, you want to 
focus on your queries, you aren't too focused on your data, you don't want to focus on aligning 
panels. You may want to actually set, okay, I want up to four panels on a row and I want them to be 
narrow, or I want them to be, I don't know, wide. And I want my dashboarding system to actually 
take care of the positioning of my panels. So this is exactly what auto grid is. If I 
select the overview here, we can see that right now we have maximum four columns per row. 
If I set this to three, then I'm going to have only three panels per row. But if I resize this, 
we can see that these get pretty small because I selected them to be narrow for standard, and for 
this screen size, they're going to be a little bit bigger. So auto grid allows us to actually 
just focus on writing queries, focus on the data, and I don't want to think and I'm not forced 
to think about how I want to place my panels. Well, one more thing, Thanos did nothing wrong, 
but he forgot to mention only one useful feature. I mentioned seven dashboards in one. That means 
a lot of panels. How can I navigate through my dashboard while I'm editing it to find my panel 
super fast? For that, I'm going to actually leverage the outline feature that we added, 
which allows us to actually go to my elements, my dashboard elements extremely fast. So for 
example, if I want to go over the CPU usage panel, I'm going to expand the instance tab here. I'm 
going to go over overview. I'm going to navigate to CPU, expand overview again, and I'm going 
to select the CPU usage here. Well, I can also rename it super fast. And mainly, these are the 
new things that we added to dynamic dashboards. Auto grid, custom grid, which is the previous 
Grafana grid, tabs, rows, outline, edit pane, and there are much, much more features to come. 
And with this, I'm going to pass it back to Thanos and I think we should switch back to slides.
Thank you, Bogdan. So seven dashboards into one using auto grid, conditional logic, and tabs. 
These are just some of the highlights and we do have some many more exciting features to expand 
that we're coming along. Dynamic dashboards are experimental, so test them just in dev. And with 
this, let me pass the mic to Mihaela and Mitch. Now, I know we spent a lot of time in 
this session, but this is not it. So, raise your hand if you think you're 
going to use dynamic dashboards after this.
You. Love it.
I was louder than I expected, sorry. That's awesome. We hope you're just as excited 
about the things we're going to talk about next as well. So Mitch and I are back to close off 
Grafana 12 with some of our favorite features, and even going hands -on to show 
you how it all works because all these live demos have gone so well, right?
Now for this next part, I'm going to play the role of a Grafana user. I've done that 
one before, to show you what we're doing to make it easier than ever to pull all your data 
together and keep your systems healthy, really. Great, and then I'll join in as the 
platform engineer and resident cat person who's responsible for the observability 
platform itself. And I'm going to be talking about what we're doing to make it easier for 
administrators and operators of Grafana to pull all of your teams together onto a complete 
and enterprise grade observability platform. And of course, we're trying to divide 
the crowd between cat lovers and dog lovers. It's clear what we love, right?
Yeah, you should all meet Jacob the cat. Now let's jump in and take a look at how Grafana 
12 brings more power and flexibility to our users in this one pane of glass. So yesterday in the 
keynote, David announced that we have 15 new data sources. Well, if you didn't know, that's more 
data sources than in the past few years combined. And these new data sources extend Grafana 
usefulness in more areas, like CICD and web platforms, connecting to your incident management 
support and analytics, connecting to other observability tools, and databases as well.
Now, instead of talking through more slides, how about we take a risk and we go into some 
live demos. So I introduce to you, Super Pets. If I ever had a side gig, it would be related to 
pets. I love my two dogs to bits and life would be really boring without them. But of course, 
I'm an engineer at heart, so this is a high-tech operation. I have automated my stock management, 
my supplier connections, I have automated pickers and packaging, all of that. And of course, 
I'm using Grafana to monitor my system. Now what you can see here is the main dashboard 
that I use to just have a look at the most critical parts of my business. This is the one 
that I use day to day. The first panel that you see here, I want to tell you a story. So one of 
my supplier systems is very flaky. It always goes down. And because I'm this techie, I've actually 
connected my system to theirs. So because of this integration, whenever their system goes down, 
it takes my down too. That's a big problem, so I need to keep an eye on it. So thanks to 
the new Atlassian status page data source, I can keep an eye on it straight in my 
dashboard. I know everything is working, right? So if we look at it here, thankfully it's 
working, so we can go through with this demo. Now next, I want us to talk about data 
visualizations and actions. So last year, I did a demo for you where I showed you in 
canvas panel, a server that I could use actions on to turn on and off. This year we introduced 
supercharged actions for you. So what you can see in this panel at the top is a list of my automated 
pickers. They're awesome. They make life even much easier for my business. However, they're quite 
flaky, like anything else. So I need to keep a constant eye on them and also sometimes they'll 
get stuck, they'll turn off, and I need to sort them out pretty quickly. And of course you can 
see here, some of them are off, so let's try and do the usual, turn it off and on again and see if 
that fixes it. Let's try and restart one of them. All right, that worked. I'm back in business. 
I, of course, have a few more to sort out. But you might wonder, okay, well how do we do 
this? So let's have a look. I'm going into go to my overrides. So you can see here that I've set 
up the two actions that you can see on screen as well. And the way it works is that it makes a 
put request to this endpoint that I've defined in my particular situation with the picker ID and 
whatever the relevant information to restart it. Now, I can take unauthenticated actions now from 
any data source. Now, not only have they expanded, they are now also generally available. What that 
means is that they are safe to use in production and they are fully supported. Now, the options 
are endless here, right? I can do more and more from my dashboard without having to switch to 
other systems to take the actions I need to take. I can just focus on this one view.
Not only that, but I can do other things, right? So I can order more stock, let's say. I 
can move stock around, there's really a lot that I can do using actions. Now talking about stock, 
this month I did a stock take. I wanted to see what inventory I have in my imaginary warehouse. I 
have these very funky manual scanners that I use. They're great when I'm doing it, however, they 
dump me the raw data and it ends up quite messy. So what I've done in this panel here is I've 
used six transformations to clean up the data, so I have various missing values and the like. 
So I had to layer some transformations to make it make sense. So that made me wonder, could I 
use Grafana 12 to make it easier than this, to go through the data and just get my stock totals? 
That's all I want, right? So let's give it a go. So if we add a new visualization, I'm going to 
get my data quickly. Now, I don't need this query because I'm going to take advantage of this new 
enterprise feature called the query library. So what I'm doing is I'm loading a query that I've 
saved previously and I know it has all my data. I love it. I'm glad you do too. Okay, so now you 
can see what I meant about the data, right?So I do have various bits of data missing. So this is 
one I want to sort out before I get to my totals. So let's use SQL expressions to do exactly that. 
So I'm going to add an expression, go to SQL, and you can see that it pre-populates a very 
simple query. What you can see here is that it uses the query names to refer to as the table 
in the particular query, and I'm going to remove this limit because I don't need it, and we're 
just going to run it. Now when you do that, it creates another frame of data, so if you 
don't want to see this, all you need to do is to hide the first query. There we are. So 
we're seeing the data that we could see before. Let's just imagine we wanted to just get our 
product data so I can quickly show you how we can tidy it up. So let's just get our product ID 
and our product name. I think that's right. There we go, now you can see what I meant. So I have, 
for example, product IDs that repeat themselves as I was scanning in the warehouse. So let's 
just pick up the distinct ones. And of course, you can see my spelling now as well, so I'm 
going to sort that out. There we go. All right, so now I have my distinct product IDs, but 
you can see I'm missing some product names here and there. This data has a lot of that, 
so I could just quickly remove those. Oop, I hope you can hear my furious typing. 
There we go, so now I have a list of the products that I've scanned and it's working.
Now, Grafana is really great at querying already. So, why not use this well-known language? Right? I 
expect most of us got to play with it at least one point in our careers to manipulate the data and 
get it to the shape that you want it to be. Now, to truly show you what this is capable of, I'm 
going to use this pre-prepared query. Now, don't be fooled. I did not write this from scratch. 
The benefit here is SQL is pretty well-known, there's a lot of information online about it. So 
you can use your favorite LLM to generate you the query. And of course, starting yesterday, 
that's Grafana Assistant, right? So that's exactly what I've done here. I did not write 
this from scratch. Thanks to AI, someone can just do it for me and then I make sure it works.
So this query doesn't do crazy amounts, but it does clean up the products that don't have a name. 
It cleans up the accounts that are empty, and it groups my information. If we just refresh this, 
there you go. So what I got you is exactly what I had before with my layered transformations.
Now you could sit and wonder, well, okay, so you're showing me basically the same results. 
So, why would I choose this approach in favor of the other? Well, one benefit is that with 
transformations, you many times end up layering transformation on top of transformation 
on top of transformation. That's doable, I've done it, but if anything changes, it's very 
hard to troubleshoot and evolve it. So with this, I can just use a few lines of SQL to make it do 
what I need it to do, and I can evolve it easily. Now, more importantly, SQL expressions are 
run in the backend. So that means they work for all backend data sources and they will 
work with alert rules and recording rules, which is something that didn't work before. So, 
let's have a go at that. See if I just go to this panel, to the menu, I can create a new alert 
rule. I want to save this dashboard quickly. There we go. We're creating a new alert rule. 
You can see that data has been pulled through, but the expression has as well. I can create 
a new alert rule with this manipulated data, and I can even manipulate it further and preview. 
In this case, apparently it would be firing, but of course I need to do something more clever 
to have an alert on my stock. There we go. So now, what I've showed you is a very basic 
example of what SQL Expressions can do. It has a lot of potential for complex processing. So 
whether you're trying to merge your analytics, similar to the example that we saw yesterday 
in the keynote, I'm merging data from multiple locations, or you're trying to clean up your 
data to answer the most critical questions in your business. This is what SQL expressions 
are for now. Now, they're available in private preview right now, and we're of course working on 
to get them out to general availability as well. What we're inviting you to do is to try them out 
in your dev environments and give us feedback. Now before I go back to my slides, you would've 
noticed by now that I have some funky coloring scheme in my Grafana. That's because my favorite 
theme is Tron, and I promise you, it's David that copied me for the keynote, not the other way 
around. Now we can go back to slides, please. Now, I love Harry Potter, but I don't know 
what the spell is to make this happen. So, there we go. Now every year at GrafanaCON, we come 
and we talk to you about new, new, new things, but it's also about better, better and better, 
right? And you saw an example of that in the keynote yesterday, where David spoke to you about 
two performance improvements. That was our blazing fast new table and the new select combo box. Now 
I get the pleasure of showing you yet another. So what you can see here is a performance 
improvement on our Geomap panel. I'm actually really excited I picked this one, because I've 
already seen the Geomap panel on a bunch of our speakers note slides yesterday, so I hope this 
benefits all of you. So what you can see here is before is us loading 10,000 styled markers and 
you can see it loading the data. Whereas now, thanks to WebGL with a million styled markers, you 
can barely see it loading. I mean, not only that, but you can't see the map for the data points, 
but. Now, Super Pets is working great. Thank you. Now, Super Pets is working great. I'm keeping an 
eye on my supplier systems. I can order more stock if I need to. I'm keeping an eye on my robot 
pickers. Everything is great. Not only that, but I get to dust off my SQL skills and manipulate 
my data so I can rationalize my stock, but this business isn't just built on my sweat and tears. 
Thanks to Mitch, our platform engineer, I have a working observability platform at all times.
I've been sweating and crying all day. So yeah, this business, like we mentioned, is built 
on the backs and Grafana is built on the backs of administrators who are working 
hard to keep their systems healthy. So, how do I make Mihaela's life easier, is the 
question and also save myself a little bit of toil in the process? The challenges basically, 
as I think many of you experienced today, maybe this morning, is as usage of Grafana grows 
within my org, I can actually start to feel like a bit of a victim of my own success. I have a lot 
more teams to support, I have more dashboards, a mix of different kinds of alerts running around in 
my instance, lots of users coming in and out. And what we'd like to do here in Grafana 12 is help 
you tidy things up a little bit with some Grafana 12 improvements. The first one. Now this topic 
has really been beaten to death, but it continues to be extremely important. As a platform engineer, 
of course, I'm excited about Observability as Code like Ryan and Dominic talked about before. The 
first thing that I would probably do is set up Git Sync so that Mihaela and her team can keep their 
dashboards backed up and version controlled. So next, let's talk about alerting. We mentioned 
that we're migrating from data source managed alerting rules to Grafana managed alerting 
rules. To understand a little bit more the difference between these two types. A lot of you 
use Prometheus, Mimir and Loki to evaluate your alerts in addition to storing your metrics logs 
and traces, and we've done that for years as well with alert Manager. However, what we've been 
doing and with patterns very consistent with Alert Manager is developing Grafana managed alerts 
to address some important gaps you've noticed. We're really excited that Grafana managed alerts 
are a super set of data source managed alerts. So first thing is, they work with 
any data source so you don't have to store your metrics in Prometheus or Loki 
in order to alert on them. The second is, they support fine-grained access control. For 
example, you can control who can see versus who can edit alerts, or even contact points. Then 
the alert authoring experience is also quite a lot simpler, as I'm going to show you in just a 
second, we have some additional contact points. So in this demo I'm going to walk through 
three things, starting with alerts like I just mentioned, and then moving on to how we're 
here to help you effortlessly manage plug-in versions for all the plug-ins you're running 
in Grafana, and then help you sync users and Teams straight to your Grafana instance 
using SCIM. Switch over to demo, please. And the screen I'm going to pop up is the alert 
rules screen in Grafana 12, which has some nice improvements. So on the top, I see my Grafana 
managed alerts as before and down below I can see my data source managed alerts. These ones all 
live in Prometheus. You can already see some of the differences like these Grafana managed alerts 
are organized into folders, which is just a handy way to keep them organized. When I click into view 
one of these alerts, I can see its status history, which is just really nice if I want to know what's 
been happening with that alert over a period of time. I can also see its version history in 
Grafana 12, or I can see where people have actually changed this alert rule itself, compare 
versions, and even restore one if I need to. When I go into edit these alert rules, I just get 
some really nice quality of life improvements. I can preview these alert rules and iterate a 
little bit on the query, or I get simplified notification routing. So in Prometheus managed 
alerts, I need to assign labels, use notification policies in order to route to contact points. 
But in the simplest case, I just want to make sure these alerts go to a specific contact point. 
There are also some new contact points we use in Grafana managed alerts like Google Chat and MQTT.
Another thing I'm very excited about and have been using myself is Grafana managed recording 
rules. Now these are recording rules like you'd be familiar with in Prometheus alerting, 
but they work with any data source. This is really handy in situations where maybe I want 
to create a time series out of a value that I can only get at a single point in time. So for 
example, if I wanted to track the number of PRs that are open in the Grafana repo over 
time, I can't get that information from GitHub, but I can use a recording rule to ping GitHub 
periodically and give me back a time series. Another really nice use of recording rules is 
that for queries that take a while to run or queries where maybe I get charged per query, I 
can create a recording rule to generate a time series and store it in Prometheus, and then 
I only have to execute that BigQuery once and I can run the recording rule over and over again.
So just to summarize, Grafana managed recording rules are a super set of data source-managed 
recording rules and alert rules, and we recommend that everybody use them right away, they're 
generally available. But I'm sitting here in an instance that has a whole bunch of Prometheus 
alert rules, so how do I move those over? And for that, we've built an import tool. This is in the 
UI and it's also available via API. So here, I'll grab my Prometheus data source, which is where 
my alert rules live today, prepped a migrated alert rules folder, and let's move over some Redis 
alert rules. The default option is to import these as paused, which we'd recommend. It's handy so 
that your alerts don't fire twice. Import those. I have the option here actually to just copy out the 
Config information and provision it back in if I prefer to do this all as code, but I'll do it here 
in the UI. Then once they're migrated over, I see they're paused, my next steps would be to route 
these to a test contact point, make sure that they work and then I can retire the old alerts.
So it's pretty handy and easy to migrate over. This is definitely something we recommend you take 
a look at as soon as you upgrade to Grafana 12. Next up is data source plugin management. So 
Mihaela, you talked about, was it 1519? 15.
Many new data sources. I'm excited about Atlassian status page and a bunch of the 
new ones. Data sources, if you're not familiar, are implemented as plugins, which means that there 
are code that's separate from Grafana core that runs alongside it. And that's great because 
it means anyone, any of us can create plugins and use them in Grafana. We can also version them 
separately, so make improvements independently of Grafana core. But as every operator knows, 
this creates a problem, and the problem is a compatibility matrix. So in the past, one of 
the biggest causes of issues in Grafana has been when people are trying to run a specific version 
of Grafana with a specific version of a plugin or two different versions of plugins against each 
other, and this just creates a lot of complexity. So last year, we set out to improve the 
way that we test end-to-end our plugins against different versions of Grafana. And this 
year, set out to give you a handful of tools to basically make sure that your plugins are always 
up-to-date and know what their dependencies are. In the connections page, when I look at my list 
of data sources, one nice kind of handy new thing is that I can install a plugin just directly 
from within the Grafana UI. This is just a lot easier than what I needed to do previously, 
which was to go to Grafana.com and install the plugins from there. You'll also notice these 
little icons next to each data source plugin, that indicates whether the plugin is up-to-date or 
whether it needs an update. And I can even filter just for plugins that need an update. So I'll 
click into GitHub, check out its version history, and I can upgrade or even downgrade just directly 
within the UI, which is just a much easier way for me to make sure my plugins are up-to-date.
The other nice little touches in this plugins page is that I can see the change log, so I can 
see what changes I'm actually upgrading to. I can see all the data source connections connected 
to this plugin. So this GitHub is a data source that uses the GitHub plugin, and a bunch of 
other handy information about dependencies, where to go for documentation or to ask 
for help. So this is basically a Grand Central Station now for managing plugins, 
and it's just a much smoother experience. One other thing I wanted to introduce you to 
is the Grafana advisor. I'd say there are three hard things in software development 
and naming things is one of them. The Grafana advisor is different from the Grafana 
assistant. The assistant is our new AI tool, and the advisor is a tool specifically for admins 
to see any issues that might be happening in their instances. We started with data source plugin 
issues, but we're looking to expand this out to other issues like auth or dashboard problems.
The kinds of things that I can see here are issues with my data sources that are failing their 
health checks, so I can see which data sources have problems that I can go and resolve. I can 
resolve those and then come back later. I can see which data sources are missing their relevant 
plugins, and I can even see once again, which plugins need an upgrade. So we're really looking 
to expand this experimental feature, the advisor, and we think it's going to be handy for admins 
who want to keep Grafana clean and up to date. Last thing that I wanted to show you is an area 
near and dear to my heart, which is in the area of auth, and that is SCIM, it has nothing 
to do with milk. SCIM is a feature in auth, works with SAML. It works right now with 
SAML Okta and Azure Active Directory, which allows you to push users and groups from 
your identity provider straight into Grafana. And returning to Super Pets, for our example, 
let's say that Mihaela just added three new warehouses to her growing business. Those 
warehouses are staffed by people who we just added to our system, and I don't have teams 
or users created in Grafana for those. That's because I have to manually create those 
teams if I want them to exist in Grafana, and those users actually have to log in order 
to exist in the database. This makes it really hard for me to do things like add them to on-call 
schedules or grant them the right permissions. The SCIM solves this problem by allowing me to go 
straight into my identity provider where, yeah, of course in Okta, I've already onboarded these 
users and created these teams. But I can pick my application, this Grafana 12 demo kit is my 
Grafana instance. I can choose which groups I want to push or even use a rule. So if I want to add 
these warehouse teams, all the teams that start with the word warehouse should exist in Grafana. 
And in my teams, they're created automatically along with all of their members. This is just 
very handy for smoothly onboarding new people. So I can go back to my schedules, quickly 
associate those schedules with these teams after I refresh my page, and then I'm off 
to the races. That means these users could actually discover Grafana and start using 
it as a result of getting notified for something going on in their warehouse. So 
just a really handy feature and a quality of life improvement for onboarding new teams.
Great, and with that, we'll return to the slides. Some of you might recognize the slide that's 
about to pop up on the screen from last year, where we presented another incremental step. 
I think this is the final step. So I'm curious who's going to recognize this slide. We've been 
replacing Angular JS with React for a long time. We've been officially using React for over 
two years now in the Grafana code base. And in Grafana 11 last year, we turned off support 
by default for Angular JS. So in Grafana 12, we're very excited. I see Torquel in the front 
row and maybe more excited than anybody else that we finally removed these thousands of 
lines of Angular code from our code base. This is really exciting to us because Angular has 
been out of maintenance for a long time, and so this is a great security upgrade and sort 
of a final step in a very long process. What do you need to do for this? Probably 
nothing. Angular's been off for a while, so just make sure your plugins are up-to-date 
and you've migrated off of old versions of those plugins, especially panels that use Angular JS. 
So we want to say thank you again to all of the plugin developers who updated a ton of third-party 
plugins and a big effort to migrate to React, and we want to say so long to Angular 
and thanks for all the two-way bindings. So that was a lot. Yeah, it's funny, it takes 90 
minutes just to say the names of all the features that we worked on this year.
Yeah, we talked about Git Sync, Foundation SDK, Grafana CTL, all of this built 
on new APIs on the app platform. We also talked about dynamic dashboards and how you can do more 
with fewer dashboards, and we got to cover some of the landmark improvements in this release 
as well from data sources to SQL expressions to improvements to Grafana managed alerts, 
and of course, Mitch's favorite, SCIM. And all this comes together in a release that's 
going to help you to onboard teams more smoothly into a very powerful observability platform, which 
then you can customize to your heart's content.

