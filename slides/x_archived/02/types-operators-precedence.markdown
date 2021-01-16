---
layout: slides
title: Types and Operator Precedence 
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Types

__We know about four or five types.  What are they?__

* {:.fragment} str
* {:.fragment} int
* {:.fragment} float
* {:.fragment} bool
* {:.fragment} (complex)
</section>

<section markdown="block">
##  Functions

__What's a function?  We know about seven built-in functions.  What are they?  What values do they expect?  What do they return?__

* {:.fragment} print - doesn't return anything
* {:.fragment} type
* {:.fragment} int
* {:.fragment} str
* {:.fragment} float
* {:.fragment} bool
* {:.fragment} input - always returns a string!
</section>

<section markdown="block">
##  Types and Operations

__What are some numeric operations that we've used?__

* {:.fragment} __+__
* {:.fragment} __-__
* {:.fragment} __/__
* {:.fragment} __//__
* {:.fragment} __\*\*__
* {:.fragment} __%__

(you can mix and match numeric types, __but not other types__)
{:.fragment}
</section>

<section markdown="block">
##  Types and Operations (Continued)

__What are some string operations that we've used?__

* {:.fragment} __+__ - concatenation - only strings
* {:.fragment} __\*__ - multiplication - string and int!
</section>

<section markdown="block">
##  Let's Talk About Comparison Operators

__What are the six comparison operators that we learned about, and how do they work with different types?__

* {:.fragment} __==__ - different types always return False
* {:.fragment} __!=__ - different types always return True
* {:.fragment} __<__ - different non numeric types result in an error
* {:.fragment} __>__ - different non numeric types result in an error
* {:.fragment} __>=__ - different non numeric types result in an error
* {:.fragment} __<=__ - different non numeric types result in an error
</section>

<section markdown="block">
##  Let's Talk About Logical Operators

__What are the three logical operators that we learned about?  Describe when each would return True.__ &rarr;

* {:.fragment} __and__ - evaluates to True if both operands are True
* {:.fragment} __or__ - evaluates to True if either operand is True
* {:.fragment} __not__ - evaluates to True if operand is False
</section>

<section markdown="block">
##  What Order Do All of These Operators Go In?

__So.  With all of these _types_ of operations, what order are they evaluated in?__ &rarr;

1. {:.fragment} Parentheses
2. {:.fragment} Numerical/String operators
3. {:.fragment} Comparison operators
4. {:.fragment} Logical operators
	1. {:.fragment} not
	2. {:.fragment} and
	3. {:.fragment} or
</section>

<section markdown="block">
##  Let's Try a Few...

__What boolean value does the following expression evaluate to?__ &rarr;
<pre><code data-trim contenteditable>
"five" == 5 or  14 == 7 + 2 * 5
</code></pre>

<pre><code data-trim contenteditable>
False
</code></pre>
{:.fragment}

__Aaaaand... how about this one?__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
False or True and not False
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
True
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##  Logical Operators and Their Operands

__How many operands does each logical operator take... what type is each operand?__ &rarr;

* {:.fragment} __and__ - 2 operands - values are treated as boolean
* {:.fragment} __or__ - 2 operands - values are treated as boolean
* {:.fragment} __not__ - 1 operands - values is treated as boolean
</section>

<section markdown="block">
##  Watch Out for This!

__Let's write a boolean expression that checks if the variable, _answer_, is equal to "yes" or "yeah":__ &rarr;

<pre><code data-trim contenteditable>
answer == "yes" or answer == "yeah"
</code></pre>
{:.fragment}

Note that the following __won't work__!
{:.fragment}

<pre><code data-trim contenteditable>
#  the logical operator, or, tries to treat "yeah" as a bool
answer == "yes" or "yeah"
</code></pre>
{:.fragment}

__let's try both versions with answer set as "no"__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
>>> answer = "no"
>>> answer == "yes" or answer == "yeah"
False
>>> answer == "yes" or "yeah"
'yeah'
</code></pre>
{:.fragment}

</section>

<section markdown="block">

##  Conditionals

* syntax - if, boolean expression, colon, indented body
* note that the end result of comparisons... are essentially the same as bare literal
* some example code I have takes the shortcut of putting in the bool literal
<pre><code data-trim contenteditable>
a, b = 1, 1
if a == b or b == 1 or a == 1:
	print("true")

if True:
	print("true")
</code></pre>
</section>

<section markdown="block">
##  [How to (Un)Complicate Things With If Statements](if-statements-advanced.html)
</section>
