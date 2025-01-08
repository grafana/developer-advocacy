# LATAM Airlines&#39; Digital Transformation to Build Customer-Centric Solutions | Grafana Labs Customer

Discover how LATAM Airlines, one of South America's largest airlines, transformed its digital operations to enhance customer ...

Published on 2024-12-18T16:30:21Z

URL: https://www.youtube.com/watch?v=IE3o-W3fE0s

Transcript: How many of you have taken a flight
in the last few years, two years, three years? Doesn't
matter. Think for a moment. Now, try to remember how long before that flight you
started looking for that flight, like dates and destination,
things like that. And I guess it was probably days,
weeks, or even months before. And the reason for that, it's because when many
industries and airlines the same, that you, we need time, we need
to look for different options. And that time tends to be
really longer compared to the physical experience in itself. So that's why many companies do digital
transformation 'cause many of the interactions that we have with companies
are with the digital channels, right? So my name is Carlos Hernandez.
I'm the head of cloud and SRE. And the story that I want to share with
you has to do with our last approach. Something that we begin about five
years ago. Well, first of all, some quick intro to LATAM. LATAM is one of the biggest
airlines in South America. We operate about 150 different
destinations, different countries. And in terms of flights, we operate about 1400 flights every day. So it's a big operation. Half of
those flights are actually in Brazil. And if we talk a bit a
little bit about passengers, we transport about 75 to 80
million passengers every year, right? So that's a little bit
of context of the company. Now, the story that I want to share
with you is the transformation that we started five years
ago, as I mentioned. But first, let me share something. Let me share what typically
happen within companies. When we seek transformations
like digital transformation. It's pretty common to
find this happen in IT or the technology organization,
whatever names that we may use. And that's fine 'cause many of the changes
have to happen within the technology organization because of
these digital interactions. Now, we decided to do
something different. We, even though LATAM is a big company, we decided to take the business unit, the commercial business unit
and part of the IT organization, and we merged them into a single new
organization that we call 'e-business'. And this e-business is the way
how we have been transforming. Again, this is just the first step. We
have many of the different business unit, but this was the approach
we decided to take. Now, putting people together from
two different backgrounds, different mindset isn't easy,
is actually really hard. But one thing we decided to put here as a condition was to have for
everyone, not just leaders, but all the people inside this
organization, the exact same goals, or it is a shared set of goals so that
all the people was pursuing exactly the same idea, the same incentives, right? So the story that I want to share with
you has to do with this transformation. Now, given that we started five years ago, the first thing that we needed to do
was to build these new capabilities. Remember, the idea was to replace our
digital experience with a new one. So this represent that transition
that took about two and a half, maybe three years. So all the red bars represent
the traffic that we were receiving on our previous experience. And the blue bars represent
the traffic on the new one. Now, all this transition, if you
see here, started about May 2020. It was actually a really complicated year. This was the year of the pandemic. So it was a hard time in many
different aspects. But anyway, during the first, I think
four, maybe five months we, after we roll out, our first
first country was in Ecuador, we realized that our ability
to detect the incidents, our ability to identify problems or
issue was, was really bad. I mean, wasn't enough. And we started working
on getting back on track somehow. And at some point, maybe
at the end of 2020, we would have many different dashboard,
many different panels like this. I wouldn't say that we felt comfortable
like the guy that you have in front of you. But, but anyway, we felt good enough, confident enough that
we could detect things. If something bad happened. Even after having all these different
dashboards and panels and monitors, we would still receive from
people that we knew. A friend, maybe a colleague or someone, whatever, a message like this
complaining about something, saying that the website was
not working or the app was, was taking too long to load
and things like that. So for, for some reason, not critical incident, but small failures were happening
during the day. A small failure, a given customer affected, and then
another one, and then another one. So that was frustrating. It was really frustrating for all the
teams and obviously for the customers. So we needed something
different. And at this point, we decided to introduce something
called fail customer interaction, or FCI And FCI wasn't an idea
that we created, right? It was actually a concept and an
implementation that the PayPal team did back in 2018 when
they had a very similar issue on their payment platform, right? So a small issue that they
were having during the day, and it was basically the same
thing that was happening to us. So we decided to introduce
this tool. Now let, let me explain you a little bit
what this fail customer interaction is. Imagine for a moment,
something like this. And this is our homepage. This is exactly what
we call our search box. And here you can select a given region,
a destination, a date for the flight, numbers of passengers, and then at
some point you would click that button. And for us, for every single
button or link like this, we defined a given action
name. In this case, the action name is
flag.selection.offer.search. So this is the interaction
that we wanted to track. Let me give you another
example. In this case, imagine you have already
displayed the different flights, and you have one link to see
the detail of that itinerary. Again, another action name
with a different name. So for every single button or
link, we have a given action name. For every one of those action names,
there is a single interaction on the UI. So it's a one-to-one mapping
or relationship, right? So that's pretty much the way how
this is, this is the basis for, for the tool that we call for
fail customer interaction. Okay? So that's the idea of fail
customer interaction on how we mapped. But there was something else
that was happening in our system. At that time, we had already built more
than 500 different services. And what you see here is our architecture. It is a layered architecture where
every one of those different boxes of different colors represent
different service. And the lines, the purple lines between them
represent different interactions. So it was a complex,
distributed system that we, there was no way for us
to fully understand this. So we needed a way to map the
different interactions on the UI, on the front end to the service
that was causing the, the error. And also, on average, every time someone would click
a button on the UI or link, we knew that about 40 different services
were also called at the same single interaction. So it was
a pretty complex system, and we needed a way to map
what was happening behind. So when you see this fail customer
interaction tool in a daily basis, how the teams were using it would look
something like this. This is after the data being ingested, you know all the different
steps that the data need to travel to at the end,
end up in a panel like this. So teams imagine in a daily imagining metrics ceremony, where they looking into
the data for the FCIs, they would see something
like this. On the right, you see all the different
services that were being generating that, that are generating different failures
that are affecting a given action name. Imagine the button that I showed before,
maybe the link or maybe the bottom. So all the different services that are
part of that single interactions are here on the right. Now, on the left, the different graphs or the
different bars represent how much of the failures were
introduced for a given service. So in this case, where you can see is that this particular
service is the one that is affecting the, the action name that
the team may have selected. So you can have a completely different
conversation, not just for leaders, but also for the developers. Everyone all the people in the teams, on
the, again, in the leadership, were using exactly the same language. So when they wanted to
prioritize something that
was affecting our customers, they would use something like this. So it was a huge change in the
daily interactions and conversations within the team dynamics. But there was a downside. The downside that is that this
data is a few hours delayed. So you can have very
good conversation about, but what to prioritize next. But it was not possible for
you as a team to use this in real time. So for instance, imagine you wanted to push a change
code into prod. You can do that, but you cannot use this dashboard
'cause it has these hours of delay. So we needed something different. We needed something that
could allow teams to operate using this concept of FCI,
but in real time, right? We, it wasn't enough to
have hours delayed. Now, this is the moment when we
introduced the Grafana Cloud stack. This is the moment when we also had to
migrate from a different solution that we had at that time. And
that's a story in itself. Imagine we migrated
everything, and at some point, one of the things that we did was to
create basically the same idea of the FCI, but now using metric collections. Now, all the data in this case was generated
by the different services and all the different services were
sending data of the failed customer interaction that were
happening on that particular artifact of service. So what you see here, and to the left upper left is that you can select the different data. In
this case, it's the environment. We have the exact same data for
all the different environments. You can select a time span and you
can also select the action that you want to look right. In this case is one action name related
to the two-factor authentication, the login process. So when
you see here, different bars, the green bars represent the success
request, the red bars the failures, and the line between is,
is the ratio. Right? Now, you as a team, imagine you, you could use this exactly for the
problem that I mentioned before. You could deploy a new change into the 2FA service login. And, and you could see if that change resulted in a failure. For instance, you could see a huge red bar and you can
react immediately and roll that change back. So that was one of the main benefits
of using the same FCI concept now in Grafana. Now the question is that, is this enough for a team to operate
a given service or an application? And the answer is, it is
good, but it's not enough. And the reason is that
there, there was no clear, or there wasn't a clear
way or to answer for the teams. Is the size of those red
bars were okay or not? I mean, is it 1.50% something that it's okay ?or
it's not okay?, It's bad and, and I need to do something about this? And it's not possible to see or to
answer those kind of questions here. So there was, the next level for us was to actually
introduce the SLO as an essential way to manage the reliability of the
different services. What you see here, this is the Grafana SLO section. We have this for many of the
different services that we have today. And you can see the time
window of that SLO. The target, the basically the same data here
of success and failures request. And then on the left, if there was
any critical or warning alert. Now, what I want you want
you to see here is this. If you look into this, it's
basically in this case, the same action name for the
link that I showed you before. Remember this the "Direto" link. So we have this panel, this same information for all the
interactions that we have. In this case, this is the link. And in our case, in
our website, just on our web channel, it's more than 600 different
interactions that we have mapped today. So it's a completely new way of operating, completely new way of defining
reliability goals and to create a new way of, of managing
reliability. Now, after all this journey of using, of realizing that we couldn't
detect some basic failures, introducing the FCI then
real time solution. And
enough at the end of the day, the Grafana SLO by building
one thing on top of the other. This is some of the benefits
that we have seen. In our case, the time to detect, which is the time it takes for us
between an incident affecting our customers and our on our side, detecting that failure was
reduced in more than 80% in this about three years, right? This was for all this severity 1 and
2 incidents across all the different squads, right? Like the fall
entire e-business organization. So I think from, from an operational
perspective, this is one of the most relevant changes that we have seen
on reducing this amount of time is, is a huge improvement. Now,
there was another change, actually. There was many
different improvements, but the second one that I want to
show you has to do with something more internal to the teams. 'Cause one of the things that takes
energy from people is to be paged at 3:00 AM right? So the noisy alert, it's a problem that we
need to address somehow. And after teams have adopted this new wave of operating the different services
that result in an alerting system based on our budget, we have seen more
than 60% reduction in noisy alerts. That is also a huge improvement. And not
all the teams are already doing this, but the ones moving from the traditional
approach to the new approach. I've seen a reduction of this amount. Now, something else that I want
to share with you you, you can try to build
capabilities. You can try to offer an SLO capability, right? For your team so they can
better operate their services, but it not just enough to give them the
ability to do this by clicking on the UI, for instance. So you need to connect the ecosystem of
tools and practices and processes that you may have. In our case, we have many different tools
in place already at that time. Something that we call starter kit, which is basically a skeleton for the
different applications when you can have access to the repo and in a specific part of that repo. You can
define all the different SLOs and, and batch edits and all
the data that you may need. And you as a developer, when you have access to that in your, you know environment as soon as you push a
change, imagine to your repo, we have the CI/CD tools and
processes take that data from that. And depending on the changes
that the CICD process see on your repo, we can interact
with Grafana, the API, the Grafana API, and we make all the different
changes as we need to IRM to SLO. And all of this is fully
automated and connected. Same idea when you are deploying
a change in in your application, imagine same idea. The application has a library
built in that helps the teams to gather all the different
telemetry that they need. And this data is also
pooled by the Grafana Stack. So all of this is connected and the
message that I want to share with you is that you have to think about
how to simplify the process, not just provide capabilities. You also have to provide a easy
way to get them to use them. Now, all of these are different
changes and the impact that we have seen so far, but what about
the future? What are we trying to do? What is our next step? And for
us, I mentioned before that the, the improvement was on our
time to the deck, right? But every time we have a incident, we split those incidents
into three different times. One is time to the deck, the
other one is time to acknowledge, which is a time it takes for us to
arrange and meetings and call different people. And then when we're
already working on fixing that, it is the time to repair. So it's
the third phase of the process. We have seen an improvement. It's
a 23% reduction, and it's okay, but for us, it's not enough. We
think, we believe that we can, I wouldn't say easily, but we think we can get and
cut this bar by half. I mean, reduce this even another
50% further, right? So this is, this is the
challenge that we have. One of the challenge that we have.
Now, how we expect to make these changes. We see three main levers here. One thing we see back using the
same idea of the application on the observability stack or the observability
backend is at the application level. This is a place that we, we can improve the way
how we generate data, how we generate the different
telemetry, but not just the how we create that telemetry, but
how is it correlated, right? Today, it's not fully correlated. We
have some data that is correlated, but some other telemetry data is not. So one thing is we can simplify
how teams can correlate the data. So it's pretty easy in the future
to move from metrics, logs and tracing, right? That's, that's
pretty much the idea. The other one is that we have a ecosystem
of tools that is more complex than what we want. And it is to
simplify this experience. As soon as you have data, right, and that data is pulled from
the application and it's already within the observability backend, how easy it is for the developers
to move within that data, right? How you can visually move from metrics
to logs to traces and how you can connect visually of this data. Today we
have more things that what we want, what we would like to have. So to streamline this developer
workflow is the second thing, the second lever that we
see. And now the third one, and I think this is the most
important one, it is that teams, many of the teams that we have today
tend to think in observability like a  process. And we see that there's a huge
impact that we can create if we introduce the observability
driven development approach. So start thinking how to
observe your applications, your service and your customers
before or at the moment you're start designing, building, testing,
and deploying your applications. So that's the third approach
that we, we we want to follow. Now, We do have, we, we've seen a few teams doing this,
actually a few teams doing this. But the moment we saw people
drawing things like this, it wasn't an actual draw
that someone did from, from a given team as we thought that there was hope of
improving this observability driven development, right? Teams doing this
like by hand. I know it's pretty, maybe it's not a beauty
diagram, but, but anyway, it was a team that we saw
drawing this at the moment, they were thinking on the new feature,
new capability that they wanted to build. So we have seen these signs,
we have seen teams doing this. So we hope we can help
all of the different, the rest of the teams
to have exactly the same practice in a daily basis. Now, one last thing that I
want to share with you. The key takeaway for me is that the
focus has to be in the customers always. As soon as you fo you, you fo
you focus on your customers, all the rest of the tool, all
the rest of the practices, all the rest of the technical
style you may need and will follow. Thank you.

