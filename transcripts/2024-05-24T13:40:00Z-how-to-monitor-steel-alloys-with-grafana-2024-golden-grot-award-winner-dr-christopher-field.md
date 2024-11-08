# How to Monitor Steel Alloys with Grafana | 2024 Golden Grot Award Winner: Dr. Christopher Field

Meet Dr. Christopher Field, our 2024 Golden Grot award winner in the professional category. Dr. Field is the Co-founder and ...

Published on 2024-05-24T13:40:00Z

URL: https://www.youtube.com/watch?v=HQWxLBROMnQ

Transcript: And Golden Grot winner for
the professional category
is Christopher Field from Theia Scientific. My name is Dr. Christopher Field.
I am the principal developer, original developer, co-founder, president,
chief barista for Theia Scientific. Yeah, so we use the Grafana dashboards
in Theia Scientific's main application. It is our primary user interface. Our users and our customers interact with
our software and with their models all inside of Grafana. What we're looking at is a material
that has been irradiated in a nuclear reactor, so it has been damaged
by radiation under various temperatures, pressures, maybe different alloys of
those different materials. And the scientists will sit there and
draw boxes or outlines around all the different black dots
they see in this image. And they will then quantify or count
all those black dots and they'll measure them and give 'em a size, a
diameter and so on and so forth. And this has all been a workflow that
has been operated manually over the last couple of decades since the
really digitization of all this. They've been doing it even before then, back when they were doing x-rays
on film and that kind of thing. So the dashboard is showing
the quantification that has occurred automatically, that is running the AI model
and drawing the outlines, but also the drawing the ruler and
getting the scale bars and measuring the different sizes and
morphology of those black dots, and then ranking them and
then showing, sort of, the confidence that the model has
in the identification of that, but also showing the
distribution of those materials. The problem we were trying to solve
was - Kevin is the co-founder. He's my brother. He's
also a nuclear scientist. He has spent a decade drawing
boxes around black dots by hand for thousands, if not hundreds of
thousands of images at this point. He never wants to do that again. And so we set out to fundamentally
change the workflow for scientists and engineers that are looking at these
materials and looking at these images. I wrote some software. I showed it to
my brother and he said, "I want that. I want that now, but I also want to change everything and
anything at any moment in time." So I sat down and said, I don't want to have to write an entire
customizable dashboard observation, observability platform for him. So I went online and I looked to
see what is out there for that, that could answer that question. And Grafana came up as
the best option for that. The examined dashboard is specifically
looking at a deep dive into the data that has been collected that
you can do at the microscope, but you can also do back at your
office, you could do it on your couch, you could do it on your
phone - sort of situation. And before us and before
using that dashboard, they would just take snapshots and they
would take an image once every minute, two minutes, whatever, or they're sitting there watching it for
that amount of time and they say, "Oh, that looks interesting. Let's take a picture." And then they'll
look at it afterwards and they don't even know if that's actually a real
thing or if that was a good sample or a bad sample or if that was something
that was of interest until they go back and look at it. What we've been able to do now is
they can do this analysis and decide, "Is that a good material while it's
still running?" And we can see the trends occur over time, whereas before it could be a year and a
half to two years before they can make that discovery. And that's
really been the part that's been the aha moment when
the microscopists see it or we demo it, they're just like, "Oh, I can
do this now?!" I don't have to wait. We had one occasion, we were talking with somebody where they
had collected a year and a half worth of data and they found out at the
very end that it was the wrong data. And if they had our system, they would've been known that on day
one and they could have just retaken the sample. . What does
it mean to win this award? What it means is it validates
the original concept that we had of this customization and the
visualization and using a web stack at a microscope. So it really sort of says
like we're onto something, but also that we sort of said, "Okay, Grafana is doing all of this with
observability and doing it in the IT side and this DevOps and, and monitoring your
web application." And we kind of said, "Let's do it for the observability
of science and does that apply? Does it actually translate and does
it work?" And this validates that yes. And that also that we are on, on the edge case of what Grafana
is used or outside that core, but it still works really
well. And then it also means that we just like, like this concept,
this weird idea that we had and like, "Can we do this?" It just validates
it. It also means that like, "Hey, we have something that's
award-winning!" .

