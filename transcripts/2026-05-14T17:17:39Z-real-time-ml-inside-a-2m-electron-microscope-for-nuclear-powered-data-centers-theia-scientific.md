# Real-time ML Inside a $2M Electron Microscope for Nuclear Powered Data Centers | Theia Scientific

Published on 2026-05-14T17:17:39Z

## Description

Chris and Kevin Field from Theia Scientific show how they built a Grafana-powered platform to run real-time machine learning ...

URL: https://www.youtube.com/watch?v=SdlftTq74-w

## Summary

The show "Real-time ML Inside a $2M Electron Microscope for Nuclear Powered Data Centers" aired on May 14, 2026, featuring Chris Field, president and co-founder, and Kevin Field, professor and vice president of Theia Scientific. They discussed the integration of Grafana with machine learning and fusion energy research through their platform called Theiascope, which enhances real-time defect detection in materials used for fusion power. Key takeaways included the importance of using advanced technology to improve data analysis in scientific research and the potential of Grafana as a rapid application development environment for scientists. The presentation highlighted the collaboration between various research institutions and the innovative use of Grafana to create a user-friendly interface for complex data analysis.

Topics: Grafana, machine learning, fusion energy, Theiascope, real-time data analysis.

## Chapters

00:00:00 Introduction to fusion energy and its relevance to AI data centers
00:06:10 Overview of Theiascope technology for real-time analysis
00:15:30 Why Grafana was chosen for real-time ML in microscopy
00:17:05 Integrating Jupyter Notebooks with Grafana for real-time ML

**Hello, and thank you for coming to our presentation.** My name is Chris Field, and I am the president, co-founder, and principal developer at Theia Scientific. With me is...

**Hi, I'm Kevin Field,** and I'm a professor and also vice president at Theia Scientific as well.

Today we're going to talk about three things that do not appear to overlap in any way, shape, or form, but hopefully, by the end of this presentation, we will convince you that there is some overlap there. Specifically, we're going to talk about fusion power, Grafana, and machine learning. These three topics will be interwoven together with a technology that we call the Theiascope. So, we're going to show how all three things come together, and we're going to start first by talking about fusion energy.

**Yeah, so as I'm a professor,** we have to start with Fusion Energy 101 and Fusion Materials 101 as part of that. What I want to talk about is how fusion energy is being used and how it will power AI data centers, but more importantly, how we know they're going to last over the decades in order to power those data centers. This is where materials become important.

Under fusion energy, you're going to have a reaction that occurs that makes energy, right? Or basically gives you the energy that you need for a data center, but it's also going to create something called neutrons. These neutrons act as tiny little bullets that are going to make tiny little holes in your materials. Ideally, we want to know if it's going to make the holes, how many, and how big. This will be a theme that you're going to hear throughout this presentation.

We have computer simulations that show us essentially how these materials are going to be affected. However, if you're a regulator in the US or even in the EU, computer simulations aren't enough. We actually have to do experiments. But we have a problem: we don't have a full-scale fusion energy center at this time. We don't have a tokamak; ITER is still being built in France. So what do we do?

In my research group, we end up using ion beams. You can think of these ion beams as little laser guns that are shooting the same type of holes in the materials that the fusion system would as well. We use the Michigan Ion Beam Laboratory to irradiate those materials and look at how they're going to perform, trying to mimic or simulate what's going to happen in the tokamak. We actually compare that with computer simulations, effectively doing experimental simulations as part of that.

What my group specializes in is seeing these defects or this damage created in the material in real time. We connect a microscope into the ion beam facility and use a transmission electron microscope. For those that are old enough, it's like an overhead transparency projector with electrons instead of white light. You magnify the image using the microscope while bringing in that laser beam of ions to hit the material. We can see the damage that's made in real time. Each one of these little black dots and loops represents damage in the material. We want to know how many and how big they are over time because we want to know the dynamics—whether this material will last for seconds, minutes, decades, and so on.

This is what it actually looks like in real life. This is one of my graduate students operating the microscope. You have a microscope here, and that ion beam comes in, allowing us to view everything digitally right on the microscope. For reference, this microscope costs $2 million, making it a very fancy piece of equipment. The students take videos and images on that microscope while we hit the sample. They then figure out how many and how big all of those little black dots are in the image.

Eventually, we hope to make a discovery, and hopefully, at some point, I'll be up here on a stage with a Nobel Prize. But we have a problem. If you're a microscopist, this is our beautiful dashboard. This is the software that most people are using, called Image J. It is basically Windows 95-grade material and has been used for the past three decades. If I submitted this, I don't think I'm ever going to get a Golden Grot at this conference using this software.

The other problem is that all of this is done with manual labor. My students sit there and manually circle every single one of those little black dots that I showed in the video or the image. This is where AI and machine learning also get interwoven. Over the past couple of years, we've started using the same technologies used for self-driving cars to automate defect detection in our images. The scientists have actually gotten pretty good at this. We've become adept at using real data as well as synthetic data to train machine learning models to find the same features in the images. This has rapidly accelerated our ability to analyze data, and the models keep improving every day or every week.

There are quite a few groups now developing these types of algorithms for automated defect detection. For those who are machine learning practitioners, the F1 scores in our field are around 0.8 and keep growing up to 1. That's like a B-minus student for those who use the US grading system. However, there's another problem. Scientists are really good at making these machine learning models because they just take them off the internet—open-source models and so on—and use them and train them. But they're really bad programmers when it comes to deployment. Almost all of them are using Colab or Jupyter Notebook with built-in dependencies. If I wanted to use another research group's data source, it ends up being almost impossible due to specific dependencies, poor formatting, and poor UI, or even no user interface.

In my group, I want to do this all in real time. I want to see what's actually happening on the microscope. Until a couple of years ago, there was no solution for this. So what Chris is going to show and talk about is our web app and our hardware platform that allows us to do all of those things together.

**Yup, thank you.** What we've come up with is this technology that we call the Theiascope. This combines Grafana and Jupyter Notebooks all on a device that you can see here on the left-hand side. This is an on-premise self-hosted device attached to that microscope because we don't want our multimillion-dollar microscopes being accessible to the outside world. So we brought the GPUs and the cloud to the microscope in this case.

Now, I could probably talk about this diagram all day, but I think it would be better and easier just to show it in action. So let's go ahead and we will hold our breath and hope this works as we flip over to the system. 

This is our home dashboard. This is the central interface, the first interface that scientists will see. We can see that we have a couple of different panels. We're using a calendar app, which Kevin really enjoys because he can tell whether his students are actually doing work or not and if they're in the lab based on one data appearance. On the other side, the left-hand side, we have our...

**Model Management Panel**

This is where we can spin up a variety of different models. I've already marked a favorite for today, and we're going to look at some TRISO particles. I'll explain what those are in just a moment. We're going to, again, hold our breath and click the **Start Actor** button. This brings out a drawer that has all those machine learning model parameters, allowing you to tune and fine-tune the inference that's occurring on the system while you're running your microscope. But we're just going to use the defaults and hit start. This will unpack that model, load it onto the GPU that is sitting right here, and it will then spin up. 

So, it's initializing, unpacking, and getting ready to go. We're now idle and ready to conduct some experiments. Now, we didn't bring our $2 million transmission electron microscope with us; they wouldn't let us have it through security. Instead, we're going to use some images that will serve as an approximation for that. 

Now, we've moved into our acquisition panel, where we will capture some images and perform real-time image analysis on these TRISO particles. If you're familiar with the US candy, Gobstoppers, these particles have sort of inner layers. What we want to know is the uniformity of each of these particles. In this case, we have about 10 images, but in reality, you probably have thousands, if not tens of thousands, of images of these particles. Normally, you would have to draw a circle around each layer, measure those layers, and then decide if this is a circular particle or not. If it's not circular, we want to reject that batch of particles.

So, we have that set up. I'm going to move this field of view so that we can focus on just the part that is in the center here and not grab the rest of the stuff. It takes me just a moment to do this with a trackpad. We're going to go ahead and start some acquisition. It's going to be in progress, and in just a moment, with luck, on the right-hand side, we will have started our very first inference, running through those images.

Now, I'm going to say, "Okay, let's move around and look at some other particles while we're doing this." This is just going through **Preview** on an Apple. We can see on the other side that we are clicking through, and it's doing that analysis in real time. We just have to use our imagination a little bit that this would be on the microscope as it's being connected to this ion beam, simulating a fusion power system to power the next generation of data centers that will ultimately power Grafana in the future.

So, we're going to go through and do a couple of different scans through these images. This is just to give us some preloading for some other things that we're going to see here in just a moment. I've loaded up those images. We can see this one is a little oblong, which we can observe as humans. But what we can also do is zoom in, and I have this **uniformity chart**. If it were a perfectly circular particle, each one of those layers would be a perfectly flat line across the plot. This allows the user, the scientists, to immediately see, "Hey, is this a good particle or a bad particle?" 

We also have on the other side some stat panels that show the standard deviation. We can turn those into metrics that will identify and aggregate if this is a good sample or a bad sample. On the left-hand side, we have our different layers, which show the performance of the model and how confident it is in finding those layers. We can go through the system and look at that.

We can also zoom in and do some further analysis by going to what we call the **Examine Dashboard**. If this works, it will give us the same kind of information. For those of us that are old enough, this is like our VCR; you can scroll through time, go back in images, and go forward in images like we were doing during the acquisition. That panel doesn't seem to want to work today, so that's fine. We'll go back over to our acquisition panel.

What we can see here is we still have this uniformity chart. I'm going to take a look at how we are calculating these uniformity plots. What we're doing is running something that doesn't look like PromQL or SQL; we're running a **Jupyter Notebook**. How are we doing that? In fact, we have Jupyter running on the system, and every time the dashboard updates, we are running through this Jupyter Notebook that a graduate student wrote to create that uniformity plot. This is in a language that the scientists are at least familiar with, and they can download these and upload them to the system. It's running this code every single time within this panel, giving us this uniformity.

This allows the scientists to create whatever kind of metrics or plots they want during the experiments while they're on the microscope. We can also do some other things with this. The way Jupyter is working and hosted on the system allows us to use notebooks and dashboard variables. We can pass those to the notebooks, and because of how it's working, we can actually put, for example, the Python code directly into the dashboard. 

So, we are running this live on the system, and we can make changes. If I don't like the parabola, we can go ahead and make that change. We can do that as we are conducting the experiment. We can copy and paste snippets of code from other notebooks or from other researchers or collaborators and make these changes in real time while running the experiment. 

As I said, we also have this tied to various variables, or we can create these other variables in the system as we're running them. We can create custom code snippets and run the code live within the dashboard in an environment that the scientists are familiar with, given that they're developing these models they want to host and deploy at the microscope to ultimately make their discovery and determine if it's a good or bad material for a fusion power plant and/or win the Nobel Prize. That's the dream.

So, we go ahead and stop the acquisition, and we will go back now to the presentation. Great! What we saw there is the whole system working together in real time on the microscope. The question is, how did we put this together, and where do we go from here? 

This brings us to the very first question we always get: "Okay, why did you do this with Grafana? Why did you pick it?" We chose it for a variety of very good reasons. One is the data sources; there's a whole community of them that are open and available. This helps with the big tent concept because that's the interoperability that allows us to connect to a variety of different microscopes and experiments and customize our dashboards. 

The very first iteration of this entire code and application that I showed Kevin was...

The feature request was, "I want a dashboard where I can change things and move things around and have them for different things." I thought, "Okay, we're gonna go with Grafana because I don't want to have to create all that." We get all of this for free, in a sense, by doing that. The other nice thing is that we have some great panels and visualizations that we can use. The documentation for creating your own visualizations, data sources, and plugins is fantastic, and that has really helped us to develop this. 

Additionally, there's this vibrant ecosystem of all the people here and around the world, putting this all together for us and helping us out in doing this. Also, Grafana is awesome, right? We're all here; it's awesome. But is it RAD? I'm going back to the 1980s, right? But RAD in the sense of can it be used to do irradiated materials characterization? And also, can it be used as a rapid application development environment? 

We have already seen something that is somewhat similar in that we have an interactive notebook-centric development environment that's pretty ubiquitous among the ML and science community that rapidly ingests, explores, and visualizes code and/or data. That's interesting because that's also what Grafana and the Observability stack do. 

So, spoiler alert: yes, we can make Grafana RAD because we just saw the demo doing that, and we wouldn't be standing up here if we couldn't do that, right? But how did we get to making it RAD? It starts with the anatomy of a panel. I sat down one day and thought, "Okay, how does this all get put together? How does this all work in a sense?" 

If you look at this and squint at it, you can sort of see the backwards G of Grafana in there. In the flow, you go from your data source to the query editor, creating data frames and using the transforms. Then you have your options, and they ultimately get put up into the view inside of a panel. 

Using that, what we have is that your query is selecting data. The transform is converting it into a format that can then be customized by the options and ultimately displayed inside the view. If we focus on those first two, we have our query and then our scripts, which are transforms and snippets respectively. 

Unfortunately, scientists are never going to learn SQL. It is just not something they can wrap their brains around. They're too busy operating those microscopes and drawing boxes around black dots. So it's not Python. That's what they're learning. That's what they use. That's what all the notebooks are in. 

What else is out there that consists of small snippets of code that does some kind of translation of maybe a request, pulls some data from a database, and returns a response? That got me thinking. I thought, "Well, maybe we could use something like Lambda from AWS, which runs Python and JavaScript." But can we do that on the device? Can we have a similar kind of thing running small snippets of Python code in an environment that's familiar to scientists and engineers? 

Yes, we can. That's what this Jupyter flow is called here, and this is what was running in the demo. You start off with your Jupyter server; we had our Jupyter Lab, which is the web interface for that. We've created a data source that passes Python code from Jupyter Lab into the server, then comes back out. But we can also go the other direction. We can go from our query editor, which we saw with the inline code, and pass that back to the server. 

This allows us to create some pretty crazy things to do with the kernels and the various Jupyter Notebooks running. We can do things like pass the dashboard variables between them, integrating the Jupyter flow into the Grafana flow of that panel. We're going from the query editor to the transforms, options, and view. 

What this makes happen is that the Jupyter Notebook becomes the data source. It becomes that part that is translating it from one to the other. We can run the code directly in there. The scientists can make the changes, and they can see it happen immediately. They get that interactivity and feedback in the system. They also have the ability to install the entire Python ecosystem because we are handling the magic keys with the percent sign there. 

So we're doing a pip install here just of time zones because we needed to do that in order to do the sign there. We now provide a rapid application development environment for scientists and engineers in nuclear materials characterization or irradiated materials characterization. Grafana is RAD. It is awesome, it is RAD, and we're able to create these custom workflows and have them run on a deployable system that's easy for scientists and engineers to use. 

Ultimately, we can share all this information to get us to fusion energy to power the next generation of data centers. We hope to convince everyone here that these three seemingly disparate things are actually interwoven together. We have also done that by using our Golden Grot, as we were the 2024 Golden Grot winner of the beautiful dashboard. That dashboard was generated by using this exact system. 

In the center is this Theiascope that connects fusion energy and AI/ML together. On top of all of that is the Grafana stack integrated with a Jupyter Notebook interface. With that, we'd like to acknowledge and thank some of our collaborators and our funding agencies, specifically the Department of Energy in the United States. The images you saw of the TRISO particles came from Oak Ridge National Lab. Some of the models we use come from Wisconsin. Idaho National Lab and Argonne National Lab are both collaborators that have let us deploy the system in their multimillion-dollar microscopes in the very early stage of the system and device. 

And with that, thank you. 

- [Kevin] Thank you. (crowd applauding)

## Raw YouTube Transcript

- Hello, and thank you for
coming to our presentation. My name is Chris Field, and
I am president, co-founder, and principal developer
at Theia Scientific. With me is-
- Hi, I'm Kevin Field, and I'm a professor
and also vice president at Theia Scientific as well. - Today we're gonna
talk about three things that do not appear to overlap
in any way, shape, or form, but hopefully, by the
end of this presentation, we will convince you that
there is some overlap there. Specifically, we're going
to talk about fusion power, Grafana, and machine learning. And what those rule of
three are gonna be doing is being interweaved together with a technology that
we call the Theiascope. And so we're gonna show how
all three things come together, and we're gonna start first by
talking about fusion energy. - Yeah, so as I'm a professor, we have to start with Fusion Energy 101 and Fusion Materials 101 as part of that. So what I wanna talk about is how fusion energy is being used and how it will power AI data centers, but more importantly, how we know they're gonna
last over the decades in order to power those data centers. And that's where materials
becomes important. So under fusion energy,
you're gonna have a reaction that occurs that makes energy, right? Or basically gives you
the energy that you need for a data center, but it's also gonna create
something called neutrons, right? And those neutrons act
as tiny little bullets that are gonna make tiny
little holes in your materials. And ideally, we wanna know
if it's gonna make the holes and how many and how big. And that's gonna be a theme that you're gonna hear throughout this. And so we have computer
simulations that show us essentially how these
materials are gonna be hurt. But if you're a regulator
in the US or even in the EU, computer simulations isn't enough. We actually have to do experiments. But we have a problem. The problem is, is that we don't have a full
scale fusion energy center at this time, right? We don't have a tokamak. ITER's still being built in France. And so what do we do? In my research group, what we end up doing is using ion beams. And so these ion beams, you can think of as
basically little laser guns that are shooting the same
type of holes in the materials that the fusion system would as well. And so we use the Michigan
Ion Beam Laboratory in order to irradiate those materials and look at how they're gonna
perform and try to mimic or simulate what's gonna
happen in the tokamak. And we actually compare that
with computer simulations, but we're effectively doing
experimental simulations as part of that. And what my group specializes is actually seeing these
defects or this damage that's created into the material,
seeing them in real time. So we actually connect a microscope into the ion beam facility
and we use a microscope called a transmission electron microscope. For those that are old enough, it's like an overhead
transparency projector with electrons instead of white light. So basically, you magnify the
image using the microscope, but you're also bringing
in that laser beam of ions in order to hit the material. And then we end up being
able to see the damage that's made in real time. So each one of these
little black dots and loops is actually damaged in the material. And what we wanna know is
how many and how big we have. And we wanna know that over time because we wanna know the dynamics because we wanna know if
we're gonna have this material last for seconds, minutes, decades, so on, so forth as part of that. This is what it actually
looks like in real life. This is one of my graduate students operating the microscope. So you have a microscope here
and that ion beam comes in and we be able to view
everything digitally right on the microscope. For reference, this microscope
is $2 million as part of it. And so it's a very fancy piece
of equipment as part of that. And so what the students will do is they'll take videos
and they'll take images on that very fancy microscope
while we hit the sample. And then they want to do
is figure out how many and how big all of those little black dots are in the image as part of that. And then eventually, we have a discovery and hopefully at some point, I'll be up here on a stage
with a Nobel Prize, right? But we have a problem. So if you're a microscopist, this is our beautiful dashboard. So this is the software
that most people are using. It's called Image J. It is basically Windows
95 grade type of material and it's been used for
the past three decades. And so if I submitted this, I don't think I'm ever
gonna get a Golden Grot in this conference using
this software as part of it. And you can see how bad this is. The other problem is that all of that is done with manual labor. My students sit there
and they manually circle every single one of
those little black dots that I showed in the video
or I showed in the image. And so that's where AI and
ML also gets interwoven. So what we've been doing
over the past couple years is starting to use the same things for self-driving cars
and so on and so forth in order to start doing
automated defect detection in our images. And the scientists have actually gotten pretty good at this, right? So we've gotten really
good at using real data, as well as synthetic data in order to train the
machine learning models to find the same features in the images. And that has rapidly
accelerated our ability to look at data, right? And they keep on getting
improved every day or every week. And there's quite a few groups now that are actually developing
these types of algorithms to do that automated
type of defect detection. For those that are machine
learning practitioners, the F1 scores in our field
is kind of round 0.8, and it keeps on growing up to one. That's like a B minus student for those that use the US
grading system as part of that. But there's another problem. Scientists are really good at making these machine learning models because they just take
them off the internet, open source models and stuff like that and use them and train them for it. But they're really bad
programmers at deployment, right? So almost all of them are
using Colab or Jupyter Notebook with built-in dependencies
and so on and so forth. So if I wanted to use another
research group's data source, it uses, it ends up being
almost impossible, right? We have this problem where they
have specific dependencies, there's poor formatting,
and there's poor UI, any or no user interface as part of it. And the other problem becomes, in my group, I wanna do
this all in real time. I wanna see what's actually
happening on the microscope. And so until a couple years ago, there was no solution for this, right? And so what Chris is gonna show and talk about is our web
app and our hardware platform that allows us to do all
of those things together. - Yup, thank you. So what we've come up
with is this technology that we call the Theiascope, right? And this is combining Grafana and Jupyter Notebooks all on a device that you can see here
on the left hand side. So this is an on-premise
self-hosted device that is attached to that microscope 'cause we don't really want our multimillion dollar microscopes being accessible to the outside world. So we brought the GPUs and we brought the cloud to
the microscope in this case. Now, I could probably
talk about this diagram all day on this sort of thing, but I think it would be better and easier just to show it in action. So let's go ahead and
we will hold our breath and hope this works and we'll
flip over to the system. So this is our home dashboard. This is the central
interface, the first interface that scientists will see. And we can see that we have
a couple different panels. We're using a calendar app, that panel that Kevin really enjoys 'cause he can tell whether his students are actually doing work or not and if they're in the lab or not based off of one data appears. On the other side, the left hand side, we have our model management panel. This is where we can spin up
a variety of different models. I've already marked a favorite for today. And we're going to look
at some TRISO particles and I'll explain what
those are in just a moment. We're gonna, again, hold our breath and we're going to click
the Start Actor button. This brings out a drawer that has all those machine
learning model parameters that allows you to tune
and fine tune the inference that's occurring on the system while you're running your microscope. But we're just gonna use the defaults and we're gonna hit start. And this is going to unpack that model, load it onto the GPU that is
sitting right here hopefully, and it will then spin up. So it's initializing
it, it's unpacking it, it's getting it ready
and spun up to do it. We're now idle and we're ready to go and we can do some experiments. Now, we didn't bring our $2 million transmission electron microscope with us. They wouldn't let us
have it through security. So instead, we're going to use some images that we'll use in sort of
approximation for that. And what I'm gonna do is now we've into our acquisition panel, and here's where we're gonna
be able to capture some images and we are going to do some
real time image analysis on these TRISO particles. So these TRISO particles are, if you're familiar with the
US candy, the Gobstoppers, there are sort of inner
layers of them, right? And what we want to know is the uniformity of each of these particles. And we've collected, in this
case, we have about 10 images, but in reality, you
probably have thousands if not tens of thousands of
images of these particles. And normally, you would
have to draw the circle around each layer and
then measure those layers and then decide is this a
circular particle or not? If it's not circular, we
want to reject that batch of particles. So we have that set up. I'm going to move this field of view so that we can say that we
want to look at just the part that is in the center here and not grab the rest of the stuff. Takes me just a moment to
do this with a track pad. And we're gonna go ahead
and we are gonna start some acquisition. So it's gonna go in progress
and in just a moment, with luck on the right hand side, we started our very first inference and we're running through those images. Now, I'm gonna sort of say,
okay, let's move around and let's see and look
at some other particles while we're doing this, right? And this is just going
through Preview on an Apple. We can see in the other side there that we are clicking through and it's doing that analysis in real time. So we just have to use our
imagination a little bit that this would be on the microscope as it's being connected to this ion beam, where they're simulating
a fusion power system to power the next
generation of data centers that's ultimately going to
literally and figuratively power Grafana in the future, right? So we're gonna go through and
do a couple different ones as we sort of scan through these images. This is just to give us some preloading for some other things
that we're gonna see here in just a moment. So I've loaded up those. We can see this one's a little oblong. We can see that as humans,
but what we can also do is, well, we can zoom in, but we can scroll down and I
have this uniformity chart. And this uniformity chart is if it was a perfectly
circular particle, each one of those layers
would be a perfectly flat line across the pot. So this allows the user,
this allows the scientists to immediately see, "Hey, is this a a good
particle or a bad particle?" But we also have on the
other side some stat panels that show the standard deviation. And so we can turn those into metrics that will identify then and aggregate if this is a good sample or
a bad sample in all of this. On the left hand side, we
have our different layers. This is just sort of the
performance of the model, how confident it is it was
able to find those model, those layers. And we can go through the
system and look at that. And so what we can also
do is we can zoom in, we can do some further analysis, and we can do that further analysis by going to what we call
the examine dashboard. And now the examine dashboard,
if this also hopefully works, will give us the same kind of information. But for those of us that are old enough, this is like our VCR. You can scroll through in time,
you can go back in images, and you can go forward in images like we were doing it
during the acquisition. That panel doesn't seem
to wanna be working. It's a little shy today. So that's fine. We'll go back over to
our acquisition panel. And what we can see here is we still have this uniformity chart. And what I'm gonna do is we'll go in and we'll take a look at what's going on, how are we calculating
these uniformity plots? And what we're doing
actually is we're running, something that doesn't look like prom QL or a SQL or something. We're yearning this notebook. We're running a Jupyter Notebook, right? And how are we doing that? Well, in fact, we have
Jupyter running on the system and every time the dashboard updates, we are running through
this Jupyter Notebook that a graduate student wrote to create that uniformity plot. This is then in a language that the scientists are
at least familiar with and they can download these and they can upload them to the system, but it's running this
code every single time within this panel giving
us this uniformity. And this is what allows the scientists to create whatever kind of metrics, whatever kind of plots they wanna have during the experiments while
they're on the microscope. But we can also do some other
things with this, right? 'Cause the way Jupyter is working and the way it's hosted on the system is yes, we can do it with notebooks and we can also use dashboard variables. We can pass those to the notebooks, but because of the way it's working, we can actually do this and we can put, as an example, we can put,
if I can scroll again, the Python code directly
into the dashboard. So we are running this live on the system and we can make some changes. If I don't like the parabola, we can go ahead and we can
make, oops, if I could type, we can go ahead and make that change. And we can do that as we
are doing the experiment. And we can copy and paste snippets of code from other notebooks or
from other researchers or from other collaborators and we can make these changes in real time while we're running the experiment. And like I said, we also had
this tied to various variables or we can create these other
variables in the system as we're running them, right? So we can do these things in
all of this different way. And we're able to create
these custom code snippets and run the code live
within inside the dashboard in an environment that the
scientists are familiar with, given that they're developing these models that they wanna host and
deploy at the microscope to ultimately make their discovery determine if it's a good
material or bad material for a fusion power plant and/or
win the Nobel Prize, right? That's the dream. So we go ahead and I'm
gonna stop the acquisition and we will go back now
to the presentation. Great. So what we saw there is the
whole thing working together in real time on the
microscope at this point. So the question's gonna be
how did we put this together and where do we go with this from here? Right? And this is going to be
the very first question which we always get, which is, "Okay, why'd you do this with Grafana? Why'd you pick it?" And we picked it for a variety
of very good reasons, right? One is the data sources, right? There's a whole community of them. They're open, they're available that also helps with this big tent thing because that's the
interoperability that we have that allows us to connect to a variety of different microscopes and experiments and customize our dashboards. The very first iteration of
this entire code and application that I showed Kevin was, the
very first feature request was, I want a dashboard where
I can change things and move things around and
have them for different things. And I was like, "Okay,
we're gonna go with Grafana because I don't wanna
have to create all that." And we get all of this for
free in a sense by doing that. And the other nice thing is
that we have some great panels and visualizations that we can use. The documentation for creating
your own visualizations and data sources and plugins is fantastic. And that has really
helped us to develop this. And then also there's
this vibrant ecosystem of all the people here
and around the world, putting this all together for us and helping us out in doing this. Also, Grafana is awesome, right? We're all here, it's awesome. But is it RAD? I'm going back to the 1980s, right? But RAD in the sense of can it be used to do irradiated materials
characterization. And also, can it be used as a rapid application
development environment? Well, we already have seen something that is somewhat similar in that we have an interactive notebook centric development environment that's pretty ubiquitous among the ML and the science community
that rapidly ingest, explores, and visualizes code and/or data. Well, that's interesting
because that's also what Grafana and the Observability stack does. So in actuality though, spoiler alert, yes we can make Grafana RAD because we just saw the demo doing that and we wouldn't be standing up here if we couldn't do that, right? But how did we get to making it RAD? And it starts with the anatomy of a panel. So I sat down one day
and I was thinking like, "Okay, how does this all get put together? How does this all work in a sense?" And if you look at this and squint at it, you can sort of see the backwards
G of the Grafana in there. In the flow, you go from your data source to the query editor,
you're creating data frames and you're gonna use the transforms. Then you have your options and they ultimately get
put up into the view inside of a panel. So using that, what we have really is that your query is your selecting data. The transform is
converting it into a format that can then be customized by the options and that can then ultimately
be displayed inside the view. And if we focus in on those first two, what we have is we have our query and then we have our scripts
and those are transforms and the snippets respectively. And those were the code
is, but I'm sorry to say, scientists are never going to learn SQL. It is just not something that they can wrap their brains around. They're too busy operating
those microscopes and drawing boxes around black dots. So it's not Python. That's what they're learning. That's what they use. That's what all the notebooks are in. So what else is out there
that is small snippets of code that does some kind of
translation of maybe a request, pulls some data from a database,
and returns a response. And that's what got me thinking. And I was like, "Well, maybe we could use
something like Lambda from AWS, which runs Python and JavaScript." But can we do that on the device? Can we have a similar kind of
thing running small snippets of Python code in an
environment that's familiar to scientists and engineers? And yes, we can. And that's what this Jupyter
flow we're calling here. And this is what was running on the demo. You start off with your Jupyter server, we had our Jupyter Lab, which
is the web interface for that. But we've created a data source that passes Python code from
Jupyter Lab into the server, then comes back out. But we can also go the other direction. We can go from our query editor, which we saw with the inline code and we can pass that back to the server. This allows us to create some
pretty crazy things to do with the the kernels and the various Jupyter Notebooks running. And we can do things like pass the dashboard
variables between them, but we're entering the Jupyter flow into and integrating it into the Grafana flow of that panel, right? We're going from the query editor to the transforms, options, and view. But what this makes it happen
is the Jupyter Notebook becomes the data source, right? It becomes that part
that is translating it from one to the other. And we can do some, like I said, some pretty interesting
and kind of crazy things. We can run the code directly in there. The scientists can make the changes, they can see it happen immediately. They get that interactivity and
that feedback in the system. But they also then have the ability to install the entire Python ecosystem 'cause we are also handling the magic keys with the percent sign there. So we're doing a pip install
here just of time zones because we needed to do that in order to do the the sign there. But we also now provide a rapid application
development environment for scientists and engineers in nuclear materials characterization or irradiated materials
characterization, right? So Grafana is RAD. It is awesome, it is RAD, and we're able to create
these custom workflows and have them run on a deployable system that's easy for scientists
and engineers to use. And then also share ultimately
all this information to get us to fusion energy
to power the next generation of data centers. So what we hopefully have
done is convince everyone here that these three
seemingly disparate things are actually interwoven together. That we have also done that by using, and we have our Golden Grot there 'cause we were the 2024
Golden Grot winner, of the beautiful dashboard. And that dashboard was generated
by using this exact system. So there's the sort of
plugin for that situation, but in the center is this Theiascope that is connecting the fusion
energy and the AI/ML together. And on top of all of
that is the Grafana stack integrated with a Jupyter
Notebook interface. So with that, we'd like to acknowledge and thank some of our collaborators and our funding agencies, specifically the Department of
Energy in the United States. But the images that you
saw of the TRISO particles came from Oak Ridge National Lab. Some of the models that we use and everything come from Wisconsin. And then Idaho National Lab
and Argonne National Lab are both collaborators that
have let us deploy the system in their multimillion dollar microscopes in the very early stage
of the system and device. And with that, yeah, thank you. - [Kevin] Thank you. (crowd applauding)

