# Introduction to Frontend Observability in Grafana Cloud (Demo) | Grafana

In this video, we offer an overview and demo of Grafana Cloud Frontend Observability, our real user monitoring (RUM) solution ...

Published on 2024-08-26T15:28:09Z

URL: https://www.youtube.com/watch?v=TZVUnCWyv0Y

Transcript: Hi, my name is Cedric Ziel. I'm a
product manager here at Grafana Labs. In this video, we'll discuss
frontend observability, our managed real user monitoring
solution in Grafana Cloud. One of the biggest challenges
observability teams are
facing today is achieving deep end-to-end visibility
into cloud native applications. Those often include
modern browser frontend, which are becoming increasingly complex. Without visibility into your
frontend apps, traditional websites, web apps, or micro frontend, we might be creating poor experiences
for our users potentially, if we don't know what the end
users are actually experiencing. I'm very excited to introduce you to
Frontend Observability in Grafana Cloud. Frontend Observability gives operators
an immediate understanding of their end users experience by measuring
the performance of the
frontend based on industry standard KPIs, it allows operators to aggregate
triage and prioritize front-end errors, and provides an end-to-end view of every
single transaction when combined with OpenTelemetry's well-established
distributed tracing. Let's take a look at how we
can use front-end observability
to find problems in my application. Here's
my overview dashboard. It is showing the performance of
the app based on core web vitals, including metrics like the time to
first bite and cumulative layout shift. These web vitals are industry standards
and important gauges of the perceived end user experience. We can also directly understand other
critical information like the ratio of overall page interactions to error ratio. We have a breakdown of the
KPIs by page and the P 75 development of the KPIs over
time, including response times. Looking at the overall errors, I get a top down view of
all my frontend arrows, which have been automatically
aggregated and ranked by the number of occurrences. Here's a number of arrows
related to the product detail page. When I click here, I come to a detailed page for that
particular page that aggregates all the KPIs, and here I can select all the errors
that are related to that particular page. Let's zoom in on that bad
request error to learn more. This detailed error view provides a lot
of specific information about the error, including the app and browser
version page URL as well as the stack trace frontend observability
automatically catches these, makes them readable by using source
maps that are created when the apps are built. I can also directly link from this error
to the user session to find out how this error came about in
this session detail view. I'll get the full picture with all my
browser related KPIs for this particular session, revealing the sequence of actions
leading up to this error On the session detail view, I have access to a detailed breakdown
of the page navigation timings for individual page loads. These can help me understand where the
requests spend time and what might be contributing to high latency. Let's take a closer look at the
events that comprise the user session, such as the initial load,
custom events like change, quantity and add to card, but also our failing
HTTP request right here. For HTTP requests, we also record distributed traces
and we have access to them. From right here, A distributed trace view shows the timings
of both the front end and server side calls. This is great for
establishing fault domain isolation. Just by looking at this, we can
visually determine the root cause. Investigating the spans related
to the Faroshop backend service, we find that the product
repository is the root cause of the error in this trace.
When expanding the span, we can see the exact
exception recorded as span event. We get a full stack trace that
includes the backend side exception, a database connection exception.
This is a severe issue, but thanks to the tight integration
between APM and real user monitoring in Grafana Cloud, we are now aware of it and can investigate
why the connection is failing for that particular endpoint. front-end observability data is stored
in Grafana Cloud logs and cloud traces, both highly scalable and centralized
solutions, brought to you by Grafana Labs. To get started, sign up for a free Grafana Cloud account
today and start monitoring your web apps to empower your teams with
end-to-end visibility across the stack.

