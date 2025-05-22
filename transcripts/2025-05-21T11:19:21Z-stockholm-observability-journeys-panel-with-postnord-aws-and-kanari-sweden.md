# Stockholm Observability journeys panel with PostNord, AWS, and Kanari Sweden

A dynamic discussion with Grafana experts and local observability leaders sharing successes, setbacks, and next steps in their ...

Published on 2025-05-21T11:19:21Z

URL: https://www.youtube.com/watch?v=XpsVrXJ39-4

Transcript: i think perhaps it makes sense to start off 
with a few introductions first so everyone   already knows who I am now so uh you want to 
head us first so uh yes I'm Marcus Nielson   i'm a product owner for observability 
and monitoring in postnord um we have a   small central team uh we're three or 2.3 
people to be more exact um so yeah okay thanks for having me uh my name is Sunita uh I'm a 
solution architect at Amazon web services based in   Stockholm i've been with AWS for around 5 years 
and I think many of you know what AWS is it's a   cloud platform uh I'm here to share some of our 
observations and insights on observability space   from a cloud perspective thanks for having me all 
right and Sarah yes my name is Sarah i work as a   sales executive at uh Canari h meaning that I take 
care of our customers and potential new customers   and um Canari is a partner to graphana and 
we work exclusively with uh observability   and digital employee experience to help uh bring 
value of both those tools to our customers all   right fantastic and as as you have the mic I guess 
first question to you then so we'll start off with   uh with with the main one then you know why 
why is observability important you know in   your case you to your customers good question um 
I would say that observability is important to our   customers because it provides a holistic view of 
their complex IT environments that otherwise can   be a jungle to to navigate in um it ensures 
operational efficiency to them and enables   them to make datadriven decisions um or even risk 
based evaluation to decision making meaning that   you look at the real data that actually matters 
and observability helps our customers to do that   very good um for us it's uh twofold because for 
AWS itself observability is a very important one   because our customers trust us so we have to make 
sure all our services are performing optimally   um and for our AWS customers um providing the 
necessary tools for their uh systems to be up and   running and making sure that uh how they avoid any 
risks or any impacts uh one of the um uh example   that I could give um for example Amazon retail 
uses AWS it's backed by AWS um I think many of   you might be using prime Amazon Prime uh Postnor 
is here so we also have a good collaboration in   Sweden um just to give you an example uh last 
year when we did prime day uh uh we observed   or we monitored about 6 trillion log events per 
hour just on the prime day so if we don't have   that type of observability landscape it's it's 
very hard to you know have that kind of uh uh   maintenance in our place yeah without uh without a 
mature observability program no one's going to be   going through six trillion log events an hour um 
yeah I mean for us um it's very important to have   um observability to to know how our um systems 
work in production basically i mean if if we don't   have observability we're we're flying blind and um 
um I mean we have u for example sorting systems uh   if they're down and we can't sort and we don't 
know what the issue is um people get mad because   they won't get their parcels of course and um it's 
very important to for you know reputation building   and um um I have I have another example we we had 
a we had an incident with um u master data that   wasn't propagating properly it was corrupted so um 
when people were checking out in in the web store   they could only choose one um point to collect 
their parcel and that's of course not good uh   so if we could notice could have noticed that much 
earlier this was 2 years ago so now we have better   observability thanks to Grafana and Grafana cloud 
that we're now using um I mean people would just   um choose some something else in the checkout 
and um yeah um so hopefully we will get we we   have reliability as one of our u value words uh 
within post nord so that's uh where we can from   the IT side uh contribute with good observability 
for our IT environment nice yeah yeah a few things   are as frustrating as uh as a system not behaving 
properly and you go to the status page on the site   and says everything's green and you go "No it's 
not green there's definitely something wrong   here." Anyway um so uh I guess question to you 
now once again you have the torch um what what   were some of the biggest challenges that you faced 
on the observability journey you've been on so far   i think what what was addressed here in I 
think was the first talk when talked about   uh culture cultural change and things 
like that so I mean we started out with   um having a central uh like no space based 
metrics uh OP5 first uh for more like business   flow overview for example all the systems being 
involved in in uh in in parcel sorting and um we   had some infrastructure and and and and the 
but the teams they would have to go to the   central team to have some of their applications 
being uh uh monitored so we we we it was quite   um uh it was it was a fragmented landscape uh 
some some um some teams use their own tools um and   uh we wanted to um u establish this central u 
platform um and I think the the culture change   as you said like you have the platform ready and 
then bringing all the developers in uh how do you   do that so we had uh Graphana stop by a couple 
of times and we had uh Graphfana days and um we   um um we were talking also to the having workshops 
with the with the uh product owners that they   would be more um interested in in in this kind of 
pri prioritizing these nonfunctional requirements   uh so that the teams would have to u be produce 
I mean observability to have a system that is   observable should be uh like a a basic requirement 
that but the product owners aren't necessarily   that uh they're more interested in or um to get 
the features out for the business and produce the   uh the value that way but they they can just as um 
if they don't know that their service is producing   the value uh then there's no use so they need 
observability so we had workshops to them to to   explain sort of why it is observability important 
for you as a product owner and I think that helped   to make the priorities in the teams as well uh 
yeah yeah yeah showing showing the value back   to them that they will get from observing their 
their applications and their environments exactly uh on the challenges um uh I echo what uh Marcus 
mentioned on the culture um it it has to be in the   basic uh foundation uh but some of the challenges 
that uh I've heard from our customers um or first   just to give a general observation even though 
we have so many proactive state-of-the-art   possible solutions out in the market on the 
observability there are so many customers who   are still performing reactive approach um and that 
leads to you know having um paying a lot of money   for that um um another thing is one customer says 
we have lot of data I don't know what to do with   that uh we we want to create meaningful insights 
well you could use you know tools and services   to create more uh business insight from it um 
one of the thing that I want to emphasize also   uh which touches on the challenge as well um there 
has been a misconception sometimes or has been   overlooked that observability is mainly just for 
application monitoring which is not you have uh it   also plays on the business side right uh deriving 
meaningful insights which impacts the business for   example if you're running an e-commerce website 
how many number of users that have been using   why there is a sudden dip and why is there is a 
you know very good performance at certain season   all these kind of things you can uh get through 
some observability tools so uh yeah more on the   reactive approach that I have been hearing from 
the customers from the challenges side nice I'm   guessing I'm going to talk about the challenges 
of our customers because our challenges inhouse   is different um but the main challenge I hear when 
I speak with our customers ers uh but also just   organizations in general um it sort of touches on 
what Marcus said with the cultural aspect um so   the main challenge I hear is that it's actually 
manhour spent fingerpointing trying to get the   root cause of the issues um rather than working 
on something else so getting people together and   working together has been the the main challenge 
when I speak with customers it's very rarely the   technology everyone is like ah technology works 
great you know it works as it should but the   people is the is the biggest challenge um and I 
also want to add to that that a lack of resources   and knowledge internally uh becomes a big 
challenge um so observability takes a lot of time   if you work with it now you know it takes a lot 
of time to adapt and to know what works best for   your business and I see that observability gets 
a bit overlooked in the whole business area so   the ones working with it see the value but it gets 
overlooked in the business and uh in that case it   doesn't get prioritized so it doesn't puts enough 
resources uh into it and that's needed to succeed   so I see that as a big challenge yeah making 
sure that you've got the the the business buy in   to really invest in observability because without 
that you're you're already kind of hamstrung from   the beginning um I also like what you mentioned 
about sort of the the sort of the challenges with   fingerpointing i was chatting with uh a customer 
towards the start of the week who was on a a big   program at the moment to improve their their whole 
incident response experience to try and get um to   sort of the point where they the the first team 
that they that they point that should be the team   where the problem actually lies not not the team 
that sort of on the surface it looks like things   and one of the metrics they're looking at is 
basically sort of how many how many people or how   many teams or how many different hops there are 
during the investigation to actually figuring out   what the root cause is and if that over time they 
can get that process to be more and more efficient   um then you know that will be for them that'll be 
a really significant win yeah a lot of people or   companies play the blame game too much and spend 
time on that um and if I'm allowed I we actually   had a a customer a year ago uh that had a big 
incident a big um customer in the financial sector   um where they had a downtime or an issue and a 100 
people got called into a like last minute teams   meeting to find out what the issues were i'm not 
joking 100 people into a team's meeting to find   over the issue were laying and everyone was just 
fingerpointing and they spent time on that and to   brag a bit about us we were the only one that 
could find the issue within 15 minutes yeah I   think there's there's definitely something there 
on like the size of a war room like the the more   people you have in a in a war room or incident 
room or something like that when something happens   possibly the more time you should be investing in 
your underlying observability platform because it   should be giving you good indicators of where 
the actual real challenges lie great points   okay so we'll switch a bit from from that side of 
things now to kind of talking a little bit about   um about how folks are organized so you 
know how do you generally see your sort   of your customers organizing around sort of the 
observability platforms the observability space   um in a dream world um the customers are organized 
where they have one observability team that runs   observability across the organization uh in 
reality uh majority looks a bit different is more   organized as siloed monitoring teams still so they 
might have observability in place but it's still   silos um with different monitoring tools um where 
observability works the best when you can get   these silos to look at the same set of data and 
talk together um all the way from IT to developers   to operations and and management and everything 
in between that they look at the same set of   data um as Canari or as us we are more organized 
around our vision and mission as a company and   as a partner to to observability vendors um and 
our vision being to be the thought leader within   managed observability and our mission to make 
observability data valuable to our customers   to not only be looking at metrics but also turning 
that data into actionable insights and and actions   and so we are structured around that we're 
45 people at Canari and we just focus on that   and the three areas we have organized around those 
that mission and mission is applied observability   digital employee experience and then advisory 
where we advise around those two excellent uh   Sen how about how about your customers how 
do you what's the breadth of organizations   you see there um it depends on different type of 
customer for example enterprise they organize in a   different way having a center of uh excellence 
team uh sometimes mid-market uh customers   uh they just have developer team sometimes when I 
talk to the management uh from the customer yeah   my developers will take care of uh monitoring and 
uh observability as well uh which sometime can be   missed uh like for example alert fatigues 
and those kind of things um so it depends   on different type different scale of customers 
that uh how they have been organized But that's   also part of how you know my role uh wherein 
I have to enable them with the uh right set of   tools and practices mainly which also covers the 
culture part that we have been discussing before excellent and with with personal how how do you 
how you organize today uh as I said we have this   uh central team um then um I mean nowadays 
when you have we want to make a s a seamless   um uh solution for the um developers to just 
um uh as part of the platform the platform   thinking so we're we're we have sort of a you 
could say a virtual platform team where we have   um um the the Kubernetes guys and then we have the 
u so they I mean they're also in involved in the   observability platform because we don't we don't 
send every uh all our data into graphana cloud   we use graphana cloud but we we also have our u um 
our own backend storage in the kubernetes clusters   uh just to offload some of the things that we send 
to Graphana Cloud to to keep it cost optimized and   um we're we've also been using the adaptive 
metrics and um uh not so much adaptive logs   yet but um uh so we we're we're trying to be 
specific when it comes to what we're sending   to Grafana Cloud to yeah to keep the budget 
um in a yeah good shape basically yeah yeah   i think the the thing that I think everyone's 
sort of called out a little bit in their own   way is that it's it's a journey like all of 
these steps you know no one no one starts out   with oh yeah we're we're just going to build a 
center of excellence from scratch right from the   very beginning like it's it's it always starts 
off from well what whatever you've got if you   all you've got is a group of developers and 
you know a couple of them know a little bit   about sort of monitoring and observability then 
that's what you start off with that's the that's   the kernel that you build from and while you know 
having a a center of excellence might might sound   very grand and and imposing it's really in my 
experience a lot of it is just about you know   adopting some core centralized practices that 
are shared you know having a shared belief of   what observability means across the organization 
and you know whether that is distributed across   you know a few observability champions across the 
organization or it's it's you know all in in one   group and you've got champions elsewhere you know 
it's that shared vision is what really matters   yeah we we we also have champions in the teams 
uh so as part of of raising sort of the maturity   levels because our teams are quite uh different in 
that regard some some teams are very advanced and   they use obserility and have been doing so for a 
long time so we wanted to um um first of all have   um everyone appoint an observability champion 
for their um team and then we sent them on this   uh on a graphana uh foundations course uh um in 
December last year and then we have continued   now monthly to have meetings where we where the 
teams get to showcase what they have been working   on um present their observability solution 
so that others can can um can learn something   and can share between the teams and and and 
get sort of the the engagement around this   uh area uh going so that I think that has been 
uh key also to raising maturity nice okay so   next next kind of question really is about how 
do you make some of these decisions you know what   are some of the criteria that you look at when 
you're choosing whether it's uh tools platforms   partners to work with those kind of things do 
you want me to continue yeah unless you want to   hand it off no I mean yeah I can I can uh I mean 
we were we started this journey like 3 years ago   um thereabouts and um we wanted to have a a 
platform that could unify everything because   as I said it was a bit scattered and fragmented 
before that and um a platform that was well known   a technology that people people already using in 
Grafana for example within some teams in post node   and it's um open source um um we didn't want 
to end up in some proprietary solution costing   loads and loads of money um so um yeah we we 
had a few of those criteria that um sent us on   the path of of graphana and and we did a we 
did a pock together with some teams and and   uh we we checked most of those boxes that we had 
and um yeah and now we're trying to and and then   we went on this journey of okay how do we get the 
developers on board as I said and and try to merge   um everyone onto the platform and that took um 
a year or so um to really get um people going   um and then we we migrated what we had in in OP5 
for example uh to to Grafana so so they the people   who were looking there before they they went to 
to Grafana now so we had a new home for for that   or for everything basically so Yeah excellent all 
right an ether like where where is it that uh you   know you see AWS being successful in these kind of 
conversations what are the sort of the values that   um organizations Yeah get from working with 
you um on choosing yeah yeah when it comes to   choosing choosing the platforms choosing the tools 
which to adopt that sort of I mean uh developers   love our platform right because we are building 
blocks you you bring in any open-source technology   use our infrastructure and um rest like how you 
want to take it forward um even though we have   uh you know specific services for each and every 
um should I call it as domain or specific areas is   uh we always first ask what customer is trying 
to solve then we work backwards from that uh   it doesn't start from technology it starts 
from the challenge that you want to solve and   then choose the technology wisely like which 
uh services that you want to pick um yeah um and for Canari yeah I would say it's the same 
that you mentioned Senita that we start not   with technology but rather the the business goal 
uh and when we come to the stage to choose a tool   uh we look at four main areas when we choose 
a tool for a customer if they don't have a   preferable one um the first is like the core 
observ ability functions in the tooling like   monitoring alerting and tracing and the second 
one is the ease of use for the intended user   like is it an intuitive interface is it 
accessible features um or what has this   person worked with before uh knowledgeable um 
the third one is the ease of integration to   other tools in the observability stack so we 
look at how it supports APIs and and plugins   um and the fourth one I think I said three the 
fourth one is that we also look at performance   how it performs uh certain gaps or potential 
improvements nice excellent all right so now   I'm going to ask you to pretend that rather than 
being a microphone that this is a crystal ball   and you're able to see into the future and where 
do you think observability is going what do you   think are some of the next kind of changes that 
we'll see in the observability uh ecosystems that's a good question um if I look into my 
crystal ball um I see a lot of developments   in observability so it's hard to choose one um but 
I'm going to go with um that I see now especially   when we speak with customers as well that we see 
um observability being more and more integrated   with security so security being a very big topic 
today uh with a lot of different regulations and   other stuff uh we see observability and security 
coming more and more together um and even in   the future to create a more full stack cyber 
resilience to get like real time threat detection   forensic analyszis and all that stuff so I see 
that as a as the biggest part y sne how about   you uh I think we already saw a preview from one 
of the demos earlier i think Riichi one showed us   uh um using LLM it gave you the contextualized 
remediation steps uh because it was hard to   understand just to look at the traces but then 
this leads to think about uh you don't have to   rely every time on a specific team uh if if the if 
if any security incident that has happened or any   type of concerns um uh that you want to remediate 
instead of picking that specific person you know   just looking at the troubleshooting steps and the 
remediation that it gives step-by-step things that   that we get from LLM you anyone should be able to 
go and rectify it right so that's one thing that   I could think of um on the on the buzz word these 
days with generative AI I think it has become in   our vocabulary uh the other one is um when we 
think about proactive approach it's also uh how   we can make it more agentic uh like self-healing 
um of course it's hard to make it zero touch even   though people mentioned we are trying to aim 
for zero touch um I slightly disagree on that   uh maybe less stats like maybe uh use less 
number of time sorry less number of hours or   uh reduce minimize the time in order to remediate 
those things so yeah I think that's that one that   one's particularly interesting because you know 
we hear developers using you know generative AI   tooling for example and then spending much much 
longer looking at the PR request because they're   not quite sure they trust it yet um so yeah we'll 
see see how that continues to develop but yeah I   think um what we want what we're trying to 
do right now is to get more of the those   uh tracing spans in that we talked about earlier 
that you want the whole chain and end to end chain   so so in instrumenting for everything um is is 
one of the things that we're looking into right   now to achieve um and then I think also using 
um um profiles profiling um that we can then   um connect it to the actual code and I also was a 
bit fascinated about the prospect of having a bot   going into the actual code and and make the PRs 
for how to optimize the code based on what it it   could find so yeah looking forward to that yeah I 
I for example am an absolutely terrible developer   and uh I've found generative AI to be genuinely 
very useful um to clean up the garbage that I   tend to produce um on occasion but so if if we 
looking at uh looking at this we've we've had so   many different conversations today um what would 
be sort of the one the one recommendation that   you would uh suggest that folks um sort of take 
on board when they're sort of considering their   observability journey well I think it is to um 
you have to have buy in of course you need and you   need to go both from top down and and bottom up 
and to to get in contact with a developer team for   example that is really um um into observability 
get them on board and then show something quickly   to to the leadership team this is what we can 
achieve and it actually has real world impact   on on on the customer experience and that makes 
them very interested and um and then you get the   um culture change stuff as I as I said you bring 
Gafana there and you have some uh some interesting   u seminars uh maybe um yeah uh Maybe the observ 
the champ the champions thing I think is is really   important to have one in each team that can be 
a sort of an knowledge center for that team that   they can go to and they can assist others and 
they can and also bring the POS on board as I   also mentioned earlier that they would actually 
prioritize things like observability and not just   um features for the business so yeah that that 
would be my recommendations excellent excellent   how about you what are your recommendations 
um it depends on the personas as well to whom   I'm giving uh but mainly I mean developers we are 
all you know you guys or we are always updated on   uh um the the tools and services that 
has that that that is in the market but   uh for me I want to address more on the 
management side sea level uh executives uh   It's it's a mindset change from what happened 
instead of uh thinking about what happened go   for what if this happens uh ask certain questions 
to your IT team is your is our system ready enough   to you know if there is any outage that are we 
prepared enough for that so ask those kind of   questions that then you will have you know right 
tools and place right tools and services in place   um for someone who starts on the observability 
journey fantastic and Sarah yeah my big uh tip   goes back to the challenge with the people um 
so my tip would be to really get the people   together and create a strategy and vision and a 
crystal clear goal of where do we actually want   to go on a business level and then scale down 
to okay what do we actually need to do today   um because observability to me and to us is more 
like a like a mindset and a way of working and   uh you know and you have need to have those 
strategies and processes in place to actually   succeed uh because we see a lot of companies 
like getting the observability tool and then   it goes one year and it has just been sitting 
there and no one knows what to do and what you   have mentioned a lot today as well like getting 
the buy in uh so really start with the people and   create the same strategy and so everyone knows 
also what's going to happen because that also   happens that people are like whoa what is this 
what are we going to do now you did something   so get everyone on the same page um so you're 
working towards a common vision and goal and   um that's actually where companies comes to Canary 
as a partner to Graphana uh to get help with as an   independent curator get help with where should we 
start with strategy and processes so We help the   customers and the companies with the strategy 
and everything from people like collecting   everyone in the same room and having interviews 
um to processing and tooling to their desired   state of goal because everyone is different 
and need different things um and we actually   have a lot of customers that went from a siloed 
monitoring team and are now working in a fully   scaled observability mindset and processes uh but 
that also took time you know like you mentioned   it's a journey uh it's a marathon not a sprint so 
remember that as well yeah that that phrase it's a   marathon not a sprint is one of my favorites and I 
use it all the time and it's it's absolutely true   especially with things like this so please 
give a round of applause for our panel here [Applause]

