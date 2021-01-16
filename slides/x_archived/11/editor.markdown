---
layout: slides
title: "Required Software"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## IDLE No More

__While IDLE has served us pretty well (_most_ of us) for most of the semester, it does have a few shortcomings__ &rarr;

* {:.fragment} unfortunately, it's a _little_ buggy (on some systems, it has a tendency to crash, lose mouse focus, etc.)
* {:.fragment} it has some decent features, but it's still fairly bare bones... for example:
    * limited ui customizations such displaying line numbers
    * a tabbed interface for managing multiple files, etc.)
* {:.fragment} its debugger isn't easy to use

__Sooo... we're going to try a different editor!__ &rarr;
{:.fragment}


</section>

<section markdown="block">
## Another Text Editor / IDE

Let's try [PyCharm](https://www.jetbrains.com/pycharm/) instead of IDLE. Go ahead an install the __Community Edition__.

1. Download the free __Community Edition__ (PyCharm CE)
2. Double click to install (you'll have to drag to your Applications folder)

__WAIT! What's so good about PyCharm?__ &rarr;
{:.fragment}

* {:.fragment} the main reason why I've chosen it is because it offers a graphical user interface for dealing with some useful Python tools
    * downloading modules
    * creating isolated environments with access to a specific set of modules
* {:.fragment} more polished user interface, more stable
* {:.fragment} feature rich - great debugger, sophisticated find and replace, etc.

</section>

<section markdown="block">
## Configuring PyCharm

__There's a bit of configuration that you have to do when creating a new project:__ &rarr;

1. Configure PyCharm to use Python 3 by [checking out these directions](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
2. Start a new project or from an existing project go to PyCharm Community Edition &rarr; Preferences &rarr;
3. You should be prompted to choose a "Project Interpreter"
4. Click the gears
5. Choose _Create Virtualenv_
6. Name it "intro_to_comp_prog"
7. Choose 3.x as your base interpreter
8. Check "Make Available to All Projects"
9. Finally, select your newly created virtualenv / interpreter combo!

</section>

<section markdown="block">
## Wait Wait, What Was That About?

1. __pip__ and __easy install__ - commandline tools for installing Python modules that don't _come bundled with_ Python
2. __virtualenv__ - an isolated _environment_ to install Python modules
    * ...so you can have sets of modules
    * ...that are independent from one another

These are all basically commandline tools that help you install and use Python modules.

(btw, these modules come from the [Python Package Index](https://pypi.python.org/pypi) - "a repository of software for the Python programming language")
   
</section>



<section markdown="block">
## Using PyCharm

PyCharm organizes your code by projects. I'd recommend using:

* 1 project per homework
* (or 1 project per class)
* creating a new file in that project for every separate file you need

Use the following commands:

* __Create a project:__ File &rarr; new Python File
* __Create a file:__ File &rarr; new &rarr; Python File
* __Run last file:__ Run &rarr; filename (control R also works for this)
* __Run specific file:__ Run &rarr; choose file name

</section>

<section markdown="block">
## Let's Try Installing a Package

__We'll try installing a package that gives us an easy way of downloading information from the web__ &rarr;

The library is called requests - [check out the documentation!](http://docs.python-requests.org/en/master/)

1. PyCharm &rarr; Preferences
2. Go to your project
3. Click on the + button
4. Type in `requests`
5. Install!

__Then... try typing in this code:__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
import requests
r = requests.get('http//google.com')
print(r.text)
</code></pre>
{:.fragment}

</section>

