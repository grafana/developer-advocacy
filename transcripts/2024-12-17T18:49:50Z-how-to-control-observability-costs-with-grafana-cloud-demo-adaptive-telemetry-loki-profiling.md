# How to Control Observability Costs with Grafana Cloud | Demo | Adaptive Telemetry | Loki | Profiling

Solving Rising Observability Costs with Grafana Cloud In this video, Grafana Labs demonstrates how Grafana Cloud addresses ...

Published on 2024-12-17T18:49:50Z

URL: https://www.youtube.com/watch?v=A-csCzclcbw

Transcript: Hello everyone, and thanks for
joining. During this video, we're gonna talk through how Grafana can
help companies solve the challenge of rising observability costs. As we talk
to customers and teams across the globe, we hear three specific things as it
relates to rising observability costs and observability teams. One, that observability costs are increasing
and they're often unpredictable. Two, that logging architectures have become
costly and resource intensive. And three, with rising observability costs, businesses are having to
make decisions on coverage. And this lack of coverage leaves blind
spots for teams like development teams and DevOps teams. Grafana
Cloud offers a unique solution. It's built on these three things.
One, we offer adaptive telemetry, which pretty much means that customers
get full visibility into not only what they're sending to Grafana Cloud, but what they're using to allow customers
to make decisions on what to send to Grafana Cloud. So they only pay for
what they're using. In Grafana Cloud, we built Loki and we built it on
an efficient logging architecture. Specifically, we've eliminated
the need for indexing overhead, and we've leveraged cost-effective
object storage. And last but not least, with these savings across
traditional metrics, logs and traces, companies are able to invest into
a fourth pillar observability, continuous profiling. This pillar of observability
allows development teams
to optimize performance of their applications while also being
able to reduce infrastructure costs. All in all, Grafana Cloud allows companies to use a
cost-effective end-to-end observability solution without having to compromise
on efficiency or performance. Let's walk through how Grafana does this. This is Grafana Cloud's Cardinality
Management tool. As you can see here, we're looking at all of the metrics
that we're sending into Grafana Cloud, and we're able to see exactly what's
being used and what's not being used. And this is important because Grafana
Cloud also allows you to use something called Adaptive Metrics
or adaptive telemetry. And in here we can actually go in and
apply rules based on if we're using or not using that data. We can go into these individual metrics
and we can see exactly what we're using them for. And then Grafana makes
recommendations for you to be able to sum, aggregate or drop labels or metrics that
are not being used to make sure that everything that you're sending to Grafana
Cloud is actually being used and the companies and teams are getting
value out of that. Second, Grafana has built Loki, and Loki is
a cost effective logging solution. The main reason that Loki is unique is
that we don't need the large overhead of index. Instead, we use a
small index built on labels. And these labels are a way for you to
understand where things are coming from and the overall health of
your logs without having to
have the large index to be able to search through everything. This is key as you're able to still get
the insight to all the things that you need, such as patterns of your log lines, errors that are happening
in your log lines. And you can see all this without having
to query using Grafana's queryless, Explore Logs feature. And last
but not least, we have profiling. Profiling is a unique way for developers
to be able to understand not only how effective or optimized their code is, but also how much resources they're
using from an infrastructure perspective. As you can see here, this
is Explore Profiling, which is a queryless experience for
you to search through your profiles. And we can immediately go in and look at
all the profiles that are coming from a specific application. And we can also look at the flame graph
of this specific application as well. We can quickly run a diff flame graph, which pretty much means we're able to
compare two different profiles and we can see exactly what the differences between
the two are. And in Grafana Cloud, we have a way for you to use a large
language model to understand exactly what this flame graph is and can actually
provide recommendations on how to fix this problem and what that would
actually mean to you, the team, and then most importantly, the
business. As I mentioned before, Grafana Cloud offers this cost effective
end-to-end observability solution to customers without teams having to make
compromises on efficiency or performance. Here's some stories from some
customers. First, here's SailPoint. SailPoint was able to use Adaptive
Metrics to be able to reduce their cost by 33%, and this was
actually done in minutes. And here's a quote from Omar Lopez talking
about how Adaptive Metrics was able to help them grow efficiently
without just blowing up metrics. And then here's Sensor Tower. Sensor Tower was able to use continuous
profiling and gain 20% savings in their AWS infrastructure bill by
optimizing just a single line of code. If you'd love to learn more about
how Grafana can solve these rising observability costs, please contact
us or visit us at grafana.com.

