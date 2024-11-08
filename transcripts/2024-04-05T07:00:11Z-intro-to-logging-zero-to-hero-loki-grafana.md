# Intro to Logging | Zero to Hero: Loki | Grafana

Have you just discovered Grafana Loki? Zero to Hero: Loki is a series of videos that aims to take you through the basics of ...

Published on 2024-04-05T07:00:11Z

URL: https://www.youtube.com/watch?v=TLnH7efQNd0

Transcript: Hello and welcome to Zero to Hero a beginners 
guide to Loki my name is Jay Clifford and I   am a Developer Advocate here at Grafana Labs. 
Our ultimate goal for this series is to take   you from zero to hero learning the ropes of 
Loki, a log aggregation solution inspired by   Prometheus. But before we get down to the 
nitty-gritty let's answer the question;   What are logs? It may seem trivial 
to some but understanding the what,   why and how will provide the foundation for 
understanding Loki’s architecture and feature set. So where did the term logs in computer 
science come from? Interestingly the   term predates computers and involves actual 
logs found in nature. The term log comes from   the nautical term logbook used to record; 
distance, speed and navigation at sea. This   was literally done by throwing a log overboard 
to measure a ship's speed through the water! In computer science, we can imagine a log is 
like a diary for a computer; what you did?,   where you went? And did any strange events 
occur throughout the day, becomes what program   or process did you start? Did you complete a 
task? Did you encounter any errors or bugs? As engineers, we care about these logs as they 
help us monitor the actions of our servers,   applications and systems. When 
things are going well we keep an   audit of their usual behaviour 
and when we encounter bugs or   errors we can use logs to investigate 
a potential root cause of the issue. Here are three examples of logs; System 
Logs, Application Logs and Security logs. System logs; An encompassing record 
that tracks the overall health and   status of your computer. Examples 
here could be a record of software   update cycles or system errors such as 
an OS crash or hardware malfunctions. Application logs; are produced by programs 
or agents running on your system that keep   records of their actions. In most cases 
the level of detail within these logs   is configurable but we will discuss 
this in more detail in a later video. Lastly Security logs; They 
keep track of events such as   login attempts, password changes, 
and unauthorized access attempts. So how are these logs generated? Where 
do they end up? How can we access a log? As we now know logs are generated from a variety 
of sources such as our systems or applications.   Let's take a look at how application logs are 
created. Imagine we are building a massive   online multiplayer game called QuestWorld. 
In QuestWorld, you roam around with other   players fighting monsters and completing 
quests. As the developer of QuestWorld,   you will likely ochesterate your code with print 
messages to command line. This allows you to   easily identify if your application is running 
through procedures successfully. As you to start   to productionize your code these print messages 
will be replaced with a logging framework. Logging   frameworks are packages which help to simply 
the creation of logs for your application. There are many logging frameworks outhere 
but the concept is universally the same;  You create logging calls throughout your 
application code to capture events. This could be   capturing when a user logs into QuestWorld, when a 
user accepts a quest, or if a specific action has   failed; a user has tried to complete a quest but 
we failed to return the reward list to the user.  In the next video, we will discuss more 
specifics of what you can include within   a log such as severity level. For now, it's good 
enough to know that when our application acts it   leaves a breadcrumb trail of these actions.
So where do all of these “breadcrumbs” go?  In a lot of cases, these end up in a log file on 
disk. Each event is appended to the end of the log   file. These files can normally be found with the 
.log file extension within your computer system.  Let's take a look at an example of where you 
can find some common logs. We have created a   sandbox instance of an Ubuntu server. You can 
find this in the description below. Let's open   up the sandbox and locate some logs. A common 
place for logging files within a Linux system   is within the logs directory which is located 
within the var directory. We can run the command;  ls /var/logs to show us a list 
of files within the directory.  Here you can see system and application 
log files. We will teach you how to open   and understand these log files in the next video. So you must be wondering if log files 
are stored on disk why do you need a log   aggregation solution for your logs? Logs although 
incredibly useful do present several challenges; The first is storage; Applications and 
systems can generate vast amounts of logs   which makes long-range storage of these 
financially impractical. Imagine if your   office produced one filing cabinet a day and you 
needed to find a location to continuously store   these cabinets without obstructing the space 
required by everyone working in the office.  A secondary issue is analysing these log files 
for useful root cause analysis. Imagine you were   requested to find a specific office event 
within the filing cabinets. You have been   told a few dates on when this event could 
have occurred and you now need to search   maybe 5 to 10 cabinets. Now imagine you have been 
asked to see if there is a pattern of this office   event. As you can see, manual investigation 
of logs is extremely difficult to scale.  Lastly is locality; in a modern system 
architecture like our QuestWorld,   we would usually be building our solution using 
microservices. Lots of smaller applications each   with their specific role and task all 
communicating with one another. These   services can be spread over 1 to many 
servers using deployment platforms such   as Kubernetes. This means we might have many 
different applications and servers all writing   their logs in different locations. Each log 
might contain a clue to solving the issue so   we need a way of bringing these logs together. 
Finding a way to bring these logs into a central   location for analysis can help us build a bigger 
picture of events occurring within our solution. This is where log aggregation solutions such as 
Loki come into play and later in this series,   we will learn about the features and services 
within Loki that tackle each of these issues.   In the next episode, we will be delving a 
little deeper into the structure of logs;   looking at log structure, format types 
and why does log standardization matter. Until next time I highly recommend checking out   our Grafana for Beginners series which you 
can find in the description below. Also,   make sure you join our Slack and Discourse 
community. Thanks for watching, stay curious!

