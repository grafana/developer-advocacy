
Project docs are the main source of truth for all instructional content about the projects at Grafana Labs. The docs for each project are stored within the project repository. Each repo should have a `CONTRIBUTING.md` page that outlines the process for writing documentation for it in more detail, but below are some general steps.

## (Recommended) Contact the docs person(s) assigned to the project

Every project has a person from the docs team assigned to maintain the documentation. It's a good idea to talk to the person assigned to the repo you want to contribute to, especially if you plan to make ongoing contributions to it. This will prevent duplicate effort and let them know what you're working on.

You can find out who the right person to reach out to is by going to the Slack channel for the project and asking there, or asking one of us.

## Set up your local environment

### Clone the project repo locally

First, clone the project repo locally. `cd` to the directory you want the project repo to be in and then run the `git clone` command with the address of the repo like this:

```shell
git clone https://github.com/grafana/loki.git
```

The Cloud docs are not project-specific and are held in [the Grafana website repo](https://github.com/grafana/website).

### Create a new branch

Within the GitHub UI, create a new branch for your changes. Different projects might use different naming conventions, but something like `docs-revamp-logql-page` would work.

Once created in the remote GitHub, create a new branch locally and switch to it:

```shell
git checkout -b docs-revamp-logql-page
```

Then, set up the local branch to track information from the remote branch like this:

```shell
git branch --set-upstream-to=origin/docs-revamp-logql-page docs-revamp-logql-page
```

Do a `git pull` to verify that it's all working. If both branches are empty, you should get a `Already up to date` message back.

### Deploy locally

If you're just changing something small, like a typo, you may be able to skip this step and go straight to making the change and creating the PR. However, if you're changing something more substantial, you need to be able to check that your changes render correctly. To do this, you can deploy a local version of the project docs that shows you your changes the way a user would see them.

#### Docker

Make sure you have the [Docker Desktop daemon](https://www.docker.com/) running. Docs at Grafana Labs use [Hugo](https://gohugo.io/), an open-source static site generator written in Go, but the Docker image lets you skip installing Hugo and Go.

#### Start the Hugo server

Every project repo has a `docs` directory. `cd` to the that directory. Then, run:

```shell
make docs
```
This command uses the `make` utility to build the docs site and start the Hugo server using the instructions in the `Makefile`. After a few seconds, you should see something like this:

```shell
Built in 1769 ms
Environment: "docs"
Serving pages from disk
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:3002/ (bind address 0.0.0.0)

View documentation locally:
  http://localhost:3002/docs/loki/latest/

Press Ctrl+C to stop the server
```

Visit the URL on a browser, and you should see the docs site rendered. From now on, any changes you make will automatically be reflected here too.

## Make your changes

Now you can make the changes you want! The [Writers' Tookit](https://grafana.com/docs/writers-toolkit/) has a bunch of useful information about how you can plan out larger changes depending on your goals. The [Style Guide](https://grafana.com/docs/writers-toolkit/write/style-guide/) has some information on how to strike a tone grammatically that is consistent with the writing on docs.

> **Warning**
> If your docs changes include adding media (such as screenshots or diagrams), follow [these instructions](https://grafana.com/docs/writers-toolkit/write/image-guidelines/#where-to-store-media-assets) to upload them to right shared folder.

If you get stuck, talk to that handy docs person you contacted earlier. They are your friend! You should do what you can to make their job easier in terms of style and grammar, but in general, they'll still be extremely happy you're helping them. Don't hold off on making changes because you're afraid you've gotten something wrong.

Commit and push your changes to your branch.

## Create a PR

On GitHub, if you go to the repository, you may also just see a message on top that says `newbranch had recent pushes 1 minute ago`. Click the button *Compare & pull request*.

Otherwise, create a pull request from your branch to the `main` branch (use `main` as base). 

Then, type out a brief description of what you changed. Click *Create pull request* when you're done.

Wait for the checks to complete. This part could take a while. Tag your friendly docs person and any other engineers (if relevant/necessary) as reviewers. Wait!

## After reviews

Once your changes have been approved by all reviewers, you don't have to do anything else! After your PR is merged and all the CI jobs run, you'll see your changes publicly, but in the `/next` section. See, at Grafana, docs changes only show up in the main site when a release is created. So initially, they'll be visible only in `next` like this: [https://grafana.com/docs/loki/next](https://grafana.com/docs/loki/next). After the next release, they'll show up in `/latest:` [https://grafana.com/docs/loki/](https://grafana.com/docs/loki/).

But that's just a bit of waiting. For now, your changes are made and this job is done.