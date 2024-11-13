# AngularJS Deprecation Warnings in 10.4 | Grafana

Angular support was deprecated in Grafana 9 and will be removed in Grafana 11. AngularJS is an old frontend framework whose ...

Published on 2024-03-06T19:52:19Z

URL: https://www.youtube.com/watch?v=XlEVs6g8dC8

Transcript: [Music] hi I'm jpe software engineer at grafana Labs angular support was deprecated in grafana 9 and will be removed in grafana 11 due to this all dashboards depending on panel or data source plugins using angular will stop working and will require migrating to a react based plug-in to facilitate identifying dashboards that use angular panel plugins or data sources we have introduced warnings on affected dashboards this complements the existing warnings within the catalog on plugins themselves grafana now displays a warning at the top of the page when viewing a dashboard that uses angular plugins grafana also displays an icon next to each panel that is using an angular plug-in this allows you to identify exactly which panels require your attention so that they don't stop working once angular support is removed when editing a panel that uses an angular plug-in grafana now displays a similar warning on the panel options pane or the data source pane we have also built detect angular dashboards an open-source tool that scans your grafana instance using the grafana API and lists all dashboards that use angular plugins this is especially useful for grafana instances with a large number of dashboards and can be combined with usage insights to help you prioritize fixes you can download this tool from from the GitHub repository grafana / detect D angular Das dashboards don't forget to check out our documentation on angular deprecation to learn why we are doing this and how this might affect you to ensure your dashboards will keep working once angular support is removed from grafana

