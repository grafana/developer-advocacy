# Cyara Shares Their Enterprise Observability Achievements with Grafana Cloud | Grafana Labs

For Cyara, a leader in AI-driven customer experience transformation, the journey to enterprise observability led them to Grafana ...

Published on 2025-04-03T16:59:37Z

URL: https://www.youtube.com/watch?v=Ms_R35KpRKk

Transcript: Right now for us across
multiple regions worldwide, thousands of servers are processing
millions of customer interactions. Some companies use a complex array
of tools to monitor this. Others, I'm told just cross their fingers
and hope at Cyara we found a better way, and that's why I'm excited to share our
observability journey with you today. I'm Brendon Ghumman. I head
cloud engineering at Cyara. My department comprises
specialized teams across DevOps, infrastructure engineering, SRE, and telecom domains that work
collaboratively to support our technology ecosystem. Together we are responsible for ensuring
the reliability of our global SaaS platforms, maintaining
24/7 operational support, implementing AI capabilities, and upholding rigorous compliance
and security standards. You see now the most familiar
slide from today. Please take note, scan the QR code and have your
questions ready for me at the end. Need to get better at my clicking game. Let's start by looking at
what we'll cover today. I'll walk you through our journey from
why we needed to evolve our observability approach through our evaluation of
Grafana to the impressive results we've achieved. But before we dive into
the observability transformation, let me give you a quick snapshot of
the scale that we are operating at. As a global leader in CX
testing and monitoring, we support Fortune 500 companies
across multiple regions, handling billions of customer
interactions through our cloud native architecture. This scale
brings unique challenges, which brings us to why we needed
to transform our observability. Our journey to Grafana began
at a critical juncture. Our previous monitoring solution's
contract was up for renewal, triggering a comprehensive
market evaluation. The renewal provided the
perfect opportunity to reassess
our observability needs and explore more innovative options. What started as a routine contract
review transformed into a strategic shift that ultimately led us to Grafana. Why Grafana you ask? The strategic
advantage, well, as you can see, there's a lot that comes
out of the box with Grafana, it's interconnected with
other systems within Grafana, there's cost efficiency. Of course, Grafana for us came in at a 30% lower
cost than what our previous vendor was and provided a whole
lot more options to us. It wasn't just about
ingesting logs into Grafana. We could also plug in
multiple data sources, and I'll give you some real world
examples later on how that helped us. The alerting system's amazing
and it's all nicely centralized. Instead of alerting coming
from different places for us, it's now coming just from
Grafana. Access control. We can give specific permissions to
specific groups within the organization, so some have more access,
some have less access. Some can only read the information in
Grafana, others can read and act on it. And I've also got a real world example
on how API integration helped us to innovate and succeed. So before we dive in, a quick recap
of the challenges we were facing. We have complex systems that are
distributed across the globe. We have multiple product lines that
are growing organically and we are also increasing number of product
lines through acquisitions. We need to be able to monitor
these in real time with real time insights, not just
insights that we can look at, but insights that we can also
action. And by actionable insights, I don't mean someone has to do something. Sometimes an actionable insight
is we don't have to do anything. The information is with us. We look
at it and go, yes, this is great, nothing needs to be done. Cost
optimization is important. We started off on a really good footing
by having Grafana come in at 30% cheaper for us, but then we also used Grafana to optimize
other costs on our infrastructure. Last but not least, we were
good with incident management. With implementing Grafana,
we've become amazing. So what were the key achievements
for us? Like I've mentioned before, incident response became much better.
Alerting is all centralized in one place. We get lots of reports out of
the box from Grafana. Again, I'll show you some examples.
Monitoring of course, but compliance is a big one for me. I'm sure there's people in this room
that work for companies that service customers on a global
scale. And these days, these customers are asking for their
data to stay within those regions. Whether it's data generated in your
platform or it's log data or metadata, they will not extend their contract with
you or new customers will not sign on with you unless you can prove to them
that even your telemetry data is staying within region for them. And that came to us from
Grafana out of the box. Alright, I'm going to dig into
some real world examples now. This is a beautiful picture for me.
It is my favorite picture right now. Well, I'd say fourth favorite because my wife
and kids occupy the first three spots. This is my fourth favorite picture. My
own profile picture would be after this. Why do I love this picture?
That one on the top laser point. Yeah, that one on the top. I don't know how easy it's to
read from back in the room, but I'll give you a read out of it. I came into our Grafana system
at a very opportune time to make screenshots for this presentation, and I was looking at a system integration
testing just before a release. So it looks like someone was doing a
heavy load test to make sure that whatever changes were made in this sprint
didn't negatively impact our system's ability to perform under load. In sort of a 15 minute window, I can see about 11 million
logs being generated. And out of those 11 million logs,
there's only 11 error logs there. That's pretty much nothing. But what that tells me is our system
stood up to scale under such heavy load. Also, Grafana didn't crash
under that kind of load. It kept up and it gave us
some good insights into how
our system was performing. Another reason why I love this
picture is I didn't have to create it. I didn't have to do anything.
All I did was go into Grafana, click on explore, pick the category
I wanted to explore, and there it is. As you can see, I can star it, I can add it to dashboard
or I can dig deeper by clicking into show logs. When I captured the previous
picture, I thought I was impressed. When I looked at this,
I was super impressed. So now my profile pictures now down
to number six, not even number five. What this is telling me again is okay, we had about 11 million logs
come in a 15 minute time window, but now I can see even deeper into
what that service was made up of. So in a real world example, let's
say this was a payment service. If we look at the second
row, first column, we'll see host name. This
service is made up of 89 hosts. So this is a really huge load
test that we were running. All of this performed well,
and from what I can see, I can now come in and pick
filters and say, okay, I want to slice and dice by such and such. Say this was an investigation into
something that wasn't working properly. The engineer that was investigating
this could just pick on the errors filter, pick any other
filters they wanted to, and then click on the share button and
send it to other people within their team. So no longer having to say, "Hey, I went in to refine. I looked at these logs and I clicked
on these other things and whatnot." No, someone's going and
investigating something that
click on the filters that need to and they just click on share, and the collaboration from
that point becomes very easy. All right. Alerting again
was pretty important for us. What we see here is pretty much run
of the mill alerting out of the box. We've got categories and we've
got different rules set up. So that to me is sort of the
run of the mill boring part. But what's exciting to me about this is
something that I didn't realize when we were setting this up. As we onboarded new people
and started looking at this, this became live documentation for
them to understand what the critical hotspots in our systems are. Instead of having to keep
Confluence up to date with things, the alerting panel shows us what
the critical hotspots for us are. They also then these alerting
rules start off conversations amongst new starters and their
teams and say, "Hey look, I was onboarded a month ago and I was
told that these pieces in the system are critical. I see that we are
alerting on three of the pieces, but not the fourth one. Why do you think that is?"
So it helps generate natural conversations instead of forced
conversations with new starters. So I'm really impressed with that
is a benefit that came to us that we didn't realize would be when we
set up the alerting dashboard. I also wanted to share with you
guys a story about innovation. So the backstory here is
before we were with Grafana, we had a service that
requires lots of heavy compute and under load we
need to spin up more of these machines. Before we were with Grafana, we were using the traditional approach
of scaling up using CPU or memory metrics. What we found with
that approach is, okay, it served the customer
well, but from our side, we were either scaling up too
early, meaning extra cost for us, or if we left it too late in the piece, then some of the results for some of
the customers on the load were delayed. They were still getting
the results but delayed. So once we started playing with
Grafana during the POC stage as we were evaluating it, we found that we were putting the
average queue time from this service into the logs. It was extremely
easy with the Grafana UI to extrapolate the average queue time
being written by multiple services, summed that over a period of time
take an average and then have an AWS Lambda called the Grafana API, to keep
pulling it at regular intervals to say, "Hey, is the average Q time below a
certain threshold?" If it is, do nothing, even if CPU and memory metrics
go plus to a hundred percent, the service is still performing well,
we don't need to scale up new instances, but if the average queue time goes up, then the Lambda spins up more
instances, and as the load comes down, the lambda's still pulling the Grafana
API Once the average fee time calms down, the instances are scaled back down. So hence helping us innovate and succeed. I spoke about cost optimization
before, and yes, Grafana, I'm saying it again,
came in at 30% cheaper. I'm sure Jim will be happy that I
keep saying this again and again. But it also helped us to reduce
our AWS footprint. So we had, how did we do this? We got real-time
monitoring out of the box. Based on that, we were able to intelligently right size. I mentioned earlier that we run a global
footprint across multiple regions. Prior to Grafana, we were running the same sort of
template across multiple regions. We had different number of instances,
but the templates were exactly the same. With real time monitoring
and intelligent insights through multi metric analysis, we could say region
one runs this template, region two and region three before
were also running the same template. But now we could say, for example, if region one's running
with 16 gigs and four cores, we know that the load in region two and
region three doesn't really even go up to 50% of region one. So we could bring
it down to eight gigs and two cores, for example. So how did we achieve that? Through another beautiful picture. Now
you may look at this picture and say, "What's beautiful about this? It's so too much for me
to ascertain from it." Yes, when you first come into it, there's a lot to look at here because we
are dealing with thousands of servers, but the way we've named our
servers, we can sort this by name. We know that certain servers,
the way they're named, they back certain use cases. So we can filter out the servers
that we don't need. And for example, we know that payment services are made up of these six servers. We'll only select those ones and then
we can see what sort of memory they're using under load, what's the CPU usage under load disc
usage and network bandwidth, right? And then we can go and rightsize
that across different regions. We know when our system's
under load through other logs, we can pick a time period like you see
at the top there the last few days. We can pick a specific time range
down to even the hour or pick a larger range, and that's what
helped us right size. Another key thing here was
we looked at our disc usage. Previously we were seeing maximum utility up to 60%. We were able to drop disc usage across
the globe and save a fair bit of money that way as well. The next thing to this was when
looking at a specific instance, we could dive even deeper into
these kinds of metrics. And again, these came out of the box, nothing had to be done from our
side to get these kinds of metrics. This one's showing that
CPU usage is pretty low, but at a quick glance you can see that
this is a memory intensive compute, but say this was a CPU intensive
compute. What I like about this one, sorry, wrong button. Say CPU was high at 50 or 60%. Generally in AWS, what you get
to see is okay, you get 50, 60, 70% CPU usage, but it's very hard to get the
breakdown of what makes up that 50% CPU usage. Grafana out of
the box will tell you, these are the top contributors to
your CPU and when your CPU reads, 50%, 30% of it was made up
by whatever that was. So it gives you further detailed
insights into how your application's performing, what you can
do to make it better. The last example I want to put in front
of you is some financial intelligence work that we were able to do. So this is still a work in progress.
What we have is a system where as customers consume
credits on our platform, if they breach certain thresholds, an alert email goes out to the account
management team and they go and have proactive conversations with the customer
to understand if that was what they were intending or if something
was misconfigured and sort of get in touch with the customer
before the customer comes to us with a build shot complaint. Again, all of that's good and it's working, but it's not coming from
a centralized place. It's emails and sometimes emails
get lost, they go into junk. There's no way to see whether a threshold
was passed or not unless you go and talk to the DBA to get 'em to run
special reports and whatnot. With this, we get a visual view, and
not just the technical teams, but the non-technical customer facing
teams get a visual view as well as to what's running close to red hot
from a customer point of view, where do we need to go and reach out
proactively instead of waiting for the customer to come to us. Just on that same concept,
this is coming from a database. We've been able to work with
our InfoSec teams to say, this kind of information in
Grafana is really useful to us. Let's sit down and work together with
some of the most common queries we get from customers and align on what values we can push to Grafana
that doesn't have any PII, PHI, PCI or any other customer sensitive data, but can help customer facing teams to run
a quick query and answer questions for the customer. So again, Grafana has become this
centralized place for us, not just in a technology domain, but also in helping serve
our customers better. Yeah, so ultimately our journey to Grafana
has not been just about monitoring, it's also adding business value for us.
We get lots of reports out of the box. We can create other reports
and put automation on them. We can set alerts on them and whatnot. We have unified visibility across all
of our platforms, across the globe, across our existing product lines, across
product lines that we acquire as well. There's proactive detection of issues
like we've never been able to do before. There's so much data for us that
our planning is now based on data. We are making data-driven
planning decisions now. There's a cross team collaboration,
as I mentioned before, when new people are on board, they
look at the alerts that are set up, and that sparked some conversations
that we've never seen spark before. There's enhanced availability for
all users. And last but not least, we've been able to have some amazing
cost savings because of this. And that's where I'd like to conclude
by thanking the Grafana team for helping us to bring business
value, not just observability, but also business value and helping us
to do more of innovation and be more successful in our business.
Thank you. Good job.

