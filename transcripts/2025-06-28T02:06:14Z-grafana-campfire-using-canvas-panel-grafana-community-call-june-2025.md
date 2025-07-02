# Grafana Campfire 🔥- Using Canvas Panel (Grafana Community Call - June 2025)

Published on 2025-06-28T02:06:14Z

## Description

canvas #grafana #oss In this Campfire Community Call, we will talk about one of the most dynamic panel that provides freedom ...

URL: https://www.youtube.com/watch?v=zKYZjG_3Axk

## Summary

In the June edition of the Grafana Campfire community call, host Usman Ahmed, along with Grafana team members Matt Ryer, David, and guests Adella, Drew, and Ehore, introduced and discussed the dynamic Canvas Panel feature in Grafana. This innovative tool allows users to create visualizations that go beyond standard charts and tables, enabling the representation of complex data in a more artistic and interactive format. The discussion covered the history and evolution of the Canvas Panel, its various use cases (including IoT applications and custom dashboards), and the latest features such as data links, customizable elements, and improved panning and zooming capabilities. The team engaged with audience questions, demonstrating the functionality of the Canvas Panel and encouraging community contributions to enhance its capabilities further. The call wrapped up with excitement for the future of the Canvas Panel and a commitment to ongoing development based on user feedback.

# Grafana Campfire Community Call - June Edition

**Date:** June 2023

---

**Usman Ahmed:**  
Okay, we are live! Thanks everyone for joining in. Hello everyone, and welcome back to the Grafana Campfire community call, which is the June edition. Today, we have something very interesting that is not just your normal time series, bar chart, or table panel. We will be discussing the **canvas panel**, a very dynamic and flexible tool that allows you to create visualizations or, quite frankly, art!

We are going to learn what the canvas panel is, what we are building, and what the future looks like. We also have some demos lined up. 

I'll start the call by introducing myself. My name is **Usman Ahmed**, and I am a staff developer advocate at Grafana Labs. I am part of this Grafana Campfire community call, which is really cool. But we also have two pioneers here who have been running the call much longer than I have: **David** and **Matt**. Maybe you can introduce yourselves?

**Matt Ryer:**  
Sure! I’m **Matt Ryer**, a principal engineer at Grafana Labs currently working on the assistant project—an exciting area involving AI and machine learning. I have never used the canvas panel, so I’m here representing the newbies. I’m keen to learn more about it, and I’ll try to be slightly humorous, even though I’m getting over a cold, as you can hear in my voice. By the way, if you don't have a headache, take a moment to celebrate it! I only focus on it when I have one. 

**David:**  
I’m **David**, and I run the Grafana team. I’m excited about the canvas panel. Essentially, since day one, we’ve seen a lot of great use cases for it. Back to you, Usman, to introduce our guests.

**Usman:**  
Definitely! Today, we have three amazing guests, which is a surprise because we usually have two. I think this call needs more attention because the panel is so amazing. 

Let’s start with **Adela**. Can you please introduce yourself?

**Adela:**  
Sure! Hi, I’m **Adela**. I’ve been with Grafana for a bit over three years now. I have been in the database squad in different forms and shapes, and I’m really excited to be here. I’ve been working on the canvas panel pretty much since the beginning, so it’s been a nice ride.

**Drew Labodnik:**  
Hi, I’m **Drew Labodnik**. I’ve been on the data visualization squad here at Grafana for just over three years. Similar to Adela, I’ve watched the canvas develop over the years, and I’m excited to see what it turns into.

**Ehore:**  
Thank you, Drew. I’m **Ehore**, a front-end engineer in the data visualization squad. I’ve been at Grafana for about two years. I love talking, and that’s why I’m here. I’m happy to answer any questions.

**Usman:**  
Thanks, everyone, for the nice introductions! I think this is the most detailed introduction we have had in a long time, which is cool. Let’s talk a little bit about the canvas panel. 

When the canvas panel was launched, I didn't know the history either, so I’ll be along with Matt as a newbie. I have used the canvas panel by learning from the community. Once it was launched, it was a big hit, and people loved it! However, there were also a lot of questions around it, which I think we will get answers to.

**Matt:**  
I have a question to start with: What is the canvas panel?

**Usman:**  
That's a good question! Who can tell me what that is?

**Drew:**  
I can try to explain. We have our general standard panels, like state timelines and time series, but sometimes you want to do a bit more. You want to visualize your stories in a way that can be understood by others—not just points on a graph. That’s how the canvas started. It’s a great way to overlay your data on something that can be visualized, like a piece of graphics.

**Matt:**  
So it’s not just an HTML canvas element, is it?

**Drew:**  
No, it’s a bit more than that. We have SVGs and HTML behind the scenes. We have a scene class with a tree structure of elements and connections, allowing for many use cases in the wild.

**Usman:**  
That’s great! So it’s like a framework on top of the HTML canvas that people can use to build their visualizations.

**Drew:**  
Yes, and it’s user-friendly. You can add elements, drag them around, resize them, connect them to create flowcharts, and visualize complex systems. It allows users to overlay their data intuitively.

**Matt:**  
Did this come from people asking for specific features that didn't make sense to build into the library but made sense for their use cases?

**Drew:**  
Absolutely! People are very creative and have many use cases. Initially, this started as an IoT use case when everyone wanted floor plans of factories or shops. Flowcharting was also a big request. We respond to these requests. 

**Usman:**  
That’s something I find cool about Grafana: the community really influences a lot of what happens by getting involved and building things. 

**Drew:**  
Exactly! The community makes sure our tools are relevant. 

**Usman:**  
Should we learn more about it?

**Matt:**  
Yes! Does anyone know when it was launched? Was it with Grafana 10?

**Drew:**  
It was generally available in Grafana 10, but we had some previews before that.

**Usman:**  
Should I share the slides now?

**Drew:**  
Yes, let’s have a look!

---

### Presentation: Canvas Going Beyond Standard Panels

- **What is Canvas?**
  - The first PR for Canvas was in September 2021 by Ryan.
  - Initially, there was one element: a text element.
  - It’s a storytelling panel where you can drag and drop things around.
  - The alpha version was released in 9.5, and it became generally available in Grafana 10.

- **Use Cases:**
  - A pizzeria visualizing pizza ovens and orders.
  - A shop floor layout.
  - Monitoring electric car charging.

**Usman:**  
Can we go back to that pizza slide? I think that one is phenomenal.

**Adela:**  
Yes! It has a background image with text components layered on top. The pizza is animated; the crust color changes as it cooks, and we have a timer.

**Usman:**  
That’s fantastic! I can see how someone could use it to monitor solar panel usage, for example.

**Drew:**  
Exactly! Imagine a pizza shop using it on a screen to track orders. It helps build custom software with the canvas panel.

**Usman:**  
Let’s talk about the core structure. 

**Drew:**  
Each element has a series of anchor points around it that can be connected. You can modify connections by dragging vertex points, allowing you to visualize flows, whether they are data or physical materials. 

**Adela:**  
You can also customize graphics in your canvas panel, using custom images and vector graphics. You can set a background image for the entire canvas and individual elements, opening up many possibilities for complex systems.

**Usman:**  
That sounds great! 

**Drew:**  
In addition to images, you can use vector graphics and custom SVGs in your Grafana instance.

**Adela:**  
Let’s move on to some cool tips!

---

### New Features

- **Tool Tips, Data Links, and Actions:**
  - Improved tool tips include the element name, data value, and timestamp.
  - Data links allow for clickable interactions at the element level, enabling drill downs to other dashboards or documentation.

**Adela:**  
Now every element can work as a button to perform actions, and we’ve added one-click functionality.

**Ehore:**  
I’ve been working on pan and zoom features. We’ve improved this experience significantly!

**Adela:**  
The UI is very intuitive. You can easily attach things and maintain a natural workflow.

---

### Q&A

**Usman:**  
Let’s move to Q&A! We have questions from the audience. 

1. **How do we start using the canvas panel?**  
   - Adela can demo this for us!

**Adela:**  
To add the canvas visualization, you create a dashboard and select the canvas option. You can select fields and create data links at both field and element levels.

2. **How to use data links with canvas dynamically?**  
   - You can tie data links to template variables to create dynamic connections.

3. **Can we add our own images to the panel directly?**  
   - Not currently, but you can point to URLs where your images are hosted.

---

**Usman:**  
Thank you, everyone! This was an informative session on the Grafana canvas panel. The future looks bright with the new features being developed. I appreciate everyone joining in today. Hope to see you again in the next community call. Bye, everyone!

**Everyone:**  
Thank you! Bye!

## Raw YouTube Transcript

Okay, we are live. Thanks everyone for joining in. Hello everyone. Uh welcome back to the Graphana Campfire community call which is the June edition. And in this call today we got something very interesting which is not just your normal time series or bar chart or table panel. A panel which is very dynamic and very flex flexible I would say. Yeah. uh which allows you to create some visualization or create actually an art. So we are talking about today all for canvas panel where we have some amazing people who are joining in today and we will going to learn what is canvas what we are building and what the future look like and we have also have some demos. So yeah I will start the call by introducing first myself. So my name is Usman Ahmed and I am a staff developer advocate at Grafana Labs and uh actually I'm part of this Grafana campfire community call which is cool but we have two pioneers here who are running the call much longer than me. So David and Matt maybe you can introduce yourself. I can certainly have a go. My name is Matt Ryer. I am a principal engineer at Grafana Labs currently working on the assistant project another AI uh kind of exciting agentic things there future machines which is a very cool area to be working in. I've never used the canvas panel so I'm here representing the noobs. I'm keen to learn more about it and I'll also be trying to be slightly humorous even though as like a hero I'm getting over a cold as you can hear in my voice. Um, but I, you know, I don't have a headache, which is lovely. And by the way, if you don't have a headache, like just take a moment to celebrate it because I only focus on it really when I have a headache. But the best time is when you don't. So, I'm just saying like take a minute to appreciate that. And that's my introduction to me. Yeah, I don't have a headache right now. I mean, I might get one later, but we'll see what happens. This episode develops. Yeah. No, I'm David. I I run the Grafana team. Um, and yeah, excited about the canvas panel. Essentially since day one, there already seen a lot of great use cases. Um, and yeah, maybe back to you Osman to introduce our guests. Yeah, definitely. We have some uh actually today three amazing guests, which is a surprise because we normally have two, but I think this call needs some more attention because this panel is also so amazing. So um uh I start with Adila. maybe can you please introduce yourself?
 Sure. Hi. Uh I'm Adela. I've been with Grafana for um almost no a bit over three years now. Um I've been in the database squad in different forms and shapes and yeah I'm really excited to be here. Uh I've been working u on canvas pretty much since the beginning. So it's it's been a a nice ride. Alendrew. Hi, I'm Drew Labodnik. I've been on the data viz squad here at Graphfana for just over three years. Uh, similar to Adella, I've watched Canvas develop over the years and um, excited to see what it turns into. Over to you, Ehore. Thank you, Drew. Um I I'm front end engineer in data visualization squat. um about two years in a graphana. Um a bit uh stuttering, but um uh love talking and that's why I'm here and I'm happy to answer any questions about uh uh over to you Yeah, thanks. Thanks everyone. Thanks for the nice introduction. I think this is the most detailed introduction we have ever get after a long time which is cool. Uh yeah, I think we can talk a little bit about canvas panel. So I think when canvas panel was launched, I don't know also the history so I will be along with Matt like I'm a I'm sort of a newbie. I have used canvas panel basically by learning from the community because once this canvas panel was launched it was a very big hit in our community and obviously they they were using it they love it there also a lot of questions around it which I think we will uh going to uh get some answers uh and uh but maybe if someone Oh Matt you want to say something?
 Well I have a I have a question I think a nice one to start with. What is the canvas panel? That's a good question.
 Yeah. What is it? I've got an idea, but who can tell me what that is? Again, I can try to explain what it is. Um, so, you know, we have our general standard panels, you know, um, state timeline, time series, but sometimes you just want to do a bit more than that. Um, and a good idea it's you want to visualize your stories. You want to do a a story line and you want to do it in a way that can be visualized by others, not just, you know, points on a graph. M
 and I think that's how how canvas started um as a great way to you know overlay your data over something that can be visualized like a a piece of graphics right? Yeah. And so it's it's not quite just an HTML canvas element is it? It's not as simple as just giving a programmer that. It's not it's a bit more than that. Um we have obviously we have SVGs, we have we have HTML clearly um behind the u behind the scenes. Um but we do have a scene class which has like a structure like a tree structure of elements of you know connections and you can do just so many things with that. We have so many use cases um out in the wild which are great and yeah people have really embraced that.
 Nice. So it's like a framework on top of that HTML canvas that people can use to build their visualizations. Yes. And it's very user friendly. You can add elements, drag them around, resize them. you can connect them together to create flowcharts and really visualize complex systems, complex layouts. Um, and then as Adella said, overlay your data on top of that to really get a good intuitive sense of your system. Yeah, sounds great. And presumably this came from people asking for spec really specific things that it wouldn't make sense to build and have as part of the library but certainly makes sense in their particular case. Were there a lot of people wanting this kind of thing? Believe so. I think people like you know they are very creative and they have lots of use cases and I think initially this started as an IoT use case when you know there was the IoT boom when you know everybody wanted I don't know a floor plan of a factory or you know a shop or something like that and flowcharting also a big use case that there was need for that so we responded Um surprisingly we have a lot of request uh people want to build tables inside Canvas which is kind of controversial but we are listen for for every uh voice. So yeah. Yeah, that that's something I I find cool across a lot of Grafana stuff is that the community really do influence a lot of what happens um by getting involved building things and and being part of the conversation. I've seen that a lot of examples and and I think that's kind of great and it's also what helps make sure our tools are relevant as well. So yeah um the yeah this sort of I already now want to go and play with the canvas tool. Um should we learn more about it? Yeah, I think one one question just just from my side. Does anyone know like when it was launched? Was it launched with Graphfana 10 or uh a bit more earlier? It was generally available in Graphfana 10, but we had some previews before that.
 Yeah. Yeah. Cool. Uh uh should I share the slides now? Is it okay?
 Yeah.
 Yeah. Okay. Yeah. Let's have a look.
 Yeah. So this is canvas going beyond standard panels. As as we said before this is not time series. This is not state timeline. This is a bit different. And you know in this presentation we're just going to go over what canvas panel is and why it exists which we already kind of touched a bit on that. Um we're going to show some cool use cases. Um we want to talk a bit about uh the core structure you know elements connections. Um we're going to touch a bit on the latest features. Um and you know we're going to have a sneak peek of what's ahead and then we're going to have some time for the Q&A. Um, so why canvas? As you can see on the on the right side, uh, that's the first PR for Canvas, which was in September of 2021, um, by Ryan. Um, we had one element which was a text element and, you know, it's a storytelling panel. we can drag and drop things around and we I think initially we needed the way to um expose explicit content over smaller elements and yeah we had it released um as an alpha version in 9.5 and it was generally available in in graphana 10 which was um you know a big milestone for us and yeah there are lots of cool use cases pieces of you know canvas in the wild. We have a pizzeria um like pizza ovens and you know orders. We have um a shop floor. You know you can even visualize how you know your electric car is charging and you know you have your factories and all elements.
 Adela can we just go back to that slide? I just want to have a quick look. Look, look at that pizza one. I think that that one's phenomenal. So,
 is that like an image uh in the background and then the text components layered on top? Is that how that works? Yes, we have I think we have a background and then we have a couple of uh elements. I think the ovens are the elements. You know, we have an animated Unfortunately, this one is not animated, but it is animated in reality. just cannot be seen on the slide. Um you know the pizza is changing like the crust color.
 It's it becomes more colored when the um when the pizza is almost ready. We have a timer and then you know there's Yeah.
 Yeah. That's so good.
 People are Yeah. People are really creative and it's it's really amazing to see what they can come up with.
 Sorry.
 Sorry. Yeah. No, I I'm just also amazed like I think one of the major use case I can see like uh in in like if someone is using like in-house electricity like solar panels for example uh they can definitely use canvas panel to monitor the uh usage and everything. M yeah I mean it's really good and you imagine in the pizza shop then somebody has that on a screen where they which they're using to track or so it's kind of like
 yeah great built their own custom software just by using the canvas panel. Yeah. Um okay so I think we want to talk a bit about the core structure. Um and as I said before we have a scene class which has like a a tree structure of all the elements and you know the elements have properties or options as as we say now uh background color text you know all these things you can do you know the animations depending on the element type and you know the properties can be fixed values or title data which this is probably the most powerful um you ability of canvas. You can actually tie your data to to the elements and you know and um you know we've we've tried we've looked into doing our own logic but it would just take well too much time. So we handle um selecting and moving the elements using two libraries movable and seleto which are really great and um you know the developer is really responsible responsive and you know we've had a really great um experience working with him in in some cases um you know elements and connections. Um we have two types of elements standard and experimental. The standard ones are, you know, the a rectangle, a triangle, an icon. And then we have a bit more advanced um or experimental uh elements which you know there's a drone, there's a button, there's a windmill and uh I think something that we want to mention here because there's something that has come up a lot in the past and I think it's still it's still something that people are asking about. it's um how can someone add custom elements and uh you know we would love to help with that um but I think people have so different use cases that it's hard to find one element that you want to add to the library that you know everybody's going to be happy about. So we strongly encourage people to you know create their own elements, make a PR. We are really happy to review, approve, add it to the library. Um and I know it might be a bit hard to figure out at first how to do that in the codebase and we have you know some example PRs um which are actually adding new elements. Um I don't know should I share that? I have the link here but I don't know if people are Yeah I think uh you can share on the chat should work.
 Yeah. So this is cool. So these are like foundational bits that you can just use. Um the experimental type's interesting. A button I feel like a button has proven itself by now hasn't it?
 Yeah. Yeah. I think so. And what's what's interesting about the button um so initially the button what we tried to do with the button was to allow API calls which is something was something new at the time and what that has evolved into is that right now we've introduced actions and basically every element that we have can act like an you know like a button can do API calls uh which is you know pretty pretty interesting I think.
 Yeah. Um this this reminds me of when I used to in the early days when I was building apps and I would use visual editors like visual basic to lay out the forms that you would build as part of your application um and wire them up in similar ways. You know take the click action and do something run some function or yeah and wire up properties in a similar kind of way. So, it's very sort of nostalgic as well, I think. Um, very very cool.
 And just to add to that, I think that's the ultimate vision is to build an app builder um to really allow customization. Um, yeah, that's a great point.
 Yeah. Uh so unfortunately I have some trouble joining yeah I have some trouble joining the chat but if yeah we can share the the PR with the example and also Drew was nice enough to create a draft developer guide PR um which is kind kind of goes through the steps that you need to to to take to to create a PR with a new element type and yeah as I said we're happy to review and to add it to the library. Um so I think yeah I think that's it.
 I I do have a question. So um on this slide so you mentioned like there are some uh standard which I believe are already available inside graphana uh when when someone installed graphana but are the experimental are also available as well?
 They are yes they are. um is just there's a toggle um so they're not initially displayed in the list of element types. There's a toggle if you toggle the experimental element types then you will see the entire list with with the more advanced one.
 Cool. Yeah, I think when when we come to the uh section of demo, I think that will be really good to show the audience like how how they can um see the advanc or or the experimental ones. Yeah. Yep.
 Thank you. Yeah, Drew, I think you might want to Yeah, happy to to take the next couple slides. Um, we can go to the next slide, please. Next slide, please. Oh, perfect. So in order to build uh flowcharts to represent complex systems or workflows, each element actually has a series of anchor points around it that can be connected to one another. Um each connection can be modified by dragging its vertex points around. Um and really this allows you to visualize the flow between elements whether it's data or physical material. Um as was mentioned the IoT use case before. Um conne the connections themselves can also be customized and tied to data. Um so we can change the color, size, radius, direction of the connections as well as the line style. Um do you want dash lines, solid lines and you can even animate um the connections to help visualize that flow. Um what you see on the right hand side, unfortunately the animation is not showing up here. Uh it's just kind of a peak under the hood at the math and the constraints that go behind uh connections. Um yeah, so next slide. In addition to being able to make connections between elements, you can also customize the graphics um in your canvas panel. So custom images and vector graphics can be used. Um you can set the background image for the entire canvas as well as individual elements. So, as you can imagine, uh this allows, as Adella mentioned, uh the user to be as creative as they want. Um and because canvas allows stacking and layers of elements, um this really um opens up a lot of possibilities. So, this can be particularly particularly useful if you have a complex system. You have an image of a layout, a map, um blueprints, etc., and you want to visualize the state on top of that by overlaying datadriven elements. Um, and then in addition to images themselves, you can also use vector graphics. Um, we have an icon element. Um, and you can use your custom SVGs. Um, anything that your instance of graphana has access to, you can render it inside of canvas panel. So, um, with that, next slide. And Adella, if you want to uh talk about cool tips. Could we just go back to the previous slide? Yeah, because I can I can see the original presentation here. And it's really cool how the little circles around those wind turbines like they are changing color, right? Like I guess like based on some kind of number, right? And it's such a great way to have just a lot of data really narrowed down into this visual way. I I think that's amazing. It's it's a shame that it's not showing. Yeah. And in fact, if you look very closely, you can see the the green dot in the top left corner. So that's actually live streaming data. So that you can really see a a smooth update of the state of your system.
 Yeah. Go ahead. Thank you.
 Yeah. The challenge with this though is once you have that, it's hard to not just look at it all day. Do
 you know what I mean? Yeah. Uh well, I think the counter to that is um if you're looking if your job is to look at a a dashboard for eight hours a day, uh why not look at something beautiful and something that's intuitive? Yeah. But then also when it goes red, you're like, "Oh my god, I got to drive two hours to this turbine." Great. Great. Um yeah, if we can go into the next slide and talk about tool tips, data links and actions.
 Yeah, sure. So um part of our latest features um we've made some improvements um you know on the tool tips um that before they were I think they were appearing only if there was a data link uh and the tool tip was only having the data link inside. So it was pretty, you know, bare. Um, and now it includes the element name, the data value, time stamp of the data point. And, um, pretty hard to notice probably in the screenshot here, but this is our standardized tool tip that you can actually see in uh,
 mostly all of our Sorry for sorry for really interrupting. Maybe can you please explain the audience like what is a data link? Um yeah so the data links we are um we are able to set you know to link something to a data point. Um and it's not it's not a new concept. It's basically we have it in the standard options. Um but this is you know enabling you know clickable interactions and uh for canvas what's new is that before they were just um at field label level in the standard options and what we did was actually move them I mean not move them because they still exist for the for the at the field level but we actually added data links at element level which is something that was uh requested uh in the past. And now every element can have a data link like a clickable action uh that you know you can they can enable drill downs. they can you know redirect to to other dashboards or to other pages you know documentation or um you know things like that uh for each element which is I think it's it's something uh really great and it covers a lot more you know more uh use cases that people were having and uh another thing that's new is the one-click functionality uh so if you enable that option for a data link you can actually click on the element and that would you know interact with the the link that you have set and uh I think we can show later in the demo we have uh a couple of use cases for example you can um you know create a data link that is changing a variable or you can create a data link that you know it's linking another dashboard or linking being you know an an uh an external source and I think that's that's that's really interesting and um another thing that we have introduced in canvas as well is um are the actions which I think I've I've uh mentioned it a bit u earlier uh now every element can actually work as a button can do something, can do an action. Uh it's supported by the by all the by all element types. Uh it has the one-click functionality which transforms each element in a button basically. And when the one click is not enabled, you can um you're going to see the action in a in a tool tip and you can do the action from the tool tip. There's a button over there. Uh, I'm going to show it a bit later. Um, yeah. And I think Ehore can talk a bit about pan and zoom because he's been working on it lately. And yeah, thank you Adela. Um, maybe I can share uh my screen. because my slides are heavily animated and it's it's like a whole point of it. Yeah, you can definitely share your screen. Uh just share it and I I will put it on the stage. Yeah, I can see now. Is it? I I was going to request that. You got to look at the beautiful animation. Yeah. Good job, Drew. Um Yeah. Can you see it? Oh. Yeah.
 Yeah. Awesome. I would like to uh talk uh about work in progress. It's it's still um you know work uh but it will be released very soon. uh we uh fully re reimplement and zoom uh before it's it's kind of yan uh panel and uh there there is a lot improvements uh to And uh we improved and zoom before it was uh mostly imitation of painting and zooming And now we are uh implemented like full working experience like uh you can expect from uh other uh kind of products. Um, uh, we have a feature when you can place element uh, relatively to the bottom or right, not only to top and left corner. And this feature will um um be maintain it even with the enabled pan and zoom. Uh because uh your panel now will represent uh your frame. It's the place where you can position uh your element. So uh when we introduced p and zoom nothing going to change visually for existing use cases it's it's important part
 yeah this is really cool it's really intuitive the the UI and obviously I've built Like I was saying earlier, I've built kind of things and used tools like this and that's it seems really sort of intuitive the the way that you can attach things. Um yeah, so that's that is very cool. It just feels quite natural that that you could that you could do that, you know. So I think that's Yeah, that's a really good good UX there. I like that. Exactly. It's it's going to be like same experience and user don't have to learn it or or anything. Uh we also made few improvements and one of them is uh again it's it's what you expect. It's it's expected.
 Yeah, but it's those Yeah, but those kinds of problems. Yeah, I can see like it doesn't sound like it would be easy to just fix that and get it to follow the rotation there. So, is that like did you have to basically rewrite the rewrite the whole the way that that works or was it just a bug that you could fix? Exactly. It's like uh you expect connection. Stay on the same place. Nothing uh weird happening and yeah, it's it's just uh additional improvement.
 Yeah. Um
 yeah, just go on the arrow and say stretchy arrow. True. That's the
 Yeah, I I I think this this this is really helpful to like create a flow because like I whenever I even like just using any other uh like software for presentation and if I have to draw a flowchart and I just move the element or the box to one place the arrow always broke. So this is pretty cool. This is definitely uh uh a major improvement like to make this rotation and still it remains intact. Really love it. Um we also implement a new feature. We expect that customers would like to build uh big canvases with all those uh factories, floors. Uh um wind power stations. It can be big. And we added uh a small toggle. Zoom to content and your elements going to uh fit to screen. Um, and you finally don't have to manually adjust your dashboard or we we even have a uh customer requests. Uh it's uh depending on your screen size you have uh different results. It's not going to be a problem anymore. Um, yeah, very cool. And again, I can just think of like there's a lot of maths involved in this. I'm sure you're controlling the scale and things, different zoom. Uh, I saw earlier as well when you were zooming in and out. Yeah.
 Um, that's very cool. Yeah. I'd actually love to read a blog post of pressure about that and how you actually did that because I think that could be very interesting.
 It's very cool.
 It It will be. It will be. Yeah. I think I think Matt really uh highlighted it because uh having this feature which are like uh like these are all amazing and it really helps uh uh users who are using our canvas panel once they know like these feature also ex uh uh getting ready and will be available in the in future. Uh having a blog post especially can help and especially also the community because uh a lot of our graphana community uses this panel. So uh they will definitely love it. It will be a big hit. Um exactly. Uh we we also have a plans to uh dynamically programmatically create layouts for for specific use cases. uh uh dynamic uh positioning uh for elements. It's uh uh when you already have the data. How to position elements depend on the uh existing or incoming data. Um, instead of manually dragging or typing the numbers and of course there there is a plan for ad hoc visualization. Uh we we really hope all this improvements are going to give the second life for canvas. and we are looking forward for your feedback and questions. So yeah.
 Yeah, it's so good. Um I think that that is really exciting to see some of those things we've got cooking as well. And we should talk separately about the assistant and how that could also interplay as David mentioned earlier. Um yes, very cool. How many people are making games with this? It feels like there's already enough that you could make, right? It's funny that me and Andrew uh have uh made an effort the last hackathon and it's it's quite of impressive. We we tied it to a live stream database too. So, uh we actually made a a sort of a multiplayer game uh using canvas which was interactive and a lot of fun. Um yeah. Oh,
 the possibilities are endless.
 Where can we play that? Uh well, it hasn't been deployed yet, so hopefully in the near future.
 Yeah, we need to that sounds like priority. definitely can be deployed if on play then uh everyone can play it publicly. Good point
 indeed. Yeah.
 Yeah. Uh we have 15 minutes uh uh before we end. Uh should we move to Q&A or uh or there is still a demo which you want to showcase? Uh probably we can combine both of them. Okay. Okay. Perfect. So I will start posting some questions. So uh for audience who are joining we got some question we can ask also on live chat. Maybe we not be able to answer everything but we will try. So uh I will start with the very first one. Let me just uh paste it here in the comment. So the first question uh how do we start using canvas panel as it looks difficult to create links and connection between elements any examples? Adella did you want to bring up the demo and maybe answer some of these interactively? Yes we can do that. Um okay so probably we should start from the beginning right um how to add the canvas visualization. So we have a dashboard. We're creating a visualization and it's a canvas and by default we have a metric value element which you know we can select the field and yeah we can create a data link which as I mentioned um on the slides we can do it at field level. Um, this is a field data link. And I don't know, it's going to do something. We're going to open it in a new tab. We're going to save it. And then let's also create a data link that's just at element level. As you can see, we can select the element and we have this section of the selected element. And we have all kinds and sorts of you know options here uh placement positioning background and we have these data links and actions we can create. This is level data link and we can open it in a new tab and here's the oneclick functionality I was talking about. Um, but let's just leave it for later. And in order for the tools tip to appear so we can see the data links, we have to disable the inline editing. And you know, there you are. And I don't know what they're too. We'll see.
 Now, Adella, in those links, you can also um add variables.
 Yes. Yes. I have an example here. Um, it's kind of hard to demo everything, but if you see here, we have a data link using variables. And I believe this is element one. Yes. And we can go down here and we can just use the the variable. This is, you know, autocomplete. So, it's going to work like this. And I have this uh variable here that we can um okay do that and we've changed it. Um and then yeah and what else? I think I lost my new panel, but or connections, uh, if you hover over an element, you can see the connection points, the anchor points, how we were calling them, and you can just drag the connection, you know, link it to another anchor point, just leave it out in the wild, and you have it right here. You can select it and you're going to have an option here just like you have for the selected element. You have selected connection and different settings. Again, you can have a fixed color. You can color it from your data. Um and you know you can have change the direction, the style, you can animate it and yeah I think another interesting thing is that you can change the shape which is also something really interesting um and useful I would say. So yeah that's pretty much how you start using it. Um, if anyone has, you know, more questions, if you need more in-depth, um, you know, demos, we can, we're happy to do that. So, yeah.
 Yeah. Nice. I think
 someone
 Yeah. Sorry. Sorry, Matt. You go ahead.
 Well, I was going to I was going to just ask this question. I was thinking the same thing. So, the question here is how to use data links with canvas dynamically. Yeah. So um as I showed here, we have you know these variables that we can we can tie together and you can you know update a variable or depending on the use case and um the other way is you know to link it to a field level data link. Um and yeah that's way it's going to be tied to to a specific u field and field value. So, so for those who do not know what uh template variables are, um I want to draw your attention to the top left of the screen and those are actually being concatenated inside of the URL for that data link. So, Oh, yeah. Great.
 Yeah. Yeah. So, we have them here. Um so, that's and then in in your data link, you had you had that at the end of the URL if I'm not mistake. Yes, it's a it's a basically a query parameter. So, um let me find it. So, we have it var dash um series is the name of the variable and then we have the value but uh it's going to be dynamic. So you can use that to link to other dashboards and drive other variables in those dashboards. So you could really like you could potentially even drill down into um particular pieces of your system. Yep.
 Yeah, that's very cool. So you can build deep links straight into say the drill down apps or something if you wanted to look at specific logs or specific metrics something like that. Yeah, exactly. So we do have this question but this is a very long question and there was a image so uh but I will read it out loud. So the question is I have created a tsx canvas element of a battery that can be tied to a metric similar to the windmill element I think as an example. How can this be incorporated to a larger library of animated elements for others to use? Um Drew, do you want to take this?
 Yeah, I can take this one. Yeah. So, um, we love, uh, the community contributions and we're definitely excited to try to incorporate those into Canvas. And, um, we hear a lot of of users asking for the ability to contribute to Canvas. And, um, as a response to that, we're building out a developer guide to, um, establish some guidelines. And, um, yeah, we look forward to contributions. Um if if you have a an interesting uh useful element type that you want to share with the community um put up a PR and we're happy to review it and um provide guidance from our side. Yeah. Yeah. And oh we we have a live user here and uh there's a question uh can we add our own images to the panel directly from visualization instead of saving it earlier in the image or icons folder. So, not currently. Um, anything the instance has access to uh with a URL can be pointed to. Um, but if you want to upload an image, um, there are some exciting new developments um, in the back end for uh, file storage that canvas will eventually take advantage of. Um, but in the meantime, you'll need to uh, point to a URL or um, as you mentioned include the image inside of the local instance. Ah, but the URL that's that's a good trick then. So all they do is host the image somewhere and then they can use point and put that in the canvas. Ah okay. Yeah.
 As long as long as the instance has access the proper um security and all that good stuff.
 Yeah. Yeah. Makes sense. Uh Adela uh do this dashboard uh is it can can we share this link to our audience it public? Um it is not. So this one is my it's my local. Um we do have a couple of dashboards in in play. So I can
 Yeah, I can I can share those ones. Can we add this one to um to play?
 Of course. Yeah, perfect. I will I will share the link. But uh in the meantime, I think we can maybe we can take one more question. And we still have a few minutes left. Um, okay. Um, I think this is the most uh I don't know if we have already answered. I believe so. But uh let me paste it here anyway because this is the most high demand question. So the question is is it possible to use an animated SVG as an icon in graphana or in canvas panel? Graphana can uh you can. However, you're you're not able to customize the color. Um as was the follow-up question to that. Um yeah, that's uh definitely a great question and I think something we should look into is being able to have more granular control over styling. That's a great suggestion. Cool. Uh,
 can you wire up any properties in the SVG to data? Is that going too far? Uh, not currently. No. Um, yeah, that that's really u where I think we could potentially go. Um though really I think in that case it might be better to break the SVG into separate U SVGs and um control them as individual icons
 because they can be overlaid on top of each other. Um yeah. Yeah, good point. You'd be cool for colors and stuff, but yeah, this is Yeah, this is getting getting to the point where you you could really just build completely new things with this. It's really kind of It's fun because when I was genuinely when I was young, I was really into computers and I had an amigga and the interface was very different. So, I I'd spent time making UI components to make it look like a PC. Uh, so it like make the the taskbar and the buttons and windows and literally draw the the the lines lighter on one edge so it gave that 3D effect, you know. So I just spent a lot of time doing that kind of stuff. So this feels very nostalgic to me for that reason. And yeah, I'm probably going to make a game though. Probably going to use it to make a game. I don't see how I can't. Right on. I look forward to it. I think I think at Grafonicon at Grafonicon someone asked me if we had a Vizio importer. I think that could be interesting. That's something that's definitely uh we've been looking forward to jumping into is importing draw.io or Vizio. Um one of our previous hackathons we uh supported importing DXF format which is a CAD uh open format. Um, yeah. So, that's one possibility as well. I wonder if there's like Mermaid or some other really sort of simple text formats that could be supported because LLMs would be very good at generating those. So, there could be some interesting crossover there.
 Yeah. And certainly at the end of the day, um, all the elements inside of Canvas are JSON. Um, so you could write your own custom script to generate um, a canvas panel potentially. Well, I think the assistant probably can work with that already. Yeah, actually this Friday going to start uh new hackathon and we kind of going to explore the idea of AI generated. So yeah, fingers crossed. Cool. I think we are also out of time. Actually, we have only 1 minute or no, but I think this was really fun. I actually learned a lot about graphana canvas pen and then especially love the new features. what will be uh I think the future definitely looks bright here because uh the development which we are making here is amazing and community loves it. I think uh some of our customers also use it. So this is amazing. Um yeah um I think that's there we will wrap up today. So thank you everyone for joining and for your time and hope to see you again in the next community call from my side. Bye bye everybody. Thank you.
 Thank you. Bye.
 Bye.

