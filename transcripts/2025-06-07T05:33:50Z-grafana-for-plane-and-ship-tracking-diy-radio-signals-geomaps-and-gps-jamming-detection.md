# Grafana for Plane and Ship Tracking?! DIY Radio Signals, Geomaps, and GPS Jamming Detection

Published on 2025-06-07T05:33:50Z

## Description

Grafana isn't just for apps! Mateusz shows how he built dashboards to track aircraft, ships, and mesh radios using cheap SDR ...

URL: https://www.youtube.com/watch?v=vwSbTrY2MA4

## Summary

In this video, Mateusz shares his journey into the world of Software Defined Receivers using low-cost USB devices and Raspberry Pi to track aircraft and ships. He discusses the evolution of these devices, the legalities of signal reception, and the fascinating data they can gather, such as tracking planes and ships within hundreds of kilometers. Mateusz explains his setup, which includes a home server and the use of Prometheus and Grafana for data visualization, while addressing challenges like metric formats and GPS jamming. He highlights real-world applications of this technology, including contributions to air crash investigations and maritime security, particularly in light of recent events involving undersea cable cuts. The video emphasizes how modern observability tools can extend beyond traditional applications, encouraging viewers to explore these technologies further.

# A Short Story about Radio Reception and Observability

Hey everyone, I'm Mateusz, and I'd like to tell you a short story. It all starts with this device.

When I was a teenager, USB sticks that allowed you to watch television were all the rage among some of the nerdy folks. As TV use started to decline, it was discovered that many of these USB sticks had a chipset that was surprisingly versatile. That's how low-cost Software Defined Receivers became easily available.

About a month ago, you could buy one that would do wonders for as low as about 15 bucks. I was always curious about aircraft and radio reception. When I discovered that people were building receivers based on TV tuners, and that it was fully legal to receive these signals since they are public, I knew I wanted one. I used a Raspberry Pi, and I was amazed by the results. 

With a fairly inexpensive setup of about $70, I could receive signals from planes hundreds of kilometers away. For those of you here, that's hundreds of miles! I set it up and kept it running for about a year until the memory card broke. Later, I also found out that you shouldn't connect the power input to the audio output, as that seems to break the Raspberry Pi.

Sometime ago, I returned to the topic and discovered that it's possible to receive signals from ships using the same type of setup. Why do people do this? Well, most of them probably just want to see what's around and get a free premium account at one of the tracking websites for feeding data back to them. For some, it's fascinating to see what's around them, but there are uses that go beyond personal gain.

You might have seen one of these uses in the media recently when there were news reports about undersea cable cuts in the Baltic Sea region. One of the points of interest was data from hobbyist AIS receivers that spotted a suspicious maneuver by one of the ships. The data from these receivers are also sometimes used in air crash investigations.

I wanted to set up a home server, so I recently bought a mini PC for this purpose. I wanted it to host the radio receivers for planes, ships, and some application monitoring. I also thought I needed a mobile solution, so I bought a Raspberry Pi and this specific device. 

At work, I'm writing charms that wrap observability tools such as Grafana, Tempo, Prometheus, or Mimir as part of the Canonical Observability Stack. Naturally, I wanted to dogfood the tools I’m implementing. As the saying goes, "If you own a hammer, everything looks like a nail." I thought it might be interesting to experiment and see if I could show the data from radio reception using Prometheus, Grafana, and a bit of custom exporters.

For planes, I adjusted an existing open-source Prometheus exporter for one of the most common tools called dump1090 to expose metrics for each of the planes. For ships, I modified the same codebase to parse a JSON file with currently received ships provided by the AIS-catcher. I also looked at ways to introduce other radio communication using Prometheus exporters. All of this data was scraped by Prometheus, deployed using Canonical Juju on my home server, along with Grafana.

The main problem I encountered was with the Prometheus metric format. If I wanted to show something that has a latitude, longitude, and potentially a few other rapidly changing characteristics, I couldn't use multiple values of a single metric. I probably also didn't want to use labels because of cardinality. In retrospect, I probably should have used InfluxDB, but I wanted to use Prometheus just for fun. So, I created separate metrics for latitude, longitude, altitude, and a metric that included all the metadata along with the last seen time.

I needed to write or adapt a few existing Prometheus exporters. That, combined with some simple manipulations using the Transform tab in Grafana and a Geomap component, worked surprisingly well. I realized that this approach could be used to show various data: aircraft, obviously, Meshtastic devices, and even ships or anything that has a latitude, longitude, and a presence.

Since I had access to all this data, I decided to focus more on the trends rather than the real-time state that I could get from tracking apps. I created a map of all the last locations of planes that had been recorded by my receivers. It was quite impressive to see that in some cases, it was literally hundreds of kilometers away. 

If you're fortunate enough to have access to a place where you can put a very cheap antenna outside with lots of unobstructed horizon, you can receive signals from countries away. If that's not the case but you keep the antenna close to a window inside, you could still get signals from a few dozen kilometers. In some places, this would still be enough to receive a lot of data.

It was also curious to see which countries of origin were most often detected by my receivers. The codes you see are airplane registration prefixes, which are not the same as ISO codes. For example, "SP" means Poland. Since most of my data was coming from Gdańsk, which is roughly 90 minutes by car from the Russian border, there was one especially curious omission in the data. I did see Russian aircraft, but they were not recognized as Russian by my exporter. This seems to be related to the database I was using, which either did not contain their data or purged it in 2022, as that was the last database update.

In some cases, I noticed sudden shifts in some planes' locations in the Gdańsk area. This is a good example of GPS jamming that has intensified in recent years. You won't see this on Flightradar24 because they filter out the noise and approximate, but ADSB Exchange, as you can see in the picture, does not filter the data. An overview in Grafana helped me better grasp the scale of the issue. 

One example is a Polish Airlines plane that was apparently near Moscow while it was actually descending to land in Gdańsk, about a thousand kilometers away. As for ships, the range is much lower, yet I received a couple of signals that appeared to be from the Russian coast. This prompted me to check my other maps offered by the tool gathering the data, where I saw a bunch of ships that seemed to be stuck on the shore next to a small enclosure. 

If you are familiar with OpenStreetMap, you might notice that military structures are marked in red. The one I captured even has an antenna in it. The ships also mysteriously teleported between that enclosure and Gdańsk Bay within minutes several times.

I learned a lot while conducting all these experiments. All of this would not have been possible without modern observability tools like Grafana and Prometheus. And who said observability is just for applications? 

Thank you! If you want to discuss more, you can find me at the Ask The Experts booth after the presentations. Thank you so much!

## Raw YouTube Transcript

Hey everyone. I'm Mateusz and I'd
like to tell you a short story. It all starts with this device.
So when I was a teenager, the USB sticks that allowed you to watch
television were all the rage among some of the nerdy folks. As
TV use started to shrink, it was discovered that many of these
USB sticks have a chipset that's surprisingly versatile, and that's how low cost Software Defined
Receivers started to become easily available. About a month ago. You could buy one that would do
wonders for as low as about 15 bucks. I was always curious about
aircraft and radio reception. When I discovered that people are building
receivers based on the TV tuners and that it's fully legal to receive
these signals as they are public, I knew that I want one, so I used the Raspberry Pi and I was
pretty amazed about the results. With a fairly inexpensive setup of about $70, I could receive signals from
planes hundreds of kilometers away. For those that are here, it's
hundreds of miles away as well. I set it up and kept that running for
about a year until the memory card broke, and later I also found out that you
shouldn't connect the power input into the audio output. That breaks the
Raspberry Pi, it seems. Alright. Sometime ago I came back to the topic
and also found out that it's possible to receive ships using the same type of
a setup. Why do people do this? Well, most of them probably just want to see
what's around and get a free premium account at one of the tracking websites
for feeding the data back to them. For some, it's also pretty
fascinating to see what's around you, but there are uses that go beyond the
personal gain. You might have seen one of them in the media in the recent months
when there were news of the undersea cable cuts in the Baltic Sea region. One of the points was the data from
hobbyist AIS receivers who spotted a suspicious turn of one of the ships. The data from these receivers are
also sometimes used in the air crash investigations. I wanted
to set up a home server, so I recently bought a
mini PC for this purpose. I wanted it to host the
radio receivers for planes, ships as well as some
application monitoring. I also thought I need a mobile one, so I also bought a Raspberry
Pi and this specific device. So at work I'm writing charms
that wrap observability tools such as Grafana, Tempo, Prometheus or Mimir as part of
the Canonical Observability Stack. So I obviously wanted to dogfood
the thing that I'm implementing, and there is a saying that you already
heard from this stage today that if you own a hammer, everything looks like a nail. So I
thought that it might be an interesting experiment to try to see if I can
show the data from the radio reception using Prometheus and Grafana and a bit
of custom exporters. So for planes, I adjusted an existing open source
Prometheus exporter for one of the most common tools, which is called dump1090 to expose
metrics for each of the planes. For ships, I gutted the same codebase to parse a
JSON file with currently received ships that's provided by the AIS-catcher. I also looked at ways to introduce
some other radio communication using Prometheus exporters. All of them were scraped by Prometheus
deployed using Canonical Juju on my home server together with Grafana. The main problem is the
Prometheus metric format. So if I want to show something
that has a latitude, longitude, and potentially a few other
fast changing characteristics, I cannot use the multiple values of a
single metric. I probably also don't want to use labels because of the
cardinality, and in retrospect, I probably should have used InfluxDB,
but I wanted to use Prometheus. It's always for fun. So I thought let's
create separate metrics for latitude, longitude, altitude, and potentially one that would have all
the metadata together with the last seen time. So I needed to write or adapt a few
existing Prometheus exporters out there. That, together with a few quite simple
manipulations using the Transform tab in Grafana and a Geomap component has
worked surprisingly well and as I realized, the same approach is pretty
generic. It can be used to show: aircraft, obviously. Meshtastic devices. I didn't know anything about Meshtastic
until about six months ago when I heard about a decentralized mesh radio system
that is using extremely cheap devices, saying about $15 in order to be able
to send text and position messages in a mesh. It turns out that there are
thousands of devices active all over the world, and I was able to receive
messages from dozens of kilometers away. The same approach can also be used for
ships or virtually anything that has a latitude, longitude, and a presence. There is something interesting in this
picture. I will get back to it later. Since I had access to all this data, I thought that I'd like to focus more
on the trends and not on the real time state that I could get
from the tracking apps. So I created a map of all
the last locations of planes
that have been recorded by my receivers. It was quite impressive to see that in
some cases it's literally hundreds of kilometers. If you are fortunate and have access to
a place where you can put even a very cheap antenna outside of the window
with lots of unobstructed horizon, you can receive signals that can be
countries away. If that's not the case, but you keep the antenna
close to the window inside, you could still get a few dozen
kilometers. In some places, this would be enough to
still receive quite a lot. It was also quite curious to see which
countries of origin were the most often seen by my receivers. The codes that you see here are
airplane registration prefixes, so it's not the same as ISO.
SP in this case means Poland. As most of my data was coming from Gdańsk, which is roughly 90 minutes by car
from the Russian border there was one especially curious omission in the
data. I did see the Russian aircraft, but they were not recognized
as Russian by my exporter. It looks like it was related to the
database that I was using for the planes that either did not contain
their data or purged it in 2022, as this is when the last database
update was done. In some cases I was able to see sudden shifts on some
planes' location in the area of Gdańsk. It's a very good example of GPS jamming
that is happening in this area and has intensified in the recent years. You don't see it on Flightradar24
because they filter out the noise and approximate, but for
instance, ADSB Exchange, as you can see in the picture on
the right side, doesn't do that. An overview in Grafana helped me grasp
the scale of the issue much better. An example that you can see here on the
left is a Polish Airlines plane that's apparently near Moscow. At the time it was descending to land
in Gdańsk about a thousand kilometers away. I also promised I will
get back to this dashboard. As you can see for ships,
the range is much lower. Yet, I received a couple of signals that were
apparently from the Russian coast. It prompted me to check out my other maps
that were offered by the tool that was gathering the data and there I saw a bunch
of ships that were seemingly stuck on the shore right next to a small enclosure. If you are familiar with OpenStreetMap, you can notice that the military
structures are marked with the red color. This one that we see here
even has an antenna in it. The ships also mysteriously teleported
between there and Gdańsk Bay within minutes a few times. I learned a lot
while doing all these experiments. All that wouldn't be anywhere new that
easy without the modern observability tooling such as Grafana and Prometheus. And who said that observability is just
for applications? Right, thank you. In case you want to discuss more, you can find me at the Ask The
Experts booth after the presentations. Thank you so much.

