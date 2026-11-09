# Why Some Roles Care About Open Source &amp; Why Others Don&#39;t: 4th Annual Observability Survey | Grafana

Published on 2026-05-13T23:47:11Z

## Description

Note: We're happy to share that since the recording of this video, OpenTelemetry *has* graduated from the CNCF! ------ SREs ...

URL: https://www.youtube.com/watch?v=67OBS1AknRE

## Summary

The show is titled "Why Some Roles Care About Open Source & Why Others Don't: 4th Annual Observability Survey," published on May 13, 2026. The speaker, Myrle Krantz, discusses the findings of the fourth annual observability survey, highlighting the increasing relevance of open source in observability across various business roles. Key topics include the relationship between OpenTelemetry and Prometheus, the importance of open source to different stakeholders, and the impact of AI on open source contributions. The survey revealed that 77% of respondents view open source as important, with notable regional differences in perception, particularly between North America and Europe. The discussion emphasizes the need for collaboration between roles to better understand the value of open source in observability.

Topics: OpenTelemetry, Prometheus, observability, open source, AI, survey results.

## Chapters

00:00:00 Overview of the 4th Annual Observability Survey
00:04:04 The importance of open source in observability
00:07:54 OpenTelemetry and Prometheus usage trends

Howdy. My name is Myrle Krantz. This is our fourth annual observability survey. We cover topics around open source and its importance in observability, which stakeholders are involved, and which new areas of the business are using observability tools. We are also very interested in seeing how AI is developing.

Last year, we conducted this survey and received 1,255 responses. This year, we received a little bit more, totaling 1,363 responses. We believe that observability is becoming more relevant, not just for IT, but for more parts of the business. I hope we will continue to hear from more people with different roles in your businesses.

Within the landscape of observability and open source, there are some things that may not have changed, but I would say the change is linear. One example of this is the interaction between OpenTelemetry and Prometheus. This relationship remains very interesting and relevant. OpenTelemetry and Prometheus continue to improve their compatibility, although there is still work to be done. 

However, there are also areas where the change hasn't been linear, and things are dramatically different, to the point of being practically unrecognizable. AI has absolutely rocked the open source world, and open source observability is no different. 

At a high level, we see that 77% of our survey cohort views open source as at least somewhat important. Our report doesn't include data about why you found open source important, but we do have some top-level quotes that support the ideas I've presented here. 

It's also interesting to note that the importance of open source varies somewhat by region. If we ignore some regions with lower response counts and focus on Australia, I apologize, but if you want me to stop ignoring you, you need to get more of your colleagues to respond to the survey. Comparing North Americans and Europeans, Europeans were significantly more likely to see open source as important than North Americans. This aligns with the years-long push by Europeans for digital sovereignty. 

I attended the Open Source Awards right before FOSDEM in Brussels earlier this January, and that topic came up repeatedly. Their current goals are to improve self-reliance. 

When we break down the importance of open source by role instead of geography, we notice that open source is more likely to be important to SREs, developers, and CTOs than to engineering managers and directors. I think you should probably be talking to each other about that, and I would be interested to hear what you learn from each other.

The survey doesn't cover why you think open source is important, so I will make a couple of guesses that might explain some of those differences by role. Open source does a lot for companies and individuals. I think executive concerns should include creating an exit strategy from your current observability vendor—not because you plan to leave, but because you want to be able to leave if necessary. 

We had an example of one of our customers who came to us because their observability vendor unexpectedly dropped them. They were able to change very quickly, likely because they had a solid open source basis. You might also want to leverage your ability to shift to another vendor during negotiations with your observability vendor. Additionally, ensure you have long-term support and an upgrade path for any observability components you rely on, whether those are SDKs, collectors, or any other pieces of your observability architecture.

There is a general belief that open source components are of higher quality because more people are working on them. Open source also tends to be better at interoperability across multiple systems due to open standards. Furthermore, it is easier to hire people who can use widely adopted open source projects.

However, it's not just executives who are interested in open source. Individual contributors, such as software developers and SREs, are also involved. At these levels, you are likely looking for the best solution to a problem. Open source solutions are often best in class and easy to evaluate because they are open. You also want to ensure your skills remain relevant when you move on to your next employer. Learning about an open source project that continues to be relevant is beneficial, especially if you need a solution that you can customize or make upstream changes to. If you discover a bug or need a relatively minor feature, open source gives you the opportunity to fix that rather than work around it.

Additionally, it's important to consider whether there are people willing to support these open source solutions and contribute to the open source technologies. This aspect may not show up in our survey results, but if we look at the contribution counts for OpenTelemetry, we see that seven of the top ten contributors are observability vendors. The remaining contributors, who are not directly observability vendors, likely include companies like Microsoft, Amazon, or Google.

This presents an interesting difference between OpenTelemetry and Prometheus. The contributors to Prometheus tend to have more of a user slant. Even if we can't see directly from the observability survey why you think open source is important, we did ask why you think OpenTelemetry is important, and those reasons are probably related. 

For instance, 37% of you liked OpenTelemetry because it makes switching vendors easier, while 41% appreciate it for its ease of adoption and management. This aligns with the reasons I listed earlier. It's especially interesting because OpenTelemetry recently attempted to graduate from incubation at the CNCF but was blocked on a couple of issues that the CNCF would like to see improved before graduation, particularly around ease of adoption and complexity. 

You are choosing OpenTelemetry for its ease of adoption, but the CNCF wants to see it become even easier. This may seem contradictory, but I don't think it is. Telemetry collection is inherently complicated, and while OpenTelemetry is making it simpler, simpler is not the same as simple.

If we delve deeper and compare some of the growth of OpenTelemetry to the growth of Prometheus in importance, we find that 74% of the respondents to our survey are using OpenTelemetry more or about the same amount as last year. Additionally, 77% are at least investigating OpenTelemetry-based observability solutions. This is very close to the 75% who said open source was at least somewhat important. Those numbers are roughly the same for Prometheus, with 77% at least investigating it.

However, when we move beyond that broad analysis and dig into what it actually means to say you are using Prometheus or OpenTelemetry, we see that Prometheus is still the more mature solution.

Who said, "Y'all are using Prometheus in all of your production workloads or the majority of your production workloads"? That's almost 40% of Prometheus users. If we look at those same numbers for OpenTelemetry, it's a tad over 20%, so about half of Prometheus maturity by that measure. 

If we compare that to last year's survey, the questions weren't identical, so this comparison might be a little misleading. However, it looks like OpenTelemetry usage has actually made relatively little headway in productionizing OpenTelemetry, while the productionization of Prometheus is pretty stable. It hasn't changed much, but that makes it more interesting that so many of y'all are saying that you're using OpenTelemetry more. 

This would be another opportunity for y'all to have a conversation and come back to me to tell me why these two things don't quite match up. If we look at the OpenTelemetry and Prometheus communities and what they're actually doing, we see that both communities are still working really hard to improve compatibility between these projects. 

At OpenTelemetry Unplugged in Brussels, beginning of February, right after FOSDEM, we had a lot of Prometheus contributors who came in and joined the group. So many people were interested in compatibility with Prometheus that it became an impromptu track at that unconference. There's an article that came out in The New Stack about this. 

Again, at KubeCon this year in Amsterdam, there were two different meetings for maintainers of both of those projects—OpenTelemetry and Prometheus maintainers—to come together. My understanding is they didn't schedule enough time, and it went out into the hallway afterwards for another hour and a half. One of the ideas that I liked the best that was discussed at OTel Unplugged is the idea of including the Prometheus exporters in the OpenTelemetry collector. 

I think the next piece that we need to dig into, and I'm looking forward to seeing what our AI people say about it, is how open source and AI play together. Some of the pieces of this puzzle are that open source is fundamental to the value of AI. AI trains on open source, and because all of Grafana's products are open source, AI works really well with our products. 

At the same time, we've got some interesting pieces where there is an increase in contribution to the open source projects—upstream open source projects, OpenTelemetry, and Prometheus. These projects are getting more and more PRs; they're also getting more and more CBEs generated by people who are using AI to generate that open source. We think that this will cause an increase in velocity for these projects. 

We're already seeing some increase in velocity for these projects, but it's also a challenge to keep up with all of these extra contributions. So, it'll be very interesting to see how this plays out in the next year or so because that rate of change is just accelerating. 

I think that y'all should go and check out the full results. You can go to grafana.com, and you can find them there. You can really dig in and slice and dice them, maybe see some things that I didn't dive into here. Thank you all.

## Raw YouTube Transcript

Howdy. My name is Myrle Krantz. This is
our fourth annual observability survey. We cover topics around open
source and its importance in observability, which stakeholders, which new areas of the business
you're using observability tools in. And also we're very interested
in seeing how AI is developing. Now we did this survey last year.
Last year we got 1,255 responses. This year we got a little bit more. We got 1,363 responses and we do
think observability is becoming more relevant, not just for IT, but for
more and more parts of the business. And I'm hoping we'll continue to
hear from more people with more different roles in your businesses. Within the landscape of
observability and open source, there are some things that
are maybe not unchanged, but I'd say the change is
linear. One example of this, the interaction between OpenTelemetry
and Prometheus, still very interesting, still very relevant.
OpenTelemetry and Prometheus continue to improve their relationship and
develop good compatibility. There's still work to do in there, but there's also some things where
the change hasn't been linear, where things are just dramatically
different so much so that they are practically unrecognizable. AI has absolutely rocked the open source
world and open source observability is no different. So at the top line, what we're seeing is that people who
see open source as at least somewhat important. Those people make up 77%
of our survey cohort. Our report doesn't include
data about why y'all found open source important, but we do have some top level quotes
that we were able to collect from y'all and they seem to support some
of the ideas that I've presented here. It's also interesting the importance
of open source here varies somewhat by region. So if we just ignore some of
the regions with lower response counts, look at Australia. Sorry, y'all, if
you want me to stop ignoring you, you need to get more of your
colleagues to respond to the survey. So I'm going to just compare the
North Americans and the Europeans. Europeans were significantly more likely
to see open source as important than North Americans were. And if we look at the years long push
of Europeans for digital sovereignty, this makes a lot of sense. I was at the Open Source Awards right
before FOSDEM in Brussels earlier in, what was it, January? And that was a topic that came up
repeatedly that their goals now are to improve their self-reliance. It's also interesting when we break down
the importance of open source instead of by geography, by role, we noticed that open source is more
likely to be important to SREs and developers and CTOs than it is to be
important to engineering managers and directors. And I think that y'all should
probably be talking to each other about that. I would be interested to hear
what you all learn from each other. What the survey doesn't cover is why
y'all think open source is important. So I'm going to make a couple
of guesses and this might also explain some of those differences
by role and importance to y'all. So open source does a lot of things for
companies and it does a lot of things for individuals. I think executive
concerns should probably include creating an exit strategy for your
company from your current observability vendor, not because you plan to leave, but because you want to be
able to leave if you have to. We had an example of one of our
customers came to us because their observability vendor
dumped them unexpectedly. They were able to change very quickly. I assume that's because they had a good
open source basis. You might also want to leverage your ability
to shift to another vendor in negotiations with your
observability vendor. You also want to make sure you have
long-term support and an upgrade path for any of the observability components
you rely on, whether those are SDKs, collectors, any of the pieces of your observability
architecture that you have to install, you want to make sure that
you can upgrade those. There's also a general belief that open
source components are higher quality because there's more
people working on them. And there's also open source tends to
be better at interoperability across multiple systems because
of those open standards. It's also definitely easier if you've
got a widely used open source project to hire people who can use
those open source projects. So those are concerns that executives
might be bringing. However, it's not just executives
who are interested in open
source as we just learned. We've also got individual contributors,
software developers, SREs, for example. I think at these levels, probably what you're looking for is
you want to find the best solution. You've got a problem in front of you, you want to find the
solution that best solves it. And open source solutions
are often best in class. They're also just easy to
evaluate because they're open. You also want to make sure that your
skills are relevant when you move on to your next employer. When you learn about an open source
project that continues to be relevant even if you have to switch and
you're looking for a solution that you can customize and
sometimes even make upstream changes too. If you have a bug that you discover or a
feature that you need that's relatively minor, open source gives you the opportunity to
fix that rather than work around it. I also think that there's not just buyer concerns or
individual contributor concerns that drive open source adoption. It also matters if there are people
willing to support these open source solutions and contribute to
the open source technologies. And this is where
observability vendors come in. These are just not very likely
to show up in our survey results. But if we go over and look at the
contribution counts for OpenTelemetry, you're going to see that seven of the
top 10 contributors to OpenTelemetry are observability vendors.
And the remaining ones, the ones that aren't directly
observability vendors probably are also observability vendors like Microsoft,
Amazon, or Google. If you look over, this is an interesting difference actually
between OpenTelemetry and Prometheus. If you look over at Prometheus, those contributors tend to
have more of a user slant. Even if we can't see directly from the
observability survey why y'all think that open source is important, we did ask why y'all think OTel is
important and those things are probably related. So 37% of y'all liked OpenTelemetry
because it makes switching vendors easier. 41% like it because of ease
of adoption and management. This definitely relates to
the reasons that I listed out. And it's especially interesting. I don't know if you all followed, but OpenTelemetry tried recently
to graduate from incubation at the CNCF and was blocked on a couple of things that
CNCF would like to see improved before graduation, especially around
ease of adoption and complexity. So y'all are picking OpenTelemetry
for ease of adoption, but CNCF would like to see it get even
easier. It sounds like a contradiction. I don't think it actually is. I think telemetry collection is actually
very complicated just by nature. OpenTelemetry is making this simpler, but simpler isn't the same thing as
simple. So if we go a litle further and we start comparing some of the OpenTelemetr
growths to the Prometheus growth in importance, we see that 74% of the
respondents to our survey are using OpenTelemetry more or about
the same amount as last year. 77% are at least investigating
OpenTelemetry-based
observability solutions. That's very close to the 75% who said
open source was at least somewhat important. And those numbers are
roughly the same for Prometheus. 77% are at least investigating Prometheus. But when we move beyond that sort of broad
strokes analysis and dig into what it actually means when we say using
Prometheus or using OpenTelemetry, what you all actually mean
when you say those things, we see that Prometheus is
still the more mature solution. So the number of people who said
y'all are using Prometheus in all of your production workloads or the
majority of your production workloads, that's almost 40% of Prometheus users.
We look at those same numbers for OpenTelemetry.
It's a tad over 20%, so about half of Prometheus
maturity by that measure. If we compare that to last year's
survey, the questions weren't identical, so this comparison might
be a little misleading, but if we compare that
to last year's survey, it looks like OpenTelemetry uses have
actually made relatively little headway on productionizing OpenTelemetry and that
productionization of Prometheus is pretty stable. It hasn't changed much, but that makes it more interesting that
so many of y'all are saying that you're using OpenTelemetry more. So this would be another opportunity for
y'all to have a conversation and come back to me and tell me why these
two things don't quite match up. So if we look at the OpenTelemetry
and Prometheus communities, what they're actually doing, we see that both communities are
still working really hard to improve compatibility between these projects.
At OpenTelemetry Unplugged in Brussels beginning of February, right after FOSDEM, we had a lot of Prometheus contributors
who came in and joined the group. So many people interested in compatibility
was Prometheus that it became an impromptu track at that unconference. There's an article that came out
in The New Stack about this. Again, at KubeCon this year in Amsterdam, there were two different meetings for
maintainers of both of those projects for OpenTelemetry and Prometheus
maintainers to come together. My understanding is they
didn't schedule enough time. It went out into the hallway
afterwards for another hour and a half. One of the ideas that I liked the best
that was discussed at OTel Unplugged is the idea of including the Prometheus
exporters in the OpenTelemetry collector. So I think the next piece
that we need to dig into, and I'm looking forward to seeing what
our AI people say about it is how open source and AI play in together.
Now, some of the pieces of this
puzzle are that open source is fundamental to the value of AI. So AI trains on open source and because all of Grafana's products are open source, AI works really well with our
products. At the same time, we've got some interesting pieces
where there is an increase in contribution to the open source projects,
to the upstream open source projects, to OpenTelemetry and to Prometheus. These projects are
getting more and more PRs, they're also getting more and more CBEs
that are generated by people who are using AI in order to
generate that open source. We think that this will cause an
increase in velocity for these projects. We're already seeing some increase
in velocity for these projects, but it's also a challenge to keep up
with all of these extra contributions. So it'll be very interesting
to see how this plays out in the next year or so because that
rate of change is just accelerating. So I think that y'all should go
and check out the full results. You can go to grafana.com and you can
find them there and you can really dig in and slice and dice them, maybe see some
things that I didn't dive into here. Thank you all.

