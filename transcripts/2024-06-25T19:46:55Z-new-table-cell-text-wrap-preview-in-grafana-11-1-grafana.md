# New: Table Cell Text Wrap Preview in Grafana 11.1 | Grafana

This highly requested feature is now available in preview! You can now wrap text in table cells. By default, the column with the ...

Published on 2024-06-25T19:46:55Z

URL: https://www.youtube.com/watch?v=wBLxYp2BLAU

Transcript: Hi, I'm Kyle Cunningham, a senior engineer
in Grafana’s dataviz squad, and today I'm excited to show you text wrapping for the table panel,
which we've enabled in preview for Grafana 11.1. This is an often-requested feature, and
so we're excited to get this out there. I have a table panel set up here
already, and as you can see, I have records with the text overflowing
and I want to be able to see it all. So all I need to do is go down
to cell options and then select Wrap Text. And as you can see,
the text gets wrapped. One of the nice parts of this,
is that even if the text is long or short, it will wrap appropriately and we'll get
the right heights for these rows here. All right, now let me just
show you one more example. In this case, I have a table
where I have multiple string fields. Let's see what happens
when I go down to wrap. Okay I'm going to
select wrap text again. Oh and there you go.
You can see the text is wrapped. By default, we try and look
and find the field that has the most text and wrap on that, since that's usually
the one that you want to wrap with. But what about in the case of the extra field?
Maybe you want to use that instead. So let's deselect here. It gets turned
off. We go down to overrides. I'll add a field override and I'll select
by name, and I'll choose the extra field. I'll add an override property and
we're going to select the cell type. It's already auto and we can wrap with that.
So let's select that and there we go. We have text wrapping on the extra field,
rather than the text field, which has the longest text. So that is text wrapping
for Grafana 11.1. We're excited for you to try this out, and we're
also working on some additional features to this, including the ability
to compare text in multiple fields and select the longest one for wrapping, 
regardless of which field it's in. We're going to be working on that,
and we're excited to get that out soon as well. We hope you all enjoyed this feature, and
we're looking forward to your feedback. Thanks so much.

