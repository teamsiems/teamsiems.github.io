Title: TinyMCE hack to shoehorn Paul Irish conditional statements into Cascade Server
Date: 2013-03-12 10:19
Author: chris
Category: Technology
Tags: Cascade, code, hack, html5, php
Slug: tinymce-hack-to-shoehorn-paul-irish-conditional-statements-into-cascade-server
Status: published

Here is some code to shoehorn [Paul Irish's conditional statements for Internet Explorer](http://paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/) into Hannon Hill's Cascade Server using PHP's ob_start() function. This is a mashup from [a few people](https://gist.github.com/seedprod/422679) on the [Cascade help forum](http://help.hannonhill.com/discussions/how-do-i/414-html5-html5boilerplate-conditional-comments). Really, it's a TinyMCE (Cascade's WYSIWYG editor) hack to get conditional code, i.e. comments, around the HTML tag. I know it's a very specific use case, but if you are trying to make your web site responsive using HTML5 Boilerplate in Cascade you'll want this. (Irony: WordPress's WYSIWYG editor won't save the code correctly so I took a screen shot.)

[<img src="https://res.cloudinary.com/teamsiems/images/w_1024,h_232,c_scale/v1585938187/paul-irish-cascade/paul-irish-cascade.gif?_i=AA" class="aligncenter size-large wp-image-3819" width="584" height="132" alt="Paul Irish Cascade hack" />](http://teamsiems.com/wp-content/uploads/2013/03/paul-irish-cascade.gif)

**UPDATE**

Hannon Hill added a set of special tags in version 7.4 of Cascade that allow code - even "illegal" code - to sit in a page unrendered. You'll find it in their knowledge base under [Code Sections](http://www.hannonhill.com/kb/Code-Sections/). Below is a revised version of the Boilerplate conditional statements using the new "protect-top" tag.

[<img src="https://res.cloudinary.com/teamsiems/images/v1585938188/protect-top-cascade/protect-top-cascade.gif?_i=AA" class="aligncenter size-full wp-image-3938" width="639" height="123" alt="protect-top-cascade" />](https://res.cloudinary.com/teamsiems/images/v1585938188/protect-top-cascade/protect-top-cascade.gif?_i=AA)
