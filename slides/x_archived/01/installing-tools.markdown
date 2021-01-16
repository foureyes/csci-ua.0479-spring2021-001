---
layout: slides
title: Installing Tools Slides
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  So You've Decided to Install Python 
<aside>Yes!  You've made a good choice.</aside>
</section>

<section markdown="block">
##  You Probably Already Have a Version Installed
<aside>It's probably the wrong one</aside>
If you're on OSX or Ubuntu...

* Python is already installed on OSX or Ubuntu
* But it's probably 2.x

__What version were we using? &rarr;__

<div class="fragment" markdown="block">
* We're using 3.x for this class
* So... you'll probably have to install a new version side-by-side with the existing default Python on OSX and Ubuntu
</div>
<details>
QUESTION - What version are we using in class?
</details>
</section>

<section markdown="block">
##  (BTW, If You Have Your Laptop, Feel Free to Follow Along!)
</section>

<section markdown="block">
##  How To Determine What Version You're On
<aside markdown="block">
This requires using the _commandline_
</aside>
1. Open up:
	* __cmd.exe__ on __Windows__ (start &rarr; run &rarr; type "cmd.exe" and run)
	* __terminal__ on __OSX__ (&#8984;-space to search spotlight &rarr; type "terminal")
	* __terminal__ on __Ubuntu__ (you probably know how to do this on if you're on Linux!)
2. Type in the following command (this should output the version of Python that you have):

{% highlight bash %}
python --version
{% endhighlight %}

<details>
DEMO - starting terminal
DEMO - show Python version
</details>
</section>

<section markdown="block">
##  Installation
<aside>If you don't have Python 3, you can install it...</aside>
* on OSX and Windows:
	* go to the Download section on python.org: [http://python.org/download/](http://python.org/download/)
	* scroll down to the list of files for __Python 3.x__  (the version is in the file name, just get the latest)
	* __make sure you're looking at the 3.x files, not 2.x__
	* save the installer and run it
* on Ubuntu:
	* sudo apt-get install python3
	* sudo apt-get install idle3
</section>

<section markdown="block">
##  Installation Continued
* you can test your installation by opening terminal or cmd.exe (see the [previous slide](installing-tools.html#4.0) on [checking Python version](installing-tools.html#4.0))
* except, this time, you should have python 3 available, so __use "python3" instead of the regular python interpreter__: python3 --version
* you can also try running IDLE
	* OSX - &#8984;-space &rarr; start typing idle &rarr; choose __IDLE - Python 3.x__
	* Windows &rarr; Start &rarr; All Programs &rarr; __Python 3.x &rarr; IDLE__
</section>

<section markdown="block">
##  [Let's See What IDLE Can Do](reading-writing-programs.html)
</section>
