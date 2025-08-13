# Grafana 12.1 TL;DR – Top Features You Need to Know

Published on 2025-07-28T13:57:02Z

## Description

Grafana 12.1 is here, and it's packed with features you'll actually use. Smarter alerting, dynamic dashboards, new regression ...

URL: https://www.youtube.com/watch?v=GOflMq8nSwg

## Summary

In this video, Shawn from Grafana Labs announces the release of Grafana 12.1, highlighting its user-focused features, including smarter alerting, enhanced dashboards, and tools to maintain instance health. Key updates include the Grafana Advisor, which performs health checks on instances, a regression analysis transformation for dynamic data modeling, and customizable variables for more interactive dashboards. The redesign of the alert management page improves performance and usability, and there's an upgrade for importing alert rules from YAML files. Additionally, security enhancements for BigQuery service accounts and support for Azure's federated credentials are discussed. Shawn encourages viewers to explore the new features and provide feedback.

# Grafana 12.1 Release Announcement

Hey folks, Shawn here from Grafana Labs, and I'm excited to announce that **Grafana 12.1 is officially out**! While it's not a major release, it is packed with features you'll actually use. So buckle up!

## What's New in Grafana 12.1

This release includes:

- **Smarter alerting**
- **Smoother dashboards**
- **Quality of life upgrades**
- **A new tool to help keep your Grafana instances healthy**

### Grafana Advisor

First up, let's talk about what will help you and your team avoid the classic "Hey, Grafana is broken!" situation where nobody notices until a blank dashboard or an error pops up. The **Grafana Advisor**, which was marked experimental in the Grafana 12 launch, is now officially in public preview. It is designed to run periodic checks on your instances to identify issues like:

- Broken data source connections
- Needed upgrades for plugins
- Misconfigurations

The advisor surfaces these issues in a centralized view for quick addressing. You can think of it as an easy health check engine for your Grafana setup. Additionally, it has the powerful ability to hook into Graf's LLM plugin, allowing you to bring your own LLM key from Google, Open AI, or Claude for diagnosing issues. 

**Note**: OSS users will need to enable the Grafana Advisor toggle, while Claude users will see the advisor by default.

### Regression Analysis Transformation

Grafana 12.1 introduces a **new regression analysis transformation**. This lets you apply a mathematical model—whether linear or polynomial—to any dataset in Grafana. Why does this matter? Because it allows you to predict values at points in time that don't even exist in your original data. This feature is super handy for:

- Estimating missing data
- Identifying trends
- Building smoother visualizations

It updates on every data refresh, making it dynamic and not just a static snapshot. Essentially, you get a smarter lens on your data without the need to export it to Excel or use a Jupyter Notebook.

### Custom Variables and Visualization Actions

More on variables: Grafana 12.1 brings a new way to make dashboards more interactive with **custom variables and visualization actions**. Instead of hardcoding everything, users can now input values in real-time, like entering a problem description when opening a support ticket or setting a target temperature in a control panel. 

This subtle feature opens the door to a bit of API auto-remediation and more dynamic workflows.

### Server Configurable Quick Time Ranges

We have also added **server configurable Quick Time ranges**, which are designed for admins to define custom presets for the dashboard time picker. For instance, if your team always looks at the last 24 hours or this week within a dashboard, you can now embed that logic directly into your server config as code. 

**Shout out** to Chris Hodges from the community for contributing this feature! It's a huge win for all users of Grafana, and we love to see ideas and solutions coming from the community.

### Enhanced Currency Formatting

For anyone working with financial data, Grafana 12.1 enhances **currency formatting**. You now have the option to display exact numbers instead of abbreviating them to something like 1.24M. Just click the currency financial dollar format to get precise, readable numbers, and yes, it supports suffixes like pounds, dollars, yen, and more.

## New Alerting Features

We also use alerts to be proactive about catching issues. In Grafana 12.1, we’ve redesigned the alerting page for better performance. It now features:

- **Faster performance through pagination**: No matter how many rules you've got, you can toggle between two distinct views: a grouped view, which organizes rules, and a flat list view, which shows the status of alerts (whether firing or not). This makes it easy to find or bulk edit your rules.

- **Importing Alert Rules**: If you're migrating from Prometheus, you can now import alert rules from YAML files directly into Grafana managed alerting. Even if you're not using a ruler, just upload the file in the UI, and boom, your rules are in!

## Improvements to Data Sources

This wouldn't be a Grafana release without improvements to the big tent family of data sources. There’s a significant win for security teams worldwide concerning **BigQuery and service accounts**. Instead of handing someone the keys to the kingdom, you can authenticate Grafana using a less privileged identity that can impersonate the actual BigQuery service account.

With this, even if a Grafana account token gets stolen, an attacker cannot query BigQuery unless they can also impersonate the target account, which requires proper IAM permissions.

Additionally, on the SSO side, Grafana now supports **intra-workload identity** (formerly known as Azure AD). If you're running Grafana in Azure and using federated credentials, this simplifies the OAuth flow and tightens your security.

**Shout out** to [mehighlow](https://github.com/mehighlow) from the community for contributing this feature!

## Conclusion

Grafana 12.1 is definitely cleaning up and introducing new features that enhance user experience. All these features are available right now in Grafana, OSS, and Cloud. 

If you're not already running 12.1, go check it out and test what's new! As always, let us know what you like and what’s not working. You can find full release notes at [grafana.com/docs](https://grafana.com/docs) or check out the Grafana 12.1 What's New blog post linked below.

Thanks for watching, and I'll see you guys in the next release!

## Raw YouTube Transcript

Hey folks, Shawn here from Grafana Labs and I'm excited
to announce Grafana 12.1 is officially out. And while it's not a major release,
it is full things you'll actually use. So buckle up now. This release includes
smarter alerting, smoother dashboards, some long requested
quality of life upgrades, and even a new tool that helps keep
your Grafana instances healthy. So let's start with what will help you
and your team avoid the classic. Hey, Grafana broken. Nobody noticed until
a blank dashboard and error popped up. The Grafana advisor, which was marked experimental
in the Grafana 12 launch
is now officially here in public preview and is designed to run
periodic checks on your instances to identify issues like broken
data source connections, needed upgrades for plugins
and misconfigurations then
surfaces them all in a centralized view. To address quickly, you can view the advisor sort of like
an easy health check engine for your Grafana setup with the powerful
ability to hook into Graf's LLM plugin, where you can bring your own LLM
key from Google, Open AI Claude, and have the advisor diagnose issues
for you. So if you are an admin, definitely start to use it and give us
feedback on how we can make this even better. OSS users will need to
flip on the Grafana advisor toggle, but Claude users will see
the advisor by default. Grafana 12.1 introduces a new
regression analysis transformation. This lets you apply a mathematical model, whether that be linear or polynomial
to any dataset in Grafana. Why does this matter? You may ask because now you can predict
values at points in time that don't even exist in your original data. This is super handy for when you're
trying to estimate missing data, identify trends, or just build
smoother visualizations overall, it updates on every data
refresh too, so it's dynamic. It's not just a static
snapshot. Basically, you get a smarter lens of your data
without having to export it to Excel or break out a Jupyter Notebook. My
Python friends will totally get that one. More on variables 12.1 also brings a new
way to make dashboards more interactive with custom variables and
visualization actions. Essentially, instead of hard coding everything users
can now input values in real time, like entering a problem description when
opening a support ticket or setting a target temperature in a control
panel. It is a subtle feature, but it opens a door to a bit of API auto
remediation and more dynamic workflows. Then we have added server
configurable QuickTime ranges, which were designed for admins to now
be able to define custom presets for the dashboard time picker. So maybe your team always looks at the
last 24 hours or this week within a dashboard, you can now bake that logic
right into your server config as code. Shout out to Chris Hodges
from the community for
contributing this feature. This is a huge win for all
of us users and Grafana, and we always love to see ideas and
solutions coming from the community. And finally, for anyone
working with financial data, Grafana 12.1 enhanced currency formatting
now gives you the option to display exact numbers instead of abbreviating
it to something like 1.24M. All you have to do is just click the
currency financial dollar format to get precise readable numbers. And yes,
it supports suffixes two like pounds, dollars, yen, and so forth. But we
aren't always just staring at dashboards. We also use alert to be a bit
more proactive at catching issues. So let's talk about what's
new in Grafana alerting. Now, for those who have managed hundreds
or thousands of alert rules, the old view could get a little
sluggish per se. Grafana 12.1, however introduces a redesign page with
faster performance through pagination. Regardless of how many rules you've got, you can now toggle between two different
distinct views, a grouped view, which shows rules, organized,
and a flat list view, which shows the status of alerts,
whether it's firing or not, making it easy to find or
bulk edit your rules. Last, if you're migrating from
Prometheus, there's good news. You can now import alert rules from
YAML files directly into Grafana managed alerting. Even if you're
not using a ruler, you just upload the file in the UI
and boom, your rules are in. Now, this wouldn't be a Grafana release
without some improvements to the big tent family of datasources supported with 12.1. There's a big win for security teams
all around the world when it comes to BigQuery and service accounts. If you're unfamiliar with what
service accounts are in Google Cloud, you can think of it like this.
Instead of handing someone the keys to the kingdom, you say, Hey, for the next
10 minutes, you can act like the king, but you got to show me your
ID at the gate. Normally, when Grafana query is big query, you
authenticate using a service account key, which is a JSON file. It's
sort of a static secret, right? If that file leaks it's game over,
the attackers have full access. But with impersonation, you don't give Grafana a key to the
target service account directly. Instead, you authenticate Grafana using
a less privileged identity, that identity is allowed to impersonate
the actual BigQuery service account. Access to BigQuery only works
if impersonation succeeds, and that requires proper IAM permissions. So now if a Grafana
account token gets stolen, an attacker still can query
BigQuery unless they can
also impersonate the target account, which they can without IAM.
Additionally on the SSO side of the house, Grafana now supports
intra workload identity, formerly known as Azure ad. If you're
running Grafana in Azure and using federated credentials, this simplifies the OAuth flow and
tightens up security for you all while reducing your overhead. So shout out to https://github.com/mehighlow from the
community for contributing this one. This is truly open source
at its best, right? So yeah, Grafana 12.1 is definitely cleaning up
and introducing a few new features that improve the user experience. All of these features are available
right now in Grafana, OSS and Cloud. So if you're not already
running 12.1, go check it out. Test whats new - and as
always, what's most important, let us know what you like
and what's not working. You can find full release notes at
grafana.com/docs or check out the Grafana 12.1. What's new blog post,
which will be linked below. Thanks for watching and I'll see
you guys in the next release.

