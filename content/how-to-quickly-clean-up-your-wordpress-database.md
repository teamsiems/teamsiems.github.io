Title: How To Quickly Clean Up Your WordPress Database
Date: 2011-04-02 00:18
Author: chris
Category: Technology
Tags: database, DELETE, OPTIMIZE, revisions, wordpress
Slug: how-to-quickly-clean-up-your-wordpress-database
Status: published

I'm putting this post on my site because I'm tired of searching for the commands.

There are plugins that will clean up your WordPress wp_posts table, but if you have access to the database you can do this yourself.

## Backup the Database

You should always make a backup copy of your database just in case something goes wrong. This is a "duh" - but it happens - and things can go wrong. You'll be deleting records from a table so before you do, make a backup.

## Run the DELETE Query

Run the following command on your database. If you have a shared host with a cPanel you probably have phpmyadmin which is your user interface to your MySQL database. WordPress usually installs in MySQL as wrdp. You want click on the right database for your WordPress install. Once you are in the right database you can run this query:

`DELETE FROM wp_posts WHERE post_type = "revision";`

This will delete all the revisions from WordPress. Just out of curiousity you might take a note of how much space the wp_posts table was taking up before and after running this query. That will tell you how much room you recovered.

## Optionally, You Can OPTIMIZE

This step is optional. If you are sweating bullets right now after deleting 20,000 revision posts, you can skip this step.

Optimization "releases" the data you deleted from memory thus freeing memory. Its like delete puts data in the trashcan and optimize empties the trash. To optimize the wp_posts table run the following query:

`OPTIMIZE TABLE wp_posts;`

Check to see the size of this table. In the YIW database, the “wp_posts” is only 3,4 Mb in size, as you can see in the photo below. It’s a lot of space saved, don’t you think?

## My Numbers

I've run this query several times over the years. It's like cleaning up your computer's hard drive - the more you use it the more you should clean it up. There were my numbers.

Start 407 rows \| 792.1 KB

Deleted 61 rows \| 96.1 KB

Finish 346 rows \| 695.4 KB

Hope this works for you. I know it works for me and I use it about once a year or so.
