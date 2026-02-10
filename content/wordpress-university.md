Title: WordPress University
Date: 2009-10-08 08:25
Author: chris
Category: Education
Tags: cms, heweb09, wrk14
Slug: wordpress-university
Status: published

Stephanie Leary  
Website Administrator, Texas A&M University

October 7

<div id="__ss_2200988" style="width: 425px; text-align: left;">

<a href="http://www.slideshare.net/stephanieleary/wordpress-as-a-cms-2200988" style="font: 14px Helvetica,Arial,Sans-serif; display: block; margin: 12px 0 3px 0; text-decoration: underline;" title="WordPress as a CMS">WordPress as a CMS</a>
<object style="margin: 0px;" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="425" height="355" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0">

<param name="allowFullScreen" value="true"></param><param name="allowScriptAccess" value="always"></param><param name="src" value="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=wp-u-key-091012144502-phpapp02&amp;rel=0&amp;stripped_title=wordpress-as-a-cms-2200988"></param><param name="allowfullscreen" value="true"></param>
<embed style="margin: 0px;" type="application/x-shockwave-flash" width="425" height="355" src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=wp-u-key-091012144502-phpapp02&amp;rel=0&amp;stripped_title=wordpress-as-a-cms-2200988" allowscriptaccess="always" allowfullscreen="true">

</embed>

</object>

</p>

<div style="font-size: 11px; font-family: tahoma,arial; height: 26px; padding-top: 2px;">

View more <a href="http://www.slideshare.net/" style="text-decoration: underline;">presentations</a> from <a href="http://www.slideshare.net/stephanieleary" style="text-decoration: underline;">Stephanie Leary</a>.

</div>

</div>

**CMS Capabilities**

- posts and pages
- scheduled publishing
- basic workflow
- easy media embedding
- excellent seo
- ubiquitous feeds

Killer Feature is the User Interface. (made by [happycog](http://www.happycog.com/))

**Post vs. Page**

Posts have...

- included in feeds
- categories
- tags
- excerpts
- comments and trackbacks
- custom fields

Pages have...

- not included in feeds
- page parent (not categories)
- template
- menu order
- comments and trackbacks
- custom fields

Pages can...with plugins

- included in feeds
- categories
- tags

The dirty little secret because pages are posts and posts are pages.

Things that are posts

- blogs
- news archives
- press releases
- podcasts
- newsletters
- magazines
- journals
- â€¦

Things that are posts

- anything you want in a feed
- anything organized by date

Things that are pages

- anything that does not change often
- anything that is not organized by date

Other things

- media uploads
- users
- links

Demo

- installation
- file import
- basic options
- reading settings
- permalinks

Less blog, more CMS

- magazine-style home pages
- great url structure
- no category or archives
- contextual navigation
- breadcrumbs
- subpage listings

Magazine Layout

- multiple content areas
- category sections
- list of subpages
- widgets

Required theme files

- index.php
- style.css

Other recommendations

- functions.php - this is where you define widgets
- screenshot.png

More files

category.php = global category theme

category-6.php = category theme for catid=6

How a theme file works

- get_header
- The Loop
- get_sidebar
- get_footer

sandbox, hybrid, thematic themes to start looking at

Inside The Loop

- title
- content/excerpt
- date
- categories
- tags
- author
- custom fields

Complicating matters

- custom loops
- multiple loops

Modify the query (query_posts)

- limit
- offset
- parent
- categories & tags (include/exclude)
- sort order
- type
- author
- status

**Sidebars**

one included by default - get_sidebar()

can use more than one with php file include syntax

**Widgets**

theme/plugin hybrid

can be defined in functions.php or installed as part of a plugin

**Built-in Widgets**

- archives
- categories
- calendar
- links
- RSS
- pages
- meta (log in/out, feed)
- recent posts
- tag cloud
- text

Plugins

6735 plugins and growing

Plugins can...

- add widgets
- create template tags
- modify loops
- create shortcodes
- alter user roles
- provide custom fields
- alter write screens
- add JS libraries

Putting it all together

We want...

- pages
- a blog
- subscribe to comments
- a podcast
- a contact form w/spam guard
- a private area
- users to be redirected on login

Sidbar login plugin

Peter's login redirect

Problems with private

visibility: menus

granularity: groups

privileges: roles

Plugin to fix this - Role manager (for now)

\[PressThis podcast talks about world press\]

Hiding the admin area

- sidebar login
- front-end editor
- P2
- posthaste

Moving servers

- changing domains
- edit database fields
- use config file constants
- changing directories
- maintaining permalinks

Caching Plugins

- WP Cache
- Super Cache
- W3 Total Cache

What's New in 2.9

- image editor
- trash (posts, pages, comments)
- new excerpt filters
- easy changes to contact profile fields
- included handbook (printable)
- category-slug.php

What's different in MU

- each user gets a blog
- each blog gets a set of db tables
- users can't upload themes or plugins
- site-wide plugins installed for all
- site admin screen (and role)

Calendar plugin: AMR ICAL Event
