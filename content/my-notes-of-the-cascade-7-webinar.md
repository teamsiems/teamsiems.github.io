Title: My Notes of the Cascade 7 Webinar
Date: 2012-06-05 14:34
Author: chris
Category: Personal
Tags: Cascade, cms
Slug: my-notes-of-the-cascade-7-webinar
Status: published

My notes from the webinar about Cascade 7. Hannon Hill should have a video of this webinar on their site in a week or so.
June 5, 2012
Bradley Wagner
Themes
1. Portability
2. Performance
3. End-user experience
4. Interface/usability
Vitals
1. Released May 8, 2012
2. Over 65 downloads
3. 2 Betas and client survey
4. 400+ Votes satisfied
5. Features for all stakeholders and user
roles
DEMO: Content Portability
whole-site export that downloads .csse files
DEMO: Database export utility
everything expect binary files
DEMO: Site Clone/Copy
It keeps local references local to the copied site, and
external references (\\_common) stay external.
DEMO: Move/Rename Unpublish
Auto-unpublish when assets are moved/renamed. This
works on manual as well as expired assets (expiration folder
set).
DEMO: Modules
Easy way to add content e.g. twitter feed.
New \>\> Block \>\> Twitter Feed
Also swap out assets (blocks) on a page. with Inline
Regions
It dynamically updates the published page with new
Tweets!
DEMO: Spectate Connector
SAS marketing tool. Makes (empty) forms really easily.
Create connector in Cascade first, then use a new button on wysiwyg to drop
in form. Also, processes form data e.g. send email.
DEMO: Features - Caching (index
blocks)
Speeds up render on Cascade.
DEMO: Features - Improved History
Type ahead with action list when users scroll over
items.
DEMO: Features - Global Search
Type ahead added.
DEMO: Improved HTML5 Support
Embed video as HTML5. CAVEAT: Chrome doesn’t like
to render videos inline, but Safari will (Why?)
Also, improved Tidy - HTML5 nicer
My Questions:
Q: How does site copy handle locked files?
A: (They didn't answer, but I think it will make a copy of the last saved version.)
Q: How does it hand internal asset references? One of
the problems we have when we copy now with 6.10.9 is
“hotlinking” images (or other assets).
A: It keeps local references local to the copied site,
and external references (\\_common) stay external.
Other Answers
Common assets (e.g. \\_common) need to exist before a site is copied.
Transport passwords are encrypted.
