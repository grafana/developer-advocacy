# Grafana 11 Features for Developers | Grafana

Grafana 11 is now GA! In this video, we do a deep dive exploring all of the new features for our developers. In this video, learn ...

Published on 2024-05-17T08:07:02Z

URL: https://www.youtube.com/watch?v=na-6pHC1Gx4

Transcript: Welcome to Grafana 11 for the
developers. In this video, we'll deep dive into
all of the new features, which are important for those who
just have an itch to extend Grafana's capabilities even further.  Grafana users and operators do not panic. There are dedicated
videos for you as well. Let's jump straight into one of
the most exciting new features. Plugin scaffolding. We wanted to reduce the friction in
setting up your development environment, ready to build plugins for Grafana. Entire plugins can now be
scaffolded with just one command. Let's jump into VS Code and
see how this can be done. The scaffolding feature can be called
using the following package managers, npm, pnmp, and Yarn. In this example, I'm just going to use npm. To start, we run the command npx
@grafana/create-plugin@latest. Now, we can start running through the
scaffolding form. You start with a name, organization, and description. Now we can choose the type of plugging
that we would like to scaffold. This could be app, data
source, panel, or Scenes app. We are gonna go with a Scenes app. You can also choose whether an app
has a backend. In our instance, we're going to be making
use of another data source, so we are going to select no. And finally, you can have continuous integration and
release workflows included if you like. After filling out this form, this will
create a fully scaffolding plugin, including a source, app config, pages, and a docker compose file.
We'll get to this in a moment. Next, we'll run through the post
scaffolding commands. First, you need to CD into the directory (that's your new plugin), run npm install, then we can install the
end-to-end test dependencies. We can then run and build our front
end to look at the codes and see it's running correctly. And finally, we can do a Docker compose up in a
separate terminal to create a test Grafana server so we can
see our new app running. We hope this feature will
help to standardize the way
our community builds apps for Grafana, as well as greasing the wheels for new
developers to start extending Grafana. The Saga design system hasn't been
specifically released for Grafana 11, but deserves an honorable mention since
it continues to be updated and improved. The Saga design system's goal is
building a well organized set of design elements, patterns, and guidelines that ensure visual
and functional consistency across all of our products. It is a guiding resource to equipped
in Grafanistas and our community with pre-established components and principles
for crafting visually appealing and easy-to-use interfaces. Let's quickly jump into
Saga design and take a look. I can access Saga design via
grafana.com/developers. From there, I can see a roadmap for
future iterations to Saga, as well as to start to navigate different
design principles and components. Let's suppose I want to
learn about adding an input. I can select input found within
components. From this page, I can see a working example,
implementation and option guidelines, as well as a working sandbox. And that's it for our Grafana
developers walkthrough. There are plenty more
features for you to discover, such as Scenes-powered visualizations
and decoupled plugging access to services such as navigation, search, and RBAC. We hope these features will help to
improve your experience as you expand the capabilities of Grafana. Make sure you check out our Grafana
11 videos for the operators and users for more great features
in Grafana 11. Once again, a massive thank you to our Grafanista
developers and our community for making Grafana 11 possible.

