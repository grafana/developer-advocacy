# How to Configure the OpenTelemetry Operator With Your Kubernetes Cluster | Tutorial | Grafana

In this video, Grafana Labs Staff Solutions Engineer Lionel Marks describes how to configure the OpenTelemetry Operator along ...

Published on 2024-10-17T23:29:09Z

URL: https://www.youtube.com/watch?v=tWvlZc1V9qA

Transcript: Hi, and welcome to Grafana's OpenTelemetry
Operator and Auto-instrumentation Tutorial. So let's get started. Now, the first thing you'll see here on my
desktop is a standard Grafana Cloud instance. This happens to be my test instance
and there's very little that's been configured here so far, and we'll head over to the
application observability function. Application Observability is a new feature
inside of Grafana Cloud that allows you to see all of your services across
any type of application workspace. Now here we have a inventory or service
catalog of applications that are automatically discovered. You'll
see in the last 30 minutes, there have not been any applications
deployed in my environment. Now what we're gonna do here is we're
gonna go ahead and move towards my Kubernetes cluster. And what you'll see here is
just a standard Kubernetes
cluster that happens to live in AWS EKS. And I've also pre-installed the Grafana
Alloy agent technology to collect all of the telemetry signals
from my applications. Now, before we actually see any data
inside of the Grafana Cloud instance, we first have to deploy that app and
then we have to instrument it properly. There are many different
ways to instrument your app. You can do it through manual
instrumentation or auto instrumentation. And then of course you need to also
set up that auto instrumentation. So we're gonna use a technique to
actually do that for us in a slip screen manner. So that's called the
OpenTelemetry Operator and let
me show you how that works. So let me go over to my
OpenTelemetry operator installation. We're gonna go ahead and
use the Helm Chart command. So the expectation in this video is that
you have some familiarity with things like Helm and Kube
Control, and if you don't, there's some links below again that
you can follow along if you wanna learn more. So I'm gonna go ahead
and execute this command and it's going to install
the OpenTelemetry Operator. And there it goes. So the OpenTelemetry operator is now
deployed into my Kubernetes cluster. Now the next thing that we're gonna do
is we're gonna install something that's called a custom resource. Now a custom resource in Kubernetes
is a more advanced topic, but in order for the
OpenTelemetry Operator to
understand what to instrument in the applications, and we do need to install this
specialized instrumentation object and it has been created. Now, anytime I deploy an app
inside of Kubernetes, it will automatically detect that app
and then instrument it appropriately. Now there's one additional step. Again, it is listed in the steps
in the tutorial below, is that we will have to ensure
that we annotate the app. So we're gonna go ahead and look at
the YAML manifest for this application. In this case, the application is
called helloworld-nodejs-app.yaml. And if we take a look at this, it's a deployment using a
standard nodejs test app from this image repository. But the most important piece here
is that we're adding an annotation. This annotation effectively instructs
the OpenTelemetry operator to inject the appropriate SDKs in order
to instrument this app. And we'll show you more
about how that looks. Once we get started now one last thing. This deployment includes a service and
the service designed to be able to talk to a distributed set of these nodejs apps. So let's go ahead and deploy this app. Using the the kubectl command. Here we go. And we will see now that
the app is getting deployed and if we navigate over to one
of these deployed pods and we scroll all the way down to the bottom, we'll see that the app was
successfully deployed in a single pod, but also there was an init container, meaning an container that spun
up to do a specific task was also initiated to inject the instrumentation
based on the annotation that we declared inside of the application
yaml. And once that job was completed, the init container is spun
down and no longer needed. So if we go back to our pods, we can see that we have our app
running along with a service right here. And now we will head back
over to my Grafana Cloud instance. Okay, so now we're back to My Grafana Cloud
instance and we will go ahead and look at the last hours worth of data. And boom, now we have my Hello World app has been
discovered in the service catalog and I can go ahead and drill in and look at
the RED metrics for this newly deployed app. In my Kubernetes cluster, we can
see things such as the latency metrics, the error metrics, the rate metrics, and then we also see the upstream and
downstream services that are connected to my Hello World app. Very useful. Now if I wanted to drill in I could
also look at the trace data for this app, sort by duration. We
can drill into a trace, we can look at the logs, we
can look at the profiles. We can also pivot to the underlying
infrastructure that's hosting this app. Very useful. So here are the
pod infrastructure metrics. So now I can very quickly
correlate different attributes
or different telemetry signals that are emanating
for this particular service. And that's pretty much it. So appreciate you taking the time to
listen to my video tutorial and look forward to gathering your
feedback. Take care. Bye.

