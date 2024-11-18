# How to enable Explore Logs app for Grafana

Here's how to enable the Explore Logs app for Grafana in a nutshell. For more information, check out our Loki Community Call on ...

Published on 2024-11-12T16:00:42Z

URL: https://www.youtube.com/watch?v=jx1DATkGIz4

Transcript: if you want to try out the new explore logs app for your open source graina installation there are three things you need to do first you need to modify your Loki config file specifically within the limits config make sure that volume enabled is true this is mandatory but there are two optional things that I want to recommend you do as well the first is to allow structured metadata and set that to true and the second is to enable the pattern ingestor as well the second thing that you need to do is to make sure you're using the right versions of grafana and Loki you're going to need grafana version 11.2 or later and Loki version 3.2 or later and the third thing is to enable the grafana plugin we go through all of these in the documentation and the video down below and in the description so check those out

