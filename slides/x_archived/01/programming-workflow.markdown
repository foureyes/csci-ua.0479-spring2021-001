---
layout: slides
title: Programming Workflow Slides
---
<section markdown="block" class="title-slide">
#  Typical Programming Work Flow
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  The Programming Process
<aside>Generally, programming can be broken down into the following steps</aside>

1. requirements
2. implementation
3. run the program
4. check the output
5. go back to step #2
	* or possibly even #1!
	* do this until... ?

<details markdown="block">
INFO - reconstruct diagram 
</details>
</section>

<section markdown="block">
##  Requirements gathering
* what are you building?
	* "problem" definition
	* how big is it going to be (scope)?
* design 
	* problem solving 
	* system architecture
	* design techniques and documentation
		* flowcharts, sequence diagrams, etc.
		* pseudocode

<details>
QUESTION: flowchart for printing even numbers
QUESTION: pseudocode for printing even numbers
</details>
</section>

<section markdown="block">
##  Coding / Implementation 
* actually writing the source code!
* implementation isn't necessarily just writing new code; it can be:
	* bug-fixing (finding and removing errors) 
	* refactoring (improving a program for efficiency, maintainability, etc.) 
</section>

<section markdown="block">
##  Executing Your Program 
* simply running your program
* our textbook includes compilation (source code to object code) as another explicit step
	* since we're using Python, this isn't something we need to be concerned with
	* we can just execute our code immediately using the interpreter
</section>

<section markdown="block">
##  Checking Output
* was there a __syntax error__ (a problem with the structure of the program)?
* was there a __runtime error__ (an issue that comes up during program execution)?
* is the output what we expected? (a __logic error__)
* if any of the above (each correspond to one of three types of errors: __syntax__, __runtime__, and __logical__) can be answered "yes", then we have to debug:
	* __debugging__ is tracking down the root cause of an error and fixing it
	* may (more often than not, will!) take a long time!

<details markdonw="block">
* QUESTION - what kind of error is forgetting a parentheses?
* QUESTION - what kind of error is adding a number to a string?
</details>
</section>

<section markdown="block">
##  Iteration
* this process is repeated many times
	* our textbook shows that iteration goes back to the writing the source code (implementation) step, but...
	* even the requirements may change!
* the process continues until the requirements or met...
	* or you're sufficiently happy with your program
	* or a deadline comes up
	* or until forever (is this forever?)
</section>

