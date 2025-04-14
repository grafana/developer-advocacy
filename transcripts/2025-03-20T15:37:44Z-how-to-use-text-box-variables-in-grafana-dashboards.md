# How to use text box variables in Grafana dashboards

Text box variables let users type whatever they want -- great for text filtering and searching! In this video we'll look at how to use ...

Published on 2025-03-20T15:37:44Z

URL: https://www.youtube.com/watch?v=F-On1KkRzAc

Transcript: Hello! I'm Ronald McCollam from the 
Grafana Labs Developer Advocacy team. Today I'm going to walk through setting up a text   box variable on a dashboard 
and using it in a query. Text box variables let viewers 
of your dashboard enter whatever   they like, usually for filtering or 
searching through large data sets. Let's get started! I'll start with a new dashboard. I'll go to the dashboard settings 
and then select the variables tab. I'll then add a new dashboard variable and 
set the type of the variable to be "text box". I'll give it a memorable 
name, in this case "city",   and I can add something friendly 
to show next to it on the dashboard and optionally some descriptive help 
text to let people know what it does. If I want, I can give it a default value as well. And when I go back to my dashboard, I can 
see my variable and the value I input. Now that I've added the 
variable, let's see it an action. I'll add a text panel to start. When I want to use the variable,   I start by typing a dollar sign ($) and 
then pick my variable from the list. Now you can see its value in the text panel. Let's see how this looks in a query. This time I'll add a table panel 
and I'll use the MySQL data source. I'll write my query, and as soon as I hit the   equal sign (=) Grafana will pop up 
that picker for the variable again. I'll need to put quotes around this value because   that's required by SQL and 
I'm querying a database. Now when I change the value and hit 
enter or click outside of the text box, the variable is updated and my query 
gets rerun with the new variable value. And there you have it: a great way to let 
viewers filter through large data sets. I hope you'll find this useful in your dashboards!

