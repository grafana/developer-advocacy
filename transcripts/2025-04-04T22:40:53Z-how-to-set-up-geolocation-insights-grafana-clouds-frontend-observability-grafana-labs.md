# How to Set Up Geolocation Insights | Grafana Cloud&#39;s Frontend Observability | Grafana Labs

Want to set up geolocation insights in Grafana Cloud's Frontend Observability? In this step-by-step tutorial, we'll show you how to ...

Published on 2025-04-04T22:40:53Z

URL: https://www.youtube.com/watch?v=2sNDZKzA7dU

Transcript: How to set up geolocation insights
in Grafana Frontend Observability. Head into your frontend application
page and click on settings. You'll see a new geolocation section. This is where you configure
your geolocation features. We use a MaxMind offline database
to translate the user's IP into geocode data. If you click the on
switch, the feature will be enabled, and you'll have a couple
options here. First, there is the specificity of your geo data. This option controls the level of
resolution you want. For example, if you select country, all levels
below that such as subdivision, city and network won't be tracked. For
this example, I'll use the city level. The other option is the
country denial list, which excludes sessions from specific
countries from the feature altogether. For this example, I'll select Germany
and Japan. For the feature to work, ensure that you have geolocation
tracking and enabled in the SDK as well. This feature is handy if you want
to control the client's side, whether this session should be
geotranslated or not. For instance, the end user might not want it, or the
browser setting might advise against it. Okay. As you can see here, I'm using A VPN for demonstration
purposes and have Athens, Greece selected as the
origin of my session. I'll go ahead and clear the local
storage to ensure that I'm getting a new session. Then I'll refresh the page. I'll also send a test event just
to make sure we have enough data. If we refresh the
frontend application page, you can see that there's now an option
to filter by the geographic origin of the signals. Okay, I'll now change
my origin to Rome, Italy, and follow the same process. Going
back to the frontend observability app, I can now see Rome as an extra option. I can also use the filter to type
in my origin and expand the filter. Last but not least, let's
make sure the deny list works. I'll now select Frankfurt, Germany as my
point of origin and repeat the process. Okay. As you can see, we don't
get any extra entry here, even though the session is normally
tracked. Thanks for watching.

