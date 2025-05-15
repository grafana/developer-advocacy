# Part 2: Observability as Code with Grafana Foundation SDK | Grafana 12 | Grafana Labs

This is part 2 of the Grafana 12 Observability as Code Foundation SDK video. In this video, Tom Glenn provides an overview of ...

Published on 2025-05-07T10:00:54Z

URL: https://www.youtube.com/watch?v=ZjWdGVsrCiQ

Transcript: Hi, I'm Tom, one of the senior developer
advocates here at Grafana Labs, and in the last video we took a look
at how you could get started with the Grafana Foundation SDK for writing
your dashboards as code. In this video, we are going to take a look at a more
complex example that uses a slightly more realistic dashboard as well as a
process for automatically deploying your dashboard into your Grafana
instance. So let's get started. Inside of VS code here, I've opened up the generate and deploy
example within our intro to Foundation SDK repository. You can find a link
to that in the description below. This example is a bit more of a real
world scenario whereby we have a web application which is instrumented
with metrics and logs, and then we're using K6 to
fire web requests at that
to generate some background data. Then we're using the Foundation
SDK to generate a dashboard for this web application and then
automatically deploy that to our Grafana instance using the Grafana HTTP API. So let's quickly dive through the main.go
file and show you what's going on. We've got some Prometheus metrics
here for the total HTTP requests, and then also we have our
request duration in seconds, and then the rest of our code here
is basically setting up all of the instrumentation for the dummy web
application that we have running. So you can see that we're configuring our
Prometheus metrics and then we're also configuring our logger to output
logs to a temporary directory. Then we have some middleware here which
basically writes out the metrics and the logs for each endpoint that is
hit within the web application. And then we've got some handlers here
for a couple of endpoints. We have a health check endpoint, and
then we have a data endpoint, which just spits out some JSON. Then underneath this we
have our main function. You can see that I've created
this Deploy dashboard flag here, and what that means is that once we
run this application with that deployed dashboard flag, it's actually going to generate
the dashboard configuration
using the Foundation SDK, and it's going to deploy that to our
Grafana instance using the HTTP API. If that flag isn't passed, then it's going to spin up
the web application as normal, and we're going to handle all of those
various endpoints such as the health, the data, and also our
Prometheus metrics endpoint. So let's take a look at what the code
looks like for generating the dashboard for this web application. We'll
open up the dashboard, go file here, and you can see that I'm importing the
Foundation SDK here. The first function here is a simple helper function I've
created to get a variable value from our environment. This just means that we don't have to
check in secure information into our GitHub repository and allows us to
look up this information from the environment, which is
just good practice. Next, you'll see that we are setting
up some data source references. We've got a Prometheus
data source reference, and we also have a Loki
data source reference here, and you'll notice that that is similar
to what we did in the getting started with our test data reference. Below this, we have the generate and
publish dashboard function. We're using very similar functionality
as we did in our getting started, and we're effectively using the dashboard
builder to create a new dashboard. We're going to give it a UID so that
it has a static UID that we know, and then we're going to assign some tags
to this dashboard. So you can see I'm assigning a tag of generated one
of Foundation SDK, and one of go. You can assign any tags that
you like to your dashboard. We're then going to set the refresh
time for this dashboard to be every five minutes, and we're going to give it a
default time range of the last hour, and we're also going to make sure that
we specify that the time zone for this is going to be the browsers time zone
itself. Next, we'll add a new role. We're going to call this overview, and inside of this we'll
add a time series panel, and we're going to pass in a Prometheus
data query here just to get the duration seconds for each of our web requests. Then next we're going to have a panel
for our average HTTP response times. Again, we're going to pass
in a Prometheus query here, and then below that we're going to have
two new panels. The first is we're going to have a logs panel, which
shows our web service logs. We're going to pass in a log QL query
here to get everything from the web service. And then underneath that we're also
going to have a dashboard service logs, which again is going to be a very
similar logs panel except this time we're going to look for logs
from our dashboard service. Once we've defined our dashboard
using strongly typed code, we're going to use the builder build
function to output that JS configuration. We're going to output
that as a Jason string, and then we're going to log this out
and we're going to call the persist dashboard function here. The purpose of the persist dashboard
function is to take that dashboard configuration and use the Grafana
HTTP client to push that into Grafana itself automatically. To do that, we're going to create the Grafana client
here. We're going to pass in our host as well as the base path and
whatever scheme we're using. You can see here that I'm using basic
authentication with the default admin, admin username and password, but you could use environment variables
to pass in your actual username and password here. Next, I'm going to check whether or not there
is a folder called provisioned folder. If there isn't, I'm going to
use the API to create one, and then I'm going to call the
post dashboard HTTP endpoint here, and I'm going to pass in the
dashboard configuration itself. I'm going to make sure that we put
it inside of that provisioned folder, and I'm going to specify overwrite as
true so that if any changes have been made to this dashboard, it's
automatically going to overwrite, so therefore we will have the most
up-to-date version every time we call this function.
And then finally, we're going to output the status of
whether or not this succeeded or failed to the logs. The last thing to look
at here is the Docker compose file. You can see that inside of this Docker
compose file, we're running Grafana, Prometheus, Loki and Alloy, as well as k6 to generate
some sample data. But then you can also see that
we have these two services here. We have our web server, which is simply running that main go
file to run the web server itself, and then we have the dashboard
generator service. Now, this is also going to
run that web application, but it's going to pass in that deployed
dashboard flag so that it builds the dashboard and then generates that and
pushes it into Grafana using the API. So let's run our Docker compose file
here by calling Docker Compose up. Now that our Docker
composes up and running, I quickly want to take a look
at add Docker dashboard here. You'll see that we have our
dashboard generator service, which isn't currently running, but that's fine because what this does
is generates the dashboard configuration js outputs it and persists
it to the Grafana instance, and then it immediately exits the process, and you can see here within the
logs we generating the dashboard, it outputs the dashboard, Jason,
and then it persists it to Grafana. You can see it says folder not found,
so it's going to create a new one, and then it says, dashboard
created successfully. Let's jump into our Grafana instance
now and take a look at what this looks like. If I refresh this page, you'll
see that we have a provisioned folder. Let's expand that, and you can see that I have our web
service dashboard here. You can also see that the tags Foundation SDK generated
and go that we assigned within our strongly type code are present. Let's open up the dashboard and you'll
see that we have all of the panels that we defined within our
dashboard dot Go file. We have our HTTP request per second, and you can see we're
getting some data here, which is because of the k6
script that we're executing. We also have our HT TP respond times as
well as both our web service logs and our dashboard logs. Let's go back into our code
now and make a quick change. I'm going to exit out
of this Docker compose, and then I'm going to come into
our dashboard. Go file here, and I'm going to scroll up to the
top and let's make a simple change. We'll add a new tag. I'm
going to call this one test, and then I'm also going to change the
title of the first panel to include the word edited in there. Let's run our
docker compose up command. Again, making sure to pass in the dash dash
build flag because we've made changes to our code. Now we'll head on over to our Grafana
instance and make sure those changes have appeared. If we refresh this
page and expand this folder, you can see that our web service
dashboard now has a new tag of tests, which we defined in our code, and
if I open up the dashboard itself, you can see that the title of our HTTP
request per second has been edited here. Hopefully, you can see how powerful
it is to write your dashboards, a strongly type code and be able to
automatically provision those into your Grafana instance using the Grafana
Foundation SDK. In the next video, we'll take a look at how we can use
GitHub actions to automatically deploy changes to our dashboard every time
we push new code to our repository. Thank you so much for watching,
and I'll see you in the next one.

