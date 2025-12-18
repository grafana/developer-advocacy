# 🎬 Videos Wrapped 2025

> A curated analysis of the most surprising, unusual, and interesting Grafana videos published in 2025.

---

## 🔥 Top 10 Most Surprising Videos

### 1. The Candle Fire Incident
**Date:** December 17, 2025  
**People:** Anonymous presenter  
**Video:** "Oops: The Dangers of Monitoring Candles | HomeLabs Big Tent S3 Ep1"

**What Made It Surprising:** A home lab enthusiast built a candle monitoring system with PM particle sensors and remote shutdown capabilities. During testing, *the wooden lid caught fire*. A genuine cautionary tale about the dangers of experimenting with fire and IoT—delivered with surprising candor about what went wrong.

---

### 2. Grafana as a Digital Audio Workstation
**Date:** September 22, 2025  
**People:** Tobias (Grafana), Ahmed  
**Video:** "Grafana & Friends Stockholm Meetup at 0+X"

**What Made It Surprising:** A hackathon project that integrates MIDI keyboards with Grafana for real-time music visualization. Using RxJS, Web Media API, and Tone.js, the team created panels that visualize piano notes, drum hits, and microphone input as spectrograms. The presenter's stated vision: *"Grafana is the most popular digital audio workstation by 2028."*

---

### 3. AI Agent Builds Dashboards via Natural Language
**Date:** September 2, 2025  
**People:** Grafana Japan Meetup presenters  
**Video:** "(Japanese) Grafana Meetup Japan #6"

**What Made It Surprising:** Live demo of the Grafana MCP Server where Claude Desktop (an AI agent) creates production dashboards from conversational prompts like "make me a troubleshooting dashboard." The presenter openly admitted the demo had a *50% success rate* and asked the audience to "pray with him." It worked.

---

### 4. AI Creates GitHub PRs to Fix Performance Bugs
**Date:** October 22, 2025  
**People:** Cyril Tovena, Dmitry Filimonov (Grafana Labs)  
**Video:** "Agentic AI for Observability: Grafana Assistant & Investigations"

**What Made It Surprising:** During a live demo, Grafana Assistant analyzed flame graphs from profiling data, identified a regex compilation issue causing CPU spikes, and *automatically created a GitHub pull request* to fix it—complete with a proper description and code changes. The fix addressed a classic Go anti-pattern of compiling regex in a loop.

---

### 5. Vertical Farming IoT Observability
**Date:** October 22, 2025  
**People:** Owen Bower Adams (Intelligent Growth Solutions)  
**Video:** "How IGS Scales IoT Observability for Vertical Farming with Grafana Cloud"

**What Made It Surprising:** Industrial vertical farms present unique observability challenges—equipment operates in environments that are essentially Faraday cages with poor WiFi connectivity. IGS uses Grafana Cloud to monitor crops and proactively alert customers about network issues *before they call support*. A fascinating non-traditional use case.

---

### 6. Real-Time Kafka Visualization Without Storage
**Date:** September 22, 2025  
**People:** Ahmed (Stockholm Meetup)  
**Video:** "Grafana & Friends Stockholm Meetup at 0+X"

**What Made It Surprising:** An open-source Grafana plugin that streams Kafka messages directly into dashboards without intermediate storage—2M+ downloads, reportedly used by Bank of America. Supports real-time monitoring, auto-complete for topics, Avro schemas, and various authentication methods. Built by one developer in their spare time.

---

### 7. Dropping 16 Billion Metric Series
**Date:** October 22, 2025  
**People:** Sean Porter, Rich Kreitz (Grafana Labs)  
**Video:** "How to Get (and Pay For) the Telemetry Data That Actually Matters"

**What Made It Surprising:** The sheer scale of Adaptive Telemetry: 16 billion active metric series dropped, 12 petabytes of logs eliminated—all through intelligent sampling. AI/ML models detect latency anomalies and automatically capture relevant traces. Internal ops cluster processes 2.5GB/second of traces and stores only 400MB/second (84% reduction).

---

### 8. Non-Engineers Building Production Dashboards
**Date:** October 22, 2025  
**People:** Jeremy White (SpotOn)  
**Video:** "Grafana Assistant Helps Keep Restaurants Running... SpotOn Explains How"

**What Made It Surprising:** Network support specialists with *no Grafana experience* used Grafana Assistant to create production dashboards for monitoring restaurant networks. They went from "not familiar with the tooling" to proactively identifying groups of customers experiencing issues before they called support.

---

### 9. Zero Budget to Complete Observability
**Date:** October 22, 2025  
**People:** Sebastian & Julia (AXA Germany)  
**Video:** "From Zero Budget to Complete Observability with Grafana Cloud & OpenTelemetry"

**What Made It Surprising:** A 5-person team at AXA Germany built a complete observability stack with literally no budget. Management's constraints: "Do it without asking developers to do anything." Their solution: build custom exporters from middleware access logs. The success eventually unlocked budget and led to Grafana Cloud adoption.

---

### 10. AI Detects Null Pointer During Deployment
**Date:** October 22, 2025  
**People:** Jeremy White (SpotOn)  
**Video:** "Grafana Assistant Helps Keep Restaurants Running..."

**What Made It Surprising:** Grafana Assistant analyzed a Kubernetes pod crash-looping alert and automatically identified a null pointer reference during a transformation process—*in real-time during a release*. The AI decorated the generic alert with specific context that made troubleshooting immediate.

---

## 🎸 Honorable Mentions for Creativity

| Project | Description |
|---------|-------------|
| **Andrew's TV Remote Debugging** | Used Grafana traces to debug why his DIY TV remote (open-source "Omote" project) wasn't sending volume updates to his receiver. Featured during the Drilldown Apps demo. |
| **Music Spectrogram Visualization** | Microphone FFT frequency data visualized as heatmaps in Grafana—whistling creates visible frequency spikes in real-time. |
| **Self-Hosted Grafana Stack at GO (Japan)** | Running Loki, Mimir, Tempo, and OnCall at scale: 2-3TB logs/day, 25GB metrics, 100GB traces—all self-managed with a small team. |

---

## 📊 2025 Themes

### The Rise of Agentic AI
2025 was definitively the year AI became *agentic* in observability:
- Natural language dashboard creation
- Automatic PR generation from profiling insights
- Intelligent alert decoration with root cause context
- Autonomous investigation across logs, metrics, and traces

### Democratization of Observability
Non-engineers are now building production dashboards. The "blank sheet of paper problem" is being solved by AI assistants that can translate intent into PromQL, LogQL, and TraceQL.

### Creative/Unconventional Use Cases
The community pushed Grafana far beyond traditional IT monitoring:
- Music production and MIDI visualization
- Vertical farming and industrial IoT
- Home automation (with fire safety lessons learned)
- Restaurant point-of-sale system reliability

### Cost Consciousness at Scale
Multiple sessions focused on reducing observability costs:
- Adaptive Telemetry (metrics, logs, traces, profiles)
- Self-hosted stacks with strategic cloud adoption
- Intelligent sampling to pay only for signal, not noise

---

## 🏆 Video of the Year

**Winner: "Agentic AI for Observability: Grafana Assistant & Investigations"**  
*October 22, 2025 — Cyril Tovena & Dmitry Filimonov*

The live demo of AI analyzing a flame graph, identifying a performance issue, and creating a GitHub PR to fix it represents the most transformative moment in observability tooling this year. It's not just monitoring anymore—it's automated remediation.

**Runner-Up: Stockholm Meetup Music Visualization**  
For sheer creativity and the audacious vision of Grafana as a digital audio workstation.

---

*Report generated from analysis of 284 video transcripts published in 2025.*

