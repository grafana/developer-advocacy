# Demo: Kubernetes support in Grafana Beyla

In this demo, we walk through the capabilities in Grafana Beyla to integrate with Kubernetes workloads: service selectors and ...

Published on 2024-01-24T17:09:10Z

URL: https://www.youtube.com/watch?v=kLxXJKp768s

Transcript: today we will talk about how kubernetes became a first class citizen in grafana baa to demonstrate the integration of baa with kubernetes we have deployed a demo application formed by multiple services and poorts in this demo application we have a l generator poort that sends HTTP requests to a front end which forwards them to a back end and this back end communicates grpc with multiple worker pods this demo application is already deploy it in kubernetes we have this front end this load generator which is a simple pot the front end the back end and the worker we will deploy the configuration as a config map so on one side we have configured the routing just to provide some hortic information and grouping of the roots and then we will tell baa for example we only want to select this or to instrument this PO we have this discovery section in which we say okay in the demo name space we only want to instrument the services that belong to a deployment name matching the front end string apart of that we will need to do some extra config configuration to let baa get information or expect information about kubernetes so on one side we have deployed this service account and this cluster role that allows baa to list and watch for replica sets and PS and then we bind this cluster rooll to this daa service account then we can deploy baa as a diamond set so uh for that we need to specify that or the service account that we use to deploy the diamond set is this baa service account that has been binded to this cluster role it's also important to let baa to access the host pit as it is deployed as a demon set it is able to access to every process deployed on that diamond set the configuration file with the discovery configuration is mounted as a volume and then we specify that this configuration can be accessed there we need also to enable the C metadata and here we provide the the grafana open Telemetry exporter information this is the end point and the heers with the authentication which have been deployed as a secret so let's deploy daa we see that the B La PO is running we can see that for example in the ls of Baya H Baya found a process name frontend it is the only process it is instrumenting because we say that we only wanted to instrument any process belonging to the to the front end uh pot so Baya should be already sending information if we go to grafana uh you can we will be able to see these uh traces here the we only see the frontend traces you can also see how this service is visible in the for example in the application observability plugin if we go to the service map we can see this front end demo service so uh we we were able to configure baa to select only a sub of the running services so let's try to remove this restriction and instrument all the processes in the demo name space we only have the the services uh for this application the front end the backend the load generator and the workers so let's redeploy baa so if now we get the logs of baa of the new baa instance you can see that now baa has found many other processes in the in the logs a process name front end another back name back end another name uh worker and another name Lo gen for the load generator uh we we were able to do a a broaden instrumentation instrument more services but even restricted only to this demo name space now if we go to the service map after a while we shall see that this map has been updated okay so now we are able to see all the services there the load generator the front end that calls to the backend and calls to the worker so if we click on any of the services we can go to the service overview so when we go to the service overview not all the data will be there it will take few minutes one two minutes to populate also the the metrics but in the meanwhile this information is populated we can go to the traces section and see how the traces have been captured if we click on any of the traces you will see not only the single spans for this front or or for this uh in that case backend application but all the distributed traces for all the different processes and after some minutes we see that the uh overview of of the services is populated with metrics like the duration the errors and rate of of the different requests so the the the demo introduces some some errors on P post just to demonstrate this work you can see the dependencies downstream and Upstream so you see that this backend service sends data to the worker and gets H requests from the front end you can see the operations and the duration thank you for your attention feel free to visit the grafana vaa documentation site for more information about how to make baa to work with kubernetes and other topics
