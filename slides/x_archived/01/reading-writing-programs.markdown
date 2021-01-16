---
layout: slides
title: Reading and Writing Programs
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
##  Reading and Writing Python Files
</section>

<section markdown="block">
##  About IDLE

__What are the two main ways that we can use IDLE? &rarr;__

<div class="fragment" markdown="block">
1. Create or open existing Python files in a text-editor view (and view the output of your program through the interactive Python shell) 
2. Type and run commands line-by-line through the Python Shell
</div>

</section>

<section markdown="block">
##  Again, You Can...

* run your program all at once (using Run &rarr; Run Module)

<aside>or</aside>

* run commands one-step-at-a-time using the interactive Python shell

Lastly, if your program ever outputs anything, it should show up in the interactive Python Shell
</section>


<section markdown="block">
##  Starting IDLE
<aside>IDLE is our IDE; we'll use it to read and write programs</aside>

Just like what we did in the previous slides, to open IDLE:

* OSX - &#8984;-space &rarr; start typing idle &rarr; choose IDLE - Python 3.2
* Windows - Start &rarr; All Programs &rarr; Python 3.2 &rarr; IDLE

<details>
DEMO - opening IDLE
</details>
</section>

<section markdown="block">
##  Starting IDLE Continued
When you first open IDLE, you should see a window titled __"Python Shell"__

* to reiterate, the __Python Shell__ is for entering and running programs __line-by-line__
* sometimes the __shell__ can be referred to as the __Python interpreter__, __console__ or __interactive shell__
* you'll probably want to start out by creating a new file...

</section>

<section markdown="block">
##  Managing Files 
<aside>Creating New Files, Opening Recent Files, Running Files</aside>

All file management activities can be found in the File menu:

* Create a new file: File &rarr; New Window
* Opening an existing file: File &rarr; Open
* Running a file: Run &rarr; Run Module

Shortcuts for creating, opening and running a file are &#8984;-n, &#8984;-o, and the F5 key respectively.

<details>
DEMO - new window, open and run module
</details>
</section>

<section markdown="block">
##  (Again, Feel Free to Follow Along!)
</section>

<section markdown="block">
##  A First Program

__"Hello world!"__ is traditionally the first program you write when learning a new language.  It simply outputs "Hello world" (yeah, that's all).  __Follow these steps__:

* create a new file
* type in ...

<pre><code data-trim contenteditable>
print("Hello world!")
</code></pre>

* run your program
	* you may be prompted you to save your file
	* if you haven't saved it yet, you'll be prompted for a file name

<details>
</details>
</section>

<section markdown="block">
##  Modifying Your Program
<aside>Most of the time, we're editing existing programs rather than creating entirely new ones</aside>

Let's modify the program that we just wrote:

* if your file is closed, reopen it
* add a second line:

<pre><code data-trim contenteditable>
print("Hi again!")
</code></pre>

* run your program

<details>
</details>
</section>

<section markdown="block">
##  Making Mistakes
<aside>Programs don't always work the way we expect them to!</aside>

Let's purposely make a mistake, then fix it

* if your file is closed, reopen it
* add a third line, but leave off the last parentheses: 

<pre><code data-trim contenteditable>
print("Hola"
</code></pre>

* run your program
* you should see a pop-up and a red highlight where your syntax error occurred
* this occurs if your program is not syntactically correct
* fix the mistake (how?)

<details markdown="block">
* DEMO - make a syntactic mistake, show where the error is
* QUESTION - How do we fix this?
</details>
</section>

<section markdown="block">
##  Making More Mistakes
<aside>That was syntactic mistake; what about errors that occur when the program is actually running?</aside>

Let's make a run-time error:

* if your file is closed, reopen it
* add a fourth line: 

<pre><code data-trim contenteditable>
print("Howdy" + 2)
</code></pre>

* run your program
* you should see the error in the console
* let's read it and try to interpret it
* fix the error
* note that the current line number is on the lower-right-hand corner of the window (prefixed with "Ln: ")

<details>
DEMO - make a run-time error
QUESTION - what line number did the error happen on?
DEMO - find the line
</details>
</section>

<section markdown="block">
##  Errors

Notice that we looked at two different _types_ of errors:

* __syntax error__ - an error with the syntax/structure of the program; the program cannot run _at all_
* __runtime error__ - the program is syntactically correct, but some sort of error occurs while the program is running
</section>

<section markdown="block">
##  A Quick Note on Syntax Highlighting

* The different colors represent different syntactic elements
* Some examples include
	* __strings__ - green
	* __built-in functions__ - purple 
	* __keywords__ - orange
* __strings__ - a primitive type of data in Python; a sequence of characters
* __keywords__ - (reserved words) words that have special meaning in Python

<details>
DEMO - function and for loop for syntax highlighting
</details>
</section>

<section markdown="block">
##  The Output Window and Interactive Shell 
</section>

<section markdown="block">
##  The Interactive Shell
* the output window can also be used to run Python code interactively
* you can also go to Run &rarr; Python Shell to open an interactive session if it's closed
* you can enter commands and have them return immediate feedback
* the prompt,  "&gt;&gt;&gt;", means the interactive shell is waiting for input
* try re-typing our hello world in the interactive shell, one line at a time

<details>
DEMO - hello world in interactive shell
</details>
</section>

<section markdown="block">
##  Help!

Note that typing __help__ in the interactive shell _actually_ gives you help!  __Let's try it!__ &rarr;

<pre><code data-trim contenteditable>
>>> help
</code></pre>

You can use help on specific things... __for example__: &rarr;

<pre><code data-trim contenteditable>
>>> help(print)
</code></pre>

__Additionally, you can check out the Python docs by going to Help &rarr; Python Docs in the menu.__ &rarr;
</section>

<section markdown="block">
##  [Let's Provide Some Structure to Our Programming Process](programming-workflow.html)
</section>
