# Microsoft’s Open Source Journey: Advancing Authentication and Security in Grafana

Published on 2025-06-07T05:32:44Z

## Description

In this lightning talk from GrafanaCON 2025, John Naizer, Software Engineer at Microsoft, takes us through a story of innovation, ...

URL: https://www.youtube.com/watch?v=gr9adaEi4VM

## Summary

In this video, John Naizer, a software engineer at Microsoft, shares his team's journey of integrating Grafana into their workflow and how they contributed back to the platform. He discusses the need for a modern data visualization solution at Microsoft, leading to the development of executive dashboards that track metrics, manage incidents, and provide real-time updates on key performance indicators (KPIs). Naizer highlights Grafana's open-source nature, flexibility, and deep integration with Azure as key advantages. He also addresses security concerns, explaining the evolution of authentication methods and how his team developed a new feature for Grafana that allows for diverse authentication options based on the OAuth2 specification. The process taught him valuable lessons about collaboration and community within open-source contributions. Naizer encourages others to engage with open source and share their innovations.

# Grafana: Our Journey at Microsoft

Thank you. Wow. Thank you all so much! My name is John Naizer, a software engineer at Microsoft, and I'm super excited to share with you my team's story of how Grafana impacted us and how we, in turn, impacted Grafana.

## The Beginning of Our Journey

Let’s start from ground zero and rewind the clock all the way back to the beginning of our journey. Our organization at Microsoft had a clear need for a modern data visualization solution—one that is fresh, flexible, and keeps up with today's fast pace in the industry. This solution would lay the foundation for what we call our executive dashboards, a one-stop shop where leadership and teams can track metrics, spot trends, and make faster, smarter decisions together without getting stuck in the weeds.

These executive dashboards have three key attributes:
- **Tracking metrics**
- **Managing incidents**
- **Providing real-time updates** to our key performance indicators (KPIs)

## Why Grafana?

Now, I won’t give you the full Grafana sales pitch, but I would love to share a few reasons why Grafana was the obvious choice for us:

1. **Open Source**: This gives us the complete freedom to build our own solution that’s scalable, customizable, and designed exactly for our needs.
2. **Plugins and Integrations**: Grafana has an endless stream of plugins and integrations, maximizing the flexibility of our use cases.
3. **Portability**: The fact that it can be Dockerized and deployed anywhere is huge for us. This allows us to build and deploy a lightweight but effective solution, enabling us to move fast and tweak as we grow without getting boxed into a single setup.
4. **Deep Integration with Azure**: Grafana’s integration with Azure native data sources like Azure Monitor and Azure Data Explorer allows us to plug directly into our telemetry streams, building rich dashboards that display real-time data.

All in all, Grafana checked every box we had. It’s cool, flexible, scalable, and super developer-friendly.

## A Fork in the Road: Security Concerns

However, we had one fork in the road, and it has to do with security. First, I have a simple rhetorical question for you all: Who here has forgotten a password before? You all should be raising your hands! Here’s a better one: Who here has a family member that forgot a password, reset your shared account, and didn’t tell you? 

It's common knowledge that passwords are becoming obsolete for many reasons, not just the silly ones I mentioned. We’re seeing more things like two-factor authentication, passkeys, and more. Companies like Microsoft are driving security evolution, covering all aspects of security. As our CEO, Satya Nadella, puts it, “If you’re faced with a trade-off between security and another priority, your answer is clear: do security.”

With this mindset, we customized Grafana authentication for when logging into Grafana as a service. We were pleasantly surprised to find that Grafana offered two choices:
1. An **authentication proxy**, a DIY solution that puts the power in our hands to customize how we authenticate.
2. An **Azure-native authentication method** built directly into Grafana.

However, we quickly realized that this method didn’t support an authentication method we highly desired for our team. The authentication proxy was quicker to set up but required extra infrastructure and potential long-term maintenance.

Implementing our own Azure authentication method into Grafana would deepen our integration with Azure identity, meaning no additional infrastructure. The major drawback was the extra engineering effort and time needed to ramp up on Grafana’s codebase and the newer Azure features we would implement. 

This was the fork in the road. We could have taken the easy route and used an authentication proxy, but where's the fun in that? As software engineers, we dove directly into Grafana's codebase and built the solution we wished already existed—one that moves us closer to a future-proof security platform and hopefully makes life easier for others, both inside and outside Microsoft.

## Introducing a New Authentication Method

What was that highly desired authentication method we had in mind? Let’s think of Grot as a bouncer at a super delicious restaurant. Only people who know the secret shared password can enter. You walk up, bend over to Grot, whisper the secret password, and enter. 

Now, what if instead of a secret shared password, he passed out public-private key pairs—certificate-based authentication? In this analogy, both methods have one thing in common: **what you have determines who gets in**. 

But what if I told you there was a third way? Not based on what you have, but who you are—analogous to a fingerprint. Think of Grot as an identity provider, like Azure Active Directory, with you being the application. 

Internally at Microsoft, we call this **managed identity**. Just like a fingerprint, you never have to worry about your identity expiring, completely eliminating the need for credential management. No more remembering secrets or rotating certificates!

### The New Feature

What did this new feature look like? A beautiful screenshot shows a new field under Azure authentication configuration called **client authentication**. This gives users the ability to choose more than one authentication method when logging into Grafana. This is the idea of accessible security—putting the power in the user’s hands to decide how they want to authenticate without unnecessary hoops.

The authentication model we built can be adopted by every other native identity provider inside the service. And here’s the kicker: it’s based on the OAuth 2 spec, so any identity provider can create their own implementation and add it as a client authentication option under their configuration.

## The Open Source Contribution Journey

Going through this open-source contribution process was a roller coaster. It was my first time contributing at this magnitude, and it taught me a lot about collaboration, patience, and how many pull request comments it takes to build something that lasts and gets merged into the main branch.

Not only are you building a new feature, but you’re also building new relationships with the maintainers of Grafana and the community—everyone as passionate about Grafana as you are. At the end of the day, you're not just pushing code; you're earning trust one pull request at a time.

**Trails need blazers. Paths need finders. Problems need solvers.** If any of you are interested in contributing to open source, specifically Grafana, be bold. Start small, dive into Grafana's codebase, and find contributors working on the same pain points. Reach out, partner up, and champion the solution together.

My advice: **email, email, email. Be persistent. Be bold.**

If you’re curious about the work we did to make this happen, scan the QR code to view the GitHub pull request that got merged into the main branch, adding this new feature. 

### Final Thoughts

Again, go light your own torch and don’t be afraid to pass it on. Thank you all so much! I can only hope that our story resonates with each of you. I’m grateful for the opportunity to share this story with you all. Whether you’re just getting started in open source or you’re deep into it already, I hope you leave this conference feeling inspired to build, collaborate, and leave things a little bit better than you found them.

Thank you all so much!

## Raw YouTube Transcript

Thank you. Wow. Thank you all so much. So yes, my name is John Naizer,
a software engineer at Microsoft, and I'm super excited to share with you
my team and I's story of how Grafana impacted us and how we
in turn impacted Grafana. So let's start from ground
zero, rewind the clock, all the way back to the
beginning of our journey. Our organization at Microsoft had a clear
need for a modern data visualization solution. One that's fresh, flexible, one that keeps up with today's
fast pace in the industry. This solution would then lay the
foundation for what we call our executive dashboards, a one-stop shop where leadership
and teams can go and track metrics, spot trends, make faster, smarter decisions together without
getting stuck in the weeds. These executive dashboards have
three key attributes to them, tracking metrics, managing incidents, and providing real time updates
to our key performance indicators, otherwise known as KPIs
for our organization. Now, I won't give you the
full Grafana sales pitch, but I would love to share with you a
few reasons why Grafana is the obvious choice for us. Why Grafana? First off, it's open source. This gives us the total complete
freedom to build our own solution that's scalable, customizable, and
designed exactly for our needs. We also love that Grafana has an endless
stream of plugins and integrations, maximizing the flexibility
of our use cases. Next, Grafana's portability. The fact that it could be Dockerized
and deployed anywhere, containerized, et cetera, is huge for us when we want to
build and deploy a lightweight but effective solution. This
also allows us to move fast, tweak as we grow and not get
boxed into a single setup. Lastly, Grafana's deep integration with
Azure Native data sources like Azure Monitor, Azure Data Explorer allow us to plug
directly into our telemetry streams, building real rich dashboards, displaying real time data.
All in all, Grafana pretty much checked every
box we had. It's super cool, flexibility, scalability, while keeping things open and modular
and honestly super developer friendly. However, we had one fork in the road and it has to do with security
to give you all some context. First, I have a simple rhetorical
question to ask you all. Who here has forgotten a password before? You all should be raising your
hands. I got a better one for you. Who here as a family member
that forgot a password, reset your shared account
and didn't tell you? Look, it's common knowledge that passwords
by themselves are becoming obsolete for many reasons and not just that silly
one that I previously mentioned. We're seeing more and more things like
two-factor authentication, passkeys, and so on. Companies like Microsoft, they even have their own initiative
driving the security evolution and not just for authentication, but
holistically covering all aspects, all facets of security. As our CEO of Microsoft,
Satya Nadella puts it, if you're faced with a trade-off
between security and another priority, your answer is clear. Do security. Having this mindset while
customizing Grafana authentication specifically for when you log
into Grafana as a service. We were actually pleasantly surprised
to find that Grafana offered two choices for us. One, an authentication proxy, a DIY solution, putting the power in our hands
to customize how we authenticate, how we log into Grafana.
And second, even cooler, an Azure-native authentication
method built directly into Grafana. However, we quickly realized that this method
didn't support an authentication method that we highly
desired for our team. The authentication proxy, it was a supported feature quicker to
set up the drawback though it would've required extra infrastructure and even
some potential long-term maintenance down the road. If we wanted to implement our own Azure
authentication method into Grafana, it would've deepened direct
integration with Azure identity, meaning that we would not have any
other infrastructure to set up. The major drawback to this was
time we needed extra engineering effort. Not only that, but we needed extra time to ramp up
on Graf's code base and also these newer Azure features we were going
to implement into the code base. This was the fork in the road
and we could have taken the easy route, throw an authentication
proxy in front and call it a day. But where is the fun in that? We are software engineers, so we dove directly into Grafana's
code base and built out the solution we wished already existed. One that would not only move us closer
to a future proof platform for security, but hopefully make life easier for others, both inside and outside Microsoft. What was that highly desired
authentication method that we had in mind? Well, we're going to use
Grot to help us understand this. Think of Grot as a bouncer at a super
delicious restaurant that you're in line for now. Only people who know the secret shared
password that Grot originally passed out can enter into this restaurant.
So it's your turn in line. You walk up, you bend over to grot,
you whisper the secret password, GrafanaCON 2025, and you enter the wristband he
gave you is your access token. Now, what if instead of
a secret shared password, he passed out public private key pairs, a certificate based authentication. Now, I personally don't know any
bouncers who would do this, but let's just say he does. What do both of these
methods have in common? It is what you have that
determines who gets in. Again, it is what you have that
determines who gets in. Well, what if I told you there was a third
way? Not based on what you have, but who you are, and some of
you may already know this, but it can be analogous
to say a fingerprint applying this technically. Think
of Grot as an identity provider. Say Azure ActiveDirectory.
You being the application. Well, internally at Microsoft, we call this managed
identity and just like a fingerprint, you never need to
worry about your identity expiring. This completely eliminates the need
for credential management all together. No more remembering secrets. No
more having to rotate certificates. This is incredible. Now, what did this new feature look like? Well, this beautiful screenshot we'll show you. It added a new field under Azure
authentication configuration, and we called it client authentication. This now gives users the ability to
choose more than just one authentication method when logging into Grafana. This is the idea of accessible security, putting the power in the user's hands
to decide how they want to authenticate without jumping through unnecessary
hoops like setting up an authentication proxy and it doesn't just stop there. The authentication model that we
built out in Grafana can be adopted by every other native identity
provider inside the service, and this is the kicker. It's
based on the OAuth two spec, so any identity provider can create
their own implementation now and add that as a client authentication option
underneath their own configuration, huh? Pretty cool. I got to say, going through this open
source contribution process, it was a roller coaster. It was my first time contributing
at this magnitude, at this scale, and it taught me a lot of lessons. It
taught me about collaboration, patience, how many pull request comments it
takes to build something that lasts and actually gets merged
into the main branch. Not only are you building a new feature, you're building new relationships with
the maintainers, Grafana's community, everyone just about as
passionate on Grafana as you are. At the end of the day, you're not just
pushing code, you're earning trust. One pull request at a time. Trails need blazers. Paths
need finders. Problems, need solvers. If any of you are just as interested
as I was to contribute to open source specifically Grafana, be bold. Start small, dive into
Grafana's code base. Find contributors working on the same
pain points that you're interested in. Reach out, partner up with them, and champion the solution together. That's exactly what we
did. My advice, email, email, email. Be persistent. Be bold. If any of you are curious about the
work we did to make this magic happen, go ahead and scan this QR code, it'll take you to the GitHub pull
request that got merged into the main branch and added this new feature. Again, go light your own torch and
don't be afraid to pass it on. Thank you guys so much. I can only hope that our story
resonates with each of you, and I'm so thankful for the opportunity
to share this story with you all. Whether you're just getting started in
open source or you're deep in it already. I hope you leave this conference
feeling a bit more inspired to build, collaborate, and leave things a
little bit better than you found them. Thank you all so much.

