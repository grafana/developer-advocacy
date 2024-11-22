# Getting Started with Google Sheets Data Source Plugin - Visualize your Spreadsheets | Grafana

Learn step-by-step how to monitor and visualize your Google Spreadsheets data by using the Google Sheets Data source plugin ...

Published on 2024-11-21T09:00:48Z

URL: https://www.youtube.com/watch?v=hqeqeQFrtSA

Transcript: Hello everyone my name is Usman Ahmad and I 
work in Grafana Labs as a Senior Developer   Advocate and in this video we're going to learn 
how to use the Grafana Google Sheets data source   plugin so that you can visualize and monitor 
the data in your Google sheet or spreadsheet   in a Grafana dashboard so let's get started. 
So this is our Grafana Google sheet data source   plugin documentation page and it explain all 
the requirements how to get started and even   how to create a sample dashboard which will also 
create in this demo so let's take a look at the   requirements. So the basic requirement is that you 
should have a Google account you can create one   if you don't have and you need to have at least 
one of the Grafana flavors installed either you   can use this on Grafana OSS, Grafana Cloud or 
Grafana Enterprise and let's take a look how to   set it up so we will click here and first go into 
the installation. So there are multiple ways how   to install and use this Google sheet plugin the 
most easy way is to use the Grafana plugin catalog   basically you will install this directly from 
the Grafana web UI which we'll also use in this   demo but there are also other methods such as you 
can install this plugin by visiting the Grafana   plugins official page so if you click on this 
link you can see this page and it will explain   how to install and also see the related content or 
the documentation similarly you can install this   plugin from our GitHub repo where you can define 
which Grafana Google sheet plugin version you want   to use and install it manually. There is also a 
command line explanation if you are using Windows   as well. Lastly you can install this plugin using 
the Grafana CLI tool so those who are using Linux   or Mac can use this instruction how to install 
this plugin there's also instruction for Windows   user so you can install this as well and also 
you can install the custom version as well for   both Linux and Windows Operating System. Once 
you install it then you can go to authenticate   configure and provisioning. In our case let's take 
a look how we can install from the plugin catalog   so make sure that you have Grafana up and running 
and make sure also that you are using the latest   version of Grafana. Now click on the menu go on 
the administration then click on plugins and data   click plugins and search for Google Sheets click 
this and in my case I have already installed it   but I can show you how I can install one more 
so I will click on add a new data source and   I can name it as demo sheet plugin okay. Now it 
is installed the next step is to authenticate so   after you have installed the plugin successfully 
it is very important that you need to authenticate   it to your Google account or the Google service 
and for that we have this page which explain how   to authenticate it there are three different ways 
which you can use for authentication the first one   is the API key which allows you to create a Google 
API key in your Google account the second is using   the JWT token or the third one is checking the GCE 
service token. Make sure that you check this page   frequently because these instruction might changes 
or maybe some new feature added when it comes to   authentication. In this demo we are going to use 
the Google API key and in my case I have already   configured it so if I go back to the data sources 
you can see that I have multiple data sources   configured and the one which actually works and 
is ready to use is the Grafana Google Sheet data   source. Once you click it you can see the similar 
details which we just saw in the documentation so   there are multiple ways which you can authenticate 
currently there are three but could be more in   future the API key, JWT and GCE account. Since 
my API key is already configured so in case if   you want to use it just paste your API key here 
by following the instructions from here or from   the documentation and once done click save and 
test and you should see a success message. Now   it is time to create a dashboard so click on the 
home and click on dashboard and click here on   new new dashboard add visualization and select the 
correct data source in our case it is this one and   now let's go back to the documentation. So there 
is a documentation section how to use the query   editor as you can see in this screenshot that we 
need the spreadsheet ID and the range the range is   optional it can Auto detect itself but we do need 
the spreadsheet ID and we need to paste this ID in   the query editor there are further instructions 
given how to use the spreadsheet ID in this   documentation and how to get the cell range we 
will take a look by creating a demo dashboard   so that we can learn by using how to make use of 
all this information so since we are already here   now we will need to open this demo sheet in our 
browser okay and this is an average temperature   spreadsheet it contains a column for month and 
three columns for three different cities Stockholm   Berlin and Los Angeles, Now how to copy the spread 
sheet ID is that you need to copy this information   here till here okay this is your spreadsheet ID 
simply copy this and go in your dashboard and just   paste it and press enter we click Zoom to data and 
now you can see the data is arriving so basically   this is our spreadsheet ID and once it is valid we 
can see the details. Also what we can do is that   since this is a Time series data we can change 
it to the table format and and view in a table   tabular form but we can do other customization 
as well so we can use some sort of different   data maybe we can use the gauge panel and we 
see different option. We can even go further   more if we want to add for example threshold that 
anything above 10 is high okay and we can also add   any the base temperature is one we can add this 
in information and anything above 4 is green and   20 means it's hot just as an example so you can 
customize your data maybe it's a scientific data   maybe it's a calculation data maybe for some cost 
saving so there are many use cases where you can   use this plugin to view information in a dashboard 
we can now name this panel as weather data   click on Save Dashboard. We name it the dashboard 
itself as a demo dashboard and now we click save.   Now if we go in our dashboard folder we should 
again we have to click the safe dashboard that   is fine now we see this demo dashboard 
here and if we click it we can see this   information. We learn that the plugin is very 
powerful as it auto detect uh the range itself   and give us the appropriate data but what about 
if we need to select the specific range. So   let's create another dashboard and we click on 
a new visualization again select a data source   the correct one and this is our spreadsheet ID 
right we paste it here it will again give us   the temperature of all three cities but we need 
information only for Stockholm and Berlin so what   we will do is that we will press shift and select 
only the required columns and now we have this   range here so if we copy this and paste this range 
here it will refresh and now you see that there's   only two cities available in our dashboard graph 
or in the time series graph Stockholm and Berlin.   So this is another very powerful use case that 
you can filter data the data you need to view   or show to others and this plugin support this 
functionality. Now let's take a look in further   more in the documentation this is also explained 
a bit here as well lastly we have the Grafana Play   dashboard demos available. The Play platform 
allows you to play with our demo dashboard in   this case we have some dashboard available for 
the Google Sheet data source plug-in to view   them just click on this link and it will 
automatically take you to that dashboard this   is the weather spreadsheet data where you can view 
this information in more detail in more different   visualization panels. Feel free to try it out 
and also let us know if you like this video.   Feel free to ask your questions or suggestion in 
the comments we will be happy to help you out. I   hope you really like this video and I will see 
you in the next one till then take care bye-bye

