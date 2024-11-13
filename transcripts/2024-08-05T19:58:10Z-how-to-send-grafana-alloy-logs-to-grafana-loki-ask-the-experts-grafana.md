# How to Send Grafana Alloy Logs to Grafana Loki | Ask the Experts | Grafana

In this video, Matt Durham, Sr. Software Engineer on the Grafana Alloy team, shows you how to send Grafana Alloy logs to Loki.

Published on 2024-08-05T19:58:10Z

URL: https://www.youtube.com/watch?v=nUwHzT1sprU

Transcript: Hello everybody. I'm Matthew Durham and I'm a senior
software developer here at Grafana working on the Alloy project. We received a question from the
community about how to send Alloy logs to Loki. So today I am gonna walk through a
very quick process on how to grab those logs and then manipulate them a
bit and then forward them to the Loki endpoint. So I have a configuration
here. It consists of three components. In Alloy, you write a pipeline that does pull some data, processes some data and sends data. So here at the top we have our logging
configuration block. In this case, level = "debug", I want the
most information possible. Format - I'm doing logfmt.
You could also do JSON. And then the important instruction
and argument here is the "write_to". This tells the logging framework
to send the Alloy logs somewhere. So in this case, I'm going to send it
to the next component in my pipeline, which is this loki.process "alloy". loki.process is a pipeline
unto itself. In this case, I'm just going to add a single label. So I have a stage in the loki.process. There's a multitude of stages
you can add in process. In this, we're just going to simply
add one label "service_name", and I'm going to name it "alloy" so
I can identify it on the front end. And then since we're talking
about these pipelines, I'm going to forward any of the transform data from the loki.process
"alloy" to the loki.write? And loki.write Is what actually
sends the data from Alloy itself to Grafana Cloud or any Loki-compatible
endpoint. It's pretty basic. I have a URL, I have some auth. I'm hiding that with some environment
variables so they're not in plain text. And then data is flowing. So I've had Alloy running
in the background for a
little bit so we can move. Let's take a look at just the
components that are running. So we have a dashboard where you can
see what's running, what's going on. If I look at this process.alloy,
not a whole lot here, I just simply see where I've
added some tags and receiver. And then let's go to the important
part. Let's go to Grafana Cloud. So I'm gonna do a refresh here just to
make sure I'm getting the most recent data. I am looking for service_name Alloy and I'm just gonna run the query here. And you can see I have some logs
coming through and service_name Alloy. So now I can see what
Alloy is doing. You know, do any sort of operations I need to here. And using that loki.process Stages, I can manipulate the data in a lot of
other ways if I wanted to to filter or transform it another way. Thank
you for watching Ask the Experts. If you enjoyed the content,
please like or subscribe. And if you have any comments on the
content we presented or want to see something else, please add
comments below. Thank you.

