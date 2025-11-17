# Grafana Tempo: TraceQL attr=nil (Community Call November 2025)

Published on 2025-11-13T17:49:14Z

## Description

attr = nil New TraceQL support for non-existent attribute queries Have questions? Please bring them! Can't comment in the chat?

URL: https://www.youtube.com/watch?v=-rJDQPeYVzw

## Summary

In the November Tempo community call, hosts Tiffany and Jenny Fam discussed the introduction of the new "nil operator," which allows users to query spans without specific attributes in their data. Jenny explained how the nil operator works, demonstrating how it can retrieve spans that lack a certain attribute, addressing a common issue users face when attributes are forgotten or not set. The conversation included examples of practical applications for the nil operator, highlighting its importance for users who need to identify spans that do not contain certain keys. Additionally, Tiffany encouraged community participation by inviting members to share topics for future calls or demos. The call concluded with reminders about previous discussions and upcoming events.

## Chapters

Here are the key moments from the November Tempo community call livestream, along with their timestamps:

00:00:00 Welcome and Introductions  
00:02:00 Introduction of Jenny Fam and Today's Topic  
00:03:30 Explanation of the Nil Operator and Its Purpose  
00:06:00 How Current Queries Work with Attributes  
00:08:30 Introduction of the Nil Operator Functionality  
00:10:15 Demonstration of the Nil Operator in Action  
00:13:00 Use Cases for the Nil Operator  
00:15:30 Discussion on User Feedback and Issues  
00:17:00 Information on Upcoming Community Call and PR Links  
00:18:30 Closing Remarks and Thank You to Participants

# November Tempo Community Call Transcript

**Tiffany:**  
Hello, welcome to the November Tempo community call. As usual, if you have not been to this call before, please feel free to ask questions throughout. I will bother Jenny here whenever there are questions at the right time. If you're unable to ask questions, please click on your profile icon in the top right corner and create a channel. This has become a Google YouTube requirement over the last few years, which is not super helpful. 

I am going to let you introduce yourself a bit, Jenny, and then also talk about what our topic today is.

**Jenny:**  
Thank you, Tiffany. Hello everyone, my name is Jenny Fam, and I have been a member of the Tempo team for over three years now. Today, we are going to talk about the **nil operator**, which has been requested multiple times, and we finally got it working. 

So, let’s get started. 

The problem we have right now is as follows: let's imagine we have three spans. The first and second spans have the attribute `fu` with different values, but span three does not have the attribute `fu` at all. Currently, we don’t have a way to get to this third span. 

If we query `span.fu is not equal to bar`, we get just span two back. If we query `span.fu is not equal to boo`, we get only the first one back. If we query both conditions — not equal to bar and not equal to fu — we receive nothing. We have no way to get this third span.

Here’s a very simplified demonstration of how Tempo finds attributes. For example, with the query `span.fu is not equal to bar`, we have an iterator that looks through the span attribute key column to find `fu`. We go through each row: the key for the first attribute of this span is `ABC`, the next one is `XYZ`, and then we finally get to the third one, which is `fu`—this matches the first portion of our query. 

At this point, we return the span before even checking the value of what `fu` is. Because of this, we skip over all spans without `fu` as the attribute, which is why we can't find span number three.

Now, introducing the new nil operator, which is just the non-existence operator equal to nil. Here, we assert the absence of an attribute. We already have an existence operator, not to be confused with this, which asserts that the attribute does exist in the span. 

For example, `span.fu is equal to nil` means we will return all spans without the span-level `fu` attribute. Similarly, we have `resource`, which will return all spans without the `resource.bar` attribute. 

A little introduction about the row number, just in case we get a little confused: each of these numbers represents a different level. I have a little color-coded reference for you. If the number changes, it means we've moved on to a new trace. If it changes again, we’ve moved on to the next resource batch, and so on. 

Now, looking at this span key attribute, each of these numbers can represent multiple things. Even though this is the instrumentation level, it can also represent the resource attribute level. The key takeaway is that there are different levels.

Moving on, we now have the new nil iterator, which iterates through the key column, but we keep track of whether or not the key has been seen. Let's look through the key together, imagining we're the iterator. 

We start at the first row number. The first key of this span is `ABC`, and the second attribute is `fu`. Then we notice the row number has changed, which means we've moved on to a new span. If we are looking for the `fu` attribute, we have already found it in the previous span, which does not fit our criteria of looking for its absence.

Now, in this new span, we again see the first key as `ABC` and the second key as `ABD`. Again, we notice that the row number has changed, indicating we’ve moved on to a new span. If we haven’t seen the `fu` key yet, this means that this span qualifies for our query of `fu is equal to nil`, and we would return this span.

We can look at another scenario where we move to the next span. If we haven't seen the `fu` value yet and we reach the end of the block, this span also qualifies for our query. 

So, back to the original problem: we can now get to span number three using the nil operator. Now, we can do `span.fu is equal to nil`, and this will return span three because it does not have the `fu` key at all. If you want to look for both span two and span three, you can do `span not equal to bar or span.fu is equal to nil`, and now you can get both spans back.

The scopes that we support are pretty much all scopes: resource, span, transition, links, and events. The only caveat about links and events is that we will only return the span where there is at least one event or one link without the attribute. Remember, there can be multiple links and multiple events in a span. So, if there are two events in the span, and one has `true` and one does not, that span still gets returned because one of the events does not have the attribute.

Here's a little demo. It’s pretty straightforward, but I will show you quickly. Let’s sample for this span. We can see that this span has one key. We will try to find all spans without this key. 

So, we do `span.key is equal to nil`. Let me close this. Oh, did my computer freeze? Okay, just kidding. Now we get here, and it tells me that these spans do not contain the key attribute. 

If we look through the attributes, it does not contain the specified key. Let’s try events. I’m pretty sure we don’t have an event called with an attribute called "not exist." This attribute does not exist at all. When we do a query for this, we only get back spans that contain at least one event. 

And the same goes for links. 

That’s pretty much the end of my demo. If anyone has any questions...

**Tiffany:**  
What are some specific cases where people are like, “Oh, I really need this”? I know there was an issue that someone had created, and people commented on it, but what are some of the key places that you're seeing people specifically caring about using this?

**Jenny:**  
Sometimes people forget to set the attribute and want to find those spans where they forgot to set the attribute, so they can locate those spans in their code to correct them. 

One user who submitted an issue wanted to look for a certain HTTP target that is not equal to "health" because that is not the target they are interested in. When they do `span.http.target is not equal to health`, they get back only the spans or traces where the target is actually set. However, they have multiple other services that are not HTTP related, so those spans get skipped over completely.

**Tiffany:**  
If folks are interested in looking at the PR, we have the PR link that I have put here and also in the chat. This makes it easier for people because I could see some people wondering how to use this feature, but now there is a way to do that.

I also wanted to share with folks that for those who watched last month’s call on the hyperlog log, there was a talk about the metrics generator registry active series demand estimate metrics. If folks want to take a look at the merged PR for that, it’s also part of Grafana Cloud Traces. 

If folks want to see more about the hyperlog log, please check out the community call from last month. This month’s call is quite short. If any of you watching have something you want to show or think would be cool, please go to slack.grafana.com, either in the Tempo channel or find me, Tiffany. It would be great to have folks outside of our team join in and share what you are doing.

If you have any questions for Jenny, please ask them here. If you think of something later or are watching this after the fact, Jenny, are you in the community channel, or should I pass things along to you otherwise?

**Jenny:**  
Yes, I am also in the community.

**Tiffany:**  
If you have questions about anything, whether it's this or topics you want to see in another community call, just go to the Tempo channel inside the community Slack. We also have a call scheduled for next month. If you have anything you would like us to demo, show, explain, or talk about, please share those ideas as well. We would love your feedback to make this better for everyone. 

If no one has any questions, this is going to be our shortest community call yet. Happy November, everyone! See you all in December, which is kind of crazy how fast this year is going by.

**Jenny:**  
Yeah.

**Tiffany:**  
Well, almost a new year soon enough. Thanks, everyone! If you missed it, go check out Tempo 2.9 and look into things like MCP and sampling. Again, comments and questions are welcome. 

Thanks, everyone!

## Raw YouTube Transcript

Hello, welcome to the November Tempo community call. Um, as usual, if you have not been to this call before, um, if you please ask questions throughout, I will bother Jenny here. Um I guess this direction bother Jenny here. Um whenever I uh there's some questions there at the right time. Um if you're unable to ask questions, please click on your uh profile icon in the top right corner and then create a channel uh sometime in the last few years. That has become a Google uh YouTube uh requirement or you can't do anything which is not super helpful. Um yeah. So I am going to let you uh introduce yourself a bit and then um also talk a bit about what our topic today is as well. >> Thank you Tiffany. Um hello everyone. My name is Jenny Fam and I have been a member on the temple team for over three years now. Um and today we are going to talk about the uh the Neil operator which um has been a has been requested multiple times but um we finally we finally got it um working. So um let's get started. So um so the problem we have right now is okay let's imagine we have three spans right here. Um span the first span and the second span have the attribute fu right they have different values but they exist and then span three do not have the attribute fu at all right and currently we don't have a way to get to this third span right if we do span of fu is not equal to bar we get just span two back and then if we do span of fu is not equal to boo we get just the first one back and then we if we do both right not equal to bar n equal to fu we get nothing. We have no way to get this third span. Um and here's a very very simplified um you know uh demonstration of how tempo finds attributes right. So here we have this query span.fu is not equal to bar. Um so what it does is we have an iterator that looks through the uh the key the span attribute key column right to find food. So we go through each row like hey the key for this first attribute of this span is ABC right the next one is XYZ and then we finally get to third one which is fu which matches the first portion of our query and so now we return the span before we even check the value of what fu is right foo is just the key of the attribute so because of this we skip over all of the spans without fu as the attribute and hence why we can't find the span number three from the last slide. Right? Um because it does not have the fu attribute at all. And then so right so now introducing the the new thing that we have the nil operator which is just the non-existence operator which is just equal to nil. Um here we assert the absence of an attribute. Um right we we already have a an existent operator so not to be confused with that which is not equals to nil right we do span of fu is not equals to nil that asserts that that attribute does exist in the span right and this is the equal to nil version of that which asserts that the attribute does not exist. Um so here we have span of food is equal to nil which means we will return all spans without the span level food attribute and here's resource um same concept right it will return uh all spans without the resource bar attribute um a little introduction about the row number just in case we get a little confused um so each of these numbers uh here represents a different level right here I have a little colorcoded thing for you. Um, right. So, this first one, if this number change, it means we've moved on to a new trace. If this number change, we've moved on to the next res uh batch or resource, right? So on and so forth. Um, so here we're looking at this span key attribute, right? Now, um just a little um aside, but each of these um numbers can represent multiple things, right? So even though this is the instrumentation level, it can also represent the resource attribute level. Um so each thing can represent multiple multiple um things but anyways but there are different the thing to know is that there are different levels. Um going off from that, we now have the uh the the new nil iterator um which it also um iterates through the key column, but now we keep track of whether or not the key has been seen or not. Right? So here we go. We let's look through this the the key together. Imagine we're the iterator now. Um we're going to go to the first row number. All right? So this span the first key the first attribute of this span is ABC first attribute of this the second attribute is food and then we go to the next line we notice this number has changed this means we've moved on to a new stand right um and see since we are looking for the the fu um attribute it means that this first stand we have already found the fu attribute which does not fit our criteria of we're looking for the absence of food. Right? So now we're in the new a new span right here. Um again we go through the same thing. The first key is ABC. Second key is ABD. And again we notice that hey this number has changed. This means we've moved on to a new span. And look we've moved on to a new span without seeing the foo key. This means that this span right here um qualifies for our um query here of fu is equal to n. So we'd return this. Right? So that's one one condition we look for is the if we've moved on to a new span or not and if the key has not been seen yet and then we have another scenario, right? We move on again next the next span, right? Um again we have not seen the full value here in in the next band but look it is the end of the block right so another exit for us is we've reached end of the block and this band still doesn't have the the the key fu it means this band also qualifies for our query right here and so right back to the original problem we can now get to span number three um using the no operator Now we can do span of fu is equal to new. And this will return span three because hey look span 3 does not have the fu key in it at all. Right? And if you're if you want to look for um both span two and span three you can do span not equal to bar or span up food is equal to nil. And now you can get both span two and three back. Um so this the the scopes that we support are pretty much all scopes. um resource span and transition and links and events. The only caveat about links and events is we um we will only return the span where there is at least one event or one link without the attribute because remember there can be multiple links in a span and multiple events in a span. So if there are two events in the span and one has true and one does not, that span still gets returned because one of the events does not have the attribute, right? Um, and here's a little demo. I mean, it's pretty much straightforward, but I will just show you quickly. Uh, so let's sample for this span. We can see in this band, this band has one here, right? So we're going to try to find all spans without this one key. So we go to do span do one is equal to nil. Let me close this. Oh, did my computer freeze? Okay, just kidding. Right. So now we get here and look, it tells me that these bands do not contain the one key attribute. Right. Oops. I think this is not as good. This one. Is it this one? Yes. All right. If we look through the attributes, it does not contain right the the one key. And let's let's try events. Right. So, I'm pretty sure we don't have an event called with with an attribute called um not exist. Right. So, this attribute does not exist at all. Right. When we do a query for this, we only get back spans that contained at least one event, right? So, here's the event. And this event does not contain um any of the the key that I specify, which is this key not exist. And the same goes for um links. Cool. Um that's pretty much the end of my demo. Um if anyone has any questions >> um like so I guess what are some like specific cases where people are like oh I really need this or like I know that there's was a issue that someone had created since and people had like commented on it but like what are like some of the key places that you're seeing people like specifically caring about using this? >> Right. So what happens is sometimes um people forget to set the attribute right and they want to let's get to those bands where they forgot to set the attribute for and they want to so that they can find those bands in their code to set the attribute for. Um and uh but also I think the one of the one of the um uh users who submitted an issue is uh they wanted to look for a certain uh HTTP target, right? Um which is not equal to I think health because that is I guess not not the one that they're interested in. But then if they once I do span.http.target target is not equal to um health. They get back only like the spans or the traces where the the target is actually set, right? But they have multiple other um services that are not HTTP related, right? So they those spans will be skipped over completely. >> Yeah. >> Okay. And then like if folks are interested in going and looking at the PR u we have the PR over the link that I have put here. It's also I put in the chat as well. Um and then uh I also Whoops, I clicked on the wrong thing. Banner. Okay. So yeah, that that definitely makes it easier for people because like I guess I could see some people like wait so how do you do that? But now there is a way to be able to go and do that. Yep. And then um I wanted to just share it with folks like for folks who watched last um um last month's call on the hyperlog log um there was the talk about the um metrics generator registry active series demand estimate metrics. So um if folks want to go and take a look at uh the merge PR that is over there for that and it's also as in part of uh graphana cloud traces as well. Um and if folks want to see more about the hyperlo log if you want to go take a look at the community call from last month. Uh this month is quite short for our call. Um if any of you watching are like hey I have this thing that I really want to show or it would be really cool. Um, please go over to the uh Slack for so it's slack.garfana.com. So go there um in the either the Tempo channel um or find Tiffany um message me because it would be really cool to have folks outside of uh us on here as well and seeing what you're all doing. Um if you have any questions uh for Jenny um please ask them here. uh if you think of something later or you're watching this after the fact um I are you in the uh community channel or should I pass things along to you otherwise? >> Yep, I am I am also in the community. >> So yeah, if you have questions you have about anything whether it's this whether it's things that you want to see in another community call if it's something that you have in general uh just go to the tempo channel inside of the community inside of the uh community slack. And then we also have uh a call um that is over next month. And then also if you have um anything that you would like us to demo or show or explain, talk about etc. Um please share those as well. We would love to have your ideas and just make this even better for you all. So yeah, I guess if no one has any questions, this is going to be our shortest community call yet. Happy November hooks. Um and then yeah, see everyone in December, I guess, which is kind of crazy how fast this year is going by. >> Yeah. >> So, >> well, almost a new year soon enough. So, yeah. Well, uh thanks everyone. And also, if you missed it, it's been a little bit now, but uh go check out Tempo2.9. Um look into things with like MCP and sampling. Um again comments we'll take those questions etc. So yeah thanks everyone. >> Thanks everyone.

