---
layout: slides
title: Errors and Debugging
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Ugh. My Program Doesn't Work
<aside>What do I do?</aside>
</section>


<section markdown="block">
##  Types of Errors 

Let's take a look at some things that may prevent your program from _working_.

Based on what we've seen in the previous classes, the online module, and (hopefully) homework #1, what are some mistakes / errors that you can make while programming? 

__Can we categorize these errors?__ &rarr;

<div class="fragment" markdown="block">
* syntax errors
* runtime errors
* logic errors
</div>
</section>

<section markdown="block">
##  Syntax Errors

A __syntax error__ is an error caused when your program does not follow the rules that define the allowable combinations of characters/symbols for a correctly written program in a particular language.

If you have a syntax error, your program cannot even be executed because the Python interpreter can't understand your program! __What are some examples of syntax errors?__ &rarr;

<div class="fragment" markdown="block">
* unbalanced quotation marks: <code>print("hello world)</code>
* an invalid variable name: <code>$my_var = "foo"</code>
* etc.
</div>

</section>

<section markdown="block">
##  Runtime Errors

A __runtime error__ is an error that occurs while a syntactically correct program is running. Runtime errors will cause your program to stop (_crash_) if you do not have special code to handle them. 

__What are some examples of runtime errors?__ &rarr;

<div class="fragment" markdown="block">
* adding a string to an int: <code>print(5 + "foo")</code>
* dividing by 0: <code>print(5 / 0)</code>
* etc.
</div>
</section>


<section markdown="block">
##  Logic Errors

A __logic error__ is in an error that occurs in program that is syntactically correct, does not contain runtime errors... but behaves in a way that is unintended or unanticipated. That is, it does not achieve the goals of what the program is meant to do.

__Find the logic error below.__ &rarr;

<pre><code data-trim contenteditable>
#  ask the user for three integers
#  print out the sum of all three integers
num1 = int(input("Give me the first integer\n> "))
num2 = int(input("Give me the second integer\n> "))
num3 = int(input("Give me the third integer\n> ")) 

print(num1 + num2 + num2)
</code></pre>

</section>


<section markdown="block">
##  Ok. So How Do We Fix Errors?

1. don't make mistakes in the first place :P (obvs... but how?)
2. debugging
</section>
<section markdown="block">
##  How to Avoid Bugs

__What are some ways of avoiding bugs?__ &rarr;

<div class="fragment" markdown="block">
* careful planning and design
* set small, incremental goals for your program (don't try and write large programs all at once)
* actually __read__ your code!
* stop and test your work __often__ as you go
* use comments to ignore lines that are giving you trouble, but you want to save for later (__let's see this in action based on our previous code__ &rarr;)
* when testing, try to focus on feature being tested
    * temporarily remove other features
    * or features that work but cause a slow down in test/verify cycle
</div>
</section>

<section markdown="block">
##  Debugging Overview

__What are some ways that you can isolate and find the root cause of errors (we know a couple, we'll introduce a few more)?__ &rarr;

<div class="fragment" markdown="block">
1. go through your code line-by-line
2. want to know what's going on? print it out?
3. use the debugger
4. use the interactive shell
5. use python tutor
</div>
</section>

<section markdown="block">
##  Working Through Code Line-by-Line

This is the simplest, and most important way of finding bugs. __Just read your code!__ &rarr;

Reading through this code carefully would reveal the error!

<pre><code data-trim contenteditable>
#  ask the user for three integers
#  print out the sum
num1 = int(input("Give me the first integer\n> "))
num2 = int(input("Give me the second integer\n> "))
num3 = int(input("Give me the third integer\n> ")) 

print(num1 + num2 + num2)
</code></pre>

This is the most important method of debugging because __this helps increase your code comprehension skills__. Also, you won't have a computer with you during the exam.

</section>


<section markdown="block">
##  Print Stuff Out!

Print out the values of variables to help you isolate where the issue is:

<pre><code data-trim contenteditable>
num1 = int(input("Give me the first integer\n> "))
num2 = int(input("Give me the second integer\n> "))
num3 = int(input("Give me the third integer\n> ")) 

// let's see what's in the input that we asked for!
print(num1, num2, num3)

print(num1 + num2 + num2)
</code></pre>

We'll see that the input looks correct... so clearly, the issue is in the calculation
</section>

<section markdown="block">
##  Use the Debugger 

A __debugger__ is software that lets you step through your code line by line... and it allows you to inspect the values of variables that exist up to a specific line.

* enable the debugger window by clicking on the interactive shell window first
* Debug &rarr; debugger
* make sure that all four checkboxes are checked: stack, locals, source and globals
* run your program (your program will pause immediately)
* then, continually click on "Over" to step through our program line-by-line (we won't be using step or out yet)
* note the values of the variables on the bottom (and the line of code on the top)
* (Go and quit stop your debugging session)
</section>

<section markdown="block">
##  Python Tutor

[Python Tutor](pythontutor.com) is similar to IDLE's debugger, but you access it online.

* go to [pythontutor.com](http://pythontutor.com/)
* click on "Start writing and visualizing now"...
* make sure that you choose Python 3.x from the dropdown
* step through your program line-by-line!

</section>
