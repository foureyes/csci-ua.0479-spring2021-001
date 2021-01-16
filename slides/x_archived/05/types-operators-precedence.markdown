---
layout: slides
title: Types and Operator Precedence 
---

<section markdown="block" class="title-slide">
#  Types, Operators, and Precedence
{% include title-slide-footer.html %}
</section>


<section markdown="block">
###  Types

__We know about four or five types.  What are they?__

<div class="incremental" markdown="block"> 
* str
* int
* float
* bool
* (complex)
</div>
<div class="incremental" markdown="block"> 
</div>
</section>

<section markdown="block">
###  Functions

__What's a function?  We know about seven built-in functions.  What are they?  What values do they expect?  What do they return?__

<div class="incremental" markdown="block"> 
* print - doesn't return anything
* type
* int
* str
* float
* bool
* input - always returns a string!
</div>
</section>

<section markdown="block">
###  Types and Operations

__What are some numeric operations that we've used?__

<div class="incremental" markdown="block"> 
* __+__
* __-__
* __/__
* __//__
* __\*\*__
* __%__

(you can mix and match numeric types, __but not other types__)
</div>
</section>

<section markdown="block">
###  Types and Operations (Continued)

__What are some string operations that we've used?__

<div class="incremental" markdown="block"> 
* __+__ - concatenation - only strings
* __\*__ - multiplication - string and int!
</div>
</section>

<section markdown="block">
###  Let's Talk About Comparison Operators

__What are the six comparison operators that we learned about, and how do they work with different types?__

<div class="incremental" markdown="block"> 
* __==__ - different types always return False
* __!=__ - different types always return True
* __<__ - different non numeric types result in an error
* __>__ - different non numeric types result in an error
* __>=__ - different non numeric types result in an error
* __<=__ - different non numeric types result in an error

</div>
</section>

<section markdown="block">
###  Let's Talk About Logical Operators

__What are the three logical operators that we learned about?  Describe when each would return True.__ &rarr;

<div class="incremental" markdown="block"> 
* __and__ - evaluates to True if both operands are True
* __or__ - evaluates to True if either operand is True
* __not__ - evaluates to True if operand is False
</div>
</section>

<section markdown="block">
###  What Order Do All of These Operators Go In?

__So.  With all of these _types_ of operations, what order are they evaluated in?__ &rarr;

<div class="incremental" markdown="block"> 
1. Parentheses
2. Numerical/String operators
3. Comparison operators
4. Logical operators
	1. not
	2. and
	3. or
</div>
</section>

<section markdown="block">
###  Let's Try a Few...

__What boolean value does the following expression evaluate to?__ &rarr;
{% highlight python %}
"five" == 5 or  14 == 7 + 2 * 5
{% endhighlight %}

<div class="incremental" markdown="block"> 
{% highlight python %}
False
{% endhighlight %}

__Aaaaand... how about this one?__ &rarr;

{% highlight python %}
False or True and not False
{% endhighlight %}

{% highlight python %}
True
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Logical Operators and Their Operands

__How many operands does each logical operator take... what type is each operand?__ &rarr;

<div class="incremental" markdown="block"> 
* __and__ - 2 operands - values are treated as boolean
* __or__ - 2 operands - values are treated as boolean
* __not__ - 1 operands - values is treated as boolean
</div>
</section>

<section markdown="block">
###  Watch Out for This!

__Let's write a boolean expression that checks if the variable, _answer_, is equal to "yes" or "yeah":__ &rarr;

<div class="incremental" markdown="block"> 
{% highlight python %}
answer == "yes" or answer == "yeah"
{% endhighlight %}

Note that the following __won't work__!

{% highlight python %}
#  the logical operator, or, tries to treat "yeah" as a bool
answer == "yes" or "yeah"
{% endhighlight %}

__let's try both versions with answer set as "no"__ &rarr;

{% highlight pycon %}
>>> answer = "no"
>>> answer == "yes" or answer == "yeah"
False
>>> answer == "yes" or "yeah"
'yeah'
{% endhighlight %}
</div>

</section>

<section markdown="block">

###  Conditionals

* syntax - if, boolean expression, colon, indented body
* note that the end result of comparisons... are essentially the same as bare literal
* some example code I have takes the shortcut of putting in the bool literal
{% highlight python %}
a, b = 1, 1
if a == b or b == 1 or a == 1:
	print("true")

if True:
	print("true")
{% endhighlight %}
</section>

<section markdown="block">
##  [How to (Un)Complicate Things With If Statements](if-statements-advanced.html)
</section>
