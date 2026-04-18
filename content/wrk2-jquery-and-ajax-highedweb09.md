Title: Client-side Interactivity Through Javascript - jQuery and AJAX
Date: 2009-10-04 22:34
Author: chris
Category: Education
Tags: AJAX, heweb09, jQuery, wrk2
Slug: wrk2-jquery-and-ajax-highedweb09
Status: published

Jason Woodward
Director of Administrative Computing, Cornell University
[@jdwcornell](http://twitter.com/jdwcornell)
October 4, 2009

## [Part 0: Bookkeeping](http://www.json.org/example.html)
- [JSONView 0.2](https://addons.mozilla.org/en-US/firefox/addons/versions/10869)
## Part 1: Tech Review
### JSON
-
### XML
-
### XHTML
-
### CSS
-
### HTTP
-
### DOM
-
### JavaScript
- Read [JavaScipt The Good Parts](http://oreilly.com/catalog/9780596517748) O'Reily Books
-
- [Secrets of the JavaScript Ninja](http://jsninja.com/)
## Part 2: jQuery
\*\$\* is a function as in \*\$(document)\* that returns jQuery object.
\*ready\* is the method
### Getting Started
-
-
- [Learning jQuery 1.3](http://www.packtpub.com/learning-jquery-1.3/book/mid/1802090m1d2r)
```

#heweb09 Twitter Session Companion

$(document).ready(function() {
alert('DOM ready!');
});

```
### Selectors
-
- [http://www.cornell.edu](http://www.cornell.edu/)
### Traversal
-
### Manipulation
-
### CSS
-
### Events
-
### Effects and UI
-
-
-
### Ajax
-
-
### Browser State Preservation
\*Use browser state preservation when someone bookmarks a page with AJAX code.\*
-
-
## Part 3: The Project
### Wireframe / Mockup
-
### Break it Down
-
### Build The Pieces
-
-
### Putting them Together
- [http://heweb09.jdwcornell.com](http://heweb09.jdwcornell.com/)
## Appendix
### \#heweb09 twitter session helper API
http://heweb09.jdwcornell.com/oauth/twitter/login
http://heweb09.jdwcornell.com/oauth/twitter/logout
http://heweb09.jdwcornell.com/api/heweb09/screenname
http://heweb09.jdwcornell.com/api/twitter/search.json?q=%23heweb09
And any other read-only Twitter API http://apiwiki.twitter.com/
http://heweb09.jdwcornell.com/api/heweb09/populate/
http://heweb09.jdwcornell.com/api/heweb09/rightnow/
http://heweb09.jdwcornell.com/api/heweb09/attendees/TPR
http://heweb09.jdwcornell.com/api/heweb09/attendees/TPR1
http://heweb09.jdwcornell.com/api/heweb09/schedule/
http://heweb09.jdwcornell.com/api/heweb09/schedule/TPR
http://heweb09.jdwcornell.com/api/heweb09/schedule/TPR1
http://heweb09.jdwcornell.com/api/heweb09/attending/jdwcornell
http://heweb09.jdwcornell.com/api/heweb09/attend session=TPR1 (POST)
http://heweb09.jdwcornell.com/etherpad/css/jdwcornell-heweb09-css1
http://heweb09.jdwcornell.com/etherpad/js/jdwcornell-heweb09-js
