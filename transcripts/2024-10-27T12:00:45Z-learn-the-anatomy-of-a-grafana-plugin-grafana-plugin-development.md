# Learn the Anatomy of a Grafana Plugin | Grafana Plugin Development

Learn about the anatomy of a Grafana plugin in this video where we'll dive deep into the various frontend and backend ...

Published on 2024-10-27T12:00:45Z

URL: https://www.youtube.com/watch?v=dzFkEAVwjGI

Transcript: grafana plugins are a powerful way to extend graph's core functionality they allow you to create custom features like new data sources visualizations or even entire applications hi I'm Tom one of the developer Advocates here at grafana labs and in this video we'll break down the anatomy of a crana plugin explore the three different types of plugins discuss their key components and show you how to structure and organize your plug-in for Success let's start by going over the three primary types of plugins within grafana apps data sources and panels each has its own unique role and components app plugins offer maximum flexibility and are perfect for creating custom experiences that go beyond visualizations or data interaction for example our kubernetes app offers an out-of-the-box observability experience for monitoring your kubernetes clusters data sources enable grafana to connect to external services and query data examples include Prem meus mongodb and Google Sheets panels allow you to create custom visualizations or widgets that can be added to dashboards these can be things like SVG displays flow diagrams or even AI powered dashboard widgets now that you know what kind of plugins are available let's dive into how plugins are composed we'll start by discussing the separation of front end and backend plug-in components while panel plugins only contain front-end components app app and data source plugins can have a combination of both so it's important to understand the differences front end components of a plugin are written using typescript and typically make use of react this means they run directly in the user's browser and importantly in order to access external Services via HTTP requests you must make use of something called the grafana proxy you can find more information on the proxy in our developer documentation backend components of a plug-in are written using go and this code executes on the server side since the code is running on the server you can expose resource Handler endpoints which can serve data to your front end these are useful when you want to perform some server side functionality such as making an authenticated call out to a third party service and returning the data in order to support alerting in your data source plugin you must create a back-end data source we'll discuss the differences between front-end and backend data sources a little later the key takeaway here is that front-end components manage user interaction while backend components handle server side logic and external interactions let's take a look at the individual components that make up an app plugin now before we discuss the front end and backend components it's important to point out that every plugin no matter what its type has a plug-in. Json configuration file this is where you'll create all of your plugins metadata such as its name description icons screenshots and any relevant links all of these will then then become available within the plug-in catalog on the front end Pages allow you to create custom Pages accessible from grana's navigation using react components to create custom user interfaces for your application your app can have as many pages as you like and in advanced use cases these can even have role-based access control to restrict certain users from accessing certain pages app plugins often include configuration Pages where users can input essential settings like API credentials or other parameters these are effectively pages that perform the specific role of allowing users to configure your app UI extensions allow developers to hook into Graf's core UI extending it with powerful custom functionality such as adding additional context menu options or navigation items moving over to the backend components now and developers can define a server side health check which could return a success or failure status which indicates the health of the app this can be a great way to ensure that your plug is working correctly and has the appropriate configuration as we mentioned earlier apps can handle server side logic such as making external API calls or processing data resource handlers can be created to expose HTTP endpoints which can be called by the front end to receive the results of these server side interactions and finally unique to app plugins is the concept of nested plugins in order to provide a cohesive out-of-the-box experience you may wish to bundle new data sources or or panel plugins in order to create your desired bespoke experience for your app with app plugins the possibilities are virtually endless when it comes to creating custom experiences within grafana now let's look at the components that make up a data source plugin firstly on the front end we have the config editor this is where users can provide connection details such as API keys or endpoint URLs for the external service it's essential for setting up the data source correctly next there's the query editor this this is what allows users to construct queries against the connected service this editor is used when adding a panel to the dashboard when using explore and when creating a new alert rule the query editor can be customized to provide a code editor or a more bespoke visual query Builder I mentioned earlier that there are both front-end and backend data source plugins the distinction lies in the way that the health check and query data functionality is implemented for front-end data sources both the health check and data components live on the front end and are written using typescript the health check is used to verify that the connection to the data source is working and it's invoked when the user presses the save and test button when configuring the data source the query data function is the component that actually queries the data source using the user's query and it's responsible for returning the appropriate data frames which can then be used by the panel itself for backend data sources the health check and query data components instead run on the server side and they're therefore written in go backend data sources can also expose resource endpoints just like app plugins can this allows you to run bespoke server side logic and return them to the front end via HTTP requests as necessary data plugins are all about making external Services accessible within grafana and these components ensure smooth integration and interaction with your data finally let's take a look at the simplest of the three plug-in types panels panels do not have any backend components and are solely composed of front-end components for panels there's the visualization component this is where you provide the visual representation of query data or the interface for your Widget the visualization is made up of a react component and can be anything from a simple chart to a complex interactive Widget the panel's render function defines how the data from the data sources passed into the visualization and how updates are handled when data or options change then there are the panel options this allows users to customize the behavior or appearance of the panel plugin the specific options available must be defined in code and can then be used from inside the panel visualization component users are able to modify the values of these options from the panel options on the right hand side when editing the panel in grafana panel plugins offer a lot of creative freedom enabling you to build visualizations that can be tailored to each user's needs now that we've understood the components that make up each PL plugin type let's discuss organizing your plug-in files when you use the create plugin CLI tool it generates a scaffolded folder structure for your project which consists of various configuration and build files for the project as well as the source code for the components we just discussed that make up your plugins functionality front end code lives inside the source directory and it's written in typescript with key files like the plugin. Json and module. TS file this is where you'll write all of the necess NE AR codee for the front end components that make up your plugin for example if you're creating an app plugin this is where you'll add the pages configuration and Define any UI extensions that make up your app for data sources you'll create the config and query editor react components you'll also Define the health check and query data components if you're creating a front-end data source and for panel plugins this is where you'll write the react components that make up the visual element of your panel as well as Define any relevant panel options the user can configure back back end code lives inside the package directory and it's written in go this is where you'll create your health check and resource endpoints for apps as well as for backend data sources along with the query data component and finally endtoend tests live inside the tests folder these are different to your justest unit tests which typically live alongside your front-end typescript code endtoend tests use a testing framework called playright and provide you with the ability to write automated front-end tests this is important for verifying that your plugin can run correctly across multiple versions of grafana for more information on writing and running endtoend test see our developer documentation portal now that you understand the essential components of a grafana plugin as well as how they're structured we recommend diving into our detailed tutorials exploring our plugin examples on GitHub and joining the grafana community to collaborate with other developers just like you when you're ready you can also learn how to publish your grafana plugin and share your work with the grafana community if you enjoyed this video be sure to leave a like and hit the subscribe button to be notified when we release awesome grafana content just like this thank you so much for watching and I'll see you in the next one
