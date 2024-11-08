# Adding data sources to Grafana (Loki, Tempo, &amp; Mimir) | Grafana for Beginners Ep. 6

Want to add your data sources to Grafana but have no idea where to start? Join Senior Developer Advocate, Lisa Jung to learn ...

Published on 2024-01-25T10:54:21Z

URL: https://www.youtube.com/watch?v=cqHO0oYW6Ic

Transcript: Hey! Welcome to Grafana for Beginners. I'm 
Lisa Jung and I'm a Developer Advocate at   Grafana. For this series, we'll be using Grafana 
to observe logs, metrics, and traces data from a   microservices app. As a first step, we learned how 
to run Grafana in your own environment and also   on Grafana Cloud. Remember Grafana doesn't 
store data. That's why we'll be adding our   data source to Grafana as a next step. The data 
we'll be working with is stored in Loki, Tempo,   and Mimir. So this episode will specifically cover 
how to add these to Grafana. You may be working   with data sources outside of these three products. 
The good news is that Grafana comes with built-in   support for many other data sources you may be 
using. Depending on the data source, the process   of adding it to Grafana will vary. However, the 
core tasks we'll be completing in this video are   common to many data sources that can be added to 
Grafana. So it will give you a general idea of how   to get started. In this video, I'll show you how 
to search for the data source you want to connect,   then give the data source a descriptive name 
so you know exactly what data is in there,   then tell Grafana where it can find this data 
source and how it can access the data source.   Before you continue, make sure you have the URL 
of the data source you want to connect. If you   need authentication to access the data source, 
make sure to have the username, password, or an   API key handy. To wrap up, I'll show you how to 
save and test the connection to make sure things   are ready to go. All right, so some of you are 
working with the self-managed edition of Grafana,   while the rest of you are working with Grafana 
Cloud. So let's get all of you on the same page   so I can show you how to add the data source to 
Grafana. If you're following the episode that   shows how to download and run the self-managed 
editions of Grafana, we ended on the homepage of   Grafana on your local machine. The link to that 
episode is shown on the info card on the screen.   From the homepage, click on the "Add your first 
data source" card. You'll see a page where you   can search for the data source you want to add. 
If there's built-in support for your data source,   you'll see it here. If you don't see it, skip 
towards the end of the video where I talk about   installing plugins for your data source. After 
you install the plug-in, you can come back to   this video and follow the steps to connect your 
data source. Now, if you're following the episode   on setting up your Grafana Cloud account, we ended 
on the Get Started page. The link to that episode   is shown on the info card on the screen. From 
the Get Started page, click on the "I'm already   familiar with Grafana. Skip setup" option in the 
upper right corner of your page. On the next page,   click on the "Connect Data" button. Similar to 
the self-managed option, you'll see a page where   you could search for your data source. All right, 
we're now all on the same page. The UI between the   two options is very similar. To keep this brief, 
I'll show you the steps using Grafana Cloud. In   this series, we're assuming that you already have 
collected and stored your data in your data source   and that you're familiar with settings, admin 
information, and query language specific to   your data source. I have my data in Loki, Tempo, 
and Mimir so we'll be adding these to Grafana. The   steps to add Loki, Tempo, and Mimir are nearly 
identical so I'm only going to show you how to   add Loki to Grafana. You can repeat the exact 
steps for Tempo and Mimir. First, you're going   to search for Loki in the search bar. You'll see 
the results populate here. To add the data source,   go to the "Data source" section and click on the 
"Loki data source" option. Then click on the "Add   new data source" option. Next, you'll give a 
descriptive name to this data source connection   so you can easily tell what data could be found 
there. Then we're going to tell Grafana how it   can find this data source by entering its URL. 
Next, if your data source requires authentication,   you'll need to include that info. My Loki data 
source does require basic authentication so we'll   let Grafana know how to access it. So scroll 
down to the "Authentication" section. Then   expand the drop-down menu and select the "Basic 
authentication" option. Enter the username and   password. Then scroll down to the bottom of the 
page and click on the "Save and test" option. Once   the data source is successfully connected, it'll 
give you an option to visualize or query the data   and that means we're done! It's super simple! 
To add Tempo and Mimir, you'll repeat the same   steps. Click on the "Connections" option up top 
to go back to the search page. Search for the data   source you're looking for and follow the exact 
steps we went over. One thing to note is that when   adding Mimir, you'll search for Prometheus and use 
the URL and the authentication info used to access   the Mimir data source. Mimir is like an enterprise 
grade of Prometheus so we use a Prometheus plug-in   for that. Now those of you who cannot find the 
built-in support for your data source, you'll have   to install a plug-in before you can connect your 
data source to Grafana. To do so, click on the   menu icon in the upper left corner. From the drop- 
down menu, expand the "Administration" section.   Then expand the "Plugins and data" section. 
Click on "Plugins" and from there search for   the plugin for your data source. Once you install 
the plug-in, follow the same steps shown in this   video to connect your data source to Grafana. If 
you don't see the plug-in you need, then you can   develop a custom plug-in. Go to the link shown on 
the screen and this page will teach you how to do   that. Now that we have added the data sources we 
need, we're ready to explore our data and see what   we're working with. You'll see what I mean by that 
in the next episode. If you want to access more   episodes of the Grafana for Beginners series, go 
to the Grafana Community web page. This is where   all the community resources are shared. You can 
access the series by clicking on the "Grafana for   Beginners" card. Last but not least, as you learn 
more about Grafana, you'll have many questions   along the way. To ask questions, scroll down on 
the page and click on the "Forums" card. The Forum   is the best place to ask questions about Grafana. 
The Grafana team and the community members answer   questions on this platform. It contains a library 
of questions and answers organized by category.   So if you have a question, first check if it's 
already been answered there. If not, submit a   new question. All right, that's a wrap. Thank 
you for watching and I'll see you in the next episode

