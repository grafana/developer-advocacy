# Save and Share Queries with Others in Your Organization (Public Preview) | Grafana 12.2

Published on 2025-09-25T14:50:21Z

## Description

Saved Queries (formerly Query Library) is now in public preview with Grafana 12.2! This feature makes it simple to save, reuse, ...

URL: https://www.youtube.com/watch?v=YzrgoFAxK_g

## Summary

In this video, Dan, a product manager at Grafana, introduces the new feature of saved queries, previously known as the query library, which is now in public preview. The feature allows users to save and share queries within their organization, enhancing collaboration. Dan demonstrates how to save a query, add tags, and control visibility settings. He shows how other users can access saved queries, utilize filters, and manage their queries through options like editing, duplicating, and deleting. Additionally, he highlights the ability to integrate saved queries into dashboards. Overall, the video explains the functionality and benefits of the saved queries feature in Grafana.

# Introduction to Saved Queries at Grafana

My name is Dan, and I'm a product manager at Grafana. In this quick video, I'll show you our feature: **Saved Queries**, formerly known as the Query Library, which we are releasing into public preview.

## Purpose of Saved Queries

This feature exists to help users save their queries and share them with other people in their organization if they believe they'll be useful.

## Creating and Saving a Query

Let's start in Explore and write a query. Suppose this query is really useful, and I want to save it for future reference. I can click on **Save Query**. This will open up the Save Queries drawer.

- **Title**: Let's give it a title, such as "Query for Video."
- **Tags**: I can also give it a tag, like "Team A."
- **Visibility**: There's a checkbox that, if checked, allows all users to see it. If it's unticked, only the author will be able to see the query.

After saving that query titled "Query for Video," I can close the Save Queries drawer and remove the query I just had.

## Adding a Saved Query

Now, let's say I'm a different user and I want to add that query. I click on **Add from Saved Queries**, go to **Query for Video**, and select the query. Here it is!

## Managing Saved Queries

If I want to replace this with a different query and I'm looking through the available queries, I can first remove the data source filter to see all the queries I have. I can filter by:

- **Data Source**
- **Author** (currently just me)
- **Tags**

If I filter, you can see how that works. I can also search, so if I type in "useful," I will get the queries that contain the word "useful" in the description.

### Favorites and Recent Queries

- **Favorites**: These are the queries that have been favorited, which you can do in the **All** tab.
- **Recent**: You can also see recent queries like this one, which I can save.

## Editing Saved Queries

Another feature to note is that you can edit these queries as well. For example, if I grab "Query for Video," the lock icon indicates that it is locked, meaning that no one can edit it for now. Only the author of the query or admins can unlock it.

Once I unlock it, I'm able to edit it. I can change information like the description to "for the recording," add a new tag (e.g., "Team B"), change the title, and save it. Additionally, in the context menu, I can duplicate or delete the query.

Once a query is unlocked, I can explore it by clicking on it. I can change the query and then save it, and the query will be updated. When you use these queries, we essentially copy and paste the whole value. Therefore, if you've used it previously and want to change it, you'll need to select the query again where it's been used.

## Using Queries in Dashboards

The last thing I wanted to show is that these queries can also be used in dashboards. If I create a new dashboard, I'm able to place a saved query. I can grab this one, and it will be automatically populated.

That's everything! I hope you find this feature useful.

## Raw YouTube Transcript

My name is Dan and I'm a
product manager at Grafana. And this is a quick video to show
you our feature: saved queries, formally known as the query library, which
we are releasing into public preview. This feature exists to help users save
their queries and also share them with other people in their organization
if they think they'll be useful. So, let's start in explore and write a query. And let's say that this query is really
useful and I want to save this query for future reference. I can go
here and click on save query. So I'll open up the save queries
draw. I can give it a title.. query for video, video query, and give it a tag. Team A. And there's also a checkbox
here where if you check the box, all users will be able to see
it. Well, if it's unticked only, the author will be able to see the query.
So if I now save that query, query for video, I've got it here and I close the save
queries rule and I remove the query that I just had. Let's say I'm a different
user and I want to add that query, click on "add from save queries",
go to "query for video", and I select the query. And here it is. Now let's pretend that I want to replace
this with a different query and I'm looking through the queries that
are available to me. Well, firstly, if I remove the data source filter, you
can see all the queries I've got here. You can filter by data source,
filter by author -- at the moment, that's just me. Filter
by tag. So if I filter, you can see how that works. You can
also search, so if I type in useful, you'll get these queries where I've
got the word useful in the description. There are favorites for when if I
remove that filter, that search, favorites, which are the queries
that have been favorited, which you can do in the
All tab and also recent, where you can add recent
queries like this, a recent query. Save. Another thing to know is that you
can edit these queries as well. So let's grab query from video. The lock icon here is here
saying that it's locked, which means that no one
can edit this for now. Only the author of the query or
admins are able to unlock a query. So let's go ahead and unlock
this. And now I'm able to edit it. I can edit information here.. "for the recording." I can add a new tag. Team B. Can change the
title and save that. I'm also able to, in that context menu,
duplicate the query or delete the query. On top of that, once the
query has been unlocked, I can edit that query and
explore clicking on it here. I can change this to something
else and now save that query and the query will have been
updated. When you use these queries, we copy paste the whole
value, essentially. And
so once it's been updated, if you've used it previously
and you want to change that, you'll have to go and select the
query again where it's been used. The last thing I wanted to show is that
these can also be used in dashboards. So if I make a new dashboard, I'm able to also place with a save query. Grab this one here and it's automatically
populated. That's everything. I hope you find that feature useful.

