---
layout: slides
title: "Modules, Installing External Modules"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## What are Modules?

__Modules__ are just files with a bunch of Python code in them:

* they include __function definitions__
* __variable definitions__
* basically any bindings of names to objects...

</section>

<section markdown="block">
## Where are Theeeese Modules?

Great... so if modules are just Python files, that implies that the modules we've used so far, like <code>random</code>, <code>randint</code>, and <code>turtle</code> are all somewhere on our file system.

__Why yes, that's true.__ &rarr;

* PyCharm specific... command B or right-click on module name in editor &rar; goto declaration
* on OSX, you can use <code>mdfind -name random.py</code> to locate the <code>random</code> module
* or Linux/OSX, use <code>find / -iname random.py</code>

You'll notice that every version of Python you have on your system has a <code>random.py</code>
</section>

<section markdown="block">
## Creating our Own?

__Let's make our own module. It's a simple as creating a <code>.py</code> file__

In __my_module.py__:

<pre><code data-trim contenteditable>
def say_hello():
    print("howdy?")

</code></pre>

In __test_module.py__, you can call the funciton you created by starting with the module name...

<pre><code data-trim contenteditable>
import my_module

# call say_hello function that's in 
# my_module.py
my_module.say_hello()
</code></pre>

</section>

<section markdown="block">
## How'd import Work?

Note that the <code>import</code> statement:

* __takes the contents of the module and dumps it directly in the place where the import occurs__
* so all of the code (in the imported module) is executed! 
* (any names created in the function will be available, like functions and variable definitions)
* (but also, all code, including prints will get executed) __wait what?__ &rarr;

</section>

<section markdown="block">
## Printing in a Module

__What if your module has print statements in it?__ &rarr;


<pre><code data-trim contenteditable>
# my_module.py
def say_hello():
    print("howdy?")
print("in my module")
</code></pre>

__What would happen if we ran the code below? Would there be an error? No output? _Some_ output?__ &rarr;

<pre><code data-trim contenteditable>
# test_module.py
import my_module
</code></pre>

<pre><code data-trim contenteditable>
in my module
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## Name == Main

If you want your print statement to be present in your module when __it's run by itself__ (for testing purposes, for example), but you don't want it to print anything when it's __imported as a module__, you can use the following pattern:


<pre><code data-trim contenteditable>
# my_module.py
def say_hello():
    print("howdy?")

if __name__ == '__main__':
    print("in my module")
</code></pre>
</section>

<section markdown="block">
## Name == Main Continued

__Wait... what's all of that nonsense about?__ &rarr;

* there's a built in variable called <code>__name__</code>
* if a file is imported as a module, <code>__name__</code> is equal to that module's file name (minus the extension, .py)
* otherwise, if it's the file that's being run, it's <code>"__main__"</code>

<pre><code data-trim contenteditable>
# my_module.py
print("name is: ", __name__)
</code></pre>

<pre><code data-trim contenteditable>
# test_module.py
import my_module
</code></pre>

* when my_module.py is run on its own, the output is <code>name is: __main__</code>
* when test_module.py is run (all it does is import my_module), the output is <code>name is: my_module</code>
</section>

<section markdown="block">
## Installing MOAR Modules

__You'll likely be using PyCharm to install packages that don't come with Python.__ &rarr;
 
However, if you're curious about how things work behind the scenes, or if you enjoy using the commandline, you'll use:

* __package management tools__ like:
    * __pip__ 
    * (or easy_install)
* __environment management tools__ like
    * virtualenv, mkvirtualenv, and workon
    * ...that create arbitrary groupings of installed packages, and switch between them when running python

If you're into the manual version of doing this stuff, the keywords to search for are <code>python3 pip virtualenv</code>... or you can drop by office hours, and we could check it out together.
</section>


<section markdown="block">
## Installing Packages/Modules with PyCharm

__If you know you'll be using external libraries, you should start off by configuring your project to use a virtualenv.__

* a __virtualenv__ is an isolated Python environment 
    * a specific version of the Python interpreter
    * along with installed libraries
* all modules that you install will go into the virtualenv for your particular project
* __for our purposes, each project should have its own virutalenv__

</section>
<section markdown="block">
## Starting a Project With a virtualenv

1. create a new project
2. click on the gear icon next to the field marked interpreter
3. choose "Create VirtualEnv"
4. fill in a name for your virtualenv 
5. ensure that the base interpreter is Python 3.x ... and hit ok
5. this will automatically set the interpreter field with your newly named virtualenv

</section>

<section markdown="block">
## Installing a Module with PyCharm

1. Go to PyCharm &rarr; Preferences
2. In the left panel, expand Project: projectname, and choose Project Interpreter
3. Click on the + icon...
4. Search for the module to install

</section>

<section markdown="block">
## matplotlib

Use the previous directions to install a module called matplotlib.

* __matplotlib__ is a plotting library for python
* has an object that mimics matlab (if you're familiar with that!)

</section>

<section markdown="block">
## matplotlib Minimal Setup 

* import (remember as!) <code>import matplotlib.pyplot as plt</code> ... common convention to call it plt
* plot a point <code>plt.plot(0.25, 0.75, marker='o', color='blue')</code>
    * can also pass Lists (with same num of elements)
* show figure/graph/chart <code>plt.show()</code> 
</section>


<section markdown="block">
## matplotlib Sample

<pre><code data-trim contenteditable>
import matplotlib.pyplot as plt

plt.plot(0.25, 0.75, marker='o', color='blue')
plt.plot(0.75, 0.75, marker='o', color='blue')

x = 0.25
for i in range(6):
    plt.plot(x, 0.3, marker='o', color='red')
    x += 0.1
plt.show()
</code></pre>

</section>

