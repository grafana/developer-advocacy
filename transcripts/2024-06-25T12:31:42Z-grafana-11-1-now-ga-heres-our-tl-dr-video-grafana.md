# Grafana 11.1 Now GA: Here&#39;s our TL;DR Video | Grafana

We are back! And ready to announce Grafana 11.1 this minor release still packs a punch with ease-of-use dashboard ...

Published on 2024-06-25T12:31:42Z

URL: https://www.youtube.com/watch?v=gjQX9-7Hsfs

Transcript: We are back and ready to announce Grafana 11.1. 
This minor release still packs a punch with some   ease of use dashboard improvements, further 
redesigns to Grafana's alerting and some   impactful changes to our overall accessibility of 
Grafana. Let's get straight into it. As always,   some great changes and features have been added to 
our dashboards and visualizations. Starting off,   we have a long standing feature request for the 
table visualization table cell text wrapping   when enabled will wrap the column with 
the longest text making convoluted and   long lines of text easier to read without 
needing to scroll across the screen or expand   the column size. You can also manually specify 
which column is wrapped using field overrides.   Sometimes less is more the standard behavior for 
percent change in the stat visualization is to   color positive percent changes green and negative 
percent changes red depending on your use case.   However, you might want to customize how percent 
change color is set. We've added the options to   have percent change color mode, inverted or match 
the same as the value. And I might have mentioned   this a little too early in the last TLDR, 
video X and Y chart is now officially GA.
  Moving on to alerting, there has been a 
whole host of updates and let's start with   my favorite. The settings page for alerting has 
been redesigned. The new settings page provides   you with a holistic view of where Grafana 
managed alert instances of forwarded decide   which alert managers receive alert instances 
for Grafana managed rules without navigating and   editing data sources. You can also manage version 
snapshots for the built-in alert manager, which   allows administrators to roll back unintentional 
changes in the alert manager configuration. We   have also added a visual diff that compares 
the historical snapshot with the latest   configuration to see which changes were made.
Next we have added alert template selector,   enabling you to easily choose which templates you 
want to use in your alert notification messages.   Select from existing templates or enter a custom 
one for your specific needs. We have also added   OAuth2 to any independently hosted alert managers 
or Mimir receivers through the contacts point   user interface. And you can now pause and resume 
alert rule evaluations directly from the alert   rules list and details view. There are so many 
quality of life updates to alerting to make sure   to check out the what's new page in the Grafana 
documentation. Last but certainly not least,   we are actively trying to improve the overall 
accessibility of Grafana for all. Starting off,   the Geomap panel can now be used with a keyboard. 
Try focusing the map area, moving around with the   arrow keys and zoom in and out. Using the plus and 
minus, we have panel shortcuts, which previously   only worked for, which have a panel you hovered 
over and now also takes into account the keyboard   focus. Simply tab to one of the visualizations 
and begin using the keyboard shortcut keys.
  Next up, the majority of screen reader users find 
things on a webpage using headings. Recently we've   been adding missing headings and correcting 
heading levels, most notably panel titles.   And lastly, reduced motion support. Users who 
are affected by lots of animations on a website   have the possibility to configure Grafana with 
reduced motion settings, making animation simpler   or removing them all together. And that's 
a wrap on Grafana 11.1. A massive thank you   to our community and Grafanistas developers 
for bringing all of these impactful changes   within a minor release. Make sure to check out our 
What's new page within the Grafana documentation   for the changes we didn't cover here. We 
will see you next time for Grafana 11.2.

