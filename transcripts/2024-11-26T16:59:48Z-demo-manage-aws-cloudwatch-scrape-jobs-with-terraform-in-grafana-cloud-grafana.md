# Demo: Manage AWS CloudWatch Scrape Jobs with Terraform in Grafana Cloud | Grafana

In this video, we showcase our latest feature: touchless management of AWS CloudWatch scrape jobs using Terraform. What ...

Published on 2024-11-26T16:59:48Z

URL: https://www.youtube.com/watch?v=EVEQBtm-SvU

Transcript: Hello, this is Tristan with the Cloud Provider
Observability Squad at Grafana Labs. And today I want to demo a new
functionality we just released that will allow you to touchlessly manage AWS
CloudWatch scrape jobs using Terraform. So for this demo, I pre-created an access policy in
my Grafana C loud organization, and this access policy
will allow me to manage access policies and stacks. And we're going to use this to actually
set up the stack and the access policy that will let us
manage the scrape jobs in Terraform. So everything in this demo will be
totally contained in Terraform except for this bootstrapping access policy. So moving on to the Terraform
itself, we have, you know, about 200 lines of code or so for this. The first part is, you know,
specifying the required providers. That's gonna be the Grafana provider,
at least version three dot 13.0. And there's also the AWS provider that
we're going to use to actually create the IM role and policy that will allow us to do service
to service between cloud and AWS. Moving on to the variables. You know, just for the
purposes of this demo, I'm going to supply
like the AWS profile and the access token that we
pre-created in the UI for this demo. I'll supply that,
you know, off screen. We're going to do everything in
prod-us-east-0 in Grafana Cloud. So this region slug can
be reused throughout. And there's also some
static data that's in our, that's covered in our documentation. This is the Grafana account id, this is the AWS account ID that we're
going to use in the service-to-service assume role policy. So first up we get a Grafana provider, which I've called stack, and that has the access token that
we pre-created in this initial step. And, we're creating the stack here and the
access policy and a token for the access policy. So we're creating a brand
new stack just for this demo. It's going to be of course in
the, the prod-us-east-0 region. And the access policy needs to have three scopes to be able to use the AWS CloudWatch integration. That's
gonna be integration management, read and write, and
reading stacks. So, uh, we have that scope to our stack
that we're creating here, and, uh, we're just creating a
token that doesn't expire, just so that we can plug
that into a later Grafana provider that we'll use to
actually manage the scrape job. Next up we have the AWS provider.
So for that we have the assume role policy that ties the account that you're deploying
this to Grafana Cloud. And then the actual policy
that gets put on the role that you're creating will give Grafana Cloud
permissions to read a couple different APIs that will a) let it read CloudWatch metrics data, but then b), also a number of metadata, you know, get APIs for different AWS
services that all allow us to retrieve resource metadata for your
various resources in the cloud so that we can, um, enrich your
metrics with useful data. I do include a time sleep
resource here, about 10 seconds, which we will tie between the AWS account data that gets
stored in Grafana Cloud. So this will have a time sleep of 10
seconds before this can actually get created, because there's some
time that's needed for global. Im propagation in AWS after
this resource gets these resources get deployed before they
will actually resolved correctly. Otherwise you might
get a 401 unauthorized, from AWS. So, moving on, we have a another Grafana
provider instance, and now we're supplying the access token that we created a little
bit earlier in Terraform. And we're also going to call
this cloud provider API with the region slug that we're
using for the stack. So prod-us-east-0 is
where the stack lives. So we're gonna call the cloud
provider API in prod-us-east-0. And then finally for the scrape
job itself, we need two pieces. The first piece is the resource
called Grafana Cloud Provider AWS account. And that's
basically going to store the AWS IAM information in one place. And when you create this
resource or update it, it'll also validate that your assumed
role policy works correctly especially for the, you know, that, that everything checks out
permissions-wise for the
regions that you specify. And also by default when
you create a scrape job, this set of regions will
be used for scraping the resource, you know, the AWS account resource can be
reused across multiple scrape jobs. So you only need to define
this information once here. Moving on to the scrape job
itself, uh, we just, you know, we're giving it a name. We're tying the resource Id like the ID that
gets generated for this resource. We're tying it into the scrape job here. And then we're defining
a number of services. So, here I specified EC2, just a couple typical
metrics like CP utilization, and a status check metric. And I'm also gonna add an EPS
cluster nametag to the metrics for enriching the metrics
with some useful data. And we also have RDS CP utilization, you know, just checking
out a couple statistics there. And then finally, I also
included a, you know, we also support custom namespaces. So here I'm using the
CoolApp custom namespace, and I have just kind
of a generic, you know, KPIs metric that, uh, we have some randomly generated data
for that that we'll see in just a couple minutes. So, all right, so
now we're in the terminal. And you can see I got a Terraform
apply loaded here with a tfrs file that I created to fill in those
two variables we covered in the coder review. So running that, we've got
eight different resources here. We've got the AWS IAM policy is for service
to service. We got the role, the policy to attach to the role for
allowing Grafana Cloud to read these different APIs. We've got the Grafana Cloud access
policy and the token so that we can have the Terraform
provider manage scrape jobs. And we've got the actual AWS
account in scrape job itself, you know, with all the different services,
custom namespace, stuff defined here. So let's go ahead and run it. Going to hit yes and hopefully it
doesn't take too long to create. All right, so everything's
created there for the most part. We just got the ten second sleep we're
waiting for so that the IAM role can propagate and that's all done. So yeah, now the scrape job and the
accounts created pretty quick. Now we're just going to wait for a little
while for some scrape job runs to go through. And then we will switch over to the
Grafana Cloud UI and show off the data. So now we're back on the
Grafana Cloud portal, and you can see now that we got the stack
that we created in Terraform showing up here. So I'm going to
go ahead and launch it. And that's going to pull up
and we're on the home page. We're going to go to cloud provider
AWS and you can see that the scrape job has been created all
three of the services, including the custom
namespace that we have here. So I'm gonna go ahead and open up some
Explore views. Like one, for example is, uh, EC2. You can see that the tag that we added
to the metric definition shows up here. We can use it in PromQL for filtering. And we have all of these nice metrics
showing up now, including, you know, CP utilization average for
this particular instance. And the status_check_failed
metric as well. We also got similarly tags showing up for RDS, like we got a couple different
CPU utilization metrics showing up for RDS, one for the average
and one for the maximum. And last but not least, we got the CoolApp metrics showing
up with all of their glorious KPIs data . We got the maximum and the sum
aggregations showing up here. So, yeah, you know, basically just goes to show
that the Terraform configuration worked out. Everything was almost
entirely touchless except for that one bootstrapping access token
that we created. And, yeah, now we can go ahead and create
many different AWS accounts, tie them to many different scrape jobs, and even templatize some of the scrape
job data to reuse across multiple scrape jobs. So, hope you get some value out
of this and hope you enjoyed this demo.

