---
layout: slides
title: Built-in Modules
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Built-In Functions

So... again, we learned a few built-in functions.  __What are some of the functions that we know? &rarr;__  These are all available by default:

<div class="fragment" markdown="block">
* print
* type
* int
* str
* float
* bool
* input
</div>
</section>

<section markdown="block">
##  Even More Built-In Functions!

We've only scratched the surface.  There are even more built-in functions!  There's a list in the official python documentation: [http://docs.python.org/py3k/library/functions.html](http://docs.python.org/py3k/library/functions.html)

For example:

* __abs__(x) - returns a number that is the absolute value of x&rarr;
* __len__(s) - returns the length of a sequence type (such as a string) as an int&rarr;
* __round__(x [,digits]) - round a number to a given precision in decimal digits (default 0 digits)&rarr;
* __dir__([object]) - returns a list of names in a module or in the current namespace&rarr;

__Let's try these out! &rarr;__
</section>

<section markdown="block">
##  More Functions, More Functions, More Functions

Python boasts that it comes with batteries included:

* it has a large and comprehensive __standard library__
* most likely, if you need it, Python has it built in!
* everything from audio file processing to parsing html documents
</section>

<section markdown="block">
##  Modules
<aside>For Batteries Included, There Doesn't Seem to That Many Built-In Functions</aside>

* that's because you can access this functionality through __modules__!
* these __modules__  _provide standardized solutions for many problems that occur in everyday programming_
* they also help in organizing code / the standard library (related functionality is grouped together in the same module)
</section>

<section markdown="block">
##  What's a Module?

A __module__ is _just_ a file that contains Python code!

* a file containing Python definitions and statements intended for use in other Python programs
* the contents of a module are made available to the other program by using the __import__ statement.
</section>

<section markdown="block">
##  No, Really, What's a Module?

So... what does that actually mean?

* there are functions (as well as other definitions) that are not automatically loaded when you run python
* these functions (and other definitions, such as variables and constants like pi, classes, etc) are grouped together in files called modules
* you can bring them in to your program by using the __import__ statement
* simply use the keyword __import__ followed by the module name (with no quotes and no extension)

<pre><code data-trim contenteditable>
import math
import random
import sys
</code></pre>
</section>


<section markdown="block">
##  So... What Can These Modules Do?

* math
	* __pi__ - a constant that contains the value of pi&rarr; 
	* __floor__(x) - returns the smallest integer less than or equal to x&rarr;
	* __ceil__(x) - returns the smallest integer greater than or equal to x&rarr;
	* __sqrt__(x) - returns the square root of x&rarr;
	* __cos__(x) - returns the cosine of x radians &rarr;
</section>

<section markdown="block">
##  So... What Can These Modules Do (Continued)?
* random
	* __random__() - return a random float that's between 0 and 1&rarr;
	* __randint__(a, b) - returns a random int that's a <= n <= b&rarr;
* sys
	* __exit__([arg]) - exits from python&rarr;
	* __version__ - a constant that contains the version of Python&rarr;
</section>

<section markdown="block">
##  We Know How to Call Functions, Right?

__So, what's the exact syntax for calling a function?  Let's start with built-in ones, like print or str.__ &rarr;

<div class="fragment" markdown="block">

* the function name
* open parentheses
* optional arguments
* close parentheses

<pre><code data-trim contenteditable>
print("foo")
str(5)
</code></pre>
</div>
</section>

<section markdown="block">
##  Calling a Function is Easy
<aside>How Do We Call a Function That's in a Module?</aside>

Call or use functions and other definitions in a module by: 

* making sure you __import__ the module first!
* no, really: __IMPORT FIRST__
* using the module name as the prefix 
* a dot (__.__)
* the function (or variable, class, etc) name

<pre><code data-trim contenteditable>
import math # import first!
#  remember - the syntax is: module_name.function_name()
math.pi
math.sqrt(25)
</code></pre>
</section>

<section markdown="block">
##  Let's Try That Again 
<aside>Step-By-Step</aside>

__How do I bring in the random module to call the randint function?  Write a short program that prints out a random number. &rarr;__

<div class="fragment" markdown="blcok">
<pre><code data-trim contenteditable>
import random 
num = random.randint(0, 10)
print(num)
</code></pre>
</div>
</section>

<section markdown="block">
##  The math Module In Use

__Write a quick program to print out the cosine of 2pi and the squareroot of 225. &rarr;__ 

<div class="fragment" markdown="blcok">
<pre><code data-trim contenteditable>
import math
a = math.cos(2 * math.pi)
print(a)
b = math.sqrt(225)
print(b)
</code></pre>
</div>
</section>


<section markdown="block">
##  The random Module In Use

__Write a quick program to print out two random numbers, one a floating point between 0 and 1, the other an int between 5 and 10. &rarr;__ 

<div class="fragment" markdown="blcok">
<pre><code data-trim contenteditable>
import random
a = random.random()
print(a)
b = random.randint(5,10)
print(b)
</code></pre>
</div>
</section>

<section markdown="block">
##  Lastly, Let's Check Out the Sys Module

<pre><code data-trim contenteditable>
import sys
print(sys.version)
#  note that the following line causes what looks like error text to appear...
sys.exit() 
print("Is this really the end????")
print("Even before this!")
</code></pre>

__BTW, what do you think gets printed?&rarr;__

<div class="fragment" markdown="block">

<pre><code data-trim contenteditable>
3.2.3 (v3.2.3:3d0686d90f55, Apr 10 2012, 11:25:50) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
</code></pre>

</div>
</section>

<section markdown="block">
##  To Use a Module, IMPORT IT FIRST! 

__What do you think happens if your forget to import the file?   &rarr;__

<div class="fragment" markdown="block"> 

<pre><code data-trim contenteditable>
>>> math.sqrt(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
</code></pre>
</div>
</section>

<section markdown="block">
##  To Call a Function in a Module, Use The Module's Name as a Prefix

__What if you don't use the module name as the prefix before calling your function? &rarr;__

<div class="fragment" markdown="block"> 
<pre><code data-trim contenteditable>
>>> import math
>>> sqrt(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> 
</code></pre>
</div>
</section>

<section markdown="block">
##  So... With All of That Out of the Way Let's Simulate Rolling a Six Sided Die Twice

__Use random to "roll" dice; print out the two die rolls__&rarr;

<div class="fragment" markdown="block"> 
<pre><code data-trim contenteditable>
d1 = random.randint(1,6)
print(d1)
d2 = random.randint(1,6)
print(d2)
</code></pre>
</div>
</section>

<section markdown="block">
##  Behind the Scenes
<aside>A Closer Look at Modules</aside>
What happens when we import?

* the name of the module actually corresponds to a python file
* Python looks in the current working folder (as well as several other locations) for a file named after the module your importing
* imagine placing the contents of that file directly into the file you're working on (at the point of the import statement)
</section>

<section markdown="block">
##  An Example Module

In fact, we can make our own modules!  We'll take a look at this later, but to illustrate how modules work, we can create two files in the same directory:

* foo.py (the module that we'll import)
* hello.py

<pre><code data-trim contenteditable>
#  foo.py
print("called from inside the foo module")
def greet():
	print("hi")

#  hello.py
import foo
print("hello")
foo.greet()
</code></pre>
</section>

<section markdown="block">
##  An Example Module Continued

__What do you think will be output when we run hello.py? &rarr;__

<div class="fragment" markdown="block">

<pre><code data-trim contenteditable>
inside my_awesome_module
hello
42
</code></pre>
</div>
</section>


<section markdown="block">
##  Um... So Where Are All of Those Other Modules?
<aside markdown="block">
They're Definitely _Not_ in the Current Directory
</aside>

Where do sys, math, random, and other modules come from?  If modules are just files, we should just be able to find them!

* the current directory
* _or_ a list of specified directories called the __PYTHON_PATH__
* these usually vary by system, but
* for example, on OSX (Mountain Lion) and Python 3.3, you may be able to find modules in:

<pre><code data-trim contenteditable>
#  for me
/usr/local/Cellar/python3/3.3.2/Frameworks/Python.framework/Versions/3.3/lib/python3.3/

#  for you...
/System/Library/Frameworks/Python.framework/Versions/ ...
</code></pre>
</section>

<section markdown="block">
##  Why Do Modules Exist?

That's great, but why bother with using and/or creating modules (aside, of course, from bringing in additional built-in functionality)?

* they encourage code reuse (DRY - don't repeat yourself)
* they provide "namespacing" to avoid name collisions
* they provide a way of organizing code
</section>

<section markdown="block">
##  Three Modules Out of ??? / HALP!

There are many more modules to explore.  Check out the [official documentation](http://docs.python.org/py3k/library/index.html) for a more comprehensive list.  You'll find modules like:

* tkinter - for graphical user interfaces
* turtle - a pen-plotter like drawing library
* wave - for reading/writing WAVE (audio files)
* http.server - a simple Python web server
* and so on...
</section>

<section markdown="block">
##  HALP!!!
To find help on these modules:

* the first place to look is obvs the [official documentation](http://docs.python.org/py3k/library/index.html) 
* you can also check out the python docs in IDLE (go to Help&rarr;Python Docs)
* you can fiddle around in the interactive shell
		* dir()
		* help()

<pre><code data-trim contenteditable>
>>> import math
>>> help(math)
>>> dir(math)
</code></pre>
</section>

<section markdown="block">
##  How About a Practical Application, PLZ?

__Rewrite our guess number game so that it uses a random number instead of a hardcoded one. It should display the correct answer after you guess.&rarr;__

<pre><code data-trim contenteditable>
#  Run 1:
Guess a number between 1 and 10!
> 5
Nope, I was thinking of 10.

#  Run 2:
Guess a number between 1 and 10!
> 8
You guessed right; I was thinking of 8.
</code></pre>

</section>

<section markdown="block">
##  Let's Review

* how do we import a module?
* what are the modules that we looked at?
* what are some functions in those modules?
* how do we call a function from a module?
</section>
