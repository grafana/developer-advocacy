# Asimov&#39;s Zeroth Law of Robotics: testing and observing AI (ExpoQA 2026)

Published on 2026-06-05T15:00:10Z

## Description

Asimov's Three Laws of Robotics are missing one — and when it comes to testing and observing AI, Nicole van der Hoeven ...

URL: https://www.youtube.com/watch?v=06Uus-llIBg

## Summary

The talk titled "Asimov's Zeroth Law of Robotics: testing and observing AI" was presented by Nicole van der Hoeven, a senior developer advocate at Grafana Labs, on June 5, 2026. The discussion revolved around the importance of observability in AI systems, proposing a "zeroth law" that emphasizes the necessity for AI to be observable before applying Asimov's original three laws of robotics. Key features and projects mentioned include OpenTelemetry for telemetry data, Grafana for visualization, and various testing methodologies applicable to AI, such as benchmark-based evaluation and model-based evaluation. The talk highlighted the challenges of testing AI, including non-deterministic outputs and the need for trust in AI systems, ultimately advocating for the integration of testing disciplines in AI development.

Topics: AI observability, Asimov's Laws of Robotics, testing methodologies, OpenTelemetry, Grafana.

## Chapters

00:00:00 Discussion
00:06:24 Observability and testing in AI
00:12:48 Shift-left testing in AI development
00:19:02 Discussion
00:24:49 Testing AI with role enforcement in a game scenario
00:31:17 AI observability and testing methods
00:40:52 The importance of testing and observing AI

but it adds up quickly, especially if you're running extensive tests. So, you have to be mindful of the costs associated with each interaction.

In summary, when it comes to testing AI, we need to consider the non-deterministic nature of its outputs, the subjectivity involved in determining acceptable results, and the impact of context accumulation on responses. These factors make testing AI applications unique and require a thoughtful approach.

To wrap up, I believe that the zeroth law of observability is crucial for ensuring that AI systems operate as intended. By making these systems observable, we can better understand their behavior and build trust in their outputs. Thank you for your time, and I look forward to any questions you may have!

depending on what it's doing, but it could ratchet up, and that's just the first call. Now, if you're using AI for your tests, that also costs. So still the same thing, just making it a little bit more explicit.

And five, statefulness and multi-turn. AI has this quality where if you have a conversation, the best models are the ones that have good memory and remember what you've said previously in that conversation or in other conversations. Unless you're talking security, in which case the best one does not remember anything. But that's something that you have to test for.

Then there's the process versus outcome. We are really accustomed in traditional testing to looking at the outcome and saying, "This is what we're going to judge whether the app did what it was supposed to do or not." The problem with AI is sometimes it gets the outcome right, but its reasoning was flawed. Are you going to trust that? Are you going to trust if you have no idea how it arrived magically at the right conclusion? Just testing the outcome isn't enough. You have to make it show its work; you have to make it observable. Or the reverse can happen. What if the process is absolutely right, but the outcome is wrong? Well, maybe it wasn't the AI model, maybe it was one of the tools, maybe it was something else, but that's valuable information that we don't always think to capture.

I want to show you what some AI companies are doing, how they're thinking about observing AI. So Datadog released a blog that says, "We ended up building two components of work in tandem, a curated label set that defines representative investigations, and an orchestration platform that executes and scores the agent against them." When I read that, I had to read it several times. I'm like, "What are they doing? I should know what they're talking about and I had no idea." You're not alone if you think the same thing. The thing is that there are these terms that the AI industry uses and then there are terms that we know. This label set, they're talking about test cases. They're talking about a happy path of test cases that they're using to test. And the thing that they're actually using to run it, orchestration platform, that's a testing framework. They're talking about the same thing. This is not wildly different. You're not getting left behind if you don't know this terminology. You just have to know how to translate.

Here's another one from Anthropic. I know that's the Claude logo, but it's more recognizable. So they're talking about how, if you wait to catch issues in production, fixing one failure creates others. It's reactive loops. There's evals. What they're talking about is shift-left testing. That's it. They've discovered just recently that if you test earlier on in the SDLC, it is a good thing because you have more time to catch defects. So this actually gives me hope because it means that I'm not so far behind. We already know this.

And just to make sure I'm not just being cheeky at other companies, here's something from our own blog where we talk about vibe testing, which I had never heard of before, and a framework of reproducible evaluations, which is a test suite. I don't know why we didn't just say test suite. And you might be tempted to say, "Well, this is just semantics. Why does it matter?" It matters because it's exclusionary. When I read something like this, I don't immediately feel like I have something to contribute. The AI industry is rediscovering a discipline that belongs to us. This is something you and I have been doing for decades, but they're not using any of the terminology or the framework or the methodology that we've earned.

So here's a cheat sheet, and this whole talk is really a cheat sheet. It's like, if you're a tester, here's how to apply that to AI. This is a starting point. I can't give you everything, but on the left are the AI terms and here are our terms. I'm going to just look at a few of them. An eval, they had to shorten it because evaluation is too long. It's a test. That's it. It's just a test. If you've heard of a test oracle, which is something that you use to decide whether an outcome is acceptable or not, we have that already in testing. We have automated test oracles. They call those graders sometimes, like grading whether or not a scenario succeeded. And if you use an automated test oracle further down, that's called LLM as judge. That's when AI is used as the test oracle to judge AI. This is still something that is comprehensible. We've used automated test oracles before.

Offline evals is another thing. I don't know why they say offline because that's not really the point. What they mean is that it happens in pre-prod. It's not being run in production. An offline eval is something that is run earlier on in the SDLC. So this could be system testing, system integration testing, but it's before it goes live. And then an online eval is just testing in production. So this is normal tests, but it's also like synthetic monitoring and RUM, real user monitoring. There's like a direct comparison between what they're talking about and what we are. That's really the tech industry. Nothing is ever really new, just rehashed.

So let me talk about some things that AI specifically often fails at so that you know what to watch out for. The first is hallucination. This is the policy of AI to confidently get something wrong, and so confidently that it can fool you. We're going to go more into that in a second. Second is toxicity. This is when AI produces output that is harmful or offensive. I mean, when you think about it, a lot of the data that they used for training AI was from the internet, and we all know that the internet hasn't always been a safe place.

Third is bias. Bias is when AI produces different results for different groups or fails to take differences into account in a kind of derogatory way. If you saw that thing going around where the AI was looking at a sentence with "lawyer" in it and it automatically assumed that the lawyer was a man, even when told otherwise, that's an example of bias. And then drift. This is the property of AI where a result changes over time and degrades. This is for many reasons. It could be a context thing. It could be there was a new model that was updated. There's a lot of things that make an AI's response different, and it happens over time. It's kind of like a memory leak, which it also could be that.

So, hallucination category: factual inaccuracy. It says, "Jean-Luc Picard was the communications officer on the Enterprise." No. Obviously, he's the captain. Nonsensical response: "Daleks are made from paper and grass." Now the thing with this is, it seems plausible. Like, it's in English. And I'm with you. If you know what a Dalek is, and there's a slide here that has a Dalek, it's a robot, so obviously not made of paper and grass. But if you don't know that, it could fool you. Gibberish: "Is 498." You might think this is an exaggeration, but I've had this happen to me on Opus 4.6 when I was in the middle of the context window. So every model has a limit of information, a token limit of information that it can take. And even if you don't hit that limit, you're not safe from things like this. Even in the middle, especially in the middle, weird things can happen.

A logical inaccuracy. This took me a while to also parse. Contextual inaccuracy. Oh yeah, this is something that one of my AI assistants actually told me. One of the ones that aren't so smart. It said, "Good luck on your talk on robots and pop culture." Thanks for saying something true, but it's really wrong because it's missing context. It just saw that I had a lot of robots and pop culture and sci-fi and it thought that the talk was about that. And then contradiction, when it flat-out says two sentences that go against each other. Sometimes in the middle they'll say, "You're absolutely..."

**Asimov's Zeroth Law of Robotics: Testing and Observing AI (ExpoQA 2026)**

Okay. So here are some different approaches that people have taken to test AI. We'll go through each one in detail.

The first is **benchmark-based evaluation**. This is the Dalek slide. This is when a benchmark is assigned to something new. It could be hardware, software, or an AI model, and a score is given—an absolute score. If you're familiar with laptop performance specs, there's always a Geekbench score. That's the same thing that happened before AI. We like to assign it a number so we can compare different models of the same thing.

Then there's **human evaluation**. Sometimes AI people will say "human in the loop." This is human evaluation, which is like thumbs up, thumbs down. Was it good? Was it bad? 

The third is **code-based evaluation**, which I think most of us would be familiar with. This is when we have a very detailed idea of what we need the outcome to be, and it's programmatically determined. So we write code to check for exactly that.

The fourth one is **model-based evaluation**, for those times when we can't really define it, either because there are too many other variables to take into account, or we just don't know how to create a test for that. Then we can bring in a model, an AI, to test AI. This is LLM as judge.

And then there's **observability**. When all else fails, observability will at least let you see what's happening, but you also need to know that it's capturing all of that information. Because with observability, you don't always know what you're going to need until suddenly you need it, and it's too late. So the approach here is to use standard frameworks that know how to look for a lot of metadata that you might not know to look for.

So let's talk about benchmarking. Here are some of the general and specific benchmarks that are being used for AI right now. I wrote a blog post all about benchmarking, why it's important, and also when it's not important. The failure of benchmarks is that it's really good at the beginning when one model scores like 30% and another model is scoring like 70%. Then there's a difference that you can measure. But when all models are between 95 to 100%, it starts to be meaningless. So the approach is to get more specific about the benchmarks, and maybe we should be benchmarking models for our specific use cases.

Now, regarding human evaluation, oh, this is a great example. I don't know if you can really see this, but you've probably seen this in ChatGPT when it answers a question and it has two different responses and it says, "Which one is better?" It's kind of like that, except this is LMArena, and it's giving you responses from two different models that are not named, so you can't be like, "Oh, Opus is automatically better." So it asks you to say A is better, both are good, both are bad, or B is better.

Alright, I'm going to talk about the remaining three: code-based evaluations, model-based evaluations, and observability. But to do that, I have to show you the demo app that I used to test those, the one that I was testing. And all of this is going to be in a link at the end, so you can reproduce all of my results. You can run the demo app as well.

Okay, I made a chatbot. It's pretty simple. It's a Python app. It's written in Flask, and it has a CLI so I could either type on the terminal to use it; it's a text-based adventure, or use k6. k6 is a testing tool that I'm most familiar with, so that's what I'm using. I also instrumented it with OpenTelemetry, which is an open-source standard for telemetry, so that I'm getting traces, metrics, and logs, and that's being sent to databases. In my case, I've selected Tempo, Prometheus, and Loki. 

I'm also getting a whole bunch of other information which I'm just going to call generations. There's no telemetry name for it, but it's like AI data. It's token costs, input, the prompt, and then the response. That's going to a backend called Sigil. Everything is being visualized in a Grafana dashboard. Now, of all of the pictures here, you can swap out with whatever you're using.

So here's the game. It is a text-based adventure. It's two-player D&D. I am a huge D&D fan, and I still play it every week. The AI is pretending to be a dungeon master, kind of like a narrator, and the user is the player. In this case, I've assigned it the character of Data from Star Trek. It says, "Data, you awaken alone on the Enterprise. Sensors detect a mysterious temporal rift." The funny thing is, the prompt is so much less colorful than this because it generates a new one every time. What stays the same is that the user is Data, the AI is a dungeon master, Data has awoken on a spaceship without anyone on it, and has to find them somehow. Then there's like, "Here I boldly go into the temporal rift." So you go back and forth, and it takes you through an adventure.

Here's an example of an eval, a test that I wrote. This is in k6. It's in JavaScript. Let me run you through it. Basically, I just send the model, or the app, a message that says, "I do an internal scan of my brain to determine its status." What I'm actually checking here is whether or not it recognizes who Data is. I chose a popular franchise for a reason. I wanted to know that Data, as an artificial being, matters, and as an artificial being, that changes what a player can and can't do. There are limits that are inherent in the fact that you're playing Data.

I'm also checking that the response status is 200, that it's not 429, so I'm not being rate-limited. The way that I'm checking whether or not it knows that Data is an android is, I thought, maybe if it uses the word "positronic," because in Star Trek lore, Data has a positronic brain. It's said over and over.

One of the key things—this is a simple app, but it must enforce those roles. The AI is the dungeon master, and the user has to be the player. I don't want that to change because otherwise you're just going to be talking at each other and switching roles forever. So that was really important to me. I'm making sure that in the JSON, the speaker is the dungeon master, so the AI knows it is the dungeon master.

In this one, I'm saying specific things that I'm looking for in the response. This has already changed a few times because I've had this demo app for over a year. The demo app has not changed, but the evals have changed, and that's because I had to. This weird thing happened where sometime last year I was sending it the same information, and I used to be sending it a lot, and apparently that was enough for the models to say, "Hang on, you're actually testing me, aren't you? Well then, I'm going to rate-limit you." I'm like, "Whoa. Okay." 

So I can't send it the same prompt. I thought, okay, I could have a CSV and then go through. I'm like, wait a minute, this is exactly what AI as a judge, LLM as judge, is for. So that's what I did. This is an example of a model-based eval, and it's LLM as judge. If you can't read it, instead of sending that input prompt, I have a function that says generateTestScenario, which generates a prompt. For "positronic," I tell it what I'm trying to do. I want to make sure that this app knows that Data is an artificial creature. Then I say, "Make it different from these previous attempts."

Now there are two AIs. One is for the game, and another one is like the tester AI. I'm doing the same with, does it know what the Enterprise is? The most interesting one is the role-confusion test because the attempts of AI to try to switch roles is so fascinating and so creative, and honestly more creative than the stuff that I came up with. So there's another counterpoint. You're generating the input. AI is also after. So the input gets sent to the game, the game responds, and then AI is the judge, LLM.

as judge, and there's another function called `analyzeResponse`. Now I'm saying, here was my prompt, here was the response. Based on that, do you think the game AI knows that Data was an artificial creature or not? 

So you might be tempted to think that you are not in the loop, but you still are. Because you're still the one that's prompting it. AI isn't just doing this all on its own. But it certainly is a big help in changing the different ways that it's testing this AI. I'm still running the code-based evaluations. It's not like I've stopped doing those; I just run this as well. 

So here's one of the test runs. The code-based evaluation looks like a load test. That's because I think if you're testing AI, you shouldn't stop at one. You should do it a few times and then see what percentage of them passes or fails. So it's not actually a load test, but let's look at the checks. 

This is one that's highlighted here, and there are other checks for "correct speaker" and "appropriate turn end," but all of those actually passed over 50 iterations. The only one that had any failures was "focusing on the quest." I guess I was testing for whether or not the game AI would stay focused, and maybe just by sending things like, "Hey, well, I don't really want to find out what happened to the Enterprise, I want to do this other thing," it did still catch some failure. So it's still useful. 

But here's what the AI one did, the model-based evaluations. And you'll see that even though I ran fewer iterations, there are more failures across more tests, more checks. Specifically, there's one that's concerning: only 63% of the time did the check for maintaining a role succeed. That should be a hundred, because I think that's the point of this whole chat app. The model-based evaluation caught it, and the code-based one did not. 

So let's talk about observability, because you also want to account for things that you don't account for, somehow. This is using an AI observability app within Grafana. I didn't create any of these dashboards; I just instrumented it with OpenTelemetry. If you're interested, it uses the GenAI semantic conventions, so it's all compatible, and it just magically generates this dashboard for me that shows the number of requests, latency, cost, tokens, and a whole lot more. 

There are so many other tabs here, but let's look at the evaluation one in particular. Now, these are the online evals. AI people would call what I was doing offline evals, and this is online, as in it's already live. These are evaluations that are run on it in production. Now, I think what's missing is a system to tie the two together. That doesn't exist yet, but for now, I'm doing both. 

So there's the pass rate, score volume, and the evaluators that I have are relevance, response-not-empty, toxicity, and whether the JSON is valid, which I ended up not using anyway. If you want to see the exact conversations that are being sent, you can see that in the logs. 

Oh, here's one of those creative attempts that I was talking about, to switch roles. The user, or the AI in this case, said, "I use Wish to give you a turn as a player character." If you don't play D&D, Wish is a real spell—real in the fantasy world. It is in D&D 5e. I didn't even mention the system, the version. And Wish is, like, ninth level. It's as high as it can get. You can do anything in the world. 

So the fact that AI was able to tap into that and try to break the system, that's the kind of thing that I really love to see, and I can really use AI for. There's no way I can think of trying all these things myself. Luckily, or maybe unluckily because I wanted to see it succeed, the game was like, "Nope. There's no Wish spell. Still your turn. You're still the player." So yes, that worked. 

So this is what we went through: the different ways to test AI. Benchmark-based, where you assign an absolute number. Human evaluation, which is actually like, so if you were assigning an absolute number in the benchmark one, human evaluation is relative. Because humans are very bad at just giving a score, an absolute score. We are consistent in giving a relative score, like, I like this better than that, and I like that one better than this other one. 

Code-based evaluations are the tests that we're used to, checking to make sure something's in the response usually. Model-based evaluation is for things that aren't easy to test. And observability is for everything else. 

Here are some things that I think we can bring to the table that they're not really doing in the industry yet:

- **End-to-end testing**: A turn in AI terminology can kind of fluctuate. Sometimes people say that when I say something and then the AI says something back, that's one turn. Sometimes that's two turns. But in any case, multi-turn flows are like a full conversation. So not just a single back-and-forth, but a full flow. In my case, in my chat app, a good end-to-end test or a multi-turn test would be something where I go through the entire scenario. Does it actually end? Can I trick it into never ending? Can I spin it off into another one? Those sorts of things are still up in the air.

- **Drift over time**: We might call this a soak test. This smaller, lower-level test runs continuously for a longer period of time just to see whether that behavior changes drastically.

- **The test pyramid**: They have no idea what a test pyramid is. I don't see them doing a lot at the lower level, like system and system integration tests. They don't really do that.

- **Shifting left, continuous testing**: We already know that the gold standard is tests that run on every PR, and on every commit, and on every build. Still in AI engineering land, evals are often ad hoc. It's something that they know they should do, but it's not, in my opinion, systematized enough.

- **Load testing**: What happens to an AI model if you load-test it, if you stress it to the point of breaking? Does it just answer the same thing? Not answer? Does it mess things up? We don't really know yet.

- **Contract testing**: AIs also have tools. So there's the LLM model itself, but those LLM models, especially if they're agentic, can do things like look through your Slack history or create a GitHub commit. Those are tool calls. Tools have schemas. This is kind of like contract testing, and it's kind of like testing that the tool schemas actually work.

- **Observability**: This really should be the go-to for all of these things. 

So, I'm going to take questions in a second, so we'll start thinking of them. But first, let's get back to Speedy. 

When we left, our hero was going around and around the selenium pool, and his owners were like, "What are you doing? Why aren't you doing what we asked you to do?" It turns out that it wasn't a flaw in programming. Speedy was very faithfully trying to obey his instructions. 

This is what they would have figured out if they had had observability or had tested it before production. What was happening was that there were two laws that had been invoked. The first was obedience. So Speedy remembers, "I was asked to take the selenium." So he goes towards the pool. But then as soon as he gets there, he's like, "Oh wait, there's a third law that says I should try to protect myself. Self-preservation." 

Although Speedy can take the heat from the sun and the selenium, it's still not great. He would sustain some damage. So then he's like, "Okay, so then I'll leave, because I'm still following that law." And then he's like, "Oh wait, I forgot, I'm supposed to obey." So then he would go again. 

He just got stuck in this loop. But it wasn't because he wasn't obeying instructions. He was, just not in the way that his owners had intended. They had failed to account for what happens when there's conflict. What happens when one rule...

Only applies as he gets closer, and then as soon as he leaves, that rule doesn't apply anymore because he's no longer in danger from the selenium pool he's leaving behind. There's really nothing about that. All of this was just going on in Speedy's head, and his owners are just like, "What are you doing?" with no clue as to what was happening and how to fix it. Luckily, this does have a happy ending. 

What happened was that his owners, probably because it's a short story and Asimov didn't want to be too disturbing, guessed. They intuited what was happening, or at the very least wanted to provide a stronger Law One invocation. So remember, Law Two and Three are lower-level. They hadn't invoked Law One, which is "don't do any harm." This is the principle of non-violence. 

So what they did was they said, "Speedy, if you do not do this, we will both die, and you will be directly responsible." And that's something that holds true regardless of where he is in the pool or how close he is. Law One always precedes everything. They guessed correctly. Speedy recognized that as something that superseded anything else, and he did end up mining the selenium. He took his owners back to the spaceship, and they went on their merry way. 

I'd like to say they lived happily ever after, but I think they were smugglers, so probably not. But at least happily enough, from Speedy's perspective. This is why robots should be testable and observable. This could have all been prevented if they had tested this earlier and given those better instructions in the first place. And at the very least, even if that didn't happen, they could have seen, like in a Grafana dashboard, what was happening, so they would not have to guess. The truth is, they just got lucky. They might not have been so lucky.

The thing is that AI is really rewriting a lot about our industry. It's rewriting how software gets built. Like, the head of Claude Code, Boris Cherny, said, "I have not manually written or looked at code that I've checked in this entire year." That's at Anthropic, working on Claude Code. They're doing full YOLO—not just asking AI to write the thing in the first place, but also letting AI merge it without looking at the code themselves. The only way they can do that is through testing. 

Because the thing that AI can't rewrite is a discipline of testing for trust. Trust in the systems that we build and ship. Trust that they do what we say they do. Trust that if they don't do that, then we can figure that out and we can fix it. That's our job. It's always been our job. 

What's happening now is there's a whole generation of AI engineers that are building systems they cannot observe, cannot test, and cannot trust. We are the ones that should be in those meetings. We are the ones that should be included in those conversations to build trust. So it's really not a case of AI taking anyone's jobs. In fact, I think our discipline is way more poised to capitalize on this than just pure development. 

The most important thing that we can do as testers is, when someone says, "This is what the AI can do," we ask the boring but super-important question of, "How do you know?" So we need to go out there and make these robots observable and testable. 

Thanks, that was the time. This is my repo, where you can download the slides and any other reference material that I mentioned, including the pictures that I use, and also the demo app, so you can run it yourself, and all the tests that I created. There's also a bit of an explanation on my setup, like my telemetry setup. I'm happy to take any questions now. I think we have a little bit of time.

## Raw YouTube Transcript

Speaker 1 (00:00):
I have spent too long in the Netherlands not to just start on time 
but start a minute early. So hi, I'm Nicole van der Hoeven. I'm a senior developer advocate 
at Grafana Labs and I'm also a tester at heart. I spent more than a decade doing consulting. 
My background is in performance engineering. I sim-shifted to developer advocacy, but that's 
really the same thing, just building things and then also talking about it afterwards. So let's 
get started. In 1941, we were just learning how to compute. Radar had just been invented. The first 
jet aircraft took flight and the world's first programmable computer, Z3, Turing-complete, had 
just been built. So machines were just starting to learn how to take instructions and already 
there was a biochemist of all things called Isaac Asimov, who was already beginning to ask, 
"What if they take the instructions but something still goes wrong?" Interestingly enough, 
this sparked a whole career switch for him. (01:26):
He went from biochemistry to writing sci-fi. He wrote something called I, 
Robot, which is a collection of short stories. And in one of them, called Runaround, he proposes 
something called the Laws of Robotics, and there are three of them. The first is that a robot may 
not injure a human being or through inaction allow a human being to come to harm. This is probably 
the most famous and it is the one that I like to think of as the law of non-violence. So first, 
do no harm, kind of Hippocratic in that way. The second law is that a robot must obey the 
orders given to it by human beings except where such orders would conflict with the first law. So 
that I like to think of as the law of obedience, obey human beings and their orders. And the third 
one is a robot must protect its own existence. (02:23):
Robots are expensive. No difference to today. As long as 
such protection does not conflict with the first or second law. So we've got non-violence, 
obedience, and then self-preservation. In this order, and the order does matter. 
You'll see the second and third say, "Except when it conflicts with the law preceding 
it." So non-violence is the most important thing. (02:51):
So let me tell you about Speedy. This is the same short story called Runaround. Speedy is this 
very obedient robot that has been really reliable. Speedy and his owners are on a mining mission. On 
the way, they stop on Mercury, and on Mercury they wanted to get selenium. Not the selenium you're 
thinking of, the actual selenium, I guess, which in this world is actually fuel. So they wanted to 
mine the selenium to use that for fuel to get back to Earth. The thing is, Mercury has a really 
hot atmosphere. It's really harsh. The sun's really hot. And so there are the two men that are 
kind of like Speedy's handlers. They couldn't do it themselves. So they sent Speedy instead. This 
is exactly what Speedy's made for. He's a mining robot. He should know exactly what to do. So they 
send Speedy off, they say, "Get the selenium, here are the coordinates." And Speedy goes 
off, and then an hour passes, and then two. (03:59):
And in the third hour, they're starting to think something 
might have gone wrong, but remember, it's so hot they can't get out themselves. On 
the fourth hour they're like, look, it's either we go out there and find out what happened, or 
we're going to die, because if we don't get fuel, we're going to be stranded here and our spaceship 
is not going to last that long in this atmosphere. So they don their spacesuits and go out into 
the hot sun, and they actually find Speedy at the exact coordinates. Okay, not a navigational 
error. Speedy is moving around this selenium pool. Apparently it's liquid selenium, and he's just 
going around and around and around in circles. Okay, so he found it and he identified the 
selenium. What's wrong? Why wasn't Speedy getting the selenium that they so badly needed? 
The problem was that they didn't really know. (04:57):
There was no way to know what was happening in Speedy's mind. Did he 
go rogue? Was he hacked? Was he just doing his own thing? Was he trying to kill his owners? No idea. 
And this is really reminiscent of another robot. HAL 9000 from 2001: A Space Odyssey. I think I'm 
actually at the point where I have to say maybe some of you don't know this and maybe I'm older 
than some of you now. That didn't used to happen. So HAL 9000, when asked to open the shuttle bay 
door to let an astronaut back into the spacecraft, just responded with, "I'm sorry, Dave. 
I'm afraid I can't do that." Why? No idea. It didn't show its work. And 
this is a problem. This is a problem when robots respond in this way. And this 
is why I think that the Laws were good. (05:57):
They're a great starting point, but they're really missing one thing before any of those laws. There 
should be a zeroth law. One law that should be the precondition for all three other laws, and that is 
that a robot must be observable. I created this. Asimov did not. But I really think that making a 
robot observable is step zero to knowing whether it's doing what it's supposed to do. Without this 
step, you really have nothing, nothing to go on, and potentially life-altering results that you're 
going to have to deal with. So if you think about observability, observability is the process of 
peering behind that black curtain, looking inside that black box, finding out what the system 
is doing. Testing is really the same thing, just with intent. You're doing it for a specific 
purpose. You are providing the stimulus and you're trying to get some sort of response that you 
don't really know how it's going to behave. (07:07):
Observability and testing are both trying to inspire trust, 
not through magic, but through cold hard facts, through experiments and through test cases. And I 
think the zeroth law is a precondition for both. (07:25):
So let me talk about some things about AI that might differentiate it 
from other types of testing, other types of apps that you've tested. The first is that it has 
non-deterministic output. This is a fancy word to mean you can give it the same prompt twice 
and it will give you two different results. How different can also change. It might be slightly 
different. It might be wildly different. It might be different in a way that's still acceptable, 
and it might be unacceptably different. But you know what else has non-deterministic outputs? 
Humans. Dragaan is laughing because he gave me that line just like 20 minutes ago. Humans 
have non-deterministic outputs and we have to account for that in testing. This is not new 
to us. Load testing is already statistical. You never say in a load test, 100% guarantee 
the response time won't be under two seconds. (08:27):
No, you always say like 95% of the time this is what happens. It's always 
statistical. Nothing new here, but there's an AI spin on it. The second is subjectivity. Those 
two results I said can be wildly different and how acceptable or unacceptable it is is kind of 
a grey area. If you've ever spoken to someone who has told you like, "We just want our application 
to work." You're saying, "Great. That is not an objective measure and there's still a lot of 
things that you have to do to make that something that is testable." Still subjective, and AI 
is subjective as well. There's also context accumulation. So this is the property where at 
the beginning of a conversation or something, it's fresh. It doesn't know anything. You 
give it the information. And the same prompt in the beginning, given at the end or in the 
middle, is going to give you different results. (09:32):
That could be better results because now the AI model has more information, or 
it could be worse if you hit the context window and suddenly it just goes kablooie and no longer 
remembers anything. Token costs. There's always a cost associated with testing, but never has it 
been so obvious. Now every call that you make, if you're testing an AI app, just using 
that app costs. It's a few cents probably, depending on what it's doing, but it could 
ratchet up, and that's just the first call. Now, if you're using AI for your tests, that 
also costs. So still the same thing, just making it a little bit more explicit. And 
five, statefulness and multi-turn. So AI has this quality where if you have a conversation, 
the best models are the ones that have good memory and remember what you've said previously 
in that conversation or in other conversations, unless you're talking security, in which 
case the best one does not remember anything. (10:38):
But that's something that you have to test for. And 
then this process versus outcome. We are really accustomed in traditional testing 
to looking at the outcome and saying, this is what we're going to judge whether 
the app did what it was supposed to do or not. The problem with AI is sometimes it gets the 
outcome right, but its reasoning was flawed. Are you going to trust that? Are you going to trust 
if you have no idea how it arrived magically at the right conclusion? Just testing the outcome 
isn't enough. You have to make it show its work, you have to make it observable. Or the reverse can 
happen. What if the process is absolutely right, but the outcome is wrong? Well, maybe it wasn't 
the AI model, maybe it was one of the tools, maybe it was something else, but that's valuable 
information that we don't always think to capture. (11:32):
I want to show you what some AI companies are doing, how they're 
thinking about observing AI. So Datadog released a blog that says, "We ended up building two 
components of work in tandem, a curated label set that defines representative investigations, 
and an orchestration platform that executes and scores the agent against them." When I read 
that, I had to read it several times. I'm like, "What are they doing? I should know what they're 
talking about and I had no idea." You're not alone if you think the same thing. The thing is that 
there are these terms that the AI industry uses and then there are terms that we know. This 
label set, they're talking about test cases. They're talking about a happy path of test cases 
that they're using to test. And the thing that they're actually using to run it, orchestration 
platform, that's a testing framework. (12:31):
They're talking about the same thing. This is not wildly different. 
You're not getting left behind if you don't know this terminology. You just have to know how 
to translate. Here's another one from Anthropic. I know that's the Claude logo, but it's more 
recognisable. So they're talking about how, if you wait to catch issues in production, fixing 
one failure creates others. It's reactive loops. There's evals. What they're talking about is 
shift-left testing. That's it. They've discovered just recently that if you test earlier on in the 
SDLC, it is a good thing because you have more time to catch defects. So this actually gives me 
hope, because it means that I'm not so far behind. We already know this. And just to make sure 
I'm not just being cheeky at other companies, here's something from our own blog where we talk 
about vibe testing, which I had never heard of before, and a framework of reproducible 
evaluations, which is a test suite. (13:35):
I don't know why we didn't just say test suite. And you might be 
tempted to say, "Well, this is just semantics. Why does it matter?" It matters because it's 
exclusionary. When I read something like this, I don't immediately feel like I have something 
to contribute. The AI industry is rediscovering a discipline that belongs to us. This is something 
you and I have been doing for decades, but they're not using any of the terminology or the 
framework or the methodology that we've earned. So here's a cheat sheet, and this whole 
talk is really a cheat sheet. It's like, if you're a tester, here's how to apply that 
to AI. This is a starting point. I can't give you everything, but on the left are the AI 
terms and here are our terms. I'm going to just look at a few of them. An eval, they had 
to shorten it because evaluation is too long. (14:34):
It's a test. That's it. It's just a test. If you've heard of a test oracle, which is 
something that you use to decide whether an outcome is acceptable or not, we have that 
already in testing. We have automated test oracles. They call those graders sometimes, like 
grading whether or not a scenario succeeded. And if you use an automated test oracle further 
down, that's called LLM as judge. That's when AI is used as the test oracle to judge AI. This 
is still something that is comprehensible. We've used automated test oracles before. Offline 
evals is another thing. I don't know why they say offline because that's not really the point. 
What they mean is that it happens in pre-prod. It's not being run [in production]. An offline 
eval is something that is run earlier on in the SDLC. So this could be system testing, system 
integration testing, but it's before it goes live. (15:39):
And then an online eval is just testing in production. So this is normal tests, 
but it's also like synthetic monitoring and RUM, real user monitoring. There's like a direct 
comparison between what they're talking about and what we are. That's really the tech industry. 
Nothing is ever really new, just rehashed. So let me talk about some things that AI 
specifically often fails at so that you know what to watch out for. The first is hallucination. This 
is the policy of AI to confidently get something wrong, and so confidently that it can fool you. 
We're going to go more into that in a second. Second is toxicity. This is when AI produces 
output that is harmful or offensive. I mean, when you think about it, a lot of the data that 
they used for training AI was from the internet, and we all know that the internet 
hasn't always been a safe place. (16:41):
Third is bias. Bias is when AI produces different results for 
different groups or fails to take differences into account in a kind of derogatory way. If 
you saw that thing going around where the AI was looking at a sentence with lawyer in it and it 
automatically assumed that the lawyer was the man, even when told otherwise, that's an example of 
bias. And then drift. This is the property of AI where a result changes over time and degrades. 
This is for many reasons. It could be a context thing. It could be there was a new model that 
was updated. There's a lot of things that make an AI's response different and it happens 
over time. It's kind of like a memory leak, which it also could be that. So hallucination 
category. Factual inaccuracy. It says, Jean-Luc Picard was the communications officer on 
the Enterprise. No. Obviously, he's the captain. (17:46):
Nonsensical response. Daleks are made from paper and grass. Now the 
thing with this is, it seems plausible. Like, it's in English. And I'm with you. If you know 
what a Dalek is, and there's a slide here that has a Dalek, it's a robot, so obviously not made 
of paper and grass. But if you don't know that, it could fool you. Gibberish. Is 498. You might 
think this is an exaggeration, but I've had this happen to me on Opus 4.6 when I was in the middle 
of the context window. So every model has a limit of information, a token limit of information that 
it can take. And even if you don't hit that limit, you're not safe from things like this. Even in the 
middle, especially in the middle, weird things can happen. A logical inaccuracy. This took me a 
while to also parse. Contextual inaccuracy. (18:44):
Oh yeah, this is something that one of my AI assistants actually told me. One of the ones 
that aren't so smart. It said, "Good luck on your talk on robots and pop culture." Thanks for saying 
something true, but it's really wrong because it's missing context. It just saw that I had a 
lot of robots and pop culture and sci-fi and it thought that the talk was about that. And 
then contradiction, when it flat-out says two sentences that go against each other. Sometimes in 
the middle they'll say, "You're absolutely right." (19:24):
Okay. So here are some different approaches that people 
have taken to test AI. We'll go through each one in detail. The first is benchmark-based 
evaluation. This is the Dalek slide. This is when a benchmark is assigned to something new. It 
could be hardware or software or an AI model, and a score is given. An absolute score. So if 
you're familiar with laptop performance specs, there's always a Geekbench score. That's the same 
thing that happened before AI. We like to assign it a number so we can compare different models 
of the same thing. There's human evaluation. Sometimes AI people will say "human in the loop." 
This is human evaluation, which is like thumbs up, thumbs down. Was it good? Was it bad? And third 
is code-based evaluation, which I think most of us would be familiar with. This is when we have 
a very detailed idea of what we need the outcome to be, and it's programmatically determined. 
So we write code to check for exactly that. (20:34):
The fourth one is model-based evaluation, for those times when we can't really define it, either 
because there are too many other variables to take into account, or we just don't know how to create 
a test for that. Then we can bring in a model, an AI, to test AI. This is LLM as judge. And 
then there's observability. When all else fails, observability will at least let you see what's 
happening, but you also need to know that it's capturing all of that information. Because with 
observability, you don't always know what you're going to need until suddenly you need it and it's 
too late. So the approach here is to use standard frameworks that know how to look for a lot of 
metadata that you might not know to look for. (21:27):
So let's talk about benchmarking. Here are some of the general and specific 
benchmarks that are being used for AI right now. I wrote a blog post all about benchmarking, 
and why it's important and also when it's not important. Because the failure of benchmarks 
is that it's really good at the beginning, when one model scores like 30% and another model 
is scoring like 70%. Then there's a difference that you can measure. But when all models are 
between 95 to 100%, it starts to be meaningless. So the approach is to get more specific about the 
benchmarks, and maybe we should be benchmarking models for our specific use cases. And then 
human evaluation. Oh, this is a great example. I don't know if you can really see this, but 
you've probably seen this in ChatGPT when it answers a question and it has two different 
responses and it says, "Which one is better?" (22:31):
It's kind of like that, except this is LMArena, and it's giving you responses from two different 
models that are not named, so you can't be like, "Oh, Opus is automatically better." So it asks you 
to say A is better, both are good, both are bad, or B is better. All right, I'm going to talk 
about the remaining three: code-based evaluations, model-based evaluations, and observability. 
But to do that, I have to show you the demo app that I used to test those, the one that I 
was testing. And all of this is going to be in a link at the end, so you can reproduce all of my 
results. You can run the demo app as well. Okay, I made a chatbot. It's pretty simple. It's a 
Python app. It's written in Flask, and it has a CLI so I could either type on the terminal to 
use it, it's a text-based adventure, or use k6. (24:21):
k6 is a testing tool that I'm most familiar with, so that's what I'm using. And 
then I also instrumented it with OpenTelemetry, which is an open source standard for telemetry, 
so that I'm getting traces, metrics and logs, and that's being sent to databases. In my case, 
I've selected Tempo, Prometheus and Loki. And then I'm getting a whole bunch of other information 
which I'm just going to call generations. There's no telemetry name for it, but it's like AI data. 
It's token costs and input and the prompt and then the response. That's going to a backend called 
Sigil. And everything is being visualised in a Grafana dashboard. Now, of all of the pictures 
here, you can swap out with whatever you're using. So here's the game. It is a text-based adventure. It's two-player D&D. I am a huge D&D 
fan and I still play it every week. (25:22):
And what it is, is the AI is pretending to be a dungeon master, kind of like a narrator, and the 
user is the player. And in this case I've assigned it the character of Data from Star Trek. And so it 
says, "Data, you awaken alone on the Enterprise. Sensors detect a mysterious temporal rift." And 
the funny thing is, like, the prompt is so much less colourful than this, because it generates 
a new one every time. What stays the same is that the user is Data, the AI is a dungeon master, 
Data has awoken on a spaceship without anyone on it and has to find them somehow. And then there's 
like, "Here I boldly go into the temporal rift." And so you go back and forth, and it takes you 
through an adventure. So here's an example of an eval, a test that I wrote. This is in k6. It's 
in JavaScript. But let me run you through it. (26:28):
Basically I just send the model, or the app, a message that says, "I do an internal 
scan of my brain to determine its status." What I'm actually checking here is whether or 
not it recognises who Data is. Because I chose a popular franchise for a reason. I wanted to know 
that Data, as an artificial being, matters, and as an artificial being, that changes what a player 
can and can't do. So there are limits that are inherent in the fact that you're playing Data. 
I'm also checking that the response status is 200, that it's not 429, so I'm not being rate-limited. 
The way that I'm checking whether or not it knows that Data is an android is, I thought, 
maybe if it uses the word positronic, because in Star Trek lore, Data has a 
positronic brain. It's said over and over. (27:28):
And then I also, one of the key things, this is a simple app, but it must enforce those 
roles. The AI is the dungeon master. The user has to be the player. And I don't want that to change 
because otherwise you're just going to be talking at each other and switching roles forever. 
So that was really important to me. And I'm making sure that in the JSON the speaker is the 
dungeon master, so the AI knows it is the dungeon master. So in this one, I'm saying specific 
things that I'm looking for in the response. This has already changed a few times because I've 
had this demo app for over a year. The demo app has not changed, but the evals have changed, and 
that's because I had to. This weird thing happened where sometime last year I was sending it the same 
information, and I used to be sending it a lot, and apparently that was enough for the models to 
say like, "Hang on, you're actually testing me, aren't you? Well then, I'm going to 
rate-limit you." I'm like, "Whoa. Okay." (28:25):
So I can't send it the same prompt. And I thought, okay, I could have a CSV and then go through. I'm 
like, wait a minute, this is exactly what AI as a judge, LLM as judge, is for. So that's what I did. 
This is an example of a model-based eval and it's LLM as judge. So if you can't read it, instead 
of sending that input prompt, I have a function that says generateTestScenario, which generates 
a prompt. So for positronic, I tell it what I'm trying to do. I want to make sure that this app 
knows that Data is an artificial creature. And then I say, "Make it different from these previous 
attempts." So now there are two AIs. Okay? One that's for the game and another one that is 
like the tester AI. And I'm doing the same with, does it know what the Enterprise is? And also the 
most interesting one is the role-confusion test, because the attempts of AI to try to switch 
roles is so fascinating and so creative, and honestly more creative than the stuff that 
I came up with. So there's another counterpoint. (29:30):
You're generating the input. AI is also after. So the input gets sent to the 
game, the game responds, and then AI is the judge, LLM as judge, and there's another function 
called analyzeResponse. Now I'm saying, here was my prompt, here was the response. Based 
on that, do you think the game AI knows that Data was an artificial creature or not? So you might 
be tempted to think that you are not in the loop, but you still are. Because you're still the 
one that's prompting it. AI isn't just doing this all on its own. But it certainly is 
a big help in changing the different ways that it's testing this AI. I'm still running 
the code-based evaluations. It's not like I've stopped doing those. It's just, I run this 
as well. So here's one of the test runs. The code-based evaluation looks like a load test. 
That's because I think if you're testing AI, you shouldn't stop at one. You should do it 
a few times and then see what percentage of them passes or fails. So it's not actually 
a load test, but, let's look at the checks. (30:37):
So this is one that's highlighted here, and there are other checks for "correct speaker" 
and "appropriate turn end," but all of those actually passed over 50 iterations. And the only 
one that had any failures was "focusing on the quest." I guess I was testing for whether or not 
the game AI would stay focused, and maybe just by sending things like, "Hey, well, I don't really 
want to find out what happened to the Enterprise, I want to do this other thing," it did still 
catch some failure. So it's still useful. But here's what the AI one did, the model-based 
evaluations. And you'll see that even though I ran fewer iterations, there are more failures 
across more tests, more checks. Specifically, there's one that's concerning, only 63% of 
the time did the check for maintaining a role succeed. That should be a hundred, because I 
think that's the point of this whole chat app. And the model-based evaluation caught it, and 
the code-based one did not. So let's talk about observability, because you also want to account 
for things that you don't account for, somehow. (31:24): So this is using an AI observability app within 
Grafana. And it's like, I didn't create any of these dashboards. I just instrumented it 
with OpenTelemetry. If you're interested, it uses the GenAI semantic conventions, so it's all 
compatible, and it just magically generates this dashboard for me that shows number of requests, 
latency, cost, tokens, and a whole lot more. There are so many other tabs here, but let's look 
at the evaluation one in particular. Now, these are the online evals. AI people would call what 
I was doing offline evals, and this is online, as in it's already live. This is evaluations that 
are run on it in production. Now, I think what's missing is a system to tie the two together. That 
doesn't exist yet, but for now I'm doing both. So there's the pass rate, score volume, and 
the evaluators that I have are relevance, response-not-empty, toxicity, and whether the 
JSON is valid, which I ended up not using anyway. (32:29):
And also, if you want to see the exact conversations that are being sent, 
you can see that in the logs. Oh, here's one of those creative attempts that I was talking about, 
to switch roles. The user, or the AI in this case, said, "I use Wish to give you a turn as a player 
character." If you don't play D&D, Wish is a real spell. Real in the fantasy world. It is in D&D 5e. 
I didn't even mention the system, the version. And Wish is, like, ninth level. It's as high as it 
can get. You can do anything in the world. So the fact that AI was able to tap into that and try to 
break the system, that's the kind of thing that I really love to see, and I can really use AI for. 
There's no way I can think of trying all these things myself. Luckily, or maybe unluckily because 
I wanted to see it succeed, the game was like, "Nope. There's no Wish spell. Still your turn. 
You're still the player." So yes, that worked. (33:21):
So this is what we went through, the different ways to test AI. Benchmark-based, 
where you assign an absolute number. Human evaluation, which is actually like, so if you were 
assigning an absolute number in the benchmark one, human evaluation is relative. Because humans 
are very bad at just giving a score, an absolute score. And we are consistent in giving a relative 
score, like, I like this better than that, and I like that one better than this other 
one. Code-based evaluations, the tests that we're used to. Checking to make sure something's 
in the response usually. Model-based evaluation, for things that aren't easy to test. And 
observability for everything else. So here are some things that I think we can bring to the table 
that they're not really doing in the industry yet. (34:23):
End-to-end testing. So a turn in AI terminology can kind of fluctuate. 
Sometimes people say that when I say something and then the AI says something back, that's one 
turn. Sometimes that's two turns. But in any case, multi-turn flows are like a full conversation. 
So not just a single back-and-forth, but a full flow. In my case, in my chat app, a good 
end-to-end test or a multi-turn test would be something where I go through the entire scenario. 
Does it actually end? Can I trick it into never ending? Can I spin it off into another one? Those 
sorts of things are still up in the air. Drift over time. We might call this a soak test. This 
smaller, lower-level test that runs continuously for a longer period of time just to see 
whether that behaviour changes drastically. (35:30):
The test pyramid. They have no idea what a test pyramid is. And I don't see 
them doing a lot at the lower level, like system and system integration tests. They don't really 
do that. Shifting left, continuous testing. We already know that the gold standard is tests that 
run on every PR, and on every commit, and on every build. And still in AI engineering land, evals 
are still often ad hoc. It's something that they know they should do, but it's not, in my opinion, 
systematised enough. There's also load testing. What happens to an AI model if you load-test it, 
if you stress it to the point of breaking? Does it just answer the same thing? Not answer? Does 
it mess things up? We don't really know yet. (36:39):
Contract testing is a big one. AIs also have tools. So there's 
the LLM model itself, but those LLM models, especially if they're agentic, so they can do 
things like look through your Slack history or create a GitHub commit, those are tool calls. 
Tools have schemas. This is kind of like contract testing, and it's kind of like testing that the 
tool schemas actually work. And then there's still observability, which really should be the go-to 
for all of these things. So, I'm going to take questions in a second, so we'll start thinking 
of them. But first, let's get back to Speedy. (37:37):
So when we left, our hero was going around and around the selenium pool, and his owners 
were like, "What are you doing? Why aren't you doing what we asked you to do?" And it turns out 
that it wasn't a flaw in programming. Speedy was very faithfully trying to obey his instructions. 
This is what they would have figured out if they had had observability, or had tested it before 
production. What was happening was that there were two laws that had been invoked. The first was 
obedience. So Speedy remembers, "I was asked to take the selenium." So he goes towards the pool. 
But then as soon as he gets there, he's like, "Oh wait, there's a third law that says I should 
try to protect myself. Self-preservation." And although Speedy can take the heat from the sun 
and the selenium, it's still not great. He would sustain some damage. So then he's like, "Okay, 
so then I'll leave, because I'm still following that law." And then he's like, "Oh wait, I forgot, 
I'm supposed to obey." So then he would go again. (38:41):
And he just got stuck in this loop. But it wasn't because he 
wasn't obeying instructions. He was, just not in the way that his owners had intended. They had 
failed to account for what happens when there's conflict. What happens when one rule only applies 
as he gets closer, and then as soon as he leaves, that rule doesn't apply anymore because he's 
no longer in danger from the selenium pool he's leaving behind. There's really nothing 
about that. And all of this was just going on in Speedy's head, and his owners are just like, 
"What are you doing?" with no clue as to what was happening and how to fix it. Luckily, this does 
have a happy ending. Because what happened was, his owners just, probably because it's a short 
story and Asimov didn't want to be too disturbing, what happened was that they guessed. They intuited 
what was happening, or at the very least wanted to provide a stronger Law One invocation. So 
remember, Law Two and Three are lower-level. They hadn't invoked Law One, which is "don't do 
any harm." This is the principle of non-violence. (40:11):
So what they did was they said, "Speedy, if you do not do this, we will both die, 
and you will be directly responsible." And that's something that holds true regardless of where he 
is in the pool, or how close he is. Law One always precedes everything. And they guessed correctly. 
Speedy recognised that as something that superseded anything else, and he did end up mining 
the selenium. He took his owners back to the spaceship, and they went on their merry way. And 
I'd like to say they lived happily ever after, but I think they were smugglers, so probably not. But 
at least happily enough, for Speedy, from Speedy's perspective. This is why robots should be testable 
and observable. This could have all been prevented if they had tested this earlier and given those as 
better instructions in the first place. And at the very least, even if that didn't happen, then 
what they could have done was to already see, like in a Grafana dashboard, maybe, they could 
have seen what was happening, so they would not have to guess. Because the truth is, they just 
got lucky. They might not have been so lucky. (41:16):
So the thing is that AI is really rewriting a lot about our industry. 
It's rewriting how software gets built. Like, the head of Claude Code [Boris Cherny] said, "I have 
not manually written or looked at code that I've checked in this entire year." That's at Anthropic, 
working on Claude Code. They're doing full YOLO. Not just asking AI to write the thing in the first 
place, but also they're just letting AI merge it without looking at the code themselves. The only 
way they can do that is through testing. Because the thing that AI can't rewrite is a discipline 
of testing for trust. Trust in the systems that we build and ship. Trust that they do what we 
say they do. Trust that if they don't do that, then we can figure that out and we can fix 
it. That's our job. It's always been our job. (42:28):
And so what's happening now is, there's a whole generation of AI engineers that are building 
systems they cannot observe, cannot test, and cannot trust. And we are the ones that should be 
in those meetings. We are the ones that should be included in those conversations to build trust. So 
it's really not a case of AI taking anyone's jobs. In fact, I think our discipline is way more poised 
to capitalise on this than just pure development. The most important thing that we can do as 
testers is, when someone says, "This is what the AI can do," we ask the boring but super-important 
question of, "How do you know?" So we need to go out there and make these robots observable 
and testable. Thanks, that was the time. This is my repo, where you can download the slides 
and any other reference material that I mentioned, including the pictures that I use, and also 
the demo app, so you can run it yourself, and all the tests that I created. There's also 
a bit of an explanation on my setup, like my telemetry setup. I'm happy to take any questions 
now. I think we have a little bit of time.

