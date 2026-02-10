Title: CSS3...In 3D! Workshop
Date: 2010-10-13 16:30
Author: chris
Category: Education
Tags: heweb10, WRK7
Slug: highedweb-2010-post-conference-workshop
Status: published

## HighEdWeb 2010 Post-Conference Workshop: [CSS3...In 3D!](http://2010.highedweb.org/EventDetail.aspx?guid=41d5783a-1216-4c03-9b7e-946201d28968)

WRK7

The advent of CSS3 allows for greater control and creativity in Web design. Attendees in this workshop will learn about using colors through RGBa and opacity, border images, text and box shadows, animations, transformations, and much much more to enrich their Web designs. And, yes, free 3D glasses will be distributed to attendees!

[Christopher Schmitt](http://twitter.com/teleject)  
Web Design Specialist, Heatvision.com, Inc.

The founder of Heat Vision, a small new media publishing and design firm, Christopher is an award-winning Web design specialist who has been working with the Web since 1993. As a sought-after speaker and trainer, Christopher regularly demonstrates the use and benefits of practical standards-based designs. He is co-lead of the Adobe Task Force for the Web Standards Project (WaSP) in addition to being a contributing member of its Education Task Force. Author of numerous Web design and digital imaging books, including Adapting to Web Standards: CSS and Ajax for Big Sites and CSS Cookbook, Christopher has also written for New Architect Magazine, A List Apart, Digital Web, and Web Reference.

via [Session Details - HighEdWeb 2010: The National Conference for Higher Education Web Professionals](http://2010.highedweb.org/EventDetail.aspx?guid=41d5783a-1216-4c03-9b7e-946201d28968).

------

My Notes

\- Apple used Safari to add behaviors  
- Split into modules  
-- Tranformations  
-- Animations  
-- Media Queries  
...

http://www.css3.info/  
http://www.modernizr.com/

background-color: rgb(55,55,55);  
background-color: rgba(55,55,55,.5);

Firefox 3+, Opera 10+, Safari support rgba  
IE can use filter:progid:DXImageTransform.Microsoft.gradient(startColor....

Text overflow  
text-overflow: ellipsis  
-o-text-overflow: ellipsis

Text-selection  
::selection

Text Columns  
welcome.totheinter.net for jquery plugin

@Font-Face  
you can define them  
fontsquirrel.com  
fonthead.com  
typekit.com  
fontdeck.com  
book "fluid web typography"

Text Shadow  
text-shadow: x,y,depth

Borders  
-- box-shadow:x,y,depth, rgba  
-- border-image:url, t, r, b, l, stretch, stretch  
-- border-radius:px (or border-top-left....

Image Masks  
- webkit-mask-box-image  
- moz-...

Gradient  
background-image: -webkit-gradient(radial, center center,900,center bottom, o, from(#abc), to(#cba))  
westciv.com/tools/

Gradient Masks  
-webkit-mask-box-image:  
-webkit-gradient(linear, left bottom, left top, from(rgba(0,0,0,1)), to(rgba(1,2,3,1))  
Example zodurl.com

Transform Rotate  
transform:rotate(270deg);  
-webkit-transform:rotate(270);

Animated Links  
-webkit-transition-timing-function  
-...  
-...

Complex animated links  
farukat.es

Animating elements // not a:hover  
position:absolute

Resources  
-  
gradients.glrzard.com
