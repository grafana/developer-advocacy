# GrafanaCON 2024 Keynote: Grafana 11, Loki 3.0, Alloy, Golden Grot Awards, and more | Grafana

During GrafanaCON 2024, we came back together in person for the first time since 2019. Grafana Labs CEO and Co-founder Raj ...

Published on 2024-04-15T20:09:06Z

URL: https://www.youtube.com/watch?v=L_GHahMOWEY

Transcript: Welcome to GrafanaCON. This is our
biggest community event so far. My name is Carl Bergquist.
I'm a principal engineer. Hi, I'm Mihaela Maior. I'm a director of engineering and I'm so
excited to be here from recording those videos - which I hope
you all appreciated... it wasn't easy - to
making this for the event. I've been so excited to join you all here. So the last time we were in person
for GrafanaCON was 2019 in LA and we are really excited to be back in
person after four years of GrafanaCON online. Could you do
a quick show of hands? For how many of you is this
the first GrafanaCON ever? Oh, wow. . How many of you were at
GrafanaCON Amsterdam 2018? 1, 2, 3  Yeah. Okay. So 2018 was very special
for me because mid-day one, my girlfriend called me and said
that we're expecting twins. And the rest of the conference
is kind of blurry to me, but I do remember the end and that is
that we could fit the whole company on stage, which is big
difference compared to now. Yeah. And at GrafanaCON 2019, we actually announced our
idea for the LGTM Stack. So at that point we had
Grafana, obviously. In 2018, we announced Loki and T and
M were kind of still ideas, but today in 2024, our open
source projects include so much. So that's Loki, Grafana, Tempo, Mimir
- our LGTM Stack, but so much more. We've got Pyroscope, k6, OnCall,
Faro, Beyla, and much, much more. So this year we've expanded GrafanaCON
to focus on all of the extended open source ecosystem. You'll hear more about
them in this keynote and
throughout the next two days as well. GrafanaCON is our opportunity to celebrate
our big tent philosophy and also our community. And with that, I'd like
to invite you to give it up to Raj. Thank you. Appreciate it. Thanks, Carl. Thank you. Hello
everyone. My name's Raj Dutt, and I'm one of the co-founders and the
CEO here at Grafana Labs. Appreciate it. Might need that. It's really a
pleasure to be here in Amsterdam. Like Carl said, we're back here after six years and
it's been five years since our last in-person event. And I gotta say, after sort of three or four
years of virtual GrafanaCONs, I'm kind of virtual-ed out. So I hope you're all glad to be here in
person and recapture some of that energy that we have at these events. So I kind of was staring
from behind the stage there. I guess there were three or four people
who joined us at GrafanaCON in 2018. Just raise your hands again. All
right. Yeah, that's surprising. So five or six people. Do you remember
how cold it was back then in 2018? It was the coldest day on record
for the year in Amsterdam, and all the flights were delayed. And
it's amazing to be back, warmer weather, bigger venue, and so much
has changed. You know, it's just been an incredible
five or six years. Carl mentioned that the last time
we were here in Amsterdam 2018, we fit the whole company on stage.
At the end of the conference, we invited everyone up. The
entire company attended, and we were about 35 people. And it's kind of just insane for me
to think that in the last six years, it would now take about 4, 7, 4 sevens
to fit the whole company together. We've grown from 30 people to over
a thousand since we were here last. And yeah, so much has changed. But my overwhelming emotion
at every GrafanaCON is really excitement and gratitude. Of
course, we're here to celebrate. I'm really excited that we launch Grafana
11. We do this generally every year, launch a major version of the open
source project that is at the center of everything that we do. So
this year is no different. Our engineering teams are always trying
to figure out how the date of the Grafana is set. And our marketing team thinks that it's
the engineering teams that come up with the date. But really the marketing team comes up
with the GrafanaCON date and kind of tricks our engineering teams into
agreeing to release it on that day. We call it conference-driven development, and we've been doing it for a long time. But obviously Torkel is
gonna be on stage shortly, and he's gonna be unveiling
what you're all here to see: a new version of Grafana
11. But like I said, really feeling grateful
today. Very excited. But I really wanted to celebrate kind
of three or four key areas as we look back and also as we look ahead. So the
first one is everyone at Grafana Labs. We call them Grafanistas. Like I said, there's over a thousand super
talented people all over the world. We like to say that we're not
really a multi-national company. We're more post-geographic.
And even before COVID, since 2014, sorry, since 2016, we were remote-first since
before it was in fashion. So we really figured out how to be this
remote organization, post-geographic, like I said, and it's really in our DNA. And it's wonderful to be such an
international company with employees, like I said, from over 40 countries. And it gives us a really global
flavor to everything that we do. And speaking of Grafanistas,
I just wanna take a pause, take a beat to just thank the events
team at Grafana Labs for putting on this incredible event. And it takes
a lot of work, all the logistics, all the planning. So from everyone, from Katy to Sonia to the
entire Grafana Labs events team. Just give a quick round of
applause. Thank you very much. I'd also like to thank our customers, and I remember really clearly at
the last GrafanaCONs, again, 2018, 2019 like another world, I used to ask people in the audience
to raise their hands if they were a customer. And I knew not a whole lot
of people would raise their hands, because at the time, we only had maybe
a dozen customers. At this point, we have over 5,000, which again, blows my mind from a milestone standpoint. So raise your hand if you're a
customer of Grafana Labs in any way. Wow, that's that's really
impressive. I'd say maybe a third, a third of the audience at this point. That's more customers in this room
than we had at the last conference. Very cool to see. And our customers big
and small from the largest, you know, top 10 companies in the world to startups
and hobbyists using the free tier of Grafana Cloud. And it's great
to see that growth. And finally, and most importantly, the thing that we celebrate at
all GrafanaCONs is the community. And the community has also grown a lot
since we last got together in person at a GrafanaCON. There's over a million instances of
Grafana out in the wild that we see, that we track, and we are so privileged to be at the
center of mass of this really vibrant community and ecosystem. And
as Carl and Mihaela said, we really believe in the big tent,
bringing together other projects, other ecosystems, other
vendors all underneath Grafana, and helping you analyze your data, understand your data no
matter where it lives. So while we're really excited to talk
about things like Grafana, Loki, Mimir, Tempo, all of our projects, it's important to remember that
no matter where your data lives, whether you're using vendors like
Elastic, Splunk Influx, Clickhouse, there's a lot of interesting technologies,
a lot of interesting databases, a lot of interesting projects
out on the ecosystem. And it's really important to our mission
to help you own your own observability strategy and be able to visualize
and understand your data, whether it's in one of our databases
or whether it's in another database altogether. And that's a true core
part of our big tent philosophy. So when it comes to community, we always take a few moments to
celebrate some dashboards in the wild. And this year is no different.
So I'm gonna look back, look at three or four dashboards that
caught our eye and share them with you. And just to kind of underscore
how flexible Grafana is, none of these dashboards have anything
to do with what most people normally use Grafana for, which is monitoring
IT, monitoring servers, monitoring Kubernetes, you know, the typical SRE observability
developer use case. None of these dashboards
have anything to do with it. So we're constantly delighted,
surprised, oftentimes amused, sometimes confused by what
our community is up to. So I'm gonna share some examples.
Before we get to the dashboard examples. I just wanna take a quick moment to
talk about a new program we have. The Champions program at Grafana, and we
launched this just over the last year. And this program really exists to
recognize all the community members who are active in our community, who help
each other, help the community at large. Whether that's on our forums, on our
Slack channels, on our community help. And so our mission with this program
is really to advance that knowledge and that outreach beyond the walls of Grafana
Labs and formalize what has always been happening kind of
naturally in the ecosystem. So big thank you to
all the champions here. I know that five or six of
you are here in the audience. And looking forward to hearing
from two or three of you speak. So big thanks to all the champions in
this new program that we've established. Alright, so dashboards in the
wild. I always find this fun. We'll take a look at a few of these. So
this first one is actually from the BBC. They have a mobile app called
BBC Sounds. Now I don't live in the UK or Europe, but who here is
familiar with BBC Sounds? Yeah. All right, quite a few of you. I thought this might be kind of a DOA
project and no one had heard of it, but apparently it's used by some of you. So BBC Sounds is a streaming app, and it gives listeners access to the
full gamut of BBC's live radio stations, and on-demand content. And this dashboard is really looking
at the mobile network connectivity performance and the streaming
audio performance across the BBC footprint. And if
listeners are on the move, if they're walking through
particular parts of the UK, it helps the BBC really track kind
of network quality and how the user experience is doing as far as
the streaming service goes. And I thought this was
pretty interesting. Again, nothing to do with traditional
observability use cases
and really nice use of geomap visualization. This next
one comes up again and again, but this is one of the nicest examples
I've seen. This is off someone's Fitbit. And so I've started keeping track of
some health stats. I use an Apple watch. I'm frustrated by how the
data's visualized on my iPhone, but this is absolutely gorgeous. And so you can see that this is actually
from a community member, Arpang, but he's visualizing all his Fitbit data, whether it's from steps to his blood
oxygen to his heart rate activity and just visualizing it beautifully in Grafana,
sending all that data to Grafana Cloud. He has long-term access to all
his health metrics and you know, looks really good too. And it looks like there's several
hundred people using this dashboard. So sharing is caring, and if you wanna
check it out you can find it on GitHub. This last one is both
amusing and maybe sinister. This is from one of our
solutions engineers, and he's using Grafana when military
school is not an option for his kids. So Brian LeBlanc, again, one
of our solutions engineers,
works at Grafana Labs, uses Grafana, Slack, as well as our incident response
management system to alert the correct household members when his
kids' rooms aren't cleaned, when their chores aren't
done. And believe me, escalations in this household
are a very serious thing. And I know Brian's even looking at
introducing a service level objective to hold his kids to. And so, you know, it's great they're learning Grafana
when they're young, they're learning, you know, they're learning how
to be good kids hopefully, too. And you can see this is all integrated
with Slack. And according to Brian, he calls this the Robo Parenting
Project, which I find amusing. But it's working out pretty well and I
guess ask him in 10 years and we'll see how it's going. And so this final example, this final dashboard from the wild is
about a topic and an area that's near and dear to many Grafanistas'
hearts: space travel. So I still remember really
clearly I think it was back in 2018 when we were watching
a SpaceX launch and we saw Grafana on launch control
through just a media clip. And we weren't sure that it was Grafana. We had to zoom into the monitor
on this random news clip. And we found Grafana was used
in SpaceX launch control. We sent an email to SpaceX,
we sent an email to Elon Musk, but he never responded to us. That's okay.
Since then, it was also used by NASA, which was really cool. And then finally, just over the last year
it's now being used by the Japanese JAXA SLIM
lunar landing modules. And we're really excited
at GrafanaCON, we're gonna welcome Satoshi Nakahira from JAXA
and he's actually gonna speak on how JAXA used Grafana to actually
help with telemetry on their lunar landing. And you can actually see from this
dashboard that's a pretty cool panel. And I'm actually really
looking forward to this talk, but there seems to be a little niche
that Grafana is able to exploit when it comes to space travel, and we're
really glad to, to see that build. Alright, so I've saved the best two
dashboards for last. Over the last year, we've launched something that
we call our Golden Grot Awards. And just like I mentioned, we've been informally kind of looking
at these dashboards every year. And over the last two years, we've launched these awards where we
look at the best personal and the best professional dashboard
from across the community. There's an internal panel of judges,
we cull it down to five finalists. And then there's a public voting period
where our entire community votes on the best personal dashboard and the best
professional dashboard. And of course, we give away a Golden Grot award. So I'd like to unveil the
two winners from this year. And here we go. So from
the personal standpoint, I'd like to congratulate Ruben Fernandez
and ask him to come up here for his Golden Grot. And Elyssa Emrich is here too, from our developer relationships program
to present the physical Grot Award. But congratulations. Congratulations,
Ruben. This is a really cool dashboard. I understand it's for
tracking your commute. You've hooked it up with the Atlanta
Metropolitan Transport Authority. You've got some Bing maps and hopefully
it's made your commute very accurate and error free. So all the
best in your future commutes, and if you ever have any data integrity
problems with judging the distance of your commute, you can't blame us. But
best of luck, . Thank you. Yeah, see ya. So that's the personal
winner for the Golden Grot. And the second Golden Grot winner for
the professional category is Christopher Field from Theia Scientific. So Christopher and his brother
are AI/ML researchers and nuclear physicists, and they teamed up at
Theia Scientific to analyze basically material science over time.
So we all know time series data, and we all think of numbers, but
this is actually getting a new image snapshot and storing it
in a time series database. There's all sorts of custom data sources, custom panels but this is actually
a visualization of part of a nuclear reactor. And it's using machine learning to
understand how these materials degrade, don't degrade and perform over time.
So it's super cool stuff and if again, completely unrelated to
Kubernetes, CPU, Disk I/O, but it just goes to show how powerful
Grafana is and some of the crazy things that our community gets up to that
we can barely understand. So Chris, congratulations on
winning the Golden Grot. All right, well then, now the moment you've all been waiting
for I'd like to call up Torkel Ödegaard, my partner in crime, our co-founder, and the man who's excited to talk
about a special announcement today. You'll notice the title CGO. Many companies have CXO titles. You know, we have a Chief Technology Officer,
he's somewhere around here. Tom, you might meet him. I have a
Chief Financial Officer, Wailun, he's busy talking to
some investors in the US. I'm the Chief Executive Officer, but there's a very important title
at Grafana Labs. It's called the CGO, and that just goes to show who we are,
and that's our Chief Grafana Officer. So Torkel, take it away. Thanks. Thanks, Raj. Well, it's a true pleasure to be
back on stage for a real in-person GrafanaCON and talk about
a new major version of Grafana. So Grafana 11. It is out in preview today. It's really kind of the summation
of a year full of minor releases, full of new features and enhancements
and many features that have been released in preview form that are now ready
for prime time in Grafana 11. So we'll have a deep dissection later
today that will kind of go into detail about everything. There's one really big new feature in Grafana 11
that we haven't showed off or released in preview form before, that I wanna demo
and talk about today. But before I do, I want to give you some background because
I think this feature really addresses the core mission of Grafana
that we've had from the start, which is to make observability
easy and powerful through good UX design, focus on ease of use and
user flexibility and freedom. In the beginning we refer to this
goal as, "Democratize metrics." And throughout the years we've
approached it in varying ways, but mostly by kind of focusing on, on making query editors easier
to use and more powerful, improving ways to sort of
build panels and dashboards, improving ways you can sort of
navigate data and explore or connect dashboards together by data links. But we always thought that
Grafana can do better, like learning to define these
queries and building these panels. And dashboards still take a
lot of learning and knowledge and time, and even the best kind of
design dashboards can suffer
from being too static. So what if Grafana could do it all
for you dynamically and on the fly? And that is kind of what, what
this new feature, Explore Metrics, is trying to do. Let's jump into a demo. So you find this new feature
under Explore > Explore Metrics, and the first time you go there, you will be jumped into what
we call a new exploration, a new metric exploration. And the
first goal is to select a metric. So instead of just being presented
by a bunch of metric names, you actually see graphs
of, of the data you have, you can filter down this list of
metric names by adding, for example, a label filter. And of course you
can type in some search words. So let's type in HTTP
because I'm interested here
in some HTTP metrics for an application. And I get to see some flask HTTP
request duration metrics here. Which sounds like a good thing 'cause I, I know we're using Flask HTTP library
in the Python application that I'm working on. And if I select this metric, I go into the kind of the
main visualization view for
this UI of this feature. And one thing to note here is
that there's no query builder. There's no query editor, really.
Grafana will create the Prometheus query automatically for you by
looking at the metric name. So Prometheus metrics have some kind of
standardized metric naming conventions that Grafana can use here to
deduce a really a suitable query and also a suitable unit as you'll see. So this is looking at the
request per second rate here. If I go to related metrics, I
can jump to a different metric that match the current
label filters that I have, but it also filters or sorts
similar name metrics to the top. So right at the top here,
I see other kind of flask, HTTP request duration metrics,
for example, this bucket metric. So if I select this metric, I
instead get three percentile queries and 99th percentile 90th and 50th. So you don't have to know how to write
a percentile query in PromQL here. It's all done for you. And you can
also switch to a heat map view here, which is a different form of Prometheus
query to do a proper heat map query. Something that can still
be quite tricky to do in, in a Grafana dashboard panel to get
the Prometheus query right and the visualization settings
correct. But here in this UI, you don't have to think about
anything, it's just done for you. So one thing to note here when I
change time range here there are new blue dots being added here. So this at the top here is
what we call the history trail. So every kind of label filter change
you do or any sort of change of the metric you're looking
at or time range change, it kind of records a new dot here, which makes it super easy to go back to
previous states of the view to previous time ranges you looked at or
previous metrics or filter states. So let's go back to this kind of
request per second metric here, because if I zoom out a bit,
it has these spikes, which is interesting because I only
have a cluster label filter here. So this spike could really be coming
from many different applications, many different instances
of that application. Many different HTTP operations could
all be contributing to this graph. So it would be really nice to be able
to deaggregate this data to be able to identify where this spike is coming from. And that's what the
breakdown tab is all about. It enables you to automatically view this, the graph at the top there, but grouped by all the different
labels that exist for this metric. So I can see the data here
grouped by container, job, method, path and pod. I can also orient this view in rows, so I can kind of align it with the graph
at the top there, which stays fixed. You can disable that the graph stays
fixed at the top there, but it's really handy to
be able to align a spike. So let's go into the job label here,
for example. And if I scroll here, I can clearly see that this spike
in the aggregated graph is clearly coming from the right service payment
job or application in this case. So I can add that to the label
filters, it gets added to the top, and I can continue this breakdown,
the aggregation workflow. I can look at the status label and
I clearly see here that spikes are generating 500 status errors because
it's correlated with this status 500 series. So I can add
that to the label filters, and I can continue here to
look at, for example, path. And I see here that all these requests are to the pay operation. So I hope you can see how fast, easy, intuitive it is to do this root cause analysis or ad hoc drill down
without having to modify a query by adding, trying different group
buys or or spending time building interlinked drill down dashboards. It's all done for you automatically
and on the fly in this UI. And speaking of dashboards, you can actually access this UI
directly from a dashboard as well. So if you have a Prometheus
query in a graph panel, you can, from the menu, open and access this Explore
Metrics UI directly inside a drawer without having
to leave the dashboard. And from here directly
do the same deaggregation breakdown. And if you find
something interesting, you can open this in the standalone
view here. Again, can share URL to this page, of course. Open the query explorer to to
do some manual changes to it, create a bookmark and if
you use the breadcrumb, you can go to the feature landing page
where you can easily jump into any of your recent explorations
or bookmarks. So yeah, I'm really excited about this feature
and general direction it takes Grafana. So that's the end of the demo and
we can jump back to the slides here. As I said, this feature is only for Prometheus
metrics, which is a shame. It would be really cool to have something
like this, but for logs as well. So luckily at Grafana Labs, we have these company-wide
week-long hackathon events where groups of people can
form teams that try to build on anything they want as long as it can
solve something for the company or it's good for the community, they
can build anything. In a week. And the winner of our last hackathon
built something really incredible. The last hackathon was in March this year
and they built something really inspired by this Explore Metrics feature. And at the end of the hackathon, each team has to submit a video that
kinda shows the problem they're trying to solve and what they built. And we thought it would be fun
to give you an insight as well, into the Grafana Labs company culture
a bit, to show this video as well. After the video, there's gonna be a demo
of this really cool hackathon project. Hello, I'm Matt Ryer. Welcome
to Grafana's LogQuest, a game show where we put new
Loki features to the test. Two contestants will go head to head. One will show us how you would solve a
problem today with current Loki tech. The other will show us how
you use innovations in this
hackathon to solve those same problems. Meet Cyril. Cyril has been working on
Loki since 2019. Cyril hello. Hello Matt. Let's meet our other contestant, Jonathan. Jonathan is new to tech and he got his
job here only because his uncle has got some dirt on Tom. I'm also
gonna have to play Jonathan. Alright. Hey Jonathan. I'm Jonathan. To be honest, I'm not really
into computers, not really my thing, right? So it's safe to say that
you don't know LogQL, Jonathan. Couldn't even spell it. Oh, ,
that's . That's good, isn't it? In round one, our contestants need to find out the
misbehaving pod within the Mimir ingestor service. It's Cyril to go
first. Off you go, Cyril. So. This is gonna be super simple. So
first we're gonna go to explore. Well, I can see why Loki is so
popular. Let's see how Jonathan fares. How would you do it with the new
UI, Jonathan, over to you. Right, well I'll just pick the
service, then filter by labels. This is done automatically for me.
Level is what I want, and I want errors. Let's have a look. Well, there you go,
that's the pod with all the errors. Okay, thank you very much. The results
are in. Well, Cyril, you used many years, three or four years of LogQL experience. Jonathan didn't use any and only
took a few seconds and is an idiot. So for round one,
Jonathan takes the point! In round two, right? We found the pod, but there's been an incident and we need
to find out which users were impacted by a particular incident.
Cyril, it's you to go first. What do you got for us? We found the pod. Again, very simple.
We just need to remove everything. Excellent. Thank you very much.
Congratulations! Jonathan, how are you gonna cope with this? Well I'll just do one
click here. Click here. And then I'll just go and do another
click here. Look, that one, that one took me two clicks. For round
two, the point again, goes to Jonathan! In the final round, we are looking
for the version number of a service, but the trouble is the logs
are very noisy. Cyril to play. No, I'm not gonna play. I know that I have to keep excluding
things one by one and it's gonna take too long. And what if I accidentally
exclude the line that I'm looking for? I think Jonathan can just do it easily
by pausing the extracted pattern. It doesn't even see the noise. You can
jump right to the river and logline. Well, I think it's, congratulations again
Jonathan, and thank you for watching. So welcome Cyril to give
you a deep dive into this amazing project. Alright, thank you everyone. Super excited to be here to show you
this new application that's inspired by Explore Metrics. We call it Explore
Logs. So we're gonna switch to the demo. So Jonathan is actually at the event. If you meet him today let him
know that I wanna say hi again. . Alright, so can we see my screen? Yes. So you're gonna see the same
pattern as Explore Metrics. You're gonna find Explore
Logs and our explore and logs. So on the landing page we
show you all the services. So it's by service name
and then a breakdown. So for each row it's a breakdown of the
volume per level, and then next to it, a glimpse of how the logs
look like. So we can see, you know, very quickly which
services is interesting. And then at the same time we
can also search for services. So I'm gonna search for Mimir
services for instance, right? So we can see for instance, that the
Mimir ingestor is having some errors. So I'm gonna drill into that. So on the second page, once
you're locked in services, and by the way, those services are actually
automatically detected for you by Loki. So once you're on this page at the top, you still see the volume histogram with
the breakdown per level at the bottom is the same as the explore log panel. So the same experience
that you used to have. And you can see the labels
for each of the log line. So however, what is different here is
that you don't even have to write a query. We actually give you tools to explore
your logs without writing any query. So let's look at all of those tools. So the first one is breakdown per
label. Those index label by Loki, which are very powerful and helps you
to query faster Loki and slice and dice the data. What's very interesting is
I can actually look at Mimir ingestor, and realize, how is it
logging across all my cluster, all my pods and all the
namespace. And I can use them to, I can use those labels to filter down the
data directly and make choice based on trend. So I'm gonna look at some cluster. So it's the same as
Explore Metrics. Again, you have like different views where you
can like combine all the cluster in a single view or go in the rows UI where it's all aligned
with the top histogram. So let's select US-East and I can go back and now
it's filtered down by US-East. And then I can look at the
pods and try to find an outlier. So one of them
that is looking much more. So let me just look at
all of them. There we go. This one seems to be looking more. So you see take decision
based on the graph directly. Alright, the second feature, which is
very interesting is detected fields. So those fields are actually not indexed. They are the one from the log
content directly that you have. And it's kinda like automatically
building for you some sort of a dashboard and shows you like for, so
this is a GRPC API mostly, the logs themselves. And it gives
you an idea of the duration, for instance. So, you know, 20 seconds right now around 20 seconds
as an average, which is not great, the type of errors that
you have in the logs. And then even the tenant that
is extracted from the content. And I can go and just suddenly
filter for tenant 1010. And then again, I'm
reducing the amount of data. So I wanna show you another services
because I think the detected fill is super powerful. I have another
services which is very popular, the nginx reverse proxy that
I'm sure a lot of you are very familiar with. So it
logs obviously in json. And what's very powerful about the
detected field is almost really building a dashboard for me, you
know, using just the logs. So I can see the request rate per host,
I can see the request rate per path. I can select a specific path if
I want, like the Loki patterns, which is a new API in Loki. And I
can keep going down and, you know, maybe just focus on the five hundreds
and then I'm only seeing in the logs now the five hundreds and
this path. So that's, that's what I think is very powerful. I wanna show you one last feature before
I stop the demo, which is patterns. Patterns detection. So this is a new feature we have
in Loki and that this app is using. I'm gonna go to Tempo distributor, which is intentionally a
very noisy application. I'm gonna change to another one
'cause it doesn't have patterns. There we go. Needed a refresh. Alright so the patterns. So this application actually logs
a lot. And if we look at the logs, you'll probably not notice the version
number when the pod is starting. But if I'm witnessing an incident, I'm actually having a lot of logs and
it's very difficult for me to find a specific log 'cause we are limited
to a thousand in the log panel. So by using the pattern and
looking maybe at the row, I can see each of the different patterns. So I can look at this one to have a bit
more information and how those patterns affect my logging output. So you can see that we have a lot of
completed block and I can remove it if I want 'cause this one doesn't sound to
be related to the incident. And I can, you know, have a sense of the trend of each patterns
and then use them and filter and find more information in my log. So this is the one that I'm interested
in every time the pod starts. So the incident about the version,
I can add it to the filter, and then suddenly I'm seeing very
quickly the version of my pods. Cool. That's it for the demo.
Gonna switch back to slides. Alright, so I wanna extend a big thank you to
the team who worked on this because since the hackathon, it
was like four weeks ago, we actually worked very hard on this. So it's been a big race to actually
release this today for you guys. And it's available in the open source. It's a new plugin that you can grab
the repo and then go and install. It's also available in play.grafana.com. This is what I just used
for doing the demo today. And this is not the only features
that we have in Loki 3.0. I wanna welcome Owen Diehl, principal engineer on the Loki project,
to talk about the new features. Thank you. He really said 3.0, that's
supposed to be my line. Okay. Hey everyone, I'm Owen. Cyril and I have
worked a long time on Loki together. So yeah, Loki 3.0. It is fresh, hot off
the presses, you can download it now. There's a lot of new stuff.
We have another session later. The interesting thing is this also
coincides with roughly five years since we started the project. And so
there's a lot that's changed, but we've kind of tried to stay
true to our roots along the way. So, which is especially important for a
logging project. You know, logging... roots couldn't really resist there.
But anyways, this is what I mean. And the top one is everyone's widely agreed
on most important metric for open source projects. I joke a little bit, but it actually is a pretty
good metric of stars on GitHub. The bottom one is actual
installations that we hear about and we doubled in about the past
year, which is really big for us. Really excited to be working on a
project that's been able to reach so many people. Does anyone use Loki here? Any?
A couple. Alright, no hands. Bummer. And so today we're gonna
talk about a lot of things. We're gonna talk about scale, but it's really important to mention that
this is kind of the roots of a lot of Loki Loki's history. It's these small
deployments, you know, the DIYers, the open source conference goers, and we started as like
Prometheus, but for logs. And I kind of love this story
because we were actually built, we still are built on top of Prometheus
and so you get a lot of really nice things transferring between
different signals that way. But now we actually have people coming
to Loki that don't use Prometheus, that haven't experienced that before. So kind of becoming the primary thing
for a lot of people has been really exciting to see in the project. So we've built on a couple
of principles. You know, we want to run on commodity hardware,
so you can run it everywhere affordably. We want it to do schemaless,
you know, so, no heavy indexing. So you can ingest logs from everywhere,
any team, any language, any source, whether you control that
or not. And as I said, we wanted kind of effortless
Prometheus compatibility. So you can switch between these things. Basically we want to make sure that Loki
is the right tool for you if this is your stage, you know, starting in the
garage and wherever you end up, if it's, you know, garage to my home lab garage
to monitoring my garden or a garage to boardroom with my startup. And so Loki can kinda go further now. And historically this has meant we
can maybe do some more features, we can scan more data faster, but we're realizing that for
us to continue to advance, we're really gonna need to be more
efficient as well. And that's not just, you know, technical empathy and
being efficient in that sense, but it also means some of the stuff
that Cyril was just talking about, building foundations for
queryless user experience, that we can reach more people and not
require people to be experts in LogQL. Also means things like making the targeted
search that Loki already does more automatic so that you don't need to
spend time figuring out how to extract value from Loki. You can spend time extracting value
from the data that you put in it. And so I'm really, really
excited to announce this. We teased it end of last year, but Loki 3.0 is launching with
experimental support for automatic query acceleration. This is done internally via special
application of a concept called Bloom Filters. And the gist of it is that for a lot
of queries we'll be able to get you the same results faster by only
querying a small fraction, you know, 10% or less, in a lot of
cases, of the data itself. And so if you really wanna
see a little bit more here, make sure you catch our talk in
about half an hour, 45 minutes, something like that. Five
years in Loki turns 3.0. Next is Stephanie Hingtgen. She's gonna talk about Grafana and a bunch
of different ways that we've extended that. Thank you. Yes, thanks. Thanks Owen. I am so thrilled that we all get to be
here together in person and I'm super excited to be sharing with you all
about the future of Grafana and plugin developments. As many of you know, plugins have long been
at the heart of Grafana. They truly embody our big tent philosophy, which emphasizes interoperability
within the wider ecosystem so that you can visualize and analyze
your data no matter where it lives, all within one single pane of glass. And over the years we have seen an immense
amount of creativity and innovation from all of the plugins
you all have developed. From the Redis and Zabbix plugin to the
status and Tree Map panel to countless others. You all have transformed the
way that we visualize and analyze data. Meanwhile, we've heard from you all the limitations
and the boundaries that you faced while developing plugins such as lacking
storage and being limited to solely defining new data sources
and panels. So for a while now, we've been looking at a way to address
these limitations and today we're incredibly excited to announce
that we found a solution. Through a major shift in
our underlying architecture, plugins will become first party
applications within Grafana. This shift is going to completely remove
the boundaries that plugins face today and will allow plugins
to access everything that
core Grafana has access to, such as storage, authentication, and defining things beyond data
sources and panels. Additionally, these new applications will be able
to interact with one another and this interaction is something we're really
excited about as it's gonna open a lot of really cool doors to creating
powerful observability solutions. To achieve all of this, we'll be evolving Grafana into an
observability application platform. We originally built this platform
internally and after deploying some cloud plugins like SLO on top of it, we've
seen the benefits that it can provide. So now we're starting to bring it into
Grafana and continuing to iterate on it there so that you all can continue
to innovate without any boundaries. As we start on this journey, we cannot wait to see where
you will take Grafana next. We have been continuously blown away by
the really unique use cases you've found for Grafana that we never thought
of. And with this new platform, we can't wait to see the new things
that you all dream of. Tomorrow, Ryan and I will be diving into what
this platform looks like and what it can give you. And then Joe will follow up
with a presentation on how
his team deployed the SLO app on top of this platform. But for now, we invite you to dream with us. Think about the problems that you faced
in the observability space before and solutions that you wish
existed. With this platform, we can build those together. And so now I'm going to invite Paschalis
up to the stage to talk about some more big tent investments we're making. Hey, so another tentpole of Grafana's
philosophy is our continuous investment in OpenTelemetry as a
vendor agnostic protocol. And Grafana Labs is one of the leading
contributors in the OpenTelemetry ecosystem. We are spearheading the inclusion of
profiles as an OTLP signal with enabling native OTLP ingestion in
Mimir, Prometheus, Loki, and Tempo has been not all native from
day one and our community members, our engineers have been really active
in the community from specification to semantic conventions, sustainability
efforts and all things. So for us, part of this journey is making sure that
we are there to meet you wherever your data is. So today we're excited
to announce our new product, Grafana Alloy. Grafana Lab's distribution
of the OpenTelemetry collector. Alloy is a spiritual successor to Grafana
Agent and comes super charged with capabilities to help you write, scale,
and debug powerful telemetry pipelines. It works with any auto compatible
backend like the open source LGTM stack. And as a collector, Alloy has first class support for the
OpenTelemetry collector components that you're already using: the receiver,
processors, and exporters, to build OTel native pipelines, but to also support for
Prometheus and Loki pipelines. This makes for a tailored experience
based on your needs wherever you are in your OpenTelemetry journey alongside
your current observability setup. Furthermore, as a
batteries-included platform, you have over a hundred components to
help you integrate with data from big cloud providers, your Windows,
Linux, and MacOS hosts, most popular applications and databases, as well as third party tools
like Vault. So to summarize, Alloy's our distribution
of the OpenTelemetry
collector and it comes with a unique feature set that is built over
our lessons learned from years of running telemetry collectors at large
scale. And our big tent values. To name a few, Alloy natively integrates with Kubernetes
so you don't have to deploy like an operator and other extra moving pieces. You can share and reuse advanced pipelines
with your entire organization using GitHub's approach. And also Alloy instances can discover
each other automatically and distribute workload gracefully.

