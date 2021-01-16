---
layout: slides
title: Scope
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Global Variables and Function Definitions

__In the following program, will something be printed out, nothing, or an error... and why?__ &rarr;

<pre><code data-trim contenteditable>
{% include classes/15/scope1.py %}
</code></pre>

<div class="fragment" markdown="block">
__s is a global variable__.  It is accessible everywhere, including the function body. 
</div>
</section>

<section markdown="block">
##  Variables Declared Inside a Function

__In the following program, will something be printed out, nothing, or an error... and why?__ &rarr;

<pre><code data-trim contenteditable>
{% include classes/15/scope2.py %}
</code></pre>

<div class="fragment" markdown="block">
An error occurs because s is inaccessible outside of the function definition.  __s is local to the function that it was defined in.__
</div>
</section>

<section markdown="block">
##  Parameters

__In the following program, will something be printed out, nothing, or an error... and why?__ &rarr;

<pre><code data-trim contenteditable>
{% include classes/15/scope2b.py %}
</code></pre>

<div class="fragment" markdown="block">
An error occurs.  You can't access the parameters (by their name) that you passed in to the function from outside of the function.  __Parameters are local to their function.__
</div>
</section>

<section markdown="block">
##  Precedence

__In the following program, will something be printed out, nothing, or an error... and why?__ &rarr;

<pre><code data-trim contenteditable>
{% include classes/15/scope3.py %}
</code></pre>

<div class="fragment" markdown="block">
Variables _created_ within a function are _local_ to that function.  A function will use a __local__ variable before global.  In this case, it will use the _local_ variable, s, instead of the global variable, s.
</div>
</section>

<section markdown="block">
##  A Quick Explanation
</section>

<section markdown="block">
##  Scope

A __scope__: 

* determines where a variable is accessible
* it holds the current set of all available names and the values that they refer to

</section>

<section markdown="block">
##  Global Scope

* anything that we define in the top level of indentation in our program is said to be in the __global scope__
* in the following example, the variables _a_ and _b_ are in the __global scope__
* they can be accessed from anywhere, even within the function

<pre><code data-trim contenteditable>
a, b = 25, "something"

def foo():
	print(a)
	print(b)

foo()
</code></pre>
</section>

<section markdown="block">
##  Local Scope

Variables that are defined in your function (one indentation level in), however, are only available within your function.  They are _local_ to that function.  The example below won't work.

<pre><code data-trim contenteditable>

def foo():
	c = "bar"
	return c

print(c)
</code></pre>
</section>

<section markdown="block">
##  Local Scope Continued

Variables that __are declared__ (created) within a function that have the same name as a global variable are totally different variables/values!  They don't overwrite the outer, global variable (there's a way to do this, though).  What will this print?

<pre><code data-trim contenteditable>
c = "on toast"
def foo():
	c = "grape jelly"
	print(c)

foo()
print(c)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
grape jelly
on toast
</code></pre>

[Obligatory Python tutor version](http://www.pythontutor.com/visualize.html#code=c+%3D+%22on+toast%22%0Adef+foo()%3A%0A%09c+%3D+%22grape+jelly%22%0A%09print(c)%0A%0Afoo()%0Aprint(c)&mode=display&cumulative=true&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)
</div>
</section>

<section markdown="block">
##  A Little More Detail on That Last Point
</section>

<section markdown="block">
##  What's (not) in a Name?


__What is the exact error that you get if you try to use a variable, function or module that you haven't created yet?__ &rarr;

<div class="fragment" markdown="block">
NameError (__Let's try it__ &rarr;)
</div>
</section>

{% comment %}
<section markdown="block">
##  Objects


__What is the the definition of an object again?__ &rarr;

<div class="fragment" markdown="block">
* a _thing_ that a _variable name_ can refer to
* an object can have attributes (data)
* an object can have methods (actions)
</div>
</section>

<section markdown="block">
##  An Object is a Thing That a Variable Name Can Refer To
</section>

<section markdown="block">
##  Objects and Names

__What operator would you use to create a new variable name and bind a value / object to that name (that is, how do you make a name refer to an object)?__ &rarr;

<div class="fragment" markdown="block">
* equals (=)
* my_variable_name = "some value"
</div>
</section>
{% endcomment %}

<section markdown="block">
##  Creating Names

* when you create a variable in a function, you're actually creating a name in the local scope
* if there's a global variable that happens to be the same name, it is not affected!

</section>

<section markdown="block">
##  Finding Names

If you use a variable name in a function, __it will try to find that name in the following places in order__:

* __local__ scope (variables defined in the function)
* __enclosing functions' locals__ (function can be defined within function definitions - we won't be using this, though)
* __global scope__ (variables defined in the top-level of your file)
* __built-ins__ (all of the built-in functions and variables that are available when Python starts)

</section>
<section markdown="block">
##  And So?

__What does the following code print out?__

<pre><code data-trim contenteditable>
color = "blue"

def my_test_function():

	color = "orange"
	print(color)

my_test_function()
print(color)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
orange
blue
</code></pre>
</div>
</section>


<section markdown="block">
##  Scope Summary

* __global scope__ - variables and function definitions declared outside of a function; can be accessed everywhere - from current file or within function definition 
* __local scope__ - variables declared inside of a function; cannot be accessed outside of the function they are created in
* __parameters are local to their function__ - parameters in a function cannot be accessed outside of a function either
* __local variables declared (created) with the same name as a global variable__:
	* are accessed first if referenced in the function definition 
	* does not change value of global variables
</section>
