# Monitoring Airport Kiosks at Amsterdam Schiphol Airport to Improve Passenger Satisfaction | Grafana

Published on 2025-06-07T05:39:29Z

## Description

Learn how Gerard van Engelen and his team built a scalable observability stack to monitor kiosks at Schiphol Airport (and other ...

URL: https://www.youtube.com/watch?v=tmrF2y4vrAI

## Summary

In this presentation, Gerard van Engelen, a DevOps engineer at Schiphol Airport, discusses the use of Grafana for their passenger experience platform, Travor. He highlights the stress associated with traveling and the importance of real-time information for travelers to enhance their experience. Gerard explains the functionality of Travor, which includes features like tracking flight status and providing assistance, and emphasizes the need for effective monitoring to ensure the system operates smoothly across various global airports. He details the technical setup involving Kubernetes, Grafana, and observability tools like Alloy, Loki, and Tempo, while also discussing data handling regulations and the necessity for efficient data management solutions. Finally, Gerard shares insights into the deployment process and offers a demo on setting up Grafana similar to Schiphol's configuration, concluding with an invitation to connect on LinkedIn and attend an upcoming event.

# Using Grafana for Travor at Schiphol Airport

Welcome, my name is **Gerard van Engelen**. I am a DevOps engineer at Schiphol, which is one of the busiest airports in Europe. I work on the Schiphol.nl website and a product called **Travor**. Today, I will discuss how we use Grafana for Travor.

If you have questions during the presentation, feel free to scan the QR code provided, and we will try to answer them afterward.

## The Stress of Traveling

People who know me are aware that I don't get stressed easily. However, traveling can be stressful for many. When heading to the airport, I often think, "Will I miss my flight?" I check my pockets multiple times to ensure I have my passport. 

Research by Forbes shows that losing luggage is a major concern for travelers. At Schiphol, we found that people are most afraid of someone else taking their luggage. When passengers disembark, they often rush to the baggage reclaim area to prevent theft. Interestingly, 40% of travelers are more worried about losing their friends than their luggage. In fact, more people fear losing friends or luggage than losing a child—though that certainly makes for a dramatic movie!

Clearly, traveling is a stressful situation, but at Schiphol Airport, we have your back with Travor. 

## Introducing Travor

Travor is a passenger experience platform that provides real-time information to travelers about their journey. By scanning your boarding pass, you can know when your plane is landing or departing. If you have spare time, you can search for stores that meet your expectations. If you need assistance, you can click a button, and someone will come to help you. You can also have real-time calls with staff if needed.

We created Travor to alleviate some of the stress for our travelers. A 1% increase in customer satisfaction (CSAT) can lead to a 1.5% increase in non-aeronautical revenues. Given that Schiphol generates €256 million in revenue annually, a 1% increase is significant. 

However, it must work. Forbes also found that if a technical solution fails, it can negatively impact CSAT by 15 to 25%. This issue is compounded with kiosks; even if you're not using one, just seeing a malfunctioning kiosk can affect your mood. Therefore, it's crucial for us to ensure that Travor operates smoothly.

Travor is deployed not only at Schiphol but also at other airports worldwide, including Athens, Frankfurt, and Iceland. We have plans for deployment in Copenhagen and are working on airports in the US and Africa. Traveling to these locations to check if the application is functioning is not feasible, which is where **Grafana** comes in.

## Utilizing Grafana

With Travor deployed globally, we need to store data from our observability platform regionally due to local legislations. For instance, boarding pass data from US airports cannot be stored in Europe and vice versa. Additionally, if an airport ends its cooperation with us, we want an easy way to delete data without complicated queries.

We aim for a data set per customer while also maintaining a single pane of glass for our developers. We don’t want them to log into different systems for each airport and risk getting lost. Grafana allows us to gather logs, metrics, traces, and more to build dashboards that support our customers effectively.

### Setting Up Observability

Let me overview how we set up our observability platform from a customer perspective. We start with a **Kubernetes** cluster running all applications needed for our passenger experience platform. Alongside our basic applications, we deploy a monitoring stack that includes **Alloy, Loki, Prometheus,** and **Tempo**.

Initially, we planned to deploy the Grafana agent on our kiosks but ultimately opted for **Faro** instead. Everything is deployed using **GitOps** with **Argo CD** at scale for each airport we support.

In Amsterdam, we run the Grafana server and Alert Manager, connecting them to OpsGenie and Slack. This setup allows for a single entry point for our monitoring solution while providing a localized version. It gives us real-time insights into kiosk performance globally.

### Implementation Requirements

To replicate our setup, you’ll need a shopping list of components:
- Helm charts for:
  - Kubernetes monitoring
  - Loki
  - Tempo
  - Kube-Prometheus stack
- Faro SDK
- Azure-managed Grafana for SSO setup
- ArgoCD
- Some Terraform for configuration

If you're unsure how to set this up, I will demonstrate how to configure Grafana as we do at Schiphol, allowing you to run it on your laptop or cluster, regardless of size.

## Demo

Let’s switch to the demo. 

We will start with the **K8s monitoring Helm chart** to create a simple Argo CD application for deployment on Kubernetes. We will insert some values to set it up. 

Next, we configure data sources for **Prometheus**, **Loki**, and **Tempo**. After deploying, ArgoCD automates the rollout of everything needed to collect OpenTelemetry data, including logs and traces.

Next, we deploy the **Kube-Prometheus stack**. I won’t bore you with the details, but it’s similar to the previous step. Once configured, we deploy Grafana and set up necessary data sources.

Then we deploy **Loki** and **Tempo**. For production, I recommend using a managed blob store like S3 or Azure Blob Store instead of local storage.

To monitor the frontend aspect of Travor, we use Faro, necessitating a separate receiver configuration to send logs and traces to our backend.

### Frontend Observability

On the frontend, we configure Faro to send logs and metrics back to our Next.js application, allowing us to monitor if the kiosks are functioning correctly. If we don’t receive information from the frontend, we know there’s a problem that requires attention.

We set alerts to notify us if a kiosk stops sending information, prompting investigation. 

## Conclusion

I hope this overview gives you insight into our observability approach at Schiphol. If you wish to stay in touch, you can find me on LinkedIn. For more details on our setup, check out the product repo on my personal Gitlab account. 

I look forward to seeing you all at the all-attendee party in the Museum of Pop Culture tonight!

## Raw YouTube Transcript

Welcome. My name is Gerard van
Engelen. Where's this line? Oh, I need to stand here. My
name is Gerard van Engelen. I'm a DevOps engineer at Schiphol, which is one of the
busiest airports in Europe. I work on the Schiphol.nl website and
I also work on a product called Travor. And I'm going to talk about how we use
Grafana for this product called Travor. So I'm not going to bother you
with how this QR code works. If you've got questions, scan it and we'll try to answer
them after this presentation. So people that know me, they know that I don't
get stressed easily, but stress is not okay. And even though I don't get
stressed really easily, I do get stressed when
going to the airport, on my way there thinking, "Will I miss my flight?" I'll
check my pockets 10 times if I grabbed my passport. And
I'm not alone in this. Traveling is one of the most stressful
situations for everybody in the world, and Forbes did a research on what people most worry
about when traveling through an airport. So one of the
things is losing luggage. And at Schiphol we did some research
and actually people are most afraid that somebody else will take their
luggage. So if you get off the plane, people will literally run towards
the baggage reclaim section to prevent anybody from
stealing their luggage. One of the other things that I think is
really interesting is that you should not make any friends at the
airport because 40% of your friends will be afraid that you'll lose
them before you go through your flight. And what's even more interesting
is that more people are afraid for losing their friends or their
luggage than their people are afraid for losing their child. But I think losing your child is something
you can make a movie about, right? We all know this one. Okay, so we can all conclude that
traveling is a stressful situation, but we at Schiphol Airport,
we've got your back. We've got a product called Travor
and Travor is a passenger experience platform, which uses a modular approach to provide real-time information for
travelers about their journey. So scan your boarding pass, and
know when your plane is landing, you know when your plane is
departing. If you have time left, you can search for stores that meet your
expectations. If you need assistance, you could click a button,
somebody will come and find you. Or if you just want to
have a call with somebody, click another button and you'll be
connected to somebody in real time. So this product we've created to take
a little bit of that stress away from our travelers, and we do that because a 1% increase in CSAT could add up to 1.5% added non-aeronautical revenues.
So if you imagine that
Schiphol makes 256 million euros in revenue every year,
a 1% increase is significant. But only when it works. Because Forbes did another
research that if a technical solution doesn't work, it could
affect your CSAT by 15 to 25%. And with kiosks it's even worse, because
even if you're not using a kiosk, but you're walking by it and
you see that it's not working, it could also affect your state of mind. So you can imagine that it's very
important for us to know if this product is actually working. With Travor being positioned
at the airport, also Air Site, you can imagine that it's difficult to
just go and see if everything is working, and especially taking
into consideration that we not only have the product
Travor at Schiphol Airport, but we also sell it to other
airports around the world. So currently we have
Travor deployed at Athens, Frankfurt, Iceland, and we just
received confirmation that next, in the coming year, we'll also be deploying it to
Copenhagen and we're working on airports in the US and in Africa as well. So just going out to Africa to see if
your application is working might not be feasible for us. But luckily we have Grafana
coming to the rescue. I wanted to do a super Grot image. I asked ChatGPT to do it, but it
keeps ending up as a alligator. And now I saw that we have
actually, we have a super Grot. So it's a bit of a shame that
I didn't know that upfront. But how do we use Grafana? Oh, no, what do we need from Grafana?
That's the most important question. So with Travor being
deployed all over the world, we need to store the data from our
observability platform regionally because each continent has their own local legislations. For example, boarding pass data from US
airports cannot be stored in Europe, and it's the
same other way around. And if for some reason an airport ends the cooperation with us, we want to be able to delete
the data easily without doing difficult queries in our data sets. So we want to have a
data set per customer, but we also want a single pane of glass.
So we don't want our developers to have to log into system X for Amsterdam and system Y for Athens,
and then remembering, "Oh damn, I'm on the wrong URL. What am I doing? I'm lost." And basically
having the airport experience. But then with Grafana. And
obviously we want logs, metrics, traces, and more because we want to build
awesome dashboards that help us support our customers with the Travor product. So I already told you that we
have the product on multiple airports. We want to be able to support
the product cradle to grave. We want to be able to support
different retention periods. What we don't want is to
have to create different setups for different airports. So create an alert and
then copying it five times over all the airports that we have. And
there are a bunch more requirements, but requirements are boring, so I won't bother you with the
remainder of that. So now that we know what we want, let's see how we
approach this part at Schiphol. So I brought an overview
of how we set this up and let's start how we set up the observability platform
from a customer perspective. So first we start with the
Kubernetes cluster that runs all the applications that are required for
our passenger experience platform. And besides our basic applications, we also deploy
a monitoring stack. So for that, we use Alloy, Loki, Prometheus, Tempo, and this drawing is a bit old. We wanted to deploy the
Grafana agent on our SSUs, so the kiosks, but we ended up going for Faro. So the rest of the presentation now will
not be handling Grafana agent but Faro. And that's everything that
we deploy for our customers. We deployed all of this using
GitOps with our Argo CD, and we do this at scale so
for each airport that we support. And now that we have set up all the stuff that
we need for an airport, we also need to set up everything
that we need for our local entry into our dataset. So in Amsterdam, we have a setup where we run the
Grafana server and Alert Manager, which we also connect
to OpsGenie and Slack. And that allows us to have
one single entry for our monitoring solution and also have a local version. So that one, okay. And after this we have real-time
insights into how our kiosks behave around the world. We have a real cost efficient
monitoring solution in regards to other monitoring platforms, and we have the ability to
create awesome dashboards. So you might be thinking, okay, this is somewhat interesting or cool and I want this for myself, but how do we
do that? So I created a shopping list. So we need a lot of Helm charts, the K8s monitoring Helm chart,
the Loki Helm, the Tempo Helm, the Kube-Prometheus stack Helm.
Then we need the Faro SDK. At Schiphol, we've deployed Grafana as an
Azure-managed Schiphol because that allows us to set up SSO real simple. We need ArgoCD and some
Terraform to dress it up. And now you might be thinking,"Okay, Gerard (Dutch) or Gerard (English), I know how to do grocery shoppings,
but I'm not really good at cooking. I've got your back as well because
I'm going to do a demo about how you can set up the Grafana
in the way that Schiphol does it, but then in a way that you can run it on
a laptop or your own cluster. It doesn't really matter if
you have one node or 250, I've got one set up that rules them all. Can we switch to the demo? Oh, I'll zoom in a bit. Is this readable for everyone? Okay, cool. So I already discussed
that we're using ArgoCD, right? We want to deploy everything as
GitOps because if we by accident, delete our cluster and bring it back up, we want everything to be
rolled out automatically. And ArgoCD allows us to do
that in a modern approach at a high scale. So let's start with the
K8s monitoring Helm chart. We'll create a simple Argo CD application, which we deploy on Kubernetes. We take the k8s monitoring helm chart, and we'll insert some values. And basically, if you want to do this, this is what you need to get
a similar setup to Schiphol. I've left out some request limits and
that sort of stuff because otherwise it would not run on a Kind cluster.
But we enable the cluster metrics, we enable pod logs, we do auto
instrumentation using Beyla, we enable application observability,
and then we're good to go. We need some data sources.
So we configure Prometheus, we configure Loki, and we
configure Tempo. And in the end, we need a couple of Alloy
collectors, the metrics, the logs, and the Alloy receiver. And if you deploy, Brave is gone, come on. Where are you? Oh crap, I'm an idiot. As I always say, the problem was somewhere
between that wall and this screen. Okay, so we apply this to our
Kubernetes cluster and ArgoCD takes the rest from us away. So it deploys everything,
Configmaps, pods, everything that you need to
collect your OpenTelemetry data, your logs and your traces. So first step done. Yes. Okay, second step, deploy the Kube-Prometheus stack. I won't bother you with this
application because deploying an Argo application is the same every time.
We'll just go through the values a bit. So I actually needed to change this name,
but for now it's my cluster name. I deployed Prometheus and I enabled the
remote write receiver because if you want to use Alloy to send
metrics to Prometheus, you need to enable the
remote write receiver. I'll deploy Grafana with
an admin user with a super secret password. I hope you
don't share it with other people. And I configured some data sources. So earlier I said that we
use Azure managed Grafana, but for demoing purposes, I deploy
Grafana using the Kube-Prometheus stack. So I would've something to show. We deployed the alert manager and we
disable some conflicting features because both Alloy and the
Kube-Prometheus stack try to measure Kube state metrics and do
node exporting and that sort of stuff. So in one of each place
you need to disable them. So I'll disable them in a
Kube-Prometheus stack. For Loki, we just blindly copy paste the
configuration from the Loki documentation to be able to
run Loki as a single binary. In this case, we're using
Minio as an S3 storage backend. But if you were to use this in production, I would advise to use managed blob store, like what is it, S3 or Azure Blob Store. And then finally we deploy Tempo. And for this, I also just blindly copied the
configuration from the documentation, which is okay, it works. Once we're done with this, we're all set up to do all
of our backend observability. But Travor is not only
a backend application, it's also a frontend application. So to be able to monitor how
Travor is working at the client side, we're using Faro. And for that you need to
set up a separate receiver. I think the K8s monitoring team is
working on implementing this as a feature for the k8s monitoring
Helm chart. But for now, you just have to deploy
a separate Faro receiver with some configuration to send
the logs to a Loki backend and a trace backend end, and then you're good to go given that you instrument
your front end application. So what do we have to do at
the front end side of things? Let's do a little bit of zoom
in here. Same size. Okay. First, we need to configure Faro to be able to send log and
metrics to a Faro backend. And in this case, we are sending the Faro metrics of Faro traces and logs back to the next
JS application because that allows us to be able to ping the application. And if we don't get some
information back from the front end, we know that the kiosk
is actually not working. So to be able to support that we use an API that is managed via Next.js. I won't bother you too much with this
code because you can look at it after this presentation. And then finally, we'll add the frontend
observability element to our layout so it's available to all the pages
that we serve, via our Next.js app, and then you are good to go. So this is a beautiful
Next.js application that I've stolen from the Grafana website. It's an example on how
you can set up Next.js. And if you look at the network traffic, you can see that Faro is actually sending, or that the Next.js application
is actually sending Faro information back to our backend. And if you then go to Grafana
and we click on explore and we look for the next front end, we can see that there are actually
traces ending up in our system. So because this Next.js,
application is sending this request, every now and then we can see that our
application is working. So we have alerts set up that if one
of our kiosks is not sending this information, that we should send somebody to look
at that kiosk because it could be that there's a firewall rule in place, or that somebody hacked it and then
threw away the page. It happens, unfortunately. Luckily not
for the Travor product, but we see it in, I think somebody played Doom
at the kiosk at McDonald's. So you understand that it's important
to keep track of what people are doing with your product, right? And
we can also drill down in other observability stuff like
metrics, just click start, boom. All the metrics that we need
to monitor our application. And the same applies for logs. And luckily enough,
everything in the demo worked. So we could switch back to the slides and I'll click through these slides
because if the demo didn't work, I had to bore you with
slides that just showed the same as what I just showed on the screen. So I hope this gave you
some insights on how we took our approach in observability. And if you like to stay in touch,
I'm available at LinkedIn. If you want to see more of what I just
showed, you can find this product, this repo on my personal
Gitlab account. And of course, I hope to see you all at the all-attendee
party in the Museum of Pop Culture tonight.

