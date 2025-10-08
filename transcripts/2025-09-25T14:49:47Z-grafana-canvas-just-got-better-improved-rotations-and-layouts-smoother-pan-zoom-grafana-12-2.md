# Grafana Canvas Just Got Better: Improved Rotations and Layouts, Smoother Pan &amp; Zoom | Grafana 12.2

Published on 2025-09-25T14:49:47Z

## Description

Grafana 12.2 introduces a rebuilt Canvas Pan & Zoom system that makes working with dashboards smoother and more intuitive.

URL: https://www.youtube.com/watch?v=xYcNnpfaBsk

## Summary

In this video, Ihor, a frontend engineer at Grafana Labs, presents the enhanced Canvas pan and zoom system designed to improve user experience in data visualization. He outlines the limitations of the previous Canvas system, such as restricted panning and unpredictable behavior during resizing, and contrasts it with the new version that offers smoother and more intuitive navigation. The updated system allows for infinite panning in any direction, stable connections for elements, and effective management of constraints, all while maintaining layout integrity. Key improvements also include element rotation that adapts to their actual shape and a new "zoom to intent" feature that ensures content fits perfectly on any screen. Ihor concludes by highlighting the benefits of the new Canvas, which enhances usability and flexibility for creating complex dashboards.

# Improved Canvas Pan and Zoom System

Hi, I'm Ihor, a frontend engineer on the data visualization team at Grafana Labs. Today, I will walk you through the improved Canvas pan and zoom system and show how it makes working in Canvas more intuitive and powerful.

## Previous Limitations

Let's start by looking at how Canvas worked before. Previously, Canvas supported panning, zooming, and even infinite panning, but the experience had some limitations that made layout management more challenging. For example:

- Panning was restricted to the panel area, making it harder to work with elements near the edges.
- Infinite panning could be enabled, but it didn't offer full flexibility for positioning elements outside the panel.
- Connections didn't always behave as expected.
- During Canvas resizing, the ground images scaled in ways that could be hard to predict.
- Switching off pan and zoom sometimes left the layout in an unintended state.

## Improved System

Now, let's take a look at the improved version. The new system is built from the ground up and offers smooth, predictable behavior similar to tools you already use for panning and zooming. This makes it much easier to create and manage complex dashboards.

### Key Features of the New System

- **Infinite Panning**: You can now pan infinitely in any direction.
- **Flexible Element Placement**: Place elements beyond the canvas edge.
- **Stable Connections**: Keep connections stable and accurate.
- **Consistent Root Container**: Pin the ground images through a consistent root container.
- **Toggle Pan and Zoom**: You can toggle pan and zoom off without breaking your layout.

### Maintaining Constraints

You may wonder what happens to constraints when pan and zoom is enabled. We have handled that too. Canvas now uses an invisible root container sized to the panel to maintain your constraints, even when pan and zoom are active. 

Here's an example with four elements, each with different constraints. Notice how all constraints are preserved, and the element positions stay consistent. Let me add the grounds so you can see the container more clearly. This ensures that constraints remain usable and predictable in any zoom state.

### Improved Element Rotation

We have also improved element rotation. Previously, connection anchors were always based on a rectangular mounting box, even if your element had a custom shape. Now, connection anchors follow the actual shape and rotate naturally with the element. Existing connections update automatically as you rotate.

### Zoom to Intent Toggle

You might have seen the new **Zoom to Intent** toggle. This feature is perfect for large panels with many elements. Instead of manually adjusting panel size or worrying about how your dashboard looks on different screens, this toggle ensures your content always fits within view on any screen or panel size. Just enable it, and everything stays visible without extra effort.

## Summary

To sum up, here is what the new Canvas gives you:

- Smooth pan and zoom
- Infinite panning
- Constrained, friendly layout
- Smarter rotation
- Zoom to content for perfect visibility
- Ability to toggle back to the default view anytime

Thanks for watching, and enjoy your new and improved Canvas!

## Raw YouTube Transcript

Hi, I'm Ihor, a frontend engineer on the data
visualization team at Grafana Labs. Today, I will walk you through the improved
Canvas pan and zoom system and show how it makes work
in Canvas more intuitive and powerful. Let's start by looking at how
Canvas worked before. Previously, Canvas supported panning, zooming, and even infinite panning, but the experience had
some limitations that made layout management more
challenging. For example, panning was restricted to the panel area, making it harder to work
with elements near the edges. Infinite panning could be enabled, but it didn't offer full
flexibility for positioning elements outside the panel. Connections didn't always
behave as expected. During Canvas resizing, the ground images scaled
in ways that could be hard to predict, and switching off pan and
zoom sometimes left the layout in an unintended state. Now let's take a look
at the improved version. The new system is built
from the ground up. It offers smooth, predictable behavior similar to
tools you already use for panning and zooming, making it much easier to
create and manage complex dashboards. You can now pan infinitely
in any direction, place elements beyond the canvas edge, keep connection stable and accurate. Pin the ground images through
a consistent root container and toggle pan and zoom off
without breaking your layout. You may wonder, what happens to constrained when pan and zoom is enabled? We have handled that too. Canvas now uses an
invisible root container sized to the panel to
maintain your constraints, even then pan and zoom. Here's an example with four elements, each with different constraints. Notice how all constraints are
preserved and the element positions stay consistent. Let me add the grounds so
you can see the container more clearly. This ensures constraints
remain usable and predictable in any zone state. We have also improved element rotation.
Previously connection anchors were always based on a rectangular mounting box, even if your element has a custom shape. Now connection anchors follow
the actual shape and rotate naturally with the element. Existing connections
update automatically as you rotate. You might have seen the
new zoom to intent toggle. This is perfect for large
panels with many elements. Instead of manually adjusting
panel size or worrying how your dashboard looks
on different screens, this toggle ensures your
content always fit within view on any screen or panel size. Just enable it and everything
stays visible without extra effort. To sum up, here is what the new
canvas gives you. Smooth pan and zoom, infinite panning,
constrained, friendly layout, smarter rotation, and zoom to content for perfect visibility and the ability to toggle
back to the default view anytime. Thanks for watching and enjoy
your new and improved canvas.

