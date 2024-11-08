# The Story of Grafana | Episode 4: Evolution | Grafana Documentary

From an open source project to an open observability platform, Grafana's evolution continues to drive massive adoption and ...

Published on 2024-02-06T17:42:09Z

URL: https://www.youtube.com/watch?v=Iy-3A10QPIo

Transcript: Besides loving to program, I have a passion for natural
history and evolution. I read every book I can find on natural
history, evolutionary psychology. If you don't think evolution is
amazing, something's wrong with you. It's the way nature programs. I mean, how much more awesome can you get? And a reminder to all personnel in the
control room. If you require RF data, be prepared to switch over
your Grafana sources and liftoff. They're using Grafana to launch rockets! This is amazing. Many of you have heard of Call of Duty. Grafana has officially
entered popular culture. There was this Australian company who
was using Grafana to track ambulances, gave them visibility into
where their ambulances were. They could track them in real time, gave them all of their stats that they
were collecting from the ambulances. So the equipment they had on
board, what speed was it going? Did it have its lights on? And it was just a complete solution
that had been built on top of Grafana. Beehive monitoring system using Grafana. How it works is you basically put
a weighing scale under the beehive, and if the queen leaves, then the bees will swarm
and the weight will drop. The story you could tell from
looking at just a graph  was really surprising. Relief efforts - when you see Grafana
being used to track how many vaccinations have been given or how many people
have been rescued from a disaster area. There was a company that was putting
shipping containers in the middle of Paris and then growing strawberries
inside those containers. And they monitored all of their HVAC
and the hydroponic system using Grafana. And I just remember that being
really interesting because it was a non-observability use case, right?
This is kind of an IoT use case almost. The thing about dashboards in the wild, the thing about Grafana is there's nothing
in Grafana that's specific to IT or observability, right? It's just a great
general purpose visualization tool. I think the shift from the
early years to the hypergrowth, I think that has been one of the most
impactful experiences of my life. One thing I think about is when you
start a startup and people say, "Oh, you should do one thing. Do it really
well." And, uh, at the time it felt like, "No, what the hell." We're just doing lots
of things and maybe not all that well, all the time, . But that
turned out to be the thing, the one thing that we did really well
was we did lots of things. Prometheus is, we talked about before,
a good example where we were able to follow the waves. It was clear relatively early on that
I would need to work towards making Grafana the default
visualization of Prometheus. Because Prometheus desperately needed
something better than Promdash. Something maybe not even
better, but easier to use. The challenge with Promdash was you
basically, you would write it in code, right? Like, it would take time.
With Grafana, I just drag and drop, just build a dashboard really
quickly, could play with it. And, they just looked so much better than
anything we'd built with Promdash, with a 10th of the effort. The growth of Prometheus and of Grafana
have always been really tightly coupled. So making Grafana the
default of Prometheus had an outsized impact on Grafana Labs. Many of you knowTom Wilkee and
his partner David arereally into Prometheus. They
have a hosted offering. We've been talking to those
guys for the last several weeks. I first met Tom a few months ago. Me and Tom Wilkee. We had a startup
that worked in a similar space. We tried to build metrics,
logs, and traces together. It was a time when three pillars of
observability came up and we wanted to unify all of those. And then, we went
to a conference called FOSDEM Belgium. The team was there and
we ran into them, uh, chatted with them and turns out
they also wanted to build metrics, log and traces. And so we
decided to join forces. So when we joined with this
vision of bringing metrics, logs, and traces together, we also wanted
to get Grafana off the wall a bit. Because at the time, Grafana was very popular in
sort of hanging in engineering
offices on the wall, right? Like displaying the company
stats, right? Or engineering stats. But we wanted it to be more of
the center of troubleshooting. And when you troubleshoot metrics
is only the entry point, right? And then you do the logs, and then you maybe figure out with tracing
what's going on in your distributed system. And so these parts
didn't exist in Grafana, so we wanted to build those out. Like couple of months after I joined,
I went to a conference with Grafana, to FOSDEM, and there was a talk about our
observability stack and how you can jump between metrics and log and traces. And he was mentioning a lot of things
like, this is what we wanna do, and like, this is our future. At the
time, there wasn't any Tempo. Loki was very new. We didn't
have tracing visualization. And just looking back, we did all of the things that
we wanted and so much more. We always had this vision
of a Prometheus-inspired
logging system. You know, maybe a Prometheus-inspired
tracing system. And this came together with
what we now refer to as LGTM. And that's more than just the backend. It was also bringing logging and tracing
to Grafana so that you could connect Grafana to Loki originally right, to
Tempo for tracing. But at the same time, we made it so it worked really
well with Splunk, with Elastic, with our big tent philosophy, with,
with any of the data sources. You know, in hindsight, that was really the
start of Act Two for the company, when Grafana became a lot more than
just metrics. When we added logs, when we added tracing, when it
became a real observability solution. You know, going from sitting
in Torkel's kitchen and being pretty happy with where
you were, thinking, "Wow, Grafana is pretty popular." But
this rocket ship was, I think, definitely a surprise. Seeing the growth is definitely surreal.
I don't believe it sometimes . I didn't expect Grafana
to grow that quickly. This is just ridiculous and magnificent. It's really incredible. It translates
to millions and millions of users using this to make their stuff run. I think the thing that makes Grafana
really different to everything else out there is the fact that we prioritize
interoperability with this wider ecosystem. You can connect hundreds of different
data sources to Grafana and we are pretty much the only tool in
the world that does that. The big tent approach has really
defined a big part of what Grafana is. Almost anyone can bring Grafana into
their organization and really start to immediately get benefit by attaching
it to where their data already lives. The product obviously evolved
from targeting mostly open source enthusiasts to being more focused
on the wider audience these days. And an even richer plugin system,
which we're currently working on. So we can extend Grafana in
ways we can't imagine today. The word we're using
for it is "observability
platform." I'm super excited because I think that's gonna give
the same effect that plugins did, where we can't really
see all the potential, but we can still be the UI for so many
different ways of storing data and reacting to data and integrating
data. Super, super happy about that. I am just super proud of what
we built and the people we have. And it's beyond anything
that I imagined at the start. Torkel really caring about this
so much. Still does, still does. He's much more interested in the way
that someone uses Grafana than building software for the sake of building
software, which is great. That's what you want. No, I still love playing
with Grafana. It's what I do.

