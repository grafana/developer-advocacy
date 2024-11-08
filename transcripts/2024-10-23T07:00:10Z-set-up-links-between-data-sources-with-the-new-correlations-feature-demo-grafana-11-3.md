# Set Up Links Between Data Sources With the New Correlations Feature | Demo | Grafana 11.3

Correlations is a feature that allows Grafana users to set up links between their data sources. Previously, the link generated would ...

Published on 2024-10-23T07:00:10Z

URL: https://www.youtube.com/watch?v=KuVlzjaVc0Y

Transcript: Hello, I'm Kristina, a software engineer
on the DataViz team at Grafana Labs. Grafana is well-known for
their big tent philosophy, meaning Grafana users can bring in
data from a variety of other systems. Oftentimes this data is distributed in
different places and investigation can require hopping between
different data sources. Correlations was introduced into Grafana
10 to allow for links between data sources and Explore. After
configuring a correlation, a data result and Explore would display
a link and clicking that link would pull up a second Explore pane with a different
data source with data from the first data source inserted inside the query.
In many instances for Grafana users, data is also exposed in other
third party web platforms. You may wanna jump from their Grafana
instance to one of these other platforms to continue investigation. To enable this, we now allow for users to
build a correlation that
goes to a URL instead of a second query. Let's take a look
at what this might look like. So I have set up a data
source to GitHub with this. We can pull labels for the Grafana project here. As you can
see, we've got quite a few of them. Another thing that we're gonna need
for this is we'll go into GitHub here, we'll look at issues and then
we'll filter issues by a label. And we're just using
this to get a sample URL, so it doesn't matter which one we
click and we're gonna copy this. An important thing to note for
the correlation here is the, this is where we want
our correlation to be. It's not gonna be on these fields and
it's important to note the name of this field is name. So we'll go into correlations
in admin, add new. We can name this whatever. It will
only really show when you do a hover. So for this, instead of having it be a
query, which is like what we're used to, we're gonna click the new
external type and paste in that URL that did the filtering by
a label, which we had before. And then if you remember the
name of that field is a name. So we'll just put that in using
the Grafana variable syntax here. Our source data source
is going to be GitHub and the field that we
wanna use again is name. So we'll add that when we go back into Explore, we're gonna
pull up the data that we had before. And as you can see now, those names
are all links, the blue links, and when you click on one, it will
pull up the link that we pasted, but with that label
applied. And so with that, we end up seeing the list of issues
with that label filter already in place. So this can show how you can use
correlations to link to a third party system. Support for external links
and correlations is going
to be available in Grafana 11.3. And I hope you like
it. Thank you very much.

