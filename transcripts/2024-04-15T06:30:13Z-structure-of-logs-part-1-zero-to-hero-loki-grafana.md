# Structure of Logs (Part 1) | Zero to Hero: Loki | Grafana

Have you just discovered Grafana Loki? Zero to Hero: Loki is a series of videos that aims to take you through the basics of ...

Published on 2024-04-15T06:30:13Z

URL: https://www.youtube.com/watch?v=cnhnoFz6xu0

Transcript: Welcome back! My name is Jay Clifford and this 
is Zero to Hero a beginner's guide to Loki. In   the last episode, we answered a couple 
of questions about logs; What they are,   their origins and what problems do they solve 
and create. In this episode we are going to look   a little deeper into how a log is structured; 
think about basic log components, formatting   types and standardizations. We have a 
lot of ground to cover so we are going   to split this lesson into two parts. Part 
1 is all about the components of a log. We can image log components as the Lego blocks 
that create a log entry. They are modular,   some are necessary and others are optional but 
build greater context. We will start by breaking   each of these building blocks down. In the last 
episode, we described a log as being akin to a   diary for a computer or application. So what is 
the key component of a diary that differentiates   it from just keeping a list of notes about your 
life? The timestamp. The timestamp ankers our   event to a specific moment in time. Timestamps 
provide us with a huge amount of context. This   is the same for logs it allows us to compare, 
contrast and correlate different log sources,   and metrics which share a similar timestamp. 
For instance, the system log is warning us of   critically high memory consumption, at the same 
time we can see a sharp and climbing trend within   our memory usage metrics this typically indicates 
a memory leak within one of our applications,   we can then jump to our application logs to 
check for potential route causes around the same   period. Timestamps within logs typically follow 
the ISO 8601 format and vary in granularity;   anywhere from seconds to nanoseconds. Now it's 
not a given that all logs will have timestamps,   as you will see in the demo later, but 
it is a best practice to include one. Next is the log level which can also be referred 
to as the severity level. We can imagine the log   level to be like signpost’s along a road. A 
signpost's colour and shape usually indicate   how important the message is for us to read 
and they typically come in 5 major flavours;  Debug: Imagine this as the white or informational 
signposts on a road, indicating non-critical   information like historical landmarks or scenic 
areas. In logging, DEBUG messages are similar:   they provide detailed contextual information 
used during development or troubleshooting.  INFO: These are akin to the blue signposts 
indicating services or facilities, such as   rest stops or gas stations. They are informative 
but not indicative of any problem. In logging,   INFO messages communicate normal, expected 
events within an application, like successful   initialization or routine operations.
WARN: This is comparable to the yellow   or cautionary signposts warning of potential 
hazards ahead, like sharp bends or merging   traffic. In the context of logging, 
WARN messages alert to situations that   are not errors but could potentially lead to 
problems if ignored. For example, deprecation   warnings or unexpected system states that don't 
prevent operation but might require attention.  ERROR: These can be thought of as the 
orange signposts alerting to more immediate   or significant issues that need attention, 
similar to road construction signs. In logging,   ERROR messages indicate problems that have 
occurred which affect the operation of the   application but might not necessarily halt 
its functionality. These are issues that   require prompt attention, such as failed 
operations or data processing errors.  CRITICAL: This corresponds to the red 
signposts that demand immediate attention,   such as Stop signs or Wrong Way 
alerts. In the world of logging,   CRITICAL messages signal severe situations 
where the application might be unable to   continue running. These are the highest priority 
messages indicating catastrophic system failures,   security breaches, or other critical events 
that need immediate and decisive action.  Log levels are important to remember when we learn 
how to parse, tag and ingest logs within Loki. The final basic component of a log 
entry is the message itself. This is   a human-readable description detailing 
the event that took place. The contents   of this message can vary greatly 
between log sources. The message   might also include identifiers such 
as User IDs and transaction IDs. Now there are some special credit components 
to logs. It is worth noting that these are   not standard across all logs but can 
improve cross-referencing within log   aggregation solutions. These can include;
EventID - Unique identifier of the type of   event being logged; such as an API exception
Source or Component - Commonly found within   distributed systems identifies the application 
or system that generated the log entry  Context Infomation - This is mostly metadata 
which can help with post-event debugging.   Think about the state of the system 
and the values of relevant variables.  TraceID - This could be linking a log to a 
specific transaction between systems within   a microservice architecture. We aren’t going 
to dive too deep here yet as this can muddy   the water between Tracing and logs. We will 
cover this potentially in another video. Let’s quickly recap what we learned. You can 
imagine log entries like a Lego set and the   components like blocks. Some of the blocks are 
more necessary than others such as timestamp,   severity level or message. Then some 
are optional but provide a more detailed   overview of our application or system such 
as; state, source, event type or traceID. In   part 2 of this lesson we will cover how these 
building blocks can be assembled together and   represented to the user. Until next time make 
sure to check out our Grafana for Beginners   series and the previous episode's intro to 
logging. Thanks for watching, stay curious.

