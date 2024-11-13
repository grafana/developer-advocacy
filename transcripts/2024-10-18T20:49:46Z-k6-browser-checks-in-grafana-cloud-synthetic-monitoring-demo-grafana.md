# k6 Browser Checks in Grafana Cloud Synthetic Monitoring | Demo | Grafana

In this demo video, Virginia Cepeda, senior software engineer at Grafana Labs, walks through the k6 browser checks feature in ...

Published on 2024-10-18T20:49:46Z

URL: https://www.youtube.com/watch?v=7TqmZqEtQdo

Transcript: Hello everyone. I'm very excited to introduce you to
the new k6 browser checks in synthetic monitoring, a fantastic new feature that's available
in public preview from Grafana Cloud starting October 2024. I'm Vika and I'm a software engineer
in the synthetics team here at Grafana Labs. So up until now, Grafana Cloud synthetic monitoring only
supported tests at the protocol level. Now using the power of k6
and the k6 browser module, you can create synthetic monitoring
tests that interact with the real browser environment. This means you can control a headless
chrome browser using a k6 script to gather insights on web vitals,
capture custom performance metrics, and simulate user actions like
clicking buttons or filling out forms. So how does it work?
Let's take a look now. We can create a new browser check by
following the same process as we do with other checks in synthetic monitoring. So now we have this new create browser
check button that we can click to get started. First, let's fill out
the job name and the instance, and the next step is to write the script
that we want to be executed on every test run. The check comes with an example script
that we can use as a starting point. We could also choose one of the
scripts from these examples list, or we can create one from scratch. So the script that we're
using here logs in to a site. It also adds an assertion to make sure
that the login works and it performs a few other interactions like creating
a new object in that site and then deleting it. This script is also
available in the documentation, so you might check it out there
a little if you're interested. And it's worth to mention that k6
browser tests are compatible with the playwright API. So if you
already know playwright, browser synthetics are
going to feel very familiar. And because browser
synthetics are powered by k6, this script can also run in
k6 command line interface, and you can also run
it in Grafana Cloud k6. Okay, so let's, let's continue
with the creation flow. Let's leave these fields in there, the
full values for this demo. And finally, let's choose the probe location
where want it to be run from. Let's now save it. And as you can see, setting up the checks is
pretty straightforward. Now we can analyze the results by
taking a look at the dashboard that was generated for us. So in this dashboard, you will find all the metrics you need
to assess your application's performance and user experience. So besides
uptime and reachability, we also display web vitals information
for page loading times, interactivity, and visual stability. We can also analyze the user journey
by checking out this new metrics by URL table where we display web vitals
information for each of the URLs that were accessed during the test. And just like for scripted checks, we display all the assertions
that were set in the test with all the information for that, the number
of testing targets, duration by probe, which in our case was just Paris,
information about data sent and received, and as well a list of logs. So to dive deeper into this new feature, be sure to check out our What's New blog
post and the official documentation on the Grafana docs site. You will find script examples and
detailed guidance to help you get started. So try that for yourself and see how
browser checks can enhance your monitoring capabilities. Thanks for watching.

