# She Built a Dungeon Crawler That Runs on Kubernetes (with Grafana!) | Brogue

Published on 2025-06-07T05:35:48Z

## Description

What happens when you mix Kubernetes with an old-school dungeon crawler? Cloud engineer Kim Schaefer hacked the game ...

URL: https://www.youtube.com/watch?v=VNyMDnrg3iM

## Summary

In this YouTube video, cloud infrastructure engineer Kim Schaefer presents his innovative project, a Kubernetes-based dungeon crawl game inspired by KubeDOOM and Doomfana. He discusses how he adapted an open-source game called Bro to run within a Kubernetes cluster, utilizing operators and Custom Resource Definitions (CRDs) to create dynamic interactions between the game's mechanics and the cluster's state. Key features include the spawning of monsters represented as deployments in the cluster, real-time updates on monster health through a custom landing page, and the use of Grafana for visualization and monitoring. Kim highlights his focus on configuration ease, real-time data handling, and future enhancements such as cloud deployment and deeper metric integration. He invites viewers to connect and explore his GitHub repository for further insights into the project's architecture.

# Kubernetes Dungeon Crawl Project Presentation

Good afternoon! My name is **Kim Schaefer**, and I am a cloud infrastructure engineer. Today, I want to share my **Kubernetes Dungeon Crawl Project** and discuss how **Grafana** plays a role in tying everything together.

## Project Inspiration

The basic inspiration for this project combines elements from **KubeDOOM** and **Doomfana**. I took an old-school dungeon crawl game called **Bro**, which is open source, and adapted it to run in a Kubernetes cluster. My focus was on using **operators** and **Custom Resource Definitions (CRDs)** so that actions in the game would impact the cluster and vice versa. 

### Game Mechanics

Let's dive into the mechanics of how creatures enter the game:

1. **Monster Spawn**:
   - Monsters enter the game through normal gameplay via monster spawns. When this occurs, a deployment in the **monster Namespace** is created that represents that monster. This deployment contains an **Nginx pod** with a custom landing page displaying details and stats about the monster.
   - As players engage with the monster, updates will appear on that page, showing health decreases when attacked.

2. **Manual Spawn**:
   - A monster can also be spawned by creating a pod in the monster namespace, which triggers the same deployment process as mentioned above.

### Player Interaction

When a player kills a monster:
- The deployment representing that monster is destroyed.
- If the monster has a pod, that pod is destroyed as well. However, due to Kubernetes' nature, the pod will respawn, bringing the monster back to life in the cluster. 

This means players should be cautious about how many monsters they create, as it can make the game significantly more difficult.

### Cheat Mode

Every game needs a cheat mode! In this project:
- If you delete a deployment in the cluster, it will kill the corresponding monster in the game.
- Deleting a monster pod will delete the deployment and the monster, but the pod will respawn, reviving the monster.

## Key Project Components

1. **Game Modifications**:
   - I modified the game to handle **POST** and **GET** requests for information exchange.
   
2. **Portal**:
   - The portal operates as a **Flask API**, providing endpoints for the game to interact with and manage CRDs representing monsters.

3. **Kubernetes Controller**:
   - The controller, referred to as the **Dungeon Master**, orchestrates all operations within the cluster.

### Integrating Grafana

As I was assembling everything, I realized I needed a **magic mirror** to tie everything together visually. This is where **Grafana** came into play. 

Here’s a screenshot of the game interface. You’ll notice the naming convention for monsters (e.g., **monstie-21** and **jackal-4**). The numbers help associate in-game monsters with their corresponding pods and deployments.

### Portal Features

The portal features:
- A basic landing page.
- A list of alive and dead monsters in the cluster, with monster names as links for easy navigation to detailed pages.
- A fun **red button** at the bottom for players who want to quickly kill a monster without engaging.

Additionally, you can view player information, equipment, and game state details like levels and gold. 

### Custom 404 Page

I created a custom **404 page** for added fun, as the standard one felt lacking when trying to visit a monster page that wasn’t fully operational or had been defeated.

## Dashboard Insights

Before the dashboard, I used tools like **canines** or **kubectl commands** to interact with the cluster. The dashboard enhances the experience by allowing you to see real-time updates as you play. For example, when I kill a monstie, the monster count updates dynamically.

### Key Learnings

1. **Configuration**:
   - I aimed for a one-command setup. I used a config map for Grafana, eliminating the need for manual dashboard configurations.

2. **Embedding**:
   - Integrating video or live streams into the dashboard significantly enhances its utility and user experience.

3. **Data Management**:
   - I utilized **Prometheus metrics** and data from the API and cluster. Understanding which data needs real-time updates versus historical data was crucial for effective management.

## Next Steps

The next steps for the project include:
- Drilling down into metrics on the dashboard.
- Getting the project up and running in a **Google Cloud GKE cluster** for broader access.
- Exploring further with CRDs and the controller.

If you have any questions or would like to discuss the project further, feel free to reach out. You can also check out the **GitHub repo** for architecture diagrams and more information.

Thank you for your time!

## Raw YouTube Transcript

Good afternoon. My name is Kim Schaefer
and I'm a cloud infrastructure engineer. And today what I want to talk to you
about and share with you is my Kubernetes dungeon crawl project and how Grafana
ended up playing a role in tying it all together. So the basic inspiration behind the
game in the project was a combination of KubeDOOM and Doomfana, and basically what I decided to do was
take an old school dungeon crawl game called Bro, and since it's open source, I was able to adapt it to
run in a Kubernetes cluster, and I really wanted to focus on using
operators and CRDs so that I could have what happens in the game impact what
happens in the cluster and vice versa. So actions in the cluster would have
an impact on the actual gameplay. To help explain that a little bit more, let's take a look at what happens when
a creature comes into the game. So the first way that happens is through the
normal gameplay amongst Monster response. Whenever that happens, a deployment in the monster Namespace
is created that represents that monster, and in that deployment,
there's an Engine X pod, and that pod has a custom landing page
that shows you all the details and stats about the monster. And
as you engage with the monster, you're going to see updates on that page.
So if you start attacking a monster, you're going to see that health go
down on that custom landing page. The second way a monster gets into
the game is if you create a pod in the monster namespace, that's going to then
cause a monster's spawn in the game, which then recreates what I just talked
about with the monster deployment. The second area of the interaction
is when a player kills a monster. So the first thing that happens when
you kill a monster in the game is any deployment out there that represents
that monster is going to be destroyed. Now if that monster happens to have
a monthly pod that represents it, that pod is going to be destroyed as well. But because of the magic of Kubernetes,
that pod's going to come back, which is going to basically bring that
monster back to life in the cluster. So the real lesson behind that was be
careful how many of these monies you create because you can make the game
extremely difficult if you keep creating these monsters. Now, every game needs a
cheap mode of some sort. So what I did is if you're in the
cluster and you delete a deployment, that's going to kill the
monster in the game. Likewise, if you delete a musty pod that's
going to delete the deployment, delete the monster. But then again, that pod's going to come back to life
and that monster is going to come back to life. The key project segments for what
I did was first, there's the game. I went in and I modified it so that it
can use posts and get requests to get information in and out of the game. The portal is a Flask API that kind
of has those endpoints that the game interacts with, but
then it also can create, update and delete CRDs that
represent the monsters. That's how you get that connection
between the game and the cluster itself. The Kubernetes controller that I can refer
to as the dungeon master is basically what makes all the magic
happen within the cluster. As I went through and was
putting everything together, I then realized that I really needed a
magic mirror because as you're going to see here in a second, there's all sorts
of pages and screens and displays, and I needed a way to tie it all together,
and that's where Grafana came in. So this is just a screenshot of the game. I have a video of it later on so
you can see the actual interaction. The only way that you can really tell
what I've done on this screen is you'll notice where it says
monstie-21 and jackal-4. The numbers that are
after the names there, I put in there to make it
easier to associate the
monsters in the game with the pods and deployments in the clusters. The monstie is an actual
monster in the game, but I gave it that tag of monstie so that
you can tell that very quickly that it actually represents a pod. For the portal itself, you
have a basic landing page, but then you can also go in and take a
look at all the monsters that are both alive and dead in the
cluster. Importantly, if you take a look, you'll be able to see that those monster
names for the alive monsters are links. That's the easy way that you can get to
see these pages that show you all the details of that monster. And
of course, to make it fun, I had to add a red button at the bottom
so that if you just want to kill the monster and not deal with it, you
can just click the red button. Yes, I know you can use kubectl commands, but
the red button is just much more fun. You can take a look at all sorts of
player information and equipment. You can take a look at game
state information about
levels and gold and things like that. You can also take
a look at just the monsties. And remember, those are the pods or the monsters that
are created from pods in the monsties namespace. They have the same play
in the game as any other monster, but they're created by the pods. So this page I set up largely to make
it easy for me to quickly generate those pods, but then of course, I had to have
more red buttons to kill more things. Now, there were times where I would either
try to visit a monster page before it was fully up and running, or I try to visit it after the
monster had already been killed. The standard 404 page just
wasn't doing it for me. So to just have even more
fun with the project, I created my own custom 404
page that has its own separate set up within the game. It doesn't affect
anything, it just makes it more fun. This screen is basically just showing
you that before I had the dashboard to interact with a cluster, I would
either use canines or kubectl commands. There's nothing wrong with
that, but as you can see here, this was a much better solution. So
I'm not actually playing the game live, I'm just not good enough at the game
to do that. So this is recorded, but you can see that as I play the game, you can see the stats on the
right hand side will update. You'll be able to tell when I kill a
monstie, you'll see that monster count, like what just happened.
It'll go from six to five, and then it's going to go back up to
six because that pod was recreated. So you can see everything right there. The bottom row is actually just
stats coming from the cluster itself, just because I figured since
it is a Kubernetes project, I should have something Kubernetes
related on the dashboard. Now, the key learning points that I
got from this is one - configuration. I wanted to be able to literally enter
one command and have everything come up. I didn't want to have to go back in and
do any sort of configuration to get the Grafana dashboard done. So what I did is I went through
and I set up in the container for Grafana. I have everything
as a config map, so I don't actually have to do any
manual configuration of that dashboard. It just comes up with one
command. Everything running. Embedding was also important. That dashboard, without being able
to play the game from the dashboard, just wouldn't be the same. So it really showed me that being able
to tie in different types of video or live streams into the dashboard can
make a huge difference on how useful and helpful that dashboard can be.
The data that I was working with, I have Prometheus metrics.
I've got the data from the API, and then data that I can
get from the cluster itself. And what I learned is there's some
things that I needed to have real time or close to it. So for example, if
you're attacking a monster and all, you need to be able to see your health
in real time to know how much danger you're in. There's other things like the statistics
about how much gold you've collected over time. That can come from a Prometheus metric
instead because you don't need to have that real time. So it just made me realize that you
really need to think through and identify what your data sources are and
which one is best for which purpose. So thanks for coming and letting me share my project with you. The next steps for the project are one, I want to be able to start drilling down
into those metrics on the dashboard. You saw all the data that I'm
actually collecting from the game. I'd like to pull more of that
into the dashboard as drilDdowns. I love playing this game
on my local computer, but the next step is going to be to get
it up and running in a Google Cloud GKE cluster, because I just think it's so
much fun that it belongs out in the cloud. And there's also some more things I want
to do - working and exploring with the CRDs and the controller. If
you want to stay in touch, I'm happy to answer any questions or
just chat about the project in general. And you can also check out the GitHub
repo where you can also take a look at the different architecture diagrams
behind the project. Thank you.

