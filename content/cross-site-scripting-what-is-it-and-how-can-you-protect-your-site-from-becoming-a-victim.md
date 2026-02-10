Title: Cross-site Scripting: What Is It, and How Can You Protect Your Site from Becoming a Victim?
Date: 2009-10-08 08:22
Author: chris
Category: Education
Tags: heweb09, tpr5
Slug: cross-site-scripting-what-is-it-and-how-can-you-protect-your-site-from-becoming-a-victim
Status: published

Paul Gilzow  
Programmer/Analyst-Expert, University of Missouri

twitter: [gilzow](http://twitter.com/gilzow)

October 7

(This was Winner of Best of Track TPR)

Presentation <http://2009.highedweb.org/presentations/TPR5.zip>

or local copy [Cross-site Scripting: What Is It, and How Can You Protect Your Site from Becoming a Victim?](http://teamsiems.com/wp-content/uploads/2009/10/TPR5.zip)

Same Origin policy: 1 page in 1 tab can't interact with other page in another tab.

Injection attack: accept exploits the trust for a site

Education sites are the worst for xss.

URL Shorteners are bad: need to be locked down in edu

Three main types:

1.  non-presistent/reflective - most common, relies on social engineering (GET data)
2.  persistent/stored - web forums, social media sites (POST data)
3.  local - less likely but dangerous (html files on your desktop)

Try

" ' \< abx \>

The People directory "search" is not google and thus another company (in house) makes the search - more vulnerable.

How to protect:

Be paranoid. Trust no one. Layers, layers, layers.

Input filtering

Input validation

Output encoding

Intrusion detection system

PHPIDS

Tidy the output

HTML Purifier

AntiSamy

[www.xssed.com](http://www.xssed.com/)

No Script plugin for Firefox.

Look at phped for php editing.
