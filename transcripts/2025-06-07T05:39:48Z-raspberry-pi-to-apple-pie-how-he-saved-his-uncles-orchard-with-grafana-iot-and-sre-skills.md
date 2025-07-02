# Raspberry Pi to Apple Pie: How He Saved His Uncle’s  Orchard with Grafana, IoT, and SRE Skills

Published on 2025-06-07T05:39:48Z

## Description

When Arthur Kepler's uncle passed away, he inherited a unique challenge: keeping a remote, off-grid orchard alive. Armed with ...

URL: https://www.youtube.com/watch?v=cpGARiAnQ5g

## Summary

In this talk at GrafanaCON, the speaker shares a personal story about automating a family orchard in Washington State using DIY technology and IoT principles, inspired by his late uncle Steve, an expert entomologist and apple grower. He emphasizes the importance of site reliability engineering (SRE) skills in managing small-scale agriculture, showcasing how inexpensive components and open-source tools like Grafana can be used for remote monitoring and control. The speaker discusses challenges faced, such as irrigation management, power supply concerns, and network reliability, while highlighting the integration of various technologies like MQTT, Raspberry Pi, and PoE for effective system operations. He concludes by encouraging engineers and hobbyists to leverage their skills in personal projects, which can enhance both their professional and personal lives.

# IoT and Automation in Agriculture: A Personal Journey

Hello, GrafanaCON! It was super cool to see IoT on the moon, but today’s talk will be much more rooted on Earth. As usual, we have the Q&A through the Slido web app. If you need more time to take a picture of the QR code, it will be on another slide shortly.

In this talk, I want to share a story that connects to quintessential Washington State industries: technology and fruit orchards. Washington proudly leads the nation in the production of apples, cherries, pears, blueberries, and more—all grown lovingly on the sunnier side of the Cascade Mountains. My goal is to inspire those who may be starting out in site reliability engineering, as well as those with gardens or family properties they'd like to enhance through automation.

There are many like myself who tinker with projects and come away honing their skills, which then become really useful at work. This isn’t about big agribusiness or expensive high-end systems; it’s about using DIY craft and inexpensive components to remotely control, automate, and monitor a property—from four hours away. In keeping our family’s orchard verdant, I’d like to share what I’ve learned in the process.

### A Personal Connection

Seven years ago, when my wife and I were expecting our second child, with our first not quite a year old, we took a September Babymoon road trip. We 4x4'd, camped, and fished in the beautiful Northern Rockies. On the way home, we stopped to visit my Uncle Steve, who was always game for fishing trips or hikes in the North Cascades wilderness where he lived. Uncle Steve was the prototypical mountain man, living in an off-grid cabin that he built himself in the 1980s.

After retiring from the Forest Service, he became an expert entomologist, studying native pollinators and researching the cultivation of apples and currants. His apple trees featured up to 40 different grafts on a single trunk, each producing a different variety. His orchard yielded a progression of fruit through the growing season—currants in June and July overlapping with cherries, then later in the summer, peaches, apricots, and plums, followed by apples, pears, and quinces in the fall. 

After several wonderful days visiting, we headed home with a bounty of apples and plums. These would actually become both of my kids' first baby food. Just six weeks later, I received tragic news. The evening after a long-haul flight to the Philippines to visit his daughter, my uncle suffered an embolism that he did not survive. There's a reason they say to get up and walk around during these long-haul flights. We still miss him deeply.

Steve was my mother's brother and a father figure who taught me about the great outdoors: fishing, hunting, and working with the land—an important balance for a city kid brought up by artsy techie parents. My family immediately recognized what a treasure we had in my uncle's research orchard, and that come spring, it would need water to survive. Being both remote and off-grid made this extraordinarily challenging. 

Beyond helping the family, including his young daughter overseas, I felt called to use my tech skills to help keep the orchard alive while the complicated estate process progressed. My career path had unknowingly prepared me for this challenge. After graduating university, I landed a job programming sophisticated AV and home automation systems in Aspen, Colorado—long before IoT (the Internet of Things) became a buzzword. I worked with custom controllers and specialized hardware, learning everything from relays to wireless Zigbee networks. 

Perhaps more importantly, I developed complex problem-solving skills and learned the value of testing before deployment. Through subsequent software roles, I moved into backend programming and then DevOps and site reliability engineering. I led an SRE team at a healthcare startup here in Seattle when the story began.

### Challenges of Automation

In the next segment, I’ll walk you through the specific challenges of automating and monitoring an off-grid orchard, showing how we can apply enterprise SRE principles to small-scale agriculture and use open-source tools like Grafana, as well as inexpensive hardware. You’ll see how skills we build in our professional lives can enhance personal projects and how hobbies can reinforce our careers in unexpected ways.

The overall goal was delivering water to the plants and trees in this orchard. Sounds simple enough, right? The IoT space has many irrigation options. Serious agriculture uses systems costing tens or hundreds of thousands of dollars, which are proprietary and not available through retail channels. Then there are consumer-grade options, which are largely cloud-based, have minimal security, and the inability to connect locally to an automation platform—not ideal for a critical system.

I evaluated several options like OpenSprinkler, but they were designed either for small garden-hose-sized output or they used power-hungry solenoid valves common in residential lawn systems. For this humble solar-powered off-grid system, every watt needed to be conserved. Through a previous hobby—home brewing—I discovered a device for automating water systems: mechanical ball valves. These simple mechanisms use a small electric signal to turn a metal valve and let water pass. 

For simplicity, I chose normally-closed valves that open when a current is applied and automatically close when power is cut. For remote control, I needed some type of smart-relay device. Eventually, I selected Signoff four-channel pro relays, which are general-purpose smart switches that are cloud-based by default, DIY-friendly, and use custom microcontroller chips that support flashing with custom firmware. Think of it like replacing Windows on a new laptop and installing and tailoring Linux to your liking. 

This allowed me to eliminate cloud dependencies and create a fully programmable, locally controlled system. Though I mostly use Wi-Fi devices due to the prevalence of hardware options, I highly recommend considering Zigbee and Z-Wave radio-based technologies as alternatives, especially for battery-operated sensors. Home Assistant is a great platform, which I do use at home, but for utmost reliability in the orchard, I used very few software dependencies—just Espurna for firmware, MQTT for coordination, and some crontab scripts for automation.

### The Irrigation System

The orchard has two irrigation systems: tall sprinklers on riser pipes that my uncle had manually positioned, and a neglected set of drip irrigation lines. I started by rehabilitating the sprinklers, but the following spring, I replaced and upgraded the drip system, which now forms the backbone of the irrigation. This project taught me more about plumbing than I ever expected to learn!

My practical recommendation for automating gardens or small orchards: invest in quality black polytube and high-grade mini-sprinkler emitters. Online irrigation supply shops have much better options than you’ll find in big box stores. I’ll link to recommendations on my website at the end of this talk.

As a site reliability engineer, understanding failure modes is critical, and the same principle applies to farming. This orchard faces numerous potential failure modes, both technical and environmental. For example, during a heatwave while I was visiting family in New Mexico, the PFSense router’s DHCP server failed, preventing the valve controllers from connecting to the network and leaving trees without water. 

This lesson: set static IP addresses directly on critical devices to build network resilience when possible. The most reliable systems are the simplest, especially with IoT. A perfect example is MQTT—a messaging protocol that serves as a communication hub within an IoT network. Think of it as a digital post office; it ensures messages get delivered between devices even when connections are intermittent. This lightweight but powerful protocol runs perfectly on a Raspberry Pi, alongside InfluxDB, the time-series database, and Grafana, the visualization platform we know and love.

### The Network Operations Center

These electronics reside in what I affectionately call the "network operations center," an upstairs room in the cabin that can reach pretty high temperatures in the summer, lacking the luxury of air conditioning. Heat, of course, is the enemy of reliability with electronics. It’s crucial to derate hardware in hot conditions, especially current-carrying components like smart plugs and solar chargers. 

For network reliability, invest in "prosumer" networking hardware like Ubiquiti or MikroTik equipment. My initial, budget-conscious approach was using custom firmware like DD-WRT or Fresh Tomato on consumer-grade Netgear devices, which, along with later PFSense on a small Intel device, yielded mixed results. Eventually, I replaced this with MikroTik and relegated the Netgear devices to access-point duty, significantly improving reliability.

The orchard operates with two irrigation pumps: the primary is a remarkable piston pump that runs directly off solar panels without controllers or power conversion, boasting 75% greater efficiency than AC pumps and performing well even in low light conditions—popular among off-grid enthusiasts. Every component of this pump is serviceable and replaceable, even decades later. My uncle purchased this pump in 2002. 

It had fallen into disuse and was full of rust when I began. After a thorough reconditioning with a rebuild kit, and a few years later replacing the entire corroded wet-end, this 23-year-old pump now runs perfectly on the original solar array of the same age—a testament to solar technology's longevity! 

Of course, there are times when a 120-volt alternating current pump running on the cabin's main battery bank inverter is actually a better choice, like during smoky weather or if the solar pump has lost its priming. This powerful AC jet pump serves as a backup, enabling overnight watering.

### Electrical Challenges

Pumps, being large motors, pose unique electrical challenges, particularly with a solar pump's low voltage, high amperage direct current. Simply switching this pump on and off proved surprisingly difficult. Unlike alternating current power, which naturally cycles 60 times a second, breaking electrical arcs, direct current creates severe arcs when switching between contacts, especially with inductive loads like motors. 

I went through a lot of IoT hardware, learning about in-rush and flyback current. After burning through numerous relays and witnessing my share of angry pixies and magic smoke, I even destroyed a 60-amp solid-state relay in spectacular fashion! The solution: have small smart relays actuate much bigger dumb relays. So the solar pump now uses a 120-amp automotive relay, while the AC pump uses a Zigbee contactor rated well beyond its required capacity. A key takeaway: always bench-test your ideas! Research and development is far easier in your workshop than troubleshooting in the field.

Initially, this project lacked any real telemetry or monitoring. After getting irrigation running, I quickly deployed a cheap cloud-based baby monitor camera looking out of a window of the cabin. This camera could barely show if sprinklers were running due to low resolution and required AC/mains power. I later upgraded this solution with a better Raspberry Pi and a USB camera that was mounted higher on the cabin, positioned with a large basin in view. 

This setup allowed me to see the basin filling, indicating that either the sprinklers were running or rainfall had happened. The next evolution placed a Raspberry Pi camera in the wellhouse aimed at an analog pressure gauge, and it also had a mirror showing the pump’s piston rod. Today, more sophisticated cameras are mounted on tall poles, providing comprehensive views of the property. 

While that original wellhouse camera has been replaced with one focused on a large analog gauge that now graces my Grafana dashboard, readings from a flow meter display both the flow rate and cumulative daily usage. Finding the right flow meter required significant research. It needed to be at least an inch in diameter and designed to prevent ice damage. I eventually found what I’d call a light-industrial model for about $120. It emits a pulse via a reed switch per gallon of flow. 

Monitoring this was perfect for an Arduino project: a tiny ESP-8266 chip, smaller than my thumbnail, counts these pulses and reports every 10 seconds to the MQTT server. It also hosts a tiny web server providing JSON metrics about flow and its own power state. If you’re a tinkerer, ESP microcontrollers are definitely worth exploring.

### Power Management

With irrigation in place, I turned to another critical resource: power. Remember, this orchard is off-grid and originally had a very small aging battery bank, so electricity had to be rationed and monitored very closely. My weather station publishes solar luminance data to a Raspberry Pi, which updates MQTT. Combined with this data and data from the solar charger about panel production and battery state, I created logic to select the best pump at any given time.

I have a Python script that runs every 10 minutes in cron. This is basically it in pseudocode:

```
If solar luminance > 450 watts per square meter: 
    use the solar pump
Else if battery bank > 70% charged or solar production > AC pump usage: 
    use the AC pump
Else: 
    turn off the pumps and try again later
```

Using metrics in automation is absolutely powerful. While metrics drive automation, dashboards are equally important—especially at a Grafana conference! Next to my cabin’s door hangs a repurposed old Amazon Fire tablet running Grafana in kiosk mode. My solar dashboard displays color-coded metrics: green for wall charging, yellow and red when draining. This shows the battery state, power flow, and the draw on critical systems. 

Grafana has become the component my family interacts with the most, providing an intuitive visual representation of our property’s power state, from 100% in green to critical levels in red. Particularly when we’re visiting in the winter, decisions like running the dishwasher or using the electric kettle versus the gas stove to brew coffee in the morning are made much easier thanks to Grafana.

### Ongoing Challenges

Power challenges have been a recurring theme in the system’s evolution. In the early days, I traced one mysterious outage to a mouse that had chewed through a router’s power connector, causing intermittent shorts. The solution involved acrylic tubing, making some protective sleeving, and thoroughly sealing the cabin. Unfortunately, my wife isn’t fond of getting a cabin cat.

The aging solar system consisted of 35-year-old panels from 1990 and another array from 2002, powering four gigantic golf cart batteries! Then I found I could save about 15% of battery capacity by directly using DC for all critical telemetry, networking, and irrigation loads instead of inverting to AC and then back to DC. Most consumer networking hardware runs on 12-volt DC, so this made it easy to adapt from the 24-volt battery bank. 

For IoT devices, I added a 5-volt bus, although later I discovered that powering through Raspberry Pi USB ports provides much better and reliable voltage regulation than through GPIO pins. I also discovered through monitoring that when low batteries start charging and don’t have quite enough charge, you get brownouts that especially affect things like wireless antennas. These were a common source of issues, easily solved by low voltage disconnect switches.

The big game changer was implementing power-over-ethernet (PoE) to power all critical systems such as irrigation and networking. This 48-volt standard powered everything from cameras to directly actuating water valves. A 150-foot Ethernet run to a gate camera was extended later to power my irrigation manifold, leveraging PoE to both directly open valves and run their IoT controllers. 

Though powering irrigation valves directly with PoE does lend a certain "nerd cred," I actually don’t recommend doing this—it turns out that when valves accumulate rust, they draw more current to open, which again causes brownouts affecting the controllers. 

When I was given a friend’s solar panel, I used it (which doubled as a roof) to charge a 20-amp-hour medium-sized lithium battery, which was more than enough for seasonal use. For remote access today, the options for VPNs have never been better with choices like TailScale, Wireguard, and CloudFlare tunnels. I actually use multiple VPNs hosted on different devices. 

We use Starlink, which uses carrier-grade NAT. Unfortunately, that prevents any form of inbound connectivity, limiting some options. All in all, the non-trivial network integrations I’ve created have allowed a reliable ability to monitor and control irrigation, gather camera imagery, and even deploy firmware upgrades to controllers like the flow meter. 

Of course, my favorite thing to access remotely is Grafana, giving me rich real-time or historical telemetry on one pane of glass. A future goal is building interactive command functionality into Grafana, such that I can press panel elements to trigger pumps and zones.

### Conclusion

After the first summer managing my family’s orchard, I had an opportunity to interview at a very well-known tech company. Their Production Engineering teams are proud of the high bar they have for system design and networking interviews, and my experience prepared me well! I landed the job and leveled up my career right at a pivotal time. 

Such was the case that the stock grants earned from this new job provided the means to purchase the property outright later when the estate was settled. Not only did this help empower my young cousin’s future, but it also unlocked the ability to invest in upgrades beyond what I could do as a caretaker. 

As I’ve progressed in my career in the years since, concepts of troubleshooting, learning many trades, and gaining experience with tools like Grafana have been very beneficial to me as an engineer. The work I’ve created has led to a well-loved monitoring stack at work, which uses Grafana, Alloy, and Loki to great effect. 

The orchard now thrives, with care provided both up close and from afar. My children enjoy Easter egg hunts among the trees that their great uncle planted, and the fruit keeps our year filled with delicious snacks, preserves, and pies. It’s still real work, but technology has made this much easier to balance.

To all the busy engineers and tinkerers out there: I hope this story has been inspirational in encouraging your hobbies and experimentation. If you’re interested in more details like code, irrigation equipment, and hardware recommendations, I have a site at [ArthurK.com/orchard](http://ArthurK.com/orchard). I’d also be happy to answer any questions you may have after the talk. You can also find me at the "Ask the Experts" booth. Thank you so much!

## Raw YouTube Transcript

Hello, GrafanaCON. So that was super cool
seeing IoT on the moon. This IoT talk will definitely be
much more rooted on the Earth. So as usual, we have the Q&A
through the Slido web app. If you need more time to take
a picture of the QR code, it will be on another slide
in a little bit. So in this talk, I will share a story
connecting to quintessential
Washington state industries: technology and fruit orchards. Washington proudly leads the
nation in production of apples, cherries, pears, blueberries, and more-all grown lovingly on the
sunnier side of the Cascade Mountains. So my goal is to inspire those who may
be starting out in site reliability engineering, as well as those with gardens
or family properties they'd like to enhance through automation.
There are many like myself, who tinker with projects and
come away honing their skills, which then become really useful at work. So this isn't about big agribusiness
or expensive high-end systems. It's about using DIY craft
and inexpensive components to remotely control, automate, and monitor a property in this
case from four hours away. In keeping our family's orchard verdant, I'd like to share what I've
learned in the process. So seven years ago when my wife and I
were expecting our second child, with our first not quite a year old, we took a September Babymoon
road trip. We 4x4'd, camped, and fished in the
beautiful Northern Rockies. On the way home we stopped
to visit my uncle Steve. He was always game for fishing trips or
hikes in the North Cascades wilderness where he lived. Uncle Steve was the prototypical
mountain man living in an off-grid cabin. He built himself in the 1980s. After retiring from the Forest Service,
he became an expert entomologist, studying native pollinators
and researching the cultivation of apples and currents. His apple trees featured up to 40
different grafts on a single trunk, each producing a different variety. His orchard yielded a progression
of fruit through the growing season. So currents in June and July
overlapping with cherries, and then later in the summer,
peaches, apricots and plums, followed by apples, pears
and quinces in the fall. After several wonderful days visiting, we headed home with a
bounty of apples and plums. These would actually become both
of my kids' first baby food. Just six weeks later,
I received tragic news. The evening after a long haul flight to
the Philippines, to visit his daughter, my uncle suffered an embolism
that he did not survive. There's a reason they say to get up
and walk around during these long haul flights. We still miss him deeply. Steve was my mother's brother, and a father figure who taught me
about the great outdoors: fishing, hunting, and working with the land. An important balance for a city kid
brought up by artsy techie parents. My family immediately recognized what a
treasure we had that my uncle had left behind his research orchard,
and that come spring, it would need water to survive. Being both remote and off-grid made
this extraordinarily challenging. Beyond helping the family, including
his young daughter overseas, I felt called to use my tech skills to
help keep the orchard alive while the complicated the estate process progressed. So my career path had unknowingly
prepared me for this challenge. After graduating university, I landed a job programming sophisticated
AV and home automation systems in Aspen, Colorado. This was long before IoT (The
internet of Things) became a buzzword. So I worked with custom controllers
and specialized hardware learning everything from relays to
wireless Zigbee networks. Perhaps more importantly, I developed complex problem solving
skills and learned the value of testing before deployment. Through subsequent software roles, I moved into backend programming
and then DevOps and site reliability engineering. I led an SRE team at a healthcare
startup here in Seattle when the story began. In the next segment, I'll walk you through specific challenges
of automating and monitoring an off-grid orchard, showing how we can apply enterprise
SRE principles to small scale agriculture, and use
open-source tools like Grafana, as well as inexpensive hardware. You'll see how skills we build in
our professional lives can enhance personal projects and how hobbies
can reinforce our careers in unexpected ways. So the overall goal was delivering water
to the plants and the trees in this orchard. Sounds simple enough, right? The IoT space has many
irrigation options. Of course, serious agriculture uses systems
costing tens or hundreds of thousands of dollars, and these are proprietary and
not available through retail channels. And then there are consumer grade
options, which are largely cloud-based, have minimal security and the
inability to locally connect to an automation platform. Not
ideal for a critical system. I evaluated several options
like open sprinkler, but they were designed either for
small garden-hose sized output, or they use power hungry solenoid valves. Common in residential lawn systems. For this humble solar
powered off-grid system, every watt would need to be conserved. Through a previous hobby-Home Brewing-I
discovered on a deal device for automating water systems
mechanical ball valves. These simple mechanisms use a small
electric signal to turn a metal valve and let water pass. For simplicity, I chose normally-closed valves that
open when a current is applied and automatically close when power
is cut. For remote control, I needed some type of smart-relay device. Eventually I selected these
Signoff four channel pro relays, which are general purpose smart
switches that wall cloud-based by default are DIY friendly, and they use custom microcontroller
chips that actually support flashing with custom firmware. Think of it like replacing windows on a
new laptop and installing and tailoring Linux to your liking. This allowed me to eliminate
cloud dependencies and
create a fully programmable, locally controlled system. Though I mostly use wifi devices due
to the prevalence of hardware options, I do highly recommend considering Zigbee
and Z-Wave radio-based technologies as alternatives. And these are especially good
for battery operated sensors. Home Assistant is a great
platform, which I do use at home... but for utmost reliability in the orchard, I use very few software dependencies. So no Home Assistant here-just
Espurna for firmware, MQTT for coordination, and some crontab scripts for automation. The orchard has two irrigation systems, tall sprinklers on riser pipes that
my uncle had manually positioned, and a neglected set of
drip irrigation lines. I started by rehabilitating the
sprinklers, but the following spring, I had replaced and
upgraded the drip system, which now forms the
backbone of the irrigation. This project taught me more about
plumbing than I ever expected to learn! So my practical recommendation
for automating gardens or small orchards: invest in quality black polytube
and high-grade mini-sprinkler emitters.
Online irrigation supply shops have much better options
than you'll find in big box stores. I'll link to recommendations on my
website at the end of this talk. So as a site reliability engineer, understanding failure modes is critical, and the same principle applies to farming. This orchard faces numerous
potential failure modes, both technical and
environmental. For example, during a heatwave while I was
visiting family in New Mexico, the PFSense router's DHCP server failed, and this prevented the valve controllers
from connecting to the network and leaving trees without water. This lesson: set static IP addresses
directly on critical devices, building network resilience when possible. The most reliable systems are the
simplest, especially with IoT. A perfect example is MQTT:
A messaging protocol, which serves as a communication
hub within an IoT network. Think of it as a digital post office. It ensures messages get delivered
between devices even when connections are intermittent. This lightweight but powerful protocol
runs perfectly on a Raspberry Pi, alongside InfluxDB, the
time-series database, and Grafana, the visualization
platform we know and love. These electronics reside in
what I affectionately call
the "network operations center", an upstairs room in the
cabin that actually can reach
pretty high temperatures in the heat of summer, lacking the
luxury of air conditioning. And heat, of course, is the enemy of
reliability with electronics. So it's crucial to derate
hardware and hot conditions, especially current carrying components
like smart-plugs and solar chargers for network reliability, invest in "prosumer" networking
hardware like Ubiquiti or MikroTik equipment. My initial, budget conscious approach was
using custom firmware like DD-WRT or Fresh Tomato on
consumer grade Netgear devices, and this along with later,
PFSense on a small Intel device, yielded mixed results. Eventually
replacing that with MikroTik and relegating the Netgear devices to
access-point duty significantly improved reliability. The orchard operates with
two irrigation pumps: The primary is a remarkable piston pump
that runs directly off solar panels without controllers or power
conversion boasting 75% greater efficiency than AC pumps and
performing well even in low light conditions, popular among
off-grid enthusiasts. Every component of this pump is
serviceable and replaceable even decades later. My uncle
purchased this pump in 2002. It had fallen into disuse and
was full of rust when I began. After a thorough reconditioning
with a rebuild kit, and a few years later replacing
the entire corroded wet-end, this 23-year-old pump now runs perfectly
on the original solar array of the same age. A testament to
solar technology's longevity! Of course, there are times that a 120-volt
alternating current pump running on the cabin's main battery bank
inverter is actually a better choice, like during smoky weather, or if
the solar pump has lost its priming. This powerful AC jet pump
pictured on the right, serves as a backup, which also
enables overnight watering. Pumps, of course, being large motors
pose unique electrical challenges, particularly with a solar pump's low
voltage, high amperage direct current. Simply switching this pump on and
off proved surprisingly difficult. Unlike alternating current power, which
naturally cycles 60 times a second, breaking electrical arcs, direct current creates severe arcs
when switching between contacts, especially with inductive
loads like motors. I went through a lot of IoT hardware, learning about in-rush
and flyback current. After burning through numerous relays,
and witnessing my share of angry pixies, and magic smoke, I even destroyed this 60-amp solid
state relay in spectacular fashion! The solution here: have small smart-relays actuate
much bigger dumb relays. So the solar pump now uses
a 120-amp automotive relay, while the AC pump uses a Zigbee
contactor rated well beyond its required capacity. A key takeaway:
always bench-test your ideas! Research and development is far easier
in your workshop than troubleshooting in the field. Initially this project lacked
any real telemetry or monitoring. After getting irrigation running, I quickly deployed a cheap cloud-based
baby monitor camera looking out of a window of the cabin. This camera could barely show
if sprinklers were running
due to low resolution. It also required AC/mains power. I later upgraded this solution to a better Raspberry Pi with a USB
camera that was mounted higher on the cabin and positioned with
a large basin in view. So I could see the basin filling, either indicating that sprinklers
were running or rainfall had happened. The next evolution placed a Raspberry
Pi camera in the wellhouse aimed at an analog pressure gauge, and it also had a mirror
showing the pump's piston rod. Today, more sophisticated cameras
are mounted on tall poles, providing comprehensive
views of the property. While that original wellhouse camera
has been replaced with one focused on a large analog gauge that now
graces my Grafana dashboard alongside readings from a flow
meter displaying both the flow rate and cumulative daily usage. Finding the right flow meter
required significant research. It needed to be at least an
inch in diameter and designed
to prevent ice damage. I did eventually find what I'd call a
light-industrial model for about $120. It emits a pulse via a reed
switch, per gallon of flow. And monitoring this was
perfect for an Arduino project, a tiny ESP-8266 chip,
smaller than my thumbnail, counts these pulses and reports
every 10 seconds to the MQTT server. It also hosts a tiny web
server providing JSON metrics, about flow and
its own power state. If you're a tinkerer, ESP microcontrollers
are definitely worth exploring. With irrigation in place, I turned
to another critical resource: power. Remember this orchard is off-grid, and originally it had a very
small aging battery bank, so electricity had to be rationed and it had to be monitored very closely. My weather station publishes solar
luminance data to a Raspberry Pi, which updates MQTT. And so
combined with this data, and data from the solar charger about
panel production and battery state, I created some logic to select
the best pump at any given time. I have a Python script and it
runs every 10 minutes in cron. This is basically it in pseudocode: If the solar luminance is greater
than 450 watts per square meter: use the solar pump-plenty
of sun. Otherwise, if the battery bank is
greater than 70% charged, or if the solar production is
greater than what the AC pump uses: use the AC pump. Otherwise, if
neither of those conditions are true: turn off the pumps and try again later. So using metrics in automation
is absolutely powerful. While metrics drive automation, dashboards are equally
important-especially at
a Grafana conference! Next to my cabin's, door hangs a repurposed old Amazon
fire tablet running Grafana in kiosk mode. My solar dashboard
displays color coded metrics, green wall charging, going to
yellow and red when draining. And this shows the battery state the
power flow and the draw on critical systems. Grafana has become the component
my family interacts with the most, providing an intuitive visual
representation of our property's power state from 100% in green,
to critical levels in red. Especially when we're
visiting in the winter, decisions like running the dishwasher
or using the electric kettle versus the gas stove to brew coffee in the morning,
are made much easier thanks to Grafana. Power challenges have been a recurring
theme in the system's evolution. In the early days, I traced one mysterious outage to a
mouse that had chewed through a router's power connector, causing
intermittent shorts. The solution involved acrylic tubing, making some protective sleeving, and
really sealing the cabin thoroughly. Unfortunately, my wife isn't
fond of getting a cabin cat. The aging solar system consisted
of 35-year-old panels from 1990, and another array from 2002, powering four gigantic
golf cart batteries! Then I found I could save about 15%
of battery capacity by directly using DC for all critical telemetry, networking, and irrigation loads instead
of inverting to AC then back to DC. So most consumer networking
hardware does run on 12-volt DC, so this made it easy to adapt
from the 24-volt battery bank. For IoT devices I added a 5-volt bus, although later I discovered that
powering through Raspberry Pi through USB ports provides much better and reliable
voltage regulation than through GPIO pins. And then something else I
discovered through monitoring is that when low batteries start
charging and don't have quite enough charge, you get brownouts that especially
affect things like wireless antennas. And so those were a common source
of issues, easily solved, of course, by low voltage disconnect switches. The big game changer was implementing
power-over-ethernet (PoE) to power all critical systems
such as irrigation and networking. This 48-volt standard powered
everything from cameras to directly actuating water valves. A 150 foot ethernet run to a
gate camera was extended later to power my irrigation manifold, leveraging PoE to both directly
open valves and run their IoT controllers. Though powering irrigation valves directly
with PoE does lend a certain "nerd cred", I actually don't
recommend doing this... It turns out that when
valves accumulate rust, they draw more current to open, and this again causes brownouts
affecting the controllers. So what I did then, when I was
given a friend's solar panel, I used it (which doubled as a roof)
to charge a 20-amp-hour medium-sized lithium battery, and that was
more than enough for seasonal use. So for remote access today, the options for VPNs have never been
better with choices like TailScale, Wireguard, CloudFlare tunnels. I actually use multiple VPNs hosted
on different devices. We use Starlink, which uses carrier-grade
NAT. Unfortunately, that prevents any form of
inbound connectivity. So
that does limit some options. All-in-all, the non-trivial network integrations
I've created have allowed a very reliable ability to monitor and control irrigation, to gather camera imagery, and even deploy firmware upgrades
to controllers like the flow meter. And of course, my favorite thing to
access remotely is Grafana-giving me rich realtime or historical
telemetry on one pane of glass. A future goal is building interactive
command functionality into Grafana, such that I can press panel
elements to trigger pumps and zones. So after the first summer
managing my family's orchard, I had an opportunity
to interview at a very, well-known tech company. Their Production Engineering teams are
proud of a high bar that they have for system design and networking interviews. My experience prepared me well! I landed the job and I leveled up my
career right at a pivotal time. Such was the case that the stock grants earned
from this new job provided the means to purchase the property outright
later when the estate was settled. So not only did this help
empower my young cousin's future, it unlocked the ability to invest in
upgrades beyond what I could do as a caretaker. As I've progressed in my
career in the years since, concepts of troubleshooting,
learning many trades, and gaining experience with tools like
Grafana have been very beneficial to me as an engineer. And the work I've created has led
to creating a well-loved monitoring stack at work, which uses Grafana, Alloy, and Loki to great effect. The orchard now thrives with care
provided both up close and from afar. My children enjoy Easter-egg hunts
among the trees that their great uncle planted, and the fruit keeps our
year filled with delicious snacks, preserves and pies. It's still real work, but technology has made
this much easier to balance. So to all the busy engineers
and tinkerers out there: I hope this story has been inspirational
in encouraging your hobbies and experimentation. If you're interested in more details
like code, irrigation equipment, and hardware recommendations, I have a site at ArthurK.com/orchard. And also, I'd be happy to
answer any questions that
you may have after the talk. You can also find me at the "Ask the
Experts" booth. Thank you so much.

