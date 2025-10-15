# Understanding Core Web Vitals | Grafana Faro

Published on 2025-05-23T17:00:21Z

## Description

In this video, we break down Core Web Vitals in Grafana Cloud's Frontend Observability and Grafana Faro. Useful Links ...

URL: https://www.youtube.com/watch?v=GsLPpUcY3RM

## Summary

In this video, Pakola, a developer advocate at Grafana, explains how to analyze core web vital metrics using Grafana Pharaoh and Grafana Cloud's front-end observability solution. He emphasizes the importance of understanding user experience when it comes to web performance, highlighting challenges like slow load times and layout shifts. The video details the two components of the solution: Grafana Pharaoh, a web SDK for collecting real user monitoring data, and Grafana's visualization tools. Pakola covers the core web vitals defined by Google, which assess load performance, visual stability, and interactivity. He explains five key metrics: Time to First Byte (TTFB), First Contentful Paint (FCP), Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS), and Interaction to Next Paint (INP), providing targets and optimization tips for each. The video concludes with an invitation to explore Grafana's documentation and subscribe for further content.

# Analyzing Core Web Vital Metrics with Grafana

Hi, I'm Pakola, a developer advocate at Grafana. In this video, we'll walk through how to analyze core web vital metrics that you can collect with Grafana Pharaoh and automatically visualize with Grafana Cloud front-end observability.

## Introduction to Grafana's Front-End Observability Solution

Before we dive in, let me provide some context about Grafana's front-end observability solution. One of the biggest challenges in front-end development is understanding how users actually experience your website and applications. Websites can have slow load times, layout shifts, and unresponsive web elements, which can go unnoticed, quietly degrading the user experience.

Grafana Cloud front-end observability brings visibility into the performance of your front end by making real user performance measurable and actionable. This solution is made up of two parts:

- **Grafana Pharaoh:** A web SDK that collects real user monitoring (RUM) data such as performance metrics, logs, exceptions, events, and traces.
- **Grafana front-end observability:** A hosted service that visualizes collected RUM data through powerful out-of-the-box dashboards, making the data clear and actionable.

With minimal setup, users get a comprehensive view of the performance of their front end and access important information like page load speed, core web vitals, error logs, and session data.

## Core Web Vitals

Now that you understand Grafana Cloud's front-end observability solution, let's dive into one of the first metrics you'll see in your out-of-the-box dashboard: **Core Web Vitals**. Core web vitals are essential performance metrics defined by Google. Google recommends monitoring and optimizing these metrics to improve the user experience of your website and its search ranking.

These metrics measure three key aspects:

1. **Load Performance:** How fast your content shows up.
2. **Visual Stability:** How stable your layout is.
3. **Interactivity:** How quickly your site responds to clicks and taps.

Grafana collects these metrics using Google's web vitals JavaScript library, and they are automatically visualized in the out-of-the-box Grafana front-end observability dashboard via queries from Grafana Loki. These metrics are color-coded, allowing you to quickly detect the performance of each metric:

- **Green:** Good performance
- **Yellow:** Needs improvement
- **Red:** Poor performance

### Key Core Web Vital Metrics

Let's walk through each core web vital:

1. **TTFB (Time to First Byte):**  
   TTFB measures the duration between a user's request and the moment the first byte of the server response is received. High values of TTFB typically indicate delays due to back-end processing, inefficiencies, or network latency. A good target for TTFB is under 600 milliseconds.

2. **FCP (First Contentful Paint):**  
   FCP measures how long it takes the browser to render any piece of content from the DOM, such as text, images, or SVG elements. This metric provides insights into how quickly users see something appear on the screen after navigating to a page. For strong performance, FCP should occur within 1.8 seconds. Developers can improve FCP by removing render-blocking scripts, prioritizing the loading of visible content, and removing unused CSS and JavaScript.

3. **LCP (Largest Contentful Paint):**  
   LCP measures the time it takes for the largest visible element in the viewport, like an image or a headline, to fully render. This metric provides a clear signal of when the primary content has loaded for the user. A good LCP should be under 2.5 seconds. To improve your LCP, compress large assets like images, reduce server response times, and eliminate render-blocking JavaScript or CSS.

4. **CLS (Cumulative Layout Shift):**  
   CLS measures the amount of unexpected movement or content (layout shift) on a page during its lifecycle. These layout shifts can be frustrating for users, especially when they try to interact with content that suddenly moves. To maintain a good user experience, CLS scores should remain below 0.1. To minimize layout shifts, developers should define dimensions for images and videos, preload fonts to avoid late loading changes, and avoid injecting content above existing elements without reserving space.

5. **INP (Interaction to Next Paint):**  
   INP measures the time between a user's interaction and when the next visual update is painted on screen. INP captures all interactions throughout the session and reflects the slowest one, excluding outliers, making it a holistic measure of responsiveness. A good INP is below 200 milliseconds. Developers can improve INP by eliminating long JavaScript tasks, deferring non-critical work, and optimizing how and when updates are rendered.

## Conclusion

There you have it! You now know about core web vitals, what they are, and how to optimize them. If you want to learn more about Grafana front-end observability, make sure to visit the documentation linked below. 

And don’t forget to tap the subscribe button if you would like to see more videos about Grafana's front-end observability solution. 

Thanks for watching, and I will see you in the next video!

## Raw YouTube Transcript

Hi, I'm Pakola, a developer advocate at Graphfana. In this video, we'll walk through how to analyze core web vital metrics that you can collect with Graphfana Pharaoh and automatically visualize with Grafana Cloud front-end observability. Before we dive in, let me provide some context about Graphfana's front-end observability solution. One of the biggest challenges in front-end development is understanding how users actually experience your website and applications. Websites could have slow load times, layout shifts, and unresponsive web elements which can go unnoticed, quietly degrading the user experience. Graphana cloud front-end observability brings visibility into the performance of your front end by making real user performance measurable and actionable. This solution is made up of two parts. Graphfana Pharaoh, a web SDK which collects real user monitoring rum data like performance metrics, logs, exceptions, events, and traces and graphana front-end observability, a hosted service that visualizes collected real user monitoring data. through powerful out-of-the-box dashboards to make the data clear and actionable. With minimal setup, users get a comprehensive view of the performance of their front end and access to important information like page load speed, core web vitals, error logs, and sessions data. Now that you understand Graphana Cloud's front-end observability solution, let's deep dive into one of the first metrics you'll see in your out-of-the-box dashboard, which are core web vitals. Core web vitals are essential performance metrics defined by Google. Google recommends monitoring and optimizing these metrics to improve the user experience of your website and your website's search ranking. These metrics measure three key things. Load performance, how fast your content shows up. Visual stability, how stable your layout is. Interactivity, how quickly your site responds to clicks and taps. Graphana collects these metrics using Google's web vital's JavaScript library. And the metrics are automatically visualized in the out-of-the-box Graphana front-end observability dashboard via queries from Graphana Loki. These metrics are color-coded too, so you can quickly detect the performance of each metric. Green means good performance, yellow means needs improvement, and red means poor performance. Let's walk through each core web vital. The first core web vital metric we see is TTFB or time to first bite. TTFB measures the duration between a user's request and the moment the first bite of the server response is received. High values of TTFB typically indicate delays due to back-end processing, inefficiencies, or network latency. A good target for TTFB is under 600 milliseconds. A high TTFB often indicates backend delays, network latency, or inefficient server configurations. The next web vital metric we see is FCP or first contentful paint. FCP measures how long it takes the browser to render any piece of content from the DOM such as text, images, or SVG elements. This metric provides insights into how quickly users see something appear on the screen after navigating to a page. For strong performance, FCP should occur within 1.8 seconds. Developers can improve FCP by removing render blocking scripts and prioritizing the loading of visible content and removing unused CSS and JavaScript. The next core web vital metric we see is LCP or largest contentful paint. Largest contentful paint measures the time it takes for the largest visible element in the viewport like an image or a headline to fully render. This metric provides a clear signal of when the primary content has loaded for the user. A good LCP should be under 2 and 1/2 seconds. To improve your LCP, compress large assets like images, reduce server response times, and eliminate render blocking JavaScript or CSS. The next core web vital metric we see is CLS or cumulative layout shift. Cumulative layout shift measures the amount of unexpected movement or content, also known as layout shift on a page during its life cycle. These layout shifts can be frustrating for users, especially when they try to interact with content that suddenly moves. To maintain a good user experience, CLS scores should remain below 0.1. And to minimize layout shifts, developers should define dimensions for images and videos, preload fonts to avoid late loading changes, and avoid injecting content above existing elements without reserving space. The final core web vital metric we see is INP or interaction to next paint. Interaction to next paint measures the time between a user's interaction and when the next visual update is painted on screen. INP captures all interactions throughout the session and reflects the slowest one excluding outliers making it a holistic measure of responsiveness. A good INP is below 200 seconds. Developers can improve INP by eliminating long JavaScript tasks, deferring non-critical work, and optimizing how and when updates are rendered. There you have it. You now know about core web vitals, what they are, and how to optimize them. If you want to learn more about Graphana front-end observability, make sure to visit the documentation linked below. And make sure to tap the subscribe button if you would like to see more videos about Grafana's front-end observability solution. Thanks for watching, and I will see you in the next video.

