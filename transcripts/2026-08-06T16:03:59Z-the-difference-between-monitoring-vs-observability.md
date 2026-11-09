# The difference between Monitoring vs Observability

Published on 2026-08-06T16:03:59Z

## Description

Understand the difference between monitoring and observability in modern systems. *Watch the complete video* ...

URL: https://www.youtube.com/watch?v=DPFCM0uyfiI

## Summary

The show is titled "The difference between Monitoring vs Observability," published on August 6, 2026. The discussion focuses on the distinction between monitoring and observability in modern systems, emphasizing the importance of collecting various telemetry signals, including metrics, logs, traces, and profiling. The speakers highlight how distributed tracing can help identify issues within microservices, using the example of a payment gateway to illustrate how tracing can pinpoint problems in the backend. Key takeaways include the necessity of comprehensive data collection for effective observability and the role of tracing in understanding service relationships.

Topics: monitoring, observability, telemetry, distributed tracing, microservices

## Chapters

00:00:00 Understanding observability and telemetry signals
00:00:46 Understanding service performance issues

Observability means you are collecting all that telemetry signals. So, basically, it's not just metrics, but also collecting logs, traces, and profiling as well. Once you have this data, it depends on how you are correlating or understanding it.

Tracing, or distributed tracing, helps you understand the relationship between multiple microservices. A classic example is the payment gateway service. If you purchase something and, just as you are about to pay, something crashes and you have to do it again, the administrator on the backend can use tracing to identify which particular service or line of code was not performing well or caused the problem. This allows them to map the issue to the specific component that failed.

## Raw YouTube Transcript

Observability means you are collecting all that telemetry signals. So, basically, not just metrics, but collecting logs, traces, and also there is profiling as well. Um and once you have this, then it depends like how you are correlating or understanding to it. Basically, tracing or the distributed tracing helps you to understand the relationship between multiple microservices because the classic example is the payment gateway service. If something uh for example, you purchase something and after just about to pay out, something crashes and you have to do it again, but on the back end side of that particular application, the the administrator, if the tracing is placed, can identify like which particular service or uh particular uh code line of code uh was not performing or caused some problems, and can map to the

