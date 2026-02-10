Title: My Notes from the 2012 MWF Conference
Date: 2012-09-07 08:56
Author: chris
Category: Personal
Tags: mwf
Slug: my-notes-from-the-2012-mwf-conference
Status: published

These are my raw notes from the webinar sessions of the 2012 MWF Conference that I attended.

Wednesday, September 5, 2012

KEYNOTE: Vice Provost of IT at UCLA  
- Cross campus “Informatics”  
- OPT: Online Polling Tool

Kitchen Sink  
- Look at [http://uxt.ucsd.edu](http://uxt.ucsd.edu/)

MWF Forms  
- “formsPolyfill” - adds functions to devices that don’t natively support the HTML5 features.  
- Look in js.php

Mobile Web Accessibility  
- User scenarios: blind, low-vision, color blind, deaf, dexterity, cognitive  
- Look at <http://snook.ca/>  
- Look at <http://web.webaim.org/>  
- Look up WCAG 2.0 + MWBP

MWF Community / MobilizeLabs / Ohmage+MWF  
- MWF 1.3 has BSD license  
- MWF 2.0 “WebBlocks” is responsive  
- UCLA is moving MWF into more HigherEd & beyond (corporate, community based)

Thursday, September 6, 2012  
MWF Roadmap  
- 9/29/2011 MWF 1.2 released: DTS  
- 4/15/2012 MWF 1.3 released: Lean CSS, Forms API, …  
-12/15/2012 MWF 2.0 “WebBlocks”: responsive. (Request GitHub access from <ebollens@ucla.edu>  
- November 2012/Spring 2013: Web Apps Sharing Environment  
- Ohmage-MWF growing features

Responsive Design  
- Has flexible grid, flexible media, media queries  
- Flexible grid: percent not pixels  
- Dynamic Image Compression: MWF via img.php; Adaptive Images via .htaccess  
(Mobile First)  
- define content linearly  
- use min-width, not max-width  
- add complexity and asymmetry as screen widen

Native App Awesomeness  
- Lookup HTTP Compression (mod_deflate) for faster load over mobile  
- Optimize images (ImageOptim MAC tool)  
- Eliminate redirects  
- preload large css images  
- remove unused JS code (customize modernizr, bootstrap, foundation, ...)  
- Defer JS  
- Look at <http://trott.github.com/>  
- A fast mobile .edu site loads in 1.75ms

Mobile Testing  
- Emulators  
- Android <http://developer.android.com/sdk/>

Mobile Governance Examples  
- 3 phases - Engaging the Stakeholders, Mobile Advocacy, and Defining the Governance Process

Responsive Future of MWF  
- 3997 different Android device resolutions (2012)  
- Look at <http://mediaqueri.es/>  
- Maps (Google API) is a good use of MWF over RWD  
- Downsides to RWD: images  
- Look up RESS = responsive + server  
What do we need  
- responsive design  
- support libraries: browser normalization, capability detection, html5 & css3 polyfills  
- rich interfaces  
A Toolkit  
- integrated set of packages  
- customizable for organizational needs  
- extended with ui elements and js interactivity  
- collaboration & federation build directly in  
Basics  
- build script for css js and images  
- support for SASS and Compass  
- jquery and twitter bootstrap  
- modernizr, selectivizr, respond.js  
- rich library of ui elements  
- javascript interactivity api  
Is this compass with libraries, sort of but more customized  
- Look up Adaptive Design Pattern  
- It has abstraction layer  
- Link between markup entities & framwork  
- Switch by changing config variable

Core Architecture in MWF Responsive Future  
- WebBlocks is framework agnostic  
What does it include  
- basic responsive framework  
- base ui elements  
- rich interactive responsive UI components  
- responsive images  
- responsive video  
- css/js minification  
Modular Architecture  
- enable what you need  
- swap out the underlying framework  
- support for integration third-party components

 
