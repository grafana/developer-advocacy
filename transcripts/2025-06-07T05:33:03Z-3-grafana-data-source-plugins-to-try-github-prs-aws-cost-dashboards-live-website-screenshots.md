# 3 Grafana Data Source Plugins to Try: GitHub PRs, AWS Cost Dashboards,  Live Website Screenshots

Published on 2025-06-07T05:33:03Z

## Description

Discover 3 Grafana data source plugins that go beyond metrics: annotate PRs with GitHub, visualize AWS cloud costs instantly ...

URL: https://www.youtube.com/watch?v=bYyYyhP_ty4

## Summary

In this lightning talk, Sarah Zinger, an engineer at Grafana Labs, discusses three essential data source plugins to enhance your Grafana stack: the GitHub data source plugin, Amazon Athena, and the Infinity plugin. She explains the benefits of using the GitHub plugin to track contributions and correlate code changes with system performance, emphasizing its easy setup and annotation features. Zinger highlights Amazon Athena's capability to monitor AWS cloud costs and query logs using SQL, showcasing its user-friendly dashboard integration. Lastly, she introduces the Infinity plugin, which allows users to connect to various web APIs, demonstrating its use in retrieving website screenshots for better context during monitoring. Zinger encourages viewers to explore the extensive catalog of over 159 data source plugins available in Grafana and to contribute to the community's growth.

# Lightning Talk on Data Source Plugins

Hello! Hi, I'm Sarah Zinger, and I'm an engineer here at Grafana Labs. Today, I'm going to tell you about three data source plugins that you might want to add to your stack after this talk. I'm not sure if we'll have time for questions, but if we don't, please come find me at the Ask the Experts booth afterward.

This is a lightning talk, so let’s jump right in.

## 1. GitHub Data Source Plugin

First on my list is the **GitHub data source plugin**. If you're not using GitHub, you might want to check out plugins for GitLab, Vercel, Netlify, Drone, or any other service that helps you track deployments.

### Why Use the GitHub Plugin?

There are many cool things you can do with this plugin. For example:
- **View your contributing stats** over time on a Grafana dashboard. It may not be terribly useful, but it’s kind of fun!
- **Wrangle your team's tech debt** by firing off an alert every time your open issues count exceeds a certain threshold.
- **Correlate code changes with downtime** using the annotations feature to mark every new pull request that has been merged.

### Setting Up the GitHub Plugin

To set up the annotations feature, you’ll follow three steps:
1. **Install the plugin**: Go to the connections page, search for the GitHub data source, and click the install button. This should take less than a minute. You'll know it's ready when you see the "Add a New Data Source" button.
   
2. **Configure the plugin instance**: Use either a GitHub personal access token or a GitHub app, both of which can be accessed from your GitHub developer settings.

3. **Create an annotation**: Select the dashboard you want annotations for, go to the settings page, and select the annotations tab. Choose the GitHub data source instance you just created, and use the query editor to query GitHub for the pull requests you want to annotate.

For example, I selected all pull requests with my project name in the title for the Grafana repository in the Grafana organization. Now, on my dashboard, I can see dotted lines marking every merge that matched my query. When I hover over those lines, I get the title of the pull request and a URL to it. By pairing this with existing metrics, I can see that I shipped a bug earlier, which caused some errors, but after the next PR, everything seems to look better. Always good when the bug fix works!

## 2. Amazon Athena Plugin

Next up is **Amazon Athena**, or really any plugin that allows you to monitor your cloud provider's costs.

### Why Use Athena?

Athena lets you write SQL queries against data stored in S3, making it very flexible and powerful. Here are some use cases:
- Many people use Athena to query their logs with SQL, which is often simpler.
- If your organization has a business intelligence team collecting user tracking data, they can analyze how downtime affects user retention.
- You can monitor all your AWS cloud costs with just one click.

### Setting Up the Athena Plugin

The setup process is similar to the GitHub plugin:
1. **Install the plugin**: Go to the connections page, search for the plugin, and click install.
   
2. **Create a new instance**: Configure this data source instance with your AWS credentials, ensuring they have the right permissions for Athena and AWS. 

3. **Import a pre-bundled dashboard**: On the configuration page of your Grafana plugin instance, click on the dashboards tab and import the cost and usage report dashboard. This will allow you to view all your AWS costs across services and regions without writing any queries manually.

## 3. Infinity Plugin

Last, but definitely not least, we have the **Infinity plugin**. This plugin lets you query a wide variety of APIs on the web in almost any format.

### What Can You Do with the Infinity Plugin?

The possibilities are vast! Here are a few ideas:
- Connect to public APIs like weather data.
- Link with custom APIs specific to your organization that don’t have a dedicated data source.
- For fun, see how hard it is to display a live screenshot of a website on a Grafana dashboard.

### Setting Up the Infinity Plugin

To set it up:
1. **Install the plugin**: Similar to the previous plugins, search for it in the connections page if it’s not pre-installed.
   
2. **Configure a new instance**: Set the base URL for the main endpoint of Google's Page Speed Insights API, which provides interesting data about performance and accessibility, and also takes screenshots.

3. **Create a query variable**: Go to an existing dashboard, click settings, and find the variables tab. Create a new variable, select the Infinity instance, and define the query for the variable. This allows you to select a property from the JSON response that contains a base64 encoded string for the screenshot.

Once you’ve set it up, you can render the screenshot in a Grafana text visualization panel. This could provide context during incidents when you’re managing multiple tabs.

### Conclusion

That covers the three plugins from this talk, but there are many more interesting data source plugins available—159 in our catalog, and more are being added every day. 

Remember, the goal at Grafana is to bring all your data into one place, creating a comprehensive picture of how your application is performing, including deployments, cloud costs, web accessibility, and more.

Don’t overlook advanced features like annotations, bundled dashboards, and variables, as they can significantly enhance your experience. If we’re missing a data source you need, please submit it to our catalog.

Lastly, a big shout-out to all the contributors inside and outside of Grafana who make these data sources possible. Thank you so much, and please submit your bug requests, feature requests, and documentation fixes. This is a great community effort.

Thank you!

## Raw YouTube Transcript

Hello. Hi, I'm Sarah Zinger and I'm an
engineer here at Grafana Labs, and I'm going to tell you about three
data source plugins to add to your stack after this talk. I'm not sure we're going
to have time for questions, but if we don't just come find me at the
Ask the Experts booth after this talk. Okay, so this is a lightning talk, so
we're just going to jump right into it. Number one on my list today is
the GitHub data source plugin. Or if you're not using GitHub, you might want to check out the plugins
for GitLab, Vercel, Netlify, drone, or whatever you're using that
can help you track deployments. So why might you be interested in
the GitHub data source plugin? Well, there's lots of cool things
you could do. For example, you could use the plugin to view your
contributing stats over time on a grafana dashboard, which okay, is
maybe not terribly useful, but kind of fun. Or maybe you
want to wrangle your team's tech debt and you want to fire off an alert
every time your open issues count raises above a certain threshold. Or maybe you want to correlate
code changes with downtime by using the annotations feature to mark every
new pull request that has been merged. Let's dig into how to set up
this last example. Basically, it takes three steps. You install the
plugin, configure a plugin instance, and then create an annotation.
Installing the plugin is super easy. You just go to the connections page, search for the GitHub data source
and click the install button. It should take less than
a minute or so to install, and you know you're ready to go when you
see the add a new data source button. After you've clicked it, we need to configure this new data source
instance with our GitHub information. We can do so with either a GitHub
personal access token or GitHub app, either of which should be pretty easy
to access from your GitHub developer settings. Next, we'll pick the
dashboard that we want annotations for, and we'll go to the settings page
and select the annotations tab. From there, we'll select the GitHub
data source instance we just created, and now using the query editor
on the annotations page, we'll make a query to GitHub for the
pull requests we want to see annotated on our dashboard. In my example here, I selected all pull requests that have
emerged in my project with my project name in the title for the
Grafana repo in the grafana org. Now, on my dashboard, I can see these little dotted lines
marking every merge on GitHub that matched my query. When I hover over those lines, I get a title of the pull request and
a URL to the pr. By pairing this with existing metrics, I can see I shipped a bug earlier
that seems to have caused some errors, but after the next pr,
everything seems to look better. Looks like my bug fix worked. Yeah,
always good when the bug fix worked. Alright, next up on my list of cool data sources
to install after this talk is Amazon Athena, or really any plugin that would let you
monitor your particular cloud provider's costs. So why Athena? Well, Athena lets you write SQL queries
against data stored in S3, so it's very flexible and powerful.
There's lots you could do with it. For example, a lot of folks like to use
Athena to query their logs with sql. Querying logs with SQL
is often just easier. Or maybe your organization has a business
intelligence team and they have a bunch of different user
tracking data files and CSVs, and they're trying to put them all in
one space and ideally next to their other observability data, so they can make analysis to
see how does downtime affect things like user retention.
Or you could do what we'll show today, which is to monitor all of your AWS
cloud costs with just one click. That sounds pretty nifty.
Let's take a look how to do it. So how it's going to feel pretty
familiar, we need to install the plugin, configure an instance, but this
time, rather than make an annotation, we'll import a dashboard that
comes pre-bundled with the plugin. Again, we'll go to the connections page, search for our plugin and click install,
and then we'll create a new instance. From there, we can configure this data
source instance with our AWS credentials. We need to make sure that
whatever credentials we use
has the right permissions to view and query Athena and AWS. We'll also need to make sure that we've
configured our cost and usage reports to get sent to Athena. Here's a QR code to the docs from AWS
if you're interested in learning more about how to do that.
Finally, the fun part on the configuration
page of our Grafana plugin instance, we'll click on the
dashboards tab. From there, we can see we have two dashboards
that come pre-bundled with the plugin. All we have to do is import the cost
and usage report dashboard and boom, we can see all of our AWS costs across
all of our services and regions without having to manually write
any queries ourselves. Okay, last but definitely not
least, the Infinity plugin. The Infinity plugin lets you query all
kinds of APIs on the web in almost any format. It requires a little bit of configuration
on our end to inform the plugin on the shape of our data, and then in exchange, it lets us connect to
almost anything on the web. So what could you do
with the Infinity plugin? More like what can't you do with the
Infinity plugin? If you're new to Grafana, it's a great way to connect to data fast
and start building an understanding of Grafana features. You can start by playing around with
a public API that maybe you're already familiar with thinking like weather
data or something simple like that. Or you might consider using it to connect
with some custom bespoke API that just your organization uses that will
never really make a data source for, but you can still see that data
alongside all your other Grafana data. Or maybe you're like me and one day you
just kind of got fixated on a very weird question of how hard would it be to see
a live screenshot of the website that you're working on a Grafana
dashboard. And the answer is, it's pretty easy with the Infinity plugin.
Let's take a look at how to do that. Well, again, we just install the
plugin, configure a new instance, and then this time we'll create a query
variable that we'll use in a panel. And actually, depending on your
setup and version of Grafana, you may not even need to install the
plugin as these days it's getting pre-installed. But if it's not, just
search for it in the connections page. Same deal as before. Okay, next we're going to configure it
with a base URL for the main endpoint of Google's Page Speed Insights,
API. There's a really cool API. It contains all kinds of interesting
data about page speed, performance, accessibility, and by the
way, it takes a screenshot, it happens to, so we're going to put then
our configuration process
a query parameter for our API key as well as A URL for the website
that we're trying to take a screenshot of. So next we'll go to an existing dashboard
and we'll click the settings and we'll find the variables tab. From there, we'll create a new variable and ensure
that the type of the variable is a query, and we'll give it a name
in this case screenshot, and we'll select our Infinity instance.
So now we're defining the query for this variable. In this case, we want to select a property off of the
JSON response that we get back from the page speed API that contains a
base 64 encoded string representing a screenshot of our website. And now that we have that
string stored in a variable, we can use it as a source attribute for
an HTML tag that we specify as content in grafana's text visualization
panel. Once we've done that, we should see our screenshot rendered. Here you can see a nice picture of a
website I'm working on for my mom's garden club, by the way--Hi, mom--And here we go. Here it is in a dashboard. So
why would anyone do this? Well, mostly I just think it's fun, but I also think having screenshots of
the websites that you're working on could be a really great way to gain context
quickly of the dashboard that you're looking at, especially during an incident when you
might have many tabs open working on many different websites.
And of course, the page insights API is not
really even about screenshots. It's just kind of a fun side
effect. It also has a lot of really, really wonderful information about
things like web accessibility. So you can see below the screenshot
here, I have some accessibility audits, and here you can see in red that I have
a problem with some color contrast. So that's something for me to go work
on so that my website is viewable for as wide an audience as possible. Well, that covers the three
plugins from this talk, but that's far from the only
interesting data source plugins. Probably not even the most interesting
use cases out there for the ones that I showed. Last I checked, we have 159
data source plugins in our catalog, but we have more and more every day.
As you've heard announced recently, if there's one takeaway
from this Lightning talk, it's at the big tent here at Grafana
is even bigger than you think. It's not about supporting the common solutions
for metrics, logs and traces, et cetera. It's about bringing all of your data into
one place to paint as big of a picture as possible of how your application
is doing, including deployments, cloud costs, web
accessibility, and a lot more. And also don't sleep on some of our more
advanced features that work with data sources like annotations, bundled
dashboards, and variables. They can make all the difference. And if for some reason we're
missing a data source here, please submit it to our catalog. And also, I just wanted to give a big shout
out to all the contributors, both inside of Grafana and
also outside of Grafana, all over the world who make
these data sources possible. Definitely thank you so much and submit your bug requests and feature
requests and documentation fixes. This is a great community effort.
Okay, that's it. Thank you.

