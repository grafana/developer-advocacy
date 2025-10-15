# Thriving Venus Flytraps in Scotland? Yes. Thanks to Grafana, Loki, Prometheus, and OpenTelemetry

Published on 2025-06-07T05:35:05Z

## Description

Can Grafana help you grow Venus flytraps and Nepenthes in Scotland? Spoiler alert: Yes. With Loki logs, Prometheus metrics, ...

URL: https://www.youtube.com/watch?v=evvMTFrEknA

## Summary

In this YouTube video, the host, who works for Grafana, shares their passion for carnivorous plants, a hobby they've cultivated for three years. They introduce various types of these plants, focusing on the Venus flytrap, the Sarracenia, and their favorite, the Nepenthes, explaining their unique characteristics and growth requirements. The host discusses their journey of successfully growing these plants indoors in Scotland, overcoming challenges related to light, temperature, and humidity with the help of IoT technology, specifically using Raspberry Pis to monitor and automate conditions. They demonstrate how they've integrated OpenTelemetry and Grafana to manage humidity levels and diagnose plant health using machine learning. The video concludes with reflections on the insights gained from this project and an invitation for viewers to learn more about carnivorous plants.

# Carnivorous Plants and IoT: My Journey

So, I promise I won't sing for long. We'll see how it goes! Today, I'm excited to talk to you about **carnivorous plants**. This has been a passion project of mine for about three years, and my partner is even more excited because I finally have someone else to discuss it with!

### A Bit About Me

By day, I work for **Grafana**, focusing on all things Loki. Please be nice to me! By night, I'm a big gamer, a Lego enthusiast, and an IoT enthusiast. However, there's one hobby I haven't mentioned, and that's my love for **carnivorous plants**. This is where I usually lose people at parties—they tend to run away! 

### What Are Carnivorous Plants?

How many of you know what a carnivorous plant is? *Okay, cool!*

Carnivorous plants gain their nutrients—not energy—by ingesting live prey such as ants and other invertebrates. There are actually 12 families of carnivorous plants, but today I'll focus on three that I raise myself:

1. **Dionaea muscipula (Venus flytrap)**: A fun fact about them is that they can count to two. A fly must trigger two hairs in the trap within 30 seconds for it to close, which saves the plant's energy.
   
2. **Sarracenia (trumpet pitcher plant)**: This plant is located in the U.S. 

3. **Nepenthes (tropical pitcher plant)**: My personal favorite! Some species of Nepenthes can hold up to one liter of digestive juices and can even eat rats, which is pretty crazy.

### Growing Conditions

The Venus flytrap and Sarracenia are located in the U.S., where they need a lot of light, high temperatures, and high humidity. Nepenthes require even more, thriving at 25 degrees Celsius with 70 to 90% humidity. Meanwhile, I'm in **Scotland**, where on a good day, we get between 2,000 to 10,000 lux of sunlight, with summer temperatures ranging from 5 to 12 degrees. The humidity is decent, but when trying to grow these plants indoors, it’s not ideal.

### My Journey with Carnivorous Plants

I attempted to grow these as a kid, placing them on a windowsill, only for them to die within a month. As an adult, I was determined to do better. I wanted to regulate the temperature and humidity to see these plants thrive in Scotland. 

On the left, you can see what they looked like as juveniles. Fast forward a year, and while they did grow considerably in my small fish tank, I became a victim of my own success. They grew out of the tank and required more humidity. The grow light was drying them out, causing me to experience crisping of leaves and shorter lifespan for the pitchers, which lasted only two to three weeks instead of the expected one to six months.

### IoT Solutions for Plant Care

As an IoT and automation enthusiast, I needed to save the day. Here’s my setup: 

- **Three Raspberry Pis**: One dedicated to sensor readings, using an I2C board with a waterproof humidity and temperature sensor to regulate humidity in the tank. 
- A camera is tethered to the same Raspberry Pi, where all the data is instrumented with **OpenTelemetry**. I decided to send the sensor data in OpenTelemetry format to our platform.
- **Alloy** is collecting those metrics and batching them, sending them to **Loki**, **Prometheus**, and **Grafana** on the same Raspberry Pi. 

In Grafana, I set up an alert that triggers a humidifier when humidity drops below 80%, keeping the environment regulated.

### Live Demo

Now, let’s switch to the demo! 

As I VPN into my home (it’s probably 3 AM there), I won’t turn on the plant light to avoid waking my partner. You can see the temperature and humidity levels are doing quite well. 

By looking at the past 24 hours, you can see the humidity peaks and troughs in the graph. When it drops, Grafana alerts me, and I trigger the humidifier to bring it back up to 80%.

I also went a bit crazy with **LLMs** earlier this year. I take a snapshot of the tank at 9 AM and 5 PM, send it to **ChatGPT**, and ask it to analyze the plants for any signs of stress, such as yellowing leaves. It automatically detects the plants in the images and provides diagnostics, which I log in OpenTelemetry format.

### Results and Takeaways

To wrap up, my plants are now thriving! The pitchers last up to five months, and humidity is consistently high. 

Some key takeaways from my journey include:

- I reduced my water consumption significantly, going from three bottles a week to just one. This is important because I need reverse osmosis or distilled water.
- I treated myself to a new terrarium, much to my partner's dismay—we had planned to use that money for painting our living room!
- This IoT project taught me a lot about OpenTelemetry and **PromQL**, grounding my experience in understanding a new query language.
- Lastly, I’ve gained the confidence to invest in more plants. I recently acquired two juvenile Nepenthes, which I hope will grow into healthy adult plants.

Thank you for your time! If you'd like to learn more about carnivorous plants, come see me at the Experts booth!

## Raw YouTube Transcript

So I promise you I will not sing
for long. We'll see how we go. Little Shop of Horrors. No. So today I'm talking to you
about carnivorous plants. This has been a passion
project for about three years. I'm super excited to tell you about it. My partner is more excited because I
finally have someone else to talk to apart from them about it. So a
little bit about me. Oh, I'll skip that one. There we have me. By day I work for Grafana
doing all things Loki. I mean your community. Be nice to me. And then by night I'm a big
gamer Lego enthusiast and IoT enthusiast. But there's one hobby I'm
missing on this and that is the carnivorous plants. And this is
where I lose people at parties, they normally go running. So what are carnivorous plants? Hands up. How many people know what a carnivorous
plant is? Okay, cool way. There we go. So carnivorous plants, if you
don't know, gain their nutrients, not their energy. Then nutrients through
ingesting live prey like ants and other invertebrae and so forth. There are actually 12 families
of carnivorous plants, but I'm only going to talk about
free today, the ones I raise myself. So the most famous one Dionaea
muscipula is your Venus flytrap. And a fun fact you didn't know about
them is they actually count to two. So you have to trigger
two hairs in a trap, let's say a fly triggers two
hairs and within 30 seconds, and that closes the trap that saves
that plant's energy. Sarracenia a trumpet pitcher plant
that's located in the US. And then my personal
favorite is the Nepenthes, the tropical pitcher plant.
A fun fact here, and I'm growing one, I've only got a juvenile at the moment, is some genus of Nepenthes
can hold up to one liter of water, one liter of digestive
juices is what I should say. And they can eat rats,
which is pretty crazy. So what we're here to do today
though is talk about location. So Venus flytraps and
Sarracenia are actually located here in the US and you can
see they need a lot of light, a large amount of temperature, and
their humidity has to be quite high. Nepenthes even more so 25 degrees over 70 to 90% humidity, which is wild. And then there's me in Scotland
where this is probably on a good day. We get 2000 to
10,000 lux of sunlight. It's about five to 12
degrees. That's our summer. And the humidity is pretty good, but
when you're trying to grow them inside, it's not great.
So bit of a timeline for you. I did try to grow these as kids
and I think we all did, right? You've put them next to a window seal
and then about a month they're dead and then you cry and then your mom and dad
throw them away and you never think about them again. Well, me as
an adult, I said, no, it has to be better. I have
to do better. And so I said, I am going to regulate the
temperature of these plants. I'm going to regulate the humidity. I want to see these things
blossom in Scotland. And so on the left hand side you can
see what they look like as juveniles and then cut to a year later,
they are slow growing plants. You can see they actually grew quite
considerably inside in the small little fish tank that I had them in.
The problem though was I was actually a victim of my own success. They actually grew out of the
tank and they became a problem. They needed actually more humidity. The grow light I was using
was drying the plants out. So I kind of had this problem here
where when you look at Nepenthes, their pictures are meant to last from
one month to six months depending on the genus. But mine were lasting
maybe two weeks to three weeks, which was such a shame. And you can see
all the crisping of lids and stuff here. So as an IoT and automation enthusiast, I've thought I needed
to save the day here. And here's my crazy architecture. I have three Raspberry
Pis running for this. Now I have a Raspberry Pi
dedicated to sensor reading. So I have using the I2C board here, I have a waterproof humidity and
temperature sensor that regulates mostly for me the humidity in the tank that
I need. And then I have a camera tethered to the same Raspberry
Pi. More on that in a moment. That's where Loki comes into this. All of that data or that telemetry is
actually instrumented with OpenTelemetry because I wanted to know
about OpenTelemetry and I
thought why not put sensor data into OpenTelemetry format
and send that to our platform, which has been interesting. Then I have Alloy sitting there
collecting those metrics, batching them, and then I send them to Loki
and Prometheus and Grafana all on the same Raspberry Pi. The cool thing for me though on Grafana
is that I actually have an alert that triggers and this points to node red. And so if the humidity
drops below a certain level, you will trigger the humidifier
automatically so I can keep the humidity at the regulated level, which I've set at is 80%.
And hopefully without any further ado, can I swap to the demo?
I'm going to try and do this live. Hey, there we go. So this
is me VPNing home currently. I dunno what time it is at home at the
moment, probably three in the morning. So I'm not going to turn the plant light
on because I'll wake up my partner. But you can see the temperature, humidity, the humidity regulations
actually doing quite well. And if I jump back
about the last 24 hours, hopefully you can see based
upon this graph here in Grafana, all of the times I've had
peaks and troughs in the humidity. So you can see that as
the moment it drops down, I kind of wait a minute based upon
Grafana is alerting and then I trigger the humidifier and you can see
the increase back to 80%. So it keeps it at a regulated humidity. What's interesting is this bit, I went a little bit crazy
with LLM's earlier this year, and if I quickly view
this panel here, sorry, that's not very big. If I plus this one, hopefully
that's a little bit better. You can see what I've done here. Oh
sorry, can we go back to the demo? Is that possible? Is the demo gone? Can we swap back to the,
no, there we go. Okay, sweet. So we have this log here and essentially
in this log is basically what I've done is I take a snapshot
of the tank at 9:00 AM and 3:00 PM and basically
what I do, sorry, 5:00 PM And what I do from there
is I then take the picture, send it to ChatGPT OpenAI, and then I take that and process it
and ask it to basically prompt as a plant doctor and I look for
those crispiness in the pictures. I ask it to look for yellowing of leaves
and then I convert it based upon a format back into logs into the
OpenTelemetry format. And what you can see here is it actually amazingly
detects the plants automatically. It even detects where they are in the
position of the picture and gives me a warning level. It gives me
plant diagnostics over them. So you can see some yellowing of
the leaves on the top left one, maybe that's a bit of
stress on that plant. And another cool thing I did here
was I did full tank analysis as well. So as well as sending the picture
and aggregating the photo, I also send up the Prometheus temperature
metrics and the humidity and then I ask it to have a look at those over the
course of eight hours and process what exactly is going on. So
that is the live demo. I can jump back. Oh sorry, I should show you the picture here they
are TA and thanks to Volkov Labs for their plugin here. This, so I could only
bring this picture in because of them. So if we swap back to
the slides, hopefully. So to wrap up if I skip
through these ones, that was just in case the demo
gods were not in my favor. We have beautiful pitchers now
these are lasting up to five months for me. Currently humidity is
staying high, which is fantastic. My takeaways from this were that I
actually reduced my water consumption. I was basically using the humidifier
on an automated cycle every hour. I don't need to do that anymore. So I went down from using three bottles
of water a week, which was expensive. It needs to be reverse osmosis
water or distilled water. And I reduced it to one. I
needed a new terrarium. Well, I didn't need a new terrarium, but I
just wanted to buy a new terrarium. That looks really nice. So
this has kept me really happy. It's kept my partner really sad. We wanted to use that money on painting
the living room, but here we are. And then for me, IoT projects taught me
a lot about OpenTelemetry and also about PromQL. Coming from an Influx
world, when I joined Grafana, I had to learn PromQL. And this for me was the way I grounded
my experience in understanding a new query language. And last but not least,
it gave me confidence to invest. I now, if you can see these two little
juvenile Nepenthes here. Yeah, they cost me a small fortune from a
really shady dealer down in South England. But I'm confident now that hopefully these
will grow into adult plants and we'll see what happens. Thanks very much.
Come see me at the Experts booth. If you'd like to learn more
about carnivorous plants.

