# How Visualizing Logs Converted to Traces Can Uncover Performance Problems | GrafanaCON 2024

Interruptions in a service and no clue why it happened? Visualizations help to identify problems and give more insight into how a ...

Published on 2024-04-25T23:28:50Z

URL: https://www.youtube.com/watch?v=Z1E647KipA0

Transcript: and thank you all for joining the session uh before we actually start I will shortly introduce myself I'm case boss I'm a software engineer at open value as open value we help other companies with our software challenges uh we're working in the teams at at the company um my focus is observability reliability and also troubleshooting um I'm using gravana for already for quite a while um and I started sharing my experience about that on the blog and also now in the stock um so I always show you what I learned uh in this situation are you ready for an incident investigation I'll take you on a journey uh which which I had on uh finding the actual problems in one of the systems we had um I will give you a bit of the background um I will show you the tools I used uh and I and we will do a step-by-step investigation on this about the background uh we have uh an Java messaging server JMS server which is a server where you have message cues uh so a producer is connecting to it with an persistent connection to it uh to be able to push messages on the cues and also consumer applications uh also creating a connection to it uh consuming the message and probably replying on it if you have a request reply setup or a f fire forget then it's just handled and no answer sent back um so um uh during uh during one of the the incidents uh it started uh uh with network patching according to the to the network team uh the patching went Flawless only two seconds downtime um and and then all Network traffic was fine again but still a lot of applications were not able to connect again to the JMS server so we're wondering okay why is that um and also in the postmortem session one of the things you often hear is yeah it's the network yeah uh the network we have TCP it's designed to to be able to handle this but uh is it then the root cause of your problems or is it probably the trigger of your problems and is your application not able to handle it and let's see what we can find there uh this is my uh swis iry knife as I call it uh I use a lot of the theana tools also locally to do the to do the analysis um yeah here you still still see prom tail and open Telemetry collector yesterday we heard allo is there so uh in the next version I'll will update that um um but this is what I used and uh what I used in this case I asked the team of the JMS server can you provide me the LW files uh and I loaded I used promil to load that into Loki uh and one of the features I use as well is uh the replace feature also to uh to Hash some Valu so you can't see the actual values but you can see the hashes so you still you can see uh information about the users and the host names and IP addresses but they are hashed so you can't you can't see the actual uh details um so let's uh have a look at it uh a question for you explore feature who of you is using the explore feature a lot okay nice I use it a lot because the dashboards uh most of the times there are the known things to look for um but yeah also in these type of cases uh yeah there is also a lot of unknown things and the explore feature really helps to find these problems and now also with an announcements yesterday also about the the metric explore and also the Lo explore that will really help also in my daily job to to find whatever issues are there um I loaded the the jmss logs so you will see a lot of a number of Lo Q queries uh but also uh uh that will also with the new features uh will become less if you can use the the explore LW feature um but um I I selected here the the jmss lws uh for a certain server and what you can see uh the network patching was done during during the night and uh you can see here uh the spikes of the number of messages so that indicates that there is a problem at that moment um zoom in to to the to the situation what you can see here um is here at the back of the line you see disconnect disconnect disconnect disconnect so the the JMS server detected that also the all the connections uh were dropped then then we will go down and then go down and you have to scroll a bit um and then you will see uh so new new connections are coming in um and what you uh so I will uh take another uh one oh no that's a bit too early so what what you can see here um for example at this line you see here okay we we do have a connection and what you if you we take this one so what you can also see here is there is an offset and the offset is calculated by the server uh the offset is uh between uh the moment the client tried to create a connection and the server actually confirmed the connection and if you have between these two moments an offset of this is milliseconds two and a half seconds to to to create a connection that's quite long so either there's Network latency or other problems or uh that was also in the documentation probably an issue with a lot of connections coming in so let's let's see uh if we can find more information about that uh of that offset so if you zoom into that then you see uh this is also with the loq query uh highlighting the the offsets and you see the offset is growing over time so it's getting bigger and bigger so that that gives a an an indication of something which is going wrong and then I thought okay uh but what if we could visualize this because that helps in the in the in the investigation so if you then have a look at so also again with with the lql query you can take the the the the query you can take out the offset so with the recal expression take out the the time for the offset and then with an average over time you can see uh what the average values is of the offset over time and you see it's especially at the first part it's growing fast and you see here 30,000 40,000 so it it has to wait 30 seconds before the connection was created uh that's quite long but if you also have a look at the Times below you see 30 seconds then it looks like that everything started to connect yeah in this period and just piling up so what is there um oh the one thing I forgot to show um no what what is here as well is as soon as uh a connection is established here is also you see here is also a message uh authenticated via or module so there's also the authentication happening for the for these for these applications so uh in this setup you have the producer and consumer connecting to the JMS server but to see if an an an application is allowed to connect and to to see data from s from from cues or push message on a queue there's authentication so um there's also the authentication server involved so let's see if we can find more information for uh on that how the how the interaction is between these two services so most of the times you have uh the producer and consumer application you write them yourself um you focus on observability for these applications but uh the server and also authentication server is more of most of the times it's commercial products and we have Lo loging of these uh applications so the the all server I requested the team as well can you provide me the LW files as well and then we can see what we can find there so um again a loq query uh so this is the access L file for the for the all server um uh and then give me all information from from uh that particular machine and then you can see a lot of connections are coming in so at least we see the connections coming from the the uh the JM server to the old server one thing you have to know more is uh we have the JMS server uh that's creating connections uh but also having a persistent connection so the J server has a persistent connection it's using the Elder protocol it's having a persistent connection to the old server and uh it's doing query okay but a new user is coming in does the user exist and what is the DN of that that user and then uh for that user is uh then authenticated over a new connection so then a bind is done uh and with a bind that's the actual authentication is the the username and password is that valid and then after that the persistent connection is again used to query okay in which groups is this user available and even uh um the group is that also participating in groups um so we were we are able to to find all the connections or at least the connects but then we need to know but what is happening on these connections so one of the advantages here is you see a connection ID so that gives some uh indication that there is more about this connection so I uh did a query on two of the connections and what you then see is you have a connection and you see a connect coming in and a bind so we see that the authentication is done for this user and here also again a connect and a bind so um we need to find out all the connection IDs so what we can do again a lq query you you have the the from the user so and you can extract the the connection ID and then print the connection IDs and if you do that then you have a list of connection IDs um I'm a bit lazy I don't want to copy paste all these uh here you can see 87 uh uh one by one copying them so what you can do you can download the file so then you at least have it in a text file and then you can do things in your text editor uh but there are there are more things you can do uh there's also Lo that's the command line UIL uh also from the Loki team which you can use to Creer uh uh and send lql queries uh from the command line to Loki and if it if it's on your command line on your shell then you can use all other tools you have on your shell as well uh and one other things you can do you can do scripting you can do uh store it in variables you can do sub subactions with it combining in it in one uh one command so what I did I downloaded the the L CLI um I created some environment variables and uh one of them which you can easily use is the the the Loki address so either you can connect to the to the Loki server itself or you can do proxy through grafana um I also created two other uh environment variables for the from and two then you don't have to mention the time ranges each time and I created a function for myself that makes it a bit easier to to to do this query so then I can use this as a command line uh action Lo ql um and I will switch to the command line uh and this is the uh the same lql query I showed you before um about uh yeah from this IP address get the connection ID and print only the connection ID so when you're in it you have the connection IDs on your on your command line so now you can do anything what you what you already can do with with with your command line so one of the things you can do is uh for examp example uh uh count the the number of lines so well it's probably a bit hard to read but here again 87 so we have the same list uh but but you can all do things like sort and then you then you get it sorted uh but you can you can do anything with that now so then you can use also other tooling and um now I have them just all on one on one line so now you can copy paste it and use that again in your in the browser so let's go to the next step so I uh copy pasted uh it and now uh I have all the connection IDs uh available in the browser uh and one other thing you can do is uh so this this is one one loog query uh and then you can add another one as well for the JMS so then you have the the log files from the access log and the JMS in one file in in in one shot and let's see what we can find then so again we see all the disconnect we have to scroll a bit and now uh what one of the first things we see is here is the user lookup so the first action done uh the from the the the JMS server a check is done is does this user exist now you see also here um a connect and a bind and you see um uh search is done so the the group lookup in which group is the user and also you see nested group group blups so um you see a lot of actions now coming from the jmss server to the old server um what if I can visualize this and I hope you can read this this part but I will see if I can highlight it more what you can see here uh so this is again the same information from the loss and uh at the start you see uh a time stamp when you have loging most of the times you have a time stamp in your loging but at that moment the action is done so that means that the end of of that action but also in the information you have you have uh in this case for the L protocol you have the E time which is the elapse time so you know the end of the action and you know the elapse time so you can calculate the start of it and uh then you can create a an a SP you can create a block of it and you can repeat it so then you see the same information again and if you uh do that uh step by step you see uh that you already get some more information then um we have the old module that also has the the end Tim stamp but there is no information about when did it start but what we know is uh you have the username uh here you have the username but at first at the first moment there was also the same the lookup for that same username so you know at that moment already that action started for the user so actually you know this is the end moment for the old mod module but it started already uh at the moment uh the first lookup was done for the for that user on on the on the old server and then you have the information about the connection there you see the offset that's the moment the client created the connection and if you combine that then you have some information uh also about the connection and if you then have a look at uh what's here below this looks like a gen chart or what you also probably can do is create a trace so um for the spans you need an end time so that is the the the the time stamp in the logging you need a start and then you you have the E time or the offset time and you have the correlation and that's a bit of the tricky part so how to do the correlation between these items so what I did is I created uh Java code I I pressed the the download button in the in the uh um in the UI to to get the merged file uh I created uh I pared the the file I created custom spans I did the correlation in Java code and I created a a trace file from it and then you can use the the upload Json file option in the browser and then let's see how that looks like so here you can uh use the the import Trace function you can choose the file and then upload it um and this is how it looks like so here you see uh the reconnects and the connects uh coming and here you see uh also quite uh quite large times and also here at the top you see uh also a a big green part and that references to the to the long waiting time so the the long offset times for the for the connections and you see here uh yeah a lot of these connections are coming in and having to wait for a long moment uh before the actual connection was established we zoom in a bit more so I only took a part of the the of the file so you can see here uh the the connections coming in and if we then open the first one here you see the old module being active so actually the whole time of where the the J the first connection was coming in it took the time for the authentication and while this authentication was active more connections came in but they didn't do anything so if you open the next one you see the old module for this one started working after the other one was finished so if you then open this one again this one started working when the other one was finished so if you just focus on the OD module part then you see if you just uh take these you see also here in the in the in the in the part above you see the the the line but also if you have here you see all these actions are done sequential so one connection has to wait for the authentication of another one before it can continue and that feels like a bottleneck and if you uh zoom in more I created an an aggregate for convenience reasons but if you then have a look here on the all server you see that first search action and the lookup of the user you see the bind action then you see uh a lot of search actions so this is the the the the group search and the nested group searches so with this you can also see the bind action is giving problems um and then I'm always uh like so I see this information in in one way can I also visualize it in other ways or can can I find the the same information so the bind information is in the L files so again a Lo Q query with average over time for the bind action um take out the bind uh the duration of it and then you see at these moments on the old server the bind the bind times go up and that is causing the problems where the authentication uh are taking long so in summary we started with a problem where the producer and consumer were not able to to uh to create the connections to the jmss servers they had to wait long and some of these applications were impatient and were not uh waiting till the connection uh to be created and tried over and over again so that was also creating more connections and then they gave up because they didn't get a connection so the a number of these applications had to restart by digging into the the LW files of the JMS server and also the authentication server we were able to find a number of problems so the performance of the Y server was not correct so that that has to be be be improved but also the the JMS server had to fix a number of things making sure that you can do the authentication in parallel rather than sequential and also um one of the things we found is that the nested group part was also not required so that also saves a lot of search actions done from the JMS server to the old server conclusion dig deeper is it really the network or do you have other problems also the observability the observability data is key so sometimes you only have the loging but uh there is more uh if you have more information use it and explore it and and try to find the problems and also visualization helps and and that's what I showed you uh just by going through the LW files you will not always see the actual problem and by visualizing it then you can see what what the actual problem was what also helped in this case is not having just one Trace in in the overview but actually having all the traces of all the actions for the uh for the users uh being in one one big Trace file and also be creative if the tools don't support it or don't support it yet then you probably have to yeah do some more things yourself and then then still you can reuse the same tools and um one one other thing I realized after the sessions of yesterday is uh what I will do I will replace uh the the the prompt on an OP collector with alloy and give it a try and I will create also a new blog post about it and also I think also with the the Loki tree uh options also with the pattern recognition and also with the explore L feature uh I think and I will I will kind of revisit the same uh uh the same thing to see if also finding the the problem lines and and uh for example the the the line the L lines with the offset if you if you get these out of it uh more easy with this I'm really curious how it looks like if we use the explore LW feature with that that's it time for questions if time permits
