# Grafana Tempo Community Call 2024-03-14

Join our next Tempo community call: ...

Published on 2024-03-14T20:56:17Z

URL: https://www.youtube.com/watch?v=nSV8tKSMBvI

Transcript: cool all right welcome to Tempo Community call March 2024 I had to look at the corner of my screen to figure out what month it was uh we have a shortest a shsh agenda today I feel like but we do have some good points on there um certainly questions are welcome as always and I think I should share let me actually find oh there it is there's the doc and let me share and prior to starting the recording we had a fantastic discussion about uh what were you talking about keyboards and our our mechanical keyboards um agenda three points Tempo 2.4 exists we cut it a couple weeks back at the end of last month um we did find an issue though actually a Community member found an issue so we don't we don't use the bucket prefix internally but all three object storage have an option to configure prefix which will just basically make Tempo use you know things a few folder pass down however you want uh somebody discover this externally that uh two4 we made some polling changes there for PCO Improvement uh and someone found that we did not honor the bucket prefix so we're getting a PR in now thank you to this BP Foster fellow um and Zach is doing a good revieww on it once we get this in we'll cut a 241 because it's just broken right now I believe Zack do you have any details on that to sh uh the change looks good um we're fighting with CI right now the go const I don't know what to say about that right now but change the change looks good and I've been testing it locally this morning so okay I think we'll get that in soon okay and I think uh this this person even added integration tests so we won't break it in the future and uh we can feel confident we won't mess it up you know next time cool uh this is a cool thing that's coming up it's kind of in progress work uh we want to stream everything through a set of grpc end points from the front end so about God it was about a year ago at this point and we've kind of wrestled with it some walked through some different Technologies worked with graa I think we finally really landed on a pattern we like but uh we want to stream a searchers which we already do we also want to stream tags we want to stream metrics we want basically all endpoints to have a grpc streaming endpoint because we just feel the user experience is so much better when you you know start receiving those results just a second or two after you uh initiate your query it also has the nice advantage of seeing um some sort of progress bar or some kind of feedback on the weight of the query you executed so you can you know make adjustments if you execute a query and 30 seconds later it's gone 1% maybe you could make some changes to make that faster or change the time range or you know you have these options instead of just staring at a um staring at a a spinning you know spinner and grafana so we did a refactor here um or this this is the second PR which Mario is definitely reviewing um the this is the first one where we added all of the different pipeline items that allow us to rewrite our HTP pipeline into this new async format uh and the second PR here is going to move all the tags over uh next I will tack all the last few endpoints and then um look at trying to get our new metrics endpoint onto streaming um so so far so good but I think this will just really make the experience of tempo you know first class open source product with grafana doing streaming all all endpoints from Tempo the distributed tracing pack uh finally uh and I I'll look to Marty if Marty has any other metrics updates we've been working very hard on it He suggests no by his reaction there uh metrics are technically available in graphon Cloud traces right now but don't tell anyone um does anyone have a graphon cloud traces account can any I don't even have one I just use our internal tooling but if anyone has one and could show this it' be great we kind of accidentally worked ourselves into a corner where both Tempo and graphon would support metrics from traces and they just rolled out so it it works right now on graic cloud with a ton of caveats like it's broken in all kinds of weird ways so if you do have a graffan cloud traces account um please fool with it play with it learn about it give us feedback currently it doesn't work for any time range over 30 minutes due to a bug uh and you can basically pipe thank you Marty any Trace ql query any descendant query any uh span set combination anything you want and then you just pipe that into a simple rate and it'll show you the rates um an addition you can do rate by field such as um uh you know such as the resource service name or the span name or the HTTP path or really anything you want so this actually works which is you know something surprising um did anyone does anyone have a graphic ches account that can show or do we all just use our internal tools uh I mean I have one but it doesn't have any data okay okay like regularly send to it yeah sure we can f with it well maybe next next uh Community call we'll do a more in-depth like state of metrics and a um uh a more in-depth state of metrics and a demo or something kind of show where we are because things have come a long way um and it's quite capable but we still just right now we're pushing very very hard on performance at hundreds of megabytes per second scale more than cleaning up loose ends and so there's a lot of rough edges when you just try to use it essentially is where we are right now cool yeah to add a little bit to that so um just performance like um scale like things like that at larger workloads is really what we want um language features like we have a huge list of all kinds of like features and capabilties that we want to add I think in some ways like that's kind of like easier we want to make sure we get it right fundamentally before we add all the additional complexity for all the new stuff on top yep uh right language feature wise I think quantile would be the next thing and after that I kind of don't care for a long time like rates and quantiles do so much work there's so much value from this that I think even just letting it sit and continuing to improve uh for a while while while we get feedback about what you know good next steps are so you know you could do quantile you know you type in perhaps your thing whatever your cont is and some field from the uh some field from the thing you could I assume we're going to write it in a way where you could even do any value feel any numerical value but I'm not going to guarantee anything obviously duration would work yeah yeah no that would work um I don't know how exactly it would work but we'll definitely support that yeah mhm yeah like I'm not sure like yeah there's stuff we need to figure out there like what would be the bucketing internally for status code like maybe yeah like are they ordered yeah I guess because they're numeric you could sort them P99 of the status code mean you'd get like a value back like 304 or something like well there you go yeah 497 it's a problem if you're 497 that means you got a lot of 500s in there somewhere yeah we're gonna write all our slos against the P99 of the status code cool uh all right I like I said it was kind of a short agenda to do a quick recap two fours out we do have a known issue we're going to do a 2401 uh streaming all endpoints is in the works it's a big Initiative for us I think the two major like user facing initiatives are the metrics and the streaming um and then um yeah if you have GIC Cloud traces if you have a free account um if you don't sign up for a free account fool with it a little bit if you do give some of these metric squares a shot but don't tell anybody because it's mostly broken but it will be working a lot better soon all right questions from the peanut gallery thoughts questions uh any ideas favorite pizza toppings keyboard screenshot I have a question for the streaming will that also work over htdp so current like for example you have a trace qu query currently you get back a big pile of Json is that also planning to somehow Support over the HTTP API or only so it it the streaming will only be over grpc um but grpc is built on http2 right and Gra actually had to put it on the same port so you can do both HTTP and grpc queries on the same port in Tempo with a configuration option uh and uh see see the streaming Behavior let me look at this real fast again uh part of this PR which is only 38 files uh and 2,000 3,000 lines changed um is adding grpc capable CLI so the CLI supports grpc call so you can run this and see the exact like raw output the Json like streaming back uh and the search already does so if you right now in tip of main Tempo two4 Tempo uh you can run a uh a grpc from the command line against the streaming endpoint and you can see every single like Json object it throws back until it closes it so graffan of course hides this from you and renders it nicely in the results but if you want to see the raw output then uh the the CLI we'll show that to you cool so graan is using the GPC endpoint to yep so if you've seen the streaming Behavior then yes that's over grpc uh what technology they use between the grafana backend and the grafana front end I'm not sure it might be websockets or something but the like connection between the temp from Tempo to grafana back end is grpc yes okay and one question to the P version four um is there any movement Chris uh Mario do you want handle that if not I can take it um I don't I don't mind but I think you're just a bit closer to it um sorry the question didn't hear it he's thinking about his favorite pizza toppings did just if there is any movement on the for py for B much reest oh v park4 um I think it's U we just decided to shove it for for a bit because we had uh other priorities um but I think eventually we'll want uh links and arrays and all of that and that essentially requires v park4 um um I think we've done extensive uh testing of it in real cells with real workloads and the performance was pretty similar the the only drawback I think was block size um basically if we add more more columns and more attributes and more ways of storing data um that's just going to increase U block size uh but yeah we think it's like um um a decent trade-off or or like a reasonable tradeoff um so yeah I don't know maybe in a couple of months we we moving forward I'm not sure right so V park4 is definitely happening like the link support like Mario is saying we absolutely want it it's happening it's just it got pushed due to the team's focus on metrics and Adrien has a small leap of absence and he was really the primary owner and Driver of that feature and without him on the team for this small bit it was difficult to really feel comfortable merging it and feel comfortable moving it Forward because he was gonna kind of be the owner of that process so once he gets back um we will he'll take it back up he'll make sure it's completely up to date he we'll get it merged there is a small performance regression like Mario was saying but I think we're just going to eat it and it's going to be fine uh and we'll just improve in the future maybe five will be more of a performance focused uh version so yeah I know Andre you're the one who put some time into that right you put a few extra columns in there yeah like to get the the service stats kind of like how many how many services are involved in it TRS how many errors and stuff yeah okay yeah uh we recognize that you know contribution and we really appreciate they put the work in and we like it too we wouldn't have merged it if we didn't think it was something valuable for us as well you know for the graffan UI um so it's a great contribution but it just kind of got caught up in this uh small leave of absence issue so no big deal um when Adrian gets back uh which he will I think in a within the next month is that correct I'm not 100% sure about the timeline but he is coming back soon and um uh you can resync with him of course the team internally will resync and then that will be his number one goal will be to finish up V par A4 get it get it merged and then we can start working on the links and you will have that data in the back end also that sounds great and one last um question I saw currently the um Tempo is internally instrumented with the open tracing SDK are you open that I change it to the open telemeter SDK please do okay we keep trying and we just cannot find the banwi to do it if you can get it over to otel we would we would love it we need to wait for the server change on that so that's the dsk kit Upstream um without that I think we're we're blocked and I know there is work on the mamir team that's happening I think this quarter um to help that so this may be coming we may be forced into it soon um so I would expect that uh we know more by the end of the quarter uh I guess I'm not totally aware of this Zach do you want to follow up real quick and see if I mean if Andreas can contribute to DS kit thing and if it's part of doing the tempo thing maybe he'd be interested in just closing the whole Loop is that possible or are you saying we have to wait on mamir for something I'm saying the work on mamir is already in flight because they're trying to convert I think we're trying to convert all the databases simultaneously and because of the way the server is instrumented we need to wait for the server change okay um if you want to poke at it some Andreas to kind of find this problem I do know like Zack is saying dsk kit does some kind of uh automatic instrumentation stuff with tracing at the at the server level so if you want to see what that is you're welcome to but it does sound like there's momentum on our side to move that forward too awesome yeah I won't get time for it immediately but in the next few weeks or something I will take a look at that sure thank you cool anything else crew all right you all take care it was good talking to youall seeing you and we'll catch you in about a month with hopefully some more metrics updates and some more V Park A4 updates but everybody take care and I'll see you when I see you bye everybody
