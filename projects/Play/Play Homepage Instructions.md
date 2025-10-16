# Play Homepage

This README outlines instructions on updating some of the panels on the Play Homepage. 

You need edit permissions to edit any of the panels. Please ask Marie Cruz if you require permissions.

## Storing images

All images are stored in this [folder](projects/Play/images). 

Once saved, the image link will be `https://raw.githubusercontent.com/grafana/developer-advocacy/refs/heads/main/projects/Play/images/<IMAGE_FILENAME>`

## Dashboard of the Month

1. Navigate to https://play.grafana.org/d/to6j8mh/home-refresh-2025?orgId=1&from=now-6h&to=now&timezone=utc&editPanel=3 
1. Scroll down to the `Content` section
1. Update the following HTML code with the new dashboard details. Refer to the inline comments for more information.

```html
<div class="panel-body dashboard-highlight">
  <!-- Add the image link here and make sure to update the `alt` attribute. -->
  <img src="https://grafana.com/media/solutions/kubernetes/kubernetes-monitoring-in-grafana-landing.png" alt="Carbon Intensity Dashboard" class="dashboard-preview" />

  <div class="panel-text dashboard-description">
    <div class="dashboard-details">
      <div>
        <h3>
          <!-- Add the dashboard link and update the link text -->
          <a href="https://play.grafana.org/d/siw7lpj/uk-carbon-intensity" target="_blank">UK Carbon Intensity</a>
        </h3>
        <!-- Add dashboard description -->
        <p>This dashboard provides a visualisation of the UK carbon intensity using the Infinity plugin.</p>
      </div>

      <div class="creator-callout">
        <div class="creator-label">🌟 Meet the creator</div>
        <div class="creator-name">
          <!-- Add a link to the dashboard creator's image and update the `alt` attribute-->
          <img src="https://s3.amazonaws.com/a-us.storyblok.com/f/1022730/71e18eec16/simon-prickett.jpg" alt="Simon Prickett" class="creator-avatar" />
          <div>
            <!-- Update name and role -->
            <div>Simon Prickett</div>
            <div class="creator-role">Senior Developer Advocate</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

## Featured Contributor

1. Navigate to https://play.grafana.org/d/to6j8mh/home-refresh-2025?orgId=1&from=now-6h&to=now&timezone=utc&editPanel=8
1. Scroll down to the `Content` section
1. Update the following HTML code with the new contributor details. Refer to the inline comments for more information.

```html
<div class="panel-body contributor-panel">
  <div class="contributor-header">
    <!-- Add a link to the contributor's image and update the `alt` attribute-->
    <img src="https://s3.amazonaws.com/a-us.storyblok.com/f/1022730/3b98648975/marie_drake.jpg" alt="Marie Cruz" class="contributor-avatar" />
    <div class="contributor-info">
      <!-- Update name and role -->
      <div class="contributor-name">Marie Cruz</div>
      <div class="contributor-role">Senior Developer Advocate</div>
    </div>
  </div>
  <div class="contributor-body">
    <!-- Update description -->
    <p>Marie has been with Grafana Labs for 3 years now and it’s an amazing company!</p>
    <p>As a Senior Developer Advocate, she teaches the community about recommended practices when it comes to
      observability and how to use our awesome products here at Grafana Labs.</p>
      <!-- Add link to work -->
    <p>Check out some of her work <a href="#">here</a>!</p>
  </div>
</div>
```

## Featured Dashboards

1. Navigate to https://play.grafana.org/d/maggk2z/featured-dashboards?orgId=1&from=now-6h&to=now&timezone=utc&editPanel=1
1. Scroll down to the `Content` section
1. Update the following HTML code with the new dashboard details. Refer to the inline comments for more information.

```html
<!-- Update dashboard link -->
<a href="https://play.grafana.org/d/mabqw4b/tripadvisor" class="launchpad-tile">
        <!-- Update dashboard name and image -->
        <div class="tile-title">London Trip Advisor</div>
        <img src="https://raw.githubusercontent.com/grafana/developer-advocacy/refs/heads/main/projects/Play/images/trip-advisor.png" alt="London Trip Advisor" />
      </a>
```
