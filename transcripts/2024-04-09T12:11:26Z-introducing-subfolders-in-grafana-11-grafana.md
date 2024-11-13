# Introducing Subfolders in Grafana 11 | Grafana

With Grafana 11, we're excited to introduce a highly requested feature — subfolders! Stay organized with subfolders or create ...

Published on 2024-04-09T12:11:26Z

URL: https://www.youtube.com/watch?v=R9mehA0EssU

Transcript: Hi everyone. Let's talk about Subfolders. I'm Amy Super and I'm a principal product
designer on the Frontend Platform team at Grafana Labs. What problem does
Subfolders solve? Well, first of all, you've been requesting subfolders
for dashboards since 2017. I know. I know. Some of you want subfolders
in order to keep things tidier, it's easy for dashboard
sprawl to get out of control, and setting up folders in a
nested hierarchy helps with that. Others of you want subfolders in order
to create nested layers of permissions where teams have access at different
levels that reflect their organization's hierarchy. We are thrilled to announce that after
a period of time when some of you opted in to try our preview version,
subfolders are now generally available. How does it work? Let me
show you. In the past, maybe you used dashboard names with
slashes in 'em to create hierarchy. In this environment, you can see that I've set up a series
of dashboards and folders with that same hierarchy. No more slashes
are needed in dashboard names. If I wanna move one of these dashboards, I'm able to select a folder within
the folder tree as its destination. You'll notice that there is no general
folder in the dashboard hierarchy. This change was made
available in the past, but as part of our subfolder project, any dashboards that were in the general
folder have now moved to the folder tree route. If that bothers you, you can simply bulk select
those dashboards and move
them to a folder of your choosing. I mentioned earlier that permissions are
a very important part of this feature. As you can see, I can set permissions
on any of these folders. In this case, I have a user set up in the system. I only want her to be able to view the
compute resources folder. As you can see, I can set her to be a viewer only on this
folder and its contents when she logs in because she cannot see the
parent folders in the hierarchy, her viewable folder displays in this
special "Shared with me" section of the folder tree. We are very excited to bring this long
awaited functionality to our community of users and customers. An absolutely huge thank you to everyone
who tested our preview version and provided us with valuable feedback. Check out the Grafana documentation
to learn more and try sub folders for yourself.

