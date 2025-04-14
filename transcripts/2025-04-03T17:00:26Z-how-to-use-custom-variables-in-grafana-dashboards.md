# How to use custom variables in Grafana dashboards

Custom variables let you define your own options for dashboard viewers to select. They're a way to fine-tune how your dashboard ...

Published on 2025-04-03T17:00:26Z

URL: https://www.youtube.com/watch?v=WV_DFh-k-Oo

Transcript: Do you make great dashboards with 
Grafana but sometimes wish you could   offer your viewers a few more options 
for customizing what they're looking at? I'm Ronald McCollam with the 
Grafana Labs Developer Advocacy team and today I'm going to be 
looking at custom variables. Custom variables let you provide a 
limited set of options for viewers   to pick from to modify queries in your dashboard. Let's take a look at how they work. I'll start with a blank dashboard. I'll open the dashboard settings, select 
the variables tab, and add a new variable. In this case I want to create my own variable 
values so I'll select the custom variable type. Give it a name, in this case "color",   and a label to display friendlier 
text next to it on the dashboard and optionally some descriptive 
text about what the variable does. Now to add the values the themselves 
I'll type my values separated by commas. Let's use "red", "green", and "blue". If I go back to my dashboard I see my variable 
label and the values "red", "green", and "blue". Let's see how this is used in a visualization. I'll add a text panel where 
I'll use HTML to display text. I'll have everyone check out my colorful text   so I'll start that and add an 
HTML style to color the words. When I want to use the variable I'll 
start by typing a dollar sign ($). Grafana will pop up a menu of available variables   where I'll choose my "color" 
variable that I just defined and now I'll finish off the rest of my HTML text. When I go back to my dashboard, you can 
see that as I change the value of the   variable it's updated inside the HTML tag 
that I wrote and the text color changes. Now what if I wanted to add something 
more custom that wasn't predefined? I'll go back to the dashboard settings 
and open up my color variable. I'll add a new value that I'll call "light violet" 
and in this case I'll add an HTML color code. What you'll see is that I have the variable key 
first (which shows up in my preview list below). I then have a colon (:) that 
separates that from the value. The value is what I want to be passed in for the   variable when it's used in 
a query or a visualization. So I'll go back to the dashboard and you 
can see I now have a "light violet" option. When I select it the HTML color 
value is updated in my text. The key part of the variable 
has nothing to do with the   value -- it's only what's shown in the dropdown. To show what I mean I'll go back to 
the variable definition and I can   change this "light violet" 
key to be anything I want. Let's use "hello". When I go back to the dashboard I 
now see "hello" in the dropdown but   the actual value of the variable hasn't changed; the value that is passed through 
is still that HTML color code. Custom variables are a great 
way to provide a limited set   of options to viewers of your dashboard 
to customize what they're looking at. I hope you find this useful!

