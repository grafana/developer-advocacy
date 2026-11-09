# How Deutsche Telekom Used Grafana Assistant for Zero Downtime at the World Cup

Published on 2026-11-03T18:51:40Z

## Description

How did Deutsche Telekom IT GmbH achieve zero downtime at World Cup scale? In this Grafana case study talk, Felix Mohnke ...

URL: https://www.youtube.com/watch?v=VYjxVWg2Khk

## Summary

The show is titled "How Deutsche Telekom Used Grafana Assistant for Zero Downtime at the World Cup," published on November 3, 2026. The speakers are Felix Mohnke, Head of Observability at Deutsche Telekom, and Neha Kumar, Consultancy Team Lead in Felix's department. They discussed how Deutsche Telekom leveraged Grafana Assistant to achieve zero downtime during the World Cup by enhancing their observability stack, which allowed them to monitor and respond to issues in real time. Key takeaways include the significant reduction in mean time to detect and repair incidents, the importance of self-service in observability tools, and the successful integration of Grafana into their operations. 

Topics: Grafana Assistant, observability, zero downtime, incident management, user experience.

## Chapters

00:00:00 Deutsche Telekom's observability strategy for the World Cup
00:07:05 Using Grafana Assistant for incident management during the World Cup
00:14:23 Grafana's role in achieving zero downtime at the World Cup

Hey. Hello and welcome everybody. My name is Felix Mohnke, and I'm really, really happy to be here today. We even have our fans as well, and we also have some other colleagues. 

So Neha, hi!

I'm Neha, and we are very excited to be here today. I mean, this is my very first time in the US, so I'm especially excited to be here today with you. But before we get into observability, I would say, Felix, let's have a quick glimpse of us outside work.

Yeah. Well, I like kite surfing whenever I get the chance. My home spot is actually located in the Netherlands, where there's always good wind. But I kited all over the world, from Zanzibar to Cape Verde to Egypt to the Dominican Republic. And I saw that we also got some good wind today. So once I'm done with my presentation over here, I will put on my bathing shorts and hop on the bay for a short boarding trip, hopefully.

So what do you do outside of work?

I love swimming, actually, but I need to tell you this: I only learned to swim this May. Yes. And I mean, I'm 30 years old. At first, one kilometer felt like a huge distance, but now I can't even imagine swimming less than that. Swimming is a skill, so is observability. I think we both enjoy being in the water, just at a very different speed, but we also love to be in the observability world. Actually, I enjoy being on the water more if the clicker works. Let's try the other one. No problem. There's always a backup, right? Ah, there you go. It's working for the first place.

So if I'm not drifting in the ocean, I'm the head of observability at Deutsche Telekom. Together with my team, where we also have some colleagues with us later, I'm heading the platform strategy of Deutsche Telekom. After our first success, which we'll talk about today, we are now scaling the platform to Germany and outside of Germany.

And I'm Neha Kumar, consultancy team lead in Felix's department and in Deutsche Telekom IT. My focus is basically driving the adoption and scaling of our observability stack in Deutsche Telekom IT, our organization.

Who of you has ever seen this T before? Okay, many? At least some T-Mobile fans. That's good. So T-Mobile US is right here, which is part of the Deutsche Telekom group. Felix and I, with Deutsche Telekom IT, are also part of the same group.

Exactly. So it will be an interactive session, short warning. Who watched the soccer World Championship final game? Show of hands. Amazing, at least some. Who was betting on Spain? Okay, one lucky guy. And who of you who watched the game was thinking about business? Me too. Who was thinking about meantime to detect? Okay. So that's basically normal. At least our system architect as well.

Yeah. So it's normal that you and many fans were focused on the match, but we were really focused on the digital services behind the user experience. And talking about user experience, I will lead you two years back to the big failure of the European Championship in 2024. I got that screenshot of our website, and this was the user experience two years before. There were 18. One guy is already smiling, so he probably liked to book the match back in the game. 

The European Championship made visible that we didn't have any visibility. The customers went to our website, wanted to book their game passes for the match to watch, and they couldn't book, or they could book, but only if the other 18,000 customers in front of them were ready with booking. Imagine that user experience, and you cannot repeat that at the biggest sports event this year. To go one more level deeper, back in the days, we didn't even know what was going wrong. Now I can safely say that because it's two years ago. We didn't have any clue what was going wrong. 

Well, this motivated us, or our management motivated us, not to repeat the same mistake again. That experience actually stayed with us because we knew we had to be better prepared this time. 

So Magenta TV is Deutsche Telekom's TV and streaming platform. A rough US comparison would be Fox Sports and Fox One as a home for World Cup coverage. We were bringing 104 matches together on one platform with Magenta TV. For us, this meant millions of people watching in real time, massive volumes of data, reliability under pressure, and zero room for downtime. 

So obviously, this was a high technology stress test for us in the organization and for everyone involved. I'm sure you might have also faced similar challenges in your own organization because, at the end of the day, we are dealing with the same challenge from time to time, which is keeping critical services reliable under extreme demand.

Oh, they changed the slide a little bit. It doesn't matter. Don't tell Grafana, but in the beginning of our journey, we were using the AI assistant to create dashboards. I know they can do much more; they can do alarming and all that cool stuff, but we had to present to our management dashboards. They wanted to see the booking journey. The mistake that was made beforehand, we didn't have to repeat. We were using the AI assistant to create those wonderful dashboards, which you can see over here. 

We had a big screen or a big wall of screens, actually, in Bonn, our beautiful hometown, where you could see how the booking journey looked. You can see some details over here. More importantly, monitoring observability is important for the company, but what is more important for the company? LinkedIn posts, right? All the managers came, went in front of the wall, took their pictures, and said, "Oh wow, we are so good. We are well prepared." 

But apart from that marketing factor, to be a little bit more serious, it also helped us sitting in that situation room, watching the dashboards, and then seeing if something went wrong. I can tell you some things went wrong.

Neha, let us give you one example from our situation room, what Felix was just highlighting. There was one day when our dashboards showed an increase in the error rate in the payment area. With the Grafana assistant, we checked what was really driving that increase of outages, and instantly our engineers could narrow down the investigation to the affected API. From there, we investigated further and could identify the root cause, which was basically that a credit card provider service actually went down. 

So we isolated the issue, we could continue our service, and thankfully our customers never noticed it. It was really, really great to be prepared in that way with the situation room because when the moment really came, we were prepared to act.

Oh, and we didn't really stop at the World Cup. I mean, you heard now roughly the story. Our vision was born roughly one, one and a half years ago when I was sitting in front of ChatGPT and said, "What could be the visibility or the observability of the future?" I just created some HTML pages, and from there it somehow went to the World Cup. But then we continued. 

It is really crazy. We signed the contract with Grafana three months before the World Cup started. Three months! We had roughly 60 applications to be connected to the stack. If you come from a big organization, you can imagine how difficult that is to discuss with each almost individually how to onboard them. 

Then let me spice up that story a little bit more. Three days before the World Cup, our backup failed. Yes. You can imagine how that feels. All the management looking at you saying, "We have zero visibility, do something." And to tell you the truth, the backup was also a Grafana solution, a Grafana open-source solution. So there was only one way: it was a fix-forward way. We took the bring your own cloud solution, shifted all the endpoints of all the applications in one or two days, and then it somehow worked. 

So we had all the beautiful dashboards and 200 million of our customers... Or no, we do not have 200 million customers. So...

200 million customers over the course of those games watched everything. And as Neha just explained, it went flawlessly. Yes, I'm repeating that time and again. We use the assistant mainly for dashboard creation. I'm running a team with 60 people, and a large part of it was creating dashboards, which took months. But we just used the assistant and narrowed it down from those four months to one day.

So, Neha, follow me if the clicker works. I probably have to click harder. Yeah. Basically, let's have a look behind the curtain at the business needs that really led us to start this journey, like Felix said, one and a half years ago. At that time, our meantime to detect was, on average, more than two hours until we realized that we had an incident in our IT landscape. It took us even more than six hours, on average, to resolve an incident, which is really a pity because we are an IT company. In many cases, the first signal came from outside our own organization, mainly from our customers. This meant that we didn't have the visibility or transparency we needed to spot a technical issue and understand its impact on the business.

A big part of the challenge was the scale and complexity of our IT landscape because Deutsche Telekom IT has a highly heterogeneous application landscape spanning a wide range of applications, systems, and deployment models. Name an observability tool, and the chances are really high that we have it somewhere in our organization. Even in our own department, we were operating eight different deployment models and observability stacks. With data spread across different tools, we struggled to connect the technical issue to its impact on the customer business. Even during 60 load tests, our IT and network teams kept discovering further applications that might be involved in a single customer journey, and the full picture was hence spread across different teams and applications. This affected how quickly we could respond.

We were configuring alerts, but we were really missing the end-to-end visibility we needed to act on time and prevent customer impact. That was when we realized we needed a central observability solution to connect the signals and the dots across our environment, detect issues much sooner, and understand the impact on the customer journey. Think about a soccer match; it lasts for 90 minutes, right? If it takes us more than two hours to detect an incident, by that time, the match is already over, and the customer is gone. The disruption for the customer is already there, and for us, the trust of the customer is then at stake.

Let me guide you from that challenge we faced during the World Cup to a broader vision that does not only apply to one single event, which was obviously a bigger event. The vision is simple: end-to-end visibility across our complex environment built on three main principles. 

1. **Integrated**: All data in one place, so teams can explore them together.
2. **Scalable**: Across both technology and teams. This is not really new; everybody's doing it these days.
3. **Self-service**: Teams can access the data together without needing to wait for a central team to react. You all know demands keep growing, but a central team cannot scale by doing everything manually.

As Felix mentioned before, we are a department or a team of around 60 people, and we can never have enough people to serve all our customers and their needs. We were configuring alarms for applications and handcrafting more than 150 dashboards. We knew we needed a different approach, and the only reasonable answer to that was self-service. However, self-service only works if people really want to use the tool. We needed a tool that people were familiar with and had a learning curve as easy as possible. From our previous implementation, we learned that people really need to like the tool; otherwise, adoption becomes a struggle. That's why we chose Grafana as the platform to bring this vision to life.

After the World Cup, I won't give you all the details about our meantime to detect and meantime to repair, but we see that applications connected to our Grafana platform have a 70% reduced meantime to detect. This number is not made up; it is real. The meantime to repair, which is still high in our company, went down by more than 50%. The numbers prove that our vision and implementation are correct. 

You also see 220 applications connected. I should bring up the Grafana dashboard; it's growing by the day. Just yesterday, we connected 10 additional applications, and the day before that, another 10. I checked this morning, and we are above 240 applications already. We are really getting addicted to our Grafana dashboard because we always see an increase in the applications onboarding our observability stack. Each morning in the chat, it's like, "How many applications?" That is really cool to see.

Additionally, we have a leaderboard so departments can see how many applications they have connected. Am I better? Am I good? Did I increase? It's almost like a soccer leaderboard these days. I think we have more than 1,500 Grafana users now. For the rest of the numbers, you can ask my system architect, who can help you out with all the details.

We talked a little bit about the vision, and Neha actually didn't want me to bring up this slide and this beautiful picture, but for me, it represents what we are driving for. We have this little flashlight that says "observability," and it points to the stars where we think we will go. We are an AI-first company, as our CIO says, and our department takes care to implement AI first in the operations area. We are doing observability to enable teams and DevOps engineers to go down that path.

Just watching the time, we are much slower than we expected because usually, we talk quite fast. I will stop here. If you have further questions regarding vision and stuff like that, reach out to us. I can talk at length about that. There’s another cool story from last week that Dennis, our Grafana counterpart, is also aware of. We had a network issue that began shortly after we made a change, affecting some applications and services within DTIT. One team member asked the Grafana assistant a very simple question: "What happened?" with a screenshot in Slovak. Our observability stack is connected to our internal change management system, so the assistant was able to bring that change into focus, along with the timing link between that change and the network issue. This provided a clear starting point for the team.

We need to mention that this person had nothing to do with that change and is not part of the team, but we follow a rule of transparency in our company. He just wanted to know what was going on. This was when we thought, "Okay, our effort is finally paying off." Driving adoption is never easy, especially in a super big company, because it takes a real shift in mindset.

**Grafana Community Call: How Deutsche Telekom Used Grafana Assistant for Zero Downtime at the World Cup**

Grafana, people already knew and were familiar with; it really helped us to build momentum. If everyone is pulling in the same direction, you cannot only see the difference, but you also feel the difference. Sometimes it's more about pushing, but anyway.

Oh, that's my slide. At the beginning, I was asking you, what were your thoughts at the final game? I think Neha, what was on our minds? We were ready. 

So, three months from challenge to delivery, we turned a fast response into lasting capability, and we know how to deliver when it matters the most. With that, I already gave you an indication: please stay in touch with us. We also want to hear your stories. We want to know what works in adoption and what does not, especially the "what does not" part.

We have with us here also Artur; I know that you're trying to hide. Artur is our system architect who had all the good ideas. Basti is also somewhere here. Ah, he's over there taking pictures. That's our product owner. 

Thank you, Artur and Basti, for being part of this lovely journey. Also, thank you to the Observability Con team for giving us the opportunity to present our story here. You all have been a wonderful audience. Thank you so much.

## Raw YouTube Transcript

Hey. Hello and welcome everybody.
My name is Felix Mohnke, and I'm really, really happy to be
here today. We even have a full ah, we have our fans as well, and we also
have some other colleagues. So Neha. Hi, I'm Neha and we are very
excited to be here today. I mean, this is my very first time in the US, so I'm especially excited
to be here today with you. But before we get into
observability, I would say, Felix, let's have a quick glimpse
of us outside work. Yeah. Well, I like kite surfing whenever I get the chance. And my home spot is actually located
in the Netherlands where there's always good, good, good wind. But
I kited all over the world. So I went from Zanzibar
to Cape Verde to Egypt to Dominican Republic. And I saw that we also
got some good wind today. So once I'm done with my
presentation over here, I will put on my bathing shorts and
hop on the bay for a short boarding trip, hopefully. So what
do you do outside of work? I love swimming actually,
but I need to tell you this. I only learned to swim
this May. Yes. And I mean, I'm 30 years old. At first, one
kilometer felt like a huge distance, but now I can't even imagine to
swim less than that. And I mean, swimming is a skill, so is observability. And I think we both enjoy being in the
water just at a very different speed, but we also love to be in
the observability world. Actually, I enjoy more being on
the water if the clicker works. Let's try the other one. No problem.
There's always a backup, right? Ah, there you go. It's working
for the first place. So if I'm not drifting in the ocean, I'm the head of observability
at Deutsche Telekom. And together with my team where we also
have some colleagues with us later, I'm heading the platform
strategy of Deutsche Telekom. And after our first success, which
we'll talk today a little bit about, we are now scaling the platform
to Germany and outside of Germany. And I'm Neha Kumar, consultancy team lead in Felix
department and in Deutsche Telekom IT. My focus is basically driving the
adoption and scaling of our observability stack in Deutsche Telekom
IT, our organization. Who of you has ever seen this T before? Okay, many? At least some tea fans. That's good. So T-Mobile US is right here, which
is part of the Deutsche Telekom group. And Felix and I with Deutsche Telekom
IT, we are also part of the same group. Exactly. So it will be an
interactive session, short warning. So who watched the soccer
world championship final game? Show of hands. Amazing, at least
some. Who was betting on Spain? Okay, one lucky guy. And who of you who watched the
game were thinking about business? Me too. Who was thinking
about meantime to detect? Okay. So that's basically normal. At least our system architect as well. Yeah. So that's basically normal that you and
many fans were focused on the match, but we were really focused on the digital
services behind the user experience. And talking about user experience, I will lead you two years back to
the big failure of the European championship in 2024. I got that screenshot of our website and this was the user experience
two years before. They were 18. One guy is already smiling, so he probably liked to book
the match back in the game. So the European championship made visible that we didn't have any visibility. The customers went to our website, wanted to book their game passes
for the match to watch and they couldn't book or they could book, but only if the other 18,000 customers
in front of them were ready with booking. Imagine that user experience and
you cannot repeat that at the biggest sports event this year. And to go one more level deeper, back in the days, we didn't
even know what was going wrong. So now I can safely say that because it's
two years ago. We didn't have any clue what was going wrong. And well, this motivated us or our management
motivated us not to repeat the same mistake again. And that experience actually stayed with
us because we knew we have to be better prepared this time. So Magenta TV is Deutsche Telekom's
TV and streaming platform. A rough US comparison would be Fox
Sports and Fox one as a home for World Cup coverage. And we were bringing with
Magenta TV 104 matches together on one platform. And for us, this meant millions of
people watching in real time, massive volumes of data, reliability under pressure
and zero room for downtime. So obviously this was a high
technology stress test for us in the organization and for everyone involved. And I'm sure you might have also
faced similar challenges in your own organization because
at the end of the day, we are dealing with the same
challenge from time to time, which is keeping critical services
reliable under extreme demand. So everybody... Oh, they changed the
slide a little bit. It doesn't matter. Don't tell Grafana, but in
the beginning of our journey, we were using the AI assistant
to create dashboards. I know they can do much more. It can
do alarming, all that cool stuff, but we had to present to
our management dashboards. They wanted to see the booking journey.
The fuck up that was beforehand, we didn't have to repeat. We were using the AI assistant to
create those wonderful dashboards, which you can see over here. We had a big screen or a big
wall of screens actually in Bonn, our beautiful hometown where you could see how
the booking journey looks. You can see some details over
here. And more important, so monitoring observability
is important for the company, but what is more important for the
company? LinkedIn posts, right? All the managers came, went in front of the wall and took
their pictures and said, "Oh wow, we are so good.
We are well prepared." But apart from that marketing factor to be a
little bit more serious, it also helped us sitting
in that situation room, watching at the dashboards and then
seeing if something went wrong. I can tell you some
things went wrong. Neha. And let us give you one example
from our situation room, what Felix was just highlighting because
there was one day when our dashboards showed an increase of the
error rate in the payment area. And with the Grafana assistant, we checked what was really driving that
increase of outages and instantly our engineers could narrow down the
investigation to the affected API. And from there we investigated further
and could identify the root cause, which was basically that a credit card
provider service actually went down. So we isolated the issue, we
could continue our service, and thankfully our customers never
noticed it. So it was really, really great to be prepared in that
way with the situation room and because when the moment really came,
we were prepared to act. Oh, and we didn't really stop
at the World Cup. I mean, you heard now roughly the story. Our vision was born roughly one, one and a half years ago when I was
sitting in front of ChatGPT and said, "What could be the visibility or the
observability of the future?" I just created some HTML pages and from there it somehow went to the World
Cup, but then we continue. It is really crazy. We signed the contract with Grafana three
months before the World Cup started, three months. We had roughly 60 applications
to be connected to the stack. If you come from a big organization, you can imagine how difficult that is
to discuss with each almost individually how to onboard them. Then let me spice up that story a little bit more. Three days before
the World Cup, our backup failed. Yes. You can imagine how that feels. All
the management looking at you saying, "We have zero visibility, do something." And to tell you the truth, the backup was also a Grafana solution, a Grafana open source solution.
So there was only one way. It was a fix-forward way. So we took
the bring your own cloud solution, shifted all the endpoints of all
the applications in one or two days, and then it somehow worked. So we had all the beautiful dashboards
and 200 million of our customers... Or no, we do not have
200 million customers. So 200 million customers over
the course of those games watched everything. And as Neha just
explained, it went flawlessly. And yes, I'm repeating
that time and again. We use the assistant mainly
for dashboard creation. I'm running a team with 60 people
and a large part of it was creating dashboards and it was creating those
dashboards over months. But we just used the assistant and we
narrowed it down from those four months to one day. So Neha, follow me if the clicker works.
I probably have to click harder. Yeah. So basically let's have a look behind
the curtain at the business needs that really led us to start this journey
like Felix said one and a half year ago. At that time, our meantime to detect was on
average more than two hours until we realized that we have
an incident in our IT landscape, and it took us even more than six hours
on average to resolve an incident, which is really a pity because we
are an IT company. And in many cases, the first signal really came
outside of our own organization, which was mainly even our customer, which actually then again meant
that we didn't have the visibility, we didn't have the transparency. We needed to spot a technical
issue and to understand its impact on the business. A big part of the challenge was
the scale and complexity of our IT landscape because Deutsche Telekom
IT has a highly heterogeneous application landscape spanning
a wide range of applications, of systems and deployment models.
I mean, name an observability tool and the
chances are really high that we have it somewhere in our organization.
Even in our own department, we were operating eight
different deployment models
and observability stacks and with data spread across different tools, we really struggled to connect the
technical issue to its impact on the customer business. Even
during 60 load tests, our IT and network teams, they kept discovering further applications
that might be even involved in a single customer journey and the
full picture was hence spread across the different teams and
the different applications. And that also affected how quickly
we could respond and we were also configuring alerts, but we were really missing the
end-to-end visibility we needed to really act on time and to
prevent customer impact. And that was when we realized, okay, we need a central observability
solution to really connect the signals, to connect the dots
across our environment, detect issues much sooner and understand
the impact to the customer journey. I mean, think about a soccer match.
It lasts for 90 minutes, right? And if it takes us more than two
hours to detect an issue, an incident, by that time, the match is already over. Customer's gone. Yeah. So the disruption for the
customer is already there. And for us, the trust of the customer
is then at stake. Let me also guide you from that challenge. We were facing during the World Cup to a
broader vision that does not only apply to one single event, which
was obviously a bigger event, but the vision is simple. End-to-end visibility across
our complex environment built on three main principles. The first one, integrated in the sense
of all data in one place, so teams can explore them
together. Second one, scalable across both technology and teams. That is not really new, right? True. Everybody's doing it these days. So third one, self-service. So teams can access the data together
and they don't need to wait for a central team to react because you all
know demands keep actually growing, but a central team cannot scale
by doing everything manually. And like Felix even said before, we are a department or a team of
around 60 people and we can never be enough people to serve all
our customer and their needs. So we were configuring
alarms for applications. We were really handcrafting
more than 150 dashboards. So we knew we really need a
different approach and the only and only reasonable answer
to that was self-service. But again, self-service then actually only works
if people really want to use the tool. So we needed a tool people actually
were familiar with and with a learning curve as easy as possible. And
also from our previous implementation, we learned that people
really need to like the tool, otherwise the adoption really becomes
a struggle. And that's why we chose Grafana as the tool, as the platform
to really bring this vision to life. So I was talking about what
happened after the World Cup, and I'm not giving you all the
details about our meantime to detect, Meantime to repair, but we see that these
days applications which are connected to our Grafana
platform have a 70% reduced meantime to detect, 70%. And this number is not
made up, but it is real. The meantime to repair, which is still high in our company
went down by more than 50%. So the numbers prove that our vision
and our implementation is correct. You also see 220 applications connected. I should bring up the Grafana dashboard. It's growing by the day. So I think
just yesterday we connected... We did not connect, but the partners,
the applications connected themselves, 10 additional applications and the
day beforehand 10 additional again. So we are already... I just
had a look in the morning. We are above 240 applications already now. And we are really getting addicted to
our Grafana dashboard because we always see an increase of the applications
onboarding our observability stack. Each morning in the chat is
like, "How many applications?" That is really cool to see.
And we also, what we did, which is maybe a lesson
to be shared with you, we have a leaderboard. So the departments can see how
many applications have I connected? Am I better? Am I good? Did I increase? So it's almost like a soccer
leaderboard these days. I think we have more than
1,500 Grafana users these days, and about the rest of the numbers you
can ask my system architect who can help you out with all the details.
We talked a little bit, or not a little bit only about the vision, and Neha actually didn't want me to
bring up this slide and this beautiful picture, but for me, it represents
what we are driving for. So we have this little flashlight.
I have the flipper here, it doesn't matter. So we have that little
flashlight which says observability and it points to the stars
where we think that we will go to. We are an AI first company, that's what our CIO says. And our department takes care to
implement AI first in the operations area. So we are doing observability to enable teams, DevOps
engineers to go down that path. And just watching at the time, we are much slower than we expected
because usually we talk quite fast. I will stop over here. If you have further questions in
regards to vision and stuff like that, reach out to us. Also afterwards,
I can talk lengthy about that. Because there's another cool
story. There was a very, very recent example of
last week, and Dennis, our Grafana counterpart,
is also aware of that. We had a network issue which began
shortly after we did a change and it affected some of the
applications and services within DTIT. And one team member, he was just asking the Grafana assistant
a very simple question, which was, "What happened?". With a screenshot in Slovak. Yeah, exactly. And also
in another language. And our observability stack is luckily
connected to our internal change and management system. So the assistant was
able to bring that change into focus, but also the timing link between
that change and the network issue. And that really gave the people
a really clear starting point. But also we need to mention this, this
guy has nothing to do with that change, and also he's not part of the team, but we are following in our company a rule of transparency and he
just wanted to know, okay, what's going around in our company? So
this was when we were thinking, okay, our effort is finally paying off and
driving and adoption is never easy, especially in a super big company
because it takes a real shift in mindset. But choosing Grafana, people
already knew and were familiar with, it really helped us to build momentum.
And if everyone is pulling in the same direction, I think you cannot
only see the difference, but you also feel the difference. And sometimes it's more
about pushing, but anyway. Oh, that's my slide. So at the
beginning I was asking you, so what were your thoughts at
the final game? And I think Neha, what was on our minds? We were ready. So three months
from challenge to delivery, we turned a fast response into lasting
capability and we know how to deliver when it matters the most. And with that one, I already
gave you an indication, please stay in touch with us. We
also want to hear your stories. We want to know what works in
adoption and what does not, especially the what does not part.
So we have with us here also Artur, I know that you're trying to hide.
So Artur is our system architect who had all the good ideas. Basti.. He's also somewhere here. Ah, he's over there taking pictures.
So that's our product owner. Yeah. And also thank you Artur and
Basti for being part of this lovely, lovely journey. And also thank you to the Observability
Con team for giving us the opportunity to present our story here. And yeah, you all have been a wonderful
audience. Thank you so much.

