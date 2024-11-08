# The Story of Grafana | Episode 3: Open (Source) for Business | Grafana Documentary

In 2014, Grafana Labs (formerly known as Raintank) was founded with one mission in mind: To build a sustainable business ...

Published on 2024-01-18T19:48:02Z

URL: https://www.youtube.com/watch?v=Q0q0pBnO-6E

Transcript: Yeah. Um, how do we get you to
work on this full time? Uh, well, so far it's been
sort of a hobby project, but after the summer I'll be working
full-time on Grafana and related things. Torkel decided that it's
time to give this a try. So he resigned from that place. Torkel left and he was
gonna do consulting. I did some consulting and I
did some talks on Grafana, and I got some open
source sponsors as well. I think that really helped me push
any plans of commercialization. I didn't really have any plan of
creating a company, I think. And that changed when, I
think, he met Raj and Anthony. This was really stumbling into it. Oh yeah. So the first time I found out
about Grafana, I was working with Raj, we had the startup idea. We knew we wanted to do something in the
monitoring space, something SaaS-based. Probably early 2014. Anthony and I were looking at a bunch
of different open source projects in the space, and we found Grafana. It
was a relatively new project, I think version 1.0
had just been released. We started using it first. We're
like, "Hey, it's open source. We can use this as the basis
of our product." And it
was just, it was fantastic. And Grafana just looked so beautiful. I just thought it was crazy cool from
the way it looked, the way it felt, the beauty of the interface. And we just reached out
to Torkel pretty quickly. That's the great thing about Raj,
right? He's a great networker. So we reached out and invited him to
New York for a week under the guise of "come and consult with us for a week.". At the time, I think he was pretty excited that
someone would pay him for consulting on Grafana for a week. We didn't actually do any work that week. We just kinda spent the whole week
talking, getting to know each other. We got along so well. We all had such
a great shared vision for Grafana. After that week, Raj and
Anthony felt like, "Oh, this Torkel guy might be good to
have on board in this project. And, not just use his open source project. We pitched him on the idea of starting
a company with us around Grafana. And that was how Grafana Labs started,
or as it was called back then, how Raintank started. Yep. Hi everyone. My name's Raj Dutt. I'm
the co-founder and CEO of Raintank. We're a brand new company. We've only
been in existence for about five months. Our mission at Raintank is to democratize
metrics and we think that our business model, which is open SaaS, can combine the best both
worlds of SaaS and open source. I'd say for a while there was
both a feeling of really positive elation, almost that the open source project was
beginning to get momentum and we were starting to see it snowball, but then for a while we were almost
panicking 'cause we couldn't really figure out how to monetize it and
translate it into revenue. My plan when I started working on it full-time was to make a
paid version of the open source product, like a pro version. But after we joined and
we created Grafana Labs, we were able to build a SaaS product, like an online service basically that was
using the open source project. So, our business plan was really around open SaaS. There were people that were comfortable
buying SaaS solutions and they had budget for that, and they
were used to that world. And then there were people who really
liked open source and open SaaS was just this word at the time that, I don't know, tried to describe what we were doing
as almost the best of both worlds. This strategy really enabled me,
for the first couple of years, to not think about
commercialization at all. And so we put everything in open
source and didn't need to make anything private, basically. We had some seed money and we
were able to hire people. I started as employee number seven. I
was the second engineering hire, uh, but only a few months later,
Daniel Lee joined, Dan Cech joined, Alex joined. We doubled
in size in a few months. I joined Grafana in 2014 to work on UX in the design side of the house. I believe I am employee 31. I think it was about 50 or 60 people.
Yeah, so we were like, a super small team. I basically go back very far with Torkel. So we grew up in the same neighborhood. Had known Raj and Anthony previously. Had worked with Torkel previously,
so we kind of knew each other. I hadn't met Torkel in that company, but he left that company I think two
months before I joined to work on Grafana, full-time. And I worked there
together with Daniel, Carl and Marcus. I didn't know anybody
here before I joined. I implemented a hiring
balance in Sweden. I said, "We can't hire any more Swedes." We were
gonna go remote first and we want to have people from other countries. There's a bunch of people in the
community. And the funny thing is, we've hired most of them,
right? Which is really funny in a cosmic sense. So then we sort of hired
random people on the Internet. Put out a job ad and they weren't
referrals, didn't know who they were. And Ivana's one of those
first people. Andrej as well. I didn't know even that
Grafana was a company, right? Like I had known just the project,
like, open source project on GitHub. Grafana took a good chance on me.
So I'm very grateful to be here. Daniel made me believe that
being new to Grafana and being a junior developer is kind
of my superpower because
I have a very unique view. I, at the time, documented a lot of my struggles
and how I overcame them. And at the time I wrote so many
blog posts and interestingly, these blog posts are still very
popular because I think those resonate with people and they always
come to them at the beginning of their journey. It's just super exciting.
And we have so many fun things that we hope to be able to do. Some of the first GrafanaCONs, one of
them was at the Squarespace office. There were so few people at the
time who were customers of ours, but everyone in that room was sort
of eager to help us, as a business, figure out how to take their money. And I just remember that
was a really funny feeling, that it was sort of something that made
me really appreciate the dynamic that existed between the company and the
community. Certainly in those early days. The whole theme in Grafana
2.5 is gonna be around empowering you with more
data source options. So we started adding support
for these other databases, but it was really cumbersome,
right? Bespoke sort of integrations, hard to maintain. I was really afraid of feature
creep and trying to cater to every possible user. I think what was the really big unlock
for us was we released this plugin system. And the plugin system helped because
anyone could develop a new database for Grafana without having to understand
how the rest of Grafana worked. And we could update these
databases without having to
update Grafana as a whole. So we started with data source plugins
and then later had panel plugins. Yeah, the plugin system was
kind of interesting given how impactful it's been in
the history of Grafana. I think the pie chart was one of the
primary reason for us building that. Pie charts are a pretty
horrible way to visualize data. But I can't remember if it was
the reason we created a plugin system. I don't remember it. I don't know
what happened. You have to ask Daniel. Yeah. That was the reason for
the plugin system in Grafana 4.6. I don't even know this is true. I don't
know if this is true. Tell me though. I don't remember. So one of the top photo issues for quite
a while was having a pie chart panel. So Matt Toback, who was
our head of UX at the time, or our only UX designer at the time. It sounds like he had a
team when he is head of ux. It was really against pie charts. We even have a blog post. I think
Matt Toback talked about this. He wrote the blog post. Pie charts just being not a great
representation... PowerPoint charts. No, you don't have to do it this way. If you have something that's 12%
and you have something that's 13%. Presentations that people are doing
'cause they think they have to; the way you represent data matters. He's not wrong, but a lot of people
like pie charts, so, you know. They're popular, right? And
you can't argue with that. You've gotta give the
people what they want. The point of the plugin system
is obviously to extend Grafana, but it made the problem of, not being forced to accept PRs that
you didn't want, really much easier, because now you could actually have a
way for those contributors to say, "Okay, but you can actually
rewrite this as a plugin and maintain it yourself." So yeah, that's
the beauty of the plugin system, is that it keeps the core of
Grafana easy and maintainable. I can validate that a big
reason for the panel plugin was, shall we say, a distaste
for the pie chart. I think that probably sounds right. The big tent approach has really
defined a big part of what Grafana is and it remains to us kind
of amusing that in the observability space, no one else is a big tent, right? It's almost strange because when
you look at, say the BI space, you'd be laughed outta the
room if you weren't big tent. So for us it was always a question of
why isn't everyone else kind of more neutral? And I think it's
worked out well for us. There's never a one size fits all. There's always this mix
of different data sources, different vendors because different
vendors might have different strengths and weaknesses. Most of that
came from Raj wanting a different company that was more
open and friendly to competitors. We want to have good relationships with
them and we want the experience for our users, that happen to be
using them, to be good. 10 years ago, you'd sell this kind of software by
taking the CIO out to steak dinners and playing a round of golf. The developers would learn months later
that a multimillion dollar deal had just been done with Company X and like it? We
don't care. It's what you're gonna use, right? And that isn't really the way that
software is bought anymore. You know, 80 plus percent of our overall
engineering time goes to open source and a lot of times we start
projects as open source, then figure out how to layer
on differentiation as we go. And we build software
for the practitioner. We don't build software for the buyer. I think it more easily allows us to
stay true to that mentality and not lose that North star.

