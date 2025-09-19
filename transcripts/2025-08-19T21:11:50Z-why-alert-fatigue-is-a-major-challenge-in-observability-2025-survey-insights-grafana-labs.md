# Why Alert Fatigue is a Major Challenge in Observability (2025 Survey Insights) | Grafana Labs

Published on 2025-08-19T21:11:50Z

## Description

Over 1200 engineers, leaders, and teams shared their biggest observability challenges in our third annual Observability Survey ...

URL: https://www.youtube.com/watch?v=be2OeAE4uI4

## Summary

In this video, Marc Chipouras, head of emerging products at Grafana Labs, discusses the findings of their third annual observability survey, which included over 1,200 respondents. The primary issue identified is alert fatigue, with 33% of respondents citing it as the biggest obstacle in incident response, affecting everyone from engineers to CTOs. Chipouras emphasizes the importance of Service Level Objectives (SLOs) in addressing this problem, noting that 24% of respondents currently use SLOs in production. Additionally, he highlights the differing perspectives between leadership and engineering teams regarding the best methods to reduce alert fatigue, particularly the use of AI/ML for adaptive alerts and root cause analysis. The video also touches on the significance of FinOps in managing observability costs, advocating for transparency and cost attribution to optimize resource usage. Overall, the discussion sheds light on the challenges of observability and the potential of SLOs and AI/ML in improving incident management.

# Observability Insights from Grafana's Annual Survey

Hello, I'm Marc Chipouras with Grafana Labs, and I’m the head of emerging products here. I have a passion for observability, and I hope you do too. We recently concluded our third annual observability survey, with over 1,200 respondents. I'd like to share some key insights from the survey.

## Key Takeaways

### Alert Fatigue
The first major takeaway is **alert fatigue**. A significant **33%** of respondents identified it as the biggest obstacle to their incident response today. This resonates with many of us; it’s not just engineers experiencing this issue. Everyone feels the strain—your CTO, your director of engineering, and the platform team are all affected by alert fatigue. This is a positive sign because if leadership is aware of the problem, we stand a better chance of addressing it.

### Challenges Faced by Engineering Managers
Engineering managers (EMs) face challenges beyond alert fatigue; they also struggle with **coordination during incidents**. EMs are often designated as the incident manager on call, which can complicate collaboration. While EMs focus on coordination, the rest of the team deals with alerts.

### The Role of SLOs
One effective way to mitigate alert fatigue is to shift towards **Service Level Objectives (SLOs)**. It’s encouraging to see that **24%** of respondents are currently using SLOs in production, with another **50%** either in a proof of concept or investigating SLOs. SLOs foster discussions between engineering and product teams about where to invest resources, promoting accountability and ultimately leading to improved Mean Time to Recovery (MTTR). Notably, **33%** of respondents are utilizing SLOs to enhance MTTR, and **25%** are using them for better accountability—all aimed at reducing alert fatigue.

### AI/ML and Alert Fatigue
When examining the intersection of alert fatigue and AI/ML, we found that **31%** of respondents believe that training-based adaptive alerts are the most effective way to reduce alert fatigue. Meanwhile, **28%** think that faster root cause analysis is the best approach. This distinction is fascinating. Leaders, including CTOs and directors of engineering, tend to favor adaptive alerts for anomaly detection. In contrast, engineers, engineering managers, and platform teams lean towards faster root cause analysis and automated checks. This raises an interesting question: are engineers more aware of AI/ML’s potential benefits, or do leaders lack confidence in these technologies?

### Observability and FinOps
Lastly, I want to discuss **FinOps** and the use of observability for cost attribution. It's crucial to monitor observability costs to ensure they don't overwhelm overall development spending. Not all observability efforts are equal; some teams utilize it more extensively than others based on performance issues or new services. Currently, **15%** of survey respondents are using FinOps in production. Larger organizations, in particular, are more likely to implement cost attribution to allocate expenses across departments. 

Increasing transparency around observability costs is essential, regardless of company size. I highly recommend that organizations implement cost attribution to show teams their spending. This practice can significantly impact how observability is leveraged to enhance engineering effectiveness.

## Conclusion
All this data is available in an interactive dashboard for you to explore further. AI/ML is evolving rapidly, and I look forward to hearing how you're using it to reduce alert fatigue. 

Thank you for your time!

## Raw YouTube Transcript

Hey, I'm Marc Chipouras with Grafana
Labs. I'm head of emerging products here. Love observability. I hope
you love observability too. We just came through with our
third annual observability survey. Over 1,200 people responded. I
want to share some notes with you. The first takeaway from the
survey is actually alert fatigue. 33% of you said it's the biggest
obstacle to your incident response today. Spot on. Everybody feels this. A lot of you actually thought it was
about lack of incident response process as well. What's really good
here as we're going through, it's not just the engineers that are
having a problem with alert fatigue. It's everybody - your CTO,
your director of engineering, the platform team - everybody
has a problem with alert fatigue. This is great because if your leaders
weren't having a problem with alert fatigue, then we don't have any chance of getting
it fixed. EMs' real challenge in this whole thing is not just alert fatigue. They're also having problems with
coordination during their incidents. This is likely because we usually put
them as the incident manager on call, so coordination, collaboration - their
biggest challenge. Everybody else, dealing with those alerts. One of the things I think is most
interesting is the best way, I think, to resolve some of that alert
fatigue is to move to SLOs, and it's great to see that 24% of you
are actually using SLOs in production today, and another 50% of you are actually
in a POC or investigation for SLOs. What's awesome about SLOs, it actually facilitates this conversation
between engineering and product to understand where you
should be investing today, and all that conversation can
happen in front of your leadership. Leads to better accountability.
Long-term, it leads to better MTTR, which is actually - 33% of you
are using SLOs for MTTR and 25% of you are using it for better
accountability. Both of those are there in order to help reduce your
alert fatigue as well. When we look into these numbers
about alert fatigue and AI/ML, we're seeing that around 31% of
you think that training-based adaptive alerts is the best
way to reduce alert fatigue, where a bunch of people, around 28%, are actually thinking a faster root cause
analysis is our best way in order to use AI/ML to reduce alert fatigue.
Both of those are really interesting. When we slice and dice it to see who
actually responded to this survey, we actually see something that's
more fascinating here. Our leaders, our CTOs, our director of engineering all think
that adaptive alerts for anomaly detection is a good way in order to
reduce that alert fatigue, but the engineers among us,
the engineering management
or platform team, SRE, actually think that faster root cause
analysis and our automated checks is a better way in order to be able to reduce
that alert fatigue. That's interesting to me - is that our engineers that
are closest to AI/ML actually see the benefits of where RCA or
root cause analysis could go, or is it that our leaders just
don't have faith in AI/ML yet? I think it's interesting. Lastly, I want to talk a little bit about
FinOps and actually using observability. In order to do cost attributions, it's actually super critical to
observe your observability costs, so these don't overwhelm your
overall development spend, especially because not all
observability is created equal. You have some teams who are using it
more and some people are using it less based on the performance issues or
the greenfield service that they're deploying, but 15% of people are actually
using FinOps in production today. That's pretty predictable and it actually
gets - the larger organizations are using cost attribution more in order
to be able to send costs across departments. It's really important from
my side that we increase transparency on observability costs. Whether you're
a small company or a large company, highly recommend that you actually
use cost attribution just to at least show back to teams what they're spending
if you're not actually applying it back to their teams. Show-backs like that can
actually dramatically change
your organization and how you're using observability to
improve your engineering department. This data is all available in an
interactive dashboard for you to explore, slice and dice. AI/ML
is changing so rapidly. I can't wait to hear more about how
you're using it in order to be able to reduce your alert fatigue.

