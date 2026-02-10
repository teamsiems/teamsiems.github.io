Title: Un-Minimizing Attributes Written With PHP In TinyMCE
Date: 2011-08-02 09:16
Author: chris
Category: Technology
Tags: Cascade, code, php, tinymce
Slug: un-minimizing-attributes-written-with-php-in-tinymce
Status: published

I think this is a "feature" of HH implementation of TinyMCE, but I noticed that the editor would "correct" my attributes when I wrote them properly in an PHP echo statement.

```

echo "$abc\n";
```

would save as

```

echo "$abc\n";
```

which of course breaks PHP. No matter how I tried to trick it into using escaped quotes it always changed back to unescaped.

My solution was to use single quotes and concatenate the variables into the string:

```

echo ''.$abc.''."\n";
```

For your reference, here are the minimized attributes that will need this treatment:

|          |                     |
|:---------|:--------------------|
| HTML     | XHTML               |
| compact  | compact="compact"   |
| checked  | checked="checked"   |
| declare  | declare="declare"   |
| readonly | readonly="readonly" |
| disabled | disabled="disabled" |
| selected | selected="selected" |
| defer    | defer="defer"       |
| ismap    | ismap="ismap"       |
| nohref   | nohref="nohref"     |
| noshade  | noshade="noshade"   |
| nowrap   | nowrap="nowrap"     |
| multiple | multiple="multiple" |
| noresize | noresize="noresize" |

There should be a better way to do this. A lot of code is written the proper way in PHP and switching it is untenable.
