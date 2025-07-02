# Why Open Source is in our DNA at Grafana Labs | GrafanaCON 2025 Closing Keynote:

Published on 2025-06-07T05:32:27Z

## Description

In the closing keynote of GrafanaCON 2025, Grafana Labs CTO Tom Wilkie reflects on the enduring –and evolving – importance ...

URL: https://www.youtube.com/watch?v=mWdVsxRLb6k

## Summary

In this video, Tom, the CTO of Grafana Labs, discusses the significance of open source in the company's operations and overall strategy. He reflects on a previous talk by Raj, the CEO, emphasizing that Grafana Labs is becoming one of the largest open-source companies amidst a shifting industry landscape. Tom outlines three key reasons for the importance of open source: it helps find customers by allowing engineers to deploy Grafana freely, it disrupts the proprietary observability ecosystem by promoting interoperability and reducing telemetry costs, and it fosters the best software development practices through community-driven collaboration. Additionally, he highlights how open source serves as a "cheat code" for leveraging AI, as the community-generated content aids in training models that enhance their software. Overall, Tom's talk underscores Grafana's commitment to open source as a core aspect of its identity and business strategy.

# Closing Keynote by Tom, CTO of Grafana Labs

Thank you, Matthew. Thank you for having me. I wonder if this is going to work. I've asked the team to add a laptop at the last minute, but we won't get to that yet anyway. 

Hello, I’m Tom, the CTO at Grafana Labs, which is still quite a strange thing to say. I wanted to spend the next 10 to 15 minutes discussing something very important to us at Grafana Labs.

### Open Source and Grafana Labs

How many people were here for the last closing talk last year in Amsterdam? A few of you? Well, obviously, Carl, I know you were, and Richi. Raj, our CEO, gave a talk about how important open source is at Grafana Labs. He made a provocative statement that with all the recent licensing changes and shifts in our industry, Grafana Labs is becoming one of the biggest open source companies in the world. This is thought-provoking, depending on your definition of open source.

I wanted to elaborate on why open source is so important to us at Grafana Labs and give you an explanation beyond the usual reasoning. 

1. **Finding Customers**: Open source is crucial in how we find customers. I'll elaborate on this shortly.
  
2. **Disruption of the Ecosystem**: Open source was important to us in disrupting what we saw as a stale ecosystem a decade ago.
  
3. **Building Software at Scale**: Finally, leading the engineering organization at Grafana Labs, I believe open source remains the best way to build large software projects at scale.

### Finding Customers through Open Source

Has anyone here read the pamphlet *The New King Makers*? It’s a short read, and I highly recommend it. The theory is that in modern businesses, software engineers make the difference. They help organizations be competitive and ship new capabilities. Even in traditional sectors like retail, with the shift online, software engineers are crucial.

What do software engineers love? They love autonomy. They are often the ones making critical decisions themselves, feeling empowered to do so. This is how Grafana Labs penetrates businesses today. Engineers choose to deploy Grafana to solve their own problems because it’s open source. They can do this without worrying about onerous licensing conditions. 

Every organization in the world is using Grafana in some way, sometimes without even knowing it. Our job when selling our software is merely to find the organizations that we can help beyond the open source.

### Disruption of the Observability Ecosystem

The second reason is about disruption in the observability ecosystem. Most vendors, at least ten years ago, were still proprietary, selling software where the code was secret, and the only way to use it was to pay. Unlike other infrastructure software categories that had shifted to open source, observability was still ripe for disruption.

We started with Grafana and Big Tent, prioritizing interoperability. Surprisingly, we are still one of the only vendors that allow you to derive value from our visualization tools without having to store your data in our systems. 

Competitors require you to put your data in their systems before visualizing it. We also contributed significantly to projects like Prometheus and Loki, driving down telemetry costs. This is beneficial for everyone, enabling better insights and monitoring capabilities without prohibitive costs.

Moreover, with the advent of OpenTelemetry, the observability ecosystem is being disrupted once again. Users now only need to instrument once, with that instrumentation sent to any technology out there. I am proud to be part of this movement that disrupts what I saw as a stale ecosystem with proprietary technology.

### Building Software with Open Source

The third significant reason is that open source allows us to build the best software. This isn’t just an idealistic view. We aim to encourage good development practices internally at Grafana Labs. We focus on documentation and asynchronous communication to help new team members understand our practices. 

Open source fosters this environment. It allows us to be a remote-first organization with teams in over 50 countries, enabling a healthy on-call culture where teams can operate in a follow-the-sun model. This is crucial since engineers don’t have to be on call at night, which is something I personally value.

We may not compete with large tech companies in salaries or perks, but we can offer the freedom to live and work anywhere. This is particularly appealing to engineers who may not want to live in big cities. 

### The Cathedral and the Bazaar Model

Another significant aspect is the *cathedral and bazaar* model, a concept that describes the difference between proprietary large organizations and loose-knit communities. The cathedrals operate under a management class dictating what should be done, while the bazaars are chaotic markets where people pursue their own interests. 

At Grafana Labs, we build software by encouraging engineers to solve problems they encounter. We give our engineers a week every three months to work on whatever they want during our hackathons. They record a five-minute video about their projects, and the winning project is rewarded with a cash prize. This encourages autonomy and empowerment, leading to projects often featured at our keynotes.

### Open Source as a Cheat Code for AI

Lastly, I want to mention that open source is our cheat code for AI. Recent foundation models have been trained on content created by the community. They already understand how to use our software due to the wealth of blog posts and documentation available. This advantage allows us to utilize foundation models without building our own datasets, unlike proprietary vendors who struggle in this area.

The collaboration between Matt and Cyril to build the Assistant is a prime example of how quickly we can deliver impressive technology using open source principles.

### Conclusion

In summary, open source is how we find customers, disrupt a stale ecosystem, build software effectively, and leverage AI. While we have around 6,000 contracted customers, we cater to tens of millions of Grafana users. Open source is integral to our approach and culture at Grafana Labs, enabling us to innovate and grow effectively.

Thank you for your time. That's my closing keynote!

## Raw YouTube Transcript

Thank you, Matthew. Thank you.
And thank you for having me. I wonder if this is going to work. I've asked the team to very
last minute add a laptop to it, but we won't get to that yet anyway,
so hello. Thank you having me. I'm Tom. I'm the CTO at Grafana Labs, which is
still quite a strange thing to say. I wanted to just spend
the next kind of 10, 15 minutes talking about something really
kind important to us at Grafana Labs. How many people were here for
the last closing talk last year in Amsterdam? Anyone? A few of you?
Handful. Okay. Well, obviously Carl, I know you were, and Richi. Raj, our CEO, gave a talk about how important
open source is at Grafana Labs, and he put forward quite a provocative
statement that with all of the recent licensing changes and with all of the
shifts and acquisitions that have happened in our industry, that Grafana Labs is becoming one of
the biggest open source companies in the world, which is kind
of a thought provoking, it depends on your definition of open
source I guess. But I wanted to riff a little bit on why open source is
so important to us at Grafana Labs. And I wanted to hopefully give you
a bit of an explanation beyond the usual kind of reasoning you
hear, right? So firstly, well, let's go through the
reasons, right? Firstly, open source is very important
to how we find customers, right? I'll go into a bit more
detail about that in a minute. Open source was also really important
to us to disrupt what we saw a decade ago as a pretty stale
ecosystem. And finally, and this one's dear to my heart, leading the engineering
organization at Grafana Labs, open source is and still remains to be
the best way to build large software projects at scale. So what do I mean about
open source is how we find customers. Has anyone here read the pamphlet
The New King Makers? It's a really short one. I highly
recommend you read it. The whole theory here is
that in modern businesses, it's the software engineers
that really make the difference. And they're the ones that help
these organizations be competitive. They're the ones that help
them ship new capabilities. And even in relatively traditional
businesses like retail, like it's still with the move online, still are the software engineers
that are making the difference. And what are software engineers
love? They love autonomy, and they're now the ones making the
critical decisions often themselves, like feeling empowered to do this, right? And that's how Grafana Labs gets
out into businesses nowadays, right? It's the software engineers out there
that choose to just deploy Grafana to solve their own, to
solve their own problems. And they can do that because
Grafana is open source. They can do that because
it's free as in beer sure, but also free as in freedom. They don't
have to worry about onerous licensing conditions. And this is key
to how we find our customers. Every organization in the world
is using Grafana in some way. Maybe they don't even know it. And our job when we're selling our
software is really just to find the organizations where we can help
them beyond the open source. So that's important. That's probably the reason that
most people think of when we say, why is open source important
to us as a business? They probably think it's all
about how we sell our software. And I'm not going to linger
any more on this one. I'm now going to talk
about the other reasons. The other reasons are the disruption
to this ecosystem and the ecosystem I'm referring to, of course,
is observability, right? In the observability
ecosystem. Most vendors, at least 10 years ago were
still proprietary. They
were still selling software where the code was secret and the only
way to use it was to part with money. And if you look in other infrastructure
software categories, that's changed. That had already changed 10 years ago. Obviously operating systems
was disrupted by Linux. Things like databases
with MySQL and Postgres, even packaging and distribution with
Docker and cluster scheduling with Kubernetes. Bit by bit all infrastructure
software became open source. And it was kind of weird to us a
decade ago that hadn't happened to observability and it was rife
for this disruption. So firstly, we did that with Grafana,
we did that with Big Tent. Our philosophy where we prioritize
interoperability and where we honestly are still surprisingly to this day, one of the only pieces of technology and
the only vendor out there that allows you to get the value and
the utility of Grafana, of our visualization tools without
necessarily using and storing your data in one of our systems.
If you look at all of our competitors, you have to put your data in their
system before you can visualize and understand it with their tools. Secondly, you then started to see with projects
like Prometheus where we do a hell of a lot of contribution to Prometheus
and projects like Loki, our log aggregation system where we really
started to commoditize the market and drive down the telemetry costs.
And this is good for everyone. This allows you to store more data, allows you to have better insights into
your systems and allows you to get out of the system the kind of situation
where maybe you can't afford to have good monitoring on your pre-prod
environments or something like that. And this is now a big trend in the
industry that the telemetry prices are tumbling and that you can do
more with less now. And finally, maybe the most recent one, as Ted
kind of talked about in the keynote, is OpenTelemetry where now the
observability ecosystems being disrupted again, where users now really only
have to instrument once and
that instrumentation can be sent to any technology
out there. So I'm really, really proud to have been part of this
movement to kind of disrupt what I saw as a relatively stale ecosystem
of proprietary technology
with this really cool open source. The third big reason though is open
source is how I think we build the best software and we being the world, it
is not just an idealistic view either. We wanted to encourage really good
development practices internally within Grafana Labs. We wanted to, you might think this is
weird for an engineer to say, but we wanted to make
sure we documented things. We wanted to make sure we wrote stuff
down and communicated asynchronously. So as people joined the projects
externally or internally, they could figure out why we
did things the way we did. Open source encourages that. It also encourages and allows us to be
the remote first organization that we are because we have these
asynchronous communication
practices because we internally run our engineering team in the same way
you might run a really big open source project. So this is key to us being remote only.
This is key to us being post geographic. And this allows us then next step to have
a pretty healthy on-call culture where we can have teams all around the world, I mean my engineering teams in 50 plus
different countries and we can have engineers all around the world be on
call for our services in a follow the sun motion. And this means engineers again, don't have to be on call at night
anymore. This is really important to me. I spent a lot of time being on
call at night in a previous life. It also allows us to
compete for talent, right? Engineers in these large
tech companies get fantastic salaries and free massages
and micro kitchens. Things we can't offer as a small tech
company. I mean, Anthony, if he's here, he'll probably offer you a massage, but we can't necessarily
compete like that, but we can give them the freedom to live
wherever they want. We can give them the freedom to work
from wherever they want. And especially if they traveling
around the world, if you like, not necessarily living in a big city, you can come and work at places
like Grafana Labs. But finally, and perhaps more importantly, the reason
why I think open source is the way, the best way to build software is really
the kind of cathedral and bazaar model. Again, this is another popular book that
describes the difference between the proprietary large organizations building
software and the loose knit community building software with the proprietary
large organizations being the cathedrals with their management class of the clergy, kind of dictating what people should and
shouldn't believe and the bazaar being the markets of just chaos where people
just do whatever they want and kind of scratch their own itches
and that chaos and autonomy and empowerment and that scratching your
own itch. That's how we build software in Grafana Labs. Every project that you've seen has come
out of a need to solve a problem that we had that an engineer sitting in
their home office or in a cafe or wherever they sit nowadays,
like thinking, oh, I can build a piece of software
that solves this problem. I can build a piece of software that
automatically instruments my golang - that would be Beyla. I can build a piece of software that
helps me store logs for my Kubernetes cluster without having to put them in
Elastic or in some other big fully indexed system - that would be Loki.
That's how I built Loki. And so we really encourage this motion
at Grafana Labs by giving engineers a week every three months to
just do whatever they want. We call it our hackathons.
We ask them one thing, we ask them to record like a five
minute video at the end of it, self-assemble into a team,
record a five minute video, and then we'll go through some rounds
of judging that result in a popular vote for the whole company. And the winning
project gets pretty big cash prize. We really want to encourage this. And those hackathon winning projects
go on to be featured at the keynote in GrafanaCON. Often. That's
how the Assistant started. That's how the Drilldown apps that
featured in the keynote last year all started. So we really want to encourage this kind
of autonomy and empowerment and really give our engineers the freedom to make
their own decisions about what's best. I will say this works really well because
we build software for other software engineers. I don't know how to
do this in other industries. So I'm glad I'm in this industry, but I firmly believe that's the best
way for companies to build software. And finally, I guess this
wasn't on the original slide. I kind of wanted to save this as my, one other thing is open source is
our cheat code for AI. And again, 2025 kind of have to mention AI, but this was a relatively recent
kind of realization for us. And I know Matt kind of touched on this
in the keynote where we learned that these new foundation models that have
come out in the last kind of six, 12 months, they were trained on the wealth of
content that the community wrote and published on the internet for us. They already know how to use our software
because there are thousands of blog posts on best practices
for building dashboards. There are thousands of blog posts on
what each individual Prometheus metric means and what the right metrics
to monitor Kafka are and so on. And they've been trained on this
information. So we didn't have to, right? As an open source company,
these foundation models know
how to use our software. This is something our proprietary
vendors that we compete with, they really struggle with that, right? They have to build their own
models and they have to invest in training their own building their own data sets
and training their own models to figure out how to use their software. We
just use the foundation models. This is how the hackathon, sorry, I
know I'm going all over the place. The hackathon that Mat and Cyril did to
build the Assistant was only two months ago. This is how we were able to so
quickly build such an impressive piece of technology like the Assistant and get
it into the hands of our users and customers so quickly. So this was a
relatively recent realization for us, but this is why open source
is so important at Grafana
Labs. It's because yes, it's how we find our customers. That only works if you don't
cannibalize too much of your community. We only have like 6,000
contracted customers, but there are tens of millions
of users of Grafana. Yes. Open source is how we've disrupted
like a really stale ecosystem, right? How we've commoditized telemetry, how
we've prioritized interoperability. Yes, open source is the
best way to build software. Something I'm very passionate about. And the culture internally within Grafana
Labs is that of a loosely knit open source community. And yes, open
source is the cheat code for AI, is how we've delivered such a cool AI
system experience so quickly and how we're hopefully going to get
it in much broader hands. And I'm not going to put
Mat and Cyril on the spot, but hopefully GA it in three
months. Yeah, maybe. We'll see. So that's my talk. That's
my closing keynote.

