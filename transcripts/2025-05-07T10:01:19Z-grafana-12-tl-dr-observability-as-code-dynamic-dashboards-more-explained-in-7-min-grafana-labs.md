# Grafana 12 TL;DR: Observability as Code, Dynamic Dashboards &amp; More Explained in 7 Min | Grafana Labs

Grafana 12 is packed with major upgrades—from writing observability as code with the Foundation SDK to syncing changes via ...

Published on 2025-05-07T10:01:19Z

URL: https://www.youtube.com/watch?v=mHSzaVYBh38

Transcript: Grafana 12 is officially here and
boy, do we have a lot to cover, especially if your job entails
keeping teams, services, and a heck of a lot of
dashboards organized. My name is Shawn Pitts and in this
TL;DR we're going to hit you with the highlights fast, starting off with how
Grafana 12 lets you version, validate, and deploy dashboards like any other
code base in your organization. Let's jump in.
With the new Foundation SDK, you can now write dashboards
as strongly typed code. This means they're predictable, testable, and ready to drop into
your CI/CD pipelines. It's all backed by a refreshed set of
API schemas and has language support for Go, PHP, TypeScript, Python, and Java. But if you prefer to create
dashboards in the Grafana UI, Git Sync brings the whole observability
as code workflow full circle. The setup is super fast. Just connect
your repo, plug in your access token, and decide how you want to sync.
You can go all in and mirror your entire Grafana instance to Git or target a
specific folder if you want to keep things scoped and tidy. Once it's up and running, any dashboard edits gets tracked and
saved as Git changes. Update a panel, hit save, and instead of
going live immediately, Git Sync opens a new branch
and creates a pull request. Those changes are now
private to the editor. That means no surprises
for the rest of your org. Reviewers can jump straight from GitHub
into the updated dashboard preview. Thanks to auto-generated links and
comments, this process is now streamlined. Just merge the PR, jump back into Grafana, and with one click the dashboard changes
are made to your instance. And don't worry, we didn't forget
about the Terraform crowd. Grafana 12 doesn't just throw you a bone,
it's dropping an entire tool set here. We're talking about a brand new dashboard
resource structure that brings more flexibility, predictability and yes, validation. The new resource model gives
you explicit control over things like UIDs, titles, and tags without
hacking around in raw JSON. But the real magic is in the
validation. In older versions, if you made a mistake like accidentally
setting a panel's height to a negative value, Grafana would technically accept
it, but then quietly ghost the panel. Now Grafana tells you
exactly what went wrong, down to the field and index. Hey, panel zero's height can't be negative 23. That's the kind of tough love we
would like from our infra tooling. And it's not just dashboards. Playlists now follow the same
consistent schema pattern, metadata, options and spec. That means less mental overhead when
provisioning different resources and a smoother path as more elements adopt
this format in the future. Yeah, yeah, I hear you. Automation is cool, but what about the actual
experience of using Grafana? Well, Grafana 12 has made some massive
strides when it comes to usability and performance. We all know dashboards
can get messy real quick. There's too many panels, too many variables in a sea of data
points that sometimes are unneeded all at once. With Grafana 12, dynamic dashboards
transform how you edit, organize, and optimize your dashboards. Autogrid snapping now lines up
your panels instantly into clean, responsive layouts. You can fine tune layouts even further
by setting minimum column widths, like narrow and row heights, like short, giving you precise control
across different screen sizes. But a layout is just the start. Imagine you have variable like engineName
in your dashboard and only want to show specific panels and
rows based on the set value. Now we can do just that. As seen here, we'll hide this bottom row of panels
when the template variable engine name equals SQLite. We can show the top panels to autofit in
four columns and hide a panel when the query result has no data. Organizing
dashboards is better than ever as well. You can now group panels into tabs or
rows, drag your panels into a new row, set a max column count, say
four, and Grafana responsibly, reflows everything automatically. All of this adds up to a
faster cleaner experience, and that theme of speed continues. The
new blazing fast table panel is a full on engine rebuild. It handles
massive data sets with ease. We're talking 40,000 plus
rows, multi-column sorting, filtering and text wrapping, all
silky smooth. It's not just fast, it's absolutely frictionless.
And while we're making things smoother, let's talk alerts. Grafana supports
tool alerting rules. Data source alerts, which are evaluated at the
source like Prometheus, Mimir, or Loki and Grafana managed alerts, which are evaluated and
routed by Grafana itself. Grafana managed alerts unlocks
some powerful advantages. They work with any data source,
not just Prometheus, Loki, or Mimir. They support granular
access control. For example, you can decide who can view, edit, or
manage alert rules or contact points, and the authoring slash creation
experience is just better. And to those users who are already
ingrained with traditional data source alerts, we want to make the migration
process quick and easy for you. Grafana 12 introduces a managed alert migration
tool that makes moving your legacy data source alerts into Grafana managed
alerts very simple. Right from the UI, you can select your alerts,
decide where they land, choose to pause them to avoid noise, and even pull recording
rules along with them. The original rules stay in place
so you can run both in parallel, making migration safe, reversible,
and way less stressful. Basically, we finally made moving fast without
breaking things the default, not the exception. Grafana
12 doesn't just run faster. It looks sharper too. We're moving past
basic light and dark themes with five new styles. Desert Bloom, a softer,
colorful palette that's easy on the eyes. Gilded grove, more natural tones for
a clean, earthy feel. Bloom, a bold, high contrast, dark theme. Sapphire dusk, which brings out deep blues for a
calm focused workspace and Tron, a futuristic neon look for when
you want to turn up the intensity. And if you've ever needed to mash up data
from different sources like logs from Loki and BI data from Salesforce, traditionally that meant
exporting to a central warehouse, writing ETL jobs or giving up and
just doing math in a spreadsheet. In Grafana 12, we're bringing SQL
expressions to the table literally. In our demo, we're pulling logs from Loki, which is query A and revenue
data from BigQuery, query B. From query A, you can see we select
fields like committed ARR instance_id, year, month, billable series, and the sum of attribution. Then we join
that data with BigQuery using the org ID field as the key, aligning metrics
from two completely different systems. This breaks down data silos without
needing an ETL pipeline or a centralized data warehouse, just
write an SQL expression, transform when you need and
visualize it all in one panel. Okay, so your dashboards are automated,
beautiful and blazing fast, but what about your users? Right? Teams
change. People join in, people leave. So how do you keep all access clean and
up to date? That's where SCIM comes in. Grafana 12 brings full support
for SCIM based provisioning, making it dead simple to sync teams
straight from your top identity providers such as Okta, Azure AD, and more.
You can onboard entire teams, assign them to on-call schedules and get
them ready to receive alerts from day one. When someone leaves, their
access is revoked automatically. No delays and no manual cleanup. So yeah, Grafana 12 isn't just a version bump. It's a full blown upgrade to how teams
build, scale, and run observability. Thanks for watching. We can't wait to see what you build
with Grafana 12 and tune into the next video.

