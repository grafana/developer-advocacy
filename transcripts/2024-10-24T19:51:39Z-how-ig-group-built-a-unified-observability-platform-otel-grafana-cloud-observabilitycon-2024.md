# How IG Group Built a Unified Observability Platform | OTel &amp; Grafana Cloud | ObservabilityCON 2024

Join Natalie Ujuk, observability technical lead at IG Group, as she shares the company's three-year journey in building an ...

Published on 2024-10-24T19:51:39Z

URL: https://www.youtube.com/watch?v=Y7cz9S36wag

Transcript: Good morning everyone. It's great to be here in New York and
I'm really excited to be speaking here today. My name is Natalie Ujuk and I'm the
observability technical lead at IG Group. A little about me. I'm originally
from Sydney, Australia, but I currently live in London
and I have been for some time now. I have over 20 years experience working
in the monitoring space in a number of different industries,
from telecommunications
to logistics to finance, just to name a few. I love to travel and I've been fortunate
enough to work in a number of cities in Australia, around the
UK, and around Europe. I'm excited to share IG's observability
journey with you and how we have embraced an observability by default
culture with Grafana Cloud. Now, to tell you a little bit about
IG, I have a video for you. Spoiler alert. IG doesn't
stand for Instagram. Trading. Your mind can work against you. Succumb to pressure, create chaos, or stay calm in the eye of the storm. If you are committed to
developing your trader mindset, we are committed to helping
you get there. Teddy. . IG, where traders are made. IG Group is a leading provider of
online trading and investment services. With its headquarters in London
and 18 offices around the world. IG Group operates a number
of brands worldwide. One of IG's most recent acquisitions
was Tasty Trade here in the US in 2021. Tasty Trade specializes in
options and futures trading. IG's goal is to become the home of
active traders by putting clients at the heart of our business. Technology is key and is our
differentiator that sets us, sets IG apart in the market. We have over 850 engineers worldwide, located in our tech hubs in London,
Bangalore, Krakow, and Chicago. Today I'll be walking you through why
we have built an observability platform, what it entails and how we are making it
part of a default engineering culture. I'll start with the reasons
behind this initiative, exploring the challenges we faced
and the goals we set out to achieve. Then I'll dive into the specifics
of what we've built from our use of OpenTelemetry to our unified
view in Grafana Cloud. Finally, I'll explain how we've implemented it
in a way that reduces complexity for developers and enhances
the developer experience. I'll get straight into the why. At IG, we began our observability journey three
years ago to address some significant challenges. At the time, we had faced issues with both
missing and duplicate data sets, making it difficult to answer
key technical questions
and business questions. Our focus was heavily internal rather
than being aligned with what truly mattered to our customer experience. Data about our applications was
siloed with domain specific tools accessible only through subject matter
experts adding layers of complexity, delays and even bias. This resulted in a cycle of
merely addressing symptoms
without reducing the toil or directly improving the customer
experience. To break this cycle, we set out to build an observability
platform capable of correlating all our data into a single source of truth, a platform that would reflect the health
of our services as perceived by our customers, understandable to
anyone across the organization. In building our platform, we considered
the following design principles. Standards were a top priority and
we wanted to define them early on. This would ensure we would
correlate between data sources. The standards would extend beyond
tags and would apply to data values, collection patterns,
and also visualization. The tooling selection would be
as vendor agnostic as possible, allowing us flexibility in changing
tool direction down the road without the headache of mass migration projects. We also wanted to adopt the
principle of everything as code. This was to overcome past challenges
where configuration relied on a central team to make changes through a UI. By shifting to code driven automation, we ensure a consistent reliant
and scalable platform while significantly reducing
dependency bottlenecks. Our platform is built
around three key goals, customer centricity, data democratization,
and providing a unified view. The platform would put a spotlight on
our customers and connect engineering effort with real user experience. Second, all data would be democratized, ensuring that its data is accessible
to everyone and breaking down the silos and we would provide a unified view that
would allow everyone to be on the same page. To bring all of this together, we built a centralized
observability engineering team. The responsibilities of this team
were to define best practices for observability across the organization and to build a platform with the
design principles and goals in mind. There was one final thing that
set the direction of our platform. All applications will be
observable by default. Our architect, James, not pictured here, boldly declared this vision one day
and it pretty much set the tone for everything that followed. In a perfect world - one with a
simplified technology stack - making all applications observable by
default would be an easy ask. But at IG we were dealing
with a complex tech stack. The underlying infrastructure
is a mix of on-prem and cloud. There's a myriad of languages and
libraries and technologies plus legacy code legacy systems and the deeply
ingrained habits that come with them. There was also people that
were resistant to change, having seen past attempts to
change the way we work fail. We had to overcome
skepticism, technical debt, cultural inertia to make
this vision a reality. I'll now dive into the platform
we built and the tooling we chose. OpenTelemetry is at the
core of our platform, enabling us to be as vendor agnostic
while implementing standard collection patterns. We've been closely following OpenTelemetry
development over the past few years and we now have adopted the all
telemetry signals as they have matured. We've also adopted the semantic
conventions as our default standard. We originally introduced IG specific
tags to align with our CMDB, but we have since dropped those IG tags
in favor of OpenTelemetry conventions. Grafana Cloud plays a central role in
our platform and I'm pleased to say that we've built a strong partnership
with Grafana over the years. We utilize Tempo as our traces
store and Mimir for our metrics. In our platform's early stages,
we initially used Influx, but we have since transitioned to Mimir
for better performance and scalability. Grafana Cloud also allows us to build our
first pane of glass and create a set of standardized dashboards that are
accessible to everyone at IG. Additionally, we use several enterprise plugins
to connect with our existing tools, further enhancing our
ability to correlate data. We do use Splunk as our logging
workflow as it's been in IG for around 10 years and as well established. Maybe one day we'll
make the shift to Loki. We also use integrate
PagerDuty and ServiceNow to for incident and alert notification. Our architecture. Initially we focused building the
platform to support applications hosted on-prem as majority of
applications are based there. OpenTelemetry collectors are configured
with default pipelines allowing applications to send to local host. A metrics and traces receiver is enabled
by default and all data is exported to Kafka. We manage OpenTelemetry gateways that
receive from Kafka and send to relevant data stores. In the gateways,
we are able to validate, gate and transform the
data before it's exported. The gateways also perform sampling
decisions on the tracing pipeline. We continue to use the Splunk Forwarder
on the logging flow as it's already established. However, there's potential for us to collapse that
collective footprint in the future and change our direction for tooling for logs. The architecture has now expanded to
support new initiatives such as our nomad container platform and
the adoption of cloud. The OpenTelemetry collector pattern
was replicated for these environments. Observability by default was easiest
for our to achieve in nomad platform. This was because it was incorporated
from the very beginning as a default standard. For AWS, since there are many AWS services, we continue to build out new
patterns to support them. The challenge with cloud comes as we
need to route the data through our gateways, which sit on-prem. We had considered running our
separate gateways in the cloud, but we were required to route all the
traces through the central gateway for sampling decisions.
However, down the line, we may opt to shift them
to cloud and if we do that, we'll be able to do it seamlessly without
impact or concern to application side. Our unified view provides a comprehensive, at-a-glance insight into service
health for any service or application sending telemetry. We ensure consistency and ease of
understanding by creating dashboards per application or technology
type like HTTP or JVM. What's powerful is that these views are
dynamically generated for any service using standard tags, meaning engineers can easily see their
data as soon as they instrument their applications that is provided
they're using the mandatory tags. We've also incorporated user-centric
service level objectives, ensuring that measuring user experience
and correlating it along with service health. We align closely with
Grafana's big tent ethos, which provides the flexibility to choose
the right tooling while maintaining a unified view. Our goal is to
minimize tool sprawl at IG, but we also recognize
that in certain cases, domain specific tools are necessary, whether it's for its
specialized capabilities, greater value or cost
effectiveness. For example, LogicMonitor is essential
for our network engineers. We integrate its data feed
into our unified view, allowing all engineering teams to easily
view network health. Additionally, we integrate key engineering
tools like GitLab, ServiceNow, and PagerDuty to provide enriched
context around service health. This allows us to correlate
incidents with specific code commits, giving teams realtime insights into
exactly when and where changes occurred, making root cause analysis
faster and more precise. So in summary, some of the defaults that we have
included are OpenTelemetry collectors available on all our VMs and container
platform with default signal pipelines. We've ensured that the
collector configurations
remain as default as possible, allowing us to manage complexity
centrally in our gateways. This setup significantly simplifies
the developer experience by reducing concerns. For developers, the main requirement is to instrument
their application with OpenTelemetry. Majority of our applications are Java, so for them it's a process of simply
attaching the OpenTelemetry Java agent to the Java process. To
utilize the unified view, we require engineers to include mandatory
tags such as service dot name and service dot namespace. The value of
these tags align with the golden source, our CMDB, which ensures that we're correlating
only a single instance of each service, maintaining accuracy and
consistency in our view. Lastly, our unified view comprises over 30
dashboards to cover a wide range of technologies. So they say if you build
it, they will come...But will they? . We've had, we used a critical business flow as an
exemplar during the first iteration of our platform. We use this as
a showcase to drive adoption. Even at the time, we had challenges with securing developer
time to instrument the full flow. This was due to different engineering
teams contributing to that single user journey. Adoption of the
platform was slow and steady. Admittedly, our first onboarding
guide had around 30 steps. But we have since reduced this by limiting
the concerns of the developers and providing self-service capabilities. We
were able to reduce this to just three. Send it. Developers will instrument their
applications with OpenTelemetry using auto instrumentation, SDKs or
APIs. Observe it. Utilize the dashboards in the unified
view, and third... Alert on it. Implement an alert on SLOs
for their application. Even though we had simplified
the onboarding guide, adoption was slow and we were under
pressure by management to increase our adoption stats and that's when that's when management issued a
mandate to all development teams. You must onboard the
observability platform. It was established as a minimum
criteria for release maturity. Following this mandate, we did
observe a rise in adoption stats. That is the number of applications
emitting this three signals and measuring SLOs were on the rise. However, we began to question whether the
unified view was being used and and if teams truly understood SLOs or if they
were simply just copying another team's SLO configuration. While numbers indicated
increased activity, we wanted to ensure that
teams were genuinely engaging
with the platform rather than just fulfilling a
compliance requirement. It became clear that this was
leading to superficial compliance. There was lack of deep
engagement with the platform, which undermined a culture
of ownership among the teams. Instead of fully embracing the platform
and understanding the tools and practices, developers
were merely ticking boxes. There was a missed opportunity for teams
to learn about their applications while gaining new skills. On a positive note, the rise in adoption allowed us
to have more data on the platform, which was great for us because we were
able to further validate and improve it. However, the lack of engagement from the developers
limited the quality of feedback that we received preventing us from
delivering what was important to them. While adoption numbers
look great on a dashboard, they didn't reflect a healthy
observability culture. We needed to shift our focus from
mere compliance to fostering a deeper understanding and ownership of tools
and practices we have in place. So how did we make that shift for
engineers to embrace observability? We fostered a learning and feedback
culture by showcasing our platform in a variety of ways, from informal demos to individuals
and to teams all the way to larger tech talk style roadshows
that were company wide. What's really exciting is how we
saw a shift over time. Initially, the observability team led the demos,
however, as we progress progressed, developers began to showcase the
platform's value to their peers. This peer-led approach not only
highlighted real world examples, but also created a sense of ownership
and community among our devs. We also established a
central place for feedback, ensuring transparency around how set
suggestions were being implemented. This mechanism allowed everyone to
feel heard and valued and created a continuous loop of improvement. Next, cross team collaboration. Learning
is truly a two-way street. We wanted our users to learn about the
platform and how to interact with our applications through telemetry, but we also wanted to understand the
developer's ways of working and the challenges they faced. To facilitate this, we actively collaborated with multiple
teams while working on new capabilities, and this accelerated the capabilities
that we were able to provide. Gaining leadership support is important
to understanding the why It's important for observability for leadership, and it's also important that we embed
that into engineering best practices and I'll talk a bit more about
that in the next few slides. At an observability road
show that we held internally, our CTO Adam Will Wright shared why
observability is important for IG. He said "The reason that this matters is
because it will drive commercial value, and that's why I'm passionate
about it." He also said, "I'm not looking to pay more money
to Grafana or any other partners. That might be an inevitability, but that's not the primary
reason for doing this. It's not so that Natalie can write, she's got a platform observability
on her cv. That will be great, but that's not the primary
reason for doing this. The primary reason is because
of the commercial outcomes
and why I think it's so important that we do lean into this
and why we have built this into our engineering best practices." As engineers, we do more than right
lines of code. We design, we build, we manage our applications in the same
way that observability is more than just signals. It is a signal
single source of truth. Connecting code deploys
to user experience. When incorporated into
engineering best practices, it empowers high performing teams and
allows 'em to ship quality code to production fast. Fast feedback loops are essential
in ensuring this is done safely. This in turn ensures that IG has high
performing and reliable technology that outperforms our competitors and ultimately
resulting in customer satisfaction. Let's take a moment to reflect back
to the video I played at the start. Just like IG is committed to helping
our customers who are the traders, develop their trading mindset and stay
calm in the eye of the storm by reducing chaos and pressure. Developing an observability
mindset is key for our engineers, so they too remain calm
and perform at their best. Engineer happiness
equals trader happiness. Three years on our platform is now
well established with OpenTelemetry and Grafana Cloud as its foundations. It is a platform built by engineers
for engineers and we continue to ensure that everyone has access to this single
source of truth that connects us to our customer's experience. There's so much more we'd like to explore. While OpenTelemetry order instrumentation
is a great starting point, we see significant opportunities
to enhance our data with additional application and business logic. Our goal is to get even
closer to understanding the
user experience. Recently, we collaborated with our
frontend engineers to explore
Grafana Faro capabilities and we're currently in the process
of productionizing this capability. We also want to ensure that all critical
customer journeys are traced to end to end and are measured by
service level objectives. We plan to build out further
cloud patterns to support
various AWS services as more applications either shift to cloud
or are built cloud first. Finally, we aim to implement dashboards as code
capability and encourage the engineering community to contribute
to the unified view. Thank you all for listening. If you would like to connect my
LinkedIn QR code is on the screen. I look forward to connecting with you
all and continuing this conversation. Thank you.

