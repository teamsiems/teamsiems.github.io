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

<http://2009.highedweb.org/EventDetail.aspx?guid=4c46d953-9dbb-495e-b8b0-02fd694e7aa4>

<http://heweb09.jdwcornell.com/links.html>

## [Part 0: Bookkeeping](http://www.json.org/example.html)

- [JSONView 0.2](https://addons.mozilla.org/en-US/firefox/addons/versions/10869)

## Part 1: Tech Review

### JSON

- <http://www.json.org/example.html>

### XML

- <http://www.w3.org/XML/>

### XHTML

- <http://www.w3.org/TR/xhtml1/>

### CSS

- <http://www.w3.org/TR/CSS/>

### HTTP

- <http://www.w3.org/Protocols/rfc2616/rfc2616.html>

### DOM

- <http://www.w3.org/DOM/#what>

### JavaScript

- Read [JavaScipt The Good Parts](http://oreilly.com/catalog/9780596517748) O'Reily Books
- <http://www.crockford.com/javascript/>
- [Secrets of the JavaScript Ninja](http://jsninja.com/)

## Part 2: jQuery

*\$* is a function as in *\$(document)* that returns jQuery object.

*ready* is the method

### Getting Started

- <http://docs.jquery.com/Tutorials:Getting_Started_with_jQuery#Setup>
- <http://code.google.com/apis/ajaxlibs/documentation/>
- [Learning jQuery 1.3](http://www.packtpub.com/learning-jquery-1.3/book/mid/1802090m1d2r)

```

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <title>#heweb09 Twitter Session Companion</title>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
    <script type="text/javascript">
      $(document).ready(function() {
      alert('DOM ready!');
      });
    </script>
  </head>
  <body>
  </body>
</html>
```

### Selectors

- <http://docs.jquery.com/Selectors>
- [http://www.cornell.edu](http://www.cornell.edu/)

### Traversal

- <http://docs.jquery.com/Traversing>

### Manipulation

- <http://docs.jquery.com/Manipulation>

### CSS

- <http://docs.jquery.com/CSS>

### Events

- <http://docs.jquery.com/Events>

### Effects and UI

- <http://docs.jquery.com/Effects>
- <http://docs.jquery.com/UI>
- <http://docs.jquery.com/UI/Tabs#Back_button_and_bookmarking>

### Ajax

- <http://docs.jquery.com/Ajax>
- <http://malsup.com/jquery/form/>

### Browser State Preservation

*Use browser state preservation when someone bookmarks a page with AJAX code.*

- <http://plugins.jquery.com/project/jquery_history>
- <http://www.balupton.com/projects/ajaxy/demos/history/>

## Part 3: The Project

### Wireframe / Mockup

- <http://www.balsamiq.com/>

### Break it Down

- <http://etherpad.com/jdwcornell-heweb09-project>

### Build The Pieces

- <http://etherpad.com/jdwcornell-heweb09-project-js1>
- <http://etherpad.com/jdwcornell-heweb09-project-css1>

### Putting them Together

- [http://heweb09.jdwcornell.com](http://heweb09.jdwcornell.com/)

## Appendix

### \#heweb09 twitter session helper API

    http://heweb09.jdwcornell.com/oauth/twitter/login
    http://heweb09.jdwcornell.com/oauth/twitter/logout
    http://heweb09.jdwcornell.com/api/heweb09/screenname
    http://heweb09.jdwcornell.com/api/twitter/search.json?q=%23heweb09

    And any other read-only Twitter API  http://apiwiki.twitter.com/

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
