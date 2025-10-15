# Observability is Getting Expensive &amp; OpenTelemetry is Becoming More Popular | Grafana Labs

Published on 2025-04-26T01:53:46Z

## Description

Grafana Labs' Jen Villa shares the latest insights into how organizations are rethinking their observability strategies — with cost ...

URL: https://www.youtube.com/watch?v=VjG6JS535jw

## Summary

In this video, Jen Villa, a product director at Grafana Labs, discusses the findings from their third annual observability survey, which gathered insights from over a thousand professionals and leaders in the observability space. The survey highlights that 74% of respondents prioritize cost when selecting observability tools, reflecting a trend of increased scrutiny on budgets as businesses face economic pressures. Villa explains how the complexity of vendor pricing and the rising costs associated with increased observability adoption contribute to this focus on cost. She emphasizes the significance of OpenTelemetry in reducing vendor lock-in and managing costs, as well as addressing hidden costs related to complexity and signal-to-noise issues in observability tools. The video concludes by showcasing real-world examples of how improved observability can lead to significant cost savings and efficiency gains, encouraging viewers to explore the survey results further on Grafana's website.

# Observability Survey Insights

Hey everybody! My name's Jen Villa. I'm a product director here at Grafana Labs, focused on our core observability databases. Today, I'm excited to share some insights from our **third annual observability survey**. We surveyed over **1,000 professionals and leaders** in the observability space to understand what's on their minds.

## Key Findings on Tool Selection Criteria

One of the standout results from our survey was regarding **new tool selection criteria**. We asked participants what factors they consider when choosing observability tools for their organizations. Notably, **74% of respondents cited cost** as a significant factor. This was part of a multiple-choice question, where respondents could select various criteria, but cost emerged as the most common response.

### Reasons Behind the Focus on Cost

Several reasons explain this focus on cost:

1. **End of the Free Money Era**: We’ve reached the end of a period characterized by low interest rates. As a result, companies are scrutinizing every budget line item more carefully than ever before. Many organizations report mandates to **cut costs by 25%**, which extends to observability tools.

2. **Rising Costs with Previous Vendors**: Many organizations have experienced spiraling costs with previous vendors. Initially, the pricing may seem manageable, but as businesses grow, vendors often price by volume, leading to unpredictable expenses.

3. **Increased Adoption of Observability**: Observability has become easier to adopt, resulting in more instrumented services. This increase can lead to observability costs consuming a significant percentage of overall infrastructure spend. Our survey found that the **median observability spend** is about **10% of total infrastructure costs**. Some vendors report higher figures, such as **20% to 30%**, but generally, we see that **10%** as a common benchmark.

### Value of Observability

The value of observability can vary based on the impact of downtime. If a second of downtime costs billions, it makes sense to invest more in observability tools. However, there is a disconnect between the reasons for selecting new tools and current concerns about observability. While cost is a common concern, **complexity** and **overhead** were also significant issues. 

When we filter the data specifically for CTOs, cost emerges as a more prominent concern. Technology executives often manage P&L and evaluate build versus buy decisions, making cost a priority for them.

## The Rise of OpenTelemetry

The enthusiasm for **OpenTelemetry** is growing, as many respondents are either already using it or actively evaluating it. OpenTelemetry aims to reduce vendor lock-in by standardizing how telemetry data is collected and transmitted, allowing organizations to switch vendors without having to rebuild their observability pipeline. Essentially, it serves as an **insurance policy** against future cost spikes, preserving freedom of choice.

## Hidden Costs of Observability

While cost to the vendor is a primary concern, other factors also represent hidden costs. **Complexity** and **overhead** in maintaining observability can drain engineering time and resources. Sometimes, paying a vendor can save your team significant headaches and fatigue. 

Additionally, many respondents reported issues with **signal-to-noise** ratios. Too much noise can drown out critical signals, leading to increased downtime and lost revenue. The longer your teams take to detect issues, the more it can cost the business.

At Grafana Labs, we recognize these challenges and have developed our **Adaptive Telemetry** feature set. This feature analyzes incoming telemetry data to identify high-value information and helps reduce unnecessary data, saving costs and reducing signal-to-noise fatigue for engineers.

## Conclusion

In conclusion, while our survey shows that **cost efficiency** is crucial, organizations are increasingly viewing observability as a **business-critical function**. This shift is evident at the CTO and director levels, indicating a willingness to invest in observability as long as the cost-to-value ratio is maintained.

Here are a couple of real-world testimonials that illustrate the value of observability:

- One developer at an enterprise software company reported that by centralizing observability, they reduced their **mean time to resolve issues by 40%**, saving approximately **$25,000 a quarter**.
  
- A platform engineer at another software company shared that by analyzing logs and performance metrics, they were able to reduce downtime by **30%**, saving **$100,000** in penalties for breaching SLAs.

The challenge is not whether to implement observability, but **how to maximize its value** to your company.

If you're interested in exploring how the trends from our survey apply to your specific use case, industry, or role, I encourage you to visit **grafana.com**. There, you can find the survey results presented in a Grafana dashboard format, allowing you to filter and slice the data in ways that align with your needs.

Thank you for watching! I appreciate your time, and I hope these insights provide valuable information for your future endeavors.

## Raw YouTube Transcript

Hey everybody. My name's Jen Villa. I'm
a product director here at Grafana Labs, focused on our core
observability databases, and today I'm excited to talk through
some of the results we're seeing from our third annual observability
survey. This is survey we run. We surveyed over a thousand
both professionals and
leaders in the observability space to get a sense for
what's on their mind. So I'm going to take you through
a little bit of the results, especially as pertained to how people in
the space are thinking about costs when it comes to observability tooling. First thing that really stood out to us
is we asked this question about new tool selection criteria. So what is it that you think about when
you are picking observability tooling for your organization? And what we see there is
that 74% of respondents cited cost. This is one of our multiple choice, multiple selection questions. So customers
could select a variety of responses, but we saw that of all the responses,
cost was the most commonly selected one. We have a couple ideas for why we
think this is happening. So number one, we've reached the end of
the time of free money, what many called a zero
interest rate period, which means that companies are
scrutinizing every budget line item more carefully than any before. We're talking
to companies who often say, "Hey, my entire company has a mandate
to slash costs by 25%. Therefore, I need to look at how I can do that
even in observability." Second, many organizations have seen
their costs spiral with previous vendors, at least when they
come talk to us, right? Which creates kind of a heightened
sensitivity around pricing. So maybe at day zero day of signing
the contract, it was like, "Oh, this seems fine. We could totally do
this." But it turns out a lot of the vendors price by volume, which can often be hard to
predict and get right up front. And it also means that when your
business starts to take off, so does your observability bill. And that's compounded by the fact that
for some vendors, pricing can be complex, which means it's actually really hard to
predict what's going to happen to your bill when your estate grows that
you're trying to observe. Lastly, we've seen that observability has
gotten easier and easier to adopt. It just results in more and
more instrumented services, and that's going to mean an
increase in costs, right? Suddenly it's going to be
a several digit or double digit percentage of your overall
spend on compute infrastructure. And we actually asked around
in the survey, what does
that percentage look like? And we did find the median observability
spend is about 10% of total infrastructure costs.
Now, you can Google around, you'll see that some other vendors
cited numbers as high as say 20 or 30%. You'll see Reddit forums where
everyone's swapping their numbers or not. But generally, we're kind of seeing and thinking
in that 10% number ourselves. And that can really vary based
on how much you value that incremental bit of observability, right? If a second of downtime on your
application costs you billions of dollars, well it probably makes sense to spend
a couple more bucks on observability. What's pretty interesting is that there's
a little bit of a disconnect if you look at the data between the criteria
for selecting new tools of which cost again was the most common response, and then respondents talking
about what are their concerns with observability today? And
so while cost was one, again, one of the most common answers, it
wasn't the most common, certainly, at least when you compare it to that
new tools answers kind of answered about the same as complexity and
overhead and signal to noise. What's interesting is if
you then filter this though, specifically to look at CTOs, costs now becomes the standout answer. And I think what's pretty interesting
here is technology executives, they're not just responsible for technical
decisions. They often manage a P&L. They're often always being asked to
evaluate build versus buy decisions. So I think for them, cost is going to
stick out more than ever based on say, someone who's more like a tech leader
or an engineering manager. To me, it actually really helps explain the
growing enthusiasm for OpenTelemetry. And we saw that the majority
of respondents that we
talked to in our survey were either already using OpenTelemetry
or actively evaluating it, and you can see why, right? The promise of OpenTelemetry
is to reduce vendor lock-in by standardizing how telemetry data is
collected and transmitted, right? The goal is instrument once and that's it.
And you could switch among any vendor you want. So what that means is if some
particular vendor becomes too expensive, their pricing starts to become
extremely unpredictable, then you as an organization can switch
to another provider without having to completely rebuild your
observability pipeline. Essentially, it's like OpenTelemetry is giving you
an insurance policy against future cost spirals, right? It's preserving your
freedom of choice. So again, yeah, it makes sense that there's so much
demand and enthusiasm behind its development. Going back to this question about what
is it that folks are concerned with observability, I think it's really interesting to think
certainly there is the cost that you pay to your vendor, but I actually think these other
two most common answers are actually costs in and of themselves as
well. More like hidden costs, I'd say, right? So if we think about complexity
and overhead of maintaining your observability, that's actually a cost to
you in terms of your engineering time, in terms of your head space. And this
is where sometimes paying a vendor can make sense. It can be a
win. What you pay to them, you sometimes get back many times
over in terms of the headache and fatigue that your developers save. So for anyone considering
your observability solution, you just want to make sure to
factor in total cost of ownership, which includes your time, not just the
number that shows up on an invoice. Now, if you think about the
signal noise problem, again, nearly as many respondents said that
one challenge they're running into with observability is way too much noise,
and that's drowning out the signal, and this connects directly to
costs in multiple ways. Number one, signal and noise problem. It's often a symptom of having a
crazy high observability bill, right? Because the bill is generally
correlated to the volume of data, given how most vendors price, but
there's also this other cost to consider, which is increased downtime for
your applications. If your teams are overwhelmed by noise, when they're trying to use
the observability tooling
to figure out what's going wrong, they're probably going to miss the
critical signals like indicating what's actually happening. And that means longer time to actually
figure out what's going wrong, longer time to detect it
means more downtime to you, which means less revenue, right? That is a cost to your business because
that minute of additional downtime, oftentimes it could cost a lot more than
what you're necessarily going to save by paying for less
observability. At Grafana Labs, we've recognized a lot of this
signal-to-noise challenge, and that's why we have our Adaptive
Telemetry feature set. Actually, it was very much the inspiration for that. Adaptive Telemetry is going to analyze
your incoming telemetry data and identify what in there are you actually
using based on the query patterns that we see based on what we know about your
services. And it's going to say, okay, this is the high value stuff,
this is the low value stuff, and then give you a way to selectively
aggregate or sample away things that fall in that low value category.
And that's great again, because of now these twofold savings, you're getting savings on the bill
you're paying to Grafana Labs, but you're also getting savings in terms
of signal-to-noise fatigue going down for your engineers. Your engineers will have the right data
at the right time rather than having to go through this massive haystack
to find the right needle, right? It's like we're basically cutting
that haystack in half upfront so you have a smaller haystack to start from.
If we just take a step back here, I think while it's clear
from this survey that cost efficiency matters a lot, it's also clear that
organizations consider
observability of business critical function at higher and higher levels.
We had this here where we see actually that observability is being talked
about again at the CTO/director level, so more and more business
critical functions. And so what that means is there is some
acceptance that observability is a thing worth spending money on. It's really just about keeping
that ratio of cost to value in check. And we have a couple of real world
testimonials that think really help paint this picture. So one developer at an enterprise software
company kind of responded to us and said, "Hey, by centralizing
our observability, we reduced our meantime
to resolve issues by 40%, and that saved us an average of
15 engineer hours per incident, which means approximately $25,000 a
quarter." Platform engineer at another software company said, "Hey, by having all of our logs
analyzed and brought together, having those performance metrics, we identified recurring patterns
of high latency in our application. We're able to reduce our downtime by 30%, which translated to a hundred thousand
dollars less that we had to pay our customers because we were breaching SLA."
So again, we are seeing lots of success
stories with observability. So the challenge isn't like, "Do I
do it or not?" Again, it's really, "How do I do it in a way that maximizes
the value to my company?" If you're interested in exploring more about how
the trends that we found in our survey apply to you, your specific use
case, your specific industry, your specific role within an organization, I encourage you to visit grafana.com
and check out the results we have here in good Grafana dashboard form. You can slice and dice by a variety of
these filters to see the answers that align most with you and
your role and your team. So thank you for watching.
Appreciate your time, and I hope these insights give
you something to chew on as you go forward. Thanks.

