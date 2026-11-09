# Agentic SRE: How DriveWealth Triages Alerts with Grafana Assistant

Published on 2026-11-03T19:02:59Z

## Description

See how DriveWealth, a real-time, regulated brokerage-as-a-service company, put a triage layer between its alerts and its on-call ...

URL: https://www.youtube.com/watch?v=UwVaRULe0DI

## Summary

The show titled "Agentic SRE: How DriveWealth Triages Alerts with Grafana Assistant" was published on November 3, 2026. The speaker, Serge Sheynkman, shared insights on how DriveWealth, a brokerage-as-a-service company, implemented Grafana Assistant to improve alert triaging and reduce unnecessary engineer wake-ups during off-hours. Key topics included the transition from a reactive alert system to a proactive one, where 25% of client inquiries are now resolved at first contact without engineering involvement, and the importance of standardization in alert management. The presentation emphasized the role of structured logs and skills written by service teams to enhance response efficiency and reduce the mean time to resolve alerts.

Topics: Grafana Assistant, alert triaging, standardization, client inquiries, engineering efficiency.

## Chapters

00:00:00 Reducing alert fatigue with Grafana Assistant
00:06:38 Standardizing alerts and diagnostics in Grafana
00:12:18 Using Grafana Assistant for alert triage and skills
00:18:59 How DriveWealth uses Grafana Assistant for alert triage

Good afternoon, everyone. Quick check before we start: Is anybody in this room currently on call? Show of hands if you are on call right now. I know we were told that we need to keep our phones off, but from my presentations, whoever's on call, feel free to put your phones on. And honestly, this is what this talk is all about.

I'm Serge Sheynkman. For the next 25 minutes, we're going to talk about 3 o'clock in the morning—the time every alert used to wake a human—and how we stopped that from being the default. There are two full... Sorry. 

Before the work, a little bit about me: I'm a dad of two grown men, 29 and 24. Neither of them went to tech. I did the root cause analysis why, and the years of "One second, I'm on a bridge" at the dinner table was it. Another contributing factor was the 3 o'clock in the morning. Corrective action was none; they made their own choices. These days, my favorite side project is for my wife, who's an elementary school teacher. I'm trying to build her an AI grading agent. At work, I review changes and PRs; at home, she reviews mine. And yes, I keep picturing a Grafana dashboard for her classroom, but she keeps reminding me that kids are not pods.

Most of you probably have never heard or heard very little about DriveWealth, and that's by design. We're the brokerage behind the brands—more than a hundred partners, investors in more than 150 countries. Someone in Laos or São Paulo opens an app, taps buy, and trusts our environment to buy them a piece of a US company for the price of lunch. That's on the math, which means two things: we are real-time and we are regulated. Hold on to both of those ideas; they're going to matter.

Here's the punchline upfront: 25% of all our client inquiries are now answered at first contact by our client-facing teams with Grafana Assistant, with no engineering involved. I'll show you how we got there, including the part where a one-time financial investment mattered. 

**Four colors, two stories.** The problem is how we approached it, what we built, and what it taught us. The two stories: 

1. **Story one** is engineering getting no answer, getting to the answer faster. 
2. **Story two** is the people who talk to clients getting answers without calling the engineering teams.

It's 3:07 AM. Your phone buzzes; you fumble for it, squint, unlock it with the wrong face, put in the wrong code—it's a disk. It bridged the threshold at 71%. It's not full, not failing, just 71%. And now you're awake. Hands up if you've been paged for something that wasn't critical, but you had really no substance of what needs to be done in the middle of the night when you get an initial call. I certainly have been part of that group, so welcome to the support group.

When you look at this chart, that was us. No triage layer between the alerts and the person. Every major and critical alert paged someone—front office, back office, all of it. This is pages per night. It goes up to the right, which is exactly the wrong chart to be proud of. Our call rotation didn't have a sleep schedule; it had a step count every time they received a call. 

Now, why does this matter for DriveWealth and maybe matters more than in some other areas? Because when something goes wrong here, it is somebody's money. On the left is what clients and partners expect: a fair price the moment they tap their app to buy, an app that they can trust. And remember, it is our partner's brand on that app. So our incidents become their incidents. Balance is right to descent and everything working at the market open at 9:30 sharp because markets would not wait for anybody to fix their problems. 

On the right is what regulators want and expect. And I'm going to say it in plain English because I'm sure citing a regulatory rule book version is going to be less fun: Get everyone a fair price, keep a perfect paper trail, keep clients' cash and shares safe and separate. Make sure buyers get their shares and sellers get their cash by the next business day, and tell regulators what happened and have the absolutely accurate trail. One error can break both promises at once. In most cases, in other organizations, it may be a ticket. In our world, this becomes a conversation with the regulator.

So here's the before and after on one slide. **Before**, alerts landed on engineers with no triage and no context. **After**, Grafana systems run the right skill when an alert fires, when someone asks from Slack or dashboard. Major and critical alerts still page a human, but now the page arrives with a diagnostic bundle attached. Info and minor alerts get the same bundle—logged but not paged. Nobody gets woken up for something that is not critical.

Here's the least exciting sentence in this talk and the most important one: **Standardize first, enforce it always.** Everything after that gets cheaper. I know you all came here for AI talk, but stay with me. The AI only works because of this slide. 

**Five boring ideas:**
- Alloy everywhere, manage through fleet management with one label set across Kubernetes and bare metals.
- Alerts on metrics, not on LogQL, over all lines.
- Structure JSON logs, so you parse fields instead of regex and strings.
- OpenTelemetry instrumentation. So trade ADs, join logs, metrics, and traces and alert of symptoms.
- Mitigate first, find the root cause later.

The payoff shows up on the billing dashboard. Initially, when we started, we just migrated to Grafana; our query usage ratio was at a thousand percent. Basically, for every hundred terabytes we ingested, we scanned a petabyte because unstructured logs meant every time we ran a query, it was a full scan looking for a needle in the haystack. Today, we're on a borderline of 60% because structured logs, good labels, and queries that go straight to the fields that they need to query. 

And here's the part that people skip often: Enforcing the standards is what makes this sustainable. Every skill, every alert, every diagnostic bundle you see in a minute depends on the standardization because if you grab something at 3 o'clock in the morning, it's not a strategy; it's a scavenger hunt without much success.

**Four boxes and three errors.** Our sources of Kubernetes and bare metals across front, middle, and back office. The pipeline is Alloy rolled out with Kubernetes monitoring home and fleet management. Ship everything to Mimir, Loki, and Tempo. Triaging is Grafana Assistant with running the skills, and when it needs help, investigations come to the rescue. Insight our paging platform pages a human only for major and critical alerts with the research bundle attached. 

Four boxes, three errors, zero magic. The lack of magic is actually what makes it work. And it covers the whole state: the front office trading, which is trading pricing, order flow; the back office, which is settlement, risk, and reconciliations; and the shared platform, the one that everybody claims first. One Grafana Cloud plane underneath all of it.

Which brings us to the new rule of the house: **Ask the assistant before you wake a human or page one.** Two things change. First, skills are written by the team that owns the service. Each dev team or support team writes the diagnostic knowledge for their own systems. The assistant runs it on alert when someone asks, and when it needs help, investigations come to the rescue. 

Second is context-enriched reach paging. Major and critical alerts page with a bundle already attached. The page now arrives with the answers attached. The engineer's job is to agree with it. 

This is the flow, and it's the one slide I'd like you to remember. Step one: every time Grafana Assistant runs the skill, it's fast, it's scoped, and becomes cheaper—cheaper every time the skills get updated. Step two: when the assistant needs help or an engineer just wants a deeper look, investigations come to the rescue—logs, metrics, traces, the whole picture with the evidence kept. Step three: only when one and two can be satisfied do we need a human to react to it.

They show up with everything already in hand. Whatever they learn goes back into the skill, so the next time, step one handles it all. The feedback loop closes the tribal knowledge gap. Our own guide says it's best. The knowledge used to live in the engineer's head; the best engineer on the team used to be a single point of failure. Now, they are skilled with the last review date, then a runbook. 

The runbook was a Wiki page, a human reads at 3 o'clock in the morning, written by somebody who got paged last and updated the runbook, which usually gets out of sync within a week. It also assumes that whoever gets paged is a subject matter expert in every single service. Now, skill is a diagnostic the assistant executes, written by the team that owns the service in their own language with the queries and the thresholds built in. 

The same five tests still apply: it needs to be actionable, accessible, accurate, authoritative, and adaptive. You build it, you run it; that was the model before. Now you build it, you write a skill. You've all seen assistant skills in product and production. Here's how we use them: we want a short document per business flow that teaches the assistant how that flow works and which Loki answers which question. One skill, one flow. 

For trading, it would cover order lifecycle, funding deposits, withdrawals, onboarding, account opening, and every skill answers four questions: 
1. How does this flow work? 
2. Which ADs does support have? 
3. Where does the data live? 
4. Which query answers which question? 

Two practical notes: the assistant finds skills by semantic search, so write them in supported vocabulary, not your service names. There is a 64 kilobytes hard limit, but what we found is if you really go above 30 kilobytes, it gets a little quirky. However, you can chain them together if you need to have more than one skill connected to the same workflow. 

Our litmus test is pretty simple. We take a real support question and we ask Grafana Assistant. If you get the answers right, your job is done. If not, you have some more work to do. Thank you. 

Here's a real example from September. For obvious reasons, we had to black out all the sensitive information that is not public, but an alert fires on the order engine. On-call asks the assistant to run the execution correction skill. The skill finds one incident logged three times, the duplicates, and then pulls the trade details, applies the correction policy, and drafts the incident for ops and the trade desk in the next step. 

My favorite part of it is that on the first run, the skill logs a JSON parser error. So it reruns again, corrects its own JSON parsing query, and updates the skill, making it available for the next time. After reviewing that, the trade desk says thank you. 

Now, the confession: when the investigation first came out, we got really, really excited, to the point where we asked Grafana to investigate our entire alert history once upfront. Needless to say, that is a credit chart, and that one spike was one big invoice, one very scoped agent. But ever since, every query and every investigation is very scoped. 

The good news is that one pass found the patterns that became our skills in many areas, and every assistant query is now scoped. Capped time ranges required label matches, and it taught us the other lessons of the slide. A runbook that just says "investigate-and-fix" is not a runbook. 

Put it together and you get our model. The foundation of the model is an investigation run once across history to map the pattern. Skills are the teams that own each domain, write them down, and then the runtime. The assistant runs the skills on every alert and inquiry, and when it needs help, we tap investigations to come to the rescue. Investigations run only once or very limited times; skills run every single time. That's the difference between a bill and a budget. 

So there are two stories in this presentation. Story one is an engineering call. Let's walk through one alert from start to finish. Say Kubernetes monitoring shows the fleet; sometimes it's off. Application observability shows a red metric generated from the trace. On-call triggers the Assistant from the alert, it applies the skill, and its needed help, and investigations come to the rescue. 

If it's a major or critical alert, the page lands with the bundle attached. The engineer has the full picture before they even open the dashboard, compared to a 3 o'clock in the morning page when you're trying to find your glasses or open your phone with the wrong face. 

Here's the bridge between our two stories. We looked at about 1,200 assistant requests over the last nine weeks, about 130 a week. Under the hood, we have Loki query handling dominated over 6,000 tool calls across 628 charts. Logs are the backbone of all of it. 

The top three queries for diagnostics are for an error, explaining a concept, and looking up an order, which, if you ever sat with a support team, is exactly what the support queue looks like. Sometimes real ones with the tail hidden. For example, why did this order take 11 seconds? The assistant traces stage by stage and finds that 10.7 seconds in this particular order was waiting for one venue after reroute. One venue, one session. This is not systemic. 

So that means we get an answer very quickly in a couple of seconds rather than having a human needing to find each step of the way. Another example: a client says that a fractional order was part of pre-market and it was filled at the market open. The question is why? Why was it not filled at the time of the order submission? We run it through the Assistant. The Assistant goes through the skill and says, "Yes, this is per design. Fractional orders can only execute during a core trading session; it's expected behavior, and no engineer needs to get involved." 

The second story is about the people who talk to our clients. The sentence that got everybody's attention at our company is that every escalation to engineering is a feature that we didn't ship but had to support. Every day, clients and partners ask us about how to use our platform, their specific accounts, their trading activity, and their regulatory obligations. 

Before, a lot of those followed the escalation chain: client-facing team to SRE, to product, to dev, to QA, to business, taking days to close, and the engineers were pulled off from building new products to answer questions like, "What happened to this order?" Now, the relationship management, trade desk, and client support teams ask the assistant directly and get complete answers in minutes. 

Tier zero deflection is a fancy way of saying that the engineers got their afternoons back to build products. Here's how that works without anyone getting into trouble. Clients ask us about three things: trade and order statuses, transactions and balances, and clearing a position. Each one has a rule book behind it, and the skills know which one. 

The inquiry comes in, the teams ask the assistant, and the assistant finds the skill written by the team that owns the domain. The skill correlates logs, metrics, and traces with account context and analytics within the rules that apply, and a complete compliant answer goes back to the client. The engineer never enters the ticket. That's a shift left, not for code, but for client operations. 

And the direction matters as much as the number. Time to context is coming down. Inquiries resolved without escalations are going up. Skills in the library are increasing, written by dev teams and subject matter experts, not just SRE or the support teams. One line goes down, two go up. 

That's the whole talk. You can leave now. Please don't; there is more. So did it work for us? Yes, we can certainly say that 25% of our client inquiries now resolve at the first contact, and we're aiming for 60% to 70%. Query usage ratio went down from 1,000% to the 60s, and the one I'm the proudest of is that meantime to resolve is down 51% since January. More than half of our...

Alerts are now resolved in under an hour. Not pictured here are the happy faces of our engineering team who don't get paged; that's the real metric. 

So, three things next: 

1. Every new service ships with a skill. It is part of our definition of done. 
2. We're building a hotline path for when self-service isn't enough. 
3. Our natural progression is towards Grafana Incident Response Management (IRM) because we want to keep everything in one place, so we do not need to keep integrating and supporting different platforms. 

If you remember three things from my presentation today, here they are:

- **Assistant first investigations to the rescue**: Context arrives before the human reads.
- **Skills are runbooks for the AI age**: The team that owns the service writes them.
- **One control plane and two audiences**: This results in faster resolution for engineering, first contact answers, and for the client teams, the roadmap capacity is back to an acceptable velocity.

And if you only remember one thing, it’s this: nobody should be woken up for something that is not critical in the middle of the night. 

Thank you. You've been a great audience.

## Raw YouTube Transcript

Good afternoon, everyone. Quick check before we 
start. Is anybody in this room currently on call? Show of hands if you are on call right now. I know 
we were told that we need to keep our phones off, but from my presentations, whoever's on 
call, feel free to put your phones on. And honestly, this is what this talk is all about. 
I'm Serge Sheynkman, for the next 25 minutes, we're going to talk about 3 o'clock in the 
morning, the time every alert used to wake a human and how we stopped that from being 
the default. There are two full... Sorry. All right. Before the work, a little bit 
about me. I'm a dad of two grown men, 29 and 24. Neither of them went to tech. I did the root 
cause analysis why and the years of "One second, I'm on a bridge" at the dinner table was it and 
another contributing factor was the 3 o'clock in the morning. Corrective action was none. They made 
their own choices. These days my favorite side project is for my wife who's an elementary school 
teacher. I'm trying to build her an AI grading agent. At work, I review changes and PRs. At home, 
she reviews mine. And yes, I keep picturing a Grafana dashboard for her classroom, but she 
keeps reminding me that kids are not pods. Most of you probably never heard or heard very 
little about DriveWealth, and that's by design. We're the brokerage behind the brands. More 
than a hundred partners, investors in more than 150 countries. Someone in Laos or Sao Paulo 
opens an app and they tap buy and they trust our environment to buy them a piece of US company for 
the price of lunch. That's an on the math, which means two things. We are real time and we are 
regulated. Hold on to both of those ideas, they're going to matter. Here's the punchline upfront. 
25% of all our client inquiries are now answered at first contact by our client-facing teams with 
Grafana Assistant with no engineering involved. I'll show you how we got there, including the part 
where a onetime financial investment mattered. Four colors, two stories. The problem is 
how we approached it, what we built and what it taught us. The two stories, story 
one is engineering getting no answer, getting to the answer faster. And story two is the 
people who talk to clients getting answers without calling the engineering teams. It's 3:07 AM, your 
phone buzzes, you fumble for it, squint, unlock it with the wrong face, put in the wrong code, 
it's a disk. It bridged the threshold at 71%. It's not full, not failing, just 71%. And now 
you're awake. Hands up if you've been paged for something that wasn't critical, but you 
had really no substance of what needs to be done in the middle of the night when you get an 
initial call. I certainly have been part of that group, so welcome to the support group.
When you look at this chart, that was us. No triage layer between the alerts and the person. 
Every major and critical alert paged someone, front office, back office, all of it. This 
is pages per night. It goes up to the right, which is exactly the wrong chart to be proud of. 
Our call rotation didn't have a sleep schedule. It had a step count every time they receive a 
call. Now, why does this matter for DriveWealth and maybe matters more than in some 
other areas? Because when something goes wrong here, it is somebody's money.
On the left is what clients and partners expect, a fair price the moment they tap their app to 
buy, an app that they can trust. And remember, it is our partner's brand on that app. So 
our incidents become their incidents. Balance is right to descent and everything working at the 
market open at 9:30 sharp because markets would not wait for anybodies to fix their problems.
On the right is what regulators want and expect. And I'm going to say it in the plain English 
because I'm sure citing a regulatory rule book version is going to be less fun. Get everyone 
a fair price, keep a perfect paper trail, keep clients cash and share safe and separate. 
Make sure buyers get their shares and sellers get their cash by the next business day and tell 
regulators what happened and have the absolutely accurate trail. One error can break both promises 
at once. In most cases, in other organizations, it may be a ticket. In our world, this 
becomes a conversation with the regulator. So here's the before and after on one 
slide. Before, alerts landed on engineers with no triage and no context. After Grafana 
systems runs the right skill when an alert fires, when someone asks from Slack or dashboard. 
Major and critical alerts still page a human, but now the page arrives with a diagnostic 
bundle attached. Info and minor alerts get the same bundle, logged but not paged. Nobody gets 
woken up for something that is not critical. Here's the least exciting sentence in this talk 
and the most important one. Standardize first, enforce it always. Everything after that gets 
cheaper. I know you all came here for AI talk, but stay with me. The AI only 
works because of this slide. Five boring ideas. Alloy everywhere, manage 
through fleet management with one label set across Kubernetes and bare metals. Alerts on metrics, not 
on log QL, over all lines. Structure JSON logs, so you parse fields instead of regex and strings. 
Open telemetry instrumentation. So trade ADs, join logs, metrics and traces and 
alert of symptoms. Mitigate first, find the root cause later. The payoff shows up on 
the billing dashboard. Initially, when we start, we just migrated to Grafana, our query usage 
ratio was at a thousand percent. Basically for every hundred terabytes we ingested, we scanned 
a petabyte because unstructured logs meant every time we run a query, it was a full scan looking 
for a needle in the haystack. Today we're on a borderline of 60% because structured logs, 
good labels, and queries that go straight to the fields that they need to query.
And here's the part that people skip often. Enforcing the standards is what makes 
this sustainable. Every skill, every alert, every diagnostic bundle you see in a minute depends on 
the standardization because if you grab something at 3 o'clock in the morning, it's not a strategy. 
It's a scavenger hunt without much of success. Four boxes and three errors. Our sources 
of Kubernetes and bare metals across front, middle and back office. The pipeline is alloy 
rolled out with Kubernetes monitoring home and fleet management. Ship everything to Mimir, Loki 
and Tampo. Triaging is Grafana Assistant with running the skills and when it needs help, 
investigations come to the rescue. Insight our paging platform pages a human only for 
major and critical alerts with the research bundle attached. Four boxes, three errors, zero 
magic. The lack of magic is actually what makes it work. And it covers the whole state, the 
front office trading, which is trading pricing, order flow, the back office, which is settlement, 
risk and reconciliations, and the shared platform, the one that everybody claims first. One 
Grafana Cloud plane underneath all of it. Which brings us to the new rule of the house, 
ask the assistant before you wake a human or page one. Two things change. First, skills 
written by the team that owns the service. Each dev team or support team writes the diagnostic 
knowledge for their own systems. The assistant runs it on alert when someone asks and when it 
needs help, investigations come to the rescue. Second is context-enriched reach paging. Major 
and critical alert page with a bundle already attached. The page now arrives with the answers 
attached. The engineer's job is to agree with it. This is the flow and it's the one slide 
I'd like you to remember. Step one, every time Grafana Assistant, it runs the skill, 
it's fast, it's scoped, and becomes cheaper, cheaper every time the skills get updated.
Step two, when the assistant needs help or an engineer just wants a deeper look, investigations 
come to the rescue, logs, metrics, traces, the whole picture with the evidence kept. Step 
three, only when one and two can be satisfied, we need a human to react to it. And they 
show up with everything already in hand. Whatever they learn goes back into the 
skill. So the next time, step one handles it all. The feedback loop closes the tribal 
knowledge gap. Our own guide says it's best. The knowledge used to live in engineer's 
head, the best engineer on the team used to be a single point of failure. Now, they 
are skilled with the last review date. Then a runbook. Runbook Was a Wiki page, a 
human reads at 3 o'clock in the morning written by somebody who got paged last and updated the 
runbook, which gets usually out of sync within a week. And it also assumes that whoever gets paged 
is a subject matter in every single service. Now, skill is a diagnostic the assistant executes, 
written by the team that owns the service in their own language with the queries and the trash 
holes built in. Same five tests still apply, needs to be actionable, accessible, accurate, 
authoritative, and adaptive. You build it, you run it, that was the model before. 
Now you build it, you write a skill. You've all seen assistant skills in product and 
production. Here's how we use them. Want short document per business flow that teaches the 
assistant how that flow works and which Loki answers which question. One skill, one flow. 
For trading, it would cover order lifecycle, funding deposits, withdrawals, onboarding, 
account opening, and every skill answers four questions. How does this flow work? Which 
ADs does support have? Where does the data live? Which query answers which question?
Two practical notes. The assistant finds skills by semantic search, so writes them in 
supported vocabulary, not your service names. And there is a 64 kilobytes hard limit, but what 
we found is if you really go above 30 kilobytes, it really gets a little quirky, but you can 
chain them together if you need to have more than one skill connected to the same workflow. 
So our litmus test is pretty simple. We take a real support question and we ask Grafana 
Assistant. If you get the answers right, your job is done. If it's not, 
you have some more work to do. Thank you.
Here's the real example from September. For obvious reason, we had to black out all the 
sensitive information that is not public, but an alert fires on the order engine. On call asks the 
assistant to run the execution correction skill. The skill finds one incident logged three times, 
the duplicates, and then pulls the trade details, applies the correction policy and drafts the 
incident for ops and the trade desk in the next step. And my favorite part of it is on the 
first run, the skill log QL through a JSON parser error. So it reruns again, corrects its own 
JSON parsing query and updates the skill and makes it available for the next time. So after 
reviewing that, the trade desk says thank you. Now, the confession. When the investigation just 
first came out, we got really, really excited, to the point where we asked Grafana to investigate 
our entire alert history once upfront. Needless to say that this is a credit chart and 
that one spike, which was one big invoice, one very scoped agent, but ever since every 
query and every investigation is very scoped. The good news that one pass found the patterns 
that became our skills in many areas and every assistant query is now scoped. Capped time 
ranges required label matches, and it taught us the other lessons of the slide. A runbook that 
just says investigate-and-fix is not a runbook. Put it together and you get our model. Foundation 
of the model is investigation run once across history to map the pattern. Skills is the teams 
that own each domain, write them down, and then the run time. The assistant runs the skills on 
every alert and inquiry and when it needs help, we tap investigations to come to the rescue. 
Investigations run only once or very limited times, skills run every single time. That's 
the difference between a bill and a budget. So there are two stories in this presentation. 
Story one is engineering call. Let's walk one alert from start to finish. Say Kubernetes 
monitoring shows the fleet, sometimes it's off. Application observability shows red metric 
generating from the trace. On call triggers the Assistant from the alert, it applies the 
skill and its needed help, and investigations come to the rescue. Four, it is the major or 
critical. If it's a major or critical, the page lands with the bundle attached. The engineer 
has the full picture before they even open the dashboard. Compared to that to 3 o'clock in 
the morning page when you're trying to find your glasses or open your phone with the wrong face.
Here's the bridge between our two stories. We looked at about 1,200 assistant requests over the 
last nine weeks, about 130 a week. Under the hood, we have Loki query handle dominated over 6,000 
tools, tool calls across 628 charts. Logs are the backbone in all of it. The top three queries, 
diagnostics are for an error, explaining concept, looking up an order, which if you ever sat with 
a support team is exactly what the support queue looks like. Sometimes real ones with the tail 
hidden. Why did this order take 11 seconds? The assistant traces stage by stage and would find 
that 10.7 seconds in this particular order was waiting for one venue after reroute. One venue, 
one session. This is not systemic. So that means we get an answer very quickly in couple 
of seconds rather than having a human needing to find each step of the way.
Or another example, a client says that a fractional order was part of pre-market and it was 
filled at the market open. The question is why? Why it was not filled at the time of the order 
submission? We run it through Assistant. Assistant goes through the skill and it says, "Yes, this 
is per design. Fractional orders can only execute during a core trading session, it's expected 
behavior and no engineer needs to get involved." The second story is the people who talk to our 
clients and the sentence that got everybody's attention at our company is that every escalation 
to engineering is a feature that we didn't ship, but had to support. Every day clients and partners 
ask us about how to use our platform, about their specific accounts, about their trading activity 
and about their regulatory obligations. Before, a lot of those followed the escalation chain, 
client facing team to SRE, to product, to dev, to QA, to business, days to close, and 
the engineers pulled off from building new products to answer what happened to this 
order. Now after, the relationship management and the trade desk and the client support teams 
ask the assistant directly and get a complete answers in minutes. Tier zero, deflection 
is fancy way to saying that the engineers got their afternoons back to build product.
Here's how that works without anyone getting into trouble. Clients ask us about three things, trade 
and order statuses, transactions and balances, clearing a position. Each one has a rule book 
behind it and the skills know which one. The inquiry comes in, the teams ask the assistant, 
the assistant finds the skill written by the team that owns the domain. The skill correlates 
logs, metrics and traces with account context and analytics within the rules that apply and a 
complete compliant answer goes back to the client. Engineer never enters the ticket. That's a shift 
left, not for code, but for client operations. And the direction matters as much as the number. 
Time to context is coming down. Inquiries resolved without escalations are going up. Skills 
in the library are going up, written by dev teams and the subject matter expert, not just 
SRE or the support teams. One line goes down, two goes up. That's the whole talk. You can 
leave now. Please don't, there is more. So did it work for us? Yeah, we can certainly say 
that 25% of our client inquiries now resolve at the first contact and we're aiming for 60% 
to 70%. Query usage ratio went down from 1,000% to 60s and the one I'm the proudest 
of is meantime to resolve is down 51% since January. More than half of our alerts are now 
resolved under an hour. Not pictured here is the happy faces of our engineering team who 
doesn't get paged, that's the real metric. So three things next. Every new service ships 
with a skill. It is part of our definition of done. We're building a hotline path for when 
self-service isn't enough and our natural progression is towards Grafana IRM because 
we want to keep everything in one place so we do not need to keep integration 
and supporting different platforms. If you remember three things from my presentation 
today, here they are. One is Assistant first investigations to the rescue, context arrived 
before the human reads. Two, skills are runbooks for the AI age and the team that owns the 
service writes them. And number three, one control plane and two audiences, which results in 
a faster resolution for engineering, first contact answers and for the client teams, the roadmap 
capacity is back now to the acceptable velocity. And if you only remember one thing, nobody 
should be woken up for something that is not critical in the middle of the night.
Thank you. You've been a great audience.

