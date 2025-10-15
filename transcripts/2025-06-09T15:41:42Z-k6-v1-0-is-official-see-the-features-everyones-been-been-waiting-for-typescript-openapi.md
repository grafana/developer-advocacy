# k6 v1.0 is Official — See the Features Everyone&#39;s Been Been Waiting For | TypeScript | OpenAPI

Published on 2025-06-09T15:41:42Z

## Description

k6 v1.0 is here—and it's officially stable! Discover the new features, including TypeScript support, powerful extensions, OpenAPI ...

URL: https://www.youtube.com/watch?v=hHvVHi3Tdds

## Summary

In this YouTube video, Théo and Ayush, software engineers from Grafana, introduce the newly released stable version 1.0 of k6, a reliability testing tool designed to enhance application performance and prevent issues before they reach production. They explain k6's functionality, which includes writing test scripts in JavaScript or TypeScript, simulating user interactions, and providing actionable insights from the test results. The video covers the importance of reliability testing as an additional layer to existing testing practices and highlights new features in version 1.0, such as first-class TypeScript support, improved end-of-test summaries, and the introduction of the k6 Studio, a no-code tool for generating tests. They also emphasize the tool's new capabilities for handling open API schemas and extensions, making it easier for teams to integrate testing into their workflows. The presentation concludes with a call for community feedback and gratitude for contributions to k6 over the years.

# Presentation Transcript

Hello everyone! You can scan this QR code to add your questions during the presentation, and we'll get to them at the end. 

Let's begin. What if the best way to prevent fires in production was to ignite controlled ones in your development environment? Hi, I'm Théo, and I'm a software engineer at Grafana. 

And I'm Ayush, also a software engineer at Grafana. In the next 25 minutes, we will tell you how **k6** can help you build more reliable systems and show you how there's never been a better time to pick it up. 

But first, let's ensure we're all on the same page. I heard a couple of people saying, "Woo," when we mentioned k6. So, what is k6? 

k6 is a reliability testing tool. Concretely, it's both a command line tool and a Grafana cloud application. It allows you to verify that your app works. 

### How k6 Works

k6 operates in three phases:

1. **Write a Test Script**: You can write in JavaScript or TypeScript, reproducing your user journeys or specific workflows in your infrastructure or application. 
2. **Run the Script**: k6 simulates concurrent users actually performing those workflows, collecting measurements and aggregating them into metrics. 
3. **Analyze Results**: Once k6 is done, it provides a summary of the test results and actionable insights to help you assess the situation and make decisions.

Additionally, k6 fits right into the observability stack, allowing you to send those metrics and samples to your favorite tools.

Théo here used quite a fancy term—reliability testing—which might sound complicated, but it is not. In practice, it helps in **battle testing** your application as you develop it. The whole idea is that while the Grafana LGTM stack helps you discover and root cause issues, reliability testing enables you to prevent those issues from ever happening in the first place.

### The Need for Reliability Testing

If I were in the audience right now, I might be thinking, "I'm already doing unit testing, integration testing, and maybe even end-to-end testing. Is yet another layer of testing the solution to all my problems?" 

We think so, as no plan survives the real world. Despite all those testing practices, bugs still reach real-world use cases, and CI pipelines still go red. Even if you're running all tests before merging any branch, somehow the main branch always gets red. Reliability testing is all about testing your application from the user perspective in real-world conditions, and k6 is a tool that helps you do that.

For example:
- To check if your system can handle all the traffic that your marketing team is promising, k6 can help you with **load testing**.
- To verify that the UI of your website looks exactly how your design team envisions, k6 can assist with **browser testing**.
- To validate individual application functionalities, you can use k6 for **functional testing**.
- Lastly, you can modify k6 to perform **contract testing**.

### Announcing k6 Version 1.0

Today, after nine years of development and countless iterations, we're happy to announce that the very first stable version of k6, **version 1.0**, is out and ready for you to grab. 

This matters because now k6 is officially stable and production-ready. It ships with many new features and improvements to make your reliability testing journey even smoother. There's never been a better moment to get started with k6 and testing.

### What Does Stability Mean?

For those who already use k6, you know we've treated it as if it was stable. But with version 1.0, we now officially acknowledge and bring the guarantees along that stability probably means to you. 

So, what does it mean for us to say that k6 is stable? It revolves around three main axes:

1. **Semantic Versioning**: You can expect a new major version roughly every year, with non-breaking features and fixes along the way. Breaking changes and deprecations will only be acknowledged with major versions.
  
2. **Support Guarantees**: If you pick up k6 version 1 today, you can expect to receive critical bugs and security fixes for at least two years or two major versions.

3. **Ecosystem**: We now have a rich ecosystem of extensions and tooling, many built on our code base. You can see what we will support for the next two years and what we won't.

### New Features in k6 v1

Our community of developers has long requested first-class TypeScript support. Now you can write more robust, predictable, and easier-to-maintain tests with type safety and IDE auto-complete. This allows you to easily reuse your existing TypeScript code and types directly in your k6 tests.

#### Extensions

k6 is quite versatile and allows you to do a lot of things. However, a single team and a single tool can only satisfy limited use cases. k6 already allowed you to extend its functionalities, but you needed a dedicated tool to build a binary and use it. 

With k6 v1, we're streamlining that process completely. You just have to push your custom extension, add it to your script, specify its name, and start using it—no custom binaries or special tools needed.

To give you a good analogy, think of how GitHub actions work. If you want to use a custom action in your workflow, you specify its name, make it accessible by a public repository, and just run your workflow. That's how extensions will work in k6 v1.

### Improved End of Test Summary

One of the most requested features for k6 has been a complete revamp of the end-of-test summary, which is what most of our users use to extract insights from the test results. 

With this new summary, we modernized it and enriched the results, focusing on three main axes:
- Created a complete hierarchical output, grouping metrics by scenario and category.
- Improved thresholds and checks for clarity.
- Offered a compact mode to focus on the most important results while still allowing for a detailed view.

### New Additions to the k6 Ecosystem

We would also like to highlight two new additions to the k6 ecosystem:
1. **Open API to k6 Converter**: This tool allows you to take an existing Open API schema, convert it to a TypeScript client, and use it directly in a k6 test without any boilerplate code.
2. **k6 Studio**: A desktop application—a no-code tool—that you can use to generate k6 tests without writing any code.

### Demo

Now, let's have a demo. In the k6 department, we are very fond of pizza. We built **QuickPizza**, a simple website where users can generate a pizza recipe. Under the hood, this is a real-world application with various protocols and a lot of data moving around, making it a good testing target.

I will write a k6 script to verify that the app is online and performs as expected. 

#### k6 Script Example

This k6 script is written in TypeScript. Before k6 version 1, the only supported language was JavaScript, which caused many issues. Now, with TypeScript, we can do interesting things. 

In this script, we define a scenario to test that the website is up and running. We use proper type definitions for better accuracy. We send an HTTP request to verify the response and simulate button clicks to ensure the API responds correctly.

### Ayush's Demo on Open API and k6 Studio

Now let’s say you're already working on a backend application and you need to change requests frequently. The **Open API to k6 Converter** is a command line tool that you can use to generate a TypeScript client from the Open API schema.

You can filter requests based on tags and generate a sample script to get started easily. 

Now, let’s switch to **k6 Studio**, a no-code tool that allows you to record user flows and generate tests without writing any code. You start with a recorder, modify behaviors with a generator, and run validations smoothly.

### Conclusion

To wrap up, k6 version 1 marks our first stable production-ready release with dedicated support and explicit guarantees. If you pick it up today, we have your back for the years to come. 

It’s now easier than ever to leverage the k6 ecosystem, integrate reliability testing into your CI pipelines, and make testing accessible for larger teams and organizations.

A big thank you to everyone who contributed features, filed bugs, and helped along the way. If you want to learn more about k6, scan this QR code to get to our documentation page.

As always, we’d love to hear your feedback. k6 is what it is because of our users and contributors. You can find us on GitHub and at the Ask the Experts booth right after this. Thank you very much!

## Raw YouTube Transcript

So hello everyone. You
can scan this QR code. Yeah, you can scan this QR code, add your questions during the presentation
and we'll get to them at the end. So let's begin. What if the best way to prevent
fires in production was to ignite controlled ones in
your development environment? Hi, I'm Théo. I'm a software
engineer at Grafana. And I'm Ayush, a software engineer at
Grafana. And in the next 25 minutes, we will tell you how k6 can help you
build more reliable systems and show you how there's never been a
better time to pick it up. But first, let's ensure
we're all on the same page. I heard a couple of people saying,
"Woo," when we mentioned k6. So k6 is a reliability testing
tool. So what that concretely means, it's both a command line tool
and a Grafana cloud application. And what it allows you to do is
essentially verify that your app works. So it works in three phases. The
first step is you write a test script. It can be in JavaScript or
it could be in TypeScript. And you're going to reproduce your user
journeys or specific workflows in your infrastructure or your application. The next step is to have k6 run that
script and it's going to simulate concurrent users actually
performing those workflows. And along the way it's going
to collect measurements, samples and aggregate them
into metrics. And finally, once k6 is done, what it's going to do is provide you
with a summary of the test results and actionable insights that will help
you to assess the situation and take decisions. And finally, the big tent was mentioned right before
and k6 fit right into this because you can also send those metrics and those
samples to your favorite observability stack. Théo here used quite a fancy
term - reliability testing, which just sounds complicated,
but it is not. In practice, it helps in battle testing your
application as you develop it. The whole idea is while the
Grafana LGTM stack helps you discover and root cause issues, reliability testing enables you to prevent
those issues from ever happening in first place. And if I was in the audience right now, I might be thinking I'm already doing
unit testing, integration testing, end-to-end testing, maybe,
if I'm fancy. Ayush, is yet another layer of testing
the solution to all my problems? We think so as no plan
survives the real world. And despite all those testing practices,
bugs still reach real world use cases. CI pipelines still go red. Even if you're running all
tests before merging any branch, somehow the main branch always
gets red. I don't know why. And that's precisely what
reliability testing is all about. Testing your application from the user
perspective in real world conditions and k6 is a tool which helps
you do that. For example, to check if your system can handle all
the traffic which your marketing team is promising, k6 can help
you do load testing, to verify that the UI of your website
looks exactly what your design team thinks it should, k6 can help
you with browser testing. To validate individual
application functionalities, you can use k6 to perform functional
testing. And last but not least, you can modify k6 to do contract testing. So today, after nine years of
development and countless iterations, we're really happy to announce that the
very first stable version of k6 version 1.0 is out and ready for you to grab. Thank you. It matters because now k6 is
officially stable and production ready. It ships with a ton of new features, a ton of bigger and smaller improvements
to make your reliability testing journey even smoother. And there's just never ever been a
better moment to get started with k6 and testing. But let's make this more concrete and
give you a short pick of what's in it for you. People who already use k6, more seasoned users knew that we
always treated k6 as if it was stable. But with version 1.0, we now officially acknowledge
and bring the guarantees along that stability
probably means to you. And so what does it mean in
general for us to say that k6 is stable? Well, it revolves around three
main axises, semantic versioning, you're probably familiar with it, but the gist means that we're going to
stick to it strictly and you can expect a new major version roughly every year.
And we'll keep shipping features, non-breaking features
and fixes along the way, but breaking changes and deprecations
will be only acknowledged with major versions. We also now
have support guarantees. What that means is if you pick
up k6 today with k6 version 1, you can expect to receive critical
bugs and security fixes for at least two years or two
major versions. And finally, when you will dive into k6, you will see that we have a pretty rich
ecosystem of extensions and tooling and most of those are built on our code base. And before everything was
considered moving parts, now we have a public API surface. So when you pick the k6 code
base to build extensions, you know exactly what we are going to
support for the next two years and what we won't. Now, this is something our community of awesome
developers was asking for a very long time. And finally, we are shipping
it, first class TypeScript support. Now you can write more
robust, predictable, and easier to maintain tests with
type safety and IDE auto-complete. This allows you to easily
reuse your existing TypeScript
code and types directly in your k6 tests. Next, extensions. So as you have seen till now, k6 is quite versatile and allows
you to do a lot of things. But a single team and a single tool
can only satisfy limited use cases. That's why k6 already allowed you
to extend its functionalities, using extensions, to add support
for new features and protocols. But you needed a dedicated tool to
first bring everything together, build a binary and use it. With k6 v1, we are streamlining
that process completely. You just have to push your custom
extension, add it to your script, just add its name and directly
start using it. No custom binaries, no special tools needed at all.
To give you a good analogy, think of how GitHub actions work. If you want to use a custom action in
your workflow, you just specify its name, make it accessible by a public repository
or direct access and just run your workflow. That's how the
extensions will work in k6 v1. But sorry. So this is a very complicated feature, hence we are doing a phased rollout of
it with cloud test runs supporting it now and the support for k6
CLI coming in recent future. Another big improvement is one
improvement that was one of the most requested feature for k6. We've completely revamped
the end of test summary, which is what most of our users use to
extract insights from the test results. So with this new summary,
we have modernized it, we have enriched the results that
we provide and basically it revolves around three main axises. So we have created a
complete hierarchical output. Before that we were showing
you everything, now metrics
are grouped by scenario, by groups, which is also a concept
in k6 and very specific categories. Another thing is we have
improved thresholds because
we considered they were a bit confusing before. Now we have completely changed how
those are displayed as well as checks. And finally, if you only need
the big picture and you're like, just show me what I care about, the summary by default will be in a
compact mode focusing only on what we believe is the most important
thing you should see. But if you want the full
picture with full granularity, you can also use a specific mode,
which we call the full mode. Now, although there are so
many more additional features, we would like to bring your attention
to these two new additions to the k6 ecosystem. First is the
open API to k6 converter, which allows you to take an
existing open API schema, convert it to a TypeScript client and use
it directly in a k6 test without using any boilerplate code to send
request or do any other thing. And the next is k6 Studio, which is a
desktop application, a no-code tool, which you can use to generate k6
test without writing any code. Now in place of just about all the things, we would like to show you how
everything comes together and looks. So let's have some demo. Yeah, let's switch to
the demo screen please. There you go. Thank
you very much. Alright, in the k6 department, we're
very, very fond of pizza. We have endless debates about
how to cut them for instance. So because we need to provide a real
world application to our users to test it, we built quick pizza.Oon the surface
this is a pretty simple website, it has this big orange button -
Pizza please. And when you press it, what it does is generate
a pizza recipe for you. But in practice under the hood, this is a real world application with
a lot of protocols and a lot of data moving around and so on. So it's an
actual really good testing target. And what I'm going to do now is
I want to write a script with k6 that's going to allow me to
verify that the app is online, that it's up and running and that
it does what I expect it to do. But let me show you in
practice what that looks like. Yeah, never too eager with security. Basically this is a k6 script and of
course you're probably noticing this is TypeScript, before k6 version one, the only supported language was
JavaScript and it caused a lot of issues. But now with TypeScript we can start
doing really interesting things. The first one being, in this
case I copy pasted the code, but you might notice that here I
import some types and I import some functionalities. Well, right now
this is some types that I copied, but you could perfectly take the types
directly from your code base if it was written in TypeScript and import it
from a k6 script. It'll just work. And why does that matter?
Because in this script, what we're doing is we're going to
test the website at the protocol level. So I want to make sure that I shoot an
HTTP request to it and I actually get a response that looks the way I want and
I'm going to simulate that when I click this button, the rest API that's under the hood
actually responds the way I expect it to respond. And so to do that here we define
a scenario. This is a bit of a detail, if you know already about
k6, you're aware of it. Otherwise I invite you to take a look. But in this test we're going to group
the results to also show you how the end of test summary makes
this really, really nice. We're going to group two functionalities
that we're testing. The first one, we want to make sure that the
website is up and running. And here with TypeScript we can actually
get some proper type definition support and we can make sure that we don't
make mistakes and we provide the right values. If I were to change the
type of the refined response, I would get a warning. We also have this assertion framework
that's shipping right now also with k6. And what we do is we shoot our request, we verify we get the proper status
code and we verify that HTML and to simulate pressing the button, we can actually send the HTTP
request to the API. And here we actually get a lot of benefit
from TypeScript because
we can leverage the types that we have just
imported. And in this case, what it's basically going to be doing
is just making sure that everything fits into place and everything
looks exactly how I want. With those expect statements,
if anything doesn't, the test immediately stops
and gives you a nice warning. But the really nice thing is that you
don't have to simulate pressing that button, you can actually press
it for real. In the scenarios, you might have noticed that we have
this UI scenario and what this does, it's going to leverage our browser module, which has an API that's
playwright compatible and we can actually open a browser in the background, which is Google Chrome is
going to be in headless mode. You're not going to see it, but you
could if you want it with an option. And we're going to go to the page,
we're going to click the button, take a screenshot just to be sure
that things look the way we expect, and then we can do the same thing. We can verify that the actual DIV shows
it has the right title and so on and so forth. But to show you in practice how that
looks like and let's pray the demo gods to be on our side. So the two scenarios
are running in parallel. The UI always takes a bit more time
because you need to spin Google Chrome, but you see this is the kind of results
you get. So if we start from the top, we have the overall results and here
you're going to see results specific to each protocols that you've been using
or technologies that you've been using. So in this case we did some
HTTP and we used the browser. And the nice really nice improvement
here and people who might be seasoned k6 user will know about is that we also show
you the scenarios and the groups that were actually used inside. And all those results are specific to
the scenario or the group that you have defined in the past. And now I'm going to pass to Ayush who's
going to show you about open API and k6 studio. Thanks. So let me just drag it down. So let's say you are already
working on a backend application. You might sending new request,
since it's an active development, you might be changing the existing
ones and you don't want to keep your performance test manually changing. Like
Théo showed, you're sending a request, you have to change the request
structure, maybe response structure. So that's why we have the open API to
k6 converter. It's a command line tool. You can conveniently use help command
to see all the different arguments and everything it takes. You
can install it with NPM. And here we are using the same QuickPizza
application and convert its OpenAPI schema to a TypeScript client. I'll just copy this code and
will quickly explain what it's doing. So after
writing the tool name, we are giving it a path to the
OpenAPI schema. It can be a URL, it can be a local file path, anything. Then I'm not concerned about all the
requests which are defined in the schema because I'm only concerned
on the user's one. So I'm filtering it with
the only tags "user". Last, I'm giving it the path where it
should generate this client. And last, including a sample script so that
I can get started very easily. Let's just run it. And here we go. The client is generated. This is the TypeScript client you're
not expected to modify it directly. And this is a sample script. I'll just remove some of the requests
so that we can easily take a look at others. So we'll now go with
the admin login and logout. And as you can see it generated the sample
data for me as well from the example. So if you have examples and
types defined in your schema, it'll generate them for you. In
the register user, for example, you can see it generated all the types
because as Théo showed you right now, he added the pizza types and everything. And I'm not fond of too much manual code, so that's why it's completely automated. You have all the types
and everything present. And let's take a look at how it works. I don't want to see the code to
know the response structure as well. So what I will do here is
start typing the response data and see what it has.
It has data and response. I'll go with data and it already
has a username that's helpful. I'll replace the password
and add a base URL here. So I'll be using the local
host one, it's already running and that's it. And let's say there are
some things I'm not defined already. For example, the CSRF token I
know is returned in the cookie. Oops. So yeah, because of the TypeScript, the cursor is also helping
me complete things directly. And that's it. You can
just directly run it and voilà everything works. We
have the CSRF token, cookie, printed and everything. So if you
add a new request or change anything, you can just regenerate the client at
all. Now let's take a step further. I don't even want to write this much
code. So I'll switch to k6 studio. And as I mentioned, it's a no-code
tool. You have three stages. You start with a recorder,
it'll give you a browser window, it can go through your whole user flow
and this application will record all the requests and responses. Then you create a generator where you can
define tools to modify the behavior of individual requests or the data. And
then you can do a validation run, which will be a single virtual user
run of seeing everything works or not. And then you can export it
to a case script or directly
run it on Grafana cloud. So let's take a quick look.
I'll again use QuickPizza. So as soon as I start recording, it'll give me this browser which
is connected to the application. We'll do a normal user login flow. So let's use the default
ID and password sign in. And I was successfully able to
sign in. Let's just close this. And as you can see, it recorded everything
which generated from the browser, even the static assets. We are not
concerned about them right now. So I'll just hit stop recording.
I'll see everything looks good. I'll create a test generator here.
You can filter on the domains. I'm only concerned about
quickpizza.grafana.com So
I'll just hit continue. And as you can see, we have all
the requests and response recorded. Let's just do a validation script
right now and see what happens. Oh, we are getting 401's in
the actual login request, which we are trying to test. Let's see
what it's showing. Invalid CSRF token. So that's because the recorded CSRF token
is hardcoded and we want to manually change it. In one of these requests, we must be getting the CSRF token
and going through all is tedious. So let's just search where we are
getting the token. Here it is. It's in this request response headers.
So these are the test tools we can use. We already have a default verification
one which checks the response status directly for us. And we'll add a new rule correlation
which will extract and reuse dynamic data. So I want to extract the CSRF
token from response headers. So I'll just change the target to header. I know it begins with "csrf=" and ends with a semicolon. And that's it. As you can see. Let me remove this. It extracted the value from this request
automatically and replaced it in the actual login one with the payload.
As you can see, it automatically got converted
to a variable. If you want, you can customize the selector and
replace it to individual request. And let's see what happens if we
run the validation now. And yeah, it worked. We have a
new CSRF token already. We can rerun it and see if
what happens. And again, we have a new token fetched from
the previous request and replaced automatically. And that's it. So we can now save this
generator to reuse it if we need. Or we can directly export the script here, get it stored and use it anywhere you
like. You can use k6 CLI, run it in cloud, in your CI, everywhere. So now you have a script without
writing any code at all. And yeah, that's it for the demo. Let's
switch back to the slides. So to wrap up, k6 version one marks our first
stable production ready release of k6 with a dedicated support
path and explicit guarantees. So if you pick it up today, we got
your back for the years to come. It's also now easier than ever
to leverage the k6 ecosystem. I mentioned extensions, we have a couple of libraries out there
that people can use and a couple of projects that are built on top
of it. And with this ecosystem, it becomes easier and easier along the
way to integrate reliability testing inside of your CI pipelines
or your development pipelines. And finally, with the addition of the OpenAPI code
generation as well as with the k6 studio app, we think that testing is actually
made even easier for both larger groups and larger organizations which
might not want to have to write the whole code for testing their application
when the code for their application is already there and ready to use. But also for people or team
that either don't know how to code or don't have the
patience to actually learn to
code for k6 or even to code at all. And before we leave you with this talk, I want to make sure to send out a
very big thank you to everyone who contributed features, filed
or fixed bugs along the way. Like I said, it's been almost 10 years. Same for all the people out there who
wrote extensions that will allow users to use specific technologies that we don't
necessarily have the need to support in the core, but that people pick
up along the way. And so yeah, a massive thank you for all
of you who have contributed. If you want to learn more about k6
in case you're on the newer side, you can scan this QR code. It'll get you to our get started
document documentation page. And as always, we'd love
to hear your feedback. k6 is what it is because of
our users, our contributors, and all the feedback we have
received over the years. You can find us on GitHub and you can
also find us at the Ask the Experts booth right after. And yeah, see you
there. Thank you very much.

