# Mastering Frontend Observability in React with Grafana Faro

In this video, we'll walk you through the steps to instrument a React application with Grafana Faro for comprehensive monitoring ...

Published on 2024-05-28T08:00:09Z

URL: https://www.youtube.com/watch?v=IA_-zkpVhIU

Transcript: hi I'm Tom one of the senior developer Advocates here at grafana labs and in today's video we'll be diving deep into instrumenting a react web application with graan Faro our tool for frontend observability we'll explore how graan farro helps you visualize crucial information such as application performance errors logs and user activity through real user monitoring before we start integrating grafana Faro let's discuss why observing your web application is essential observability helps you understand not just what your application is doing but why it's behaving in certain ways for developers this Insight is crucial for optimizing performance and enhancing user experience one key component of front-end observability is real user monitoring or Rum rum tracks and analyzes how real users interact with your application it captures data like page load times and user interactions helping you tailor your app to meet real world usage scenarios effectively another critical aspect is understanding web vitals these metrics are what Google considers important for a good user experience on the web they include largest contentful paint which measures loading performance first input delay which measures interactivity and cumulative layout shift which measures visual stability within your application by monitoring these metrics you can proactively spot issues that might not surface in a development environment but significantly impact user experience in production this is where graan Faro comes into play grafana Faro provides an integrated Suite of tools designed specifically for front-end applications it allows you to capture analyze and visualize key performance indicators errors and usage patterns in real time farro comes packed with preconfigured dashboards that automatically display these metrics streamlining your monitoring setup and enabling you to focus on optimizing your application based on actual user data far also includes featur for tracking user Journeys and behaviors giving you deeper insight into how users interact with your application and where they encounter issues so with that said let's take a look at how we can instrument a react application using the farro react SDK and then use graffan Cloud's front-end observability to monitor our application's performance okay so you can see here that I have a react application up and running this react application is hitting a third-party API that I have running in the cloud that API is then connecting to the steam store API to return all of the featured games currently on the store we can add any of these games to our favorites and then head on over to the favorites page where we can see any games that we've already added to our favorites we can remove them here and then we can also head over to the search section to search for any games within the steam store however you'll see that if I search for a game here we're going to run into some runtime issues this is going to be indicative of what a user may experience within your application when it's running in production now here I can obviously see the error myself however when a user is using your web application in production you won't necessarily be able to see them running into these issues directly so we're going to need a way to visualize these within our graphon dashboard so what I want to do is I want to instrument this web application so that we can start Gathering some information about things such as page load times time to First Bite see any logs that are being generated and in particular like I mentioned see any errors that users may be encountering with our web application so to do that I'm going to come over to my grafana cloud instance here and then on the left hand side I've clicked into the front end app section you can see here that I'm now in the graphon Faro or front end observability as it's known in grafana Cloud section of My grafana Cloud instance I'm going to create a new application here I'm going to give it a name of folly demo so front end observability demo below that we have this cuse allowed Origins section this is going to allow us to determine what URLs are allowed to push data into our graan Faro collector now since my application is running locally on my machine it's running at Local Host Port 3000 so I'm going to enter Local Host Port 3000 and I'm going to make sure to add the HTTP protocol to the front of this below that we have this default attributes section this is going to allow us to add metadata to any logs events and errors that go into our grao Faro collector by default which means that we don't have to manually add these to anything that we're pushing from our application this allows us to save bandwidth and it means that we can add things that will always be present so for example here I'm going to add an application name parameter and it's always going to have a value of steam store front end so that we can search for that within the logs below that I'm going to acknowledge that this is going to incur some costs to create and then I'm going to press the create button we've now been taken to the front end observability application that's specifically been created for our Folly demo and we've gone to the web SDK configuration tab by default this is going to tell us how to instrument our application by adding some code to the start here I'm going to copy this code block and we're going to make some changes to this you'll note that this is importing from a faral web SDK package however my application is running as a react application rather than a standard JavaScript application so there's specifically a package for grao Faro when you're using react and I'll show you how to do that in a second so we'll copy this and we'll head over to our applications code the first thing I'm going to do is I'm going to import the packages that we need via mpm so let's stop the application from running and I'll run mpm install I'm going to install the grafana farro react package instead of the farro web SDK and then I'm going to install the grafana farro web tracing package with those two packages installed let's paste in the initialization code that we copied before I'm going to make a few changes here so you'll see that again this is importing from the farro web SDK package I'm going to change this so it imports from the farro react package I'm going to remove the farro variable here because we're never going to use that and then down here below what I want to do is I want to instrument our react router so that we can start seeing page load information errors in the context of our individual routs so for example our home favorite search and so on to do that I'm going to import a few things from react rout up here and then I'm also going to import a couple of extra things from this faral react package so I'm going to import the react integration and the react router version then down here where we have our instrumentation section of our farro initialization I'm going to add a new instrumentation here this is going to be our react integration you can see here that I've got a router property I'm specifying the version as react rout version version six and then I'm passing in all of those dependencies that I imported previously you can find all the documentation for how this react integration works on the graffo Faro documentation I'll leave a link to that in the description below but for now let's save this page and we're going to have to make one small change in our app.js file and this is where Our Roots live instead of using the roots component from react router we're actually going to use a farro Roots component so let's remove the import for the roots object here and then let's import Our faral Roots component from our farro react package and then let's save that we'll run the application again with mpm start and now what I want to do is I want to click around in our application a few times just to try and start generating some data here so let's refresh this page a few times we'll head on over to our favorite section let's perhaps remove a couple of favorites here we'll go back and add a couple of things to our favorites and then finally we'll perform a couple of searches here so let's search for Final Fantasy again we're going to get that error message so let's go back to our search page and let's search for broken sword here again we're getting that error message and now what I want to do is I want to head back into our overview tab on our front end observability section of grafana cloud on the right hand side here I'm going to change this dropdown to be every 5 Seconds we want to Auto refresh this site and then we'll start seeing once we refresh this page some information being sent to our graan Faro instance and being visualized here on this dashboard so you can see that already we're getting seven page loads we've got all of our web vitals information here up top such as time to first bite first contentful paint largest contentful paint cumulative layout shift first input delay and interaction to next paint we then also have an indication of how many errors have been encountered on our application below that we have our page loads and errors in real time and you can see here that we have our page loads and then errors here are displayed in red below that we have our page performance section now this is split out by root because we integrated that react integration for our react router we're getting all of the information split out by for example our favorite section our search page and our root page here and then below that we have three panels here which are 75th percentile indicators for things such as page load cumulative layout shift and input response time this is going to give you a broad Strokes overview of what the vast majority of users are experiencing with your application now with all of this information the first thing I want to immediately draw my attention to is this two errors here up at the top I want to figure out what's happening within my application what errors the users are experiencing and then figure out if I can fix it so at the top here where we have our tabs let's click into the errors Tab and you can see here that we get this page load and errors timeline again but we also get this top errors section and top page Roots by error count and this immediately indicates to me that we've got a 404 request failing and we also can see that it's on the search page so let's click into this error here and you can see that we get the full stack trace for this error it's an axios error and it's request filled with status 404 and we can see that it's happened on the search page so let's come back into our overview dashboard here and we know that it's on our search page and we know that it's a 404 so immediately I could go into my code and I could make sure that the URL I'm using is correct but there's one other thing I can do here as well and that's head into our search section here for our search page and we can see all of the user sessions that have happened or currently happening within our application let's click on the session ID here to be taken into the session details and this is all of the information about this particular user's Journey throughout our application you can see here that we can see all of the events and measurements that are being gathered and collected from that user and then inside the activity section I'm going to toggle over to the traces section here this is going to show me all of the traces within the application so you can see that I've got a bunch of get requests going out to third party applications here let's click through some of these and see what's going on so in the first one you can see I've got a 200 okay get request here for a featured endpoint and this is on my steam API and now the second one here again is a 200 okay clicking through some of these here you'll see that eventually we will stumble upon the 404 endpoint here and I can see immediately that this is hitting my game's endpoint and it's searching for that Final Fantasy game that we were looking for however I can see here that immediately there is a typo in this URL it's got games with double s instead of just single so let's come into our application code here we'll go to the search page and then we'll fix this URL here so let's change that back we'll save this and then we'll come back into our application and go to the search page here now let's type search in for Final Fantasy again and you can see now that we have results returning successfully awesome so what I want to do now is you've seen that we can gather information about the page load times all of our web vitals we can see logs errors and traces from our application however I want to add some additional context to all of the logs and events that we're pushing to graan Faro so that I have better indications about things such as the user Journey for example I might want to push a log entry and an an event that tells me when a user has performed a search and what the results of that search were so let's dive in to our code again and after we've performed our search here I want to add a custom log entry that is going to be sent to graan Faro that tells me some additional context about that search so we're going to import a couple of things here let's import the far object as well as the log level from far react package and down here now just after we've received our results for our search we're going to call the far. api. push log function we're going to give it a string here that says search result for search term found response games we're going to change the level here from warn to info it's not actually a warning and then we're going to pass in some additional context here we'll pass the search term we'll pass the results and we'll also pass the user ID now this expects to be a string so what I'll do here is I'll change this response data length into a string just using some string interpolation there and then we'll save this file what I also want to do is I want to push an event so let's use the same Farrow API but this time we're going to use the push event function here we're going to give it a name we're going to pass in some of that additional context and we're going to also specify what domain this event belongs to and then finally what I want to do is I also want to send a custom error to graan Faro whenever an error is encountered perhaps in this search section again so let's wrap this whole thing in a try catch block we're going to catch an error let's just fix the format in here and when we get this error here what I want to do is I want to use the Faro API and we're going to push the error to graph Faro the other thing I'm going to do here is I'm going to do a set is loading to be false just so the user isn't presented with A continuous loading spinner what this is going to do now is when this URL is called and anything goes wrong either within setting the games from the response or perhaps the URL goes incorrect or anything else happens here we're going to push that error message specifically to graan Faro and then the user is not going to get that continuous loading spinner so let's save this now and let's go back back to our application we'll go to our search panel here and now if I type in let's say for example broken sword and we can see the results here let's add some things to our favorites and now let's search for example Master Chief and we can see the Master Chief Collection has come up here I want to add that one to my favorites as well and now let's dive back into our grafana front end observability dashboard here for our application and what I want to do now is under our page performance section I'm going to click on the search endpoint here I'm going to expand this session for the user and I'm going to click on explore to come and have a look at the Loki logs for this particular session I'm going to open up the Builder here for our log and I'm going to change the operation here I'm going to add a new label filter let's change this to be kind and I want to search for any events that might have happened for this particular user let's run the query here and we'll change the time span to be the last 30 minutes and if we come down into our logs here you'll see that we have all of the events that have been captured for this particular session and you can see here there's an event with a name of search let's scroll down on the page a little bit here and you can see all of the information for this particular search event that I've just pushed from my code specific specifically we can see the event data search term was Master Chief we can see the user ID which is the user ID for my user within my application let's also come up here and change this kind to log and we'll be able to see the custom log entry that we sent as well so here inside of our logs panel you can see a message of search result for Master Chief found one game we'll scroll down and we can see that additional context there was one result the search term was Master Chief and again we've got the user ID for our user there and with that we've successfully instrumented our react application using the grafana farro SDK and grafana frontend observability in grafana Cloud thanks for watching as we explored how to enhance your react app with grafana Faro for a comprehensive front-end observability solution if you want to dive deeper into grafana Faro and explore more about front-end observability make sure to check out our documentation the Link's in the description below if you found this video helpful pleasee remember to give it a like and consider subscribing to the channel for more gra tutorials and insights if you have any questions or feedback please don't hesitate to leave them in the comments below so until next time take care and I'll see you in the next one [Music]
