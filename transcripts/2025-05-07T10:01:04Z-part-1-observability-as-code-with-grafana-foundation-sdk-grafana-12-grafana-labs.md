# Part 1: Observability as Code with Grafana Foundation SDK | Grafana 12 | Grafana Labs

Compose dashboards from code and manage changes without managing complex JSON or using Grafana UI. With the ...

Published on 2025-05-07T10:01:04Z

URL: https://www.youtube.com/watch?v=_OKQoABmg0Q

Transcript: Hi, I'm Tom, one of the senior developer
advocates here at Grafana Labs, and in this quick video I'm going to be
introducing you to dashboards as code with Grafana. Dashboards in Grafana are typically
composed of a JSON configuration file. This makes up all of the
rows panels, data sources, and queries that make up
your actual dashboard. But when you want to
manage these at scale, it can become difficult or complex to
manage these JSON configuration files or just to modify your dashboards
within the Grafana UI. So there's another way to do this,
and this is using dashboards as code. A solution to this is the
Grafana Foundation SDK, the Grafana Foundation SDK is a set of
libraries that allow you to write your dashboards as strongly typed code. You can then check this into
a repository such as GitHub, and then provision these directly into
your Grafana instance using something like a GitHub action.
In this quick video, I'm going to be showing you how you can
use the Grafana Foundation SDK to write your first dashboard as code and
then import it into Grafana directly. Before we take a look at any code, I want to point out the Grafana Foundation
SDK has its own set of documentation, which you can find directly
on the GitHub page, or you can find it in
the description below. This documentation portal covers all of
the languages that the foundation SDK supports, such as Go Java,
PHP, Python, and Typescript, as well as a bunch of examples
to help you get started. Let's switch over to VS code and
take a look at how we can use the Foundation SDK to
generate a simple dashboard. Here you can see I'm using Go, so therefore I'm using the
Foundation SDK's Go Library. Inside my main func, I'm creating a reference to the data
source that I want to use within this dashboard. Your dashboard
may have multiple data
sources, however, in my case, I'm just going to use
the test data source. So I'll set up a reference to that
Here at the top. Underneath that, I'm going to use the dashboard builder
that comes as part of the Foundation SDK, to create a new dashboard
with a title of my dashboard. Inside this dashboard,
I'm going to have a panel, and you can see here that I'm using a
stat panel. I'll use the builder here, which you can find references to within
the Foundation SDK documentation. And I'm going to give
it a title of version. I'm going to use the test data source
that we defined at the top there, and then I'm going to pass in some options
here for how we're going to grab the data for this stat panel. And finally, I'll pass in a target function here.
This will then use a data query builder on that test data
source. And for this, I'm going to use the CSV content scenario, and I'm going to pass in some CSV
content here, just static data, just for an example purpose.
For all of the functions here, you can find references for them and
what they do in the Foundation SDK documentation. Alternatively, you can create a dashboard directly
within Grafana and take a look at the JSON configuration for that dashboard. The property names there will map directly
to functions within the Foundation SDK. The next thing I'm
going to add is a new panel. This time we're going to
be a time series panel. We're using the time series
panel builder for this. I'm going to give it a title
of random time series. Again, we're using that test data reference, and then we're going to pass in the query
builder for this test data. And here we're just going to pass the random walk
scenario ID in just to give us a random time series graph there. The final thing we're going to do is
called the builder's build function. This is then going to output the JSON
that we're going to use to import into Grafana. I'm going to serialize
this out to a JSON string, and then I'm going to print
it out to the console. So what does this look like in practice? So if I come over to the terminal
here and I run this go run main.go, you'll see that we get an
outputted JSON payload. This is the dashboard itself. So I'm going to copy this and I'm going
to come over to our Grafana instance here, and I'm going to
create a new dashboard. I'm going to press the
import dashboard button. I'm going to come down to the JSON input
field here and paste in the output from our Foundation SDK code.
Then I'm going to press load, give it a name and press import. And you'll see here now that we have
our dashboard that we generated from strongly typed code, we have the stat panel with the content
here that we specified in our code. And then we have the random
time series graph here. So that was a super quick
introduction to the Foundation SDK, and how you can use it to write
strongly typed code and convert it into dashboard JSON configuration
files that Grafana can understand. You can find all of the code for this
example in the GitHub repository linked below. In the next video, we'll look at a more complicated
example and show you how you can use the Grafana HTTP API, to automatically import your dashboards
directly into your Grafana instance. Thanks for watching, and
I'll see you in the next one.

