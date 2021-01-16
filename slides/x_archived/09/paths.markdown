---
layout: slides
title: OSX File System, Paths
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Where are My Files Again?

<aside>Navigating the file system in three parts</aside>

Warning: this part is fairly OSX-centric... __if you're on windows, let me know, and we can do a separate session__.

* Definitions (of course)
* OSX's directory structure
* A little bit about pathnames

</section>

<section markdown="block">
##  First, Some Definitions
</section>


<section markdown="block">
##  Directories

What's a __directory__ (to simplify things, we can use "directory" and "folder" interchangeably)? &rarr;

<div class="fragment" markdown="block">
* a __directory__ is an organizing structure in your file system; it references other files (and directories)
* we can think of it as _a thing that contains files_ 
* ...or because directories can be nested, you can think of your directories and files as a tree! ([what a terrible looking tree](http://itp.nyu.edu/groups/flyby/wp-content/uploads/sites/6/2014/09/unix-file-system-example-1.png)!?)
</div>
</section>

<section markdown="block">
##  Root

__root__ (or just /) is:

* the top most directory on a disk 
* think of it as the _root_ of your tree!
* it's the directory that contains all of the other files and directories
</section>

<section markdown="block">
##  Pathnames

What's a __pathname__? &rarr;

<div class="fragment" markdown="block">
* a __pathname__ is the general form of the name of a file or directory; it specifies a unique location in a file system
* for example, in finder, to locate a file or folder, you follow a particular path - __let's check this out__ &rarr;. 
* __what's the path to the Desktop starting from the _top most_ folder, the hard drive (probably Macintosh HD)?__ &rarr;
</div>
</section>


<section markdown="block">
##  Let's Look at OSX's Directory Structure
</section>

<section markdown="block">
##  Some Structure

Each operating system organizes their files and directories differently.  OSX's file structure looks like this (it's similar to other UNIX based file systems):

* __/__ - (also called __root__) the top most folder on a disk (the directory that _contains_ all of the other files and directories)
* __/Applications__ - where shared applications are kept
* __/Users__ - all user accounts and their accompanying files are stored here
* __/Volumes__ - all disks that are attached to your computer including USB drives, hard drives, etc.
* __/System__ - _system specific_ files, libraries, preferences that are critical to the operating system

</section>

<section markdown="block">
##  More About the User's Directory

It's worth noting the directories nested under Users.  They should seem familiar to you.

* __/Users/username__ - (also called __home__ when you're in your own username's directory) contains files specific to that particular user
* __/Users/username/Desktop__ - represents the user's Desktop
* __/Users/username/Downloads__ - the user's downloads folder
</section>


<section markdown="block">
##  And Now... To Pathnames!

<aside>We know a little bit about the file system structure; let's take a closer look at how we locate files</aside>

</section>

<section markdown="block">
##  What's a Pathname?

A __pathname__ is the general form of the name of a file or directory; __it specifies a unique location in a file system__.
</section>

<section markdown="block">
##  Path Separator

A __path separator__ is a character that's used to join together each directory in a pathname that contains nested directories (for example, Desktop was located under Users and username...  there was a character that separated each directory).  

__What character represents the path separator on OSX (we just saw this)?__ &rarr;

<div class="fragment" markdown="block">
* it's a __forward slash__, __/__
* (sometimes just called __slash__ when referencing directories) 
* for windows, the separator is backslash 
</div>
</section>

<section markdown="block">
##  Absolute vs Relative Paths

* __absolute paths__ are paths expressed as starting from root
	* example: /Users/username/Desktop
* __relative paths__ are paths expressed as relative from the current working directory
	* example (if you're starting from /Users/username): Desktop

</section>

<section markdown="block">
##  Some Special Paths

There are shortcuts to represent specific paths:

* __~ (tilde)__ is _your_ home directory
* __/ (forward slash)__ is root directory

The following paths are relative to the directory _that you're in_:

* __. (dot)__ is the current directory
* __.. (dot dot)__ is the parent directory
* __../.. (dot dot slash dot dot)__ is the parent of the parent directory

</section>

<section markdown="block">
##  Let's See Some Pathnames Through Finder

* Desktop
* Downloads
* root (probably Macintosh HD)
</section>
