# Beginners Guide - How to Configure a Candlestick Visualization | Grafana

What is a candlestick and how can you visualize price movements in Grafana? Join Senior Developer Advocate Marie Cruz in this ...

Published on 2024-04-22T09:00:10Z

URL: https://www.youtube.com/watch?v=IOFKBgbf3aM

Transcript: Hi everyone! My name is Marie Cruz, 
and I’m a Senior Developer Advocate   at Grafana Labs. In back with 
another beginner-friendly video   tutorial and this time, I’m going to 
talk about candlestick visualizations. By the end of this tutorial, 
you should know when to use a   candlestick and what data it needs so you 
can visualize it correctly in Grafana. So, let’s say you want to start investing, 
and you’re interested in monitoring how the   price of a stock or any financial asset 
has changed over time. A candlestick   chart allows you to visualize these 
price movements easily at a glance. Each candlestick represents a period of time, 
such as days, hours, or minutes. The candlestick's   rectangle part represents the asset's opening 
and closing prices during a specific period of   time. Candlesticks are often visualized as 
different colors so traders can easily know   if an asset has appreciated or depreciated. By 
default, Grafana uses the green and red colors,   but this can be easily customized as 
part of your candlestick configuration. A green candlestick represents when the asset’s 
price has appreciated or went upwards. In this   scenario, the opening price, which is the price of 
the asset at the beginning of the time period, can   be seen at the bottom of the candlestick’s body. 
On the other hand, the closing price, which is   the asset's price at the end of the time period, 
can be seen at the top of the candlestick’s body. A red candlestick represents when the 
asset’s price has depreciated or went   downwards. In this scenario, the opening price 
is seen at the top of the candlestick’s body,   while the closing price is seen at 
the bottom of the candlestick's body. You can also see some lines 
sticking out the candlestick's body,   which are called "wicks" or "shadows." 
These lines represent the highest and   the lowest prices the asset has 
reached during the time period. In short, think of a candlestick as 
a visualization of price movements. With that investment explanation out of the way,   let me show you how you can use the 
candlestick visualization in Grafana. OK, so first, let’s add a new 
visualization to a dashboard and   make sure the grafana-testdata-datasource 
is selected. This data source again comes   built-in with Grafana and is perfect for 
Grafana beginners. Then, under the scenario,   I’m going to pick the CSV file scenario 
and then choose the ohlc_dogecoin.csv file. Let’s change the visualization type 
from time series to candlesticks   and I’m also going to click zoom to 
data to get the correct date range. As you can see, we are now getting some data. 
To zoom into a more specific time period,   I can also click the graph directly 
and drag it to a particular point. Now,   you should see clearly the different candlesticks. Let’s click table view to find out the underlying 
data for this scenario. As you can see,   there is a time, open, high, low, closing prices, 
and other relevant information about the asset. As a minimum requirement, your data must 
have a timestamp, the opening, closing,   and the highest and the lowest prices to 
be visualized correctly as a candlestick. If you have any issues, make sure that 
the timestamp is of type time, and also,   if you have different column names 
for the opening, closing, highest,   and lowest prices, you can map them 
by going to the candlestick options   and mapping the columns manually using 
the Open, High, Low, and Close fields. Returning to the chart, notice that if I hover 
my mouse over the bottom of the red candlestick,   the closing price is focused or set to bold. 
The opening price is focused if I hover my   mouse over the top and likewise, if I hover 
my mouse over the upper wicks or shadows,   the highest price is focused, while the lowest 
price is focused if I hover my mouse over the   lower wicks or shadows. The opposite observation 
can be made if it was a green candlestick. Ok, now let’s customize 
our candlestick a bit more. Since our data also contains the volume, 
which can represent the number or volume   of trades done, our visualization also 
displays the volume count. If you want   to exclude this and just focus on 
viewing the actual candlestick,   you can click Candles mode. To display both the 
candlesticks and the volume count, select both. You can also change the color 
scheme however you want,   but I’m going to stick with the default here. Now, since this data also contains other 
relevant information about the asset,   you can ignore or include the other data. 
If included, the data will be plotted as a   time-series visualization. I’ll keep most of the 
other options here as the default but in any case,   if you want to customize the time-series options, 
my wonderful colleague, Leandro Melendez,   has created an informative video tutorial 
on configuring a time-series visualization,   which you can find in the video description below. Finally, let’s update the panel title to Dogecoin 
prices and go ahead and save all the changes. And there you have it! In this beginner-friendly 
video tutorial, I’ve explained what candlesticks   are and how you can configure a 
candlestick visualization in Grafana. Check out our documentation if you want 
to know more about candlesticks and all   the different configurations, which you can 
always find in the video description below. I hope you found this video useful, and if you do,   let us know in the comments and 
as always, happy visualizing!

