# The road to GrafanaCON + big news for GrafanaCON 2024! | Grafana

VP of Culture Matt Toback reflects on past GrafanaCONs while this year's co-chairs Carl Bergquist and Mihaela Maior share big ...

Published on 2024-01-11T19:11:15Z

URL: https://www.youtube.com/watch?v=VkeMkT29OW4

Transcript: GrafanaCons... When I think back, they’re
like these milestones. So the first one in Squarespace, one of the first times
that we see the community in person. Then we do the thing
on the aircraft carrier, right? And then it gets bigger and we’re in a real
theater and like, that feels incredible... and we go to Amsterdam and
we also like had this beautiful theater, and we have the
entire company on stage. Which we thought was incredible because then
we’re like, ‘look how big the stage is!’ Now I think about it and I'm like,
look how small that stage and is we all fit on it. And then, GrafanaCON L.A. we do...
those are those meaningful moments. I want to extend a warm welcome to everyone to
GrafanaCONline 2020, our first virtual GrafanaCON. We were looking forward to returning to
Amsterdam this year, but it wasn't to be. We're so excited to announce
the next GrafanaCON, which is our biggest
community event of the year. For the first time in five years,
we're going to meet in person, in Amsterdam, in April, and we can't wait for this. So, Carl, what are you most
excited about this year? So, this is a
big event for us. We're going to bring the whole open
source community together again, and this year it's not just going to be
about Grafana, the project, it's also going to be about all the open
source projects we have at Grafana Labs. So it's going to be a massive
big tent with a lot of different projects. The call-for-paper is now open, so if you have
any interesting or cool work that you want to show us regarding Grafana, its plugins,
any of the metric collectors, or anything about LGTM stack, please submit something to us,
and I hope to see you in Amsterdam. On top of that, if you have any dashboards
that you're really proud of, please apply to join
the Golden Grot Awards. If you win, not only will your
dashboards be presented on screen, but you'll get to join us in Amsterdam
and be part of the celebration. Please go to our website to sign up
if you want to be some of the first that get to register as a participant for the
conference and we can't wait to see you there. Good morning. Good afternoon. Good evening. First of all, I have to say it's a bit
strange to sit here presenting to you media and the living room,
but hopefully you'll find my presentation on the how to get an organization
to adopt this central telemetry solution. Interesting. And hopefully there's some nuggets of information
that you can take away. So as I said,
I hope the process of learning about how we built the central telemetry
part of the number of previous protocols, we have covered
a lot of the technical aspects. So today I will cover the non-technical
aspects of what we did to to drive the adoption of the platform. If you want more detail on a working as part of the graphic design,
a week's, you can hit me up on Slack. If you're watching later, please feel free
to reach out to me by email or share my email address
at the end of the presentation. So first of all, the most important part. Who am I? My name is Steve Sampson
and I've been a Bloomberg since 2003. The first 12 years
I spent as an application developer, a team leader and manager
for our Trading systems group. A lot of that time I actually wished
I had a telemetry platform. What I've been building
as part of being an infrastructure manager in a group called Production Visibility
for the last four years. So you are you are Bloomberg. Bloomberg was founded in 1981
by Mike Bloomberg. What you can see on my slide right now
is the Bloomberg terminal. The Bloomberg terminal is built up
of many different applications. We call it functions. So it's really over
10,000 different products that operate independently, yet share a lot of the
the core infrastructure, both from a from a from a data point of view
and also from just the core infrastructure. So what does the terminal deliver? The terminal deliver
real time market data. News and messages. Messaging being both email
and our chat product. On top of all this real time information,
we deliver analytics and so basically are a huge realtime
information aggregator that lets our subscribers take action to related to their financial decisions. Right. So who are our our users? Basically, anyone that wants to be involved
in the financial markets, it ranges from from investment banks
to hedge funds to government regulated national and central banks. And we deliver both features to individuals and also to enterprises. So enterprise functionality
for how our firm will operate to get around and be a major part
of the financial markets. We also have products that are on
and off the terminal, like our news product,
which is both TV, radio, magazine, web and mobile. So let's talk a bit
about the scale of this and sort of from a more technical
point of view. So first of all, we have about 325,000 subscribers around the world
and I said is a premium product. So it's all the important players in the world. We do about 120 billion pieces of market
data across the terminal every day. So this needs to be processed and distributed in real time
without the net buffering the way in
just about 2 million new stories. I just already mentioned some introduce
ourselves and others we take from a total of 125 approximately
25,000 servers around the world. We are
the largest financial social network in terms of that,
we process and send about a billion emails and instant Bloomberg chat messages, data. Through this we do. We do this by 20,000 employees in about
a quarter of these employees or something. So on the technical side,
we own and operate our major data centers on this
as the company was formed in 1981. VB We also have software running in those sites around the world
and on our clients PCs. So they really care about monitoring
anything from the clients PCs
and all the way back to our data centers. So it's a it's a rather large and broad set of things
that needs to be monitored. And interesting enough, I actually made
these slides a couple of months ago. So during the global pandemic, we seen quite different numbers
and sort of the market data has more of a doubled more or less overnight. So we now see regularly over 200 million with a peak of 240
billion pieces of of market data a day and our email and chat services
also almost doubled. So these are sort of
two of the leading indicators. So most of the the the low than the traffic on the platform
US has really, really doubled. So when I say central telemetry, what I mean by
so I mean basically an internal service provider for
every anything or everything telemetry. So metrics distributed trace log aggregation
visualization of the above, alarming of the above
and reporting on everything. So why, why do we produce it? What's the goal? The goal is obviously really
to give us one single pane of glass such that we can have a common standard
for the for the firm,
both when it comes to visualization of of our metrics and our metrics
and and how we monitor as well as sort of setting a firmwide standard for for for for rules and alarms such that the we know we know we've covered everything. So what what did we have before we started the central telemetry product,
we had a trimming endless amount of bespoke solutions
that were very single purpose that solved one on one problem, right? So you sort of jokingly said that the
the only thing they had in common is that they were all started
by an intern, unfortunately not the same intern, but they were probably
all started by name. So obviously this resulted in in a lot of things
like inconsistent naming conventions and persistent coverage and time
zones, inconsistent, you name it. But it was very,
very, very hard for anyone to debug something beyond their own system. And they had to go from one sort of monitoring
system to a different monitoring system. So it just became
it just made it really difficult for us to effectively debug through them many layers of of dependencies. So obviously it's also sort of quite obvious
that we need a central telemetry platform. So why would I want someone not want this central telemetry platform? So I don't plan to read out these excuses here because I don't really want
that to be the only thing you remember from my presentation. So but if there's an excuse out there,
we have probably heard it. So so what can we do in order
to get the people onto the platform? Right. This telling people to do it? Strong arming
doesn't necessarily always work. Right? So we had to take a sort of a quite measured and I wouldn't say novel approach,
but it's it's definitely some places where we really rethought of of things
a bit broader and that sort of we do the meat of the presentation
I'll get into into now so the yeah the first thing is probably also the most important right set the set the right goals like it probably should have been
if that's the right goal because it's only really one goal
that I think is important and we're all engineers
and we all like to build stuff. So starting to set goals
around the technical parts of the platform and how many message we need to handle
and all that sort of stuff probably drives
a lot of the wrong behavior. So we set one main goal. The main goal is that we are responsible for help
improving the stability of Bloomberg. We are not just building
at some of the telemetry platform. So what does this really sort of mean? It really helps us prioritize the work and really
look at the right things. Right like, say, we we have to make decisions around short term gains
and and how much the how much return we would get on any investment return
being improved, the reliability and investment of the time
spent on building it. So but everything we did
was really to drive stability and not to build a platform on building a complete product
like the sort of mentioned the product isn't just the platform that's
able to ingest and process all the data. The platform is a lot more,
especially when it comes to sort of internal products.
We quite often cut corners on some of these things,
but it's important not to. So having good documentation,
good self self-service tools provide, provide training and support and support. I think the sort of the most
important thing when it comes to support is really to be able
to provide a quick response. So what I mean by quick response is it's in our case,
the most important quick response is sort of a persistent chat room
we have internally. It actually has about
half of the engineers in it where you see
questions, scroll through all day. We we make sure that the people
that are on call for for the platform
also handles the support questions. Why is it important? Because a lot of times
building or instrumenting a code is something that people do
when they have a bit of spare time or they are waiting
for something, they are able to sort of finish off. And so if I could add
the other metrics at the end and if they struggle to get going and sort of have to start looking up something or post a question
that will take a day to answer, to get an answer, it's likely
that they will go back and do it. So it's very important for us to that
to sort of answer quick questions very quickly and sort of
make sure that people move forward and can can can continue instrumenting their code
and adding the right measurements. Right. And when you're building a platform,
it's important to have partnerships
and then sort of think about the the broader strategic
and the tactical partnerships. And I'll get get into that a bit later. And again, back to setting the right goal. Like whenever you get questions, make sure
that you answer them as a stability. Consult,
not just someone providing a service. Even someone might think they know
what questions, what they're asking
and what answer they want, and the asking and the right specific way. So teach people
to ask clarifying questions and really think of the best way
to solve the problem, not just on the answer,
the question that that that people might have. So obviously not all solutions
are what I mentioned earlier, sort of really these in turn build one off
solution. There are good solutions
and some some teams might even have third party systems that are using and that ultimately that you're hoping to replace. Right. So so we should look
at the current solutions that we should make sure
we ask the right questions. So don't get caught in terms of trying to figure out
what it would take to get the people that have a good platform to move over to your platform
and think about those things. Those are not the questions
you should ask. The questions you do rather ask sort of What did you do for us when you build or or started using this platform? What are you using the most? What functions
and what features you found most? You find most valuable? Trying to get this information
such as you can sort of get going on your own platform
and provide the valuable solutions to people that don't have something,
rather than try to target the people that have a lot
and try to get them to go just to get the extra last
final piece of their puzzle build bottom up. So this is not really so much
about building a sort of read more about what part of the infrastructure you sort of plan to build out first, right? Because as I mentioned,
we we have our own data centers and making sure that we provide
good monitoring for the for that
the physical layer and the data. So it means that we cover
a lot of our users. Not everyone is interested
in that library. So we're now giving something to everyone
and we sort of got a foot in with every single team, even before we have sort of
even talked about talk to them about instrumenting the code
or adding their application level metrics. Right? So figure out how you can give a lot of a little value to a lot of people
and a lot of value to them, probably to most people in this case, to consider the different audiences. There's a lot of different users off of your platform, right? And this is sort of really
where the partnerships come back in with. I mentioned that idea, right? So I think consider different audiences. It's really all about how we use help
drive adoption short term and long term and how that will impact the the overall stability
of of the company. So so the two most obvious
obvious people to to obviously use a group to look at
is sort of service providers. There's a lot of other teams
that provide some infrastructure as a service and they're consumers. So if you if you can build with the service providers in mind
and build with them such that they then provide value to their end, consumers and sort of you
reach again, sort of a follow out type approach in terms of providing value
to some and a lot of other to similarly to value to a lot of people. And if you can't get them to the service
providers directly, partner up with their consumers and
figure out how you can solve the problem for you, a consumer,
but in a sort of a generic way such that it will be applicable
to many different consumers. You also have obviously support
organizations like incident management and so on that has a lot of clout
in the organization. Partner up and then figure out what challenges they have
and help them with their solutions. In the same way in companies like Bloomberg,
where you have a a true engineering management chamber,
a report up to ultimately up to the head of engineering. That report to the board,
figure out what challenges they have on each level of the chain and
try to help them build their solutions. By doing this, you sort of get volume
and a bit of some of the consumer pressure on on people to to to to continue to add metrics. And so on to their app
to to their applications. Right. So there's a lot of different users
with a lot of different problems, Again, trying to figure out how are you
can you help some, help others, and then ultimately
you provide the most value to the company. Transparency. Don't be afraid to discuss the whys. So transparency is paramount
to build trust and transparency comes at many different levels when it comes
to a project like the telemetry. But obviously you should have full transparency
into the performance and stability of the of the platform and that people can
really trust the platform and rely on it sort of goes without saying
but also the comes into will be building for engineers internal
to our company. Right so we should provide
full transparency into the roadmap and honesty on what's on the roadmap, why something is on the road map
and why something is not on the roadmap. Be completely transparent
in terms of why we prioritize something over something else,
and that allows the the users to read and make their own decisions
about when they plan to on board and or if to have to make any adjustments
their own plans. And also very, very important rebuilding for engineers
that really love technology. So be prepared to discuss technology
choices. Be prepared to discuss right
exciting technologies with not chosen and stand by your choices,
but be open to discussing with your fellow engineers. I sort of said that I wouldn't talk too much
about product or about technology, but one thing that's key
is to build a product that has a low barrier of entry
as possible. There. There might be free lunch after all,
and people do like free lunch, right? So I already mentioned this to make it as easy as possible
to get onto the platform where possible, give people completely free stuff
like infrastructure metrics. We started at the bottom for a reason
to give everyone the the, the foundation
of what they needed for free. And also when it comes to owning
the product, own the product end to end. That means owning the API,
owning the agents and not just building them,
but also owning to make sure that you are responsible
for operating them where possible, upgrading and so on, such
that the application teams really only need to care about their own metrics
and what making the best metrics possible and make it easy to registries it
to get everything onto the platform. Have you been successful? It's not easy to define
or declare success. I'm not sure
if you've been 100% successful, but there is a couple of ways
to look at it. Number one,
we can begin to get adoption or I think we can say we've been successful. Some high level stats. About 40% of our engineers open
at least one graph on the dashboard week. We have about 500 million time
series and growing baby. We have about 170 terabytes of logs
flowing through our systems. They so not necessarily really explaining
if we have improved stability, but and that's hard to measure
and it's hard to sort of declare that you you avoided something
because you built something. Right. So but I think even one thing and sort of
where I started off with sort of the the Bloomberg system
has been under unprecedented load during the pandemic,
during the global pandemic. And I'm been very, very grateful for how
well the Bloomberg systems have performed, how well we've been able
to serve our clients, and what the visibility,
the central telemetry platform are provided into these systems. So I'm not really sure
what what we would have done without the
the central telemetry platform. Thank you very much. And as I said in the beginning,
if you want to discuss any details, at least contact me on this email
and please also check out our open roles. We are always hiring and always looking
to have good engineers across the firm. Thank you very much.

