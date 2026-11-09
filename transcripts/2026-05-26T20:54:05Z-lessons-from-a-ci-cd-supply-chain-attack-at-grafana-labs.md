# Lessons From a CI/CD Supply Chain Attack at Grafana Labs

Published on 2026-05-26T20:54:05Z

## Description

When a compromised GitHub Actions workflow targets your CI/CD pipeline, how do you respond — and what do you change so it ...

URL: https://www.youtube.com/watch?v=4D068lS85NY

## Summary

The show is titled "Lessons From a CI/CD Supply Chain Attack at Grafana Labs," published on May 26, 2026. The speakers are Nick, a principal security engineer, and David Andersson from the Security Engineering Team at Grafana. They discuss a security incident involving a CI/CD pipeline compromise, detailing how an attacker exploited a GitHub Actions vulnerability to exfiltrate secrets without causing customer impact. Key takeaways include the importance of preparation, the use of canary tokens for detection, and the integration of open-source tools like Zizmor and TruffleHog for vulnerability scanning and secret management. The incident led to significant changes in Grafana's security practices, including migrating secrets to HashiCorp Vault and implementing mandatory security scans for all pull requests.

Topics: CI/CD security, GitHub Actions, vulnerability scanning, canary tokens, open-source tools.

## Chapters

00:00:00 Overview of the CI/CD compromise incident
00:07:00 Understanding the CI/CD supply chain attack at Grafana Labs
00:13:05 Using tools like Zizmor and Gato-X for security during a supply chain attack
00:19:18 Lessons learned from a CI/CD supply chain attack

# Lessons From a CI/CD Supply Chain Attack at Grafana Labs

**Published:** 2026-05-26T20:54:05Z

---

Good morning, Barcelona! How are you all? I hope you are enjoying GrafanaCON. We're going to be talking through lessons from a security incident where everything went wrong. Really, almost everything that could go wrong did go wrong, but it all ends up right in the end.

My name's Nick. I'm a principal security engineer at Grafana, and I'm in the Detection and Response Engineering Team—possibly a team we named purely for the abbreviation. I can't confirm or deny that. When I'm not busy tracking down people trying to hack Grafana, I do actually like doing a bit of running. I enjoy going up and down mountains. I've run up and down the hills around Barcelona already and occasionally run further than most people like to drive. 

I'm joined here by...

**David:** First off though, a little bit of running—that's a euphemism for 180 miles last couple of weeks ago?

**Nick:** Yeah, something like that.

**David:** Somewhere there around. Good! So, yeah, I'm David Andersson. I work at the Security Engineering Team at Grafana. We don't have such a fancy abbreviation, but we do everything from secure best practices to how to implement secure coding principles and these kinds of things. I'm not an avid runner, but I like to be on stage, mostly singing and dancing on occasions, and also enjoying sitting in the audience enjoying musical theater.

Alright, so we're going to take you through a Saturday morning. Do you hear that, David? It sounds a bit like a canary singing. Well, it was an otherwise normal weekend. We woke up, looked at our phones, and went, "Hmm, that's a weird alert. I've not seen that one before." Two eagle-eyed security team members just happened to notice a particularly concerning alert that had popped up. Normally, we don't worry too much about this, but this one was... this was a big one. It was actually indicating that there was a complete CI/CD compromise. All of our secrets had been exfiltrated by an attacker, and at that point, most organizations are going, "Oh God." In fact, anyone is thinking, "Oh God, this is the worst possible outcome." 

Yet, we were able to write, very shortly after, that there had been no customer or user impact whatsoever. We were able to show that nothing had actually been done with those secrets that had any outcomes. But we're going to tell you that story of how we got there, the problems that we encountered at the beginning, how it happened, and then how we investigated, rectified, and made changes to make Grafana more secure. So I'm going to hand back to David. Thank you.

**David:** Before going into the details of the actual hack and the incident, I want to talk a bit about these two triggers. For those of you who have worked with GitHub, you're aware you have two triggers that you can use when responding to a pull request in GitHub Actions. One is "pull request," the other one is "pull request target." They look so alike; they are, in fact, not. 

So, "pull request" is a safety vault. Your developers, your fork maintainers, what have you—the ones forking your code—run their workflows in their context. It's a safety vault: no access to your environment, no access to your secrets, all fun. "Pull request target," not so much. Immediately, they have access to your repo with your secrets, and it becomes your problem. 

It has a legitimate purpose; it's designed for maintenance tasks, automated labeling, these kinds of things. But the thing is, when you combine "pull request target" with something that a user can control, all of a sudden, the fork code becomes trusted code. So this small change here is the gap between looks safe and is safe.

Fast forward to April 25th. We had one small change. It looked benevolent; it was internally contributed by a Grafana employee. It looked a lot like a CI improvement. What happened, though, is we had a pull request moving to "pull request target" with a combination of this script request. So with that, the user checked out the code, made a pull request against us, and executed... and GitHub Actions executed the command. This is the combination that mattered. 

Any contributor could then run arbitrary commands against our secrets. One merge is all it took, and the door was open. I want to highlight this line right here. If you're familiar with GitHub, it has a lot of built-in features, and GitHub repositories automatically populate GitHub SHA and automatically populate GitHub head ref—though that's GitHub speak for the name of your branch. That's what it took. This was the attack vector, and this is completely user-controlled. 

So the payload here wasn't something fancy; it wasn't a zero-day with sophisticated... Well, obviously, it was a hacker with a hoodie, we all know that. But it wasn't sophisticated in any other way. The payload was a branch name. We've looked at the door now or introduced the concept of the door. What did the key look like then? 

The attacker used Gato-X; we know this, and we will get to it a bit later. But Gato-X is a tool designed to be used at scale. It scans GitHub organizations at scale, finds vulnerable GitHub Actions workflows, maps them, and actively tries to exploit them. This was done in a three-step process. 

1. First step was to get access to the fork. Hey, we're an open-source company. That's easy.
2. Step two was to trigger the workflow. Do the PR against our repo, done.
3. Step three, get creative. 

With that whole malicious payload, they now could enumerate, exfiltrate, and do a lot of nasty things. As I mentioned, the branch name was a payload. It looked like this: it's embedded in dispatch-check-patch-conflicts-main, a request to do a curl command that downloads a GitHub gist, which contained a lot of nasty stuff. 

This is automated, it's fast, it runs across multiple repos, and in any repo, it gets access to our GitHub environment variables. If we have a GitHub token with tightly scoped credentials, that's bad. If you have a GitHub token with broad tokens, well, it's even worse. Let's leave it at that.

And what made this impact really, really bad was the way we were storing secrets, which is the way most people store secrets in GitHub. We were using GitHub Secrets. Unsurprisingly, right? It's in the name; that's where you put your secrets, right? GitHub Secrets is very liberal in how it approaches storing and providing secrets. You've got a secret here, have it, have the secret. It's not that secret, right? Oh, oh, maybe it should be. Oh well, oh never mind. Well, yeah, it just gives away secrets to everything available. It puts them immediately into the environment without any additional checks or anything like that. 

So if you have a script like that that then fetches all of the environment, you are getting everything. And that's a real risk. We had actually done some migration. Some of our repos had moved their storage of secrets into Vault—HashiCorp Vault, I'm sure many of you are familiar with it. It allows us to store secrets and provide them to GitHub workflows. But it's a multiple gate-jumping exercise to get them. You have to go fetch the right ones, you have to know... you have to have the OIDC token to be able to request it in the first place. It gets in the way, it slows down an attacker, and it doesn't provide you all the secrets for free immediately. 

Where we had migrated, this impact was minimal, but unfortunately for Grafana, we hadn't at that point, and that's where we saw the attack happen. 

So the attack timeline's pretty simple. At 16:40, the API was open to add this change. At 17:52, the change was applied, and we were immediately vulnerable to anyone running Gato-X and accessing this. Which is actually not immediately what happened. The first thing we had was a report from a security researcher. We have a bug bounty program, and we got a very well-meaning report where they pointed out that this was actually vulnerable. Unfortunately, bug bounty...

**Lessons From a CI/CD Supply Chain Attack at Grafana Labs**

Programs are slow to turn around. We take a while to actually process them. We didn't see this immediately and weren't able to respond to it. Then, at 04:30 the next day, we saw the actual attacker execute Gato-X and start exfiltrating our secrets about 10 hours after the original door was opened. Within 10 hours, the attacker had identified this vulnerability and was immediately using it to steal our secrets.

This is where we got a tiny bit lucky. Our attacker decided to explore the secrets they had and, when they did that around 16:15, they triggered our internal alerting. That's when we got involved and started digging into it. We will talk about how we found that immediately in a moment.

After that, it was a whirlwind of response activities, which took over the weekend and several weeks later. We used a bunch of tools as part of this. One of the key parts was IRM. I'm sure many of you are familiar with using IRM. It's a great tool we use internally for normal operational instances, but also for security incidents, managing coordination, communication, and making sure everyone's on the same page when these kinds of attacks happen.

We heavily used Loki; a large amount of our logs, all the key logs for our instance, went into Loki. We were able to query and find them to understand what happened. We brought in loads of open-source tooling. We used Zizmor, a tool to automatically verify whether or not your workflows in GitHub are vulnerable. We also used TruffleHog to find out if we had any secrets that might be vulnerable in the repositories. Have we placed secrets in repositories? We rectified those as part of it. 

We also used Gato-X, the hunter turned gamekeeper. Gato-X is the tool the attacker actually used, and it's great to verify you are not vulnerable by using the tool the attacker was using. As I said, IRM was a key cornerstone to the entire response process. It really enables easy communication. We use it for security and operational events, and it's available to everyone for free in Grafana Cloud. It has close integration with all our tooling like Slack and Google Docs, simplifying communication to everyone involved, making sure they're aware and informed as necessary.

Of course, we integrate Grafana Alerting tightly into it, so we can move from alert to incident really easily, keeping all that context together and ensuring that the people who needed to know what happened were informed. Loki is, of course, our log storage database, and we used it very heavily throughout this incident. All our key logs from GitHub were being written not only to GitHub storage but also to our Loki. This was really important because attackers can delete logs from GitHub if they have the right permissions, and logs can expire. We have our Loki instance configured to retain our logs so we can go back and look at them, understand exactly what had happened, and see the full extent of the compromise.

Loki also has an incredibly powerful query language. The query languages provided by tools like GitHub are quite limited and do not allow us to investigate properly. But with Loki, we could dig into our logs and find the vulnerabilities and evidence of where those vulnerabilities had been applied.

Moving on to Zizmor, another tool in the open-source ecosystem, working in this ecosystem was extremely helpful in this situation. The tools were available to us immediately when we needed them. A GitHub Actions workflow is essentially a code file. Zizmor is static analysis specifically for those kinds of source codes. It flags certain behaviors and patterns, immediately flagging pull request targets and saying, "This is almost always used incorrectly. Please take a look again if you really need this." It also detects unpinned actions. 

For example, in the last couple of weeks, we as an industry have seen a lot of supply chain attacks. This is something that Zizmor detects, along with other things like injection vulnerabilities. During the incident, we knew that they used one GitHub Actions workflow, but we had more. We weren't vulnerable in more places, so we started scanning all of our repositories, internal and external, with Zizmor. We got a list of prioritized findings—these are the things you need to look at immediately. From there, we started fixing finding after finding and re-enabling workflows for each repo asset we fixed. Needless to say, this now lives in our CI and is a mandatory control.

The fun thing, as we talk about open source again, is that we actually started contributing to this. Our team implemented an automated fix suggestion for Zizmor as an immediate outcome of this incident. 

TruffleHog, which we've also spoken about, is a tool that was used by the attacker. In essence, it's a dual-use tool; it can be used for good and bad. It finds secrets and can verify these secrets against live services. For example, if you find a secret that is supposed to be a GitHub token, you can ask GitHub, "Is this a valid secret? Is it up to date?" The same goes for AWS and all other secrets and tokens you can get your hands on. From a log perspective, it looks a lot like normal auth traffic, so it doesn't stand out in terms of normal log analysis. However, since one of the tokens I accessed was a canary, that is what triggered us to respond to this. 

Neither of these tools replaced human judgment, but they sped up our response from days to hours. Obviously, we have to talk about Gato-X. This was the attacker's tool and also our tool during the response. In a way, it's similar to Zizmor; it scans for vulnerable GitHub Actions workflows but takes it one step further by trying to exploit them. It maps the paths and tries to execute them. Running it ourselves gave us an attacker's eye view. Finding the list using Zizmor gave us a net list to fix these things. Then we tried Gato-X to see if there was something we had missed. It is extremely disorienting to do during a live incident, but it's also very useful. 

A question I would like to leave you with regarding Gato-X is: assume that these kinds of tools will be used against you. Are you running it yourself first? 

I should probably say that the logo we are using for Gato-X was not Gato-X's official logo. There isn't one, sadly, but Gemini's best attempt at what it might look like did not do a bad job, I think. 

So how did we actually find this in the first place? We did this thanks largely to security canary tokens. Canary tokens are a really simple idea. You create tokens that have no permissions; they can't do anything at all. They're limited in access, only having access to an empty project, and they can't do anything anyway. But when anyone uses them to authenticate in any part of your system, you send an alert to security. That's exactly what we have distributed throughout all of our infrastructure. They look just like juicy AWS keys, something an attacker loves to find. But when they pull the top off and try to do anything with it, that's when we get alerted and find out that it's being compromised.

This really changes the dynamic for a hacker. Without canaries, they're a child in a chocolate factory. Every tasty, sweet-looking treat is available to grab and delicious without consequence. But if they're in your environment, suddenly they change the world.

**Changes.** It's a nightmarish parallel Willy Wonka dowdy-esque hellscape where all the sweet treats suddenly also could be poison, worrying that anything they touch might make them blow up like a giant glowing orb visible to everyone. It was actually thanks to Trufflehog's validation feature that we found this attack. Trufflehog tried to validate our canary token, connected, made an authentication attempt, and oh, we're getting alerted about it now. 

Though I will note that if you are using, sadly, Trufflehog... Sorry, Thinkst free offer in this space, Trufflehog knows how to pick it up and it will actually not try to validate the free Thinkst token, sadly. Annoying.

So, the response pipeline, as we said at 04:30, we had the attack event. GatoX was used to compromise Grafana, stealing all our tokens. Our canary token then fires at 6:15, where they used Trufflehog to validate the tokens and fired our canary token. We kicked off an incident at 08:00, having understood the threat of the compromise and the importance of it. IRM was, of course, integral in that response. 

We started digging into all our logs and fully understanding the breadth and full depth of that compromise by 11:00 using Loki. Over the next day and continuing days, we started using Gato-X, Trufflehog, and Zizmor to try and make sure we weren't going to be vulnerable to this again.

And obviously, we wouldn't be at GrafanaCON without having at least one Grafana dashboard in our presentation. This one is specific to Trufflehog, but we have similar for Zizmor and other relevant tools. Specific to Trufflehog, just because you've blocked a PR in your CI, that doesn't mean that it's safe. The secret is still there and got git log somewhere. So the rotation of that secret is mandatory. Having it blocked is one thing, but getting this kind of observability that makes it actionable. You can build alerting features around it. 

As you see here, we have 192 repos that have been scanned with 666 scans running total. It scales with finding scans with findings, seven. But these are all known things that we want there. The important thing here is verified secrets, zero. If that number ever were to go up, automatically we would get an alert and be able to start working on that, rotating... making sure that the secret has been rotated. 

Goes without saying, but detection without visibility, that's noise. This is how you turn findings into action. 

**To recap.** What went right? What were the lessons that we learned? Preparation beats reaction every time. Canaries, static analysis, secret hygiene, all of that makes you able to respond, not react. And observability. It's not just something you have for production; you need it in CI/CD as well. 

And don't just take our word for it. Adnan Khan, the author behind Gato-X, said, "Ooh, looks like Grafana was hit by an attack recently." We were able to respond within a really, really short timeframe to this tweet and then got this response: "Kudos to the Grafana team for breaking up the attack. CI/CD detection engineering is non-existent in most places. Should be good for others to learn from this." Open source is a security advantage, not only for attackers but by defenders too. 

And the customer impact post that Nick alluded to earlier, you earn the right to make that post by doing the work beforehand. 

**So the lessons we learned.** Well, we moved all our secrets from as easy as it was to use into vault. It was a more secure environment that was harder to use. We introduced a bunch of pain to a bunch of our teams, sadly. But it was the right choice. We'll talk a bit more about why that was in a second. 

We implemented mandatory Zizmor and Trufflehog scans. Every PR against any GitHub repo in the Grafana org will automatically have Zizmor and Trufflehog run against it. Some of you may know, you may have seen it yourself. We've broadened our canary token coverage. You can always have more canary tokens; they can just go anywhere. So we dropped them around, just trying to make it a bit more hellscapey for those attackers. 

We really reduced... One of the impacts here we haven't talked too much about is GitHub Apps and how broad their accesses can be. It can really be a significant impact. We really shrunk those. We broke down existing super users that were able to access anything and really reduced their accesses. 

And of course, we had to do a bit of user education. Okay, I hold my hand up and say, I am not a GitHub workflow security expert. I have an understanding of it and I have learned a lot over the multiple incidents we've encountered at Grafana, but very few people are experts, and it's really easy to miss those kind of little weird edge cases that you wouldn't necessarily think to be a problem. 

That education meant that actually when we had similar incidents again, as many of you may know, there was an Aqua security breach where their Trivy scanner was compromised in a supply chain attack against many people. Axios, in a similar way, got hacked in a very similar way. We got touched by these, but we were not hit by them. 

What I mean there is that because of the work we've done to limit the scope of attack access and so on and so forth, we really prevented the attackers who hit us via these from actually stealing anything. We were able to verify that within hours, not weeks of effort, which significantly reduced their cost. 

And with that, we are finished. Thank you very much. 

*(audience applauds)*

## Raw YouTube Transcript

- Good morning, Barcelona. Try that one again. How are you all? Hope you are enjoying GrafanaCON. We're gonna be talking through lessons from a security incident where everything went wrong. Really almost everything
that could go wrong, did go wrong, but it all ends up right in the end. So my name's Nick. I'm a principal security
engineer at Grafana. I'm in the Detection and
Response Engineering Team, possibly a team we named
purely for the abbreviation. I can't confirm or deny that. And when I'm not busy tracking down people trying to hack Grafana, I do actually like doing a bit of running. I like going up and down mountains. I've run up and down the
hills around Barcelona already and occasionally run further
than most people like to drive. And I'm joined here by- - David. First off though. A little bit of running, that's a euphemism for 180 miles last a couple of weeks ago? - Yeah, something like that.
- Somewhere there around. Good, so yeah, David Andersson, I work at the Security
Engineering Team at Grafana. We don't have such a fancy abbreviation, but we do everything from
secure best practices, how to implement secure coding principles and these kind of things. Not an avid runner, but I like to be on stage, mostly singing, dancing on occasions, and also enjoying sitting in the audience enjoying musical theater. All right. - So we're gonna take you
through a Saturday morning. Do you hear that, David? It sounds a bit like a canary singing. Well, it was an otherwise normal weekend. We woke up, we got up, we looked at our phones and went, "Hmm, that's a weird alert. I've not seen that one before." Two eagle eyed security team members just happened to notice a
particularly concerning alert that had popped up. And normally we don't
worry too much about this, but this one was... This was a big one. It was actually indicating that there was a complete
CI/CD compromise. All of our s have been exfiltrated by an attacker and at that point, most organizations are going, "Oh god." In fact, most people, anyone is thinking, "Oh God, this is the worst possible outcome." But yet in fact, we were able to write, very shortly after actually, that there had been no customer or user impact whatsoever. We were able to show there had been... Nothing had actually been
done with those secrets that actually had any outcomes. But we're gonna tell you that
story of how we got there, the problems that we
encountered at the beginning, how it happened, and then how we investigated, rectified and the changes we made to make Grafana more secure. So I'm gonna hand back to David. Thank you. - Before going into the
details of the actual hack and the actual incident, I wanna talk a bit about
these two triggers. So for those of you who
have worked with GitHub, you're aware you have two triggers that you can use when responding to a pull request in GitHub actions. One is pull request, the other one is pull request target. They look so alike, they are in fact not. So pull request, this is a safety vault. You're in your... Your developers, your fork maintainers, what have you, the one forking your code, they run their workflows in their context. It's a safety vault. No access to your environment, no access to your secrets, all fun. Pull request target, not so much. Immediately they have access to your repo with your secret and it
becomes your problem. So it has a legitimate purpose. It's designed for maintenance task, automated labeling, these kind of things. But the thing is, when you combine pull request target with something that a user can control, all of a sudden, the fork code becomes trusted code. So this small change
here is the gap between looks safe and is safe. Fast forward to April 25th. We had one small change. It looked benevolent. It was internally contributed
by a Grafana employee. Looked a lot like CI improvement. What happened though is we had pull request moving
to pull request to target with a combination of this script request. So with that, the user checked out the code, made a pull request against us and executed... And GitHub Actions executed the command. And this is the combination that mattered. So any contributor could
then run arbitrary commands against our secrets. One merge is all it took and the door was open. And I wanna highlight
this line right here. So again, if you're familiar with GitHub, it has a lot of built-in features and GitHub repository
automatically populated GitHub SHA, automatically populated
GitHub head ref though, that's GitHub speak for
the name of your branch. That's what it took. This was the attack vector. And this is completely user controlled. So the payload here, it wasn't something fancy, it wasn't a zero-day with sophisticated... Well, obviously it was
a hacker with a hoodie, we all know that. But it wasn't sophisticated
in any other way. The payload was a branch name. We've looked at the door now or introduced the concept of the door. What did the key looked like then? So the attacker used Gato-X, we know this, we will get to it a bit later. But Gato-X is a tool
designed to be used at scale. It scans GitHub organizations at scale. It finds vulnerable
GitHub actions workflows, it maps them and it actively
tries to exploit them. This was done in a three step process. First step was get access to the fork. Hey, we're an open source company. That's easy. Step two was to trigger the workflow. Do the PR against our repo, done. Step three, get creative. So with that whole malicious payload, they now could enumerate, they could exfiltrate, they could do a lot of nasty things. And as I mentioned, the branch name was a payload. It looked like this. It's embedded in
dispatch-check-patch-conflicts-main, a request to do a curl command
that downloads a GitHub gist, which contained a lot of nasty stuff. So this is automated, it's fast, it runs across multiple repos and in any repo it gets access to our GitHub environment variables. And if we have a GitHub token with tightly scoped credentials, that's bad. If you have a GitHub
token with broad tokens, well, it's even worse. Let's leave it at that. So- - And what made this
impact really, really bad was the way we were storing secrets, which is the way most people
store secrets in GitHub is we were using s. Unsurprisingly, right? It's in the name, that's where you put your secrets, right? And s, it's very liberal in how
it approaches storing and providing secrets. You've got a secret here, have it, have the secret. It's not that secret, right? Oh, oh, maybe it should be. Oh well, oh nevermind. Well, yeah, it just gives away secrets to everything available. It puts immediately into environment without any additional
checks or anything like that. So if you have a script like that, that then fetches all of the environment, you are getting everything. And that's a real risk. We had actually done some migration. Some of our repos had moved
their storage of secrets into Vault. HashiCorp Vault, I'm sure many of you're familiar with it. It allows us to store secrets and provide them to GitHub workflows. But it's a multiple gate
jumping exercise to get them. You have to go fetch the right ones, you have to know... You have to have the OIDC token to be able to request
it in the first place. It gets in the way, it slows down an attacker and it doesn't provide you all the secrets for free immediately. Where we had migrated, this impact was minimal, but unfortunately for Grafana, Grafana, we hadn't at that point and that's where we saw the attack happen. So the attack timeline's pretty simple. 16:40, the API was open
to add this change. 17:52, the change was applied and we were immediately vulnerable to anyone running Gato-X
and accessing this. Which is actually not
immediately what happened. The first thing we had was a report from a security researcher. We have a bug bounty program and we got a very well-meaning report where they pointed out that
this was actually vulnerable. Unfortunately, bug bounty
programs are slow to turn around. We take a while to actually process 'em. We didn't see this immediately and weren't able to respond to it. And then after that, at 04:30 the next day, we are seeing the actual attacker execute Gato-X and start
exfiltrating our secrets about 10 hours after the
original door was opened. So within 10 hours, the attacker had identified
this vulnerability and was immediately using it
to actually steal our secrets. This is where we got a tiny bit lucky. Our attacker decided to actually try and explore the secrets they had, see what they had. And when they did that about at 16:15, that's when they triggered
our internal alerting and that's where we got involved and started digging into it. And we're gonna talk about how we actually found that
immediately in a moment. After that, it was then a whirlwind
of response activities, which took over the weekend
several weeks later. And so we used a bunch
of tools as part of this. One of the key parts was IRM. I'm sure many of you
are familiar using IRM. It's a great tool we use internally for normal operational instance, but also security instance, managing coordination, communication and making sure
everyone's on the same page when these kind of thing attacks happened. We really heavily used Loki, a large amount of our logs, all the key logs for our
instance went into Loki and we were able to query and find them and understand what happened. We brought in loads of
open source tooling. We've brought in Zizmor, this is a tool to automatically
verify whether or not your workflows in GitHub
are vulnerable or not. We used TruffleHog to try and find out have
we actually got any secrets that might be vulnerable
in the repositories? Have we placed secrets in repositories and we rectified those as part of it? And we also used Gato-X, the hunter turned gamekeeper, Gato-X is the tool the
attacker actually used. And it's great to be able to
verify you are not vulnerable by using the tool the attacker was using. So as I said, IRM was a key kind of cornerstone to the entire response process. It really enables easy communication. We use 'em for security
and operational events and it's available to everyone
for free in Grafana Cloud. It's got really close
integration with all our tooling like Slack and Google Docs. Just simplifying, communicating to everyone who's involved what's going on and making sure they're aware and informed as necessary. And of course, we integrate Grafana
Alerting tightly into it. So we are able to move from
alert to instant really easily and keeping all that context together, making sure that the
people who needed to know what happened knew. Loki is, of course, our log storage database and we used it very heavily
throughout this instant. All our key logs from
GitHub were being written not only to GitHub storage
but also to our Loki. And this was actually really important. Attackers can delete logs from GitHub if they have the right permissions, they can... Logs expire. We have our Loki instance configured to make sure it retains our logs so we can actually go
and back and look at them and make sure understand
exactly what had happened and see the full extent of the compromise. And incredibly powerful
query language as well. The query languages provided
by tools like GitHub are really quite limited honestly and really, really don't allow
us to investigate properly. But with Loki we could
actually dig into our logs and really find the vulnerabilities and find the evidence of
where those vulnerabilities have been applied. - Moving on to Zizmor, another tool in the open source ecosystem. This... Working in the open source ecosystem was extremely helpful in
one of these situations. The tools were available to us immediately when we needed them. So a GitHub Actions workflow
is essentially a code file. What Zizmor is is static analysis, specifically for those
kind of source codes. What it does, it flags certain behaviors, certain patterns, so it immediately flags
pull request target and says that, "This is almost always used incorrectly. So please take a look again
if you really need this." But it also detects unpinned actions. For example, the last couple of weeks, we as an industry have seen a
lot of supply chain attacks. This is something that
Zizmor detects again, but also other things, injection vulnerabilities and a bunch of these things. What we did during the
incident was, all right, we know that they used one
GitHub Actions workflow, we have more. We weren't vulnerable in more places. So we started scanning
all of our repositories, internal and external with Zizmor. We got a list of prioritized findings. These are the things you
need to look at immediately. And from there on, we started to fix finding after finding and re-enable workflows for
each repo asset we fixed. Needless to say, this now lives in our CI
and is a mandatory control. The fun thing though as... Talking about open source again and again, the fun thing is that we actually started contributing to this. Our team implemented an
automated fixed suggestion for Zizmor, it's immediate outcome of this incident. Trufflehog, we've also
spoken a bit about this, a tool that was in fact
used by the hacker, the attacker. But in essence, it's a dual use tool. It can be used for good and bad. What it does is it find secrets and you can ask it to verify these secrets against live services. So for example, if you find a secret that is
supposed to be a GitHub token, you ask GitHub, "Is this a valid secret? Is it up to date?" Same goes for AWS and all other secrets and tokens that you can get your hand on. From a log perspective, it looks a lot like normal auth traffic. So it doesn't stand out in
terms of normal log analysis. But since one of the tokens
I got access to was a canary, that is what triggered
us to respond to this. Neither of these tools
replaced human judgment, but it sped up our response
from days to hours. And obviously we have
to talk about Gato-X. This was the attacker's tool and actually our tool during response. So in a way it's similar to Zizmor, it scans for vulnerable
GitHub Actions workflows, but it takes it one step further. It actually tries to exploit them. So it maps the paths. it tries to execute them. And running it ourself, well, it gave us an attacker's eye view. So finding the list using Zizmor, gave us a net list to fix these things. Then we tried Gato-X, is there something that we have missed? It is extremely disorientating to do during a live incident, but it's also very, very useful. But a question I would
like to leave you with in regards to Gato-X is assume that these kind of
tools will be used against you. So are you running it yourself first? - I should probably say that also the logo there we're using for Gato-X was not Gato-X official logo. There isn't one sadly, but Gemini's best attempt
at what it might look like. It did not a bad job, I think. So how did we actually find
this in the first place? And we did this thanks largely
to security canary tokens. So canary tokens are a really simple idea. You create tokens that
really have no permissions, they can't do anything at all. They're limited in access. They only have access to an empty project and they can't be able
to do anything anyway. But when anyone uses them to authenticate in any part of your system, you send an alert, you send an alert to the the security. And that's exactly what
we have distributed all the way through all
of our infrastructure. They look just like juicy AWS keys, something an attacker loves to find. But when they pull the top off and try to do anything with it, that's when we get alerted and find out that it's being compromised. This really changes the
dynamic for a hacker. Okay, without canaries, they're a child in a chocolate factory. Every tasty sweet looking
tree is available to grab and delicious without consequence. But if they're there in your environment, suddenly they change, the world changes. It's a nightmarish parallel Willy Wonka dowdy-esque hellscape where all the sweet treats
suddenly also could be poison, worrying that anything they
touch might make them blow up like a giant glowing
orb visible to everyone. And it was actually thanks to Trufflehog's validation feature that we found this attack. Trufflehog tried to
validate our canary token, connected, made an authentication attempt and oh, we're getting alerted about it now. Though I will note that if you are using sadly Trufflehog... Sorry, Thinkst free offer in this space, Trufflehog knows how to pick it up and it will actually not try to validate the free Thinkst token sadly. Annoying. So the response pipeline, as we said 04:30, we had the attack event. GatoX was used to compromise Grafana, Grafana stealing all our tokens. Our canary token then fires at a 6:15 where they used Trufflehog
to validate the tokens and fired our canary token. We kicked off an instant at 08:00, having understood the
threat of the compromise and the importance of it. And IRM was, of course, integral in that response. We started digging into all our logs and fully understanding the breadth and full depth of that
compromise by 11:00 using Loki. And then over the next
day and continuing days, we started using Gato-X, Trufflehog and Zizmor to try and make sure we weren't going to be vulnerable to this again. - And obviously we
wouldn't be at GrafanaCON without having at least
one Grafana dashboard in our presentation. This one is specific to Trufflehog, but we have similar for Zizmor
and other relevant tools. And specific to Trufflehog, just because you've
blocked a PR in your CI, that doesn't mean that it's safe. The secret is still there
and got git log somewhere. So the rotation of that
secret is mandatory. Having it block is one thing, but getting this kind of observability that makes it actionable. You can build alerting features around it. So as you see here, we have 192 repos have been scanned with 666 scans running total. And scales with finding
scans with findings, seven. But these are all known
things that we want there. The important thing here
is verified secrets, zero. And if that number ever were to go up, automatically we would get an alert and be able to start
working on that, rotating... Making sure that the
secret has been rotated. Goes without saying, but detection without visibility, that's noise. This is how you turn findings into action. All right, to recap. What went right? What were the lessons that we learned? Preparation beats reaction every time. Canaries, static analysis, secret hygiene, all of that makes you be able to respond, not react. And observability. It's not just something
you have for production, you need it in CI/CD as well. And don't just take our word for it, Adnan Khan, The author behind Gato-X said, "Ooh, looks like Grafana was
hit by an attack recently." We were able to respond within a really, really short
timeframe to this tweet and then got this response. "Kudos to the Grafana team for breaking up the attack. CI/CD detection engineering is
non-existent in most places. Should be good for others
to learn from this." Open source is a security advantage, not only for attackers, but by defenders too. And the customer impact post that Nick alluded to earlier, you earn the right to make that post by doing the work beforehand. - So the lessons we learned, well, we moved all our secrets from s as easy as it was to use into vault. It was a more secure environment
that was harder to use. And we introduced a bunch of pain to a bunch of our teams, sadly. But it was the right choice. And we'll talk a bit more
why that was in a second. We implemented mandatory Zizmor and Trufflehog scans. Every PR against any GitHub
repo in the Grafana org will automatically have
Zizmor and Trufflehog run against it. And some of you may know, you may have seen it yourself. We've broaden our canary token coverage. You can always have more canary tokens, they can just go anywhere. So we dropped them around, just trying to make it
a bit more hellscapey for those attackers. And we really reduced... One of the impacts here we
haven't talked too much about is GitHub Apps and how
broad their accesses can be. It can really be a significant impact. And we really shrunk those. We broke down existing kind of super users that were able to access anything, really reduced their accesses. And of course, we had to do a bit of user education. Okay, I hold my hand up and say, I am not a GitHub
workflow security expert. I have an understanding of it and I have learned a lot
over the multiple incidents we've encountered at Grafana, but very few people are experts and it's really easy to miss those kind of little weird edge cases that you wouldn't necessarily
think to be a problem. And that education meant
that actually when we had similar incidents again, as many of you may know, there was a Aqua security breach where their Trivy scanner was compromised in a supply chain attack
against many people. Axios in a similar way got
hacked in a very similar way. We got touched by these, but we were not hit by them. And what I mean there is that because of the work we've done to limit the scope of attack
access and so on and so forth, we really prevented the attackers who hit us via these from actually stealing anything. And we were able to
verify that within hours, not weeks of effort, which significantly reduce their cost. And with that, we are finished. Thank you very much.
- Thank you all. (audience applauds)

