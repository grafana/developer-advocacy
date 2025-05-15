# GrafanaCON 2025 Keynote Livestream

This is the livestream recording of the GrafanaCON 2025 keynote, where we unveiled what's new in Grafana 12, including new ...

Published on 2025-05-07T17:16:08Z

URL: https://www.youtube.com/watch?v=JYVf-Z320Y0

Transcript: Please welcome to the stage, Grafana. Please welcome to the stage, Grafana
Labs co-founders, Raj, and Torkel. Hello everyone. My name's Raj and I'm the one of the
co-founders and the CEO at Grafana Labs. My name is Torkel Ödegaard, and,
I'm also a co-founder and I started the open source project in 2014. Amazing. It's great to be here in Seattle. This is our biggest and hopefully bestest
GrafanaCON yet — our 10th GrafanaCON. It's hard to believe that we've been
doing this and the open source project has existed now for over a decade. Who here has been to a previous
GrafanaCON anywhere in the world? That's pretty cool. Hard to see in the dark, but that
seems to be like, quite a few hands. So really, it's a pleasure
to welcome everyone here. We've got, almost, 600 people, and
a few thousands on the, live stream. We've got, I think a heck of a keynote. Lots of interesting announcements. And, let's get started. I'll find my clicker, which I
should have picked up earlier. There we go. All right. like I said, welcome. I wanted to get started by having a
quick conversation with my co-founder, Torkel since it's been over a decade. And, I guess the question, Torkel,
really simply is what keeps you excited about Grafana now that we've been
doing this for more than 10 years? Yeah. It's been a few years. In fact, I've been working on Grafana for
more than 11 years now, which is crazy. And to be honest, I keep
thinking sort of one more year, then Grafana is gonna be done. I'm gonna be done. It's gonna be perfect, and
then I find one year passes and there's still so much left to do. I still find there's so many
ways Grafana could be better, look better, be easier, do more. And then there's the fact that work in
Grafana has been and continues to be super rewarding, especially at events like
GrafanaCON where I get to meet and talk to users and see what the community has been
up to, a community that keeps on expanding and finding new ways, of using Grafana. But what also keeps me super excited
is the fun and impactful projects and teams with incredible engineers
I get to work with every day. I can't wait to show what we've
been working on and what's coming in Grafana 12 and beyond. We have some super cool demos
to show you today of a new Git integration that is in the works. Some new as code workflows, new
dynamic dashboard features, a new AI feature and much more. So that's what keeps me
excited after all these years. What about you? You've been at this for a while now. What keeps you excited these days? First of all, I have to say it's great
having a team and a co-founder that's so engaged and continues to be so engaged. I think, Torkel, it's pretty
amazing that, someone like you 10 years in is still so into Grafana. I'm gonna embarrass you a little bit,
like at the moment, still the number one contributor from a code perspective
to Grafana, if I'm not mistaken. Thank you very much. I had a few had years headstart. Yeah. Obviously, the team's a lot larger too,
and I guess you get to work on what you wanna work, which, which helps too. No, that's really cool. What I'm really excited about,
you started to touch on it, is —
We've built not just this incredible open
source project Grafana, but we've really built this, started to build this wider
ecosystem in open source at Grafana Labs. And when we first started the company,
I think we had this vision that open source was going to radically
change the observability space. And it's just really cool to see how
we as a company and as a team have had a big hand in that transformation
over the last decade, right? Not just with our own projects like,
Grafana and Loki and Mimir, but also parts participating in other parts of the open
source ecosystem like Prometheus and OTel. So it's really satisfying
for me to sit back and. realize that we've become like a force
in open source observability, but we've done it as part of this wider
community and wider ecosystem, right? And we really believe and continue
to believe that open source is gonna win, and it's ultimately
the best way to develop software. So I'm really proud that the team gets to
work on, open source software every day. And obviously we have our commercial
software too, but, we're primarily doing a lot of work out in the open, and
you can see some of these stats here. We've become a top 50 ranking organization
in GitHub, across all our projects. And speaking of ecosystem, I'm
also really proud and enamored and excited about the growth that we're
seeing in our Grafana Champions program, almost a three X growth. And these are community members who are
really passionate, not just about Grafana, but across the wider open source projects
that we develop and the wider ecosystem. They've become trusted voices in
the community, providing feedback, supporting other users, and really
helping the wider user base, whether you're a new user or an advanced user. Really wanted to thank
all the Grafana champions. You can see their names here
on this slide and this slide. And, they really help pull that
community together, and I think that's a sign of a really healthy ecosystem. So thank you to all our
Grafana Champions too. Thanks. All right, so every year we have
a tradition, and this year is no different, where we take a look at some
of our favorite dashboards from the last year that we've seen in the wild. And the cool thing about Grafana is
you can do anything with it, right? You can visualize any data from
so many different data sources for all sorts of use cases. And so here's our pick
of some of our favorites. Most interesting, most strange,
most inspiring, most bewildering dashboards from the last year. So we've seen Grafana used at Wimbledon,
in Major League baseball games. We saw it in the Tour de
France and in F1 races. And this last year we're
adding two new sporting events. We spotted Grafana in the command
center for the Sail GP boat race. It's an international sailing competition
featuring high performance catamarans in races that take place around the world. And speaking of sports, if,
for all the college hoops fans out there, that's, basketball. In case you didn't know, one
of our Grafanistas built a dashboard for March Madness. And this included live bracket,
live stats during the games. I'm not a huge basketball
fan, I'll be honest. This stuff's pretty meaningless to me. But the dashboard looks really cool. If you want to check it out though,
there's a QR code here, and we actually have this live on Grafana Play. And, again, one of our own
Grafanistas developed this and feel free to play around with it. Pretty cool. And using a variety of visualizations. So moving on from sports, we spotted
Grafana in a documentary about monitoring volcanoes in Italy. So I think of it as volcano observability,
not a use case I imagined for Grafana. when I started it out. But anyway, in the Vesuvius Observatory
in Naples, they're are monitoring Vesuvius as well as other volcanoes in
the region, 24-7 And Grafana was being used to help visualize some of the
sensor data coming from their seismic sensor network, which is pretty cool. And so this one's from Microsoft. Now, Microsoft's been a great
partner for Grafana and Grafana Labs. We've worked together to launch
the Azure Managed Grafana Service. They're working to use Grafana as the
defacto visualization for Azure Monitor. And they've really been a friend of
Grafana and Grafana Labs, but we recently found that they were using Grafana
for something pretty far out there. So this is all about
quantum computing, right? So depending on your perspective,
this could either be the great hope or the great hype of our lifetimes. It could maybe enable world-changing
abilities or it could destroy Bitcoin and cryptography or both. But, the Microsoft team has been
working on this new processor called, Majorana, and it's designed
from an entirely new material, and it has the potential to scale to
millions of qubits on a single chip. And so enamored that Microsoft
is using Grafana to support the development of this new processor. This isn't anything you can buy
or is coming to the market soon. Don't get too excited, yet and,
keep your Bitcoin for now maybe. Alright, so next up, we have one of the
most beautiful dashboards I've seen. It was created by Arpan Ghosh, who
wrote a Python script to fetch Garmin health and activity data, which it
then saves into an InfluxDB database. He then built this dashboard
to monitor and track long-term health and activity trends. So from the activity of your
health to the activity of the surrounding airplanes in your area. A Redditor recently developed a
Grafana dashboard that combined weather information with ADS-B information. So A DSB is the signal that every airplane
that's flying in the United States. Has to emit by law. I believe this law changed
about five years ago. This is the same signals that people
have been using to track Taylor Swift's planes and Elon Musk's planes. I'm sure you've seen that all on the news,
but this Grafana user is using ADS-B. He's actually got an ADS-B receiver
outside his window and he can track with confidence all the airplanes in his area
and correlate that with the weather. Pretty cool. So we have seen Grafana used
a lot by the space industry. We have seen it used by SpaceX, by NASA,
and at GrafanaCON last year, we heard and saw how the Japanese Space Agency
used Grafana to monitor their lunar lander as it kinda was journeying across
to the moon and to the lunar surface. And this year we've seen a satellite
startup company based in, Bangalore, India use Grafana, in their command
center in a launch in January. We also saw a Hungarian, company
called Puli, used Grafana to monitor their Athena lunar probe as it
was descending and touching down near the moon's southern pole. This was part of the
Intuitive Machines launch. And finally, Grafana dashboards
were used to monitor the landing and two week operations on the
lunar surface for Firefly Aerospace. Blue Ghost Mission 1, the first fully
successful commercial lunar landing. And we have Jesus Charles, the
Blue Ghost Mission Flight Director speaking at GrafanaCON later today. That's super cool. I'm always a fan of seeing Grafana
in space, Torkel, it seems like we've got that niche cut out. Maybe there'll have to be
a Grafana Galactic edition. Yeah. One of these days. But no, we know what everyone's
here to see during the keynote, obviously the Grafana 12 release. I did just want to hat tip to some of the
exciting things we're gonna be hitting everyone with during this keynote. We're gonna be talking about
observability as code, some of the investments in OpenTelemetry. We've also got some paradigm
shifting, UI changes, and experience changes with Drilldown
that we're excited to talk about. And of course, no conference
could be complete in 2025 without some serious noise and some
really exciting stuff in AI. So that's something we're
really excited to share soon. Stay tuned, strap in and thank you so
much for joining us at GrafanaCON 2025. See you soon. And I meant to introduce our
global director of engineering for Grafana, David Kaltschmidt. Alright, thank you. Alright. Happy to be here. Let's talk about Grafana 12. It's available to download at Grafana.com,
but if you've been on Grafana Cloud already, you might have had access to some
of those features already over the year. But Grafana 12 also is the sum of the
work that we really put into Grafana, and we've got really some exciting
stuff today but I'm only gonna cover really a handful of those features,
but there's gonna be a full deep dive tomorrow at 9:00 AM, so let's get started. UI performance. Grafana 12 got a major speed up. So I run the Grafana team now, but back
when they still let me contribute code, I wrote the first edition of the
logs panel and I'm happy to report that the team now has thrown this
out and they've rebuilt this from the ground up and it's super fast. They did the same with the
table panel and is now, silky smooth with scrolling as well. What's more important than speed? Themes. So for Grafana 12, we're shipping
five new experimental themes, and they are not just for looks. We have been investing into
making the UI more accessible. And so among those five themes
is an additional light theme and a high contrast dark theme. And so my favorite is Tron, I think
it's showing right now, which is a new, which is a new sci-fi, sci-fi theme. Alright, next up, data sources. Grafana's superpower really is to bring
together data from various sources. And so we call this the big
tent, but we have try to go bit beyond time series and logs. So these new data sources help you
also get better understanding of the data of your infrastructure
directly via data sources like drone. Al or Netlify, but we also wanna bring
you observability to your business processes with sources like Zendesk. And ultimately, we want you to be
able to ask, is my infra healthy? Is my team productive? Is finally, how is my business doing? So we've got all this data, right? So let's talk about dashboards. Dashboards really is our bread and
butter, and we've also seen some amazing dashboards earlier today. But if you've noticed over
time that the dashboards just getting more and more complex. And so I don't know about you,
but I've never seen a dashboard become simpler over time. People just keep adding things, right? So 12, we have been working on a set of
features that hopefully, fundamentally change the way that you build dashboards. So the first one is auto grid. And so auto grid lines up
your panels instantly to a clean and responsive layout. You can specify how many panels you
want in a row, how tall the panel should be, and Gana takes care of the rest. And so this is fully responsive,
so you can resize your browser window and Gana knows what to do. Conditional rendering also got an upgrade. The show and hide rules now
react to template variables. And this example, we're hiding a whole row
if the database engine name equals SQLite. I think this is really powerful. This makes your dashboards not
just cleaner, but also faster. So in this third feature is my
favorite one, it's tabs layout. Grafana 12 brings you a tab layout
that helps you organize your dashboard at the top of the page. And so this new layout engine. Supports nesting. So you can also place tabs
inside of rows as it's shown now. But remember, we're still
working on this so you might have to turn on a feature flag. But we love your feedback and I
truly believe this will change how you build dashboards. Alright, let's talk about
another power feature. SQL expressions. So Grafana's dashboards already make
it possible to combine data, but now we're making it easier to also
transform and manipulate this data coming from those various sources. And this is what this
looks like in a product. You add a query and you select
expression and you start writing SQL to refer to data from the other queries. And imagine what this could enable, right? No more ETL pipelines, no funneling
data into a central data lake. So you can simply use the language
that your analysts already know sql. And the best thing is this
also supports alerting. And so here's one of my
favorite use cases for this. This panel is titled For
Which Customers Is Broken. It combines error logs from Loki
customer Data from BigQuery. And when things break makes it
really easy for your support team to spot who to engage with first. So whether it's joining Time series with
business data or just reshaping lock data, SQL expressions, or making Grafana even
more powerful single pane of glass, so fewer ETL pipelines, fewer data lakes,
this is an absolute power feature. Alright, and for this next
section, I have to apologize. So who here remembers the
old built-in alerting? I've definitely used, it has this
nice handle for the threshold, right? But we needed something more scalable and
we introduced Prometheus based alerting, which was more scalable, more powerful. And then who year was frustrated that
we had two alerting solutions then? So I definitely was, fi we have a third one, but time has progressed, right? And we are working hard to
really make this the only one. And we've, for on at 12, we're
also shipping a migration tool to get all these old alerting rules
onto the new alerting system. And for some of our cloud customers,
we've already successfully migrated tens of thousands of rules. What's really cool about this thing is it
allows you to see if the, new rules are working before you remove the old worlds. Last one. So it's really important, or what's
really hard to overstate how important this is, and you probably can't tell
or excited I am 'cause I'm German. But, the story here starts in 2014 and
the Grafana project was barely a couple months ago, right? So this was 10 years ago, right? Someone already started wondering,
of these dashboards, like how can I manage them programmatically? And yes, we added the HTTP
API and provisioning, but both of these had drawbacks. And more importantly, you couldn't
create dashboards programmatically because there was no schema. So we also couldn't validate them, right? And so this same person, Jaime, realized,
however, what we came up with, it had to be somehow also, recommended. There had to be an official
way to do this, right? So 10 years on, Jaime. If you're watching this,
we've got something for you. So we're introducing versioned
APIs for all actions on dashboards. It took really a major architectural
change of qana, and most importantly, we're publishing version schemas now. And so this allows the creation
and the validation of dashboards and these new APIs and schemas are
enabling a very exciting use case that I'd like to share with you today. And for this, I'd like
to welcome Ryan McKinley. All right. Hey, I'm Ryan McKinley. I'm actually gonna go back one slide. 'cause. I do wanna make sure that we know
that this is really important. It may seem underwhelming, but
we're now working with versioned consistent APIs with schemas
for dashboards, and that's huge. Any sane as code solution will depend on
that, but we're not gonna talk about that. Oops. There we go. There we go. We're not gonna talk about that today. what I want to show you is using,
Git to manage your dashboards. And I think many of us have
figured out solutions for that. It's a little cumbersome. You're copying JSON from the UI,
pasting it here, whole set of tools, but let's all pray to the demo
gremlins and see if we can switch over to my computer, see what happens. Oh, there we go. Okay, so we've got a
new, a new feature out. This is Git provisioning. It's a little, early in the development
process, but it's really important to, to show you where we're going with this. So what I have locally is
just a very simple, dashboard set up a few data sources. Here's some, dashboards. Great. So I wanna show you moving
all of those into Git. So pretty set simple setup here. The most complicated thing is
figuring out your access tokens. I've saved a few here, so
I'm just gonna play that. There we go. So this is pointing it to
a new empty repository. This then reads what I have locally,
where the external storage is, and I'm gonna synchronize everything. I'd like to include all of the
history along with that, and let's see what happens here. Great. So it went through it. Read what I have. We've now written that into Git. I'm gonna enable all of the features
we've got here and let's see what happens. So my Grafana instance, let's see, if I look at the history, you
can see all my effort to prepare this. We got some effort from
Roberto and Dominic. So the full history, all the
dashboards is now in Git. here we go. Same dashboards here. Let's go back to, this guy, local host. There we go. So I've got a dashboard here and
let's make some changes to it. So here we go. colors. Maybe let's try spectral. It's a nice color scheme. So I'm gonna save that. And now when I save it, I've got new
options because it's now managed by Git. So we will save that. And what you'll see is we're
viewing this, it's not actually saved in our Grafana database. I'm gonna open a poll request,
create poll request here. And so now we haven't
saved that in Grafana. We've saved it in Git. but we have an agent running in
the background that's gonna show me the difference between what
I've saved and what's coming soon. 'cause again, as we all know, we
can look at the JSON, but that's really hard to tell what's happening. So from these previews, I can open
up, see these dashboards directly. So now let's go back and actually, get.... so from our pull request, we
can go ahead and merge it. Merge, poll, request, confirm, merge. And now back in Grafana, I should have my, oh, that classic error. Let's see. Here we go. Oh man. so we can see here. We'll try this one. This one I will edit
directly and do, let's see. Let's change, let's change
this one, the state timeline. We can change it to a heat map. And again, I'll save. Alternatively, we can
push directly to Main. So I'm gonna save. And same thing this time we wrote
directly into, into Git, but from Git. So that was my temperature value here. I can edit this directly. So let's see. I'll change the name. And where have we got the name here? Title, that's again,
temperature edited from GitHub. Let's commit that. We'll just go again straight
to main and coming back here. I'll reload. What this is awesome. this is really the greatest. "I'm still impressed!" You're
still impressed, I swear it works. The demo gremlins are, I swear. What we have is a method that
we're writing, from the UI into Git back into our database. And alternatively, you can write from, straight into Git and we synchronize
back into Grafana, but we all know that's a little dangerous, right? So when we go through our APIs, we
do validate them before we write them, but if you write to Git there's
all kinds of ways of doing that. So that's really flexible. So many of us are gonna want
some, helper tools for that. So we have got a new tool that we're releasing,
it's command line manipulation that talks to our APIs. So this is grafanactl and it knows about
the set of versioned APIs we have and can do all the basic crowd operations. So this guy, I'm gonna do
just a grafanactl resources, get dashboards and dashboard. No whammies. Always good. Always good. Oops, get sorry, pull. I think something weird with network,
but so we go, we can pull resources, edit them, and then push them back. So it's really, it's, based
on, it's modeled after, the Git commands, but it allows
you to edit those while having validation that happens locally
backed by the dynamic APIs. In addition to that, there
are people who want Terraform. So we've got a new Terraform provider
that's reading again, the dynamic APIs registered in the API server. And we set this up and I can do, let's see, Terraform apply auto approve,
and we'll see in my Grafana instance. I should now have a new folder
with multiple dashboards, managed from, Terraform. Again, all of these things all work
at the same time, and when that doesn't work, we can also use, that
one did work, so I'm proud there. so we'll do, let's see. You can always do curl, gonna
always fall back to curl. So in this one we can replace a tag
with a generic, JSON patch command and great, the server rejected my request. This is awesome. but you get the idea. it's, so we're going to switch
back to the slides. and so all of everything I showed
you is all based on dashboards. but the reality is all of the
foundation is coming from these dynamically registered APIs. So currently we're doing
dashboards and folders. Soon it will be all data sources,
alert rules, contact points, all of the observability resources
that you wanna deal with. this is the power of schemas. I've been calling evangelizing
schemas recently, but my new friend Ted, has talked about semantic
conventions for quite a while. So proud to talk to, to welcome him. Thank you. Hello? Hello. Hello. Yes, I am indeed Ted Young. I am one of the co-founders of
the OpenTelemetry Project, and I recently joined Grafana Labs. And I just have to say it is so
amazing to be at a place that understands open source so deeply. I've been working on observability
for about eight years, but I've been working on open source
software for closer to 20 years. And one conversation that gets really
tiresome of having over and over again is having to explain some of
the fundamental value of open source and how it aligns with what everyone
else is doing at the organization. So to be at a place where open source
is embedded so deeply into everything everyone is doing is such a relief. It's such a supportive place. And I'm just so happy to be here. But when we're talking about supporting
open source, we're not talking about any project, we're talking about one project
in particular, and that's OpenTelemetry. But before I dive into the ways that
we, before I dive into the ways that we support OpenTelemetry, I'd like to
take a step back and talk about why we think the project is so important. I'll give you three reasons. The first reason is
OpenTelemetry is vendor neutral. Vendor neutral is an interesting term. It doesn't just mean open source. It also means widely adopted across
the industry, and that's really important because when you're standing
up observability, one of the heaviest lifts is adding all the instrumentation
to all of your applications, services, and infrastructure. That can be a lot of work, and if you
have to rip and replace all of that instrumentation every single time you want
to try a different observability tool, we don't think that's really acceptable. We think you should write once,
run Everywhere, and we believe that OpenTelemetry is the tool
that provides that feature. The another thing that's pretty boring,
but also really important is standardizing the data coming out of your system. In OpenTelemetry, we call this Semantic
Conventions, but what it basically means that if we're reporting an HTTP request,
it's always reported the same way, whether it's coming from a Java service
or Python application or Kubernetes. HTTP should always look like HTTP. Same thing for SQL and everything else. It should be very, regularized, and this
is really, helpful with just about any task you're doing downstream, whether
you're making dashboards or using AI to find correlations across your system. Being able to predict what
the data is going to look like is a really valuable feature. The third thing is something I don't
think we talk about enough, and that's the way that OpenTelemetry unifies all
of these different signals together. Traditionally tracing metrics and logs
and now profiling we're all separate tools and they had completely separate stacks
and they were siloed from each other. That made it hard to move across
all of these different data systems. OpenTelemetry doesn't just take
those different signals and stack them next to each other. It actually integrates all of that
information into a single graph. And that, again, is very, valuable
when you're building observability tools, especially tools that wanna
integrate all of this information and synthesize a wider view of your system. Okay, so that's why we're interested
in OpenTelemetry, but what are we actually doing about it? And there's a number of things
we've done this year that we think are really important. First and foremost, we are
donating Beyla to OpenTelemetry. Beyla is a form of auto instrumentation. Remember earlier I was talking
about what a big lift it might be at an organization to add
instrumentation to all of your software. If you have a large fleet of surface
services, that can be really ones. So any kind of shortcut you can take
there is gonna be really helpful. Beyla provides auto instrumentation for
a variety of different languages and it does it using eBPF, which means if
you're using any kind of modern Linux operating system, it's readily available. We're excited to have this as part of
OpenTelemetry because Standard Data, we'd like it to be the case where whether
it's auto instrumentation or manual instrumentation, the data looks the same. And we're also interested in
Unified Telemetry, in particular, combining eBPF with Profiling. Another place where we support
OpenTelemetry really heavily. It's nascent within OpenTelemetry. It's not ready yet, but we're really
excited to see pro profiling take flight. This is a really, valuable form
of observability, but one that's traditionally been somewhat
underutilized because it's been a little hard to understand how you would
actually deploy this in production. So we tend to use it mostly in
development, but when you attach it to the rest of the OpenTelemetry tool chain,
a lot of exciting ideas become possible when it comes to running, always on
profiling or spot checking your system. So we're really excited
to see where this goes. Another place where we support
OpenTelemetry is Prometheus. What, these are two separate tools,
but they're both within the CNCF and they're both really popular. And when we look at our users, we
actually see lots of people using both of these projects together. so we would like them to work
well together, and we think Grafana Labs is actually uniquely
positioned to make that happen. So anywhere within the OpenTelemetry
project where it's possible to, supply high quality Prometheus
support, we're trying to do that. One place where we're doing that is
in a project we call Grafana Alloy. So Alloy is our version of
the OpenTelemetry Collector. So it works just like a collector,
but it has a bunch of other features that we think are really valuable. One in particular is high
performance Prometheus pipelines. So the Collector is a really good
Swiss Army knife for converting data formats and massaging all kinds of data. But if it's Prometheus in and Prometheus
out, you don't actually want to do any of those data format conversions. That's just cost essentially
in that situation, you want high performance pipelines. So Alloy takes both of these
things, combines them together into one awesome system. Last is certainly not least, a lot of the
day-to-day work in OpenTelemetry goes on in the language SDKs, the implementations
in all the different languages, the clients, the instrumentation packages. That's quite a bit of effort, keeping all
of that up and running and maintained. And we try to push in as much as we can
in as many different languages as we can and help support the project in general. So I would love to bring everyone up on
stage who's committed to OpenTelemetry and thank them individually,
but because I can't do that. I'd like to do this instead. This is a slide with all of my
favorite people at Grafana Labs. This is everyone who's committed
to the OpenTelemetry Project. We value you so much on the
OpenTelemetry side of the fence. We really appreciate all of the work
you all have put into the project. Yeah, absolutely. Hells yeah. Okay. it's not just, within the project
where we support OpenTelemetry, though it's also downstream in all
of the databases and analysis tools that we provide at Grafana Labs. We want all of this tooling to
be open to telemetry native. So when you look at the data,
we want Grafana Labs to be the best place to go and do that. and that's really important
because we see the future of observability as an integrated system. I. It's not the case that
you have a logging problem. So you look at your logs or
you have a metrics problem and you look at your metrics. You have a system problem, and
you're moving across all of these different signals to understand
what the heck is actually going on. And we believe that an integrated
solution is how you do that. And so we're building integrated
tools here at Grafana Labs. And to Drilldown into that more
deeply, I would like to invite Andrew Stuckey onto the stage. Thanks, Ted. Hi everyone. I'm here to give you an exciting update
on the Grafana Drilldown applications. A quick reminder about what the
Drilldown applications stand for. First and foremost, these are
queryless, point and click experiences. No queries required. We tailored each experience
to their database counterpart. The Drilldown spark was lit by a
hackathon last March, last GrafanaCON in 2024, we announced Metrics and Logs
Drilldown, and in ObservabilityCON in September, we rolled out a preview of
the Drilldown suite, which included Traces and Profiles Drilldown. Over the last 12 months, we've experienced
a 600% growth in monthly page views. Drilldown has been a wild success. Let's briefly go back to the
beginning with Metrics Drilldown. Since last showing Metrics
Drilldown, some things have changed. I'm gonna walk you through those changes
by looking at a real world example. But first, we wanted to address some
feedback we heard from the community. Finding the right metric among a sea
of metrics was still challenging. Let's look at a DDoS attack on an
authentication microservice through the lens of Metrics Drilldown. First, we have a new sidebar, which
rapidly helps reduce the sea of metrics. Looking at the sidebar, we see that we can
use metric name prefix filters among other filters to narrow down our result set. Let's select the HTTP prefix filter. With just one click, we reduce the
sea of metrics from 313 to just three. Immediately we spot an
anomaly, a spike in traffic. We are convinced this new workflow will
help you wrangle the chaos and Prometheus environments with lots of metrics. Logs drilldown provides the same
Drilldown experience, but for logs. We've been hard at work, improving the
logs Drilldown experience like adding support for JSON logs, a new logs panel,
and various performance improvements. Stay tuned for upcoming
updates later this year. Now let's talk a little
bit about Traces Drilldown. We built traces Drilldown to help you
pinpoint where issues are occurring within large distributed systems. With that said, I'd like to
officially announce the general availability of Traces Drilldown. Woo. Let's look closer at Traces
Drilldown and come back to our authentication microservice. This time a user has reported
trouble logging in with multi-factor authentication. I wanna show off the service structure
tab just one of the many ways in which you can break down your data. This feature aggregates spans across
multiple traces, which quickly highlights recurring trends in our case. I see something interesting,
a longer running notification request, so I'll dig in. Digging further into these span
details, we see that the send SMS notification request is the culprit. If we expand into the span and
look at its attributes, we see that our upstream notification service
is rate limiting in our request. This was our issue. Finally, let's talk
about Profiles Drilldown. We've historically thought a lot about
profiles from the perspective of cost savings, performance improvements, but
we wanted profiles to be so much more. We built Profiles Drilldown to be a
place for multiple use cases, including using profiles for root cause analysis. With that said, I'd also
like to announce the general availability of Profiles Drilldown. Our poor old authentication
service has yet another issue. Users this time are reporting a
slow login after the deployment of a new version of our service. After selecting our service, let's
look at the available labels here to help drill into our issue. Very conveniently, we
have a version label. Selecting the version label allows
us to compare performance between the different versions we've deployed. Comparing the baseline versus
the new version, there are some pretty clear differences here, so
let's look a little closer at the flame graph to understand more. Looking more closely at the flame graph,
we see that we added a new password hashing library called Argon two. This library was causing our slowdown. Okay, I have one more thing... i'd like to announce. A new Drilldown feature
called Investigations. Investigations allows you to move
between Drilldown app and Drilldown app and collect the signals. You can find investigations
in the menu bar. To get started, add a panel from Drilldown
or click to create an investigation. From here, we'll find a panel of interest. Click the context menu
and add to investigation. You can now add comments or continue
your investigation by collecting panels in other Drilldown applications. This powerful new experience
brings the context from all your telemetry signals into one place. If you think this was interesting,
wait until what you have to hear from Mat and Cyril. Thanks, everybody. Hello. Hello everybody. Thank you. my name's Mat Ryer and
my name is Cyril Tovena. I asked the marketing department
to come up with a slide that expresses AI is everywhere, and
they came up with this monstrosity. Graifainai?? That looks like an LLM generated
in an image, doesn't it? We're so worried about AI taking our jobs. They're taking an AI's job there. but who? AI is everywhere. Who uses AI in their work? Yeah. So there's a lot of people. Who uses the AI that is agentic
and really tightly integrated into the tools, like work, like
cursor, warp, those kinds of tools. Yeah. And we, use these two. We noticed that this
makes a big difference. Like ChatGPT I think
was a big kind of step. And this is another one. It felt like another. A kind of major leap here, having the
integrated experience and favorites of ours are the warp terminal. So in the command line you can
still type commands, but you can also write just in plain language
and it will generate commands. It will look at the response from a
tool that runs, and so it can iterate. And cursor has the same kind of thing. It goes further because it
shows you a diff of changes. So you can see what it's suggesting
and then you're free to accept it or not, or keep the conversation
going and iterate on it. And we've noticed a big productivity
boost with these kinds of tools. And we thought, what if
Grafana had this capability? What would that look like and
what, could you do with it? It goes beyond just AI chat. This is, when we give access
to your data, suddenly it's not just answering generally. It's specific. It's able to look at your real telemetry
data and work with it and iterate with it. If it's this reactive agent
thing, you get the feedback. It can run investigations, so it can have
it dig in for you and poke around, and you don't have all the knowledge always. Sometimes it has more knowledge than
you in certain places, and sometimes you are the one that has the knowledge. So you work together in this integrated
way, and we're really excited, I can't wait to show you this. So thoughts and prayers. We're gonna do a live demo now. I'm just kidding. I'm a demo atheist, so I'm on my own here. Let's switch to the, okay, we are here. Yeah, let's go. yeah, let's go. The assistant can be opened on
the top right corner of the new icon and it opens as a sidebar. So it's always with you, always available
to help you on your observability journey. It knows about the page where you are. So we can see here that it's
talking about the OnPage. So he knows about this and it
can use that context to give you information about the page. Alright, let's ask our first question. So I'm gonna ask, show me
the CPU usage, per part. So the assistant is equipped with a lot of
tools around Grafana and it can use them to help you find metrics, query metrics,
and then answer the question that you ask. So right now it's is doing that,
it is actually looking for metrics, related to CPU if found one. and I is gonna actually do a query. Yeah, and notice it's gonna use
Grafana visualizations wherever it can. So it's not just a wall of text, it's
actually going to use the Grafana tools and all the beautiful stuff
that people have already built to be part of that conversation with you. And it can navigate too. So it's just moved us to this new page,
so it knows where Grafana, like it knows how to build URLs and deep links straight
into the relevant bits for you to see. So it's the fastest way ever of
jumping to the right specific bit. And I can use that if I want
to start iterating on the corridor I'm building right now. I don't know if you see that here,
but it is giving us also a summary. So it is actually looking at the data too. So it's telling us, what is the
current CPU usage of the pods, and give us a quick summary, to
quickly have some more information. So let's ask a second question. and this time I'm gonna ask a bit more. So how many nodes are we running
in this cluster and which kubernetes version is this? Alright. And by the way, the assistant won't
be this big when you have it on yours. It depends on your monitor size. This is the biggest I've ever seen it. I'm loving it. So yeah, we have these, these great
kind of tools that you can do. And the thing is, like with LLMs, how
do you know they're not hallucinating? This is the big trouble is
like, how do we know that it's for sure telling us the truth? Our answer to that is that we show all
the working so you can see everything. It's doing all the tools, it's making
the inputs and outputs of those tools so that you can see where it's going.. If
it goes wrong, you can understand why, but actually it just gives you trust
that it's following a logical step and it hallucinates less as well because of this. So it gave us with the answer,
so we're using kubernetes 1.30. It's a EKS cluster. It actually went a bit beyond and
gave us more information using the metrics that he pulled out. so it's telling us about the
availability, the container D version. We're using like the candle version. very insightful information. Yeah. Now we haven't pre, this
isn't a pre-baked demo. This is a fresh install. and it's just answering these questions
by making these different queries. We actually introduced a Postgres
connection error into this instance. So maybe a product manager doesn't know
what that means technically, but they might say, customers are telling me the
product catalog service is not working. It's struggling. Something's gone wrong. Help me. Yeah, and this time I'm gonna select
two data sources so that you can actually use both logs and metrics. The context here, those pills
that you can see and is actually suggesting me, the promises one. So it's, muted and I can click
on it and it's gonna, it's gonna use that in the context. And as with ai, more context is better. So you can add different type of context. You can add, data source as you see. You can add labels, names, labels, value. You can actually use
metrics or dashboards. you can use the menu, but also use the
in chat context by using the at mention. So it's running the
investigation, right now. And because that's gonna be a
long investigation, I think. In the meantime, I want to show you
something that is pretty interesting. The chats, all the chats are
automatically titled for you. So this one is called,
Product Catalog Service Issue. And I can look at the past conversation
and they run in the background. So if I switch, this one's still
gonna be running, so I could actually use multiple investigations at the
same time if there's an incident. So let's look at this one. So this has information that's
packed in, and this has a sort of general knowledge, that, it's got
general observability knowledge. Grafana has an advantage here
because it's all open source. The LLMs kind of already have a
good intuition about how to use Grafana tech and all the open source
things around it in the ecosystem. But we've also added specific Grafana
knowledge and prompts and things to, and access to docs and things so that
you get really like proper Grafana knowledge baked into this as well. Let's go back to investigation. We can see that it's actually,
it just actually moved us to something, to another page. So let's see what it's saying. Oh, it made some mistake
along the way, by the way. Yeah, so this is, interesting. You can see one of the
tools just failed there. When there's an error, we feed
that back into the conversation. So the agent has a chance to look
at what it's done, realize it's made a mistake, and correct it. So you get this kind of
self-correcting thing. If you use Cursor and some of those
other tools, you'll see you'll probably be used to this kind of interaction. It's not perfect, but you
are there to help guide it. And the visual, seeing
the graphs is great. Like having, answers not
just a wall of text, but just these gorgeous visualizations. I think it's just icing
on the cake, right? So we find that the problem database
connection exhaustion is giving us like key finding, telling us
about the root cause and give us also some recommended action, on
how to try to mitigate this issue. And at the same time, it moved us
to, Drilldown, metrics to show us a, metrics that shows the problems. Basically fa failed requests here. Yeah. So it's really helping us there. I made a Postgres
dashboard last week, Cyril. You did? So can you see if you can,
if the agent can find that? Yeah. Because that also would
be helpful in this case. So if you know what you're looking
for and you've got your knowledge, you can also just ask specifically
in more pinpointed questions. Yeah. And again, it is gonna use like tools that
it asked from Grafana to search dashboard and try to come up with an answer. So there's two of them and he is
suggesting us to, go to the, new ones. I'm gonna say yes, I was promised no French. yes. So that's cool, right? If there's any ambiguity,
it comes back to you to ask. So it's this, it is conversation. Right, nice dashboard, Mat,
but sounds like there's one panel that is not working. What? Oh, that's embarrassing. Can you it get it to fix it? Yeah. I'm gonna ask the assistant. Fix the database size panel. I'm actually also gonna ask to
change all the colors of the panel at the same time just to showcase
how we can bulk update a panel. Oh yeah. And you don't have to be a hundred
percent perfect in what you type. It's completely, it's the
LLM, it's already very flexible, knows what you mean. So again, it's gonna use the
tool, so it's reading the, panel. I'm a bit wired that is already trying to
validate cos because it should be trying to look at oh, actually managed to fix it. Wow. That's actually the fastest it's done. That, yeah, that's fast. So it read the panel, it figured
out what the mistake was. It's fixed it, also can just
make bulk edits like this. I think this is gonna be a real sort
of superpower for anyone working with dashboards, or any of the Grafana tech. Really exciting. That's the demo. Back to the slides. Thank you. Oh, there's another part of the demo. Maybe we can. Pardon? We could show the dashboard creation. Show the dashboard what? Dashboard creation. Oh, yeah. Shall we? Yeah. Okay. Back to the demo. It's going so well, it's going so well. All right. So we can edit, yeah, we can edit, we
can fix, we can do bulk things, but can we create dashboards out of thin air? Yes. It's correct. Yeah. Spoiler alert. let's see. To be honest, this demo, every
time we do it is different. Yeah. So we are scared. Create a dashboard for monitoring Kafka. So it knows what Kafka is. It's got the general knowledge. You don't have to tell it everything. And it's also gonna
look at best practices. What makes sense to show on a
dashboard, with five panels. So is this doing the same? This time is actually going
for multiple type of metric. So it's looking for JVM metrics, it's
looking for Kafka metric general metrics. So it did free call to find those metrics. Can you open one of these tools so we
can look at the inputs/outputs in there? Yep. So he just created the dashboard, so
that's the response from the tool. So he looked at Kafka topic, all
the Kafka topic metric patterns, and then the Kafka server patterns. Yeah. Get your hands ready because
if this works, we've, we have to raise the roof here. It's created the dashboard. Yeah. you also can give feedback at the bottom. What? Thank you. Look at the detail in this, the. The units. It's got there, it's got titles,
everything's labeled nicely. Descriptions. Yeah, it's got a description. It looks nice. Chooses the right visualization. It tries to, if you're not happy with
any of this, you just keep chatting. You just say, nah, I don't know. Can you make them all purple please? Maybe we should just
turn that on by default. Actually, just make it purple. So it's cool, isn't it? This time? That's it. And that is the end of the demo now. Thank you. So there you have it. You know, Grafana assistant lets you
ask questions, high level questions. Our CTO uses it. Our CEO uses it to ask, learn about the,
the information about what we're doing, the stack, based on this telemetry data. If you know specifics, you're a
senior, SRE, you can be very specific. Context is everything. So the more you provide,
the better the results. It can take you places around Grafana,
it knows how to deep link into all the different interesting bits. So it can show you things
instead of just telling you. It can do investigations. It's reactive. It's this agentic thing that will dig
in and maybe it, it, does a query, finds a spike and drills into that. Or maybe there's no spike and
it moves on to something else. and of course you can make
changes, editing dashboards, fixing them and creating new ones. And we're so excited about this
project, like we've got so many ideas of more things we can do. Wasn't there an incident yesterday? Yeah. We had an incident and one of the
engineer was, using the assistant and he was able to find the root cause. It was amazing. Yeah. So we are using it internally and
we are just finding that this is actually really changing things. And so we can't wait for you to
get your hands on it as well. And that's it. So I'm now gonna hand over to the people
who make this conference possible. So please welcome Carl,
Mihaela, and RichiH! Cheers. Hello, my name is Carl Bergquist. I'm a senior principal engineer. I'm Mihaela Maior, a
director of engineering. And I'm RichiH, part of
the office of the CTO. So why are we here? What do co-chairs do? So we are responsible for selecting
the  content at this conference. We're also responsible for polishing
the content and we're responsible for the whole experience for the
community around all the content. So to recap what we seen today,
we released Grafana 12, with a lot of great improvements. Just look at this big screen. There's improvements all over it
from new dashboard capabilities to version APIs and schemas. Tomorrow morning, we'll have
a deep dive covering some of these Grafana 12 features. If you wanna sign up for the private
preview of Git Sync and Grafana CLI, you can scan this code, and
we'll reach out when it's ready. As you just saw, it's still early days,
but we really wanted to show because we're so excited about this and there's
no doubt that the observability as code solution we're building at Grafana
will change how we build, iterate, and collaborate on dashboards in the future. And any other resource in Grafana. As you just saw in the presentation
from Matt and Cyril, we're also working on the Grafana Assistant,
and you can scan this code if you on you want the private preview. You can also swing by to
ask the expert boot later. This is something the team started
working on just a few weeks ago and we're really impressed with the real
value it's been able to deliver.

