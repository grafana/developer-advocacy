# GrafanaCON 2026 Golden Grot Awards Ceremony: Aurora Chaser, Blue Ghost Mission 1, AI Innovations

Published on 2026-05-14T17:17:51Z

## Description

The fifth annual Golden Grot Awards at GrafanaCON 2026 — celebrating the most outstanding dashboards and AI-powered ...

URL: https://www.youtube.com/watch?v=MSrsyO-sSh4

## Summary

The show is titled "GrafanaCON 2026 Golden Grot Awards Ceremony: Aurora Chaser, Blue Ghost Mission 1, AI Innovations," published on May 14, 2026. The ceremony featured speakers including Raj, who hosted the event, and award winners Mohamed Adem, Jackson Sweeney, Oren Lion, and Dhananjay Yadav, who presented their innovative projects. The awards celebrated outstanding dashboards and AI-powered solutions, highlighting Mohamed's "Aurora Chaser" dashboard for tracking the northern lights, Jackson's observability system for Firefly Aerospace's lunar lander, Oren's use of Grafana Assistant to streamline incident management at TeleTracking, and Dhananjay's AI wearable device that prioritizes privacy while optimizing speech processing. Key takeaways included the importance of addressing specific questions with dashboards, leveraging AI for efficiency, and the significance of cost observability in tech projects.

Topics: GrafanaCON, Golden Grot Awards, Aurora Chaser, Blue Ghost Mission 1, AI Innovations, Grafana Assistant, Observability, Incident Management, Privacy in AI.

## Chapters

00:00:00 Golden Grot Awards: Aurora Chaser presentation
00:06:11 Using Business Charts in Grafana for advanced visualizations
00:11:45 Blue Ghost Mission 1 and its dashboard technology
00:17:10 Using Grafana Assistant for incident response and insights
00:23:29 Grafana Assistant for cost optimization
00:28:55 Challenges in optimizing user experience and cost in wearable devices

Hello again, and welcome to one of my favorite parts of GrafanaCON, the coveted Golden Grot Awards. These are becoming some of the most desirable awards and statues in the Observability industry—more popular and coveted than the Grammys or the Emmys. This is serious stuff. This is the fifth year that we're presenting these gold awards. No, no, they're not really solid gold, but these gold statues are designed to recognize excellence and innovation within our community.

Each year, the bar gets higher, and this year, it's clear that AI is shaping what's possible. We have four Golden Grot Award winners to present today: two dashboards and two projects. Let's start this year's awards in the personal dashboard category. 

I would like to congratulate **Mohamed Adem**, who has created something called the **Aurora Chaser**. I'm sure everyone here is familiar with the Aurora Borealis—it's spectacular if you get a chance to see it. I went to Iceland a few years ago, and I did not get to see it during the entire four days I was there. But Mohamed has a solution for us all. Please welcome **Mohamed Adem** to present **Aurora Chaser**. 

*(upbeat electronic music plays)*

*(audience applauding)*

I appreciate it. Thank you, everyone. My name's **Mohamed Adem**. I lead a software team at DRW, and I am based out of Montreal, Canada. I am this year's Golden Grot winner for the personal category. I'd like to thank everyone that voted; it's truly an honor to be doing this. 

I started working with Grafana about three years ago when I first interned at my company. I've used it a lot professionally, and this year, a lot more personally as well. This year, in particular, I wanted to build something to compete for the Golden Grot, so I built the **Aurora Chaser**. If you haven't seen it already, it is a dashboard to track the northern lights. I think the northern lights are one of the coolest natural phenomena we have, and I recommend that anyone given the chance to go out and see them. 

As **Raj** said, it's very difficult to do so. Throughout my research, I was able to find a lot of public indicators and websites around the scientific probability of the northern lights, but I wasn't able to find a composite view or indicator on whether or not these northern lights would be visible at a specific location. So that's what I decided to focus on. I aggregated a bunch of public data to create my own landing page to answer the one question: "Should I go out tonight to see the Northern Lights?"

It's probably a good idea to do a quick TL;DR on Northern Lights. I want to preface this slide by saying that I'm not a scientist; this is what I understand so far. In our solar system, we have this big giant star we call the sun, and the sun produces these charged particles we call solar wind. We find out that solar wind has its own magnetic field. We actually have data around this magnetic field from our ACE and DSCOVR satellites parked at the L1 point. We're specifically interested in the Bz component of this magnetic field, which tells us the north-south direction of the magnetic field.

As solar wind approaches Earth's magnetic field, one of two things happens. If Bz is south or negative, these particles get funneled into the poles, react with the gases in the atmosphere, and we get this cool light effect where oxygen glows green, nitrogen glows blue or purple, and we see the northern lights. If Bz is north or positive, nothing really happens; these particles get deflected, they don't enter our atmosphere, and no northern lights occur.

I live in Canada, so I was fortunate enough to catch the northern lights at some point in my life three years ago in Newfoundland, Eastern Canada. This is a picture of me and my friends at around 3:00 AM in the morning, freezing to see the northern lights. But since then, living in Quebec, I have missed a few northern lights occurrences simply because I was asleep and found out about it the next morning. I see myself using this dashboard in the future and hopefully setting up some alerts to get paged when it tells me to go outside.

In terms of the setup, it's pretty straightforward. All my data is public. I mainly use NOAA, the North Oceanic Atlantic Administration, which publishes data around the Bz component we spoke about, solar wind, and so on. I use Open-Meteo for atmospheric weather data, which includes cloud coverage, visibility, and so on. When it's cloudy, you can't really see the northern lights. I also use NASA for some sun imagery. 

I have a collection layer running Telegraf, and I essentially pull these sources and write line protocol to InfluxDB Cloud. In Grafana, I query all this data in SQL. For the sun imagery, I have a text panel rendering it using a direct URL. 

Now, let's jump into the demo, please and thank you. 

*(demo begins)*

There’s a lot going on. With the time I have, I'll try to highlight the important things. I think the most important stat panel is the one on the top left. This is my own aurora go/no-go score. I'm querying three variables: the K-index, which is the global aurora activity index; Bz, which we discussed; and cloud coverage. I come up with a score from 0 to 100 to map them into statements about whether to stay home or drop everything and go outside.

Scrolling down, this is the sun imagery from NASA that I spoke about. I believe these get updated every 15 minutes. This one here is pretty cool—the magnetogram. If you see these dark spots, those are actually solar flares, which produce the solar wind to start the reaction. 

I have some more time series data here, comparing the solar wind data from ACE and DSCOVR satellites. It's pretty consistent across the board. There are some discrepancies, but they're negligible to say the least. At the bottom, I have some live webcam panels that I found online for different cities. I actually got this idea from last year's winner, **Ruben Fernandez**. He had this in his dashboard, so thank you, Ruben. I don't know if he's here tonight.

At the bottom, I have a table for all the data sources that I used and the links to those data sources. There's one more panel I want to highlight—this one here. This might not look familiar to you as a standard panel type in Grafana. What this is, is a Business Charts panel type. If you're not familiar with Business Charts, it's a plugin developed by Volkov Labs and now maintained by Grafana, I believe. It allows you to import the Apache ECharts library and configure any of their charts here in Grafana.

If you're not familiar with Apache ECharts, it's a JavaScript open-source library that allows you to write some JavaScript and configure these charts natively into Grafana. I believe there was a talk this morning about people trying to create a Digital Twin of the Ocean. They mentioned that one of their limitations in their dashboarding was 3D or 4D graphs. There might be something here, honestly, so it's worth a look.

So, if we can jump back to the slides. Key takeaways from doing this and building dashboards in general: I always like to start with a question. I think the most meaningful dashboards answer a specific question—whether or not your server is down or should I go outside to see the northern lights. For collection, if you have public APIs, you can always point Telegraf to them, and you basically unlock free time series data. Nowadays, with AI-assisted development, you can generate Telegraf configs pretty easily. The Telegraf docs are pretty well written.

for visualizations, whenever I hit a use case where I can't use a native panel type in Grafana, I reach out to Business Charts and Apache ECharts. Essentially, you unlock 100 plus new visualizations. And that's pretty much it. If you want to access the dashboard, you can scan this QR code; it is public. If you have any questions, you can reach out to me on my LinkedIn. I will also be at the Ask the Expert booth right after this. Thank you. 

*(audience applauding)* 

- Amazing stuff. I wish I had this when I was in Iceland. I wouldn't have been disappointed. But congratulations and amazing job. Give it up again for Mohamed. 

*(audience applauding)* 

- Thank you. 

*(photographer speaks indistinctly)* 

- Thanks. 

- Grab the clicker. Cheers, thanks. All right, can we get back to the slide deck, please? 

Okay, so our next Golden Grot winner is truly from a mission-critical environment. A lot of times we say mission-critical when we're talking about something that isn't really, maybe that mission-critical, but this is literally landing something on the Moon. You don't get a do-over; you don't get to redeploy and try again three minutes later, right? The stakes are super high. 

So, Jackson Sweeney, the winner of our next Golden Grot Award, built this Observability system for Firefly Aerospace's Blue Ghost lunar lander. At the most critical moment, the actual landing, this dashboard became a primary decision support tool. It really proved that observability and visualization weren't just about monitoring systems, but actually enabling organizations to achieve an actual outcome, right? The whole world was watching this. So I'm a huge fan of aerospace, and this really gets me excited. 

Please join me in welcoming Jackson Sweeney from Firefly Aerospace. 

*(audience applauding)* 

- There you go. Cool, yeah. 

*(upbeat electronic music)* 

- I get walk-up music. *(chuckles)* Hey, everybody, my name is Jackson Sweeney. I'm with Firefly Aerospace. Today, I'm going to be talking to you all about the dashboard that enabled us to land on the Moon. At Firefly, I am a thermal engineer. 

So what I'll be talking about today is just a little bit about Firefly Aerospace, what we do, and then talking a little bit more about the Blue Ghost lunar lander. After that, I'll discuss the dashboard a little bit more and then close out with some mission imagery, showing you all some cool pictures that we got. 

About Firefly Aerospace: we have three key pillars of our business. First is launch. We develop two rockets in-house called Alpha and Eclipse. Alpha is considered a small launch vehicle, and Eclipse is considered a medium launch vehicle. Both of these rockets have the primary goal of delivering payloads, primarily satellites, into space. 

Next is land, which is my area of expertise. What we're going to be talking about today is that we developed the Blue Ghost lunar lander. It is the first commercial lunar lander to ever successfully touch down on the surface of the Moon. Lastly, we have orbit. We have a line of satellites that we call Elytra. These are satellites that can range anywhere from Earth orbit to lunar orbit and deep space for any kind of mission that it may need. 

About the Blue Ghost lunar lander: we design and build it all in-house at our facilities in Cedar Park, Texas, which is right outside of Austin. Blue Ghost Mission 1 is the only mission that we've done so far. It launched from Florida on January 15th, 2025, and successfully landed on the surface of the Moon on March 2nd, 2025, about six weeks later. 

Blue Ghost Mission 1 delivered over 100 kilograms of scientific instruments for NASA. There were some pretty cool things, like a drill that drilled into the surface of the Moon, a telescope that was looking back at Earth, and a sort of vacuum-style device that actually sucked up some lunar regolith and did some science on it, along with a few other cool things as well. 

At Firefly, we're planning for yearly missions to the Moon starting in 2027. So next, we have Blue Ghost Mission 2 coming up, and 3, 4, and hopefully some more after that. 

Here is a slide just talking a little bit more about the engineering behind Blue Ghost. I could talk about this for hours if they would let me, but I think all I'll say here is that most of everything you're seeing on the screen we design, build, and test all of that hardware in-house at our facilities in Texas. 

So the dashboard. This dashboard, like Raj mentioned, is incredibly critical to us. It was our tool that we used to verify the vehicle's health during the mission. This allowed us, while we were in the operation center, to make informed decisions about the vehicle so we weren't making risky decisions that could potentially end the mission. 

To get all of this super important data in front of us, we queried over 500 different telemetry points for this dashboard, which is thermal-focused. So what you're looking at is mostly temperatures and also data about heaters that we have on board the vehicle. We also want to know about the power system of the vehicle, such as how charged our batteries are, for example. 

I'm also curious about how the vehicle is oriented in space, so what side of the vehicle is the sun shining on, because that has a big effect on temperature. Another thing that's really important to us is being able to quickly access all of the data. So we're able to take all of these telemetry points and, using Grafana, neatly organize them on just two screens. 

Lastly, I have some pictures from our mission. Starting here in the top left, that is when we launched into space. You're looking up at the lander right now while we're still connected to the rocket. The rocket dropped us off into Earth orbit, which is the picture that you're looking at on the top right. We're looking down the side of the vehicle now, and you can see, I believe that's the Pacific Ocean of Earth that we're looking at. 

Next, we jump over into lunar orbit, where, again, you're looking at a similar camera view, looking down the side of the vehicle. Here, you're actually looking at the far side of the Moon. Lastly, this picture here on the bottom right was taken directly after we landed on the Moon, probably about 10 minutes after. You can see the shadow of the vehicle; the sun is behind us, and our shadow is projected out onto the surface of the Moon. That little dot you see there in the background is Earth. 

With that, I'll say thank you. I'm super happy and honored to be here. Much thanks to the Grafana team and the Grafana community. Thank you. 

*(audience applauding)* 

*(upbeat electronic music)* 

- Excellent. Thank you, Jackson. Really inspiring stuff. And, you know, maybe you could add this to the next mission payload, and we could get Grot on the Moon. I don't think NASA would approve, but good job. Thanks. Give it up for Jackson. 

*(upbeat electronic music)* 

*(audience applauding)* 

- Here. 

- Thanks. Appreciate it. 

- Yeah. 

All right, that was amazing stuff. So for our next two Golden Grot winners, this year's theme, of course maybe predictably, was using AI, right, to recognize the incredible ways that our community is using AI, leveraging AI in their workflows to create new capabilities. We really wanted to extend the Golden Grot Awards to pick two really compelling projects and people. 

So our first new category is pioneering AI in Observability. The next Golden Grot Award goes to Oren of TeleTracking, who's using Grafana Assistant to transform how their team triages, mitigates, and reports on incidents, cutting investigation time from days down to minutes. 

So please welcome Oren. 

*(audience applauding)* 

- Thank you. 

- Thank you, Raj. Thank you, thank you. 

- All right. Well, good afternoon, everyone. I'm thrilled to be here at GrafanaCON and...

very honored to be selected for the Golden Grot Award. When Grafana Assistant was released last year, I used it here and there. But now it's part of how we get things done every day to accelerate incidents. To fully appreciate our need for speed, here's what we aim for at TeleTracking: we work to optimize the flow of patients through the healthcare system. Think of the logistics that enable patient care. Patients are admitted, transferred, and transported. Bedside care is coordinated, patients get discharged, and bed cleaning is scheduled. We like to say our platform is like air traffic control for hospitals. The availability and performance of our platform have a direct impact on patient care.

My name is Oren Lion, and I lead logistics engineering at TeleTracking. As we move to work on our new platform, we still need to support our current platform. We're transitioning engineers, which means we have more responsibilities on fewer people. To manage this, we're looking to save time to get more done, and we're doing that through Grafana Assistant.

There are two areas that we're focused on: one is the incident response lifecycle, and the other is directional insights. I just want to back up one second. Okay, yeah, sorry about that. I think these slides got out of order. But what I was saying is that we're moving engineers to work on our new platform, and so the current engineers have more responsibilities. In order to manage this, we're using Grafana Assistant, and we all go through the incident response lifecycle.

It starts like this: for most of you, there's a change, an anomaly that's detected by Grafana, alerting the on-call engineer. They go through recovery and root cause analysis. Once that's completed, they look back into a post-incident report, but then they look forward in the mitigation phase where they work to avoid having the incident recur, thus mitigating defects.

Now, I'd like to demo the incident response lifecycle in areas where we've seen acceleration. So we'll switch to the demo. 

In this case, there was an incident, and it was picked up by Luke. He declares an incident in Grafana Incident, and he sees that alerts are firing, and he's getting pager stormed. It feels like everything's going down. In the alert, he's got a link to the dashboard. He starts investigating and sees that the alerts start to self-resolve. But, as we all know, things that self-resolve can always fall back. So let's take a look at the dashboard he was looking at.

In this dashboard, we see the anomaly. While he's investigating, we bring up Grafana Assistant in the side panel and start the assistant analysis. As that's running, I'll switch to the output of the assistant on that day. We see a couple of interesting things. First, we see that the assistant picked up that this could be a traffic spike or a broker issue—two hypotheses. As it's going through its reasoning, it's actually showing us what it found. It found that all three brokers in Kafka took a knife drop, took a hit. At this point, it's ruling out that it was a traffic spike and concluding that it was probably a cluster-wide disruption. 

Over here, it concludes that it was probably a blip in AWS, and we buy that, so we don't need to spend more time doing analysis. A couple of things to note here: the grounding is showing up right here in the Grafana Assistant report. We don't need to go outside; when you use Google Gemini, there's a source, and you can check the grounding. This is all right here in the assistant output. This is a pretty good post-incident report, and it's saving us time on that front, too.

Lastly, after an incident, there's a mitigating defect phase. We've had an incident, we've recovered it, we've gone through a post-incident report, and it's already baked into the incident. For mitigating defects, we can also use Grafana Assistant to create an alert. In this case, we had a noisy service that was bearing error messages, and we wanted to create an alert on a deviation in errors. We can easily do that in Grafana Assistant. It creates the alert, and we look over the alert. We see that it would be hard for a human to read that, so we can ask Grafana Assistant to simplify. Grafana Assistant is able to simplify as well.

Now, this wouldn't be enough for us to actually check into code because we do Alerting as Code, and we can import that into Grafana Assistant. In Grafana Assistant, to continue adding the annotations that we require in alerts, it has a link to the alert editor. In Grafana, there are many features. Sometimes you don't know if they're out there; an assistant helps you find them. So we'll let the assistant bring up the alert editor, and we can add in the annotations that we would need to check in the code. 

Over here on the left, you see the alert editor, and we can check in things like a runbook or a dashboard link. 

Switching back to the slides, as we pivot the business, we're looking for fewer people to support more with task-by-task acceleration from Grafana Assistant. But how are we managing spend? Quick trip down memory lane: two years ago at ObsCON in New York, this chart helped me see which application was eating all the money for Observability, and we used adapter metrics to optimize cost. Two years later, accelerated by Grafana Assistant, after about four hours of prompting and Grafana's cost attribution feature, we can see application spend as a percentage of total spend, target cost optimization by team, and track results over time. And it's real.

In this chart, on the right, I've got one of the prompts from Grafana Assistant, but we can see an application as a percentage of total cost. We can see things like cost drivers, and the team can take this and work to optimize cost over time. Now, everybody wants to know how to prioritize. Since we have the over/under budget panel over here, and since we are over budget, this becomes a higher priority. 

I can honestly say that Grafana Assistant is helping us spend less time and get more done across any role, individual contributors as well as managers. Thank you. 

(audience applauding)

Great. 

- All right, amazing. Thank you, Oren. I'm really glad to see that you were able to improve efficiency, and thanks for your support over the last few years. 

- Thank you, sir. Thank you, sir. 

- So enjoy your Golden Grot. Good luck getting that through airport security. 

- I'll try, thank you. 

- (chuckles) All right. 

- Bye. 

(audience applauding)

Okay, we've got one more around the AI innovation category. I just met this winner backstage for the first time about 20 or 30 minutes ago, and he was wearing a really cool device around his neck. This is a privacy-focused AI assistant that records all the audio that's happening while you're going about your day. I think this example really exemplifies that by using Grafana Cloud and Grafana Assistant Investigations, there's a really cool way to optimize complex speech-to-text and LLM pipelines, ensuring performance, quality, and cost stay on track as AI systems scale. It's kind of cool. It's an example of AI on the edge, I suppose. 

So please join me in welcoming Dhananjay Yadav to the stage, the winner of our next Golden Grot. Thank you. 

(audience applauding) 

(mid-tempo electronic music) 

- Thank you. Hello, everyone. Super excited to meet you. I'm Dhananjay Yadav. I'm the CEO and co-founder of NeoSapien. What you are seeing over here is the world's first AI wearable, which understands all my conversations and creates an individualized knowledge graph to build a deep context. Now, how this is done is through this. So what is NeoSapien? We are Neo 1. Our AI wearable device sits with you seamlessly to understand all your daily conversations, be it telephonic, online, or...

Offline. And then on top of it, there is conversational intelligence, which, at a single point in time, has four different AI services being performed for your diarization, transcription, and summarization. The pipeline we have created is patented as well. 

We wanted to always be privacy-first because, for me, the hardware devices and cell phones we are using are never privacy-first. I wanted to build a privacy-first device. So how do you do it? You basically make sure that your audio lives in memory and then gets destroyed. There is no way of going back to it; just the raw transcript and the traces are the only things that could be figured out. So it's like forensics, isn't it? This is where our pipeline comes into the picture. 

Every conversation gets ingested into your cloud via Kafka. Then we go through speech-to-text and LLM processing. Again, this is done by four different AI processes. Our orchestration layer takes place every time, and this then sits on our personalized knowledge graph algorithm, which we have created ourselves, wherein now every entity and every relationship gets differentiated based on facts, figures, and entities. 

So, what are the challenges? Because audio can never be stored—only the traces and logs—the constraint gave rise to figuring out how to get it more optimized and understand what is breaking and what is not. For us, three big pillars were identified: 

1. **Latency**: For example, today I'm having this conversation, and at that point in time, for any user, the conversation time needs to be standardized. If you are getting it within 13 seconds, it needs to be 13 seconds. If even for one percentage of the memory it hits two to three minutes, the user experience falls off. 

2. **Discard Rate**: As humans, we talk a lot. We want to understand which conversations need to be stored versus which do not. For example, if you are making noises or talking to a third person, those shouldn't come to our model to optimize it. 

3. **Cost**: In our wearable device, which works 24/7 with you, optimizing the cost is critical. The entire pipeline needs to ensure that the cost is standardized at every point in time. If there is a variance, there should always be an alert to tell us that we need to figure it out. 

How do we do it? I will take you through it one by one. First is on the discard ratio. We log shape and not the content. On the left-hand side, you can see the conversations and their duration. On the right-hand side, you see the discard rate. When we say our median is around 11.5%, that is the most optimized scenario. But when it reaches about 60-70%, we need to understand why that happened. If we cannot understand it, that memory might never come back to the customer. 

The second part is pricing. Because there are four different AI services working at a single point in time, we want to ensure that every part of our orchestration layer is standardized. If there is any leakage, we need to understand it quickly; otherwise, it can result in continuous leakage. 

The last part, and one of the most important, is latency. For any user experience, it needs to be standardized. Users need to get memory within 30 seconds. If it crosses two minutes for one memory, that is a massive alert, and user experience can dive down significantly. 

That's when we started using Grafana Assistant Investigations, which really helped us out. We are a small team with only four engineers. With them, we were able to run the complete assistant program on our entire pipeline to understand the key bottlenecks across the system. 

What we found was very interesting. One of the examples we encountered was an issue with our BLE advertising failures. We realized that there were certain issues with our BLE that were impacting the complete user experience. We were able to figure it out, fix it, and validate it directly in our codebase. 

What I believe is that any partnership where you learn about what is happening is not good enough; it's about how they can help you fix it. That's what Grafana has done for us. For such a small team, we have been able to scale significantly, so much so that we are among the highest-selling wearables in India and are now launching globally. 

What did this make us learn? Three important things: 

1. When there are intense constraints, like in our case where no audio could be stored, it actually gave us more clarity on what needs to be done and how to log it better. 

2. Cost observability: One of the biggest models is that per-user cost needs to be very optimized, and that is what Grafana helped with. 

3. Privacy is not equal to blindness. Even if we cannot store audio, we can still understand significantly through duration, discard rates, and latency. 

This is what we have built, and I am super excited to share our learning with you all. Thanks a lot, and feel free to reach out to me. 

*(audience applauding)* 

- Thanks, Dhananjay. Great stuff. Careful, this one's really heavy. No, just kidding. (Raj chuckles) Great job, and all the best in scaling up your hardware products. 

- Thank you. 

- It's always cool to see new players in the space. Congratulations on the Golden Grot. 

- Thank you. 

- All right, and that's it for the Golden Grot. Hope you enjoyed it. *(audience applauding)*

## Raw YouTube Transcript

- Hello again, and welcome to one of my favorite parts of GrafanaCON, the coveted Golden Grot Awards. These are becoming some of
the most desirable awards and statues in the Observability industry. More popular and coveted than
the Grammys, than the Emmys. This is serious stuff. And this is the fifth year that we're presenting
these solid gold award. No, no, they're not really solid gold, but these gold statues that are designed to recognize excellence and
innovation around our community. So let me grab the clicker
since I didn't do that yet. And each year, the bar gets higher. And this year, it's clear that AI is shaping what's possible. So we've got four Golden
Grot Award winners to present today, two
dashboards and two projects. And so let's start this year's award in the personal dashboard category. So I'd like to congratulate Mohamed Adem, who has created something
called the Aurora Chaser. So I'm sure everyone here is familiar with the Aurora Borealis. Spectacular if you get a chance to see it. I went to Iceland a few years ago, and I did not get to see it in the entire four days I was there. But Mohamed has a solution for us all. Please welcome Mohamed Adem
to present Aurora Chaser. (upbeat electronic music)
(audience applauding) - Appreciate it. Thank you. Thank you, everyone. My name's Mohamed Adem. I lead a software team at DRW. I am based out of Montreal, Canada, and I am this year's Golden Grot winner for the personal category. I'd like to thank everyone that voted. It's truly an honor to be doing this. So I started working with
Grafana about three years ago, when I first interned at my company. I've used it a lot professionally, and this year a lot
more personally as well. This year in specific, I
wanted to build something to compete for the Golden Grot, so I built the Aurora Chaser. And if you haven't seen it already, it is a dashboard to
track the northern lights. I think the northern lights are one of the coolest
natural phenomenons we have, and I recommend anybody if given the chance to go out to see them. But as Raj said, it's
very difficult to do so. And throughout my research, I was able to find a lot of
public indicators and websites around the scientific probability
of the northern lights, but I wasn't able to find a
composite view or indicator on whether or not these northern lights would be visible at X location. So that's what I decided to focus on. I decided to aggregate
a bunch of public data to come up with my own landing page to answer the one question, "Should I go out tonight to
see the Northern Lights?" It's probably a good idea to do a quick TL;DR on Northern Lights. I wanna preface this slide by saying that I'm not a scientist. This is what I understand so far. So yeah, in our solar system, we have this big giant
star we call the sun, and the sun produces
these charged particles we call solar wind. And we come to find out that solar wind has its own magnetic field. And we actually have data
around this magnetic field from our ACE and DSCOVR
satellites parked at the L1 point. And we're specifically
interested in the Bz component of this magnetic field. It basically tells us the north-south direction
of the magnetic field. And what happens is, as solar wind approaches
Earth's magnetic field, one of two things happen. If Bz is south or negative, then these particles get
funneled into the poles, react to the gases in the atmosphere, and we get this cool light effect where oxygen would glow green, nitrogen would glow blue or purple, and we get the northern lights. If Bz is north or positive,
well, nothing really happens. These particles get deflected, they don't under our atmosphere,
and no northern lights. I live in Canada, so I was
actually fortunate enough to catch the northern lights at some point in my life three years ago in Newfoundland, Eastern Canada. This is a picture of me and my friends at like 3:00 AM in the morning, freezing to see the northern lights. But since then, living in Quebec, I have missed a few
Northern Lights occurrences simply because I was asleep and I found out about it the next morning. So I do see myself using
this dashboard in the future and hopefully setting up some alerts, to get paged when it's
telling me to go outside. In terms of the setup, it's
pretty straightforward. All my data is public. I mainly use NOAA or the North Oceanic
Atlantic Administration. They publish data around the
Bz component we spoke about, solar, wind, and so on. I use Open-Meteo for
atmospheric weather data. So this is the cloud coverage,
visibility, and so on. So when it's cloudy, you can't really see the northern lights. And I use NASA for some sun imagery. I have a collection
layer, running Telegraf, and I essentially pull these sources and write line protocol to InfluxDB cloud. And then in Grafana, I
query all this data in SQL. And then for the sun
imagery, I have a text panel essentially rendering
it using a direct URL. So we can jump into the
demo, please and thank you. There it is. So there's a lot going on. With the time I have, I'll try to highlight
the important things. I think the most important stat panel is this one on the top left. And essentially this is my
own aurora go/no-go score. And essentially what I'm doing is, here, I'm querying the three variables, the K-index, which is the
global aurora activity index; Bz, which is what we spoke
about; and cloud coverage. And essentially coming up
with a score from 0 to 100 to essentially then map
them into statements, whether to stay home or drop
everything and go outside. Oops. And scrolling down,
this is the sun imagery from NASA that I spoke about. I believe these get
updated every 15 minutes. This one here is pretty
cool, the magnetogram. If you see these dark spots here, these are actually solar flares. It's what produces the solar
wind to start the reaction. Scrolling down, I have some
more time series stuff. Here, I'm comparing the solar wind data from ACE and DSCOVR satellites. It's pretty consistent across the board. There's some discrepancies, but it's negligible to say the least. And all the way at the bottom, I have some live webcam panels that I found online for different cities. I actually got this idea from last year's winner, Ruben Fernandez. He had this in his dashboard. So thank you, Ruben. I don't
know if he's here tonight. And all the way at the bottom, I have a table for all the
data sources that I used and the links to those data sources. There's one more panel I wanna highlight, probably this one here. This might not look familiar to you as a standard panel type in Grafana. What this is, is it's a
Business Charts panel type. And if you're not familiar
with Business Charts, it's a plugin developed by Volkov Labs, and now maintained by Grafana, I believe, and essentially allows you to import the Apache ECharts library and then configure any of
their charts here in Grafana. If you're not familiar
with Apache ECharts, it's essentially this
JavaScript open source library that allows you to, and what Business Charts
allows you to do essentially is write some JavaScript, configure these charts
natively into Grafana. I believe there's a talk this morning, the people that were trying to do a Digital Twin of the Ocean, they said one of their
limitations in their dashboarding was 3D or 4D graphs. There might be something here, honestly, so it's worth a look. So if we can jump back to the slides. Yeah, so key takeaways from doing this and building dashboards in general. I always like to start with a question. I think the most meaningful dashboards answer a specific question, so whether or not your server is down or should I go outside to
see the northern lights; for collection, I think
if you have public APIs, you can always point Telegraf to them and then you basically
unlock free time series data. Nowadays, with AI-assisted development, you can generate Telegraf
configs pretty easily. The Telegraf docs are pretty well written. And then for visualizations, whenever I hit a use case where I can't use a native
panel type in Grafana, I reach out to Business
Charts and Apache ECharts, and essentially you unlock
100 plus new visualizations. And that's pretty much it. If you wanna access the dashboard, you can scan this QR code, it is public. If you have any questions, you can reach me out on my LinkedIn. I will also be at the Ask the
Expert booth right after this, and thank you. Oops.
(audience applauding) - Amazing stuff. I wish I had this when I was in Iceland. I wouldn't have been disappointed. But congratulations and amazing job. Give it up again for Mohamed.
- Thank you. (audience applauding) (photographer speaks indistinctly) Thanks.
- Grab the clicker. Cheers, thanks. All right, can we get back
to the slide deck, please? Okay, so our next Golden Grot winner is truly from a mission
critical environment. A lot of times we say mission critical when we're talking about something that isn't really, maybe
that mission critical, but this is literally
landing something on the Moon that you don't get a do-over, you don't get to, you know, redeploy and try again three minutes later, right? The stakes are super high. So Jackson Sweeney, the winner of our next Golden Grot Award, built this Observability system for Firefly Aerospace's
Blue Ghost lunar lander. And at the most critical
moment, the actual landing, this dashboard became a
primary decision support tool. And it really proved that
observability and visualization, you know, wasn't just
about monitoring systems, but actually enabling
organizations to achieve like a actual outcome, right, and the whole world was watching this. So I'm a huge fan of aerospace, and this really gets me excited. So please join me in
welcoming Jackson Sweeney from Firefly Aerospace. (audience applauding) There you go. Cool, yeah. (upbeat electronic music) - I get walk-up music. (chuckles) Hey, everybody, my name
is Jackson Sweeney. I'm with Firefly Aerospace. And today, I'm going to
be talking to you all about the dashboard that
enabled us to land on the Moon. At Firefly, I am a thermal engineer. So what I'll be talking about today, just a little bit about Firefly
Aerospace, what do we do, and then talking a little bit more about the Blue Ghost lunar lander, and then I'll talk about the
dashboard a little bit more, and then close out with
some mission imagery, show you all some cool
pictures that we got. So about Firefly Aerospace. We have three key pillars of our business. First being launch. We develop two rockets in-house called Alpha and Eclipse. Alpha is considered a
small launch vehicle, and Eclipse is considered
a medium launch vehicle. Both of these rockets, their primary goal is to deliver payloads,
primarily satellites, into space. Next, land, which is my area of expertise. And what we're gonna be talking
a little bit about today, we developed the Blue Ghost lunar lander. It is the first commercial lunar lander to ever successfully touch down
on the surface of the Moon. Lastly, we have orbit. We have a line of satellites
that we call Elytra. These are satellites that can range anywhere from Earth orbit to
lunar orbit and deep space for any kind of mission that it may need. So about the Blue Ghost lunar lander. We design and build it all in-house at our facilities in Cedar Park, Texas, which is right outside of Austin. Blue Ghost Mission 1 is the only mission
that we've done so far. It launched from Florida
on January 15th, 2025, and successfully landed on the surface of the
Moon on March 2nd, 2025, about six weeks later. Blue Ghost Mission 1
delivered over 100 kilograms of scientific instruments for NASA. There were some pretty cool things. There was like a drill that drilled into the surface of the Moon. There was a telescope that
was looking back at Earth. We had a sort of vacuum-style device that actually sucked
up some lunar regolith and did some science on it, and a few other cool things as well. At Firefly, we're planning for
yearly missions to the Moon starting in 2027. So next, we have Blue
Ghost Mission 2 coming up, and 3, 4, and hopefully
some more after that. Here is a slide just
talking a little bit more about the engineering behind Blue Ghost. I could talk about this for
hours if they would let me, but I think all I'll say here is that most of everything that
you're seeing on the screen we design and build and
test all of that hardware in-house at our facilities in Texas. So the dashboard. This dashboard, like Raj mentioned, is incredibly critical to us. It was our tool that we used to verify the vehicle's
health during the mission. So this allowed us, while we
were in the operation center, to make informed decisions
about the vehicle so we're not making risky decisions that could potentially end the mission. So in order to get all of this super important data in front of us, we, for this dashboard,
which is thermal-focused, so what you're kinda looking
at is mostly temperatures and also data about heaters that we have on board of the vehicle. Queried over 500 different
telemetry points. So like I mentioned,
temperatures, heater info. Also wanna know about the
power system of the vehicle, so how charged are our
batteries, for example. And I'm also curious about how the vehicle is oriented in space, so what side of the vehicle
is the sun shining on because that has a big
effect on temperature. And another thing that's
really important to us is being able to quickly
access all of the data. So we're able to take all
of these telemetry points. In using Grafana, we neatly organize them on just two screens. Lastly, I have some
pictures from our mission, starting here in the top left, that is when we launched into space. So you're kinda looking up
at the lander right now. This is while we're still
connected to the rocket. The rocket dropped us
off into earth orbit, which is the picture
that you're looking at on the top right. We're kinda looking down
the side of the vehicle now. And then you could see, I believe that's the
Pacific Ocean of Earth that we're looking at. Next, we jump over into lunar orbit where, again, you're looking
at a kinda similar camera view where we're looking down
the side of the vehicle. And here, you're actually looking at the far side of the Moon. And lastly, this picture
here on the bottom right, this is directly after
we landed on the Moon, probably taken maybe 10 minutes after. And you can see the shadow of the vehicle. So the sun is behind us
and our shadow is projected out onto the surface of the Moon. And that little dot that you see there in the background, that is Earth. And so with that, I'll say thank you. Super happy and honored to be here. Much thanks to the Grafana
team and the Grafana community. Thank you. (audience applauding) (upbeat electronic music) - Excellent. Thank you, Jackson. Really inspiring stuff. And, you know, maybe you could add this to the next mission payload and we could get Grot on the Moon. I don't think NASA would
approve, but good job. Thanks. Give it up for Jackson. (upbeat electronic music)
(audience applauding) - Here.
- Thanks. Appreciate it.
- Yeah. - All right, that was amazing stuff. So for our next two Golden Grot winners, this year's theme, of
course maybe predictably, was using AI, right, to
recognize the incredible ways that our community is using AI, leveraging AI in their workflows
to create new capabilities. And we really wanted to
extend the Golden Grot Awards to pick two really compelling
projects and people. So our first new category is pioneering AI in Observability. And the next Golden Grot Award goes to Oren of TeleTracking, who's using Grafana Assistant to transform how their
team triages, mitigates, and reports on incidents, cutting investigation time
from days down to minutes. So please welcome Oren. (audience applauding) Thank you.
- Thank you, Raj. Thank you, thank you. All right. Well, good afternoon, everyone. I'm thrilled to be here at GrafanaCON and very honored to be selected
for the Golden Grot Award. When Grafana Assistant
was released last year, I used it here and there. But now it's part of how we
get things done every day to get acceleration on incidents. And to fully appreciate
our need for speed, here's what we aim for at TeleTracking. We work to optimize the flow of patients through the healthcare system. So think of the logistics
to enable patient care. Patients are admitted,
transferred, and transported. Bedside care is coordinated,
patients get discharged, and bed cleaning is scheduled. We like to say our platform is like air traffic control for hospitals. The availability and
performance of our platform has an impact on patient care. My name is Oren Lion, and I lead logistics
engineering at TeleTracking. So as we move to work on our new platform, we still need to support
our current platform. We're transitioning engineers, and so we have more
responsibilities on fewer people. And to do that, we're looking
to save time to get more done, and we're doing that
through Grafana Assistant. There are two areas that we're focused on. One is the incident response lifecycle and the other is directional insights. I just wanna back up one second. Okay. Yeah, sorry about that. I think these slides got out of order. Yeah, but so what I was saying is that we're moving engineers
to work on our new platform and so the current engineers
have more responsibilities. And in order to do that,
we're using Grafana Assistant, and we all go through the
incident response lifecycle. And it starts like this. For most of you, there's a change, there's an anomaly that's
detected by Grafana, alerting, the on-call is paged, they go through recovery
and root cause analysis. Once that's completed, they look back into a
post-incident report, incident reporting, but
then they look forward in the mitigation phase
where they work to avoid having the incident recur. So mitigating defects. And now I'd like to demo the
incident response lifecycle in areas where we've seen acceleration. So we'll switch to the demo. All right, so in this
case there was an incident and it was picked up by Luke. He declares an incident
in Grafana Incident, and he sees that alerts are firing, and he's getting pager stormed. It feels like everything's going down. In the alert, he's got
a link to the dashboard. And so he starts investigating and sees that the alerts
start to self-resolve. But, as we all know,
things that self-resolve can always fall back. So let's take a look at the
dashboard he was looking at. In this dashboard, we see the anomaly. And while he's investigating, we bring up Grafana Assistant
here in the side panel and we start the assistant analysis. So, as that's running, I'll switch to the output of
the assistant on that day. And we see a couple interesting things. First, we see that assistant picked up that this could be a traffic
spike or a broker issue. So two hypotheses. And we come down here, and as it's going through its reasoning, it's actually showing us what it found. And it found that all
three brokers in Kafka took a knife drop, took a hit. So at this point, it's ruling out that
it was a traffic spike and that it was probably
a cluster-wide disruption. Over here, it concludes that
it was probably a blip in AWS, and we buy that so we don't need to spend more time doing analysis. Now, a couple things to note here is that the grounding
is showing up right here in the Grafana Assistant report. We don't need to go outside, like, when you use Google Gemini, there's a source and you
can check the grounding. This is all right here
in the assistant output. This is a pretty good post-incident report and it's saving us time
on that front, too. So lastly, after an incident, there's a mitigating defect phase, right? So we've had an incident,
we've recovered it, we've gone through a post-incident report, it's already baked into the incident. And for mitigating defects, we can also use Grafana
Assistant to create an alert. So in this case, we had a noisy service. It was bearing error messages, and so we wanted to create an alert on a deviation in errors. We can easily do that
in Grafana Assistant. It creates the alert, We look over the alert, and we see that it would be kinda hard for a human to read that, so we can ask Grafana
Assistant to simplify. And Grafana Assistant is
able to simplify as well. Now, this wouldn't be enough for us to actually check into code
'cause we do Alerting as Code, and we can import that
into Grafana Assistant. So in Grafana Assistant, to
continue adding the annotations that we require in alerts, it has a link to the alert editor. And in Grafana, there are many features. Sometimes you don't know
if they're out there, an assistant helps you find them. So we'll let assistant
bring up the alert editor, and we could add in the annotations that we would need to check in the code. So over here on the left,
you see the alert editor, and we can check in things like a runbook or a dashboard link. All right, and switching
back to the slides. So as we pivot the business,
we're looking for fewer people to support more with
task-by-task acceleration from Grafana Assistant. But how are we managing spend? Quick trip down memory lane. Two years ago to ObsCON in New York, this chart helped me see which application was eating all the
money for Observability, and we used adapter
metrics to optimize cost. Two years later, accelerated
by Grafana Assistant after about four hours of prompting and Grafana's cost attribution feature, we can see application spend
as a percentage of total spend, target costs optimization by team, and track results over time. And it's real. So we can do a demo on this, too. Right, so in this chart, on the right, I've got one of the prompts
from Grafana Assistant, but we can see an application
as a percentage of total cost. We can see things like cost drivers, and the team can take this and work to optimize cost over time. Now, everybody wants to
know how to prioritize. And since we have the over/under
budget panel over here, since we are over budget, this
becomes a higher priority. So I can honestly say
that Grafana Assistant is helping us spend less time and get more done across any role, individual contributors
as well as managers. Thank you. (audience applauding) Great. - All right, amazing. Thank you, Oren. I'm really glad to see that you were able to improve efficiency, and thanks for your
support the last few years. - Thank you, sir. Thank you, sir. - So enjoy your Golden Grot. Good luck getting that
through airport security. - I'll try, thank you. - (chuckles) All right. - Bye. Over here. (audience applauding) - Okay, we've got one more around the AI innovation category. So I just met this winner
backstage for the first time about 20 or 30 minutes ago, and he was wearing a really
cool device around his neck. And this is a privacy-focused AI assistant that records all the
audio that's happening while you're going about your day. And I think this example
really exemplifies that by using Grafana Cloud and Grafana Assistant Investigations, there's a really cool
way to kind of optimize complex speech-to-text and LLM pipelines, ensuring performance, quality,
and cost stay on track as AI systems scale. It's kinda cool. It's an example of AI
on the edge, I suppose. So please join me in welcoming Dhananjay Yadav to the stage, the winner of our next
Golden Grot, thanks. (audience applauding) (mid-tempo electronic music) - Thank you. Hello, everyone. Super
excited to meet you. I'm Dhananjay Yadav. I'm the CEO and co-founder of NeoSapien. What you are seeing over here is the world's first AI wearable, which understands all my conversations, creates individualized knowledge graph to build a deep context. Now, how this is done is through this. So what is NeoSapien? We are Neo 1. Our AI wearable device
sits with you seamlessly to understand all your daily conversation, be it telephonic, online or offline. And then on top of it, there is conversational intelligence, which, at a single point of time, we have four different AI services which are being performed
for your diarization, transcription, and summarization. The pipeline, which we have
created, is patented as well. And on top of this, we wanted to always be
privacy-first variable because, for me, the hardware devices, the cell phones which we are
using, are never privacy-first. I wanted to build a privacy-first device. So how do you do it? You basically make sure that
your audio lives in the memory and then gets destroyed. And then there is no
way of going back to it, just the raw transcript and
the traces are the only thing which could be figured out. So it's like forensics, isn't it? This is where our pipeline
comes into picture. So to device, every conversation gets ingested into your cloud via Kafka. And then we go through
speech-to-text and LLM processing. Again, this is done by four
different AI processes. Our orchestration layer, which
is taking place every time. And this then sits on our personalized
knowledge graph algorithm, which we have created ourself, wherein now every entity,
every relationship gets differentiated on the basis of facts, figures, and entities. So now, what are the challenges? So because audio couldn't ever be stored, only the traces and logs, the constraint gave us rise to figure out how to get it more optimized and understand what is
breaking, what is not. And that's where, for us,
three big pillars were. One is latency. So, for example, today I'm
having this conversation, and at that point of time, for any user, a conversation time needs
to be always standardized. For example, for any conversation, if you are getting it within 13 seconds, it needs to be 13 seconds. And if even for one
percentage of the memory, if it hits two to three minutes, the user ability or
the user actually gets, doesn't get proper
understanding of the product or, just for him, the user experience of
the products falls off. Second thing is we as
humans talk a lot, right? So for us, discard rate is very critical because we want to understand what are those conversations
which need to be stored versus what are those conversations which don't need to be stored. Things like if you are
talking anything, right? You are making some noises, you're talking to third person, things which are not meaningful, those shouldn't ever come to our model to optimize it, right? So for us, discard rate is very critical. Second thing is cost. In our wearable device, which is basically working 24/7 with you, the most critical layer
is optimizing the cost, and that's where our (indistinct). So all the pipeline which works together needs to make sure that the
cost is always standardized at every point of time. And if there is a variance, then there should always
be an alert to tell us that there is a variance and
we need to figure it out. So how do we do it? I will take you one by one. First is on the discard ratio, right? So what you can see is we log
shape and not the content. So, for example, you can
see on the left-hand side the conversations, the
duration of conversations. And on the right-hand side, what you see is basically
the discard rate. When we say our median is around 11.5%, that is the most optimized scenario. But when it reaches to about 60, 70%, we need to understand why did it happen. Because if at that point of time we are not able to understand, then that memory might
never come to customer, that conversation might never
come back to the customer. Second part is the pricing. Like I had mentioned, because there are four
different AI services working at a single point of time, we want to make sure that every part of our orchestration
layer, which it follows, should be standardized. If there is any leakage, we
need to understand quickly otherwise it's a leakage,
which, in our case, can result into a continuous leakage. The last part, and one of
the most important part, is the latency. So for us, for any user experience, it needs to be standardized. They need to get memory within 30 seconds. Even for one memory, if
it crosses two minutes, that is a massive alert. And that's where a user experience can actually dive down significantly, and that is something which
we need to guard against. And that's when we started using Grafana Assistant Investigations, which really, really helped us out. We are a small team. We
had only four engineers. And with them, we were able to run the complete assistant program
on our complete pipeline to understand what are some
of those key bottlenecks across the complete system. And what we got was
something very interesting. So when we ran, one of
the examples which we got was an issue with our
BLE advertising failures. So here, we realized that
there were certain issues with our BLE, which was actually impacting the complete user experience. And that's where we were able
to figure it out, fix it, and validate it directly in our code base. What I believe is that any partnership where you get learning about what is happening
is not good enough, but it's about how they
can help you in fixing it. And that's what Grafana has done for us. And for such a small team, we have been able to scale significantly, so much so that we are among the highest-selling wearables in India and now launching soon globally. And yeah, what did this make us learn? Three important things. When there are intense constraint, like in our case there was no
audio which could be stored, it actually gave us more clarity to understand what needs to be done, how do we need to log it better. Second is cost observability. For us, one of the biggest
mod was per user cost needs to be very optimized, and
that is what Grafana helped. And third is privacy is
not equal to blindness. If you think that even if we
cannot actually store audio, but we can still understand significantly through duration, discard
rates, and latency. And this is what we have
built and, yeah, super excited to share our learning with you guys. Thanks a lot and feel
free to reach out to me. (audience applauding) - Thanks, Dhananjay. Great stuff. Careful, this one's really heavy. No, just kidding. (Raj chuckles) Great job and all the best in scaling up your hardware products. - Thank you. - It's always cool to see
new players in the space. Congratulations-
- Thank you. - on the Golden Grot.
- Thank you. - All right, and that's
it for the Golden Grot. Hope you enjoyed it. (audience applauding)

