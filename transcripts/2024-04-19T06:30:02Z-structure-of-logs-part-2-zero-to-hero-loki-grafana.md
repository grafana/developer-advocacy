# Structure of Logs (Part 2) | Zero to Hero: Loki | Grafana

Have you just discovered Grafana Loki? Zero to Hero: Loki is a series of videos that aims to take you through the basics of ...

Published on 2024-04-19T06:30:02Z

URL: https://www.youtube.com/watch?v=8_JyqEqaHiw

Transcript: I hope you watched part, this is part 2 
of this two-part episode all about the   structure of logs. My name is Jay Clifford 
this is Zero to Hero a beginner's guide to   Loki. Buckle up in part 2 of this 
lesson it's all about log formats. Let’s quickly recap about what we learned in 
part 1. We imagined a log entry as a Lego set,   with the log components such as timestamp, 
severity level and message as Lego blocks.   If we continue with this analogy, 
Log formats are like Lego manuals,   they provide the method for assembling these 
blocks together and how we represent them to   the end user. In short, like Lego, there 
are many different ways log entries can   be structured. Today we will focus on three of 
the most common types you will see day to day:  Interestingly one of the most common types of logs 
still used by developers today is plain text. It   is the natural successor to print statements 
and provides the most amount of freedom in its   design. Plain text log entries can be appended 
to many different file types. and in general,   be universally opened by most operating systems. 
One of the primary problems with this format of   log is actually due to the flexibility and lack 
of standardization. Essentially developers can   structure logs how they wish which makes these 
types of logs difficult and costly to parse.  Next are structured logs, which you will be 
hearing a lot of in this series. This is where we   take our log components and format them within a 
common data format such as JSON, XML or YAML. The   key benefit here is that it reduces the friction 
of automatically parsing logs with other data   processing tools such as a log aggregator such 
as Loki. However in general, as the complexity   of a log grows within a structured log file it 
can become more difficult for a developer to   read directly compared to a plain text file.
Lastly, the third most common type of log is   an interesting one. Originally designed in 
the 1980’s Syslog is one of the earliest   standards for logging and managing messages 
in a network environment. Syslog quickly   became the de facto standard for logging 
system messages on Unix systems and later   on a wide range of devices and platforms such 
as; routers, firewalls and even some Windows.  One of the primary drawbacks of using Syslog 
within a modern logging architecture is   its limited to ability to represent 
metadata within distributed systems. We have discussed a lot of theories around 
log components and their representation.   What we will do next is check out a small 
interactive demo you can try online to see   how this all comes together. You can find the 
link in the description below. In this demo,   we have created a small messaging board 
application similar to Hacker News or   Reddit. The idea is users can post messages 
and upvote posts they like. We have been good   developers and orchestrated our application 
code with a logging framework. So when we run   different actions within our application 
a log entry is appended to a log file. let's jump into our log file to see how this 
logging framework represents these log entries. We   can see our log entry structure is quite unique, 
a hybrid between plain text and structured since   it utilises key-value pairs. The first component 
we can see is the severity level which currently   shows INFO so our application is in normal 
running conditions. Let's spice things up a   bit and generate some errors by incorrectly 
filling out the forum and see what happens.  Log entries are now being flagged with the level 
error since our application failed to process the   user's entry. As suggested in part 1 of this 
video, the error shows a significant failure,   in this case failing to process data entry but 
does not crash the entire application. We have   also introduced an interesting cross-over of 
metrics into our log called duration. We will   focus on how we can utilise this metric 
in another video. As we move through this   series we will be building up this demo to 
add more interesting components to this log. And with that, we have come to the end of this 
two-part episode on the structure of logs. Now   you might be asking, Jay when are you going to 
start talking about ingesting logs into Loki?   Have no fear this is currently the end of the 
theory content around logs. There is a method   to this madness as when we start to release 
lessons around Loki ingest, setup and query   this theory will help provide the grounding to 
understanding why Loki works the way it does.  Until next time make sure to check out our Grafana 
for Beginners series and join our wonderful   community on Slack and Discourse. Thank you for 
watching, my name is Jay Clifford, stay curious.

