# Infinity (Plugin) and Beyond: The Future of Grafana&#39;s Data Source Ecosystem | GrafanaCON 2024

In the first 10 years of the Grafana project, the plugin ecosystem has grown to support more than 100 data sources.

Published on 2024-04-25T23:22:50Z

URL: https://www.youtube.com/watch?v=wI3U1NbTqt8

Transcript: [Music] hello everyone I'm Andre and today we're going to talk to you about infinity and beyond it's about uh data sources ecosystem at grafana about the past present and the future let's get started so grafana is a unique open source software that allows you to integrate uh data from varas hundreds data sources and systems into one single pane of glass and we call this grafana big 10 philosophy and the best part of it is that you can uh connect to your data and visualize it in grafana without actually moving your data to grafana and in the course of lifetime of grafana in 11 years together with Community we created uh around 150 data sources and recently weed data sources like looker sumic P Duty Dy serial DB as Mitch mentioned yesterday a lot of DBS to our catalog and more plugins are in development and even more are in the pipeline okay this 150 data source plugins is just not another feature just not a fancy number but it's entire grafana data sources journey and observability journey so over this uh 10 11 years uh we develop new plugins we learned a lot we failed several times we learned we corrected our mistakes and we never hesitated hesitated to change things yeah let's take a look at what has changed over time so grafana initially was created as a fork of kibana to visualize the data from graphite and later on we started to add more and more data sources and in the early days of grafana as you can see all our data sources we were able to fit them in this small drop down and now if you go to grafana and create a new data source you will see this ever growing like huge long list of data sources okay so not only we scaled number of plugins but we also adding new features new capabilities to our plugins say for example our Cory editors so can can you imagine the Cory editor first Cory editor of Prometheus just have a simple text box which accept inputs no autoc completion no query Builders but now we evolved into a modern Advance query Builders which does lots of uh job for you to make your queries and not only this query Builder we also added many US ux friendly features such as making your learning your query within the query Builder say example kick your query explain your query and lots of features we are adding to our query Builders and we are also adding AA based uh query builders in some of our data sources so many things change in the querying world uh alongside query Builders our configuration Pages for data sources also have changed not only we add new featur features and capabilities but we also try to make them easier to use and setup and for example recently in the last year we did this configuration redesign project where we redesigned and updated the configuration pages of the most used data sources that we have so our goal is to for you to have this successful connection message as soon as possible and with less effort okay not only the query Builders config Builders but underlying tools also change so one of the biggest changes initially our plugins were created using angularjs which is already duplicated as Mitch mentioned we are going to remove in the completely removing the next uh grafana and we have put it behind feature flag so that's one of the biggest transition so lots of tooling also the changed how we develop the plugins and the way we scaffold and bundle our plugins also has changed so previously we had this grafana toolkit package that is now deprecated it was good it was working it was doing his job except the cases where it wasn't working and then it caused us a lot of trouble so we learned from that and created this new grafana create plugin that is now the standard for scaffolding and bundling your plugins front end so not only the way we scaffold the plugins change the way we publish the plugins also change can you imagine 5 years back if you are a data source developer you want to publish a plugin you just go to the repos Tre and put all your details and uh create PR to publish a now it's just a simple click of uh click of the form and submit in the gra.com you can submit as many as new versions you can with single click so many things changed and as you can see even the way we spell gra has changed so in the early days maybe 10 years ago it it happened that grafana was spelled differently but now we try to make sure we had the spell checks um to make sure that grafana is always spelled correctly and like graph now graa are not allowed anymore right so many things change as said but only thing that didn't change is the need for more plugins our customers our community wants to bring their data from many sources into grafana and make the big 10 bigger and also as the software ecosystem Evol there is always a need for more and more plugins new tools coming in new uh new applications we are developing so always there is a need for new plugins uh we are continuously expanding the catalog of our data sources but the speed is not enough to cover all the needs of our customers and users but we wanted the community still to empower them to bring their data and visualize it into grafana even when data sources are not created yet so here where Infinity data source comes into rescue now shiran will share a bit more about the story about infinity and its features okay so what is Infinity data source plug-in so this is the data source plugin which you can download it from graph catalog like any other plug-in but what makes this special so this is a universal data source plugin which allows you to pull data from multiple sources multiple applications using their rest if your application provides some rest APS you can use it Infinity to connect you don't need to wait for a new plugin uh to come up so uh so this means we are referring this as our goto plugin uh for cases when the there is no native plug-in exist so if you don't have native plug-in for some of the things such as snake or something you can use our Infinity data source plugin and connect and get the data as you see in the screenshot so you just put this URL of the your AP in point and get the data and do some data massaging if required and you get the data right how how this all started so in 2020 uh actually as a h project I wanted to visualize uh some of the interesting data I found in Wikipedia uh in grafana So at the time I had very limited options either I can write some Prometheus exporter and scrap the things and publish into Prometheus or inflex then visualize that is also another option I can use existing simple Jon APA which is our uh pre-processor of this uh infinity plugin I could have used that but the developer in my in me ask me to do some adventurous thing I want to develop a new data source plugin which is where the infinity comes in so when I develop infinity infinity I created as a data source plugin to just scrap content from any HTML page then once I develop I quickly realized okay it has more potential not only the HTML so if if it can uh scrap the HTML and convert into some nice graphs it can also capable of doing data pulling data from any other formats like this on CSP like we often refer this Infinity as a versatile Plugin or a Swiss or minif of plugins because it can connect many things it has many capabilities you can play around a lot so it it it covers very basic use cases and also to the complex use cases say for example very basic use cases such as just pasting your CSV URL and getting the data visualized and the complex example such as uh you connecting to some graphql apas and visualizing your application traces data and do something like that so it covers versatile use cases okay as I mentioned uh infinity supports different data formats jsan CSV exam uh and the way the infinity is designed it's also make make us easy to add more formats in future for example if there is we want to uh we want to create graphs from yaml file no one do that but if you want to do that we can support that in future right let's see what are the response format Infinity helps okay the most common um use case for the infinity is to visualize the Json data as you see here in the screen uh I am visualizing uh some of the data from an iot platform iot platform called things speak so which sends me some sensor data about my uh the traffic traffic situation in some of them as you can see that's a nice Json so I I don't need to write any new plugin so I can simply use Infinity to visualize the data so here and the right screenshot you see I'm just putting an URL of the feed which is public uh I'm I'm simply selecting the fields I want and and saying okay this is my Fields this is my format I want use then you get the data out of the box okay you can try this yourself in this play. gra URL play. grafana Infinity Json we can share this later another most common format uh infinity support is like d Limited Format like CSV or TS or any other D Limited Format so here you can see I am visualizing a public uh GitHub public GitHub data I found uh which is talk about natural disasters over the years so same as Json I'm just pasting the CSV URL and selecting the fields and I make sure they correctly formatted say for example here it says year but I need to explicitly make sure this is passed as date not just number and also deaths I want to make sure this is a number not the so I need to specify all these details to get this graph okay the same principle goes with uh XML as well like Json CSP so here uh here I am just visualizing the status feeds uh from Google Cloud which is the it can be any RSS or any jsn format uh sorry RSS or autom format XML format so here you see I'm getting all the incidents uh I'm selecting the same way as how I did my Json CSV I'm putting the URL and selecting the fields and even I'm just doing some alasi thing and all those things so and I get the details of the Json think about you have some Legacy application which have some soap AP still we stuck with but you can still visualize uh the data from those OP apas using this Infinity plug-in right so since uh we can talk mostly about this uh Json HTTP CSP things it also needed for Infinity to support other HTTP based options say for example you want to customize uh your headress you want to customize your Cod string you may want to customize your body so infinity have those options so that means with all these options now you can easily connect your graph end points as well not only the rest AP end points so here in this example I am visualizing some public data from graphql which shows me the list of countries and some some relevant details okay so here in the bottom you see we have uh some variables in grafana uh in graphql I want to pass it so in the infinity graphql it also supports you passing the grafana variables to the underlying variables so you get the data only uh what you want and also there's play. graan URL you can play around okay so we got the data we got the data from Json we got the data from CSP but what what next so all the time the data doesn't needs to be in the format you like sometimes you need to do some data massaging like some sometimes you may need to do aggregation sometimes you may need to filter out the data and you need to do some transformation of course there's a gra transformation which can help but what cool is if the data source itself can't do the transformation that's awesome like any other SQL stuff let's see what are the passing options we have over the time so Infinity uh provides few several parsing options so initially when I created this Infinity I started with the simple passsing options say for example it automatically tried to pass all the array objects uh and visualize your data so that means it's a very simple and basic use cases uh it all the passing happening in the browser the front end so here here you can see I'm selecting the default passer uh in the query and I'm also selecting from this Json I'm selecting country as my uh root object and select in the fields okay before that there's an example so here I'm using a public API which which allows you to check how popular your name is uh some nationalized uh something I will uh where I'm putting in my name I'm getting the results so I'm searching foram okay SRI Ram is popular in India and Singapore so something like that so I can visualize this data uh in the in the grafana like this so you can select the simple personer and select the fields I select the country and Country ID probability and get the data and then we realized okay we we have the simple parser uh it is not enough for doing aggregation and filtering and other stuff so we need some complex uh parsing options so we introduced uql l in grafana uh sorry infinity point4 version uh which is something similar to other Cory languages such as uh uh spun CU custo so it's bit flexible uh in terms of parsing uh so it it does provide various options to do post processing of data like filtering and manipulating things so here in this example I I'm uh visualizing some data from an analytic sites called meta mode demo data uh so here with the simple queries and I'm visualizing the data right so again all this uql and frontend part happens everything in the front end but in grafana world we what we want is we want more so we want uh our data needs to be backend compatible so that means we can do the alerting we can do public dashboard we can do query caching we can do recorded queries and all those nice features so Infinity 1.0 we introduced backend parser which means you can select the back select the parser as a back end then automatically your data will be processed in the back end and compatible with all the alerting systems so here in this example uh that's a simple uh GitHub URL which Lees me some of the users data okay uh with the backend pass I can simply select I want to say name Age Country and other things but in real real world that may not be the case you may need to do some manipulation so we use we can use Json Json Json is a Cy language uh you can put the Json cores to do the manipulation say for example I'm doing some calculations I'm doing some Transformations Etc so you can do play around and so simp as you can see the simple Json converted into the complex uh results with all the manipulations okay so Infinity is not just only for the hobby users it is also for the Enterprise use cases most of the times all the Enterprise apis will come up with complex authentication system security system Network systems so Infinity does supports that so basically infinity have few several authentication options which makes it bit powerful connect with multiple systems so it it supports authentication systems ranging basic C uh barer token and digistar and even uh o o and JWT toenut and we also have the cloud provider based authentication say for example aw does have a specific authentication called sigv4 authentication Infinity does support that even if you are using Azure Azure things you want to connect uh your AP is behind aure authentication you can still use with or to Cent credential and if if your AP is be AWS or Google you can use JWT and other authentications so that means with this uh all the authentication systems you can connect to many of the possible apas okay let's see some real real time examples how we how we are using and how customers are using and what is the what's the capability of this okay uh I have say for example I have a Prometheus uh graph which shows me some error metric uh error rate suddenly my error rate goes up I need to know why my error rate is I can eventually start debugging corate with other metrics but what happen if if I'm using some cloud provider like Google if there's a Google outage so if you have annotations over your error graph saying okay there's a outage in Google in this region because of that your error rates are going up so with infinity you can simply uh correlate uh using graphon annotations and this Json you can easily visualize okay there are rates and this there outage that saves me tons tons of time okay here this is another example so in this example I'm visualizing my custom application locks data my uh my custom application currently doesn't uh send the data to Lo in that case it just expose only through apis so I can use Infinity so as you can see it's not only visualizing the lcks as a table it also uh nicely display as a graph locks format uh as you can see I am passing all the graph macros say start time uh so I don't want to pull all the logs uh from the API I want to restrict and sync it with the dashboard time range so I can pass all the dashboard context user context using Infinity macros to the underlying APS so that means you will get the only relevant data to the dashboard and also at the bottom you see there's a small button which is uh traces uh which takes me to the corresponding traces from the trace ID and again this is the corresponding traces ID view uh this traces ID view again it uses the same application but the the end point is now this time traces end point instead of logs end point it is going to the traces end point so again with the simply passing the URL and I'm getting all the traces data as you see I'm selecting the formats traces instead of logs I'm selecting traces so this this transformation uh from the logs to traces done via uh our correlations graph correlation features which we announce last year so so here this two slides are here just to prove okay not only Infinity visualized data it it also interact with other graan other graffan elements such as logs traces correlations okay sometimes when you are calling a data your data might be coming in few pages like it may be in the chunks say first you me to get first 10 results then you need to Pate for next 10 results something like that so Infinity does supports the pagination here in this example I'm calling a Pokemon API Pokemon AP send me first two results in the first quy then I need to paginate again to get the next set of two results or 10 results Infinity does provides those such pagination options you can choose okay what the parameters you want to pass in the each page so that Infinity knows how to iterate through pages and how to consolidate before sharing to your dashboard uh in in real world it's not a simple page Nation the pation can be complex like some page ination can be simply number based page get me page number one page number two something like that or sometime it can be offset based page okay my I want offset by 10 offset by 20 something like that you can do offset based pagination as well and sometimes your data will be uh having metadata like cursors so cursor based pagination you will send uh like cursor in the first URL and the same pass the cursor to the second URL like that so infinite does support those spination which will make infinity easy to get lots of data okay last week I came up came across with this community use cases and how Community is using this Infinity this some examples I want to share so here in this uh in this example uh user uh one of the user from the London visualizing their uh public transport data tfl data using grafana and infinity so here what they trade is they want to see when their next bus is coming using the tfl AP and what cool thing is even they tried the back uh back end parser so that means now this dashboard can be accessed by public so public dashboard feature the user is utilizing so you can play around this cool dashboard in this URL and another example is like here uh we see the the user is tracking uh some Airport departures but unfortunately the user doesn't have the apis that the user doesn't have Json or doesn't have CSV to visualize but what they have is they see simple web page which is very interesting for them so they try to visualize this so here is as you can see the user selected HTML type so and selected the HTML Fields they want it's bit of fun thing to do with this HTML so still you are able to get the user managed to get the data from the simple HTML page like how I did in the Wikipedia scrapping same way the user did for some other page and get theboard dep purches it's really cool okay so not only this community use cases there are also some complex use cases uh such as this one so here in this one of these YouTube video a user was showing how they're connecting to the key clock key clock application key clock is one of the authentication some kind of application uh but the keyock apas are just behind uh tication mechanism O2 authentication so the user make use of infinity2 authentication and specified all the details they want to pass the API so that API can be authenticated and authorized and get the relevant data so this is the example and how they visualize and once you get the data even you can do alerting on top of it you can do all the cool C things you can do okay again this is another cool example uh from one of the user from Japan where the user uh showed how they are visualizing the stock market data so as you can see the user selected uh maybe the screenshot is too small uh the user selected simple front end parser so they don't need to do any complex post processing they put the URL they select the fields they want and they get the stock market data in our Candlestick chart okay I'm continuously getting amazed with how how many use cases our community comes up with infinity and also the how they show their love towards the infinity plugin I'm really really impressed with that and also uh there's a lot of active community members uh actively interacting in the community Forum grafana Community Forum asking questions and helping each other about infinity and all the cool use cases they trying to connect and even recently uh the infinity got 12 million downloads in k.com C so all the along with all these Community use cases our Enterprise customers also trying many different things say for example they are connect trying to connect with things like uh big Panda they're trying to connect things like Snak or they're visualizing AWS cloudcast or Azure security events so lots of things they trying to connect into grafana and making the grafana their grafana big ttin bigger being said that uh last February we announced graan Labs now officially maintains and supports Infinity plugins so that means it's no longer uh a simple one person hobby project so it's no longer my personal hobby project it's officially supported by grafana grafana now spends a huge engineering efforts to make this better and adding more features to the Infinity uh after this announcement we made in February we quietly add lots of new features uh one of the recent feature we had is like PDC support for the infinity which is mostly as by our Enterprise customers they want to connect uh their cloud data uh Cloud instance to their API running on PR so with this PDC support they can already do this securely and we also moved the inte documentation into the gra.com so you can learn more about Infinity within graana.com itself and even we also improved our demo instance where you can play around and learn more about Infinity you can play around play. graana.com SL Infinity we will share the link later and with all these cool things there's also the infinity will stay remain open source anything okay so as you just saw Infinity is a great data source and we're are really happy to have it in our plugins catalog but is it really our final destination or do we do we want to stop here actually no we want to go beyond Infinity but why to go beyond infinity well Infinity is indeed really powerful data source just saw it was able like single plugin was able to fetch the data from various data sources VAR systems with different uh formats different data types and so on but some users might consider this plug-in a bit Technical and complex definitely not us sham for you is everything easy but for some User it's still a bit complex and it kind of shifts complexity from plug-in development to dashboard development meaning that when users create uh pen when they set up queries they need to understand how the underly apis work how the system works which data it returns how to Pro process it and so on so even though Infinity helps us a lot and it fills the Gap where the plugins doesn't exist yet we still realize that we need to develop more native plugins and we even set up this goal for ourselves so in the 11 years of grafana together with Community we created 150 data sources and actually more than half of that was created by Community but now we want to push this forward and we set this goal to scale up to 200 native data sources in one year um but creative creating native data sources it comes with cost right so it takes a lot of time and effort and also even though we use like reusable sdks and components we still find ourselves that we repeat uh certain parts of code bases and as we develop and maintain a number of our plugins it grows also grows the maintenance cost and it's becomes much harder to keep all these plugins consistent so how can we overcome all these challenges how can we achieve all the goal of 200 data sources in a single year well of course we we're going to use more of reusable components so we create them more for example there's already authentication component that has been used across various data sources in the configuration page and um we will use improved tooling as we shared today there was created the gra create plugin package that is used for scaffolding the bundling plugin and we will use automation for example recently very recently there was the plug-in end to end test and pay package uh published I think version 1.0 which we use for endtoend test across various grafana versions but all this still not enough so we're going to innovate and for that of course like we're going to use the Graal apps hackathons that are regularly organized and as you already know U many features that are now available to users and our customers were started as hackathon projects well what we can say of course definitely we don't want to to stay here we want to move forward we're going to go beyond infinity and what you can expect from us in the future of course more new features delivered to infinti as fream already mentioned and also to our existing native data sources much more native data source plugins created and improvements to create and maintain our plugins and who knows maybe next year maybe we'll be standing here and sharing how exactly we achieve this 200 goal uh which new features we delivered and how it's very easy to create and maintain plugin at this point and to add what Andre said uh if you're Enterprise customer or if you're cust consumer of you don't if you are looking for some plugin and you are waiting waiting for the plug you don't need to wait uh for the plugin to available you can try with infinity and try more things yeah exactly so that's all from us at this point if you want to hear more on plugins consider joining these sessions from our colleagues later today and we'll be available after the talk in the ask the experts Bo so feel free to come and uh ask questions thank you thank you
