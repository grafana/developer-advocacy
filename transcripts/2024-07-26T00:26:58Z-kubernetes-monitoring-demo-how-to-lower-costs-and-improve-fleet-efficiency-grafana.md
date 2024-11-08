# Kubernetes Monitoring Demo: How to Lower Costs and Improve Fleet Efficiency | Grafana

The Kubernetes Monitoring app in Grafana Cloud helps you visualize infrastructure costs across providers, identify unallocated ...

Published on 2024-07-26T00:26:58Z

URL: https://www.youtube.com/watch?v=OpIzdlArRMM

Transcript: Hi, this is Vijay Tolani from the
Technical Marketing Team at Grafana Labs. If you're using Kubernetes infrastructure, you're likely familiar with the challenges
of budget scrutiny from FinOps and surprisingly high cloud
infrastructure bills. The Kubernetes monitoring app for
Grafana Cloud helps you visualize infrastructure costs across providers. You can identify unallocated and
idle resources and ultimately visualize usage and capacity
along with requests and limits. This helps you keep your fleet as
efficient and performant as possible, all while reducing costs. Teams that utilize this have reduced
their infrastructure costs by 20 to 30%. We'll start with the
cluster navigation view, where we can see all of our
clusters, their associated costs, including the costs of idle resources. Let's drill into this
cluster to find out more. We can immediately see this cluster is
overprovision for CPU with six cores allocated, but usage remaining
below one core. And with memory, we have a capacity of 11 gigs,
but usage is around five gigs. Clearly, there's more infrastructure being
provisioned than our apps actually need, which is a big waste of money. Let's take a look at our
namespace to see how we got here. Here we can see all of our namespace
along with their associated usage. Let's drill into production
to find out more. With CPU, we can see our usage
actually exceeds requests, which is a performance bottleneck, and many of our containers
don't have requests set at all. Setting these requests on our workloads
will help ensure our applications get the resources they need to
perform well with memory. We can see we have requests
configured at 4.4 gigs, but usage remains below three gigs. We can safely reduce these requests, reducing our infrastructure costs
without hurting application performance. And finally, we can see the health of our workloads
making it very easy to identify hotspots and opportunities for efficiency. If
you're struggling with Kubernetes costs, take a look at the latest features of
the Kubernetes monitoring app for Grafana Cloud.

