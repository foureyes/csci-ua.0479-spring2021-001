---
layout: slides
title: Tools Slides
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block" markdown="block">
##   We're Going to Be Using...
<div class="img-container" markdown="block">![Python Logo](../../resources/img/python-logo-master-v3-TM.png)
</div>
</section>

<section markdown="block">
##  About [Python](http://python.org/)
<aside>We're using Python because it:</aside>
* is a __friendly__ and __readable__ __high-level__ programming language
* is an __interpreted__ programming language (though there's __compilation__ behind the scenes)
	* what's the difference between the two? &rarr;
	* why might it matter? &rarr;
* supports multiple __programming paradigms__
* well-known as a mainstream programming language
* comes with _batteries included_

<details open markdown="block">
* QUESTION - what's the difference between compiled and interpreted again?
* INFO - technically it's compiled to bytecode, much like Java or c#, but there's no explicit compilation step 
* QUESTION - what paradigm are we using again?
* INFO - imperative / procedural, object oriented functional 
* INFO - comes with a lot of functionality "out-of-the-box"
</details>
</section>

<section markdown="block">
##  Where You've Seen It Before

* web frameworks like:
	* [Pyramid](http://www.pylonsproject.org/) / Pylons (Dropbox, reddit, FreshBooks)
	* [Django](https://www.djangoproject.com/) (Instagram, Pinterest, Disqus)
	* [Tornado](http://www.tornadoweb.org/) (quora, FriendFeed)
	* [Turbogears](http://turbogears.org/) (SourceForge) 
* EVE online
* original Bittorent client
* embedded scripting in Maya and Blender

<details open markdown="block">
QUESTION - does anyone use any of these sites?
</details>
</section>

<section markdown="block">
##   Some Python History
*  yes, it was named after Monty Python
*  based on ABC
*  invented in 1991 by this bearded Dutch guy (Guido van Rossum):

<div class="img-container" markdown="block">
![Guido Van Rossum, BDFL](../../resources/img/guido.jpg)
</div>

<details open markdown="block">
* ABC - teaching / prototyping language meant to replace BASIC, Pascal, etc
* Also known as Python's "Benevolent Dictator for Life"
</details>
</section>

<section markdown="block">
##   Where It's Going
<aside>And how it's getting there</aside>

* two active branches of Python: 2.x and 3.x
* Python Enhancement Proposals (PEPs).
* Python Software Foundation (PSF)

<details open markdown="block">
* ABC - teaching / prototyping language meant to replace BASIC, Pascal, etc
* 3.x meant to remove duplicate features and perceived flaws with prior implementation
* 3.x is not backward compatible, but some features have been backported
* PEPs provide structure for evolution and dev of Python; add language features as well as conventions
* PyPy - Python in Python!, Jython - for the JVM, etc.
* PSF - non-profit organization that provides organizational structure, governance and community building
</details>
</section>


<section markdown="block">
##   So, Which Version of Python, Exactly?
<aside>We're using Python 3!</aside>
All of the in-class examples, exercises and homework solutions will target __3.x__.  We're using Python 3 because it:

* is an excellent language for learning programming (readable, consistent, etc.)
* smooths over many of the perceived flaws and inconsistencies in Python 2
* is the future of Python 

Note, however, that Python 3 is not yet widely deployed in production systems.
</section>


<section markdown="block">
##   But, How Will We Write Python Programs?
<aside>You can't use Microsoft Word!</aside>
</section>

<section markdown="block">
##   Python Programs Are Just Text
A __text file__ is simply a file that contains human readable text.

* some text files have .txt as its extension
* you might have opened a text file in Notepad or TextEdit 
* Python programs are text files that (usually) end in __.py__ (for example, hello.py)

<div class="img-container" markdown="block">
![Python file icon](../../resources/img/text-x-python-icon.png)
</div>
</section>

<section markdown="block">
##   Why can't We Use a Word Processor Like MicroSoft Word or Pages?
<aside>These programs don't work with text files</aside>
* a .doc or .rtf file isn't actually just text 
* it has a bunch of other stuff in it that Pages or Word uses to render or display your file
* consequently, you can't use a word processor to create plain text files

</section>

<section markdown="block">
##   You'll Need a Text Editor or an IDE
* a __text editor__ is specifically used for editing text files
	* Some text editors, such as Notepad or TextEdit are very simple
	* Others contain features that aid in programming
* an __IDE__ is an application that is meant for reading and writing programs
	* It stands for Integrated Development Environment
	* Aside from editing text, it has many features that help programmers

<details open markdown="block">

an IDE is pretty much a text editor __plus__ some other stuff

</details>
</section>

<section markdown="block">
##   What's Makes a Good IDE?
* a full featured __text editor__ with:
	* __syntax highlighting__ - to make your program more readable
	* __syntax checking__ - to make sure your program's syntax is correct
	* inline documentation / help
	* code auto-completion
	* text editing tools - such as the ability to insert predefined chunks of code
* an integrated __interactive shell__ - to easily experiment with your programming language
* an integrated __debugger__ - to step through your program
</section>

<section markdown="block">
##   We'll be Using IDLE
<aside markdown="block">
Sticking with the Monty Python theme, perhaps a reference to [Eric Idle](http://en.wikipedia.org/wiki/Eric_Idle)
</aside>
* IDLE is an IDE (written in Python!)
* it's simple enough to not get in the way, but it has some very helpful features
* it's usually bundled with Python, so it should be present when you install Python
* as an IDE, it has two main functions:
	* __text editor__ &rarr;
	* __interactive Python shell__ &rarr;

<details open markdown="block">
* DEMO text editor
* DEMO - interactive shell
* Show:
	* syntax highlighting
	* syntax checking
	* auto-complete and integrated help
</details>
</section>

<section markdown="block">
##   Text Editor vs Interactive Python Shell
<aside markdown="block">
They look like they do the same thing, and that can be confusing!
</aside>

Again, IDLE comes with both:  

* a text editor
* an interactive Python shell

Both allow you to write code!  __So, what's the difference? &rarr;__

</section>

<section markdown="block">
##   Text Editor

<aside>Generally, you'll be using a text editor to write your programs.</aside>

The usual workflow is: &rarr;

* start writing a program or load an existing one
* make changes to your program
* save your changes
* run your saved program

It's similar to working on a regular document.

</section>

<section markdown="block">
##   Interactive Python Shell

<aside>There's also an interactive shell for quick experimentation:</aside>

* code is entered line-by-line
* code is executed as __each line is entered!__
* you get immediate feedback
* generally, you won't be able to save and re-run all of the code that you've entered
* ...__and__ any output from programs that you've edited and run through the text editor will be placed here
</section>

<section markdown="block">
##   [Now That We Know What Tools We're Using, How Do We Install Everything?](installing-tools.html)
</section>
