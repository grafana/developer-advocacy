# How to Detect Infrastructure Anomalies with Kubernetes Monitoring in Grafana Cloud | Grafana

This video provides a comprehensive guide to initiating Kubernetes monitoring within Grafana Cloud, detailing a straightforward, ...

Published on 2024-02-27T18:29:52Z

URL: https://www.youtube.com/watch?v=hnzgByDTWFU

Transcript: welcome to detecting infrastructure anomalies with kubernetes monitoring in grafana Cloud let's dive into identifying individual anomalies when you access the kubernetes monitoring landing page in grafana Cloud first evaluate the pots in trouble panel here PS have exceeded a threshold maybe they're hogging too much CPU stuck in a crash Loop or just can stop restarting with just a click you're taken into the heart of the issue the PO is constantly restarting because it stared from both RAM and CPU clicking into the Container specifics we see the pattern there too there it is a tailet recommendation to bump up the CPU limits based on the recent Trends further on a graph shows CPU throttling and restart buttons adjust the requests in limits accordingly and the issue is fixed handling systematic anomalies is more complex the key here is to separate the meaningful signals from the noise our revamped alerting experience makes your life easier even with this level of complexity you can see all your alerts in one place and pinpoint the real issue note these alerts from the duplicate cluster by filtering by name check out the last aler click on the Pod link and observe the events that show available nodes zero out of one this is how easily we discover a bottleneck a shortage of available ports a few adjustments later and we're back in business detecting Fleet anomalies can help decrease mttr and improve overall system reliability whether you're identifying and fixing a single misbehaving component or navigating through a CF alerts we've got you covered there is much more to explore on how you can keep your Fleet healthy performant and efficient with kubernetes monitoring in grafana Cloud so head over to graana.com solutionset
