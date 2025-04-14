# How to use constant variables in Grafana dashboards

In this video we'll look at constant variables. Constant variables let you add a value to a dashboard that can be changed by an ...

Published on 2025-04-11T13:42:03Z

URL: https://www.youtube.com/watch?v=0bpfstBJzgQ

Transcript: Have you ever been building a dashboard in Grafana and want to put a string or a value 
in a bunch of different panels only   to realize that that's inevitably going to change and it's going to be a real pain 
to have to update everything? I'm Ronald McCollam with the 
Grafana Labs Developer Advocacy team and I want to talk to you 
today about constant variables. Constant variables let you create a variable that 
can be used in multiple different dashboard panels but only need to be updated in one 
place when you want to make a change. Let's take a look! I'll start with a blank dashboard. I'll go to the dashboard settings, select the variables tab and add a new variable, select the constant variable type and I'll give the variable a name. This 
is how it will be referred to in queries. Now I could add a label, but because constants are   hidden on dashboards this value 
will never actually be displayed. Same with the description: it 
won't be shown on the dashboard. But it can be useful to provide more 
information to administrators and   dashboard editors about what your variable is for so I suggest filling this in. Finally I'll add the value for my variable. I'll go back to the dashboard and you'll see   that where variables normally 
appear, we don't see anything. That's because constants are hidden. So let's add a visualization and 
see how constants are actually used. I'll add a table visualization and 
let's use the Postgres data source. I'll add a query to select 
from the "employee" table. When I want to use the variable that I just 
created I'll start by typing a dollar sign ($). Note that in many cases, 
Grafana will give a pop-up   list of available variables 
but in this case it does not. So I'll just go ahead and type the variable 
name surrounded by braces and run the query. If I go back to the dashboard, I see five rows. Now, maybe we go to production and decide 
five isn't enough -- we want to limit the   number of rows returned by default 
but we need to see more than five. So I'll go back to the dashboard settings, 
open the variable, and change the value to 20. Now when I go back to the dashboard you'll 
see I have 20 rows returned from my query. And there you go! Next time you find yourself using the 
same value over and over again in a   Grafana dashboard, remember constant variables. They'll definitely make your life 
easier when you need to update things!

