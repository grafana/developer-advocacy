# Grafana Assistant Helps Keep Restaurants Running... SpotOn Explains How

Published on 2025-10-22T16:36:06Z

## Description

At SpotOn, reliability means everything — because when a restaurant can't operate, customers and revenue are at risk. Hear from ...

URL: https://www.youtube.com/watch?v=gvsSJwFfR3w

## Summary

In this video, Jeremy White, the leader of the platform engineering team at SpotOn, discusses how the company supports restaurants through various technological solutions, particularly focusing on observability and reliability. SpotOn's products help restaurants manage orders, payments, marketing, and employee management, with the aim of allowing them to concentrate on their guests rather than technical issues. White emphasizes the importance of observability in preventing operational disruptions in restaurants, especially given the challenging environments of kitchens. He highlights the usefulness of Grafana Assistant in improving observability participation among engineers, facilitating faster dashboard creation, and aiding teams in troubleshooting issues more efficiently. White shares a success story about the client environment team, who, despite not being familiar with Grafana, utilized the tool to create proactive dashboards, enhancing customer support. Ultimately, he advocates for Grafana Assistant as a means to boost observability adoption and focus on resolving customer issues effectively.

## Chapters

00:00:00 Introductions and Overview of SpotOn  
00:01:30 Importance of Observability for Restaurants  
00:02:15 Challenges Faced with Hardware and Environment  
00:03:00 Role of Grafana Assistant in Observability  
00:04:10 Overcoming the Blank Sheet of Paper Problem  
00:05:00 Example of Client Environment Team Using Grafana Assistant  
00:06:30 Proactive Problem Identification with Dashboards  
00:07:15 Managing Alerts and Reducing Reactive Work  
00:08:00 Grafana Assistant's Contribution to Troubleshooting  
00:09:15 Conclusion and Encouragement to Use Grafana Assistant  

# The Importance of Observability at SpotOn

Hi everyone, I'm Jeremy White. I have the privilege of leading the platform engineering team at SpotOn. At SpotOn, we help restaurants run successful businesses through our point of sale system and a suite of other products. These products assist with various tasks, such as taking orders, processing payments, running marketing campaigns, managing employees and tips, and ultimately working towards making restaurants more profitable.

Our goal is simple: we aim to ensure that our restaurants focus on their guests rather than on the underlying tools.

## Observability and Reliability

For us, **observability** is much more than just dashboards and alerts. Reliability is crucial to ensuring our customers can operate effectively. We understand that restaurants depend on us to run their businesses smoothly. One of the worst nightmares for a restaurant is having to close its doors, forcing them to turn away both staff and guests. This is something we are committed to preventing.

The challenge we face extends beyond the cloud; we support hardware in thousands of restaurants and kitchens across the country. These environments deal with high heat and grease, and kitchens often resemble Faraday cages, making Wi-Fi connectivity challenging. Therefore, we rely on observability to help us understand and stay ahead of potential issues, avoiding disruptions to our customers' operations.

## The Role of Grafana Assistant

Observability is effective only when people actively use it. This is where **Grafana Assistant** has been particularly beneficial for us. It has transformed the onboarding experience for new engineers who may not be familiar with where our logs and metrics are located for various services. With Grafana Assistant, they can engage in incidents and triage issues simply by conversing with an AI agent, eliminating the need for extensive training.

Grafana Assistant has also been helpful in managing dependencies across our many products. As teams span different products, the assistant makes it easier for those unfamiliar with different systems to bridge the knowledge gap. 

One of the features I appreciate most is how it addresses the **blank sheet of paper problem**. This issue can make it difficult to get started, but with Grafana Assistant, users can transition straight from ideas to dashboards, allowing for quicker iterations. This ease of use has significantly boosted our participation in observability and expedited the time to value for our customers.

## Success Stories

One of my favorite examples of this is our **client environment team**, composed of network support specialists. Their primary goal is to ensure that client networks operate smoothly without impacting business operations. These team members were not experts in Grafana and were unfamiliar with the tooling, but they successfully utilized Grafana Assistant to create dashboards. These dashboards provided insights into a single restaurant, displaying all network devices and potential issues in one place, enabling them to triage problems more efficiently.

Moreover, they continued to innovate, creating additional dashboards that allowed us to proactively identify groups of customers experiencing issues. This proactive approach enabled our support team to reach out and resolve problems before customers even had to call us for help. This exemplifies how our teams can focus on being subject matter experts and solving customer problems rather than getting bogged down by the tooling.

However, we sometimes generate so many signals that it can overwhelm our development teams, leading to more reactive work than anticipated. For instance, anyone familiar with Kubernetes knows about the **Kubernetes pod crash looping alert**, which can fail for numerous reasons. We found that Grafana Assistant can help decorate that alert with additional context, making troubleshooting easier. In one case, it identified a null pointer reference during a transformation process in one of our services right at the moment it occurred during a release. This made troubleshooting more efficient and less time-consuming, facilitating a quicker resolution.

While it may not always pinpoint the exact cause or solution, Grafana Assistant helps build confidence in what to investigate and can rule some issues out, thus accelerating our resolution process.

## Conclusion

Overall, we are excited about the capabilities of Grafana Assistant. It has lowered the barrier to entry, encouraging greater participation and engagement across our teams in observability. It has sped up the time to value by addressing the blank sheet of paper problem and has allowed us to concentrate on solving customer issues and achieving customer outcomes rather than focusing solely on the underlying tools.

If anyone else is interested in accelerating their observability adoption, I encourage you to take a look at Grafana Assistant.

## Raw YouTube Transcript

Hi everyone, I'm Jeremy White. I have the privilege of leading the platform engineering team at SpotOn. So at SpotOn, we help restaurants run successful businesses. We do this through our point of sale. We have a suite of other products that help handle things such as taking orders, processing payments, running marketing campaigns, managing employees and tips, and ultimately trying to become more profitable as a business. And our goal is pretty simple. We try to make sure that our restaurants are focused on their guests, not on the underlying tooling. Now, for us, observability is a lot more than just about dashboards and alerts. Reliability is really how we make sure our customers are able to operate because we understand our restaurants depend on us in order to have successful business. One of the worst nightmares that a restaurant can consider is having to close their doors for some reason and having to turn away their their staff and their guests. And that's something that we aim to try to prevent from happening. And the challenge is bigger than just the cloud. We support hardware that's in thousands of restaurants and kitchens across the country. These are places where you deal with a lot of heat, you deal with a lot of grease. The kitchens are basically fairday cages, so Wi-Fi is not so great. So, we rely on observability to help us understand and stay ahead of a lot of those problems in order to avoid interrupting their business and their day-to-day operations. Now, observability only works when people are actually using it. And this is one of the areas where we found Graphana Assistant really helped us out. It's gone from having new engineers stepping in and not being familiar with where our logs and metrics are for all the different services and actively being able to participate in incidents and triaging. And again, this is all from basically having a conversation with an AI agent as opposed to having to go through all that training and understanding. It's also been helpful with dependencies. We have a lot of different products. So as you span into different products and have to understand how different teams have instrumented their systems again assistant able to bridge that gap a lot easier for people not familiar with those teams. One of the areas I really enjoy about it is it solves the blank sheet of paper problem. This is the problem where sometimes it can be a little difficult to get started, right? But with graphana assistant, we found that some people could go straight from idea to dashboard and then iterate and that iteration was a lot easier for people to handle as opposed to solving that blank sheet of paper problem. So this has been a huge boost uh to our participation in observability as well as the speed to value and how quickly we can get to value for our customers. One of my favorite examples of this is our client environment team. Now this is a team of network support specialists. Their goal is to try and make sure that the client networks are operating successfully and not impacting the business at all in any way, shape or form. Now these are not Graphfana experts, not even familiar with the tooling, but they were able to use Graphfana Assistant to get started and create dashboards. dashboards that could look at one restaurant and be able to tell all the network devices, all the possible problems we might be seeing, pull it together in one place and allow them to triage those issues a lot faster. But they didn't stop there. They kept moving even though they weren't familiar with the tool and started to build additional dashboards that moved more to a proactive nature. One where we could identify groups of customers that were experiencing issues that we could contact our support team and have them reach out to the customers and solve the problem before the customer called us asking for help. This is a great example of where our team can focus on being subject matter experts and focus on solving customer problems, not on the tooling. Sometimes though we end up generating so many signals that it can overwhelm some of our development teams and cause more reactive work than we expected. An example of this is for anyone familiar with Kubernetes is a cube pod crash looping alert. So this is a common alert that has a hund different reasons for why it could fail. Uh and and what we found is we can use graphana assistant to decorate that alert and provide additional context of why it happened because again not all engineers are used to troubleshooting this particular issue. So what that did is we had one case where it even found a null pointer reference during a transformation process in one of our services. It noticed right when it happened during the release and so it made it a lot easier and a lot less timeconuming for us to troubleshoot that issue and ultimately get to a solution. So while it doesn't always pinpoint the exact example and the exact solution, it does help build confidence on what to look into and sometimes what not to look into because it rules some things out. So, this has really helped us get to that resolution a lot faster. Overall, we're really excited with the capabilities of Grafana Assistant. It's really lowered that barrier of entry, allowing us to get more participation and engagement across our teams and observability. It's sped up that time to value by solving that blank sheet of paper problem. And ultimately, it's allowed us to really focus on solving customer problems and getting to customer outcomes rather than the underlying tooling. So if anyone else is interested in accelerating their observability adoption, I'd encourage you to take a look at graphon assistant.

