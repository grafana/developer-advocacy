# Grafana Tempo: TraceQL metrics arithmetic (July 2026 Community Call)

Published on 2026-07-10T05:00:02Z

## Description

Links/resources: Learn about https://grafana.com/oss/tempo/ Get started with the Grafana Cloud forever-free tier: ...

URL: https://www.youtube.com/watch?v=n9mBEd00D1s

## Summary

The show is titled "Grafana Tempo: TraceQL metrics arithmetic," and it took place on July 10, 2026. The speakers included Marty, who presented the session. The discussion focused on the new features of TraceQL in Grafana Tempo, particularly the ability to perform arithmetic operations on metrics queries. Key takeaways included the introduction of mathematical operations such as addition, subtraction, multiplication, and division within TraceQL, allowing users to analyze error rates and other metrics more effectively. The session also highlighted the use of exemplars for tracing specific spans and the performance optimizations made in the new implementation of TraceQL.

Topics: Grafana Tempo, TraceQL, metrics arithmetic, exemplars, error rates.

## Chapters

00:00:00 TraceQL metrics and arithmetic operations
00:06:22 Understanding exemplars in Grafana Tempo
00:11:44 TraceQL metrics arithmetic in Grafana Tempo
00:17:52 Discussing TraceQL math operators and limitations

Hello everybody and welcome to our July Tempo community call. Today, you've got myself and Marty, and we are going to be looking at math here in a minute. Before we get into that, as always, please post any questions in the live stream chat on YouTube, or you can post any questions in our Slack channel, the Tempo community channel. I'll keep an eye on that. It doesn't have to be about today's topic; it can be about anything Tempo-related. I'm more than happy to answer anything.

There is a secret trick to be able to post on YouTube. I’m going to try to get this correct because Tiffany usually gets this. You have to create a channel in the top right of your account, and then that will let you chat within the YouTube chat interface. 

So, without further ado, feel free to add comments at any time. Don't wait until the end or save them for later. We'd much rather answer them as they come in, even if they're off-topic. We’d much rather engage with the community than give a presentation. So again, don’t hold off on asking questions; feed them to us and we'll answer them.

Now, without further ado, I'm going to turn the show over to Marty. Marty, if you want me to initially post up your screen share, I can, or if you want to do an intro, we can do that too.

**Marty:** Uh sure. Yeah, did you say we're going to talk about math?

**Host:** Yes.

**Marty:** Super exciting. 

*(laughter)*

**Marty:** I hope everybody is getting lunch, thinking, "Oh yeah, let's talk about math."

**Host:** Edge of their seat stuff here, buddy. Don't downplay it.

**Marty:** It actually is, I think, going to be pretty cool. So, we’ll try to...

Um yeah, we can go ahead and share the screen. What we're talking about today is TraceQL metrics and some additions we've made to the query language. A metrics query is something like this: I have spans, I can do a search, I want to turn this into metrics, and I have functions like rate. This has been in there for a while; I think everybody has probably used this by now. Hopefully, it's going great.

Now, we want to do math and other computations between series. I can do things like this: I can get the rate, and maybe look at segmenting this by service name. So, I'm exploring my data, but I want to do other stuff between different queries. Maybe I want to look at my errors. Just my errors. Now I want to know, well, this is great. I have 100 spans a second that are airing, but I don't understand how this relates to my full data set. Is this a high error rate? Is this a low error rate?

What I really want to be able to do is compare this against maybe that other query, which was the full rate. This is what we've been working on in TraceQL. I can do things like this and add a query here. Now, this is two separate metrics queries, both of which I've kind of run for you here. This first one is the error rate, and now I'm going to divide it by the total rate of data. So now I'm seeing it's proportional. Now I know, okay, it's 40% of my spans are airing. That's cool, and I can actually start typing in any query I want in here. Maybe I want to know what's the error rate per service? 

Now I can see, oh, it's actually these two services. This is the k6 client tracing or test tracing data generator here. So that's what this is. The gateway and all service every few minutes are kind of running into some trouble here. What I'm getting is what's the error rate by service among all the data. I can see that 30% of this is coming from the gateway, 13% is coming from the all service, and down here Tempo, which is what I'm querying right now, has some errors too. If I click on this, I can kind of see those. 

This is really cool. We can do all kinds of operations between stuff like this. While we're here, I want to show some cool stuff. If you notice some of these little dots here that I'm highlighting, exemplars are fully supported. There’s some interesting stuff going on here. If I click on one of these gateway ones, we can see the gateway had an error here. If I click on one of these Tempo exemplars, I'll see this is coming from a different trace, which is from Tempo. 

What's interesting here is that this query involves every span. This is maybe a little detail about exemplars and how they work. How did it know Tempo is doing the work to know that this exemplar is going to the gateway? These ones are going to the Tempo service, and this is usually pretty normal, but my denominator here is actually every span. So, technically, every span belongs to every part of the query. Tempo is trying to figure out which of these is the most defining part of it and attach the exemplar there. 

Anyways, that's a little tangent about exemplars. The gist is that they should just work. Now, this is showing me my error rate for my service across all my data, but I want to be a little more precise. What is the error rate for each service among all of its data? I can do that if I put the same attribute here and group by the same one on the top and bottom. It'll do the division, and just like Prometheus, Tempo will match it up. 

I can see here that these services are failing 100% of the time. So, that is the test data.

**Host:** Hey, Marty.

**Marty:** Yeah.

**Host:** What is an exemplar? Give me a quick lowdown.

**Marty:** Sure. To do an exemplar, let's take a simpler query. We'll go back to my error rate. An exemplar is a way to know, "Give me an example of a trace that went into this specific line on the graph." Like right here, my rate was 100 spans per second. Tempo knows all the spans that went into that. An exemplar is a standard way to let the front end know what one of those trace IDs were. If I hover over it, we'll see the trace ID here, and I can click the trace and go straight to that trace on the back end. 

So, I know this trace right here, this 209 etc., went into whichever one of the dots I clicked on. It works for any query. We have a default number of exemplars that we send in, and we try to populate that. I think it's 100. You can see they're kind of spread across time. 

Now, that's actually not the best example of when you might use exemplars. What exemplars are really good for is if you're looking at things like P95s. The exemplar here, the height of it, is actually the duration that went in here. I can see this one was a much slower span. Right? So, I'm computing my P95, and I'm looking at this span, and I can see this is a slower one, 800 milliseconds here. Whereas, if I click on one of these ones down here, right? 13 milliseconds. 

That's where exemplars are really a lot more useful because I'm trying to plot out my slow queries and I want to see an example of them. Or maybe I do something like this, right? So, in this case, I can add a filter and I'm only going to get those. They’re a way to really hone in and see a spike on a graph like this one. Oh, wow, what was that? That was very slow. 15 seconds maybe?

**Grafana Tempo: TraceQL Metrics Arithmetic (July 2026 Community Call)**

It was Tempo. Yeah. So, there you go. That's where exemplars are really powerful because you can go straight from that line on the graph to the specific trace set on the back end. Does that make sense? Yeah, cool, cool.

Um, back to the riveting TraceQL metrics math. I think we're talking about this one. So, if I group by the same thing on the top and bottom, now it's actually doing that math and it's matching the series as you would expect, just like Prometheus would. 

Now, this error rate is for these services. If I click on one, it's 100% failing and then 0% failing. This is kind of like that synthetic data, and maybe Tempo is a little bit more realistic, right? So, I have like 5% failures here. This looks like a timer. I think this was the back end schedule. 

And maybe this is cool. This is between zero and one, like a floating point, but I can also do things like this. Maybe I want to multiply it, and now I've brought it into the range that's a little bit more human-readable. Maybe I want to plot this one differently. Now it's between zero and 100. You can string along any kind of mathematical operator here, including multiplication by statics and things like that.

So, that's the kind of stuff that we can do. I wanted to show one more thing. What about this multiplication? Back here to my quantile. These are in seconds, and this is another use case where multiplication might be really useful. You can plot that just fine, but I could also do something like this multiplied by 1,000, and now I've brought it into the range of milliseconds. 

So, we can do stuff like that too. And cool. That is the basic gist. I think there's a lot of cool stuff that you can do. We definitely had in mind things like error rates and manipulation of these quantiles. 

Now, there are some limitations and benefits where we diverge from PromQL a little bit. If you know TraceQL, Tempo is not using the Prometheus engine to run TraceQL. A lot of this is re-implemented, and it has benefits like letting us push queries down differently and do different things that are more trace-specific. 

If I go back to this query here, it's going to compute my service rate, my error rate by service across all my data. If you notice, all I'm doing is a simple divide here. This is an area that we're happy with; we feel like it was a good usability improvement. If there is an unlabeled series in the denominator, Tempo will just know to divide it or multiply by it, etc. 

If you've written a lot of PromQL, you might know that previously you had to control the series matching between the two sides a little bit more. This would achieve the same effect if you were doing metrics queries. But in this case, because we're implementing it from scratch, we've been able to say, "Oh, well, actually, I think it would be great if it just worked." 

So, that's one thing we've done. The flip side is that we don't yet support that fancy grouping. I have an example query here that does not work. Let's say I want to do a little bit of fancy manipulation. Now, I have different groups on the top and bottom. 

Let's say I'm getting my errors by user, and I want to know what percent of that is within the company. In my data, I have multiple companies and users, for example. We don't support that, but what you would want, if we did, would be something like "on company, group left, right?" That would let you control the way the series match together, and maybe you can add and drop labels or things like that. 

So, we don't yet support that. That is something we do want to support because this would be a really cool query. But for now, we're really happy with the way this is working, and we hope it's pretty useful for everybody. 

I'm just trying to think if there's anything else that I wanted to call out. Oh, yeah. It's not just division and multiplication. You can also do things like this. Maybe there's a reason you want to run two different queries and add them together. 

Oh, okay. I don't know what that was, but it definitely works. Now, this is basically adding these together. I wanted to call out the labels down here. Hopefully, they try to match the general structure of the query you're running. We kind of did that because I don't know what other kind of label you would put on this. 

In this case, we know we're doing a rate plus a rate, so that's what we get here. Cool, cool. And this should totally work. Yes, yes, math works. 

It's 1.0. Perfect. And the label works. Cool. 

I was a little surprised because of the floating point. 

Yeah, you expect some jitter maybe? 

Yeah, but in the back end, it might see those integer values or something. 

Um, yeah, a few little questions here, and you may have covered this one while I was looking at something else, but the little red squigglies—like I assume at some point will the front end catch the kind of new operators? 

Yeah, exactly. We do have some open PRs to get this supported. Basically, the language parser in the front end needs to be updated to support this new structure. Even though these red squigglies are here and I'm using Grafana 12.3, they definitely work. It'll send the query to Tempo, and it'll show the results. 

It can be a little bit alarming, but if this is in a dashboard panel, no worries. You won't have to look at it. But yeah, we do have that work in progress. 

If I wanted to run this on OSS Tempo, is this in main 3.x, 2.x? What is the current state of the feature? 

Yeah, everything I'm showing here will be in 3.1. I believe there was maybe a small PR or two that made its way into 3.0, but you should really expect the full feature to land in 3.1. 

Is there any feature flags or configuration necessary to do this? 

I want to say no. 

Okay. 

Yeah, it should work. 

And is there any performance... 

Well, hold on. To take a step back, if metrics are working, then it's there. I think in 3.0, we maybe still have a little bit of the—I can't remember if we fully dropped all of the old architecture or not. But if you're running some of the old architecture, you may have to have enabled it through the generator local blocks. If you're running the new architecture with block builders and live stores, all of this is going to work right away. 

So, the true test is if you can come in here and run this. I love running this query to just debug and know things are working all the time. If you can come in here and just run a rate and you see a graph, you know this will work. 

Awesome. 

In 3.1. 

Um, is there any, like, other than just rerunning the queries, is there any sort of performance concerns or, you know, with running the math other than you're probably duplicating queries? 

Oh, yeah. Do you mean like if I want to do something that's a little complicated? 

Yeah. 

Um, no. So, what we did is we tried to give this the best performance possible. You might think we do it by running this query and then running this query, and we bubble it all...

Back up into one place and we do the division. It's not how it works. We actually push this entire thing down as far as possible, all the way down to the individual block files. We evaluate all of this together and then bubble it up once.

Oh, cool.

So, we pushed out as much as possible. Um, but yeah, I think, you know, there it's going to be a little bit slower. There is more work involved, you know, room for profiling and optimization for sure.

Yeah. And, uh, what are the basic math operators supported? Is there a listing of maybe the math we actually support?

The full listing is probably in the TraceQL parser files, honestly. Um, I can't remember. We might need to add a little bit more to the documentation, but yeah, there is more. Um, I think, you know, maybe something like this.

Yeah. Oh, yeah. Wait, sorry. Is that the actual operator? Maybe it's times. I can't remember, but I believe we do support other operators. It's totally—I don't remember, but I really thought we had like exponential operators in there. So, yeah, there should be a full host of math stuff.

Yeah.

Um, I mean, I assume subtraction, addition, multiplication, division.

Ninety percent of the use case is like four operators, basically, right?

Exactly. Um, yeah. And so, you know, I would love to hear about limitations, like a query that you would love to have if we just supported group left or something like that. So, you know, when we hear that feedback, we'll do the work in those areas.

Okay. Uh, all right. I think that's kind of all the questions that I had queued up while you were...

Sure.

...going in doing the awesome demo. Uh, we'll give just a minute or two here to see if anything falls or comes through.

Yeah. Oh yeah, I wanted to show this because we were talking about this earlier, but if you run a histogram over time, the UI has been updated to just know to show this as a heat map, and this is super cool. So, histograms—this is actually the same functionality behind the scenes that we used to compute quantiles. These are the buckets. These are all of my spans that are in this bucket here, which is 3 milliseconds to roughly like, you know, 6.7, etc. So, these are exponential buckets, so that's really cool. Maybe I just want to look at, you know, just my errors—like how long are those taking? So, those are much slower. You know, things like that. Um, I think this is cool. The heat map looks really cool.

Fantastic.

All right. 

Yeah, so, you know, like we use this internally on some dashboards. So, maybe you want to look at a certain route, and maybe I want to look at my tag lookups or something. Uh, that's a little sparse. 

[snorts] 

Maybe we'll try a different one while we're here just playing around with stuff. 

Yeah.

[clears throat] 

Anyways, that's kind of cool. Yeah, so you can hone in on certain jobs and things like that. Yeah, this is the same visualization that you might see in drill down for the histogram. Same function, but now it works in Explorer as well.

All right. 

Um, cool.

Yeah, so I appreciate you coming on here and showing off math a little bit.

Oh, yeah. I want to mention one more thing.

Okay.

Absolutely.

So, if you notice, there's a lot of parentheses floating around here. And right now, we require parentheses, so it always looks like this. Right?

Oh, yeah.

Okay. In text, this looked easier to read. But the form is always like this: parentheses around a query operator, parentheses around a query. The reason we do that is because of just parsing ambiguity. For now, we require the parentheses. You know, because if you do something like this, it becomes a little bit harder to parse definitively. And, um, this one is, you know, because maybe I add like 100 here, it's not quite exactly clear which order of operations this is going to take place in. Is this 100 part of this query or is it separate, right? So, right now, for now, we require the parentheses everywhere. So, you'll see that.

Awesome. 

All right. Get a second here to see if anything may come through. 

Uh, one thing I wanted to call out from the community is some great people in our community created the 3.0 to Boh helm chart. I'll put the PR here. Um, so I wanted to call that out. Um, so yeah. That's great. Now you can run the helm chart with 3.0, which had a lot of breaking changes. So, I'm sure that was not a small endeavor.

But all right. Well, that gets us about time unless there's any other questions. We appreciate you coming on here, Marty, and we appreciate everybody for watching. Again, if you have any questions, they don't have to be during the community time. Feel free to post them up in the Slack channel. That's probably the quickest and easiest way to get a hold of us. And as always, we'll be back in about a month. So, I appreciate everybody. Thank you.

Cool. Cool. Thanks. Bye.

## Raw YouTube Transcript

Hello everybody and welcome to our July uh Tempo community call. Um so today uh you've got myself and Marty and we are going to be looking at math here in a minute. Um before we get into that though, as always, uh please post any questions in the live stream chat on YouTube or um you can post the chat any questions in our Slack channel. Uh the Croda community channel, there's a or >> [clears throat] >> Slack and there is a Tempo channel there that you can post up and I'll keep an eye on that. Um doesn't have to be about the topic of today, can be about anything uh that we're uh you know, Tempo related. More than happy to answer anything. Um there is a secret trick to uh be able to post on YouTube. I'm going to try to get this correct cuz Tiffany usually gets this. Uh you have to create a channel I believe in the top right on your like account and then that will let you uh chat within the uh YouTube chat interface. So uh without further ado uh actually, with one more further ado, uh feel free to add comments at any time. Don't wait till the end. Don't like save them till if we have time. We'd much rather answer them as they come in uh even if they're you know, off topic. You know, we I'd much rather uh engage with the community uh than give a presentation. So again don't hold off on asking questions. Uh feed them to us and we'll answer them. So now, without further ado, I'm going to turn the show over to Marty and Marty, if when uh if you want me initially to post up your screen share, I can or if you want to do a a intro, we can do that too. >> Uh sure. Yeah, did you say we're going to talk about math? >> Yes. >> Super exciting. >> [laughter] >> I hope everybody is on their like getting lunch. Like, oh yeah, let's talk about math. >> Edge of their seat stuff here, buddy. Don't you be downplaying it. >> it actually is, I think, going to be pretty cool. >> So, we'll try to >> Um yeah, uh no, we can go ahead and share the screen. Yeah, so what we're talking today is about Trace QL metrics and some additions we've made to the query language and a metrics query is something like this. Um I have spans. I can do a search. I want to turn this into metrics and I have functions like rate. So, this has been in there for a while. I think everybody has probably used this by now. Hopefully, it's going great. And math is now we want to do math and other computations between series. So, I can do things like this. I can get the rate. I can maybe look at, you know, segment this by service name, right? So, I'm exploring my data, but I want to do other stuff between different queries. Like maybe that one I just had and this one. Um maybe I want to do something like this. Um I want to look at my errors. Just just my errors and and now I want to know, well, this is great. So, I have 100 spans a second that are airing and but I don't understand like how does this relate to my full data set? Is this a high error rate? Is this a low error rate? >> [clears throat] >> And so, what I really would need to want to be able to do is to compare this against maybe that other query which was the full rate. So, this is what we've been working on in Trace QL and I can do things like this and add a query like here. Where so, this is now two separate metrics queries, both of which I've kind of ran for you here. Um this first one is the error rate and now I'm going to divide it by the total rate of data. So now I'm seeing it's proportional. So now I know, okay, it's 40% of my spans are airing. Okay, that's cool and I can actually start typing in any query I want in here and maybe I want to know what's the error rate per service? And so now I can see, oh, it's actually these two services. This is the K6 uh client tracing or test tracing uh data generator here. So that's what this is. Gateway and all service every few minutes are kind of like running into some trouble here. And so what I'm doing is now I'm now the query I'm getting is what's the error rate by service among all the data. So I can kind of see that 30% of this is coming from the gateway. 13% is coming from the all service and down here Tempo, which is what I'm querying right now, has some errors too and if I click on this, I can kind of see those. And so yeah, this is really cool. So we can do all kinds of operations between stuff like this. Mhm. And while we're here, I want to show some cool stuff. So exemplars, if you notice some of these little dots here that I'm highlighting, exemplars are totally fully supported and um there's kind of some kind of some interesting stuff going on here. So if I click on one of these gateway ones, we can see the gateway had an error here. And if I click on one of these Tempo exemplars, I'll see this is coming from a different trace, which is from Tempo. And what's interesting here is that actually this query involves every span and this is maybe a little bit detail about exemplars how they work. But how did it know Tempo is doing the work to know that this exemplar is going to the gateway. These ones are going to to the Tempo service and this is usually pretty normal, but my denominator here is actually every span. So, technically every span belongs to every part of the query. So, but anyways, Tempo is trying to figure out which is which of these is the most defining part of it and attach the exemplar there. Anyways, that's a little tangent about exemplars and the gist is that they should just work. Um okay, now this is showing me my error rate for my service across all my data, but actually I want to go a little bit more precise. What is the error rate for each service among all of its data? Like actually how what is the error rate per service? And so, I can do that if I put the same attribute here and I group by the same one on the top and bottom, it'll do the division and just like Prometheus, Tempo will will match it up. And so, I can see here actually these services are failing 100% of the time. So, that is the test data. >> Hey, Marty. >> Yeah. >> What um what is an exemplar? Give me like a quick >> Oh, what's an exemplar? >> second uh lowdown. >> Sure. Yeah, so to do an exemplar, let's take a simpler query. We'll go back to my error rate. And an exemplar is a way to know give me an example of a trace that went into this specific line on the graph. Like right here, my rate was 100 spans per second. Well, Tempo knows all the spans that went into that. An exemplar is a way a standard way to let the front end know what one of those trace IDs were and if I hover over it, we'll see the trace ID here and I can click the trace and I can go straight to that trace on the back end. So, I know this trace right here, this 209 etc., went into whichever one of one of dots I clicked on. Went into that is specific part of the graph. And um it works for for any query. So, we have like a default number of exemplars that we send into and um we try to populate that. I think it's 100. So, there you can kind of see they're kind of spread across time. Now, that's This is actually not There's a better example of when you might use exemplars. And what exemplars are really good for if you're looking at things like P95s. And so, this is the duration. Now, the exemplar here, the height of it is actually the duration that went in here. So, I can see this one was a much slower span. Right? So, I'm computing my P95 and I'm looking at this span and I I can see this is a slower one, 800 milliseconds here. Whereas, if I click on one of these ones down here, right? 13 milliseconds. So, that's where exemplars are really a lot more useful because I'm trying to plot out my slow queries and I want to see an example of them. And you know, or maybe I do something like this, right? Yeah, so in this case like I can add a filter and I'm only going to get those. So, they're they're way to really hone in and you see a spike on a graph like this one. Oh, wow, what was that? That was very slow. 15 seconds maybe? Yeah, that was a 15 It was tempo. Yeah. Uh yeah, so there you go. So, that's where exemplars are really powerful because you can go straight from that line on the graph to the specific trace set on the back end. Does that make sense? Yeah, cool, cool. Um Yeah, yeah. So, back to the riveting trace QL math metrics math. Uh I think we're talking about this one. Yeah, yeah. So, if I whatever I group by, if I group by the same thing on the top and bottom, now it's actually doing that math and it's matching the series as you would expect just like Prometheus would. Um so now this error rate is for these services by click on one it's 100% failing and then 0% failing and so this is kind of like that synthetic data and maybe Tempo is a little bit more realistic, right? So I have like 5% failures here. This looks like a timer. I think this was the back end schedule. >> [clears throat] >> And um maybe uh this is cool. This is between zero and one. This is you know, like a floating point, but I can also do things like this. Maybe I want to multiply it and now I've brought it into the range that's a little bit more human readable. Maybe I want to plot this one differently. Um so now it's between zero and 100 and so yeah, you kind of string along any kind of uh mathematical operator here including multiplication by statics and things like that. Um so yeah, so that's the kind of stuff that we can do. And um I wanted to show one more thing. What about this multiplication? So back here to my quantile. And so these are in seconds and this is another use case where multiplication might be really useful. These are in seconds and you can plot that just fine. But I could also do something like this multiplied by 1,000 and now I've brought it into the range of milliseconds. So yeah, we can do stuff like that too. And cool. So that is the basic gist. I think there's a lot of cool stuff that you can do. We definitely had in mind things like error rates, um like manipulation of like these quantiles and things like that. Now, there are some limitations/benefits where we diverge from PromQL a little bit. So if you know TraceQL, um we Tempo is not using the Prometheus engine to to run TraceQL. So a lot of this is re-implemented and it has benefits like it lets us push queries down differently, it lets us do different things that are more trace specific. Um and this is actually if I go back to this query here, going to compute my service rate, my error rate by service across all my data. And if you notice, all all I'm doing is a simple divide here. And this is an area that we're happy we feel like it was a good good uh usability improvement. If there is an unlabeled series in the denominator, Tempo will just know to divide it. And or multiply by it, etc. And so, you know, if you've written a lot of PromQL, you might know that maybe previously you had to do like in PromQL you have to do stuff like this, you have to control the the the series matching between the two sides a little bit more. And so, this would achieve the same effect if you were say doing metrics queries. Um but in this case, because we're implementing it from scratch, we've been able to kind of like say, "Oh, well, actually, you know, I think it would be great if it just just worked." So, that's one thing we've done. Um but the flip side is is that we don't yet support that fancy grouping yet. So, I have a example query here that does not work. Um let's say I want to do a little bit of fancy manipulation here. Oh, sorry, this is not supposed to be there. Like this. Now, I have different groups on the top and bottom. So, let's say I'm getting my errors by user and I want to know what percent of that is within the company. So, in my data I have multiple companies and users, for example. We don't support that, but what you want, if we did, would be something like on company, you know, group left, right? Then that would let you like they're asymmetrical two sides and it would let you control that the way the series match together and maybe you can add and drop labels or things like that. So, we don't yet support that. Um that is something we do want to support because this would be a really cool query. Um but yeah. So, but but for now like we're really happy with uh the way this is working and we hope it's pretty useful for everybody. And I'm just trying to think is there anything else that I wanted to call out? Oh, yeah. So, it's not just division and multiplication. You know, you can also do things like this. So, I maybe there's a reason you want to run two different queries and add them together. Um but Oh, okay. I don't know what that was. But definitely works. So, now this is basically adding these together. And oh, yeah. I wanted to call out the labels down here. Hopefully try to kind of match the general structure of the query you're running. So, we kind of did that because um I don't know what else you would what other kind of label would you put on this? So, because So, in this case we know we're doing a rate plus a rate. So, that's what we get here. Cool. Cool. And this should totally work. Yes. Yes, math works. >> [laughter] >> It's one 1.0. Perfect. And the label works. Cool. >> I actually was I'm a little surprised because of the floating point. >> Yeah, you expect some jitter maybe? >> Yeah, but but in the back end it might see those integer values or something. Um yeah, a few little questions here and you may have covered this one while I was uh >> Mhm. >> I'm looking at something else, but uh the little red squiggly's like I assume at some point will the uh front end will catch the um kind of new operators. >> Yeah, exactly. We do have some open PR's um that to get this supported the basically the language parser in the front end needs to be updated to to choose yeah, to support this new structure. And uh yeah, so even though these red squigglies are here and I'm using Grafana 12.3, um even though these are here, they definitely work. It'll send the query to Tempo, it'll show the results. Um So, it can be a little bit alarming, but you know, if this is in dashboard panel, like no worries. You won't have to look at it. Uh but yeah, we do have that that work in progress. >> If I wanted to run this on like OSS Tempo, um is this in main 3.x, 2.x? What is the kind of current state of the feature? >> Yeah, it all of everything I'm showing here will be in 3.1. I believe there was maybe a small PR or two that made its way into 3.0, but yeah, you should really expect uh like the full feature to land in 3.1. >> Is there any feature flags or configuration necessary uh to do this? >> Uh I want to say no. >> Okay. >> Yeah, it should work. Yep. >> And is there any like performance >> Well, hold on, to take a step back. So, it you know, if metrics are working, then it's there. And I think in 3.0, we maybe still have a little bit of the I can't remember if we fully dropped all of the old architecture or not, but if you're running some of the old architecture, you may have to have enabled it through the generator local blocks. If you're running the new architecture with block builders and live stores, all of this is going to work right away. So, the true test is if you can come in here and run this, and I love running this query to just debug to just know things are working all the time. So, if you can come in here and just run a rate and you see a graph, you know this will work. >> Awesome. >> In 3.1. Yeah. >> Um is there any like other than just rerunning the queries, is there any sort of performance uh concerns or um you know, with with kind of running the math other than you're probably duplicating queries. >> Oh, yeah. Do you mean like if I want to do something like that that's a little complicated? >> [clears throat] >> Yeah. Um, no. So, the tempo what we did is we tried to give this the best performance possible. So, you might think, you know, we do it by running this query and then running this query and we bubble it all back up into one place and we do the division. It's not how it works. We actually push this entire thing down as far as possible all the way down to the individual block files. And evaluate all of this together and then bubble it up once. >> Oh, cool. >> So, we So, we pushed out as much as possible. Um, but yeah, I think, you know, there it's going to be a little bit slower. There is more work involved. You know, room for, uh, profiling and optimization for sure. Yeah. >> Yeah. And, uh, what what Are are are the basic math operators supported or is there a a listing of maybe the, you know, what what math we actually support? >> The full listing is probably in the TraceQL parser files, honestly. >> Um, I can't remember We might need to add a little bit more to the documentation, but yeah, there is more. Um, I think you know, maybe something like this. >> Yeah. Oh, yeah. Wait, sorry. Is that the actual operator? Maybe it's Maybe it's times times. I can't remember, but I believe we do support other It's totally I don't remember, but I really thought we had like exponential operators in there. So, yeah, there should be a a full host of math stuff. >> Yeah. >> Um, >> I mean, I assume >> subtraction subtraction yeah, addition multiplication division. >> 90% of the use case is like four operators, basically, right? >> Exactly. Um, yeah. And so, you know, I would love to hear like limitations part like >> [clears throat] >> you know, a query that you would love to have if we just supported group left or something like that. So, you know, when we hear that feedback, we'll do the work in those areas. >> Okay. Uh all right. I think that's kind of all the questions that I kind of had queued up while you were >> Sure. >> going in doing the awesome demo. Uh we'll give just a minute or two here to see if anything uh falls or come through. >> Yeah. Oh yeah, I wanted to show this because we were talking about this earlier, but if you run histogram over time, the UI has been updated to just know to show this as a heat map, and this is super cool. And so histograms is the actually this is the same functionality behind the scenes that we used to compute quantiles. So, these are the buckets. These are all of my spans that are in this bucket here, which is 3 milliseconds to roughly like, you know, 6.7, etc. So, these are exponential buckets, so that's really cool. So, maybe I just want to look at you know, just my errors like like how long are those taking? So, those are much slower. You know, things like that. Um I think this is cool. See map looks really cool. >> Fantastic. All right. >> Yeah, so um you know, like we we use this internally on some dashboards. So, maybe you want to like look at a certain route, and maybe I want to look at my tag lookups or something. Uh that's a little sparse. >> [snorts] >> Maybe we'll try a different one while we're here just playing around with stuff. Yeah. >> [clears throat] >> Anyways, that's kind of cool. Yeah, so you can hone in on certain jobs and things like that. Yeah, this is the same visualization that you might see in drill down for the histogram. Same Same function, but now it works in Explorer as well. >> All right. Um >> Cool. >> Yeah, so I appreciate you coming on here and showing off math a little bit. >> Oh, yeah. I want to mention one more thing. >> Okay. >> Absolutely. >> So, if you notice, there's a lot of parentheses floating around here. And right now, we require parentheses, so it it always the form always looks like this. Right? >> Oh, yeah. >> Okay. In text, this looked it was easier to read. But, the form is is always like this. So, parentheses around a query operator, parentheses around a query. And the reason we do that is because of just parsing ambiguity for now, we require the parentheses. You know, cuz if you do something like this, it's a little bit becomes a little bit harder to to parse definitively. And um this one is uh you know, cuz maybe I add like 100 here, it's not quite exactly clear which order of operations this is going to take place in. Um is this is this 100 part of this query or is it separate, right? So, right now for now, we require the parentheses everywhere. So, you'll see that. >> Awesome. All right. Get a second here to see if he may come through. Uh one thing I wanted to call out from the community is uh uh some great people in our community created the uh 3.0 to Boh helm chart. Uh I'll put the PR here. Um so, I I wanted to call that out. Um so yeah. That's great. So now you can um you know, run the home chart with 3.0 which had a lot of breaking changes. So I'm sure that was not a small endeavor. But all right. Well, that gets us about time unless there's any other questions. Well, we appreciate you coming on here, Marty and we appreciate everybody for watching and again uh if you have any questions, they don't have to be during the community time. Feel free to post them up in the Slack channel. That's the probably the quickest and easiest way to get a hold of us. And as always, we'll be back in about a month. So I appreciate everybody. Thank you. >> Cool. Cool. Thanks. Bye.

