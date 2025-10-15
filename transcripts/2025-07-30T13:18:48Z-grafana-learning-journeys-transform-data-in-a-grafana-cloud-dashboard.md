# Grafana Learning Journeys: Transform data in a Grafana Cloud dashboard

Published on 2025-07-30T13:18:48Z

## Description

In this Grafana Learning Journey supplementary video, Developer Advocate Marie Cruz shows how to use common data ...

URL: https://www.youtube.com/watch?v=g1DXq_IuJ7I

## Summary

In this Grafana learning journey, Marie introduces viewers to transforming data into dashboards using Grafana Cloud. She covers essential prerequisites like having a Grafana Cloud account and basic dashboard creation skills. The video focuses on five key data transformations: "Add Field from Calculation," "Group By," "Filter Data by Values," "Join by Field," and "Organize Fields by Name." Marie demonstrates each transformation step-by-step, explaining their purposes and applications, such as creating new columns, aggregating data, filtering rows, merging tables, and organizing fields for better visualization. She also describes how to export these transformations as CSV files. The video concludes by encouraging viewers to explore more learning journeys on the Grafana website.

# Grafana Learning Journey: Data Transformations

Hello and welcome to another Grafana learning journey. My name is Marie, and today I'll show you how you can transform your data into a Grafana Cloud dashboard. 

As part of this learning journey, you'll learn common scenarios for some of the most popular transformations, apply them to your dashboard, and in the end, export these transformations outside your dashboard. 

## Prerequisites

To follow along in this learning journey, you need to have:
- A Grafana Cloud account
- A data source or integration connected and configured
- Basic familiarity with creating dashboards and panels
- Some familiarity with the queries that you want to transform

Once you have all the prerequisites set up, let's start your Grafana learning journey!

## Understanding Transformations

Transformations allow data to be changed in different ways before the visualization is shown. They are available for all supported data sources and integrations in Grafana Cloud. If your data source or integration can't provide the output that you want, transformations are a great option. 

With transformations, you can easily join and merge data from different queries or data sources without using an external data processing tool. You can also adjust your dashboards and visualizations as requirements evolve, without waiting for changes to the upstream data pipelines.

Grafana has a lot of transformations, and you can apply multiple transformations to your data. Understanding when to use each transformation can be beneficial. 

In this milestone, I'm going to discuss five data transformations:

1. **Add Field from Calculation**
2. **Group By**
3. **Filter Data by Values**
4. **Join by Field**
5. **Organize Fields by Name**

### 1. Add Field from Calculation

The **Add Field from Calculation** transformation allows you to create a new column by performing a custom calculation on one or more existing fields in your data. Use this when you need to create a new field, such as calculating the total, difference, percentage, or ratio.

### 2. Group By

The **Group By** transformation allows you to group rows that share the same values in one or more fields. It's similar to the SQL `GROUP BY` clause. Use this when you need to aggregate data based on one or more fields, such as grouping by a specific category or region.

### 3. Filter Data by Values

The **Filter Data by Values** transformation allows you to include or exclude rows based on specific values in one or more fields. It's similar to the SQL `WHERE` clause. Use this transformation to selectively filter data points directly within your visualization.

### 4. Join by Field

The **Join by Field** transformation is used to combine two or more data tables that share a common field. It's similar to the SQL `JOIN` clause. Use this transformation to merge multiple results into a single table, enabling the consolidation of data from different queries.

### 5. Organize Fields by Name

The **Organize Fields by Name** transformation allows you to rename, reorder, or hide fields returned by a single query in your panel. Use this to make your visualizations more organized, especially after applying multiple transformations.

## Demo of Each Transformation

### Add Field from Calculation

To demo the **Add Field from Calculation** transformation, I have a visualization that shows a table containing dummy website traffic. I want to calculate the average views per user in each country and show it as a new column.

1. Click the **Transformations** tab, followed by the **Add Transformations** button.
2. Select the **Add Field from Calculation** transformation.
3. Under **Mode**, select the mode of operation (in this case, *binary*).
4. Choose the operation and calculation, and update the alias field to give a new name to this column.
5. The transformation should be applied automatically. If not, click **Refresh** to verify.
6. Save the dashboard.

### Group By Transformation

To demo the **Group By** transformation, I have another visualization that shows the sales revenue for a specific region. I want to group by similar regions and get the total sales revenue for that region.

1. Click the **Transformations** tab, followed by the **Add Transformations** button.
2. Select the **Group By** transformation.
3. Choose the field to group by (in this case, the *region* field).
4. Apply the calculation type (e.g., total sales amount per region).
5. The transformation should be applied automatically. If not, click **Refresh** to verify.
6. Save the dashboard.

### Filter Data by Values Transformation

To demo the **Filter Data by Values** transformation, I have a visualization that shows a pie chart about browser market share.

1. Click the **Transformations** tab, followed by the **Add Transformations** button.
2. Select the **Filter Data by Values** transformation.
3. Choose whether you want an *include* or *exclude* filter.
4. Select the condition (match all or any).
5. In this example, filter browsers that have lower than or equal to 5% market share.
6. The transformation should be applied automatically. If not, click **Refresh** to verify.
7. Save the dashboard.

### Join by Field Transformation

To demo the **Join by Field** transformation, I have a visualization that shows two different queries. I want to combine these two queries into one table and join them by their ID.

1. Click the **Transformations** tab, followed by the **Add Transformations** button.
2. Find the **Join by Field** transformation.
3. Choose how you want your queries to be joined (e.g., *inner join*).
4. Select the field to be joined from the two tables (e.g., *product ID*).
5. The transformation should be applied automatically. If not, click **Refresh** to verify.
6. Save the dashboard.

### Organize Fields by Name Transformation

To demo the **Organize Fields by Name** transformation, I have another visualization that shows different car makes and models displayed in a table. I want to hide some fields and rename others.

1. Click the **Transformations** tab, followed by the **Add Transformations** button.
2. Find or search for the transformation.
3. Choose whether to reorder the fields manually or automatically (in this example, I'll keep it as manual).
4. To hide fields, click the eye icon to disable them (e.g., hide *year* and *origin* fields).
5. Rename the *miles per gallon* field.
6. The transformation should be applied automatically. If not, click **Refresh** to verify.
7. Save the dashboard.

## Exporting Data Transformations

In this milestone, you will learn how to export your data transformations outside Grafana Cloud. By default, Grafana doesn't support exporting your data transformations directly to an external database or other tools. However, you can export the data transformation manually as a CSV file.

1. Click the **Queries** tab and then the **Query Inspector** button.
2. Select the **Data** tab and expand the data options row.
3. Enable the **Apply Panel Transformation** option.
4. Finally, click the **Download CSV** button. 

You should now have a CSV file with the transformation applied to your data.

## Conclusion

Congratulations on completing this learning journey! I hope you enjoyed this video while learning about the value of data transformations, how to apply common data transformations to your dashboard, and how to export them as a CSV file manually outside of Grafana Cloud. 

If you find this type of learning useful, check out the rest of our Grafana learning journeys at [grafana.com/docs/learningjourneys](https://grafana.com/docs/learningjourneys). 

I hope to see you on the next one. **Happy visualizing!**

## Raw YouTube Transcript

Hello and welcome to another Grafana learning 
journey. My name is Marie, and today I'll show you how you can transform your data into a Grafana 
Cloud dashboard. As part of this learning journey, you'll learn common scenarios for some 
of the most popular transformations, apply them to your dashboard, and in the 
end, export these transformations outside your dashboard. To follow along in this learning 
journey, you need to have a Grafana Cloud account. You also need to have a data source or an 
integration connected and configured. Next, you need a basic familiarity with 
creating dashboards and panels. And finally, some familiarity with the 
queries that you want to transform. Once you have all the prerequisites set up, 
let's start your Grafana learning journey. Transformations allow data to be changed in 
different ways before the visualization is shown. It's available for all supported data 
sources and integrations in Grafana Cloud. If your data source or integration 
can't provide the output that you want, transformations are a great 
option. With transformations, you can easily join and merge data from 
different queries or data sources without using an external data processing tool. You can 
also adjust your dashboards and visualizations as requirements evolve without waiting for 
changes to the upstream data pipelines. Grafana has a lot of transformations, and 
you can apply multiple transformations to your data. So understanding when to use 
each transformation can be beneficial. Grafana has a lot of transformations, and 
I wish I could talk about all of them, but I have limited time. So in this 
milestone, I'm going to discuss five data transformations starting from the 
add field from calculation transformation. The add field from calculation transformation 
allows you to create a new column by performing a custom calculation on one or more existing 
fields in your data. Use this for when you need to create a new field, such as calculating 
the total, difference, percentage, or ratio. The group by transformation allows you to 
group rows that share the same values in one or more fields. It's similar to the SQL group 
by clause. Use this when you need to aggregate data based on one or more fields, such as 
grouping by a specific category or region. The filter data by values transformation 
allows you to include or exclude rows based on specific values in one or more 
fields. It's similar to the SQL WHERE clause. Use this transformation to selectively filter 
data points directly within your visualization. The join by field transformation is used 
to combine two or more data tables that share a common field. It's similar to the SQL 
join clause. Use this transformation to merge multiple results into a single table, enabling 
the consolidation of data from different queries. Finally, the organize fields by name 
transformation allows you to rename, reorder, or hide fields returned by a single 
query in your panel. Use this to make your visualizations more organized, especially 
after applying multiple transformations. It's up to you if you want to learn how all these 
transformations work, or you can choose which transformation you want to focus on. If you are 
watching this from the Grafana learning journey documentation, you can jump to the transformation 
by going to the correct milestone. Or if you are watching this from our YouTube channel, 
you can skip to the correct chapters. I'm now going to demo how each of 
these data transformations work. To demo the add field from 
calculation transformation, I have the following visualization which 
shows a table containing a dummy website traffic. I want to calculate the average 
views per user in each of the country here and show it as a new column. To apply the 
add field from calculation transformation, click the transformations tab, followed 
by the add transformations button. Next, let's select the add field from the calculation 
transformation. Under mode, I'm going to select the mode of operation. Since this would be a 
basic binary operation, I'm going to select binary. You can refer to this table as a guideline 
to help you decide which modes to choose. Now, I'm going to select the operation and the 
calculation. I'll also give a new name to this column by updating the alias field. The 
transformation should be applied automatically. If not, you can click refresh to verify. All 
what's left now is to save the dashboard. To demo the group by transformation, I have 
another visualization here that shows the sales revenue for a specific region. I 
want to group by similar regions and get the total sales revenue for that region. 
To apply the group by transformation, click the transformations tab followed 
by the add transformations button. Next, let's select the group by transformation. You 
can also search for it. Then I'm going to select group by on the drop-down of the fields 
that I want to group by. In this example, it will be the region field that I want to group. 
Next, let's apply the calculation on the field we want to calculate and select a calculation type. 
In this example, it will be calculating the total sales amount per each region. The transformation 
should be applied automatically. If not, you can click refresh to verify. All 
that's left now is to save the dashboard. The next transformation that I'm going to demo is 
the filter data by values transformation. To demo the filter data by values transformation, 
I have the following visualization which shows a pie chart about browser market share. To 
apply the filter data by values transformation, click transformations tab followed by the add 
transformations button. Next, let's select the filter data by values transformation or 
you can search for it. On the filter type, select if you want an include or exclude filter. 
On the condition, select if you want the filter type to match all conditions or just match any. 
You can use the following table as a guideline for when to use the different conditions. In 
this example, I'm going to filter browsers that has lower than or equal to 5% market share. The 
transformation should be applied automatically. If not, you can click refresh to verify. All 
that's left now is to save the dashboard. Moving on to the join by field transformation. 
To demo this transformation, I have another visualization which shows two different queries. 
I want to combine these two queries into one table and join them by its ID. To apply the join by 
fill transformation, click the transformations tab followed by the add transformations button. 
Next, find the join by fill transformation. You can also search for it. Under mode, select how 
you want your queries to be joined. You can use the following table as a guideline for when 
to use the different modes. In this example, I'm going to choose inner join. Next, select 
the field to be joined from the two tables. In this example, it will be the product ID. The 
transformation should be applied automatically. If not, you can click refresh to verify. All 
that's left now is to save the dashboard. The final transformation that I'm going 
to demo is the organize fields by name. To demo this transformation, I have another 
visualization that shows different car makes and models and displays the information as 
a table. I want to hide some of the fields and rename some of them. To apply the 
organized fields by name transformation, click the transformations tab followed by the add 
transformations button. Next, find or search the transformation. Choose if you want to reorder the 
fields manually or automatically. In this example, I'm going to keep the option as manual. 
To hide some of the fields, click the eye icon to disable them. In this example, I'm going 
to hide the year and origin fields. I'm also going to rename the miles per gallon field. The 
transformation should be applied automatically. If not, you can click refresh to verify. All 
that's left now is to save the dashboard. In this milestone, you're going to learn 
how to export your data transformations outside Grafana Cloud. By default, 
Grafana doesn't support exporting your data transformations directly to an 
external database or other tools. However, you can export the data transformation manually 
as a CSV file. To export the transformation, click the queries tab and then the query 
inspector button. Select the data tab and expand the data options row. Enable the apply 
panel transformation option. And finally, click the download CSV button. You should now have a CSV 
file with a transformation applied to your data. Congratulations on completing this 
learning journey. I hope you enjoyed this video while you learn about the value 
of data transformations. how to apply common data transformations to your dashboard and 
finally how you can export them as a CSV file manually outside of Grafana Cloud. If you 
find this type of learning useful, why don't you check out the rest of our Grafana learning 
journeys at grafana.com/docs/learningjourneys. I hope to see you on the 
next one. Happy visualizing!

