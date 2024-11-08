# Creating Great User Experiences | Synthetics, Load Testing, RUM Demos | ObservabilityCON 2024

Learn how you can monitor and improve user experience with three key tools from Grafana Labs: Frontend Observability for ...

Published on 2024-10-24T19:52:21Z

URL: https://www.youtube.com/watch?v=UfUsRXh0UTo

Transcript: Hey, welcome everyone to
understanding the user experience. So I'm Peter Schretlen. I'm an
engineering manager at Grafana Labs. I work on the synthetic monitoring
squad and I'm based in Toronto. Hello everyone. I'm Vika. I work also in the synthetic squad as
a frontend engineer and I'm based in Argentina. My name is Marcelo. Hello everyone. I'm also a software engineer in
the synthetic monitoring squad. And I come from Costa Rica. Okay, we're gonna start off today
with a question and a show of hands. How many folks here have heard
of web vitals, core web vitals? Maybe you've seen reports that look like
these ones somewhere on the web. Okay, I see a few hands going up. For those of you who aren't
familiar with web vitals, they're these signals that you can
collect on a webpage that tell you the quality of the user
experience you're gonna have. There's three that got talked about
a lot. These are core web vitals. And you can see them
here on these reports. So there's one for page loading time,
which is largest Contentful paint. There's one for interactivity
interaction to next paint, and there's one for visual
stability, cumulative layout shift. So these three signals among many other
web vitals suggest you're gonna have a much better experience
visiting the site on the left. Some of you may be familiar with it. You may have heard of grafana.com
compared to the site on the right, which has a lot more orange and red. Now, the site on the right
happens to be one. I, I've obscured the name
to protect the innocent, but it's one that I worked
on a couple of years ago. And this is what it looked like before
a performance optimization effort that lasted six months. And this is also what it looked like after
that performance optimization effort. That lasted about six months. So this can be quite a difficult problem
making the user experience better. And I'll tell you three
lessons that I learned from, from this experience
working on this site. The, the first is these web
vital signals very useful, but they're also extremely broad. So there's a ton of things
that can influence them. And especially as your site gets
more complex, you add more features, introduce more dependencies,
integrate more third party tools, it could be really hard to understand
what's making these web vitals degrade. It can be even harder to figure
out how do I make them better? How do I get them back to where they
were? So that's the first lesson. The second lesson is that
these web vital signals, again, useful as they are only capture
one part of the user experience. You go to a site, there's a
bunch of a bunch of interactions. You're doing many different
pages, you're visiting there, there's a flow and a journey
that you're going through, and that's not captured by
these single page page metrics. That whole flow has to work well
for the user experience to be great. So we can't just rely on web vitals alone. And the third experience or the third, the third lesson is the experience
that I had wasn't very successful, but it didn't have to be that way. And
it doesn't have to be that way for you. If you take on a similar
project with Grafana Labs, there's tools that you can use and
approaches that you can take to go from a an okay web experience
to win. That's fantastic. And that's what this
session is about today. So today you're gonna see three tools, and I'd like you to think about them
as three slices of Swiss cheese. So you take these three slices, you
bring them together and then combine. They compliment each other so there's no
holes for the user experience problems to get through. The first slice of cheese you're
gonna see is front end observability. This tells you what's going on in
the wild. What are my user journeys? How are they performing, how
often are they happening? The second slice of cheese you're
gonna see is Grafana Cloud k6. This gives you lab data that you can
compare to your, your data in the wild. So you can take a user journey, recreate
it in a lab environment and test under, under different scenarios, some of
which you may be seeing in production, others you may have
never have seen before. And that way you can get confidence that
when you deploy a production, you've, you've covered all your bases. And the third slice of Swiss cheese
we're gonna look at is Grafana Cloud Synthetic monitoring. This lets you take critical
aspects of the user experience and continuously monitor them in
production. So if they change, you'll know right away
'cause it'll get an alert. So we're gonna use these three tools
together and to really understand what's going on, we're gonna set the stage by
looking at, at a poor user experience. So if we switch over to
the video, this is a, a recording I captured the other
day of the Open Telemetry demo, and I open the web, the homepage,
where's my banner image? That loaded a little slowly. I'm
gonna click on a product here. Where's the product image? There?
It's, I'm gonna click add to cart, nothing's gonna happen. Boom,
I see an empty cart. Oh, then the product's there and I'm
gonna click the place order button. And again, nothing happens for a second.
And then I get the order confirmation. So very, very short recording.
But even that short time, you can see that there's a
couple of things there off. The images are loading slowly, you add to cart and the order
button are a little laggy. So to help us understand what's
going on, I will pass it over to ika. Thank you, Peter. Okay, so let's explore what's going on by
describing a few tools that we can use. So first, let's talk about
front end observability. So with frontend observability, we can measure and report on where
vital information such as speech, loading times interactivity, and visual stability in order to
provide the best experience that we can. It gives us an end-to-end view into real
user interactions with our application front end. And it also lets us aggregate triage
and prioritize on errors for faster troubleshooting. So thanks
to recent developments. Now it's pretty easy to also go from
front end to backend transactions by leveraging user sessions
and trace identifiers. So now if we click on this new services
button that is linked to a page id, it'll take us to Grafana Cloud
application of observability. So here we can take a look at all the
backend traces that are related to a user session. And as here we can inspect in particular
where the times are spent and the different interactions that are front
end makes with our backend services. So going back to Peter's user journey
we could see there that there were two main issues, right? So the images were pretty slow to load
the banner and the product didn't show correctly, like it took
some some time to load. And also adding to cart was pretty laggy. So let's try to investigate a bit
further to see what's going on and in particular to find out where to
focus when creating a fix for this. So let's play the video now. And the first thing that we can do is
we can go to the main page of frontend observability. Here we can take a look
at the web vital section in particular. Let's look at the LCP value, which
is showing it's taking three seconds. This seems pretty high and it's probably
related to the slow loading images. Now let's take a look at his session
here among all the information that we have. And we can take a
look at the page load event. This shows us the different times that
are spent in the faces of loading and rendering the app, but nothing
really jumping out here, which indicates that the page
document is loading fine. But let's investigate a little, a little bit further by now
inspecting the traces for the, the services and the resources
that we're interested, like the banner in particular, we
can see that it's loading correctly. We have a 200 status code, but
let's look at at the traces for it. So let's click this button and this will take us to
application observability. So here, if we inspect the traces, we can see that it's taking almost two
and a half seconds to allow this image and seems like a pretty high number,
right? Just for, for one image. So we know that we might want
to improve this with our fix. Let's do something similar.
Now by searching for the cart, we get more information about how much
time it takes and what's going on with it. So let's inspect the
traces for it as well. And here we can see it's
taking well two six seconds in total. And in particular the add
item operation from the cart service. And they get cart operation. Also from the cart service
are taking 1.3 seconds each, which seems like a high time if we add
them up, like we get this total time. So we might also want to
improve this in order to, to get the experience a little bit better. So frontend observability is
telling us what users are seeing, but it will it will be great
to be able to replicate what we see and experiment with changes
to see that the fix that we actually work on actually works before
deploying it to production. So with this in mind
now let's talk about k6. So k6 is a very versatile
tool for creating load and
performance tests. With it, you can write tests in JavaScript and run
them in the command line or in Grafana Cloud k6. And you can also integrate them
with CI/CD to have a great development experience. So what k6 does is it create allows
you to create realistic tests in a controlled lab environment so that you
can replicate issues that you have seen in production, like the
ones we saw today just now, or you can prepare for situations
that you haven't encountered yet. And it also integrates with
Grafana Cloud logs, metrics, and traces so that you can correlate
testing and observability data in a very simple manner. And recently we also added support
for creating performance tests in the browser. So these tests are great for measuring
user experience and finding issues that are difficult to catch
at the protocol level. They never  the k6 browser
testing APIs and allow you to interact with your obligation front end in order
to find and fix performance issues. And with this we also
added new two new features, which are the browser timeline
and the browser screenshots, which allow you to see in more detail
what happens during each of the steps of the test. And also easy access to
view and download images from it. And there is also the new
browser recording extension. This extension is great for creating
browser tests without the actual need to write them because it creates for us. So it is available for Chrome and what
it does is it records all the browser interactions that you make,
such as clicks and navigations, and at the end it creates a script
for you that you can use to create a performance test in k6. So let's go back to our demo. We already identified which ones
were the main issues and we created a fix for it. But now let's try to recreate
it first by recording the same interaction using
the browser extension. We are gonna do the same steps as before. And when we're done recording we're going
to copy the script that is generated for us here. And with this we're going to create
a performance test in Grafana Cloud. So let's run this test. And the first thing that we can see is
that the LCP value is now down to one second before it was three,
which is a good sign. Now if we inspect the browser timeline
here we can get information about each of each of the steps of the
test and how much time it takes, and we can also inspect each of the
iterations that were executed during this test run. So in a similar way, we can also take a look at the screenshots
that were generated for this test so we can see what happened during each
step so we can get a visual clue of that. But now let's, let's inspect
the browser metrics stuff here. We can search for the resources that
we're interested, like the banner. So let's, let's filter by that in this field
to get a look of how much time it's taken. So now it seems like it's taking 93
milliseconds to load when before it was almost three seconds. Let's do something similar by
filtering by the cart URL here to get an idea of how much time it's taking. Now it says it's taking
one second in average. So this also looks like an improvement, but in order to get even more confidence, we can create a comparison
between a test that was run before the fix and this current
results. So let's do that. Now we can compare in this visualization. The LCP value in the dash
yellow line is before the fix. And in the solid yellow line
is the values after the fix. So we can see that it
works in a consistent way. And finally we can go back to frontend
observability where we can click this k6 browser button to compare data from
the real world with our test data. So this is giving us the confidence to
know that our fix works so we can deploy to production and, and be sure that
it's actually actually an improvement, but it would be great to be able to
prevent this from happening in the future. So now let's ask Marcelo to
show us how we can do that. Thank you Vika. To recap, what we have done so far is we have
set up Frontend Observability so that we know what our actual
users are experiencing in
the, in the, in the website. We have also set up performance
testing using k6 so that we know that the site can take it. And what happens if a bug
goes undetected and gets released into production?
When will we know about that? That is the job of Synthetic Monitoring, basically telling our users something
is wrong, we're working on it, we're going to fix it.
With Synthetic Monitoring, you can continuously monitor
your targets or services for multiple locations around the world.
We have different types of checks. Probable checks are the first
line of defense In this strategy. We have the DNS check. Basically the question is
are the DNS servers up and responding because it's always DNS. So the second step is what about
the path to our network? For that, we have the ping TCP
and trace route checks. And last we can send out simple HTTP request to verify that the HTTP servers
are responding as suspected as well. Between these types of checks, we have enough basic coverage to figure
out if everything is going as suspected, if everything is going well.
For more complex interactions. For example, if we, if you need to send out multiple requests
inside a single synthetic monitoring check, we have a check that
we call multi HTTP. Basically, you can set up the multiple
steps, collect metrics, and log along each of them and
capture the output of each step to use at any layer later,
later point in the test. This is built using the same
technology that powers k6, the thing that we have
been talking about here, but without requiring the
users to write actual scripts, this allows us to deploy with
confidence and basically monitor that our interactions in the
websites are going as suspected. But if you think back to
what Vika was describing, what we have there is a complex
API that might require custom retry logic and where we, where we might need to
simulate interactions are more complicated than what
multi HTTP can handle. For that, we are thrilled to announce scripted
checks. Basically these are k6 scripts that can be used as for synthetic
monitoring purposes. With this, you can leverage the familiar JavaScript
language and the power of k6 in order to create highly customized
synthetic monitoring solutions. In order to author these scripts, you can use the tools of the convention
like the recorder or maybe k6 Studio as mentioned in the keynote. Building on top of that synthetic
monitor will soon have a browser check type. It's the same kind
of technology that Vika showed, so we can use the same script
that she was, she was showing us. But for synthetic monitoring, meaning we can continuously
monitor our services from browsers, not from just the scripts, and we can collect the
metrics and data obtain directly from browsers. If you think back to what Peter was
talking about at the beginning of the presentation with vitals, they present, they provide us with
interesting information, useful information about the
performance of our services. So synthetic monitoring scripts will
have access to that information. As an example, you can set up a a check, a validation where you look
at the LCP metric and if it ever goes beyond a particular
threshold, you will, you can set up an alert for that. Going back to our demo, remember that we had issues with panel
loading and the behavior of the cart. So because have fixed that and
we, we can do something to, to make sure that it stays like
that. The first thing is the banner. Since that should be fast, we're going to set up an HTTP check that
is going to have a low threshold and we will set up alerting with
a high sensitivity so that
we're notified if it ever changes that behavior.
For the case of the card, it's a little bit more involved. For
that, we might need a scripted check. Remember that we need to
set up the session id, we need to fetch a card and we
need to add something to the cart. If you look at the script that
is displayed on the screen, you can see those parts create the
session ID after the cart fetch a cart. We're also showing that you can set up
thresholds at that level so that if for, in this example, if the request
goes above 600 milliseconds, the test will fail. So if we
look at the data as deployed, you can see that for
the image loading test, things in the United States are
behaving better. But in Amsterdam, our test has come to, has come close to trigger an alert at
least three times in the recent past. For the car ttest, you can see that
it's been failing most of the time. But if we go look at the time series data
that we have gathered using Synthetic Monitoring, you can see that it's
been trending in the right direction. So we actually have a fix. So what we have presented in this talk
is three different tools that can be used as a standalone tools
or in tandem with each other. The first one that we represented
is Frontend Observability
so that we know what the actual experiences of real users is. The second one is k6 that we can
use to do performance testing and we can deploy with confidence
that the services will stay up because shopping season is around the corner. And the last one is synthetic
monitoring that allows us to monitor services in a continuous manner so
that we can inform our users of issues instead of the other way
around. But at Grafana Labs, the story doesn't end there. We're at, we're continuously working on all these
three products in order to deliver improvements so that you
can benefit from them. That is our presentation. We
thank you for your attention.

