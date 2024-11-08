# Navigating Observability at a Shipping and Logistics Company | DFDS | Grafana

DFDS is a historic pan-European shipping and logistics company. Jan, the Cloud and Automation Architect discusses the ...

Published on 2024-06-13T21:53:05Z

URL: https://www.youtube.com/watch?v=ggQIrIcXND0

Transcript: All right. Hello. Can you
hear me? It sounds like it. This is me. My name's Jan. I am the cloud and automation
architect at DFDS. DFDS is, if you don't know it, a pan-European
Shipping and Logistics Company. So that some of the things that we
have done and why we've done it makes a little bit sense. I'll spend a very
short amount of time setting the stage. This is one of the first
DFDS ships. It's a steamship, so it's a very old company. I think most Danes nowadays mostly
know DFDS from this cruise ship, but 2024 DFDS is actually kind of big
and much bigger than we think it is. Rail, trucks, e-trucks,
terminals, and very, very big route map across
Europe. We are in Turkey, all across the Baltics,
North Sea, and Gibraltar, I need to find an excuse to go in
there and inspect something, I think. 17 and a half thousand
employees and three data centers with 450 people in the tech group, all serviced by a comparatively rather
tiny five person platform group, which does everything related
to developer platform. As with so many other companies we are, we
have data centers, core data centers, and land. We also, two of
the major public clouds, AWS and Azure a little bit oddly. We also have almost a hundred data
centers that are floating around somewhere and intermittently connected Like any other old enterprise,
we have a vast variety of stuff. We have the hyper modern
microservices, serverless going ranging all the way
to yes, really old stuff. Quite a few visual basic
six two layer applications, and a bunch of third party appliances
will have no effing idea what they are and what they do and how
to instrument anything. We will this'll be an interesting journey. I will spend the next 15 minutes, it'll be a very fast talk
running all of these four topics. So in Business speak, what were the
drivers for us even starting this journey? We want to be cost effective. The margins
and logistics is surprisingly small. We want to be very effective. We also want to improve incident
detection and resolution time. One second. Yep. We also want to be more effective in
resolving incident as I think if anybody ever set through an incident called where
there's 45 people washing their hands at the same time, you can
probably relate to that if this is not a highly regulated
industry, fortunately. So we, we don't, not like a bank or, and we're not like a
aerospace manufacturer and
we don't quite have all these high requirements, but we are
seeing growing regulatory pressure, especially within cybersecurity, and I think that's a
really good thing actually. But let me try to translate those
business needs to something that we can actually build a project on. Yes, sales journey reliability, because we want to very
reliably take your money Having taken your money. We also want
to deliver on that as that's also, you know, kind of important for
two reason both because, you know, we want to succeed in the market and we
want to give you our customers, you, us, and many others, a great experience. And we also want to try to avoid the
situation that we have seen a couple of times that where if there is a
operational problems in the terminals, this is what the Google Maps
traffic map around, for example, double terminal starts to look like, and then there very senior people start
calling our very senior people and we really don't want that. The third, first priority. Yes. that was not actually given any priorities
to all of this, spend less money And reduce complexity. That's
also an important thing. But I want to go back a little
bit to, I mean, what is the, what is our main actual problem? And that is that DFDS
is a very heterogeneous, very big organization across multiple
countries. When I joined DFDS as a distributor systems engineer
in 2018, there were very, very few microservices. They were
not on the critical production path, and basically it was just mostly
monoliths doing database calls to itself. But the picture now is
very, very different. DFDS
is unifying, standardizing, and there are many, many API
calls crossing business units, which means it's also a
much bigger problem to find
the root cause if something goes wrong. The example I
have here is just that, okay, so we have a very long call chain,
it's crossing four tribes, maybe five, who knows what's going on? Why
is this request failing? That's, that's actually a cheap problem
figuring out why it failed. And sometimes it's not a matter of
things failing and you get an immediate response by some curve immediately
going up. You can also have a, I've had an interesting case last
year where there was a bug in some old Java system. It started sending a few buyers of spaces
to another visual basic applications. And so it went, one message comes over
and the visual basic things goes, what? You're talking empty, empty spaces to me, I will send you free and this empty
spaces back. The other application goes, if empty spaces, I will send you an empty space for
each on new set and the other went, I will send you nine
empty spaces now. Alright, and there were two interesting
things about this that surprised me. The first one was this can actually
go on for a very long time. Considering the exponential
growth of that curve, it took quite a few hours before
things starting tipping over. The other thing is, and
I will lead it up to you, your imagination to
wonder how this could be, why was the end result that there was no
cooling truck capacity left anywhere in Denmark, But try to figure that out when you have
no observability and it's all a visual basic six, I think I'll skip a little bit faster
on this one because this is one of the advantages disadvantages have coming last. A lot of other people have talked about
this. We had a lot of the same thoughts, but like, what model do we want to go with for a
lot of the rest of our cloud platform? We have, we've gotten the second option to
deliver a product that's optional to use, but where people opt into using it
because it's just the easiest way to get stuff done. In this case, we are, yes, we're still offering a platform product, but there's much greater push from central
management to onboard to it because we have real issues. And I think your options
here will depend on how you, how great your need is and how
mature you are as an organization. If you start late there's likely to
be more recognition of the need for it from the business side, but you will also have factions that
have really love Elasticsearch or CloudWatch. Actually nobody
will love CloudWatch. But there will be factions that has
their own opinions about things. So there are advantages and disadvantage
is no matter where you are in that maturity journey. A little bit about scope and people
involved, I hope you can read it. We very early on decided that we wanted
to distinguish between application observability and physical
infrastructure observability. And that is, even that is a very
vague boundary. Fundamentally, we wanted to focus on customers
that were developers, DevOps, and the business users
using those applications. The other main group that would've been
obvious to discuss with was the physical infrastructure. IT people, the VMware people the network
group, the physical network group. But that just broadens the scope quite
a lot and I absolutely believe that the downsides to a one size fit all would
have elevated the upsides of going with a slightly narrow scope. In this case, I do expect it to start to bleed over a
little bit on it every once in a while. I also want to say now I distinguish
a little bit between application observability and infrastructure, but it's very essential to have the
application infrastructure here as well. Databases, API gateways, Kubernetes, all of the software defined
infrastructure basically. Yeah, sorry, I forgot to tap. In DFDS We have a, a very strong
enthusiast community and that's, that's absolutely a blessing, especially
with a very small platform group. We don't have like an official
enthusiast role or anything like that. Not an engineering fellow
or anything like that, but we make a lot of space for people
who are passionate about the craft. And we host tech talks and actually
take the boat on a yearly cruise around where people talk nerd
stuff for three days. So there's a lot of room in here and
we try to build that community in here. A little bit cynical to say it's a very
cheap way to get shit done when you have, don't want to pay for the,
for dedicated platform group, so you can take that as you want. So yes, I think having an enthusiast
is absolutely worth it. It helps a lot to drive something. There are some people in here
who are passionate about it. If you're going to Turkey for example, and you want to sell
them on observability, having people there who care about it
and that you have boosted and you are giving them a slot and you give
'em the credits and all this, it'll help so much in getting
your buy-in for this journey. So you will notice that there
is no center of excellence here. That also means that we actually also
depend on the enthusiast group to, as I said, provide free labor, but also to come up and help us define
the standards that are absolutely essential for this product's
project to succeed. I'm not going to claim it's easy to run
a project like this because you will have much less control over the output. Both because people might disagree with
you and they might need to spend a lot more time convincing them that
your idea is the right one. And maybe you'll lose a few
times, but it's generally okay. But you might also risk that, for example, if the logistics tribe has
gotten their needs met, then you don't have then they'll have
to bow out because their management does not want them to spend all
that much time on it anymore. So there'll be much more
cycling of people in and out. I'm going to skip a little
bit over quickly over
everything about architecture. I think the main takeaway I want to
make here is that to avoid multi-tenancy issues and to give as
much autonomy to people, we try to identify or rather
let people identify which gravity sensor that were like
if you a logistics tribe, you have the monolith application,
fine, you get a stack, you also have the microservices fine, you also get a stack and then you don't
have to argue about how that's set up and you can configure the collectors
and pipelines accordingly, according to your own needs. And because we want to solve the
distributed burden , Unless there's specific need
for anything to stay secret, all of the engineers can look
at everything that's coming in. Similar, we host the collector centrally to make
it more efficient for the developers, but we allow them to customize the
configuration just via git pull request. At least we're gonna try that out and
see how that works because it's not actually running it. People... There's different kind of people
in any company and in the world. We have those that are charging
ahead. That's super cool. We're also seeing a lot of people who
are, who like following the enthusiasts, copying them and taking
notes from the enthusiast. They really like to talk
about what they're doing. They also have pride in their craft, and so you can give them  and
they will drag a lot of these followers along for free. And
that's again, super cool. And then a lot of the enthusiasts will
hit all the teething issues and they'll be tolerant of that. The
followers will hit much, many fewer teething issues
somewhere down the line. The pragmatic, careful
people will follow along. And then I think you should just accept
that there's a segment that is going to be a pain in the butt to get
along. They don't want to, there's no business
needs, whatever. It won't, you'll never get to full coverage on this.
I don't expect that in DFDS at least, that's fine. I don't think it's an
issue. If there's a business need for it, it'll get fixed. We did plan out a lot of this. If you go back to what I said
about the third first priority here, cost efficiency. The idea was that we wanted to basically
set up Grafana Cloud and let people onboard to it and then let people shut
down all of the legacy and shadow IT observability solutions as quickly
as possible, saving us money. Then we will start to roll out tracing, then we will start going back to the cost
efficiency thing by showing people how much money they were spending. Then
we could start with SLIs and SLOs. It is all great plans and then it ended
up with the vessels at the end because that's actually the hot part here with
those floating things that are only connected every a few
hours every seven days. And by that plan, we should be
somewhere around here. The reality, well, okay I still, I still think the arc of
the plan is sound. Okay. I mean starting from the core
and growing out from that, that was sound maybe putting up artificial
barriers for which features people could use. That was so we're not doing that
anymore and that's cool. Why stop people if they, if they have a need for tracing and they
can demonstrate the value, super cool. And we are already the having had some
people who'd give tech talks to the rest of the DFDS about the value
and what you can get out of it, and that's work taking off
my plate. Again, super cool. I'm not going to bore you going through
every single initiative we have done to get some buy-in for this, but
there's two I want to mention. One of 'em is that like, I think Novo Nordisk also did we have
put preconfigured packages out there that people can plop into
their own applications. So that becomes really easy to onboard
and they're opinionated because we don't, I mean they had come in
with some pre-configured
defaults that make it really easy to onboard. We don't need
to solve every situation. I mean, fortunately here we are not Grafana, we don't need to have a very
generic solution. We can
focus on our narrow needs. So that's fine and it helps
a lot of people very quickly
for for least amount of effort. The other thing I want to highlight here
is that Grafana has a lot of teaching material and, and really cool workshops. I have been in the workshop with Mathias, I think he's maybe out
in the hall somewhere. He's really good at having workshops
and you use those resources. I mean, they're free and they're there,
they are for you to be like Grafana, so you start paying them money. That's
super mutual benefit here going on. Lessons learned. Yeah, so lemme, yes, sorry. I think be realistic about how fast this
thing can go and how much work. It's, it takes a lot of time. I don't know exactly where
this misconception in DFDS turned up, but I do know that somebody at the senior
management level thought that, hey, we'll sign the contract by 1st of January
and then by the 1st of April we'll be completely done. And then needless to say, that has not happened and I
did not expect it to either. So identify user journeys.
Like I said before, if you really want your sales process
to be reliable and it's crossing so many different tribes to get there, you need to have somebody to shepherd it
all the way through. Governance model, skipping all that. Yes, it's a
strategic decision. It needs buy-in. You can only go so far
with bottom up enthusiasm, at least if you are DFDS's size, if you are a small startup or scale up
and absolutely I don't think you then you can sneak it by management, but you
can't do that at our size. Alignment. You need to agree on how to use this
thing and how what to call things because otherwise things will not be
compatible and you cannot find it. I've dropped some examples, so we will
not go through the many in great details. But also think about the
more alignment that you have, you're also raising the bar for how
much effort people have to put in to buy into this thing. And that that means that they are
more resistant to opting into this thing and it also means that they are, even if they do implement it,
they will probably do so poorly. So try to aim for some reasonable amount
of effort for people to onboard to this thing. Now I said what's, what's, why is it important to align
on namings for example? Okay, let's see that you want to
do a super simple query. You want to know what is the uptime
metrics of all your production services. And I'll ask a rhetorical question. How many ways can we express for every
given service that is a production service? Yes, you can do that. So it does, I count as 14 . So you need to agree on about what to
call one. Is it E-N-V dash production. Is it E-N-V colon production?
Is it prod, non-prod, P, PROD or whatever production is
called in Turkish? I don't know. I also saw a couple of those local
languages. That's really weird.  Regulatory, super boring topic. But it actually cost us
a month in the beginning. When the security architect stopped
by and said, Hey, it's super cool, we got this thing. Can you make sure that
we now live up to these requirements? Then he had this as a long piece of text. I took a small example up here. So you should give access only
to account with business need. What the heck does that
mean? I don't know. Okay, so now I have to talk to
exactly how do I talk to, because I know now if I go talk to
the GDPR team, oh, that's dangerous. Let's not talk to the GDPR team.
 Should I talk group legal? Hmm. Oh no, that's
probably also dangerous. They ended up getting the
CTO to sign off on that. He accepted the global reach
thing that I mentioned earlier, simply based on giving him an estimate
of a more granular access solution, how much engineering effort it would
take for people to have some sort of opt-in. So it, so that's
don't do that . And also this is your thing, right? All of the certifications that you
see that this is this GDPR compliant, all the thing, it only covers
the vendor's part of it, the things they can control. So it really is your
responsibility to get this right. When it comes to GDPR, well, the easiest way to not run into GDPR
issues is to not allow any GDPR data. So tell people they are stupid if they
send GDPR data to the logging system. Also, plain text password is
also bad. And then you can, you can use collector configuration
to fill out the most obvious. There's also some plugins. I don't
think Grafana Cloud has it yet, but there are also plugins on the server
side where you can scan through leakage on some systems. Financial. Also boring, but still
interesting. , I was kind of surprised and I think
everybody is that no matter, I mean you, you do an estimate, right? You
go through and count, I think, I think I probably have I'll
have 500,000 metric series. You'll have at least four
times as much, maybe 10. Now, the positive side is at an incredible
large proportion of that is complete garbage, worthless garbage. So there's plenty of room to optimize
as long as you set aside some time to actually do that. I'm really
running out of time now. There's tools available use them. One example here is that a lot of the
people tooling you will get, right? It has a ton of metrics
points that is sent out. And then you can use a data metrics on
Grafana Cloud to find out how much we actually not using, well, we are not using 99% of the thing
we're actually paying full price for, you know, every one of those 26,000
metrics is actually costing
you money and you're using 1% of them. Great. And some of them are really
over configured in my opinion. I saw one that had had host IP, host
name, fully qualified host name, file path it was running from, file path
it was loading the configuration from, and now every one of those escalates
into quite an analytics explosion. So it runs up really, really quickly. Yeah, set up a showback loop or
feedback loop so you can see your cost. We're gonna use Grafana
for that. Practical. We've had some issues mixing old and new. I don't think I have a one size fits
all solution to this, so just be aware. It might happen if you, if you run some of the old stuff and
you put a collector in that scrapes, both all the new stuff some, some issues Use as somebody also mentioned, it was a really great tip to say that you
can chain collectors and you can apply a configuration to them so you
can do a lot of local processing. Really use metrics or
logs wherever possible. It is much cheaper to send a
series of numbers than to have a lot of log lines that say the CPU load
is now 50%. The CPU load is now 60%. The CPU load is now 55%. Why are
you laughing? It's not a joke. Yes. Remember your infrastructure and I
was told I need to have a call to action slide at the end. So this is
it. It is my claim that modern, modern architecture, especially in
enterprise, is really complex. Yes, Dall-E created that
one. And I think nobody, none of us would want to fly a modern
airplane if there were no readouts for the pilots or anything like
that. So I think it's, it's, it's fairly self-obvious that
we want to have some insights, the instrumentation in how
our software is working. And I think that in a lot of
cases you will pay a lot more money if you don't have a observability
strategy and implementation. I went five minutes over time
I don't know if we have time, otherwise I'll also be
the networking later.

