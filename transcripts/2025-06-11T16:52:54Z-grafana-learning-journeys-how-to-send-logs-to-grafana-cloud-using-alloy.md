# Grafana Learning Journeys: How to Send Logs to Grafana Cloud Using Alloy

Published on 2025-06-11T16:52:54Z

## Description

In this Grafana Learning Journey supplementary video, Developer Advocate Marie Cruz shows how to send system logs to Loki in ...

URL: https://www.youtube.com/watch?v=Xa3mCIdsno4

## Summary

In this Grafana Learning journey video, Marie provides a comprehensive tutorial on sending system logs to Loki in Grafana Cloud using Alloy. The video covers the installation and configuration of Alloy, a data collector compatible with observability standards, and explains the purpose of Loki, a log storage and search system. Marie outlines prerequisites for the tutorial, including having a Grafana Cloud account and access to system logs, and demonstrates how to install Alloy, configure it to source logs, set up necessary components, and verify the installation. She also introduces Alloy UI for monitoring and troubleshooting telemetry pipelines and concludes by showing how to view exported logs in Grafana Cloud. The video serves as a practical guide for users looking to enhance their observability with Grafana technologies.

# Grafana Learning Journey: Sending System Logs to Loki with Alloy

Welcome to another Grafana Learning Journey! My name is Marie, and in this video, I'm going to show you how to send your system logs to Loki in Grafana Cloud using Alloy. 

## What You Will Learn

As part of this learning journey, you will learn:

- How to install and configure Alloy to send logs to Loki.
- How to use Alloy to understand and troubleshoot your telemetry pipelines.
- How to verify that your system logs appear correctly in Grafana Cloud.

Before we dive in, let's first talk about what Alloy and Loki are.

### Alloy and Loki Overview

- **Alloy** is a data collector that gathers metrics, logs, traces, and profiles from your systems. It's fully compatible with popular open-source observability standards such as Open Telemetry and Prometheus.
  
- **Loki**, on the other hand, is a log storage and search system inspired by Prometheus. It can store logs and allow users to explore them with queries.

## Prerequisites

Before we jump into the tutorial, here are a few prerequisites you need to know:

1. You need to have a Grafana Cloud account.
2. You need access to your system logs. If you don’t have any access, create a dummy file with some log content.
3. You should have basic familiarity with Grafana and Loki, and ensure Loki is up and running and connected as a data source. I’ll be using Grafana Cloud Logs in this video, so feel free to pause here and get ready.

## Installing Alloy

For the first milestone, you'll install Alloy on your local machine. 

1. In your Grafana environment, open the navigation menu on the left.
2. Scroll down to **Connections**, and then click **Collector**. 
3. You should see the **Install Grafana Alloy** button. Click that.

Depending on your operating system, select the appropriate platform and architecture. For Mac OS users, choose your installation method. 

Next, create a new API token or use an existing token. If you are using an existing token, ensure it has the correct permissions. For this learning journey, it should have at least the following permissions. 

I’m going to toggle the **Enable Remote Configuration** feature off as I won't be using Fleet Management. 

Now, in the **Install and Run Grafana Alloy** section, I’m going to copy a few scripts. First, I'll install Alloy via Homebrew. Then, let’s switch to my terminal and run that command. 

Once installed, I’ll copy the setup configuration script, which will generate a configuration file. Finally, I’ll start Grafana Alloy as a service. 

To verify that Grafana Alloy is installed correctly, navigate back to Grafana Cloud and click **Test Alloy Connection**. You should see the message "Awesome! Grafana Alloy is good to go." 

If you encounter any issues with the installation, you can use the troubleshooting guide included as part of this milestone in the Grafana Learning Journey. Alternatively, if you're watching this directly from YouTube, let us know in the comments below, and we’ll direct you to the correct resource.

## Sending Logs to Loki

In this milestone, you’ll learn which Alloy components to use to send your system logs to Loki. In Alloy, a component is like a building block that does one specific job in collecting, processing, or sending telemetry data. It’s similar to a LEGO piece, where each one has a specific purpose that you connect to build a working pipeline.

### Components Overview

For this learning journey, I’ll demonstrate how to use three Alloy components:

1. **local.file_match**: This component searches for log files on your system based on a pattern.
2. **loki.source.file**: This component reads the log lines from the logs found by the local.file_match component and parses them for Loki.
3. **loki.write**: This component sends the processed logs to a Loki backend.

### Wiring the Components

The next step is to wire all these components together to build a working pipeline, similar to LEGO. 

In Alloy, the `config.alloy` file defines the pipeline for how Alloy should receive telemetry data, process or transform it, and later export it to Prometheus, Loki, Tempo, or other platforms and databases. 

The default location for the configuration file depends on your operating system. For Mac, it is on this path. For Linux and Windows, it’s here. You can open this file with Vim or Nano, but I recommend using VSCode with the Alloy plugin installed for better syntax support.

When you open the configuration file generated by the setup guide in Grafana Cloud, you’ll notice it’s not empty. At a high level, the components here collect and expose internal metrics about Alloy itself and forward them to Prometheus. 

If I scroll down, you should see the `loki.write` component with my Loki URL, username, and API token, but it’s not wired up yet. We still need to add the other two components mentioned previously.

Let’s go ahead and do that:

1. Configure Alloy to search for log files to source. This configuration creates a `local.file_match` component named "local files," telling Alloy which files to source and checking for new files every five seconds.
2. Configure Alloy to read log entries from files and forward them to other Loki components. This configuration creates a `loki.source.file` component named "logs scrape," which connects to the "local files" component as its source and forwards the logs it scrapes to the `loki.write` component called "grafana cloud loki."

For better readability and organization, we highly recommend adding the components in order. 

After saving the file, we need to let Alloy know of the new changes by reloading the configuration file. 

To reload, I’ll call this reload endpoint. You should see a confirmation message.

## Monitoring with Alloy UI

Now, you might ask, how do I know if everything is working correctly? The answer is **Alloy UI**, which we’ll explore in the next milestone. 

The Grafana Alloy UI is a lightweight built-in web interface provided by Alloy to monitor its internal status, debug data pipelines, inspect telemetry data, and view configuration and component states. Unless configured otherwise, Alloy UI defaults to listening on localhost port 12345. 

When you open Alloy UI, you can see all the components you have configured and their status. You'll be able to see if any components have been reported as unhealthy. 

Clicking the **Graph** tab at the top leads you to the Graph page, which shows a visual representation of the components defined in the configuration file. You can see how the Loki components are wired up and observe their flow.

When you click a component in the graph, you’re redirected to the Component Detail page, which shows more information about that component, including its health, arguments, exports, debug info, and any dependent components. For example, the `local.file_match` component will show all the log files that Alloy is sourcing.

## Viewing Logs in Grafana Cloud

You’re almost finished with this learning journey! The last step is to view the exported logs in Loki in Grafana Cloud, which we’ll cover in the next milestone.

To view the logs:

1. Go back to your Grafana environment.
2. Open the navigation menu on the left side of the screen and click **Drilldown**.
3. Click **Logs**. You should see the Logs Drilldown Overview page, which displays log visualizations and samples for all the services in your selected Loki instance.

If you can’t see the logs, make sure to select the correct Loki data source. If you have multiple log files, you can click the file name to view logs by file. To explore the logs themselves, click the **Show Logs** button. Grafana will then display the Logs tab of the selected file name.

## Conclusion

And there you have it! In this video, you learned:

- What Loki and Alloy are.
- How to install and configure Alloy.
- How to edit the configuration file to wire up the components needed to send logs to Loki and Grafana Cloud.
- What Alloy UI is and how to use it to investigate or troubleshoot your telemetry pipelines.
- How to view the logs exported to Loki in Grafana Cloud.

I hope you found this video useful! If you want to learn more about the Grafana platform, check out our Grafana Learning Journeys. 

**Happy visualizing!**

## Raw YouTube Transcript

Welcome to another Grafana Learning journey. 
My name is Marie, and in this video I'm going to show you how you can send your system logs 
to Loki in Grafana Cloud using Alloy. As part of this learning journey, you're going to learn 
how to install and configure Alloy to send logs to Loki. You're also going to learn how to 
use Alloy to understand and troubleshoot your telemetry pipelines. And finally, you're going 
to verify that your system logs appear correctly in Grafana Cloud, but before any of that, let's 
first talk about what Alloy and Loki are. Alloy is a data collector that gathers metrics, logs, 
traces and profiles from your systems. It's fully compatible with the most popular open source 
observability standards such as Open Telemetry and Prometheus. Now, Loki on the other hand, is a log 
storage and search system inspired by Prometheus, it can store logs and allow users 
to explore them with queries. Now, before we jump in into the actual video 
tutorial, there are a few prerequisites that you need to know. First, you need to 
have a Grafana Cloud account. Next, you need to have access to your system logs. If 
you don't have any access, then create a dummy file with some log content. You also need 
to have basic familiarity with Grafana and Loki and also Loki should be up and running and 
connected as a data source. Whether you've locally installed it or you're using Grafana Cloud Logs. 
In this video, I'll be using Grafana Cloud Logs, so feel free to pause this video here 
and when you're ready, let's get into it. For the first milestone, you'll install Alloy on 
your local machine. In your Grafana environment, open the navigation menu on the left. Scroll 
down to Connections, and then click Collector. You should see the Install Grafana Alloy 
button. Go ahead and click that. Depending on your operating system, select the appropriate 
platform and architecture. For Mac OS users, select the installation method as well. Next, 
create a new API token or use an existing token. If you are using an existing token, make 
sure that it has the correct permissions. For this learning journey, it should 
have at least the following permissions. I'm going to toggle the Enable Remote 
Configuration feature of as I won't be using Fleet Management. Now in the 
Install and Run Grafana Alloy section, I'm going to copy a few scripts. First, 
I'm going to install Alloy via Homebrew. Then let's switch to my terminal and 
run that command. Once it's installed, I'm going to copy the setup configuration 
script, which will generate a configuration file. Finally, I'm going to start Grafana Alloy 
as a service. To verify that Grafana Alloy is installed correctly, navigate back 
to Grafana Cloud and click Test Alloy Connection. You should see the message 
"Awesome! Grafana Alloy is good to go." If you encounter any issues with the installation, you can use the troubleshooting guide that 
we've added as part of this milestone in Grafana Learning Journey. Or if you're 
watching this directly from YouTube, let us know in the comments below and 
we'll redirect you to the correct resource. In this milestone, you're going to learn which 
Alloy components to use to send your system logs to Loki. In Alloy, a component is like a building 
block that does one specific job in collecting, processing, or sending telemetry data. It's 
similar to a LEGO piece where each one has a specific purpose and you connect them to build 
a working pipeline. For this learning journey, I'm going to demonstrate how 
to use three Alloy components. As you get more familiar with Alloy, you're going 
to use more components depending on your use case. For the full list of available components, 
refer to the Alloy component documentation. Now, the first component that you need to 
know is the local.file_match component. This component will search for log files 
on your system based on a pattern. The next component is the loki.source.file 
component. This component will read the log lines from the logs found by 
the local.file_match component. It also parses the logs to prepare them for Loki. 
The final component is the loki.write component, which sends the process logs to a Loki backend. The next step is to wire all these 
components to build a working pipeline similar to a LEGO. In the next milestone, 
I'm going to introduce you to the Alloy configuration file so we can wire all these 
components together to send logs to Loki. In Alloy, the config.alloy file defines 
the pipeline for how Alloy should receive telemetry data, process or transform it, 
and later export it to Prometheus, Loki, Tempo or other platforms and databases. The 
default location for the configuration file depends on your operating system. I'm on a Mac, so 
mine would be on this path. For Linux and Windows, it's here. You can open this file 
with Vim or Nano, but I recommend opening it with VSCode with the Alloy plugin 
installed as it offers better syntax support. When you open the configuration file 
that's generated by the setup guide in Grafana Cloud, you'll notice that it's not empty.
On a high level. The components that you see here collect and expose internal metrics about Alloy 
itself and forward them to Prometheus. If I scroll down, you should see the loki.write component with 
my Loki URL, username, and API token, but it's not wired up yet. We still need to write the other two 
components I mentioned in the previous milestone. So let's go ahead and do that. First, I'm going to 
configure Alloy to search for log files to source. This configuration creates a local.file_match 
component name "local files." This tells Alloy which files to source and checks for new files 
every five seconds. Next, I'm going to configure Alloy to read log entries from files and 
forward them to other loki components. This configuration creates a 
loki.source.file component named "logs scrape", which connects to the "local 
files" component as it source and forwards the logs it scrapes to the loki.write 
component called "grafana cloud loki." On a side note, we highly 
recommend that you add the components in order for better 
readability and organization. I'm going to save the file and 
then go back to my terminal. Now, we need to let Alloy know of the new changes, 
so we need to reload the configuration file. To reload, I'm going to call this reload 
endpoint. You should see the following message. Now, you might ask, how do I know 
if everything is working correctly? The answer to that is Alloy UI, which 
we'll look at in the next milestone. The Grafana Alloy UI is a lightweight 
built-in web interface provided by Alloy to monitor Alloy's internal 
status, debug data pipelines, inspect telemetry data being collected or sent, 
and view configuration and component state. Unless configured otherwise, Alloy UI defaults 
to listening on localhost port 12345. For this learning journey, we're just going to 
use the default. When you open Alloy UI, you can see all the components that you have 
configured and their status. You'll be able to see if you have any components that have been 
reported as unhealthy. Clicking the Graph tab at the top will lead to the Graph page, which 
shows a graph view of components defined in the configuration file. You can see how the Loki 
components are all wired up and how they all flow. When you click a component in the graph, you are 
redirected to the Component Detail page for that component. This page shows more information about 
the component, such as its health with a message explaining why, its arguments, its exports, 
any debug info, and any dependent components. In this example, the local.file_match component 
shows all the log files that Alloy is sourcing. You're almost finished with this learning 
journey. The last step is to view the exported logs in Loki in Grafana Cloud, 
which we'll look at in the next milestone. To view the logs, go back to your Grafana 
environment. Open the navigation menu on the left side of the screen and click 
Drilldown. Now click Logs. You should see the Logs Drilldown Overview page, which 
displays the log visualizations and log samples for all the services in your selected 
Loki instance. If you can't see the logs, make sure you select the correct Loki data 
source. If you have multiple log files, you can click the file name to view the 
logs by file. To explore the logs itself, click the Show Logs button. Grafana then 
displays the Logs tab of the selected file name. And there you have it. In this video, you 
learn what Loki and Alloy are. You learn how to install and configure Alloy, and how 
to edit the configuration file to wire up the components needed to send logs to Loki and Grafana 
Cloud. You also learn what Alloy UI is and how to use it to investigate or troubleshoot 
your telemetry pipelines. And finally, you learned how to view the logs 
exported to Loki in Grafana Cloud. I hope you found this video useful, and if you 
want to learn more about the Grafana platform, check out our Grafana Learning 
Journeys. Happy visualizing!

