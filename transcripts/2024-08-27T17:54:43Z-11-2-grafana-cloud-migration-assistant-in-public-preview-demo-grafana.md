# 11.2 Grafana Cloud Migration Assistant in Public Preview (Demo) | Grafana

In this video, Mitch, the Director of Product Management at Grafana, introduces the Cloud Migration Assistant, available in public ...

Published on 2024-08-27T17:54:43Z

URL: https://www.youtube.com/watch?v=66W1UMHtX3U

Transcript: Hello from Grafana. Let's talk
about a new cloud migration tool. This is a new feature available in public
preview in Grafana 11.2 coming out in August 2024. I'm Mitch, I'm the director of product management
working with the Grafana team. We'll start with the problem this
feature solves. So imagine that like me, you've just set up Grafana on your home
computer to monitor something like your MacBook or your Raspberry Pi. So here I've got a couple of
dashboards running on local host, one that shows me the weather
conditions in different cities. And another that shows me
the state of my MacBook. You can tell I bought way too much
computer for a product manager. But let's say I wanna share this
dashboard with somebody over the public internet. That's impossible for me right now because
I'm running on local host or imagine a totally different scenario where you're
running Grafana Enterprise on premise with hundreds of users for your company, but you'd prefer the convenience and the
extra functionality of Grafana Cloud. So for example, maybe you want to use
Grafana OnCall, App Observability, or one of the other products
that we sell in Grafana Cloud. There's tons of functionality here
that's not available in open source. So how do you move the things over that
you have already created in your open s ource or enterprise instance,
like dashboards and data sources? So this is already possible to some
extent by using our APIs or using CLI tools, and you can learn about those
in our migration guide documentation. But what we've created here is a much
simpler point and click UI for migrating your things from Grafana Open Source
or Enterprise over to Grafana Cloud. So here's how it works. In
my open source instance, it's also available in enterprise.
Under Administration, General, I see an option to
Migrate to Grafana Cloud. This gives me some onscreen
instructions and a blue button, which invites me to create a
grafana.com account to set up my cloud stack. In this case, I've
already set up a cloud stack, so I'm gonna go and find the mirrored
option in my brand new cloud instance, migrate to Grafana Cloud, which
allows me to generate a token. And this token provides the connection
details and the credentials for me to connect my on-prem instance
to that cloud stack. The next step is to build a snapshot, which goes through my
instance and collects all of
the integratable resources. Right now, this feature supports
just dashboards and data sources. That's part of this being in
public preview. But in the future, we intend to add things like plugins. So you can migrate your your
panels and data source plugins, as well as alerts, annotations,
and other Grafana resources. So next, I press one
button upload snapshot, and that migrates all of those dashboards
and data sources over to my cloud instance. So now when I go into
dashboards and refresh the page, I can see all of the dashboards that I
just migrated over. So this is great. It's migrated my dashboards
and data sources. So I can see that weather overview
dashboard that I created. However, when I click into the Mac
overview, I see some errors, and that's because the Prometheus
instance that I'm running on my local machine is not accessible
over the public internet. But there's a solution for this too. This migration tool is compatible
with Private Data Source Connect. Private Data Source Connect allows
me to connect my network secured resources, which in my
case are on my computer, but they could also be in
a virtual private cloud on
a public cloud provider or otherwise in a private network. All I need to do is to deploy
an agent in my private network that establishes a connection between
my private network and Grafana Cloud so that I can query that data source.
So here I've deployed the agent, and when I turn it on, I can see that it's connected. That means when I go into the data
source that I just migrated over from my on-prem instance, I can choose to connect it
through that PDC connection. And once I've created that
connection, my dashboard loads, even though it was based on
private data. This is great. So there are some important limitations
to this migration tool as it stands. So right now we
can move over data sources, but if you've created a data source
based on a plugin that you've downloaded, that data source won't work until you
install that data source in Grafana Cloud. So, for example, I had this Astra DB data source that was
based on that plugin and that plugin's not installed. So I need to install
it before this data source will work, but once I install it, it will work
right away. The second thing is, like I mentioned, this currently works
for dashboards and data sources only. So things like alerts and annotations
won't migrate directly. However, you can follow our migration
guide like I mentioned before, to use the API or CLI tools to
migrate those extra instances. But one of my favorite things
about this feature just to mention, is the ability to securely migrate
your data sources along with their credentials. So in the past, you had to recreate all your data sources
because we didn't have a secure way to move the passwords or the tokens along
with the other configuration details. But now that's just a one button push
and you don't have to go and ask for all those passwords or ask your users
to reconfigure their data sources. So this feature is in public preview. That means that we
recommend you test it out, but don't rely on it in production
quite yet. So in your on-prem instance, you also need to enable a
feature toggle to use it. Feature toggles are tools we use
for features in public preview. The feature toggle for this one is
called On-prem to Cloud Migrations. So that's this one. So you enable this in your on-prem
instance in 11.2 or higher, and you'll be able to use this feature. We'll turn this on by default once it's
generally available in a later release. So this feature is free to use. It's available in Grafana
Open Source and Enterprise. Note that once you
migrate to Grafana Cloud, we have the most generous
free tier around, but you do pay to use Grafana Cloud
once you exceed those free tier limits, which I think are pretty high. So please feel free to check out
our migration guide, the docs, or just try the feature
out to learn more. Thanks.

