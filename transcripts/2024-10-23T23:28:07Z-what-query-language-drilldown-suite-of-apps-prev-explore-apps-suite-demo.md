# What Query Language? | Drilldown Suite of Apps (Prev. Explore Apps Suite) | Demo

Update: As of Feb. 20, 2025, the Explore apps (Explore Metrics, Explore Logs, Explore Traces, Explore Profiles) are now the ...

Published on 2024-10-23T23:28:07Z

URL: https://www.youtube.com/watch?v=YICcDk_ddC4

Transcript: I'm gonna continue on the topic of how
we're making observability easier for a wider audience to adopt. And to do that I'm gonna talk about
Explore metrics and explore logs. Some of you may remember we
first announced these back
in April at GrafanaCON. What they are are experiences that
allow you to navigate data stored in Prometheus or any
Prometheus-compatible backend like Mimir. Or in the case of Explore logs, a Loki backend and do it without
having to write a query language, say PromQL or LogQL. And why is this? We'd heard from a lot of users that one
of the biggest challenges to getting started with observability is the fact
that you had to learn a query language before you could actually start to get
any value out of your observability data. So what we did with Explore Metrics
and Explore Logs is that we now have replaced typing queries
with a point and click UI. We've replaced empty start screens
with pre-populated visualizations, making it possible for anyone from day
one to start getting value outta their metrics and logs. Now, since we
announced this back in April, we've seen a ton of enthusiasm
and adoption for both of these. And given that we've spent the last
couple months really listening to early adopter feedback and making a lot
of improvements to both and that's why today I'm super excited to announce
the fact that both Explore Metrics and Explore logs are now generally
available for both cloud and in open source. Now we made a number
of improvements in the lead up to GA. With Explore Metrics, we've improved
our related metrics section, making it easier and better
recommendations about what
metrics you should look at based on the one you
currently have open. With Explore Logs, we added the ability to automatically
visualize attributes stored in Loki's structured metadata. This is particularly great for those
of you out there using OpenTelemetry logging. We also tuned our pattern
detention functionality so
that we can quickly surface the most common patterns
in your log lines to you. And we're definitely not
done there. After this GA, we intend to fast follow with a number
of upgrades to both explore metrics and logs. For Explore Metrics, we're
adding support for native histograms, a higher resolution histogram type
relative to classic histograms. We're also gonna be incorporating machine
learning into our related metrics so we can surface metrics that have similar
shapes and patterns to all of your users. With Explore Logs, we're adding streaming support
both to your graphs and to the log lines we show you, which means less
time for you waiting around for results. Now based on the success of both
Explore Metrics and Explore Logs, I'm excited to announce that we have two
new additions to the family - Explore traces and Profiles. We've decided to extend the experience
of these two across all the pillars of observability. Both of Explore Traces and Profiles
are available in public preview, again, both in cloud and in open source. Upon completing this
suite of Explore apps, what we can now offer is a
full suite of options so each user can choose how it
is that they wanna work. This reflects our belief
that observability isn't a
one size fits all solution. For those who are gonna want that
full control and infinite flexibility, they can type out queries in
code mode. And lemme tell you, I have been blown away by the things
I've seen some of the folks on our engineering team do with these
like 50 plus line PromQL queries for those who want something
kind of more in the middle. There's the builder mode. That's sort of what I think of as maybe
like a low code or a visual programming experience. That's gonna be a great way actually
to learn the query languages 'cause it gives you a point and click way to
string together numerous operations. And then for those that just want
push to start, let's get going. We have the Explore apps,
no queries, no code, just easy insights. Whew. Well it wouldn't be a Grafana
Labs keynote without a live demo, so I'm gonna try to do
this right now. You know, I had wanted to do a video demo
and then Tom told me that was lame. So please cross your fingers for me. I'm about to take you on a little
ride through Explore Traces - one of our newest additions to the family. Now I'm a product manager, which means I've left the noble
discipline of engineering. But let's pretend for the sake of this
demo that Jen is still an engineer working on an e-commerce platform. If you drop into Explore Traces, let's say I'm just here on the screen
and let's say I've gotten a page that my error budget SLO from my product
catalog service is burning down a bit quicker than we would expect. Dropping into the main Explore
pages Explore Traces page. You see your RED metrics at the
top, your request rate, error rate, and your duration. Since
my page was about errors, I'm gonna start by selecting Errors. Hopefully down here you'll see that
Explore Traces automatically breaks down that error rate by service name. Since my page was about the
product catalog service, I'll quickly add that to my filters. The next thing you kind of ask yourself
in a classic debugging workflow is what is unique about these requests that are
erroring as compared to the ones that are completing successfully? Luckily, now we have this comparison
tab to help you with that. What the comparison is going to do
is compare a selection. In this case, the selected traces are my
erroring traces to my baseline. So those are the traces representing
requests that are completing successfully. What Explore Traces is
gonna do is, out-of-the-box, it's gonna look at every single
attribute on my traces and compare the baseline to the selection. It's gonna sort to the top the attributes
that show the largest delta between the baseline and the selection. And what
do I see quickly push to the top here? Well, it actually looks like all of my errors
are happening on one particular product ID and clicking inspect,
that's exactly what I can see. This product ID represents
all of the errors. All of the other product IDs
seem to be completing just fine. I can quickly add that
product ID to my filters, and then from there I can actually open
up some erroring traces matching that criteria. Again, speeding along my debugging because I
go to exactly the sort of representative trace that I want. Now let's pretend while we've been
here dealing with our error, SLO I, at the same time, got a
notification from my support team. It seems like some of my users on my
e-commerce site are complaining that the site's loading pretty slowly for them. Maybe they weren't using the
synthetics that Tom was talking about. So there, since the page
is about slow loading, what I'm gonna do is look at
my duration signal. Again, the first thing you see is that Explore
Traces is showing you all of your services and breaking
down their P90 latencies. What I can see is that I have
several services with P90s on the order of seconds. So I wanna now
figure out what again, is going wrong. And so again, I ask myself, what is unique about these high
latency requests versus those that are completing in a reasonable
amount of time? Again, I come over to my trustee comparison tab. This time we can actually use a
selection ability in the Explore Traces app to pick a set of traces. I'm gonna try to select here the
slowest of the slow traces here up top. Then I'm gonna be able to compare
the traces falling in this selection, this orange box to the traces
falling outside of that my baseline. I'm gonna hope that my page actually
loads. All right, there we go. And so again, you see the distinction. We're automatically comparing
across all attributes. The difference between my selection,
my super slow traces and my baseline. Since support said it was
something related to some users. I'll quickly filter down
to user-related attributes. And what I can see is, hey, there's a certain set of user IDs that
seem to be in the slow traces group and then a certain set
that are in my baseline. I can similarly see if I look at
the user location that certain locations are disproportionately
represented in those slow traces. So that allows me to, again, narrow my search and look at traces
from those particular locations to figure out what's going on. It's also great for me because I
can go back to support and say, Hey, this looks like this probably isn't
an issue for all of our users, but it's just a subset.

