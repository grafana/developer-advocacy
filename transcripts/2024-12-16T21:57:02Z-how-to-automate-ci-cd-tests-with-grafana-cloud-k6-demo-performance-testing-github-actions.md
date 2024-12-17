# How to Automate CI/CD Tests with Grafana Cloud k6 | Demo | Performance Testing | GitHub Actions

Performance Testing with Grafana Cloud k6: Seamlessly Integrated into CI/CD Pipelines In this video, Grafana Solutions Engineer ...

Published on 2024-12-16T21:57:02Z

URL: https://www.youtube.com/watch?v=4K2JdkDxclA

Transcript: Hi, I'm Sean Carolyn,
Grafana solutions engineer, and I'm here to show you how Grafana
k6 integrates with CI/CD pipelines. So you can always be testing
even before your code reaches QA. Downtime isn't just a technical
problem, it's an organizational one. It delays projects, lowers team
morale, and increases onboarding costs. By making performance testing an
integrated part of your CI/CD process, you can catch bottlenecks
early, avoid costly downtime, and give your team back the time they
need to focus on meaningful work. With Grafana k6 and continuous profiling, you get developer friendly performance
testing tools designed for modern workflows. These tools integrate seamlessly with
your CI/CD systems to ensure your applications are reliable and
optimized. Let's do a demo. Here's our sample app, Quick Pizza, a modern frontend that needs
to perform reliably under load, especially during peak ordering times. Now let's say we've got
a small change to make. We need to post an update
to the homepage UI. Let's go ahead and make an edit to
our file here and commit our change. And now the magic happens. A GitHub action is kicked off to trigger
a load and performance test using Grafana k6 Cloud. This ensures that every code change is
tested for performance impact before it hits production with no
manual intervention required. And let's take a look at the test and
I can click this link here to jump directly over to my Grafana Cloud account
where I can see the results of the test. Here we can see
3,000 requests were made. We had zero failures and we
had a good response time. So this test passed, things look
good, something had gone wrong. We could notify a developer right away, potentially catching dangerous
things before they get to production. Advanced users might also like to
take advantage of Grafana's continuous profiling feature. With this
feature, powered by Pyroscope, we can pinpoint individual lines of
code that might be causing performance issues. Before Grafana Cloud k6, Carvana often faced barriers to performance
testing. It was hard to adopt, time consuming to create tests,
and lacked customization options. As a result, the test coverage was low
and the developers didn't
trust the results enough to make performance testing a
core part of their workflow. Let's look and see how the Carvana team
transformed their developer testing with Grafana. With Grafana Cloud k6, we've seen a hundred percent
increase in the test creation speed. So they basically doubled the speed
at which they could create new tests. We saw 115% boost in the numbers of tests, so there was greater coverage. And now the developers are able to
do most of this work themselves, resulting in more confidence,
faster deployments, and freed up time for other tasks. These results reflect how developer
friendly tools can lead to better, more reliable applications and fast
safe software delivery. To recap, we showed you Grafana k6 testing
integrated directly into a workflow. And you've got a small peek at
our continuous profiling tool, which helps pinpoint problems in your
code before they reach production. Thanks for watching this demo, and feel
free to reach out to us at the URL here.

