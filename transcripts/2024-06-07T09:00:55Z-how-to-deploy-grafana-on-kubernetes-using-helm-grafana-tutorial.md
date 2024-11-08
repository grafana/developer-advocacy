# How to Deploy Grafana on Kubernetes Using Helm | Grafana | Tutorial

How to deploy Grafana on Kubernetes using Helm Charts, customize the default configurations from values.yaml and also debug ...

Published on 2024-06-07T09:00:55Z

URL: https://www.youtube.com/watch?v=sgYrEleW24E

Transcript: Hello everyone. My name is Usman Ahmad and I work in
Grafana Labs as a Senior Developer Advocate. In this video, I'm gonna teach you how to
install Grafana using Helm chart. It'll be a complete step-by-step
introduction so that you can install, configure, and deploy it easily on
Kubernetes. So let's get started. So we have a complete
helm charts documentation, and you can find it easily
by going to grafana.com. And click go to the docs. And here you will click on Grafana. On the left side you will
find the link set up. So if you click it should
give you the option to install Grafana, expand it. And there you will
find the link Grafana on Helm Charts. A quick introduction about Helm. Helm
is basically an open source tool, which helps you to deploy
applications on Kubernetes easily. The traditional way is
to deploy via YAML files, but you can automate it or make it easier
by using this helm chart templates. And we will now take a look
into it. Before you begin, please make sure that you have a
Kubernetes cluster up and running on your machine. And also you need to
download the Helm tool itself. You can find the link here, which
will take you to the official page. So let's get started. The first thing we will do is that
we will create a Grafana repo. And by doing that, we need to first add
add the repo in our Kubernetes cluster. So the very first thing, we
will add the Grafana repository. So this is important so that we can
download the Grafana packages in our Kubernetes cluster. So what I
will do is that copy this command, and I'm already on my terminal
and I will just paste it. And now Grafana repo is added
and you can verify it by using helm repo list command, and it'll give you the information
that yes Grafana repo is there. You'll also need to update
it. So helm repo update, and now our repository is
up to date and ready for installation. Now the next thing we are gonna do
is to create a Kubernetes namespace. What it'll do, it'll create a separate area for our Grafana Helm chart so
that if we are using the default namespace, maybe there might be a
conflict with ports or settings. So using a different namespace
will give us isolation, and still we can do our deployment
easily. So in order to create a namespace, you will just copy this command
kubectl create namespace, and I'm giving this name as monitoring. So like that. And now
the namespace is created. The next step will be is to
search for the Grafana repos. So you can search for
Grafana repo using this. Command, which will give you
a list of Grafana repository. So we are interested in
installing the Grafana repo. And in order to do that we will
use the helm install command. And we are telling basically
that hel install my Grafana. This is our logical
name, right? And Grafana, Grafana is the repository and
the namespace is monitoring. So we'll just paste it here. And now Grafana is available
on our Kubernetes cluster. It also give us some information. For
example the name is my-grafana, that is, the name we give to our deployment
this is the last deployed timestamp, the namespace and so on. What important here is
that we need to get the Grafana admin password. And to do
that we have to run this command. So basically just copy this
whole command, copy it, and then paste it. And this will
give you the password. So for now, I will just copy it and I
will just save in a Word file. The next step is to
access the Grafana server. And to do that we have
to run the, this command. This is all instructions given
by the helm chart itself, so it's not something different.
And you will also get it, so you just copy it and
now run the second command. What this command is telling us is
that we are telling that that using the kubectl to port forward, the
Grafana port on the port 3000. And what it'll do that it'll start port
forwarding. So if I go on my browser, I will be able to log into Grafana. Now, in order to log in, you can
type the admin as the user, but for the password, you need
to copy paste the password, which which was provided
in the instructions. So you copy it and paste here. And now we are log into
our Grafana server. Now Grafana is up and running, but there are few things which we
need to make sure before we before we can say that that Grafana is running
correctly and we need to customize its configuration. And to do that, we
have to use the value stored ML file. Basically, when you install a
Grafana or any other application, you using helm charts and
use the helm command it, it is a bundle of package which
contains the default configuration. And in order to modify
this default configuration, you have to use the values.yaml file. The values.yaml file basically contains
all the configuration details of a particular application in
our case such as Grafana. And you can read more about
values.yaml file from the Helm official link using this one. And in our case, we need to download the values.yaml file. So I have already downloaded
this file and let me show you. So this is how a
values.yaml file look like. So basically it's sit as a collection
of all the Grafana configuration and we can modify it. So the first thing which we need to
make sure is to enable the persistent storage. So right now
the PVC is not enabled. So what it means that if we try to
create a Dashboard or configure a Data source, it'll not be saved because
there is no volume defined. And let me show you what it means
that if I go in this file and I search for persistence, so you can see that the type is PVC,
but it is not enabled by default. It is set to false and we need to enable
it. So what I will do is that I will I will set it to true. And now after that we need to run the helm upgrade command. So helm
upgrade my-grafana, the repo name, then pointing to the file -f
values.yaml and then to the namespace monitoring. And even just before that we can also
verify that PVC is does not exist. So how you can do that. So kubectl get pvc -n monitoring. So currently it says no resource
found in monitoring namespace. Now, if we run this command, because we have already the file
values.yaml configured and set it to true for PVC, it'll take a moment. And now it says that it is deployed. But what we are interested is to see
that if the PVC is now available, so if we run the same PVC
command using kubectl, now we will see that that it
is the name of our deployment. my-grafana status is right now pending, but we will see shortly
that it is populated. And now that means we can
save our Dashboard and Data sources and other data work
wherever we create in Grafana. So now if we take a look again, now the volume is populated that
it has a volume PVC with a number. The capacity is 10 GB. And with read, write ReadWriteOnce as the access mode, and you can do same for plugins. If you want to install you can go to the
plugin section in the values.yaml file. And for example. If you want to install a
Grafana Clock panel or Zabbix plugin you can do that here as well. For the troubleshooting it is
important to get the logs if you run into issues. And to do that,
you can simply run this command. So what it'll do is that
let me clear my screen. If I run this command, I will get the complete log
files of my Grafana deployment. And this can be useful if if
need for troubleshooting or, or creating an issue for
a bug or, or problem. Similarly, you can increase the log level, so the default level of
Grafana is the info mode, but maybe you need to
enable to debug mode. And to do that you can simply
again edit the values.yaml files. So let's find instructions. So we will first clear
the screen and go to the values.yaml file, and we will search
for the string grafana.ini Okay, so here we find the grafana.ini, and then we will go to
the log mode console, and here we can add the part as level: debug and then save our configuration. And now if we want to
apply this configuration, we will again use the heml upgrade
command, copy it, paste it here, and now if we try to look our
log file using the kubectl logs command, we will see
the log level in debug mode. So let me show you. Yeah, so the level is debug mode now and
it shows more detailed logs and this is helpful if you want to
troubleshoot issues. So that's all. Thank you very much. I hope you'll learn a lot from this
session and see you in the next video. Take care. Bye.

