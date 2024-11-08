# Getting started with GitHub Data source plugin - Visualize your repos | Grafana

Learn step-by-step how to monitor and visualize your GitHub data by using the Grafana GitHub Data source plugin. It provides a ...

Published on 2024-08-15T08:50:01Z

URL: https://www.youtube.com/watch?v=DW693S3cO48

Transcript: Hello everyone. My name is Usman Ahmad and I work in
Grafana Labs as a Senior Developer Advocate. And in this video I got something
very exciting for you that how you can visualize your GitHub data such as
issues, pull requests, workflows, and commits using Grafana and visualize
them and view them in a Grafana dashboard. So let's get started. So we have this GitHub documentation
available on Grafana website. The GitHub data source plugin can
be used with any version of Grafana. Either you're using Grafana, OSS,
the Enterprise or the Cloud version. Basically what this plugin does is that
it connects with the GitHub API and fetches the data. And then you can
visualize them in a Grafana dashboard. So this plugin offers a lot of features
such as you can create the following types such as commits issues,
pull request, repositories, and so on. Also, this plugin provides some
additional features such as
you can visualize queries, use template variables. Also, configure
annotations and caching as well. Caching is available on
this plugin as default, so you don't need to
configure anything special. And also if you look at the
requirements, how to use this plugin. So the requirements are
very straightforward. Basically you need to have
at least a GitHub account. You can either use the GitHub free account
or GitHub Enterprise account as well. And then what you need is a Grafana
instance or a Grafana server. And as mentioned that you can use any
of the Grafana flavors such as OSS Enterprise or Cloud. To get started,
we will follow the guide defined here, that first we need to set up. Then we will take a look how we can
configure it and then create some sample dashboards. In order
to set up this plugin, we first need to install the GitHub
data source and on this page you will see a list of various methods
that how you can install a data source plugin. Personally for me, the most
easiest way is to use the Plugin catalog. So basically in this method, all you need to is to log in into the
Grafana UI as a server administrator or as a root account. So I am already logged-in in my
Grafana account and I will click on administration plugins and data plugins. And here I will type GitHub, Make sure that the state is set
to all so that when you type GitHub in the search
field, it does appear. Now we will click on it and
click add a new data source. Now the data source is added, but we need to configure the
GitHub personal access token. So the next step is to create
a personal access token. Github provides two types
of personal access token. The first one is known as fine
gained personal access token, and the second one is the
classic personal access token. In this example we will use that
classic personal access token. So all you need to is to log into
your GitHub account. So in my case, I am already logged
into my GitHub account. And after that you can click on this link, which will take you to the personal
access token settings for your account. As you can see here that I'm now
under Settings and Developer Settings, and here you can see that we have options
to use fine gain and Token Classic. So what we'll do, we will create a new token and we
will click on Generate new token as (classic). It'll ask you for some
information that such as the name, what is token for expiration and so on. I have already filled out
the requirements here, such as I give this name as a Grafana
demo. Expiration in this case is 30, but you can set it to either custom or
no expiration if you want to use it for a longer period and setting the scope. So basically here we need to
define some certain permissions. In order for the plugin to work correctly, you need to define the following
permissions which are defined here. So I have already fill it out. And you can also check here. And in case if you want to also
monitor some of your private repository, then you have to select repo
full control of the private repository. What it means is that you
have to check this, this one, and then you will have the
access to your private as well as it mentions here, but in
this case, we don't need one. Okay, and then we will click
on the Generate token link. Now this is my new GitHub token and make sure to copy it,
maybe save it to your, your favorite editor in this case, I'm just saving here
for now in our document, we need to use this token
in our data source plugin. So we will go back and here in the connection we will
paste this personal access token and click save test Hurra!! It's working. So data source is working
correctly, this is good news for us. And now we can start
creating some dashboards. So let's go to the dashboard
and create a new dashboard. Add visualization and select
the GitHub data source plugin. And here you can define, let's say we want to see the issues or the owner is Grafana in my case is
Grafana and the repository is also Grafana and we can set it
right now for the table panel. Okay. And now it is showing some
data, but we can use query labels. So basically let's say that we want
to view all the issues which are opened. So we will use the GitHub
label, which is known as is:open And set that time to in the last 30 days. And now you can see that we are viewing
all the issues which are currently open. They are not closed, the
close is set to false. Similarly, if we want to view
issues which are closed, then we can change from open to closed. And now you can see that it is
showing us all those issues which are closed in the GitHub. Okay. So this is really easy
and powerful to use. Now let's try to use a sample
dashboard where we can see more data and we have pre-configured
dashboard available by Grafana Labs. So if you go to the documentation and
click on create sample dashboards, it provides you some information that
how you can import an existing dashboard. There are several methods to import it. The one way is to go to the grafana.com/dashboards website
and import the dashboard with ID 1400 or the other way is to import
from the data source plugin as well. We will use the dashboard method. So we will click here and this will take
us to the Grafana dashboard website. And this is a pre-configured
dashboard available for the GitHub. And to use it, we will copy the ID, go to our dashboard, Click import, and then
paste here, load it. It'll give you the name as
GitHub default looks nice. Folder will be dashboard. And we need to select here the plugin. So the data source plugin is GitHub data
source. And now we will click import. Let's wait for a moment.
And now while it is loading, you can see that it is taking some
time because it fetching a lot of information. But now we have all
the stats here, some pull requests, issues and so on. Not every data might be visible here
because it can take time or depends on the configuration of your repo or the
query, what you are trying to query. But this is really powerful
because here you can select dashboard variables or the
templating for example, if I want to view the
organization for Grafana. But I want to check the Loki issues. Now it'll update, take a bit of time and now we can
see the status of the Loki repo as how many issues are opened,
how many pull request and so on. So this is really cool and I think
this helps a lot of developers who are working maybe as a DevOps engineer, SRE, even managers who are managing
teams for a complex project. So this makes a very good use case. Also, we have some sample dashboard available. So if you go here on the
documentation homepage and click on this link, it'll take you to
the Grafana play. Grafana play, basically a play area where you
can try out different things. And we have created some
sample dashboard here as well. So try it out and you can see once it loads that we have some example dashboard
which can give you some more ideas, how you can create your own dashboard, maybe copy this one and use it. And yeah, I hope that we enjoy this
video and learn a lot from it. Feel free to ask your
question in the comments. I leave all the useful links
in the video description, so please don't forget to check it out.
And I hope to see you in the next video. Till then, take care. Bye-Bye.

