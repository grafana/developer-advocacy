# How to Use FlameGraph Item Collapsing in Grafana (New in 10.3)

Grafana's FlameGraph now offers item-collapsing, allowing you to manage visual clutter by collapsing similar repeating items ...

Published on 2024-01-23T19:16:01Z

URL: https://www.youtube.com/watch?v=Y1c32Cf5nSE

Transcript: Hello, I'm on the Observability, Traces, and Profiling team and I would
like to show you a feature, FlameGraph Item Collapsing, that's currently experimental and
will be released in Grafana 10.3. So what is this feature about?
Well, for our FlameGraph, sometimes stacks contain lots of
levels with similar repeating items. For example, long stacks of framework
code that usually isn't that interesting but takes up a
lot of vertical real estate. So what this feature does is it
allows you to collapse similar items together. That means instead of rendering
all of the items that are similar, you would render only one and you
could expand and collapse that on demand. So as you can
see in front of us here, now we have our Flamegraph and you can also see this
gray vertical line here, which indicates that all of these
levels are similar in nature, as in, they have a very similar amount
or the exact same amount of samples. We have a smaller one down here
where there are four nodes involved. So what I can do is, if I click
on any one of these nodes, I can actually say Collapse Group and
that will take those four nodes and turn them into one with a little
visual indicator of four
to say there are four nodes collapsed here. I can expand that
as well, of course if I want to. Now, if I have multiple groups
and my Flamegraph is quite large, what I can do is I can just
say Collapse All Groups. And of course that obviously collapses
everything in the Flamegraph that is of a similar nature. Then as you can see, I cannot click Collapse All Groups
because there's nothing else to collapse. They're all collapsed. All I can do is Expand All Groups
or expand a particular group. If I click on that group
itself, expand one at a time, or I can expand all of them. And
that is the collapsing feature. It is also behind a feature
toggle at the moment. Flamegraph Item Collapsing needs to be
enabled if you want to use this feature. Thank you.

