# Get Insights From Your Metrics, Logs, Traces and Profiles Without Query Languages | Feat. Shopify

This video discusses Grafana's continuous profiling platform and how the Explore Suite simplifies troubleshooting for non-experts ...

Published on 2024-10-24T19:49:41Z

URL: https://www.youtube.com/watch?v=K8TmlvSsEdc

Transcript: Hi, what's going on
everyone? My name's Ryan. I am a principal product
manager here at Grafana. One of the many hats that I wear here. I'm also one of the founders of Pyroscope, which is our continuous
profiling platform. We're gonna talk plenty more about all
that later. But before we get started, obviously you have the the Slido
slide here. If you have any questions, feel free to ask throughout
the presentation. We got a bunch of people talking today, so hopefully we will have time
for questions, but if not, we'll be at the Find the Experts booth
after, and you can ask us there. So yeah, we got a lot of people talking today,
so I'm gonna go ahead and get started. You know, obviously welcome to
ObsCON, New York. We're on day two. Hopefully you all have had a chance
to get out, explore the city, see New York a little bit. Just by show
of hands, I'm curious, how many people, is this your first time in New
York? Okay. Oh, we got a lot, a lot of new, new New Yorkers.
Anybody from outside the country. Oh, wow, that's way more than I thought. So a lot of international people
as well. So yeah, again, welcome. I'm not from New York, but it is one
of my favorite places in the world. I love that the mix of cultures here, the the fact that it's the center of
so much culture, whether that's art, movies, tv, fashion, politics,
like whatever it might be, a lot of that originates here
in New York. And so, you know, if you're interested in landmarks,
obviously we are here. You know, there's a ton of really
historic landmarks, right, where we are literally sitting today. But really any neighborhood
you go to you know, you can find some interesting
stuff there. If you're into sports, there's plenty of you know,
sports to see almost so many. There's like two teams for
pretty much every major sport. There's even a soccer team here.
And you know, there's bars, music I know a bunch of people or a
couple people went to a concert at Madison Square Garden. I don't see them here
today, so hopefully they will you know, make it back later. But
you know, my favorite food, like really just no matter what
you wanna do, a lot to do here. So my favorite rapper, who is also a New York native said it's
the concrete jungle where dreams are made of. There's nothing you can't do
including quote Jay-Z in your tech talk. So I bet you didn't have that
on your ObsCon Bingo card. Anyways it's kind of a double-edged
sword, though. There's a ton to do here, but at the same time, that makes it really hard when you wanna
do something specific to filter through all the many options that you
have to see something specific. This happened to me yesterday. All the Grafanistas here
know how much I love pizza. And I wanted to find the
best pizza in Manhattan, and I sort of had two options
of how to go about it, right? And so option one was to you
know, ask an expert. Luckily, I have a friend Michelangelo, who
if you can't tell by his name, is of Italian descent. And if you can't tell by the profanity
that the marketing team has so kindly blurred out of my presentation
here is also a native New Yorker. So he was the best expert
that I could ask about pizza, and he was able to recommend me
somewhere. It was really good pizza. If, if you get the chance to go
there, try it out. But also, how many people in here have a a
Michelangelo in your life who you can ask about pizza in Manhattan?
It's like three hands, maybe out of the 300 people here, maybe
the top percent have access to that. And so for the other 99% of us,
if we want to get our pizza fix, we have to find some other way to find
that pizza. And so enter Google Maps, which I'm sure you've
already used here so far, where you can filter by what's
open now, what fits your, you know, your price range, what's
top rated, et cetera, and makes it accessible for the
rest of us, right? And so, you know, what does this have to
do with Grafana? Well, our old Explore experience was
kind of the main option, right? And so if you add an expert on your team
who knows how to write PromQL, LogQL, TraceQL, FlameQL, knows how to
write all these query languages, you could reach out and ask them and they
can tell you, oh, here's your problem. Here's what you got paged about.
Here's how you fix it, right? But for the other, you know,
maybe they're on vacation, maybe they're asleep and you got
paged in the middle of the night. Maybe you just don't
know who that person is, or maybe that person doesn't exist at
your company, in which case, you know, you have to find some other
way to solve your problems. And so that's why we created
all of these Explore apps, which is what we're gonna talk about
today, to make it easy for the other, you know, 99% of us who may not be experts in
all these languages to still get value from all that telemetry data that you
know, you're collecting from your logs, metrics, traces, profiles,
et cetera. And so you know, enter our queryless Explore Suite
is what you're gonna see today. You're gonna see a couple demos from
you know, metrics, logs, and traces. And then we have a special guest from
Shopify who's gonna talk about how they get value from their
profiles. And so with that, I'd like to bring Catherine on stage
to start us off with Explore Metrics. Thanks so much, Ryan, for the intro. So I'm gonna talk about Explore Metrics
and Explore logs, but before I do that, I want you to imagine this, it's Black Friday and you and your
team are getting ready for the big day. You're hoping your systems can
handle the onslaught of customers, and things seem to be going
smoothly. So you go to bed, however, you wake up and you're getting pinged, your customers are seeing slow response
times, your webpages are timing out, and you and your team is panicking. Now, looking at a video here, you might be using Grafana
for metrics. And in general, you can probably narrow this down,
but it can take some time. You know, there's slow response times
happening in your system, so maybe you're gonna look for, you
know, a metric related to slow requests, and you start to query it
and you don't find a problem. So you look for another metric here, and it takes time, you know, to
query and look for other metrics. And once you get there, you might be able to find a metric
that eventually shows a problem and you get there, but there
might be issues with, let's say, a CPU metric as well. So you
repeat this process all over again, and let's not even talk about the upfront
effort it took for you and your team to learn PromQL. So going back into the
slides with Explore Metrics, you're able to visualize all metrics
from a Prometheus data source without having to write a single query. That
means you can dig into each metric, making it much quicker for you and your
team to perform an investigation leading to much faster time to first insight.
Now I'm gonna demo what that looks like. So as you can see here, there's a list of metric
graphs on Explore Metrics, and you can scroll through them. You can also hover over some tool tips
and learn more about the metric in terms of the description and type. You can
also filter or search for metrics. You can filter, for example, if you
knew it was coming in from Kubernetes, or if you know there was a container
it was coming in from a container. Now in my case, I know that this customers have
been seeing a slow response time, so I might want to look for a request
metric. So I will search for that. And I know this has been happening,
let's say in the past 12 hours. So I'll change for that
time range as well. So I can see there's some
metrics showing spikes here. So I'll go into one of these metrics,
and I can see this graph again, along with a list of labels and some
more information about the metric. I can also go into this breakdown tab, which shows a list of graphs
related to the labels as well. Now, in my case, I feel like this problem
might be related to an endpoint. So I can select this endpoint
value endpoint label, and then I can see these different values. I can see there's spikes showing up
again for the login and payments. So I might wanna add this to a filter. Now that I know that this is
related to let's say, an endpoint, I wanna look at other related metrics
that might be having problems too. And I can do this by clicking
the related metrics tab, which shows a metrics
related by the string name. So I can click into another
metric, I can take a look here. And once I finish my investigation, I may want to do other
things. Like, for example, I can bookmark this for later. I can share this
investigation with a coworker, and I can also open this and explore.
So when I open this and explore, you can see the query. Again, if you wanted to manipulate this
or if you wanted to, for example, to add this to a dashboard.
So this is Explore Metrics, and for this, you're
able to find a problem. But what exactly is the
actual problem? Well, this is where Explore
Logs comes into play. So with Explore Logs, the challenging, the challenges of looking for logs are
very similar to the challenges of looking for metrics in Grafana. So looking at a video here you
can see that someone is trying to query again, and maybe you're able to
kind of like find the data you need. So if, even if you're able to,
let's say, understand that, hey, I know it's coming in from a service, it's really hard for you to be able to
really like narrow down what you look for if you don't know, for example, like the fields or the patterns
you're looking for in the log lines. So Explore Logs allows you to really
streamline the process of identifying issues caused by high log volume. You're allowed to filter further and
you're allowed to really efficiently pinpoint problematic log
lines through this and Explore Logs works with all Loki data sources. So I'm gonna demo Explore Logs as well. So this is Explore Logs.
As you can see here, there's a list of services and
associated with each service. You can see essentially a
graph showing log volume, as well as a graph showing,
like a table showing log lines. So I'm gonna refresh this, and you can see now that there is a
full graph showing all of the log lines. And as I'm scrolling through this, I
might see something interesting with, let's say the Mimir ingestor service.
So I'm gonna go into here. Now, in my case, I might want to
filter by labels. For example, in my previous demo, I saw that there was something happening
in one of the specific endpoints. And while I don't see endpoints here,
I may wanna then look into like, let's say log patterns. And I can see that this log pattern is
showing something really interesting with here. And there's some spikes.
So I'm gonna include this as a filter. Next, I'm gonna go into fields. So
fields are key value pairs for log lines. And I can see there's interesting
patterns showing up with a lot of these different fields. But I'll go into, let's say this tenant field, and I see that there's
interesting patterns showing
up with this specific tenant id. So I will add this as well.
Now that I added in some filters, I will go back into the logs tab. Now I can view logs in two different ways. The first is just
looking at the log lines. I can expand this and I can see a
list of all of the fields and filter out or filter in some specific fields, or I can look at it in the table format, which is really good
for JSON formatted logs. So here I can manipulate columns here,
I can manage them in different ways, or I can even click on a certain
field and then add it as a column. And then similarly, to Explore Metrics,
you can then open this and explore. You can add the query into a
dashboard or you can manipulate the query some more. But as you can
see here, this query is quite complex, making it really hard for me to
really be able to write out this LogQL unless I actually knew, like, for example, the patterns I was looking
for or these specific fields. So this is Explore Logs. So going back into the slides
as part of this launch, I will also wanna announce that we are
having support now for OpenTelemetry. We know that many of our customers
are using OpenTelemetry to collect and instrument their data. And now you can use Explore Metrics
and Explore Logs to view your OTel-compatible metrics and logs. This
is now available in public preview. So as a recap with Explore
Metrics and Explore Logs, you're able to reduce
time to first insight. You're able to reduce time to diagnose a
problem leading to significant time and cost savings for you and your team.
So as a recap, again, Explore Metrics, Explore Logs is now available
for GA on OSS and Cloud, and you can try this out today.
And now I will pass it off to Joe, who will talk about Explore Traces. Awesome, thank you. Hello. Hello. Hey everyone. Thank you Catherine for
the awesome Explore Logs, Explore Metrics demo. Hope to follow that up
with a Explore Traces demo. I guess I'll hit forward here so
we can see that yellow screen. And then we're gonna go into
a demo for Explore Traces. Oh. Oh, there we go. Cool. Can we swap
to the laptop? Thank you. Awesome. so Explore Traces we got to
see a little bit of yesterday. Jen Villa showed us some
basic capabilities here, how we're taking our tracing data and
showing an aggregate to find errors and duration, slower traces. Today I hope to show a couple more
features that she didn't get a chance to highlight yesterday. In addition I'm gonna talk a little bit
about some flows that I really enjoy using for the, with this application.
As well as talk about, you know, our philosophy a bit, why we chose what we chose why
we built this the way we did, like what we think is
important about traces. So first of all she talked about
there's the RED metrics here, right? We have rate, errors and duration, and the app kind of revolves around these
three and orients yourself orients the user to if you're choosing and
looking at errors to find erroring traces, if you're doing
duration, to find slow traces. And then rate is meant to be more of
like a general exploratory experience. You're just trying to learn and understand
how your applications talk to each other. So I think this is the
first superpower of tracing. It is the signal that teaches us how
our applications talk to each other. And that's a really critical and
important part of explor traces. And we'll see a little bit
more of that in a second. So I'm gonna share this flow with you
for both duration and with errors. And we're gonna go find some slow traces. We're gonna use filters and we're
gonna use this root cause trick here. And then we're gonna do
the same with errors. And we're gonna see a very powerful
method of using this tool to go determine, "What is, what is what is
wrong in my system? What, what is bad thing is occurring right
now," I suppose. So first of all, we're gonna start with duration. Here
you see I have a heat map at the top. It's ranging from a couple hundred
milliseconds up to a couple seconds. And down here at the bottom, I have a similar breakdown tab we've
seen in all these Explore applications. And I can kind of click around, oops, I
did not wanna exit full screen though. We can do something different than
that. Let's just do this right here. Oh double click. Yeah, we will
just be like that for now. And I could you know, click on each of these attributes
and try to figure out where, which of these attributes was
correlating with my latency, right? Jen showed us this yesterday,
and it's fantastic. It is this automatic way to, for
all of the attributes of my traces, immediately find these correlations
for us. We can visually scan these set of graphs here and determine
very quickly which attributes on our spans are tightly
correlated with our slowest traces. So we're also highlighting
those, bringing those to the top. Here I can see this particular
span name profile occurs inside that box at the highest
level, the slowest traces most often. And then we can see some of these other
options here are only below the box location. So we're not
concerned about these. We have a couple other that are kind
of in between avatar and contacts but maybe we're not so
concerned about this. We clearly have one of our endpoints
that highly and tightly correlates with high latency. So let's go
investigate that a little bit. I will click add the filters, and apparently I'm gonna bring
up the dictionary a bunch. Again, now that we've added this, the filters, we're looking at a subset of the data we
can scan down and visually quickly see that there's not much
more information here. Nothing is really nicely
correlating anymore with that high latency. I'm seeing a lot of even bars. And this is telling me that it's basically
the same inside and outside the box. A very quick visual indicator that
maybe we don't have a lot more to learn here. So we're gonna go to this next
tab, which is root cause latency. So this is gonna show us from that
profile endpoint that we identified as a slower endpoint using the filters, it's gonna show us those spans
in aggregate beneath profile that are pushing out the length of this call. So this is a couple thousand
or a couple hundred traces. We're looking for a bunch of examples. And we aggregate those all
together to show you one view, to show you very quickly what is
occurring beneath slash profile that is slowing us down and or slowing
us down and making we should be slowing us down and it's
something we should investigate. So I can kind of clearly see
here, I have a user service. The user service is actually doing
the job of finding the profile. Perhaps we see a couple hundred, a
hundred millisecond spans there. And, but we also see this off
service, which is three seconds. So we can see visually very clearly
that this off service is a problem. We can jump into, now we're looking at individual traces
that we were aggregating to create this aggregate trace. And maybe we
can start building a a story, an understanding of why this off service
is pushing out our profile endpoint. I can look here. Now, I know
because this is synthetic data, but I can look here and there's an event.
And if I look at all of my examples, I can very quickly see all
service is always this problem, this event Tex acquire is
occurring late in my span. I probably wanna spend some development
effort on on figuring out what the locking issue is in this all service. So if you see the profile
endpoint is low or, or very slow, your initial instinct may be,
let's go look at the user service. It's the thing that services the profile
endpoint. But with a couple clicks, we could very quickly in
the Explore Traces app, very see that the all service
is actually the issue. We're gonna go dig on that actually
and determine what's wrong. So this flow is very important to
me. Start with your comparison tab, filter down, find those
attributes that are correlating, and then go from there to the root cause
tab that's gonna dig deep in the trace. So again, that is the
superpower of tracing. How do my services talk to each other? What causes what true
causal relationships, not just co correlative
relationships, tracing tells us that. And that is an important element
of our application. So, real quick, let's kind of walk through a similar
thing with errors to show you we can do this with errors as
well. So, similar idea, we're starting looking at all errors
across everything in our system, all of our traces. Comparison,
again, very quickly, this is gonna highlight those attributes
on our spans that correlate with errors. Very easy to visualize this. You can immediately see these first few
boxes have important information for us. These endpoints here in stock, item, these all seem fine. They're all green,
no big deal. Clearly we have one here. Location, location. Oops. Oh
my bad. The tool tip froze. Yeah, purchase, purchase is
highly correlated to our error. So this purchase endpoint is clearly
having some issues. As before, we're gonna add the filters. As before we can see clearly no more
information available at this level. We can scan visually and quickly see this. And just like our latency with, or
just like our aggregate latency, we can do aggregate error
errors through our traces. So this is hundreds or thousands of traces
aggregated together to determine the path of errors and very quickly and
instantly show you this error at the edge, this air at the gateway slash purchase.
How many services down is the root air? How far down do I have to go?
Is it five? Is it 10 services? Where is the thing actually occurring
that's bubbling up all the way to the top? This is the question tracing can
answer. And I am very happy that, and very proud that we can do
this in our Explore Traces app. So here we can see a couple of options.
Purchase endpoint, cart service. Cart service is going to this database. And the database here is failing. So immediately we have some very good
information. We have a failing database. It's impacting this purchase
endpoint. We didn't spend 10, 15 minutes looking at a whole bunch of
different a applications to see what errors were correlated. We immediately were able
to stitch together with our
tracing data all the way to the root cause, this
database issue itself. The final thing I would
like to demonstrate here is the fact that tracing data is highly
structured, right? So log data, a lot of times is just a a text string. Metrics of course are
a bunch of data points, but tech tracing data has attributes, some attributes that indicate clearly
what is occurring. Like for instance, a database access a a span will often
look the same no matter what application creates it, especially if you have a set of semantic
conventions like with OpenTelemetry. So, so far we've only
looked at full traces, like we've looked at an entire trace and
we've determined where errors are and we've dug down into that trace. But because because tracing
data is so highly structured, we can look at any element of your
applications across all of them. So I'm gonna look specifically
at database calls. These applications are using the OTel
semantic conventions. And because of that, the tracing app can the tracing app can
show us across all our applications, what are our databases doing right now,
because all those spans look the same. So we're gonna aggregate that information
instead of the traces themselves. So let's jump to our comparison tab. This is now across all
databases in our entire system. This is showing us those attributes on
our spans that correlate to the database failures. So we instantly should be able to learn
things like what services are failing, what database calls are failing,
what databases are failing. We should see these visually and we
should be able to jump to those databases and fix them immediately. So I
can see this insert database, that's what we saw previously was
an insert. So that's the span name. I can kind of dig right here. Individual
span or individual database statements. I can see this insert is failing
more than, than it is succeeding. And I can even browse over here and
see, oh, I have some other selects. Those seem fine. Those are all
succeeding. I can see the exact service. It's highlighted for me so clearly 'cause
that red bar is so much larger than the green. And then finally, even the
database name itself. So I can see, okay, I got this inventory database, it
seems fine. The user's database though, that one is the one having problems.
So with this comparison tab, we were able to instantly
correlate across all our databases, all our database accesses, and see
the service, the database itself, the kind of operation that was failing. And we have a huge set of clues to now
take to our database and go look at logs, go look at metrics. Are we under tuned?
Do we have locking on a table? You know, what is causing this issue? I have so
much information and it took me very, like, maybe a couple minutes to
determine that with the traces out. Cool. So I think that's it for
me. Thank you so much. Ryan Perry is now gonna
show us Explore Profiles, the latest and greatest telemetry
signal. Take care, everybody. Alright, I'm back. Yeah, so Explore
Profiles. I'm not gonna go through a demo. I think you kind of get the idea of
how these Explore apps make things much easier to you know, to get insights
from your data, which is, you know, what we intended to talk to you about. And I also wanna leave
some time to you know, have our guests from Shopify come up
and talk about how they get value from profiles. But before I do that profiling is
a somewhat newer signal relative to metrics, logs and traces. And so I do want to kind of take a second
to sort of explain how profiling kind of fits into the bigger picture along
with the other telemetry signals that people have. And so the example
I usually give is that, you know, when you have a hammer,
everything looks like a nail. If you're just using metrics,
if you're just using logs, you're gonna find a way to solve
every problem with metrics or logs. But a lot of times, similar to, you know,
how you use actual tools in a toolbox, there's a better tool for the job. And
so, you know, a lot of people think of, oh, first I start with metrics and
then I do logs, and then I do traces, and then I do profiles. But in reality, they're all kind of useful in
different scenarios, and it's not a, it's not exactly a kind of sequential,
you know motion to use those. And so this, this slide kind of just shows
a little bit of what that looks like, you know, so for example, let's say
you have a spike in your CPU metrics, you know, that's useful knowing
that something is going wrong there, but now someone's gonna get paged. Maybe you have an alert
based off of that spike, maybe it's outside of a threshold. At some point you're gonna
need to understand, okay, what do we do about this spike? How
do we make our CPU go back down? Same thing with logs. You know, maybe you have an out of memory error
that is showing up in your logs, maybe you found it via
the Explore Logs app, and now you need to resolve that issue. You need to drill down into somewhere
and see that code level root cause of what's causing that. And you
know, similarly with traces, maybe you used Explore Traces, you've determined that some code issue
is the reason that your trace band is slow. Again, you need to go change some code somewhere
in order to make things you know, make things right. And so that's where profiling comes in
and is very useful at giving you that code level root cause of
why something's going wrong, and how you can then fix that issue. And we have spent a lot of time focusing
not only on the Explore Profiles app, which again, is very similar to
what you saw with these other three, but also making it so that profiles
can be kind of inserted and easily shown within your traces or linked
to from your metrics or logs or anything else that you're using with
your load tests, et cetera. So yeah, so the thing I wanna talk
about too, just since you know, profiling might not be as familiar is
kind of what the business value is. And so there's sort of, you know, three
areas. There's, there's, you know, you have the proactive side of things
and the reactive side of things. One thing that we found to be very useful
with profiling is that you don't have to wait till something goes wrong in
order to get value from your profiles, right? You can already kind
of understand, you know, particularly in the cost cutting
scenario. And then often as well, even though latency here is in the
reactive section you can also do that proactively as well if you have some
initiative to make things run faster. Profiling is very useful, you
know, for those use cases. And so just an example
of what that looks like. Some of you may have seen a similar slide
to this before. In the past, you know, year, we've had a lot of customers
onboard onto our profiling product. And what we've seen is that,
you know, a lot of times, you know, in the past costs were less as time goes
on. And as your, as your company grows, costs tend to grow. And so, with just like a minimal amount of
overhead, we often see, you know, something like 10% of just like low
hanging fruit easy costs that you can optimize in your infrastructure in
order to get value and get a good ROI on your profiles, again, before anything goes wrong or before
you even realize that something's wrong. Perfect example of this. This is actually
a company that I used to work for. But yeah, basically they
were using a bunch of Kafka queues in order to do
a bunch of jobs, right? And so this was a huge part of our
infrastructure and and they were basically able to use profiling to understand
that there was a essentially a part of the compression code that by
default was set to the maximum level of compression. And so what they didn't
realize was that, you know, by simply, you know, adding an actual,
like variable there, instead of using the default compression
that took it from using, you know, a significant amount of CPU to compress
things to a much, much smaller amount, which ended up saving 20%
on the AWS like compute bill for this service in particular. And,
you know, that's a huge win. And again, that's the type of thing that you don't
realize that a lot of this kind of bloat has crept into your systems
until you're using profiling. I don't want to go through what
is a profile, but if you, if you're interested in like what
the actual the actual output of profiling is, how
flamegraphs work and stuff, feel free to come by to
the Ask the Experts booth. I wanna make sure we have plenty of
time to talk about everything else. But yeah, this is the Explore
Profiles UI. You know, I just wanna show this just 'cause similar
to what Joe showed with this sort of like baseline and comparison workflow,
this is how you would understand, for example, you know, what is
the difference between, you know, a healthy period before something went
wrong and then an unhealthy period after something went wrong. You get this
output that shows you sort of in green, the good stuff in red, the bad stuff, and what codes you should look at
in order to resolve that. And so talked a little bit about that. Elijah is about to come on from Shopify
one of our customers who has been using profiling very effectively. And yeah, he is gonna tell you a little bit more
about how these profiling at Shopify to you know, to resolve some of
their performance issues. Cool. Thank you. Cool. I'm Elijah. I work at Shopify. Just with a quick show of hands how many
of you have purchased a product from a Shopify merchant within
the last year with Cool. It's about as many as I actually expected. Shopify is the platform behind
a lot of the merchants that you might shop on in North
America and around the world. So we have millions of merchants
across 170 plus countries. 10% of US' e-commerce
goes through Shopify, but we're in the
background typically. Cool. So profiling why does it
matter? Right? Black Friday, Cyber Monday last year,
145 billion requests, 60 million requests per minute, 4.1 billion in GMV. So a minute of downtime for
us can mean up to 2.85 million lost in GMV for our
merchants. So at Shopify, performance is critical for us
maintaining that reliable user experience for many of our shoppers. And in a large platform like
issues around latency or CPU they can have a real impact across
millions and millions of requests. So we really wanted to find a solution
that allowed us to understand at a more granular level what is
performance like for Shopify? Cool. So the challenge before
Pyroscope, what did it look like? Shopify is, Our core
app is a Ruby monolith. And so before we start using Grafana
Profiles we face challenges around like, how do we monitor this thing? We have this really large fleet of
machines and our solution at the time was you kind of put in this header and that
header would kick off a profile for the given request, and then you get that
profile and look at it in speed scope, but like one ad hoc request
does not tell the whole story. And so something that we wanted was
to be able to look across the fleet, across all of our processes and
understand how they were performing. In addition to that things like
Google Cloud Profiler just simply didn't scale for us. Cool.
So what's the shift? Well, the shift started about three and a
half years ago. I came to Shopify. We built our own internal
observability product we call Observe. It's on my shirt but that's built
on Grafana and we used open source Grafana. So we built our own metrics, we built our own logs and
our own tracings product, and we had a small team of about
three people looking at profiling. And this kind of speaks more to that
big tent mentality that Grafana has. We were able to use open source Grafana and connect it
with Pyroscope to do profiling. And so what what this
gave us was that granularity, the ability to dive in and look
across all of the requests aggregated across Shopify core, our monolith.
Cool. So what does that look like, right? And what does
success look like for us? At Shopify we have a saying not all software is great, but all great software is fast
and we really care about that. The faster we can render our sites, the faster we wanted to make it
easy for people to check out. So we actually do it 1% at a time and we kind of just
kind of iterate, right? So little changes across a fleet
like ours make a big impact. So on CPU we've done this
multiple times where we'll have 1%, 2%, 5%, we've even seen up to 20% wins
just by looking across the fleet, digging in and finding where
we're spending time in GC
as well as allocations. And so speaking of allocations,
Ruby's Garbage collection that means we have a lot of,
we do a lot of allocations, which means if we can reduce the
amount of allocations we have, we also reduce the amount of time we
spend in doing garbage collection. And then on the front we use Ruby on
Rails. We're proud that we are a monolith, like I said but that's built
on open source components. And so anywhere we can
optimize the Rails apps or make contributions back there, we can then roll that out across
Shopify and reap the benefits of those optimizations across
all of our apps. Okay. So yeah, so Pyroscope actually
for CPU we saw a lot of performance benefits that just
from analyzing across thousands of requests. So before we
could not look at like, what was this given controller
and this action doing? And now we can do that across
any controller at Shopify, across any app across our entire fleet. And so that drill down allows us to
dig into places and optimize them. Specifically one of the things
that we were able to optimize was aggregating the stack profs
object profiles in Ruby. We were able to kind of reduce those
and then that reduced the amount of allocations, which meant we were
able to reduce the amount of garbage. And then taking that, we're able to roll that out across
all the Ruby apps at Shopify. So then the performance profiles
got a lot better across Shopify, which actually translated into
actual performance benefits for more reliable checkouts. And then here you can see these
are actual contributions we've made back to the open source
and back into rails using optimizations that we
found from Pyroscope. So things like active record. Internally we use StatsD to
measure a lot of our internal cluster. So that's our protocol. We migrated from a vendor that
emits StatsD I'm not gonna name them last year. However one of our core
apps emits a lot of metrics and these metrics grow with time. And we found just by connecting
Pyroscope and looking at the profiles an optimization that led to a 20%
CPU reduction across our entire fleet. So, yeah I'll just
show this really fast. We have many apps at Shopify
and that are written in Ruby. We have our own profiles processor. This is kinda how we do it
and takes the Ruby profiles, transforms them to p-prof and
writes them to Pyroscope. Observe, again, that's our open source in-house built
Grafana observability tooling and our developers get to just come in. And then one of the best things for us
by enabling continuous profiling across all of our applications is now that
engineers don't have to think about it, right? They don't have to go like, "How do I get the profile for this
thing?" We just do it automatically. And that was a big win for us. And so now they can focus in on going to
find the optimizations and hunting for places to improve. So
last thing I'll say here. One of the engineers on my team or at
our, at our company focused on efficiency. Once we got continuous profiling onset, I have no idea how I did my job
before continuous profiling. And so just wanna shout
out. Thanks Pyroscope. It's been really awesome to work with
this team as well as the three engineers that do all of this work for
us at Shopify. And so yeah.

