# How to Automatically Remediate Incidents with Grafana IRM

Build automatic remediation workflows to preemptively resolve system issues and minimize downtime. With observability-native ...

Published on 2024-09-05T14:48:39Z

URL: https://www.youtube.com/watch?v=it-BCdo7hZg

Transcript: hi this is VJ tilani in this video I'll show you how to set up automated remediation workflows using escalation chains web Hooks and Integrations all using grafana irm this helps you prevent outages when you're not able to respond quickly enough and makes being on call just a bit less stressful in this common scenario we're alerted that the dis supporting one of our databases is almost full we'll take a look at our dashboard and sure enough we see 6% free dis space this is a fairly common issue so we built in automated remediation workflow to help prevent outages here we see that workflow kicking in triggering a GitHub action grafana irm offers Integrations with GitHub service now jira and a number of other tools to support a variety of workflows we see that GitHub action calls terraform to scale our database dis and if we look at our terraform apply we can see where we scale our requests and limits from 1 gig to 2 gig of disc by automating this action I bought myself time and avoided the stress of another firefighting situation looks like our Auto remediation has completed we can see before this started we were at 6% free dis space our Auto remediation began finished and when it was done we're at 54% free dis space grafana on call escalation chains are primarily used to notify the right responder and get them to perform the right actions to resolve issues in this demo we've shown you how you can automate operational workflows with incoming and outgoing web hooks the possibilities are endless here we see when this error condition is met we not only send a slack notification but there's an escalation train which triggers a web hook to execute a GitHub action orchestrating automated remediation leads to fewer mistakes which helps improve reliability and reduce the stress of being on call try building your own automated remediation workflows with grafana irm on grafana cloud today [Music]
