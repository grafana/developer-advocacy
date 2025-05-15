# Simulate Real User Workflows | Introduction to Grafana Cloud Synthetic Monitoring

Just because your app is up doesn't mean it's working. Behind the scenes, users could be facing failed checkouts, broken ...

Published on 2025-05-01T18:02:16Z

URL: https://www.youtube.com/watch?v=bXjvH-RBAPA

Transcript: Software teams often lack visibility
into how end users are actually experiencing their applications. An application may appear
to be running smoothly, but behind the scenes critical
workflows could be failing, preventing users from
completing essential actions. Without proactive monitoring,
these issues often go unnoticed, which leads to customer
dissatisfaction, revenue loss, and increased operational burden. This disconnect between how systems
appear to be performing and what users are actually experiencing is what Grafana
Synthetic Monitoring is built to uncover and fix. With Grafana
Cloud synthetic monitoring, you can continuously test and validate
your most important user workflows before issues reach your users. Whether it's a simple ping check or
a complex end-to-end browser test, you'll have visibility into when, where,
and why users are hitting problems. Let's explore what's possible with
Grafana Cloud Synthetic Monitoring and how can enable your team to confidently
deliver reliable services. Grafana Cloud Synthetic Monitoring
allows you to proactively simulate user behaviors.
You can run a variety of different checks: HTTP, Ping, DNS, TCP, Traceroute, and
advanced browser checks. All these checks can run from globally
distributed public and private probes. This means you're no longer
reacting to user complaints. You are testing proactively from dozens
of global locations like Calgary and Tokyo. These checks help you assess
availability, responsiveness, and functional correctness, which ensures a consistent
seamless experience for your users. For teams using infrastructure as code, all checks can also be
managed via Terraform, which streamline setup and
automation across environments. Browser checks take synthetic
monitoring to the next level. They allow you to validate entire
user journeys, not just endpoints. With browser checks, you can simulate user interactions
on a webpage such as navigation, clicking, form submission, and scrolling, execute requests (both
at the protocol level), and within the browser to emulate
realistic interactive user scenarios. Configure window sizes to test across
various device views, including mobile, tablet, and desktop.
Browser checks leverage k6 scripting API, which provides playwright
compatibility in the browser module. This means you can reuse your synthetic
monitoring scripts for k6 performance testing and vice versa, enabling you to interact
with your application and
gain meaningful performance insights. Let's walk
through a simple example. We'll use a custom browser script
to test a sample e-commerce site. This script mimics a real user who
browses products and completes a purchase. Grafana also provides a recorder
that generates browser check scripts automatically for you.
But in this example, we'll highlight what's
possible with custom scripts. We'll start the script by
importing the k6 browser module. We'll choose the target URL to test,
which is the demo website. Next, we will mimic the following user
actions: Visiting the homepage, checking for product listing, viewing a product and adding a product
to the cart, completing a checkout, and finally validating a success message.
Once our test is complete, we can visit Grafana Synthetic Monitoring
out-of-the-box dashboard with real time performance insights. Alternatively, you can record a browser
check using k6 Studio, an open source desktop application that
helps you create k6 test scripts quickly and easily via a visual interface. Now let's review the browser check
results dashboard. In this dashboard, you'll see uptime and
reachability core web vitals like FCP, LCP, TTFB, and CLS charts
for test assertion response time, request logs, and more.
With these insights, teams can detect and resolve performance
issues faster often before they impact users. If you want to see it in action, explore the live dashboard example at
Grafana Play Synthetic Monitoring linked below - where you can view a dashboard
with a variety of active checks. To get started with Grafana
Synthetic Monitoring, sign up for a free Grafana Cloud
account. Check out the link below.

