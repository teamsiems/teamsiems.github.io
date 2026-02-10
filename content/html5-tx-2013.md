Title: HTML5.tx 2013
Date: 2013-02-07 13:56
Author: chris
Category: Technology
Tags: Austin, css3, html5, javascript, Texas
Slug: html5-tx-2013
Status: published

I attended HTML5.tx in Austin, Texas, February 1-3. Friday, February 1, was 8 hours of CSS3. Saturday was a series of 7, 1 hour-long talks. Sunday was 5 hours of JavaScript. Here is a brain-dump of my notes.

## Links

- [HTML5.tx](http://html5tx.com/)
- [@HTML5TX](https://twitter.com/HTML5TX)
- [Schedule](http://lanyrd.com/2013/html5tx/schedule/)
- [Capital Factory](http://www.capitalfactory.com/)
- [@capitalfactory](https://twitter.com/capitalfactory)

## Friday

CSS: from Knowledgable to Ninja  
Estelle Weyl  
@estellevw  
http://standardista.com/  
http://estelle.github.com/CSS-Workshop/

Course Outline Selectors Specificity  
Generated Content  
Media Queries  
Debugging  
Colors & Transparency  
Fonts / Typography  
Backgrounds & Borders  
Gradients  
Transforms  
Transitions & Animation  
Other Features

http://copypastecharacter.com/

data-FOO is HTML5 for creating your own attribute.

http://caniuse.com

http://modern.ie

## Saturday

Adaptive Images for Responsive Web Design  
Chris Schmitt  
http://github.com/teleject/hisrc/

http://www.useragentstring.com/

Feature Testing  
1) width  
2) screen resolution  
3) bandwidth

but speed test hinder ux

there is native speed test  
modernizer network-connection.js

Img old school  
1) .htaccess  
2) \<picture\> and or srcset  
3) HiSRC

hisrc.js w/ jquery.js  
and data-1x, data-2x  
or  
css media queries and single-pixel gif replacement

Workarounds  
1) background-size:auto (fittextjs.com)  
2) svg  
3) font-based solutions  
4) compressed jpeg (not for high contrast)

Img new school  
1) simple design for users  
2) browser, server handshake  
3) same,...

DOM  
codylindley.com/domit

1\. document node  
2. element node  
3. text node  
encompass 90% of nodes

jQuery = "find something, do something"

The New Rules of the Responsive Web  
@matthew_carver  
http://www.slideshare.net/matthewcarver/new-rules-of-the-responsive-web

"The Responsive Web"  
Use code 13rw37 for 37% off book  
http://manning.com/carver/

Tech has changed in the last 18 months.

People create with big device, consume with small device.

Rules:

1\) responsive design doesn't end with squishing

2\) there is no responsive pixie dust

Think: prototyping

3\) your workflow will change

Think: style tiles

4\) your tools will change

Think: CSS preprocessors; scss, sass, less  
Book: SMACSS (lumberjack book)

5\) the web is responsive by default

6\) embrace unpredictability

LIGHTNING TALKS

Aaron Murray  
10 Minutes that can save hours of debugging headaches  
or Dodging Javascript pitfalls  
@aaronkmurray

In developer console

parseInt(010) - octal = 8

a == true doesn't check type  
=== does check type

----------------------------------------------------

Ryan Joy  
Drop the widgets  
embrace html5

@atxryan  
ryanjoy.com

\<form\>  
\<progress\>  
autocomplete  
drag and drop  
audio and video  
contenteditable  
javascript (sizzle)  
css  
input type=date  
color picker input type=color  
context menu

----------------------------------------------------

Austin Hallock  
clay.io

html5 games - cross platform  
\<canvas\>  
github.com/austinhallock/html5.tx

10 Things You Didn't Know Browsers Could Do  
Estelle Weyl  
@estellevw  
estelle.github.com/10

1\) \$('selector') without jquery  
Selectors API

2\) everything is editable  
contentEditable()

3\) can store lots of data  
local storage  
session storage  
webSQL (webkit)  
indexedDB  
your whole site with appcache

4\) svg as background image

5\) count with css

6\) css can calculate

7\) IE6 and IE7 can buy you a house

8\) take your picture  
navigator.getusermedia

9\) animate sprites

10\) help you manage memory

HTML5 on TV  
Mike Taylor  
github.com/pepelsbey/shower

Opera is everywhere

beware of overscan

navigation - spatial navigation (keyboard)

input

libraries - microjs

vanilla-js.com

javascript, html5 & DOM

storage

cookies

audio/video

tools

opera tv emulator  
dragonfly

templates

dev.opera.com/tv

Model-View-Websockets  
Garann Means

javascript

SPA - same page application

issues:  
scaffolding  
how/when to redraw  
where client interactions fit  
those damn http requests

twitter flight  
airbnb - node.js  
meteor  
mvc vs. eda

model = object  
view = presentation  
controller = ?

eda - event-driven architecture

Controller

spine.js in Toolmvc

Presenter  
backbone.js in todomvc

Viewmodel  
knockback.js in todomvc

CRUD  
REST

WebSockets  
server push dataq  
bi-directional  
no request, no responce

Rapid Templating: "Designing in the Browser" with Sass, Compass, and Serve  
Nathan Smith  
@nathansmith

j.mp/get-serve  
https://speakerdeck.com/nathansmith/rapid-templating-with-serve

get-serve.com

nathansmith.github.com

unsemantic.com

## Sunday

Advanced Javascript Training  
Pamela Fox

http://tinyurl.com/html5tx  
http://www.teaching-materials.org/workshops/html5tx.html

developers.whatwg.org

CLIENT SIDE STORAGE  
1)localStorage/sessionStorage  
Use a library like store.js or lscache https://github.com/pamelafox/lscache  
Careful, there are ways not to use localstorage

2)IndexedDB  
Again use a library like lawnchair,  
Not in all browsers, need fallbacks

3\) File APIs  
There are many file APIs

jshint.com

MULTIMEDIA IN HTML5  
online-convert.com - online video converter  
handbrake - download video converter

Subtitle tag Use a tool

JavaScript APIs  
There are javascript tools and hosted services.

GRAPHICS IN HTML5  
Try to make it without use of plugins.

SVG  
embed, inline, scripted, CSS background  
There are tools and libraries.

\<canvas\> tag\</canvas\>  
\<canvas\> HTML and Javascript.\</canvas\>  
\<canvas\> Animation is redrawing the canvas.\</canvas\>

Javascript drawImage.

Canvas has lots of libraries & tools.

WebGL  
Most people use ThreeJS.  
There are libraries and tools.

CSS 3d Transforms

BONUS:

I managed to make videos of me at my hotel. I posed them to youtube: [Irony in a hotel](http://www.youtube.com/watch?v=SD8IQfrpI78) & [Irony in a hotel part 2](http://www.youtube.com/watch?v=g7xW7aOPWMk).
