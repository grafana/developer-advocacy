# Grafana Tempo 2.6: New TraceQL features

In this video, you'll see a deep dive demo of new TraceQL features for links, events, and arrays in Grafana Tempo 2.6. Blog post: ...

Published on 2024-09-05T13:54:53Z

URL: https://www.youtube.com/watch?v=aIDkPJ_e3W4

Transcript: hey everyone thanks for joining us we just cut Tempo 2.6 I am Joe Elliot and I'm Jenny and we're going to show you all the new Trace Q features right now uh as always as always we will start with an empty query empty queries are great for uh simply finding anything and I like empty query it's a good place to start but we're going to start showing you of course events we'll start there then uh links and arrays uh events have an intrinsic called name which allows us to find uh an event by uh well name Jenny what would you say the difference between an attribute and an intrinsic is well an intrinsics are just things that are always there as while attributes are custom um key value pairs absolutely so on events there is a intrinsic and you can tell it's an intrinsic cuz we have this colon here so event uh colon is telling us intrinsic name all attributes will have a name so a CL a little query to just start finding any event would be event name not equal to empty and you can see my data set here this is a synthetic data set but we'll have some fun with it has this event uh named mutex acquire which as one might expect would be when a mutex is acquired um and we can see here we've done our query uh we can uh we have our filter and we're finding very quickly a uh an event with the name mutex choir what uh any other attributes or maybe let's let's say any other intrinsics Jenny on the events well we've also added support for um time since start which is a um the time the event start in relation to the spam start time a fantastic intrinsic uh absolutely so uh if we were to for instance to want to find some mutex that perhaps took a moment to acquire versus a mutex that was acquired very quickly uh perhaps a query like this would help so here I'm saying I'm looking using my event name I guess I've still left it as not equal to empty and I've said how long after the beginning of that span did it take for this event to occur and now I'm looking for finding spans that only uh have this event after a few seconds so I can see here this took 2.87 seconds I can kind of jump around to some of these other options here and maybe now I'm finding traces that took a moment due to a mutex issue cool so events they have intrinsics and colon is going to always specify intrinsics they have attributes um which are custom key value pairs as Jenny said and they um yeah and that's it and there are great ways to Mark specific times inside of a span uh what's next Jenny are we doing links or are we doing arrays what do we talk about links links absolutely uh so links like um links like events have both intrinsics and uh these custom key value pairs attributes and we will use an intrinsic to find uh any link essentially so we're going to use the trace ID intrinsic um and I'm going to look for links where the trace ID is not empty uh we can jump here for instance uh and we're going to be able to find any link so Trace ID uh like uh like the name on an event is intrinsic every single link has this it's a very simple way to just go find any link essentially uh attributes also so so I do actually have some link attributes Jenny uh we're going to use these next how can we specify uh an attribute versus intrinsic here right for intrinsics we use the colon and for attributes we are using the dot um syntax so if we're searching for links um attribute we'll do link dot the key of the attribute cool so let's use this job one so I I have this job here this is a purchase on the cart service this job is maybe uh they've successfully gone through the purchase the API returns but we're queuing up a way to email a receip and instead of directly uh creating those spans inside of this we're going to link to a new Trace so let's say I'm interested in debugging some issue with my receipts I can now find any link oops I've spelled this terribly uh any link with this particular custom attribute so um with links we have those spans or sorry we have those attributes and we have those uh intrinsics and we can select all of that uh with Trace ql uh like Jenny said dots for attributes uh colons for intrinsics final new feature what are we looking at arrays absolutely arrays uh I think arrays are most common in the headers have you seen arrays anywhere else uh Jenny um not that I'm aware of it's mostly in the header the HTP header so a lot of the open telemetry clients will uh encode HTTP headers as AR raise even if there's only one value and for a long time in Tempo this was actually impossible to query uh and in Tempo 2.6 with VP park4 as the default uh we cannot do that not only can we query it but we can uh have working intellisense so uh let me grab one of these oops application Jason I kind of did a bad query there so now this is actually an array HP request header accept previously this would have been possible to query in Tempo um but now we can see our a rendered array over here uh if this string appears anywhere in the array if the aray had five or 10 or 30 items and the string was anywhere in it we would successfully uh find the span so we have more explicit array support in the future but right now with Tempo 26 and B par A4 just immediately it's going to work um you can just use your standard equals operators greater than less than all that's going to work uh very with RS uh thank you for joining us a bunch of awesome new features in 2.6 I am super excited to have Jenny here she wrote all of these new features um I have had very little hand in this recently and I am uh very excited that we have other developers making awesome Trace skill features so events we talked about uh links uh links events and arrays and also went a bit into the new Trace ql senta with regard to intrinsics with the colon and attributes with the dot so get excited about trq or sorry Tempo 26 with the new Trace ql features and we look forward to seeing you in 27
