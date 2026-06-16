# Dropbox Ingests 5GB-6GB of Logs per Second Using Loki. Here&#39;s How | Grafana Everywhere

Published on 2026-03-03T18:30:05Z

## Description

As part of the Grafana Everywhere series, Chris Hodges from Dropbox shares why they chose Loki for their logging stack after ...

URL: https://www.youtube.com/watch?v=3-TG4AzV0SQ

## Summary

In this video, Chris Hodges, a software engineer at Dropbox, discusses the importance of observability in enhancing product reliability and performance. He highlights the evolution of logging practices at Dropbox over the past five years, transitioning from manual logging methods to using Loki, a log aggregation system that integrates well with Grafana. Chris explains how migrating to Kubernetes necessitated a more efficient logging solution, leading to the use of Loki's multi-tenancy features, which allow for fine-grained control over logging limits for various services. He notes the positive response from users and an increase in satisfaction since implementing Loki.

## Chapters

00:00:00 Introductions and background of Chris Hodges  
00:01:15 Importance of observability at Dropbox  
00:02:00 Change in logging practices over the past 5 years  
00:02:30 Challenges with traditional logging methods  
00:03:00 Migration to Kubernetes and its impact on logging  
00:03:30 Introduction of Loki as a solution  
00:04:00 Benefits of Loki's integration with Grafana  
00:04:30 Multi-tenancy functionality in Loki  
00:05:00 Operationalizing Loki at scale  
00:05:30 User satisfaction and feedback on Loki implementation  

Hey, I'm Chris Hodges. I've been at Dropbox as a software engineer for about four years now, and I work on one of our observability teams. Observability is crucial at Dropbox because it directly impacts how our customers perceive our products, as well as the reliability and performance of those products.

Almost every engineer at Dropbox looks at observability data on a daily basis. Five years ago, logging looked a lot different. We had engineers SSHing into machines, using VI, or pulling log files over the network, which just wasn't sustainable. We needed tighter production access controls, and we were migrating to Kubernetes, which meant that the logs became more ephemeral. That's where Loki came in as a natural fit.

We really liked the fact that Loki is natively supported by Grafana because we want logs, traces, and metrics to all be in the same UI. The biggest challenge for us in operationalizing Loki at scale was utilizing the multi-tenancy functionality. Essentially, every service at Dropbox is a tenant of Loki, allowing us to have very fine-grained controls in terms of limits per service.

The response has been quite positive. We've received a lot of enthusiastic feedback from users, and we've continued to see satisfaction levels rise since we deployed Loki.

## Raw YouTube Transcript

Hey, I'm Chris Hodges. I've been at Dropbox as a software engineer for about 4 years now and I work on [music] one of our observability teams. Observability is so important at Dropbox because it directly impacts how our customers perceive the products and our reliability, the performance of the products. >> [music] >> And like almost every engineer at Dropbox is looking at observability data on almost a daily basis. 5 years ago, logging looked a lot different. We >> [music] >> had engineers SSHing into machines VI or pulling log files over the network and this just wasn't sustainable. We needed [music] tighter production access controls and we were migrating to Kubernetes, which meant the logs were more ephemeral and so Loki was kind of a natural fit there. We really liked the fact that Loki was natively supported by Grafana because we want logs, traces, and metrics to all be there [music] kind of in the same UI. I would say the biggest thing for us to operationalize Loki at scale was the ability to use the multi-tenancy functionality. So, basically every service at Dropbox is [music] a tenant of Loki and that allows us to have very fine-grained controls as far as limits go per per service. Yeah, the response has been pretty positive. We've got a lot of users who are very enthusiastic [music] about using it. We've continued to see satisfaction go up since we've deployed Loki.

