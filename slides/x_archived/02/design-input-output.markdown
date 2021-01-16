---
layout: slides
title: Design, Input, Processing, and Output
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>
<section markdown="block">
##  Review of the Programming Workflow

__What are steps involved in creating a program?__ &rarr;

(hint: it's not just _program something_!)

<div class="fragment" markdown="block">
1. requirements
2. implementation
3. run the program
4. check the output
5. go back to step #2 (or possibly even #1!)
</div>
</section>

{% comment %}
<section markdown="block">
##  Programming Workflow Continued

Note that {{site.bookq}} mentions a very similar workflow (ehhh... they're pretty much say the same thing; I'd accept either on an exam):

1. design the program
2. write the code
3. correct syntax errors
4. test the program
5. correct logic errors
(go back to step 1)
</section>
{% endcomment %}

<section markdown="block">
##  Some Steps are More Important Than Others

__Which of these steps do you think is the most important?__ &rarr;

1. design the program
2. write the code
3. correct syntax errors
4. test the program
5. correct logic errors
{:.fragment}

</section>

<section markdown="block">
##  Requirements Gathering / Design

It would seem like the most important part of programming is... well... _programming_.  However, __determining what you're programming and how you're going to do it__ is arguably more important!  Before getting into code, you must:

* understand what your program is supposed to do 
	* (through requirements gathering)
* ...and design how your program will work
	* this is the foundation of your program!
	* can you break down your program into discrete tasks or components?
	* is there an algorithm involved?
</section>

<section markdown="block">
##  Some Tools in Your Toolbox

{{ site.bookq }} introduces two tools to help start thinking about program design:

* pseudocode
* flow charts

</section>


<section markdown="block">
##  Pseudocode

Sometimes it's helpful to not have to deal with the syntax intricacies and implementation details with writing actual code.

* that's where __pseudocode__ comes in!
* __pseudocode__ is basically _fake_ code
* it's more like natural language!
* used to sketch out actual code... for example, think of a thermostat program

<pre><code data-trim contenteditable>
measure the temperature of the room
if it's over the temperature threshold
	turn on the air conditioner
</code></pre>
</section>

<section markdown="block">
##  Flow Charts

Flow charts help graphically depict the steps involved in a process or program.  Here are some  common elements in a flow chart:

<div class="img-container" markdown="block">
![Flow Chart Elements](../../resources/img/flow.png)
</div>
</section>

<section markdown="block">
##  Fortune Telling Program

Imagine the following fortune telling program:

<pre><code data-trim contenteditable>
What is your question?
&gt; What's the meaning of life?
42
</code></pre>

The corresponding flow chart may look like...
</section>

<section markdown="block">
##  Fortune Telling Program Flow Chart

Here's what the flow chart for the previous program might look like:

<div class="img-container" markdown="block">
![Fortune Telling Program Flow Chart](../../resources/img/fortune-flow.png)
</div>
</section>

<section markdown="block">
##  Make a Flow Chart for an ATM

<aside>What do you think this would look like?</aside>
</section>

<section markdown="block">
##  ATM Flow Chart, Example 1

<div class="img-container" markdown="block">
![ATM v1](../../resources/img/atm-flow.png)
</div>
</section>

<section markdown="block">
##  ATM Flow Chart, Example 2

<div class="img-container" markdown="block">
![ATM v2](../../resources/img/atm-flow-2.png)
</div>
</section>

<section markdown="block">
##  Input, Processing, and Output

The majority of the programs that we write in class will consist of:

* user driven input (usually via keyboard)
* some sort of processing on the input data
* ... and finally output (usually via the Python console)
</section>

