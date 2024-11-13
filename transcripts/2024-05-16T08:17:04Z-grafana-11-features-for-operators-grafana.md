# Grafana 11 Features for Operators | Grafana

Grafana 11 is now GA! In this video, we do a deep dive exploring all of the new features for our operators. In this video, learn more ...

Published on 2024-05-16T08:17:04Z

URL: https://www.youtube.com/watch?v=-C9C7VfFPHg

Transcript: Welcome to Grafana 11 for
the operators. In this video, we'll deep dive into all of the new
features which are important for those who maintain Grafana instances for everyone
else. Grafana users and developers, don't panic. There are dedicated
videos for you as well. Let's jump straight into one of the most
important new features for operators - Subfolders. Subfolders have arrived just
in time for that spring clean. Many of you requested subfolders to
maintain cleaner dashboard groups as it's easy for dashboards to become
cluttered and organizing them into nested folder structures removes the need
to implement your own path within the dashboard name. Others are eager to use subfolders
to implement layered permissions, enabling teams to access information
at levels that match their roles within their organization hierarchy. Let's quickly run through
creating a sub folder. Within the dashboard panel, I have a parent folder
called Grafana 11.0. If we open this folder, we can see
that I have a nested folder called, "For the developers." Let's
create a new nested folder and move our Grafana 11 dashboard into it. First click on the Grafana 11.0 folder, then select the button "new" and
select "new folder." This will create a new folder and we will
name it for the operators. Finally, let's jump back up one layer
and move our dashboard into this folder. Check mark the Grafana 11
dashboard, select "move, use the dropdown bar to find our sub
folder and press "move." And there you have it. We are excited to introduce this highly
anticipated feature to our Grafana community. Time to organize those
dashboards and celebrate cleaner, more structured dashboard management. You can now configure the Azure Monitor
data source to authenticate as the logged in Grafana user when making
query and resource requests. If you also use Azure Entra to
sign your users into Grafana. Current user authentication allows you
to enforce Azure RBAC restrictions on your Grafana users by removing the need
to provide broad service credentials. Once a data source is configured
with current user authentication, a user will only have access to
resources they have access to directly in Azure. Data sources configured to use current
user authentication are also less likely to be impacted by throttling issues
due to the individual level of access. A quick note from our development team. Current user authentication does not
inherently support backend features such as alerting. To account for this, data sources configured with current user
authentication can optionally specify service credentials that will be utilized
for backends features when no signed in user is available. Last but not least,
for our cloud and enterprise users, team LBAC! It's hard for teams to collaborate on
dashboards because they have to use different data sources. Grafana instances become cluttered and
confusing with hundreds of data sources each allocated to different teams to
ensure data integrity and security. Essentially, I only want my team seeing the data
that they have permission to access. Team LBAC or label based access
control is our first step towards seamless management of Grafana
teams access for Loki logs. Each team views the same data
source filtered by their teams label permissions. Teams can view queries to the same
data source with different LBAC rules applied, which are all configurable
via API and the Grafana UI. Simplified LBAC notation is automatically
converted into correct custom headers when making requests to Loki. Here is another tip from our developers. We recommend you only add query
permissions for teams that will have LBAC rules and remove default view
and editor query permissions. As an initial setup, we recommend defining as few
rules as possible for each team. Make sure that they are additive
rather than negating one another. For validating rules, we recommend testing each
rule in the Loki explore view. This allows you to see the logs that
would be returned for a specific rule. And that's it for our Grafana
operators walkthrough. We hope these features will help to
improve your experience within Grafana as you scale for production. Make sure to check out our Grafana 11
for the users and developer videos for more great features in
Grafana 11. Once again, a massive thank you to our Grafanista
developers and our community for making Grafana 11 possible.

