# Grafana in the Ocean: A Digital Twin Powered by Grafana for Marine Conservation Research at DIGI4ECO

Published on 2026-05-14T17:19:02Z

## Description

What does it take to build a real-time digital twin of the ocean — and can Grafana serve as its front end? At GrafanaCON 2026 ...

URL: https://www.youtube.com/watch?v=2cjpzJKN3kI

## Summary

The show is titled "Grafana in the Ocean: A Digital Twin Powered by Grafana for Marine Conservation Research at DIGI4ECO," published on May 14, 2026. Speakers Jacopo Aguzzi from the Marine Science Institute of Barcelona and Enoc Martinez from UPC, Technical University of Catalonia, discussed the DIGI4ECO project, which aims to create a real-time digital twin of the ocean for ecological monitoring. They highlighted the use of robotic platforms for data collection, the integration of AI for data processing, and the role of Grafana in visualizing complex datasets. Key takeaways include the importance of monitoring marine ecosystems, the innovative use of technology in data collection, and the potential for AI to enhance ecological research and management.

Topics: Digital Twin, Marine Conservation, Ecological Monitoring, AI in Marine Science, Grafana Visualization

## Chapters

00:00:00 The need for ecological monitoring in marine environments
00:06:31 Building a digital twin of the ocean for marine conservation
00:12:05 Building a digital twin of the ocean for marine conservation
00:18:30 Monitoring underwater sensors with Grafana

Thank you very much. Good morning, everyone. I'm Jacopo Aguzzi from the Marine Science Institute of Barcelona, one of the five Marine Institutes in Spain belonging to the Spanish National Research Council, which is the largest academic institution in Spain. 

Let me introduce myself properly. My background is in marine ecology, and I work in fishery management. For more than two decades, I have specialized in technological development for solutions to monitor the marine environment, from coastal areas to the deep sea.

**Enoc:** Hi, everyone. My name is Enoc Martinez. I work at UPC, the Technical University of Catalonia. My background is in electronic engineering, although I have spent the last 10 years focusing on scientific data management in scientific data infrastructure, specifically related to the ocean. Here you can see me on a boat, but I actually spend 99% of my time behind a desk.

Let's start with the context of DIGI4ECO, which is focused on ecological monitoring. Why do we need ecological monitoring today? As you all know, we have a problem in the sea, similar to terrestrial environments. There is an increasing amount of anthropic activity that damages different ecosystems, and there is a growing interest in monitoring them. 

I have chosen two iconic figures to illustrate this. The first refers to industrial extractive activities, such as trawl hauling, which occur almost along all continental margins of the planet and sweep entire ecosystems on a daily basis. The second is the omnipresent effect of plastic pollution. These are just two of many impacts we face, which is why we need to monitor the environment. 

Policy environmental management agencies, including the European communities, are interested in developing metrics to assess the Good Environmental Status (GES) of marine ecosystems within the biodiversity agenda of the European community. GES is part of the Marine Strategy Framework Directive, which aims to measure the status and health of ecosystems through 11 descriptors or ecological indicators. These descriptors include seabed status, biological diversity, the presence of contaminants in seafood, and the status of commercially exploited marine species. 

However, these descriptors are semantically open, requiring thoughtful dialogue between scientists and policymakers on what type of data we need to compute them. Environmental biological data, special temporal scales, and ultimately, the discussion always leads to technologies. 

Why technologies? Because monitoring the ocean is expensive. Most of what we know about the sea has been collected by vessels over the past 200 years. Vessels are costly technologies. For example, we have a star vessel in the Spanish fleet named Sarmiento de Gamboa. This vessel is about 70 meters long, which is average in size, and it costs up to 25,000 euros per day. This means that collecting data is expensive, and we need a strong budget to support it. Additionally, there are many more people wanting to use the vessels than there are vessels available, leading to scheduling issues.

That's why DIGI4ECO aims to drive ecological monitoring toward the use of robotic networks. We are developing autonomous platforms that bring scientists from the decks of vessels back to their offices on shore. Sorry, Enoc, you will be more in the office.

We use three major types of robotic platforms in DIGI4ECO. The first are cabled observatories, which tether the platform through telephone or internet cables to shore. They stream data continuously in real-time and receive power to operate over consecutive years. The second type is Landers, which are standalone versions of cabled observatories. They have no cables and can be strategically redeployed, but they have much shorter autonomy due to their battery packs, generally lasting up to one year.

These two platforms have limited data collection capabilities because they are fixed. The environment is more heterogeneous than a single pixel of space where these platforms are placed. Therefore, we are working with robotic solutions to automatically sweep the environment around these platforms at a hectare scale. I'm referring to data-collecting crawlers, which are trackable vehicles that I will describe in a few slides.

Why is this important? Because the European community is trying to change the paradigm of research. One of the lines of this change is the creation of a digital twin of the ocean. A digital twin of the ocean is the creation of virtual replicas of ecosystems. The more data we have, the better the replica is. 

What type of data? We stream data from our platforms that are equipped with multi-parametric sensor assets. We have three major types of data that we stream into the digital twin: biological data, which involves AI to process images; acoustic data, where we listen to the seascape for biological sounds, which Enoc will describe in more detail later; and geochemical data provided by sensors that characterize dissolved oxygen, methane, CO2, nitrates, phosphates from agriculture, pH, turbidity, and other factors, along with classical stenographic sensors that characterize water masses in terms of salinity, temperature, and current speed and direction.

With this data, we aim to create not only virtual replicas of the environments but also real-time updated replicas. Why? Because we want to know the present status to run "what if" scenarios using artificial intelligence. The IPCC, the International Panel for Climate Change, informs us about the expected status of the sea over the next 50 years concerning temperature, salinity, and other factors. 

We want to model the biological response of living components in the ecosystem. For example, in relation to increasing temperature and salinity, we want to know how the presence of species will change—whether they will migrate, go extinct, or reduce their populations.

All this information needs to be synthetically collected into a web framework where citizens and policymakers can log on and access meaningful ecological outputs that they can understand and use. This is where web visualization comes into play.

In this respect, DIGI4ECO has the following aims: We want to virtually recreate digital replicas of four coastal ecosystems—two in the Atlantic and two in the Mediterranean, at a depth of 20 meters. Why coastal ecosystems? Because humanity has developed along the coast. Coastal areas are the first line of impact from human activity. 

We have master platforms in this robotic network establishment for these environments, which include two cabled observatories—one in Galway Bay, Ireland, and the other near Barcelona, which I will describe in more detail later. We also have crawlers operating in Kristineberg, above Gothenburg in Sweden, and then we will...

have been developed to identify different species of fish in the underwater video footage we collect. This is crucial for understanding the biodiversity in the areas we monitor.

In the Eastern Mediterranean Sea, off the Italian coast in Ancona, we will build a standardized digital twin for four different environments. The heart of this digital twin will be an online data bank that will remotely store all the data, pre-process it for homogenization and standardization, and embed AI routines for flagging data quality, eliminating outliers, and using different models to fill in gaps caused by sensor malfunctions and other issues that depend on the length of the missing values.

We are going to build up our digital twin. This is the backend. The front end, or the phenotype of DIGI4ECO, as it will appear online to end users, is represented in this mock-up. The project is four years long, and we started only two years ago, so we have two more years to go. This mock-up illustrates where we're heading in terms of interaction on the web with people who will log onto the project website. Users will select the area, the platforms, and the sensors, as well as the biological and environmental variables they want to analyze together. They will also select the time window for their analyses. Based on the screening of data quality, they will be advised by artificial intelligence on the best multi-environment statistical tools to operate those analyses. In the end, they will receive a matrix as a descriptor of the biological data from the marine observation platform.

I will now speak about artificial intelligence in image processing. In marine ecology, we are essentially inventing the wheel now because the industry is possibly smarter; you are much more expert than us. However, we are interested in overcoming the human bottleneck in processing terabytes of information we receive weekly. Artificial intelligence in image monitoring is something we have developed over the past decade, thanks to our connection with Ocean Network Canada, which provides a network of cable observatories in British Columbia. 

At one kilometer depth, we monitor sable fish, which is a significant fishery item for Canada, the US, and Japan. Because this sampling is limited, we are using a crawler. This is only one kilometer depth data to that cable node, and we drive it remotely with the right panel from Barcelona. However, we don't want to drive it; we are equipping it with edge computing routines, giving the crawler the capability to operate itself back and forth along transit and to count animals of different species.

Bringing together all this experience, we are elevating the intelligence of OBSEA, the master platform that belongs to us and will service technological development in DIGI4ECO. It is located one hour south of Barcelona, in a very nice place. Please visit if you have time. It is four miles off the harbor of Villanova, in a Natura 2000 area, which is a protected area. We have been streaming biological and environmental data continuously for 10 years. The results show AI automatically classifying animals in a very complex operational scenario, with several species of fish appearing together.

To conclude, we are interested in increasing the virtual representation capability of all digital models by ingesting any type of data we can, including very different sources: satellites and fishing vessels. The long liners and crawlers that work 20 kilometers around all deployment areas will provide us with their logbooks, in which they annotate the species per day. This gives us huge time series of biological data, which we can introduce into the forecasting strategies of DIGI4ECO, also providing information about the socio-economic output.

Enoc will now explain in more detail the application. Thank you very much. Thank you, Jacopo. The engineers will speak about data flows, servers, and these kinds of things. Jacopo explained what we aim to do: we want to monitor ecosystems and create this virtual copy. We have this platform that gathers data, and that's what we have here. We have observatories with sensors and platforms gathering scientific data. We also want to use socio-economic data. Is there aquaculture in the region? Is there any fisheries data? Do we have industrial impact in the area? All this needs to be sent to what we call the digital twin, where we have all these AI tools, repositories, simulations, filtering duration, etc. Users can access this data, run simulations, and conduct "what if" scenarios.

We want to replicate this four times, as we are using it in four different locations: Ireland, Sweden, Italy, and Spain. I will focus specifically on OBSEA, which is where I work, and I would say it is the most advanced. OBSEA, as you can see in the top right, is a picture of this observatory at the seafloor. It has been running for the last 17 years, and we have been acquiring data from various sources, including acoustics, video cameras, and classical sonographic sensors.

In terms of IT, we have real-time data flowing from the seafloor to our infrastructure, where we are acquiring this data and ingesting everything that is a time series into a Postgres database with a timescale extension. We also have everything that is file-based exposed publicly in an engine instance, including videos, pictures, sounds, etc. Here are some images of the kind of data we are working with.

Why are we here? Because we are also using Grafana. For what? To visualize this data, of course. We have all this data flow that might seem a bit exotic to you coming from the seafloor. We store it in a traditional database, and then we display everything in Grafana. So, of course, there will be some Grafana dashboards. 

What kind of dashboards are we using? How are we using Grafana to provide scientific services to the community? First, we display time series data. For example, we have a sensor called a CTD, which measures conductivity, temperature, and depth. It is a classical physical sonography sensor, and we can plot our data to see if everything is okay. Do we have a cold water mass? Do we have a hot water mass? We also have some quality metrics about our data.

We can do things a bit more complicated. For instance, we also have wave data, where we measure different wave heights, wave periods, and directions. We can plot this in a Windows-like plugin, in this case, which I think is Operato Windrose. We have several different kinds of dashboards in Grafana.

Let's make it a bit more complex. We are also working with underwater acoustics. For that, we use hydrophones, which are basically our underwater microphones. Since we are sampling sound at 100 kilohertz 24/7 all year long, we cannot display this data as a simple time series. Instead, we pre-compute spectrograms, which are visual representations of periods of sound. For instance, we can see a ship going towards our observatory and then leaving.

We can also pre-compute some of the data, like pressure levels, and display statistics, such as histograms. We have this data pre-computed, and we can use it to create more complex graphical dashboards. As Jacopo mentioned, we are also using AI, specifically to detect fish species. In this case, we are running some yellow object detection models that have been developed to identify different species of fish in the underwater video footage we collect. This is crucial for understanding the biodiversity in the areas we monitor.

Detecting species allows us to extract time series data, and we can also examine individual pictures to see the detections. We can filter them and select different species, as well as look at the sourcing image and the processed image. For instance, we can compare different textures to see if there is a prey and a predator, to determine if they are together or if one is attacking the other, etc.

This discussion is primarily about scientific data. However, we need to understand that the ocean is a very harsh environment. There are numerous issues, such as corrosion and storms. Everything in the water will eventually break; it's just a matter of two days, two weeks, or two years. We need to monitor that. 

We face physical issues, like cables breaking due to 20-meter waves, but we also have other problems, such as corrosion where sensors degrade. Additionally, we encounter what we call bio-fouling, which is when shellfish decide to attach themselves to our sensors. These sensors can be quite expensive, costing tens of thousands of euros. 

After deploying a new sensor and obtaining excellent data, we may find that, after some time, it looks like this: the same sensor deployed for one year with various shellfish attached. For example, a conductivity cell with a perfect geometry can have a mussel on top of it, distorting our measurements. We need to monitor these situations so we can clean the equipment and redeploy it.

For this purpose, we are also using Grafana. Here, we can see a classical physical parameter, salinity, and we observe a significant drop at a certain point, specifically when shellfish are present in our conductivity cell. Since sensors are so expensive and difficult to manage, we need to keep track of their history, which we also do using Grafana. 

We maintain a database with all our metadata stored, along with adjacent BLOBs and controllable crawlers, utilizing various tools common in the scientific community. We can display all this information in Grafana. We have pictures of sensors before and after deployment, a sensor history, and a timeline, allowing us to quickly get an overview of the sensors and their operational life. For instance, we can determine if a sensor has failed three times in the last year, indicating it may need to be sent to the manufacturer or replaced.

We have dashboards for individual sensors, but we can also create dashboards for groups of sensors. Since we manage tens or even hundreds of sensors, we cannot check each one individually. Therefore, we have lifetime dashboards in Grafana to monitor the operation and lifespan of all sensors.

Finally, we are conducting research that may seem exotic to most, but at the end of the day, it's about data flowing from sensors into a database where we perform processing. This requires servers, databases, and IT infrastructure, which we also monitor using Grafana. In this case, we use Zabbix to provide the metrics, visualizing everything in Grafana dashboards. This allows us to quickly see the status of our servers, check for enough space, and identify any issues with excessive requests.

To wrap up, we aim to build a digital twin of the ocean, a virtual representation of the ecosystem where we manage multi-parametric data flows and underwater assets. We have various tools that are somewhat common but applied in a very specific context, such as data simulation, modeling, and AI-based products. 

Initially, we envisioned a sort of old-school dashboard to view all this data at once. With Grafana, we have something that looks very similar, allowing us to use it as a front end for our vision of a digital twin. We can display the data we acquire from the ocean in a visually appealing format using Grafana, which is an excellent open-source tool that we are delighted with.

Specifically, we use Grafana to visualize real-time data, historical scientific data, our operations, and to monitor infrastructure health. What is missing in Grafana for us? Although it is a niche requirement, it would be beneficial for scientists working in earth observation to display four-dimensional data in Grafana, meaning time, latitude, longitude, and depth, as well as gridded data like satellite or model data. 

I understand this may not be of interest to most of the audience, but it is a critical need for scientists. If we could solve this issue, we could use Grafana as a complete front end for digital twins of the ocean.

The DIGI4ECO European project is a four-year initiative, and we are currently in the middle of it. We have done a lot of housekeeping, harmonizing the data, and consolidating everything in one place. Over the next two years, we will focus on creating scientific products to generate statistics from the ocean, visualize data, and run "what if" scenarios. Stay tuned for more updates, as we hope to deliver a complete digital virtualization of the ocean in the coming years. 

Thank you very much for your attention. Thank you.

## Raw YouTube Transcript

Thank you very much. Thank you very much. Good 
morning, everyone. I'm Jacopo Aguzzi from the Marine Science Institute of Barcelona, one of 
the five Marine Institute in Spain belonging to the Spanish National Research Council, which 
is the largest academic institution in the planet. Sorry, in the planet Spain. Okay.
Let me introduce myself properly. This is my background. It's in marine ecology. I work 
in fishery management. And since more than two decades, I got specialized, alphabetized toward 
the technological development for solutions to monitor the marine environment from the 
coastal areas to the deep sea. Enoc? Hi, everyone. My name is Enoc Martinez. I work 
at UPC, Technical University of Catalonia. And my background is electronic engineering, although 
I spent the last 10 years doing scientific data management in scientific data infrastructure 
specifically focused to the ocean. And here you can see me on a boat, but I actually 
spend 99% of my time behind the desk. Okay. Let's start with the context where DIGI4ECO 
board, which is the ecological monitoring. Why we need ecological monitoring today? As all you know 
for sure knows, we have a problem in the sea, like in the terrestrial environments, there 
is an increasing piece of anthropic activity that damage different ecosystems. There is 
an interest to monitor them. And for here, I choose two iconic figures. For you, the first 
one is referring to the industrial extractive activities by trawl hauling, occurring almost in 
all continental margin of the planet that sweep entire ecosystems on a daily basis. And then we 
have the omnipresent effect of plastic pollution. These are two out of many impacts we have. 
And that's why we have the need to monitor the environment and policy environmental management 
agencies, including the European communities. The European community are interested in developing 
metrics to assess the GES, the good environmental status, of marine ecosystems within the 
biodiversity agenda of the European community. GES is something that belong to the Marine 
Strategy Framework Directive, which is a policy ruling body. And that is aiming to measure 
the status, the health of those ecosystems through 11 descriptors or ecological indicators. 
Descriptors like, for example, the seabed status, the biological diversity, the presence of 
contaminant in the seafood as a service we extract from the ecosystems and we heat, or the 
status of commercially exploited marine species. But those descriptors are semantically open, so 
they require a thoughtful dialogue of scientists and policymakers on which type of data we 
need to compute them. It's very important. So environmental biological data, special temporal 
scales, and in the end, the discussion always goes to technologies. Why technologies? Because 
monitoring the ocean, it costs a lot of money. You have to think that what we know about the 
sea, most of the sea, is because we have been collecting data by vessels in the past 200 years. 
Vessels are very expensive technologies. Why? Because if you think that we have a star vessel 
in the Spanish fleet that is named Sarmiento de Gamboa, Sarmiento de Gamboa is an average 
length vessel of, I would say, 70 meter length, more or less. It's not so big, it's not so small.
In the world planet of the fleets, so it's in the average size. It costs per day up to 25,000 
euros. It's a lot of money. So this means that for us to collect the data, data is money, 
and we need to have a strong budget in support. Plus, there are much more people willing to use 
the vessels than the vessels themselves. So we have a problem of calendar. They're always 
booked. That's why DIGI4ECO is willing to drive ecological monitoring toward the use 
of robotic networks. So autonomous platforms that are being developed under dilemma bring 
back scientists from the decks of the vessels, so from the field to their office on the shore.
Sorry, Enoc, you will be more on the office. And we use three major type of robotic platforms in 
DIGI4ECO. The first one are cabled observatories, which are tethering the platform through 
telephonic or internet cables to shore. So they stream data continuously in real time and they get 
power to be fed over consecutive years of action. And then, we have their equivalent, which 
are Landers. They are a standalone version of cabled observatories. No cables, easy to be 
adaptively redeployed, strategically redeployed, but with a much shorter autonomy because 
they have battery packs. In general, up to one year. Because those two platforms have 
a limited data collection capability because they're fixed. Environmental more heterogeneous 
than a single pixel of space in which you place those platforms. Then we're working with 
robotic solution to automatically sweep the environment around those platforms at an hectare 
scale. And I'm talking about data-read docked crawlers, which are trackable vehicles 
that we'll describe you in a few slides. So why this is important? Because European 
community is trying to change the paradigm of research. And one of the line of of these 
changes to paradigm is digital twin of the ocean. Digital twin of the ocean is the creation of 
virtual replicas of the ecosystems. More data we have, better the replica is. Which type of 
data? The data that we stream with our platforms that are endowed with multi-parametric sensors 
assets. We have three major type of data that we stream into the digital twin. Biological, and I'm 
talking about AI to process images. Then we have AI to process acoustic output because 
we listen to the seascape looking for biological sounds. That's something that Enoc 
will describe with more detail later on. And then, we have geochemical data which are 
provided by sensors that characterize the solvent oxygen. For example, the solvent methane, CO2, 
nitrate, phosphate from agriculture, pH turbidity, and all the stuff, plus the classical 
stenographic sensors that characterize the water masses in terms of salinity, temperature, 
and water speed and direction for currents. With these, we pretend to create not only virtual 
replicas of the environments, but also real-time updated replicas of those environments. Okay, 
why? Because we want to know precisely the present status to run "what if" scenarios by artificial 
intelligence. We have from one side, the IPCC, the international panel for climate change, that's 
telling us that on the basis of present knowledge, the status of the sea in the next 50 year will 
be, in relation to temperature salinity and so on, what it will be. Okay? I won't enter in that.
But we want to model the biological response of life, living components, in the 
ecosystem. So we want to know, for example, in relation to an increasing temperature 
and salinity, what will be the presence of species as we see now. If they will go away, if 
they will go extinct, or they will reduce their numbers of individuals and things like this.
Plus, all these need to be somehow synthetically collected into a web framework in which citizens 
and policymakers can log on and can synthetically strategy information in a meaningful ecological 
output that they can understand and can use. That's web visualization. So in this respect, 
the DIGI4ECO has the following aims. The first aim is that we want to virtually recreate digital 
replicas of four ecosystem, coastal ecosystems, 20 meter depth in the Atlantic, two in the Atlantic, 
two in the Med, in the Mediterranean. Why coast? Because humanity developed along the coast. Along 
the river as well, but this is not the target of our project. Coastal lines are the first line of 
impact of humanity. We have master platforms in this robotic network establishment for this for 
environment, which are two cable observatories, one in Galway Bay in Ireland, the other one here 
close to Barcelona that I will describe you later in a bit, and then we'll go in more detail.
Then we have crawlers operating in Kristineberg above Gothenberg in Sweden, and then we will 
have in the Eastern Mediterranean Sea, of the Italian cost in Ancona, landers. We will build a 
standardized digital twin for these four different environments. The heart of it will be an online 
data bank that remotely will store all the data, will pre-process them for homogenization and 
standardization, and that will be embedded AI routines for flagging data quality, eliminating 
outliers, and using different models to fill up the gaps in that acquisition for sensor 
malfunctioning and all the stuff that will depend on the length of the missing values.
We are going to build up ... Of our digital twin, this is the backend. The front 
end, so the phenotype of DIGI4ECO, as it will appear online to end users, will 
be this one. This is a mock up, because the project is four year and we started only two 
years ago, so we have other two years to go. Okay. This mock up is telling you where 
we're going in terms of interaction on the web with people that will log on on the 
project website. They will select the area, they will select the platforms and the sensors, 
so the biological and environmental variables they want to analyze together, and they will select the 
time window in which they will be willing to run those analyses. And then, they will be advised by 
artificial intelligence based on the screening of data quality, which are the best multi-environment 
statistic tool to operate those analyses. And in the end, they will have some sort of matrix 
as the descriptor that I told you before. Which type of biological data from marine 
observation platform we are talking about? I will speak about artificial intelligence 
in image processing. Today in marine ecology, of course, we are inventing the wheel now because 
the industry possibly is smart, you are guys are much more expert than us, but we are interested 
in overcoming the human bottleneck in processing terabytes of information we get by week.
Artificial intelligence in image monitoring is something that we elaborated in the past decade 
thanks to the connection with Ocean Network Canada. Ocean Network Canada providing a network 
of cable observatories in British Columbia. At one kilometer depth, this is an example, we monitor 
sable fish. Sable fish is a relevant fishery item for three countries: Canada itself, US, and 
Japan. But because this sampling is limited, we are using crawler. This is only one, one 
kilometer depth, data to that cable node, and we drive it in remote with the right panel, so from 
Barcelona. But because we don't want to drive it, we are endowing it with edge computing routines, 
the crawler of capability to operate itself back and forth along transit and to count animals in 
different species. Okay, that's what we're doing. Bringing together all this experience, what we are 
doing? We are elevating the intelligence of OBSEA, the master platforms that belongs to us and will 
service technological development in DIGI4ECO. It is located one hour south driving from Barcelona. 
Very nice place. Please visit if you have time. Four miles off the harbor of Villanova in a 
Natura 2000 area, which is a machine protected area. 10 years of streaming of biological and 
environmental data continuously, okay? And that's the results. The AI automatically classifying 
animals in a very complex operational scenario, several species of fishes appearing together.
To conclude, we are interested in increase the virtual representation capability of all digital 
models by ingesting any type of data we can. Also, very different one: satellites and fishing vessel. 
Because the long liners and the crawlers that work 20 kilometers around all deployment areas will 
provide us with their logbook in which they annotate the species per day. So we have huge time 
series of biological data. They will annotate what is happening to the biology. We can introduce this 
in the forecasting strategies of the DIGI4ECO, providing also information about the 
such economy output. Enoc now we'll explain you better in detail the [inaudible 
00:13:41] application. Thank you very much. Thank you, Jacopo. And the engineers have to 
speak about data flows, servers, and these kind of things. So Jacopo explained what we aim to 
do. We want to monitor ecosystems. We want to create this virtual copy. We have this platform 
that gathers data, and that's what we have here. So we have the observatories with centrals and 
platforms gathering scientific data. We also want to use socio-economical data. Is there some 
aquaculture in the region? Is there any fisheries data? Do we have industrial impact in the area? 
And all this needs to be sent to what we call the digital twin, where we have all these AI tools, 
all these that are repository, the simulations, the filtering duration, et cetera.
Users can get this data, do the simulations, run these "what if" scenarios. And 
we want to replicate this four times, because we are using it four different 
times: in Ireland, Sweden, Italy, and Spain. I'm going to focus specifically on 
OBSEA, which is where I work. And it's, I would say, the most advanced. OBSEA, 
you can see here in the top right, a picture of this observatory at the seafloor. 
It has been running for the last 17 years, and we have been acquiring data from different 
data sources, from acoustics, video cameras, classical sonographic sensors, et cetera.
In terms of IT, what do we have? We have real-time data flowing from the safe floor to 
our infrastructure where we are acquiring this data and we're ingesting everything that is a time 
series into a Postgres with a timescale database. And we also have everything that is file-based 
exposed publicly in an engine instance. So videos, pictures, sound, whatever. And this, 
you can see here, some of the images of the kind of data that we are working with.
And why are we here? Because we are also using Grafana. For what? To visualize this data, for 
sure. We have all this data flow that could be a bit of exotic to you coming from the sea floor. 
We store it in a traditional database, and then we display everything in Grafana. So of course, there 
will be some Grafana dashboards. What kind of dashboards are we using? How are we using Grafana 
to provide scientific services to the community? So first thing, simple enough, displaying time 
series data. So we have this sensor that you can see here. This is what we call a CTD. It 
measures conductivity, temperature, and depth. It's a classical physical sonography sensor. And 
we can plot just our data to see if everything is okay. Do we have a cold water mass, we have 
a hot water mass? Whatever. We also have some quality metrics about our data. Simple enough.
We can do things a bit more complicated. We are also having, for instance, wave data where we 
have the different wave height, wave period, the direction. We can plot this in a Windows-like 
plugin, in this case, which I think it's Operato Windrose. We have several different kinds of 
dashboards in Grafana. Let's make it a bit more complex. We are also having underwater 
acoustics. And for that, we use hydrophones, which is basically our underwater microphones, 
simple enough. And then, since we are sampling 100 kilohertz or sound 24/7 all year long, 
we cannot really display this data as a time series. So we do things a bit more complicated. 
For instance, we pre-compute spectrograms, which is basically a visual representations 
of periods of sound. So we can try to see what's in this sound. For instance, here we 
can see in the middle, a ship going towards our [inaudible 00:17:24] and then leaving.
We can also pre-compute some of the data, like some pressure level. We can also 
display statistics, like in this case, the histogram. We have this data, we pre-compute 
it, and then we can use all this pre-competed data to show a bit more complex graphical dashboards.
Of course, as Jacopo mentioned, we are also using AI. And specifically, we're using AI to detect 
fish species. So in this case, we are running some yellow object detection models that detect 
species, then we can extract the time series, and we can also look at individual pictures to 
see the detections. We can filter them. We can select different species. We can look at the 
sourcing image, the processed image. Here, for instance, you can see that we are 
comparing to different textures to see if there is a prey and a predator, to see if they 
are together or one hits the other, et cetera. Okay, this is just about data for now, scientific 
data. But we need to understand that the ocean is a very harsh environment. You have all sorts 
of issues. You have corrosion, you have storms. Everything in the water, everything will break 
eventually. It's just a matter of two days, two weeks, two years, but it will break and it will 
fail at some point, and we need to monitor that. We have these physical issues, like your cable 
breaks because you have a 20 meters of wave, but then we also have other physical issues like 
corrosion, your sensor degrades. But you also have what we call bio-fueling, which is basically 
some shellfish deciding to lift in your sensor. These sensors are quite expensive. They 
can be tens of kilo euros. And then, you buy your new shiny sensor, you deploy it, 
you have excellent data, and after several time, you have this. This is the same sensor 
deployed for one year with all sorts of shellfish attached to your sensor. You have your 
conductivity cell, which has a perfect geometry, and then you have a mussel on top of it distorting 
your measurements. And we need to monitor that. We need to see when it happens so we can go there, 
take out the equipment, clean it, and deploy it again. And for that, we're also using Grafana.
In this case, we can see here we have in top what is a salinity classical physical senography 
parameter, and then we see a significant drop at some point, specifically when there's some 
shellfish in our sensor, in our conductivity cell. And for that, we are also using Grafana.
Since sensors are so expensive and they are difficult to manage, we need to keep track 
of sensor history. And for that, of course, we are also using Grafana. We have a 
database with all our metadata stored, adjacent BLOBs with controllable crawlers and all 
these tools that we are using in the scientific community. And then, we can display all this 
information into Grafana. We have pictures of sensors before and after deployment, we 
have a sensor history, we have a timeline, and we can get relatively quickly an overview 
of the sensors and of their operational life. So we can say, "Oh, this sensor failed three times 
during the last year. Maybe it's time to be sent to the manufacturer or to buy a new one." And of 
course, we have dashboards for individual sensors, but we can also create dashboards for 
groups of sensors. We are managing tens or even hundreds of sensors, so we cannot 
go one by one. And for that, we also have lifetime dashboards in Grafana where we can see 
the operation and the lifetime of all of them. And finally, we are doing this kind of research 
that I'm pretty sure will be exotic to most of you, but at the end of the day, it's data flowing 
from some sensors into a database where we do some processing. So we need servers, we need databases, 
we need IT infrastructure. And of course, we are also monitoring IT infrastructure. And how do we 
do that? With Grafana. In this case, we are using Zabbix to provide the metrics, and we visualize 
all of this into the Grafana dashboards. So we can have in a quick glance. We see all our servers, 
the status. Do we have enough space? Are we having issues with too many requests, et cetera?
To wrap up, some conclusions. We want to build a digital twin of the ocean, which is this virtual 
representation of the ecosystem where we have multi-parametric data flows and we need to manage 
underwater assets. We have all these tools that are more or less common, but in a very specific 
context, which is data simulation, modeling, AI based products, et cetera. And the idea that 
we had at the beginning is what you can see here, which is a sort of old school dashboard 
where we can see all these data at once. With Grafana, what do we have? Something like 
this, which looks very much the same. So we can really use Grafana as a front end for our 
vision of a digital twin. We can see the data that we acquire and we gather from the ocean, we 
can display it in a nice format using Grafana, which is an excellent open source 
tool that we're delighted with. Specifically, what do we do with Grafana? What do 
we use Grafana for? To visualize real-time data, to visualize also historical scientific data. 
We can visualize our operations and we can monitor infrastructure health. What is missing 
in Grafana for us? I know that it's very niche, but it would be nice for us as a scientist 
working in earth observation that we could also display four dimensional data in Grafana, 
meaning time, latitude, longitude and depth, gridded data like satellite data or model data. 
Of course, this is a niche. I know that it's not of interest to most of the audience, but 
that's what scientists really need. That would be the very last issue that, if we can 
solve it, we could use Grafana as a complete front end for digital twins of the ocean.
And DIGI4ECO European project. It's a four-year project. Now we are in the middle. We did 
a lot of housekeeping, keeping the data, harmonizing the data, putting everything in the 
same place. And now we will work during the next two years in creating scientific products to 
create statistics from the ocean, to visualize, to run "what if" scenarios, et cetera. Stay 
tuned for more. And over the next two years, we hope to deliver this complete digital 
virtualization of the ocean. Thank you very much for your attention.
Thank you.

