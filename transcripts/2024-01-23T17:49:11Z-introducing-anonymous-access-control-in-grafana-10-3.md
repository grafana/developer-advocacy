# Introducing Anonymous Access Control in Grafana 10.3

Gain control over anonymous access in your Grafana instance with the new Anonymous Access feature. Tailored for both ...

Published on 2024-01-23T17:49:11Z

URL: https://www.youtube.com/watch?v=B72X3_9e-ds

Transcript: [Music] hey I'm Eric Lamark a software engineer for the identity and access team here at graphon Labs uh let's talk about Anonymous access that's available for 10.2.3 in OSS and Enterprise now we've seen that uh customers who enable Anonymous uh access to their instances have a hard time figuring out how much of this is being used so we have um a way of monitoring and viewing the anonymous axess to any of the grafana instances with this feature that's coming out now we Define a active device that is U accessing grafana without being logged in for the last 30 days this enables any of the the last devices that have been active at the grafana in now we've also a device limit so if you are in need of limiting the anonymous access for your graphon instance you have a way of setting the device limit Now setting the device limit to some number H enables you to configure this many devices is the maximum limit and any Anonymous access that is trying to access the instance Above This threshold will be denied access here is the regular users Tab and now if you have Anonymous access enabled you'll see this new tab which is anonymous devices we save for the devices and then we have a way of showing the total amount of the anonymous devices that have been active during the last 30 days in the stats page now go check out the docs on authentication to learn more and uh go check out the users tab uh with the anonymous device T thank you

