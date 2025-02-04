# Extra Security for Plugins: Plugin Frontend Sandbox in Grafana 11.5 | Grafana Labs

Grafana plugins offer powerful new visualization options and extended functionality—but with great power comes great ...

Published on 2025-01-29T17:35:01Z

URL: https://www.youtube.com/watch?v=o7qsMDgFdug

Transcript: Hey, let's talk about the plugin
frontend sandbox. I'm Esteban. I'm a software engineer on the
plugins platform team at Grafana Labs. So what problem does the plugin frontend
sandbox software can offer powerful functionality, new visualizations
options, which you can take advantage of, but those new options can sometimes
create risk or increase risk. You may be hesitant to, in general, install third party plugins from the
community or want to additional security guarantees for plugins that you are
already using. Our catalog is big. So that is why we built the
plugin frontend sandbox. It provides an extra layer
of security-isolated plugins, so they cannot access other parts of
your Grafana interface, interfere, other plugins, or affect core functionality -
allowing you to confidentially use plugins while keeping your instance
protected. So how does it work? Let me show you. If you are in Grafana
Cloud, you can go to the plugin catalog, which we're showing
right now on the screen, and you can find the plugin that you want.
To enable the sandbox, we're going to
use the ACE.SVG plugin as an example. Over here you can see that the plugin
is already installed and we can also see that there is a switch
here for the frontend sandbox. To enable the frontend
sandbox in this plugin, all you have to do is
toggle the switch on, and now we'll have this
plugin running in the sandbox. If we go to a dashboard
that I previously created, you can see that the plugin
is running exactly as before, but now it has an extra layer of security. So whenever anything inside of this panel, when to access anything outside
of this panel, it cannot do it. So if you are not in Grafana Cloud and you are in a local instance,
you can go to your configuration file. You'll have to enable the feature
toggle plugins frontend sandbox, and you can use the enable frontend
sandbox for plugins configuration key inside the security configuration path, and comma-separate plugin IDs of
plugins you want protected in the sandbox. If you want to disable the frontend
sandbox for any reason that might be, it could be that you don't
need the extra security, or it can be that this plugin
is not working as suspected. You can safely switch it off in cloud or remove it from your configuration file
and restart Grafana in case you are not in cloud. The plugin frontend sandbox is included
in all Grafana editions starting from 11.5. It makes it accessible for
everyone to have enhanced security. We invite you to check the documentation
in the plugin management of how to enable the frontend sandbox and the
compatibility so you can start using this functionality right away.

