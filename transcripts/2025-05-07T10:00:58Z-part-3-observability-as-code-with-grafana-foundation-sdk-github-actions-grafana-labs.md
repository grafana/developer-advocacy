# Part 3: Observability as Code with Grafana Foundation SDK | GitHub Actions | Grafana Labs

This tutorial shows how to deploy Grafana dashboards using GitHub Actions and the Foundation SDK. Push changes to your repo ...

Published on 2025-05-07T10:00:58Z

URL: https://www.youtube.com/watch?v=cFnO8kVOaAI

Transcript: Hi, I'm Tom, one of the senior developer advocates
here at Grafana Labs and in this video I'm going to be showing you how you can use
GitHub actions to automatically deploy your dashboard, changes from the dashboards you've
created using the Foundation SDK. So to get started, let's open up the Intro to Foundation
SDK repository in VS code and you can see that there is a GitHub actions
example folder within this repository. If we open up the main.go file, you can see that what we're doing here
is creating a very simple dashboard with a stat panel as well as a time series
panel in a very similar fashion to the way we did in the previous two videos.
If you haven't seen those yet, I'll leave links to those
in the description below. Once we've created that dashboard, we
are then outputting this as a file, so we're serializing the JSON for the
dashboard and then outputting this as sample dashboard.json.
 to the file system. One thing to note here
is that for this example, we're going to be using the new
Grafana CTL/CLI tool and that requires dashboards to be wrapped in
a Kubernetes style wrapper. So you can see here I've created
this wrapper structure here. It's got an API version. This
is the dashboard.grafana.app, API that we'll be interacting
with via the Grafana CTL tool. We specify the kind here, so this is a dashboard resource that
we're going to be producing and then we're going to give it a piece of metadata here
and we're going to specify the name is my dashboard, and then for the spec we'll pass in
the whole dashboard object that's been generated by the Foundation
SDK. Once that's run, we're going to end up with a sample
dashboard.json file on our file system there. So now let's go over to our GitHub action.
You can see up here in the top I have a .github folder with a workflows folder, and then underneath that there
is a deploy_dashboard.yaml file. Inside this deploy_dashboard.yaml file,
we're going to do a couple of things. We're going to make sure that this runs
every time we push to either the main branch or the Tom GitHub actions branch. That's just because I'm working from
a branch for this particular video. We can see that this job is running on a
Ubuntu and then we've got the steps for the actual action here. So what's
going to happen once this action runs? So first of all, we're going to check
out the whole code for this repository. Then we're going to make sure we have
the appropriate version of go installed for the action. So we're going to choose 1.2 4.2
for this particular demo. We're next going to verify that the go version
is correct and then we're going to download and extract the Grafana CTL tool. You can find this on GitHub
at grafana/grafanactl. And what we're going to do is we're
going to take one of the release versions here and we're going to
download that using Curl. We're then going to extract it, we're going to give it the
appropriate permissions, and then we're going to move it into
the user/local/bin folder so that we can execute it in the next step. One thing to note here is
that for this download URL, we are passing in a variable here for
the Grafana CTL version we want to use, and this just means that we don't have
to modify the GitHub action file itself, whenever we want to use a new version
of the Grafana CTL tool. We can just go into our GitHub settings and we
can change that variable there. So after we've downloaded
and extracted the tool, we're going to generate
the dashboard.json, by moving into the GitHub
actions example folder, and then running go run main.go.
That's going to execute that go script, which is then going to produce that
sample dashboard.json file on the file system. The next final step here is to deploy
the dashboard with the Grafana CTL tool. We're going to make sure we've got a few
environment variables configured here that the Grafana CTL tool is going to
pick up. So the first is a Grafana server, so that's the URL of the server that
we want to deploy the dashboard to. In this instance I'm using Grafana Cloud, so I'm going to give it
my Grafana Cloud URL. Then we need the Grafana stack id. Now
if you are using Grafana open source or Grafana Enterprise and not Grafana Cloud, instead of passing the
Grafana stack ID here, you can pass in the grafana org ID
and you'll be able to pass in the organization ID in your
specific Grafana instance. Next is the Grafana token. You can
create this within Grafana itself. I'll show you how to do this in a second, but you essentially create a service
account and generate an API token for that that you can then pass to GitHub in the
settings of your repository and that will allow the tool to deploy the
dashboard to Grafana instance. The next thing we're doing here is we're
essentially checking whether or not the sample dashboard.json file
exists, and if it does, we're going to use the Grafana CTL
tool to push that to our instance. So the command here is very simple, Grafana CTL resources push dashboards, and then we give it a path
to the dashboard file that
we want to deploy in this case sample dashboard.json, if the
file doesn't exist for whatever reason, we're just going to echo that out so
that we can see that there's an issue. And then finally the last thing here is
we're making sure that we're running all of this within the GitHub actions
example folder within the action itself. So let's head on over to our
Grafana instance here and
just make sure we can see how to get the Grafana token. So if I head over to my browser
and I'll pop open my Grafana instance here on the left-hand side, if you come down to administration
users and access and click on service accounts, you'll be able to create a brand new
service account here for your GitHub action. You can see I've already created
one at the bottom here, GitHub actions, it's an admin enroll, which is important to make sure it has
permissions to push dashboards to your instance. You can obviously give it
finer grain permissions if necessary. I've just gone with admin here
for demonstration purposes. I'll click the GitHub
actions service account here, and you can see that I have a few
service account tokens generated. If you to create a new one, you can simply press the add
service account token here, give it an expiration
date and press generate, and that will give you a one-time copyable
token that you can paste into GitHub, and I'll show you where to do that now.
So if we head over to our GitHub repository and go into
the settings section here, and then we come down to our secrets
and variables and choose actions because this is going to be the secrets and
variables we use in for our GitHub action itself. Within the secret section, you can see I've got a
Grafana token secret here, and this is where I would paste in that
copyable token that we've just generated from the service accounts page.
Then underneath the variables tab, I have a few different things here.
I have the Grafana CTL version. For this particular version
we're going to be using 0.0.5. I then have the Grafana server variable. This is going to point to
my Grafana Cloud instance, in which case it is devrel.grafana.net, and then there's the Grafana stack id, and you can find this within your Grafana
cloud configuration settings page, or alternatively, if you're
using open source or enterprise, you would pass in the grafana org ID
and make sure you pass the appropriate organization ID into that variable itself.
Okay, so let's open up our Grafana instance
here and let's go to the dashboard section. And you can see right now that I've got
a few dashboards that come by default, I've got a couple of extra
ones here that I've created, but I haven't got any that have been
generated from the Foundation SDK. So what I'm going to do is I'm going to
come back to my VS code instance here and we're going to open
up the main go file. Let's scroll up and you can see again
we've got a simple dashboard with a stat panel and a time series panel. What I'm going to do is I'm going to
push this code to my repository and that should trigger the GitHub action. So I'm
just going to make a small change here. I'm going to do commit, and
I'm going to say testing, and I'm going to push this
to my repository so you can see that's pushed. And if I head
over to my GitHub here and go to the actions section, you'll see that
I have this workflow running here. So if I click onto this and
go into the deploy section, you can see that it's running through
each of those steps that we configured within our action. Currently
it's on the Generate dashboard. You can see here that it's just
output all of that dashboard there. Now it's deployed it with
the Grafana CTL tool. The response here you can see is that one
resource has been pushed and then it's running its post setup steps. So let's fire on over to our Grafana
instance and let's refresh this page. And you can see now that we have a new
dashboard here. It's called My Dashboard, and you can see that it's got some tags.
It was generated by the Foundation SDK, it's got a generated tag and it's also
got a GitHub actions tag here. Let's open this up and you can see that our stat
panel and our random time series panel are there. Let's not a simple change to our code
and push that change up to the repository and see how that will be automatically
deployed to our Grafana instance. If we come over to our VS code
instance here, let's add a new tag. We're going to pull this one test, and then let's change the
title of this here to edited. We'll save this, we'll create
a commit so edited dashboard, and we'll now push that up
to our repository. Again, we'll come over to our
GitHub instance here, and we'll go back to our
GitHub actions workflows. You can see we've got our edited
dashboard. Let's go to the deploy section, and you can see again it is running
through all of those workflow steps there. So we're currently extracting Grafana CTL.
We're now generating the dashboard.json. That's then going to generate that
output and the file on the GitHub actions file system. We're then deploying that
with Grafana CTL. You can see again, one resource has been pushed
and now we're doing the cleanup. So let's come back into
a Grafana dashboard. Let's just go to the dashboard
section and refresh this page. And you can see now that we have that
new test tag on our My Dashboard, we'll open up the dashboard and you
can see that the title of this is now version edited. Hopefully that shows you how quick and
easy it is to set up a GitHub action to automatically deploy your
generated dashboards to Grafana. You can find all the source code to
this project in our GitHub repository. I'll leave a link down
in the description below. If you found this video useful
or you have any questions, please don't hesitate to ask
them in the comments below, and we'll be sure to try and help.
Thank you so much for watching, and I'll see you in the next one.

