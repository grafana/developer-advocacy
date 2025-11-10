# Visualise your APIs with Grafana Infinity Plugin

In this Grafana workshop, we will transform our API data to beautiful Grafana dashboards, using the versatile Infinity data source plugin! 📊

![Infinity workshop](images/infinity-workshop.png)

**No prior knowledge of Grafana is required as this workshop is beginner-friendly, but bring your laptops as this will be a hands-on workshop!**

For this workshop, we will use the [TfL API](https://api-portal.tfl.gov.uk/apis), but any public APIs can also be used.

## Install Grafana Cloud

To make it easier for everyone to start learning about Grafana, please sign up to a [Grafana Cloud account](https://grafana.com/auth/sign-up/create-user) and start with the free forever plan.

![Grafana Cloud signup](images/grafana-cloud-signup.png)

## Install Infinity data source plugin

Infinity is not installed by default.

Please follow the instructions [here](https://grafana.com/docs/learning-journeys/infinity-json/install-data-source/) on how to install the Infinity plugin.

## Add the Infinity data source plugin

Once the plugin is installed, Infinity has to be added as a data source.

Please follow the instructions [here](https://grafana.com/docs/learning-journeys/infinity-json/add-data-source/) on how to add the Infinity plugin.

## Explore the TfL API

Feel free to explore the TfL API! Since these are all basic GET requests, you can just load them up from your browser of choice. You can start with the following requests:

### Get status of tube lines

[https://api.tfl.gov.uk/Line/{{tubeLine}}/Status/{{fromDate}}/to/{{toDate}}]()

where:

- {{tubeLine}} - victoria, district, bakerloo
- {{fromDate}} - YYYY-MM-DD
- {{toDate}} - YYYY-MM-DD

example:

https://api.tfl.gov.uk/Line/victoria/Status/2025-11-05/to/2025-11-06

### Get real-time travel disruptions

[https://api.tfl.gov.uk/Line/Mode/{{mode}}/Disruption]()

where:

- {{mode}} - bus, tube, dlr

Please visit https://api.tfl.gov.uk/Line/Meta/Modes to find all the available modes (`modeName`)

example:

https://api.tfl.gov.uk/Line/Mode/bus/Disruption

### Get real-time arrivals

[https://api.tfl.gov.uk/StopPoint/{{NaptanID}}/Arrivals]()

where:

- {{NaptanID}} is a unique ID for every public transport access point in Great Britain.

Please visit https://raw.githubusercontent.com/ZackaryH8/tube-naptan/refs/heads/master/data/naptan.json to find all the naptan IDs for all tube stations in London.

You can also find a [CSV file](https://tfl.gov.uk/bus-stops.csv) of all naptan IDs for different bus stops in London.

## Let's build a dashboard!

We will freestyle this section. 😎

But, here's an [example dashboard](https://play.grafana.org/d/ec0c1486-03e6-4b64-bc80-11e764466e66/london-transport-tfl) which includes live bus arrivals, tube line status updates, and current service disruptions.

![TfL dashboard](../../projects/Play/images/featured-dashboards/tfl.png)

## (Optional) Use Grafana Assistant

[Grafana Assistant](https://grafana.com/docs/grafana-cloud/machine-learning/assistant) is our built-in AI-powered agent that helps you learn and solve problems in Grafana easier than ever.

You can try and ask Grafana Assistant to improve the visual look of your dashboard.
