# Managing users and Permissions in Grafana | Grafana for Beginners Ep 12

When using Grafana in a shared environment, managing users and permissions becomes necessary. Join Senior Developer ...

Published on 2024-04-17T14:56:41Z

URL: https://www.youtube.com/watch?v=59uCGJN5hPI

Transcript: Hey! Welcome to Grafana for Beginners. I'm Lisa 
Jung and I'm a developer advocate at Grafana. So   far, we operated Grafana as a single user. Down 
the road, we may want to have multiple people use   Grafana in a shared environment. In that case, 
managing users and permissions becomes necessary   and that is what we'll be learning about today. 
To start, log into the admin Grafana account.   If you're using Grafana Cloud, this would be the 
user account you initially created the account   with. If you're using the self-managed edition 
of Grafana, it'll be the default account called   admin. Regardless of where you're running Grafana, 
the steps of managing users and permissions are   very similar, except for the initial step of 
creating users. So we'll go over that first,  then I'll show you the rest of the steps using the 
Grafana Cloud interface. All right, let's go over   how to create users in Grafana Cloud. When you log 
into Grafana Cloud, you'll be taken to the Grafana   Cloud portal. From there, under the Org settings, 
click on "Members". From the members page,   click on the "Add member" button. Then enter the 
email of the member you want to invite, then you   can assign a role for this user. You'll see three 
options. The viewer gets to view all dashboards   but can't edit them. The editor can view and edit 
all dashboards but can't change data sources. The   admin can view and edit all dashboards, they could 
add remove and modify data sources, and they could   also add users and change user roles. There's 
no need to have a single admin account so feel   free to add multiple administrators as needed. For 
our example, we'll give this member a viewer role,   so click on that. Then click on the "Send invite" 
button. You'll see that there's a pending invite   for the member you just added. The invited member 
will receive an email. All they have to do is   click on the button to join the group, then choose 
a password. Click on the "Create my account"   button. Once they accept the invite, you will see 
an option to view their user profile and update   their role. You could change their role at any 
time by clicking on that option. You could also   remove a member by clicking on this icon here. In 
Grafana Cloud, users are managed in the Grafana   Cloud Portal. Permission settings for dashboards 
however are managed at the dashboard level. To   get to the dashboard, go to the Grafana instance 
where the dashboard is stored. In our case, our   Grafana instance is called Grafana for Beginners, 
so we'll click on that. When you launch Grafana,   it'll take you to the homepage of your Grafana 
instance. We just added a user to our Grafana   Cloud account. Let's go over how you can do the 
same in the self-managed edition of Grafana.   The steps to creating users in the self-managed 
edition are very similar, except that you start   from the homepage of your Grafana instance. 
When you log into the admin Grafana account,   you'll see the homepage. From there, click on 
the "Administration" option. From the dropdown,   click on the "Users and access" option, then 
click on the "Users" card. From the user's page,   click on the "New user" button. From there, 
type in the name email username and password   of the user you want to add. Then click on the 
"'Create user" button. On this page, you'll be   able to edit the user information or delete the 
user. To assign the role, go to the organization   section and click on the "Change role" option 
and select the role from the dropdown. Then click   on the "Save" button. With self-managed Grafana, 
there are two things you can do to invite a user.   If you want to send an email invite directly 
from Grafana, you can configure an email server   by making changes to Grafana configuration file. 
Or you could send the username and password to the   new user outside of the Grafana platform so they 
can log into your Grafana instance. All right, we   just went over how to manage users in both Grafana 
Cloud and self-managed edition. For both options,   we ended on the page of the Grafana instance. 
Next, we'll learn how to manage permissions.   From this point on, we'll go over the steps for 
Grafana Cloud only as the process for both options   is very similar. Before we get started, let's go 
over when you may want to manage permissions. So   far we have assigned roles to our users such 
as viewer, editor, and admin. Each role comes   with default permission that applies to all 
dashboards in the Grafana instance. This means   that if you're assigned the role of an editor, you 
can view and edit all dashboards in your Grafana   instance. Depending on your use case, the default 
permission may not work for you. For example,   you may have dashboards with sensitive information 
that should only be viewed by a select few or you   have teams that rely on particular dashboards. If 
someone were to accidentally make changes to the   wrong dashboard, it would impact the work of the 
team who depends on it. In situations like these,   you can manage permission at the dashboard level. 
Let's talk about the best practice for managing   permissions for dashboards. If you're working 
with a very small team and have a few dashboards,   adding permissions for individuals may be 
manageable. But let's say you're working with   multiple teams and several dashboards and you're 
managing permissions with individual users. The   chances are a user may change roles or leave 
the company at some point. When that happens,   you may have to check every dashboard to update 
the permission settings and we don't want to do   that. Instead, you can group users into teams and 
manage permissions with teams. So when changes   need to be made, you can update permissions 
in one place. So let's create a team. From   the page of your Grafana instance, expand the 
menu, then expand the "Administration" option,   then "Users and access", and click on 
"Teams". Click on the "New team" button,   then give your team a descriptive name. We've been 
monitoring on e-commerce app with a microservices   architecture. Let's pretend that we're creating 
a team of users who monitor the checkout service   dashboard. So we'll name the team as such. Now 
you have the option to assign a role for the team   and add email address to create an avatar for the 
team. We won't do that and we'll just create the   new team by clicking on this option. You'll see 
that the checkout service team has been added and   the admin was automatically added as a member. 
To add additional members, click on this option,   then click on the "Choose" drop-down menu 
and you'll select the "User" option. Then   you can type or use a drop- down menu to select 
the user. Select the member you want to add,   then you can give the user a member or 
admin status. We'll assign the member status   then click on the save button. Using the same 
page you can always edit the permission for   the team as needed. All right, we just added 
a member to the checkout service team. Next,   we'll manage permissions for the 
checkout service dashboard. To do so,   go to the menu, then click on "Dashboards", 
then select the "Checkout service" dashboard,   then click on "Settings". From the settings 
page, then click on the "Permissions" tab. Let's say we only want the admin and the checkout 
service team to be able to view and edit this   dashboard. To do so, we'll remove the default 
view and edit permission from the dashboard by   clicking on the "X" buttons here. We won't make 
any changes to the admin. Let's add the team as   authorized editors of this dashboard. To do 
so, click on the "Add a permission" button,   click on the "Choose" option. From the 
dropdown, choose the "Team" option,   then click on the "Select the team" dropdown 
to choose the team you want. Then assign the   role for the team for this specific dashboard by 
clicking on the drop-down menu. We'll give this   team the edit permission to the checkout dashboard 
and save it. So let's look at the dashboards page.   This is the page that would be presented to the 
checkout service team. The same page for non team   members however would not show the Checkout 
service dashboard on this page. All right,   in this series, we learned the fundamentals of 
getting started with Grafana. It's time to put   your knowledge to work by participating in the 
Grafana for Beginners challenge. You can apply   what you've learned from the series and create 
anything that would help others get started with   Grafana. This could be in the form of a blog, 
a video, a dashboard, or anything you could   think of as long as it can be shared with the 
community. Feel free to post your contribution   to your social channels and tag Grafana Labs. 
Each quarter, we will pick one winner who'll get   swag and a shout out on their contribution 
across Grafana social media platforms. For   more details about the challenge and to submit 
your creation, go to this link. The link is in   the info card up top. If you want to access more 
episodes of the Grafana for beginner series,   go to the Grafana community web page. This is 
where all the community resources are shared. You   can access the series by clicking on the Grafana 
for beginners card. Last but not least the Grafana   for beginners challenge isn't the only way you 
could contribute to the community. For example,   you can share your user story to inspire others. 
You can report bugs and suggest feedback on our   open- source projects. You can also participate 
in the Grafana Champions program to contribute   and get celebrated for your accomplishments. 
For more details, click on the cards under the   "Contribute and share" section. That's a wrap. 
Thank you for watching and I'll see you soon!

