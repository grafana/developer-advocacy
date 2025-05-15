# Grafana k6 1.0 Overview and Demo: TypeScript, Extensions, More | What&#39;s New | Grafana Labs

Grafana k6 1.0, now generally available, delivers a number of features, such as TypeScript support, revamped test insights, and ...

Published on 2025-05-07T10:00:57Z

URL: https://www.youtube.com/watch?v=cIBQ3JvcdpU

Transcript: Grafana k6, version 1.0 is
officially released. Hi, I'm Bukola, a senior developer advocate at
Grafana. Over eight years ago, k6 began as an open source
project with a simple but powerful idea - helping developers prevent
fires in production by safely starting controlled ones during
the testing process. Since then, k6 has become a go-to for
developers, QA engineers, and performance testers,
looking to create reliable, scalable tests without the overhead
of handwriting every script, k6 makes it easy to go from idea to
execution and allows you to produce clean reusable testing code. k6 supports a wide variety of test cases, including high load performance tests
with spike stress and silk testing, browser-based testing to capture real
user metrics and identify front-end performance issues, synthetic testing to continuously
monitor your service performance. Today we're marking a major
milestone with the release of k6, version 1.0. This new release brings
a wide range of new and exciting features. The first feature is clear support and
semantic versioning guarantees so you can test with confidence. The second
feature is full TypeScript support, so you can write more robust
and maintainable tests. The third feature is extension support, so you can extend k6 without
extra tooling or custom builds, and finally, a completely revamped test summary that
gives you deeper and more actionable insight at the end of every run. All these updates double down on
our promise to make reliability testing predictable, scalable,
and developer friendly. Whether you're simulating 10
users or a hundred thousand users. Let's take a closer look at what's new.
Let's start with the first major update, which is that k6 now has clear
support and versioning guarantees. k6 has always prioritized
backwards compatibility. As the project grew, the need for well-defined boundaries
became more important. With version 1.0, we formalize these boundaries
so you can test with confidence. Here's what's included. First, k6 now follows semantic versioning. This means breaking changes will only
happen in major releases like version 2.0 and always with clear deprecation
warnings ahead of time. Second, k6 is committed to long-term support. Every major version will receive
critical fixes for at least two years. So whether you stay on version
1.0 or choose to upgrade later, you'll have the stability
and guidance you need. Third, we've defined a public API surface. If
you're building or using extensions, you now have access to stable
while documented go modules. All these changes are documented in
detail and you can find the full breakdown in our updated documentation linked
below in the description box. The next feature we're excited to
announce is native TypeScript support. This was one of the most requested
features from our community, and we are happy to deliver this update.
With native TypeScript support, you can now write more robust and
maintainable tests with full type safety, auto-complete, and
improved developer experience. You'll also be able to reuse your existing
TypeScript code and type directly in your k6 test. This makes it easier to integrate
performance testing into your existing workflows. The next feature we're excited to
announce is extension support for k6. In older versions, using extensions with k6 often
required custom builds and external tooling, but with this version
1.0 that is no longer the case. You can now use k6 extensions
or extend k6 itself without forking or a complex setup. k6 now supports importing a set of
pre-approved extensions directly into your test. The feature is already available for
tests ran in Grafana Cloud using k6 cloud run and k6 run dash dash local
execution and support for k6 will be rolled out in a future release.
Let's walk through an example script that uses the k6 slash
x slash faker extension First, import the k6 slash x slash
faker extension into your script. Next, we'll create a random name
using the faker dot person class, and finally, run your script as
you normally would. As you can see, there is no need for
dedicated tooling anymore. Another top request from the community
that we've delivered on in this version 1.0 is a completely modernized
end of test summary. This new summary includes
scenario specific metrics, group specific metrics,
hierarchical grouping of results, improved checks results, different levels of granularity of
information collected and displayed. By default, k6 shows a compact view that
surfaces the most important insights, but if you want more details, add the flag dash dash summary
dash mode equals full and k6 will walk through
every layer of the test. The final updates are updates to
stability and the quality of k6 core modules like k6 slash browser, k6 slash net slash grpc, and k6 crypto.
These are all now stable. You can now stream local test results
to Grafana Cloud using the command k6 run dash dash local dash execution. The k6 command has also been revamped
to be more powerful and flexible and provide a richer integration with
the Grafana Cloud k6 ecosystem. As we wrap up, I want to give a
big thank you to the k6 community. Whether you contributed code,
built extensions, filed issues, or simply advocated for k6
within your organization, this release wouldn't have
been possible without you. If you're ready to get started
with k6, head to k6.io/docs. There, You'll find everything
you need to dive in. Please see the link in
the description box below. You can also explore the full
release notes on our GitHub, and if you want to connect with others
using k6, visit k6.io/community. Thanks for watching, and I'll
see you in the next video.

