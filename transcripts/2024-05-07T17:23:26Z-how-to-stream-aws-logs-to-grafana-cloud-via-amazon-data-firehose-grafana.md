# How to Stream AWS Logs to Grafana Cloud via Amazon Data Firehose | Grafana

In this video, we show you the steps to configure your Grafana account so you can start streaming AWS logs to Grafana Cloud ...

Published on 2024-05-07T17:23:26Z

URL: https://www.youtube.com/watch?v=2G9sm2WMUyg

Transcript: hi my name is Pablo and I am an engineer for grafana AWS observability team and we're going to talk about our new solution for moving logs from AWS leveraging fire host data streams this solution leverages Amazon data fire host previously known as Kinesis which is a fully managed service for delivering realtime data this will allow you to configure a fire host stream that will deliver all your B valuable AWS Lo data to grafana Cloud locky for all your long-terms storage and quering needs to configure just go into your graphon account and navigate through the knp on the left hand side under infrastructure AWS configuration once there just click the lock with fire host card that will take you to our configuration steps to configure you can use either cloud formation or terraform the steps are basically creating a grafana token launching the template for creating the infrastructure resources and then that's it once the data is Flowing you can go into grafana Explorer and look for the job label with the cloud AWS valy and that will fetch all your infrastructure locks that's it thanks for watching [Music]

