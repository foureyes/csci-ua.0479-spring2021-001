---
layout: slides
title: Boolean Logic 
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Some Computer Science History...
</section>

<section markdown="block">
##  For Context - What's this Boolean Stuff About?
<aside>It's This Guy...</aside>

<div class="img-container" markdown="block">
![George Boole](../../resources/img/boole.jpeg)
</div>
</section>

<section markdown="block">
##  George Boole

<aside markdown='block'>
The _Father_ of Computer Science!  SCIENCE!
</aside>

* English Mathematician, Philosopher and Logician in the 1800's
* Proposed that logical propositions can be expressed by algebraic equations (mathematical logic - AND, OR, NOT)
* This idea, now called __Boolean logic__, is the basis of computer science!
</section>

<section markdown="block">
##  In Python...
As we talked about in the review, Python has a __bool__ type to represent Boolean values

* True or False
* just like other values, can be assigned to variables
* __comparison operators__ (we learned the equality operator) return Boolean values
* Boolean values can be combined into expressions using __logical operators__
</section>

<section markdown="block">
##  Comparison Operators
</section>

<section markdown="block">
##  Comparison Operators
__Can you guess what some of the comparison operators are?  Like I said, you already know one!__ 

There are six comparison operators:

<div class="fragment" markdown="block"> 
* __==__ - equals (can be called logical equivalence or equality operator)
* __!=__ - not equal
* __>__ - greater than
* __<__ - less than
* __>=__ - greater than / equal
* __<=__ - less than / equal
</div>
</section>

<section markdown="block">
##  Comparison Operators Continued
* again - these operators always return a bool
* these operators do what you would expect 
	* __==__ - returns True if both sides are equal &rarr;
	* __!=__ - returns True if both sides are not equal &rarr;
	* __>__, __<__, __>=__, __<=__ - returns True if value on the left is greater than, less than, greater than / equal, or less than equal to the value on the right &rarr;
* never put equals first on >=, <=
</section>

<section markdown="block">
##  Comparison Operators Have Feelings Too
<aside>Just as Sensitive to Type Mismatches as Numeric or String Operators.  Well... At Least Some Are</aside>

__What do you think will happen if we compare 8 >= "four"?__ &rarr;

<div class="fragment" markdown="block"> 

<pre><code data-trim contenteditable>
&gt;&gt;&gt; 8 &gt;= "four"
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: unorderable types: int() &gt;= str()
</code></pre>
</div>

</section>

<section markdown="block">
##  Comparison Operators and Different Types
* objects of different types, except different numeric types, are never equal
	* equals (__==__) will always return False for different types &rarr;
	* not equals (__!=__) will always return True for different types &rarr;
* the <, <=, > and >= operators... 
	* will raise a TypeError if the objects are of different types that cannot be compared &rarr;
	* will happily compare numeric types (for example comparing floats and ints works as you'd expect)! &rarr;
</section>

<section markdown="block">
##  Logical Operators
</section>

<section markdown="block">
##  What are Logical Operators?

__Logical Operators are operators that combine Boolean values.__  

* these operators always return another Boolean value.  
* furthermore, these operators can be used to create more complex Boolean expressions. 
</section>

<section markdown="block">
##   Three Logical Operators:
1. __and__ - 
	* takes two operands, one on each side 
	* to return True, both sides of the operator must be True &rarr;
2. __or__ - 
	* takes two operands, one on each side
	* to return True,at least one side of the operator must be True &rarr;
3. __not__ - 
	* only takes one operand to the right
	* to return True, the original value on the right must evaluate to False &rarr;
	* two nots cancel eachother out (fun!) &rarr;
</section>

<section markdown="block">
##   Logical Operators _in Action_

Note that these are all expressions that result in a value that's of type __bool__:

<pre><code data-trim contenteditable>
&gt;&gt;&gt; True and False
False
&gt;&gt;&gt; True and True
True
&gt;&gt;&gt; True or False
True
&gt;&gt;&gt; not True
False
&gt;&gt;&gt; not not True
True
</code></pre>
</section>

<section markdown="block">
##  That Can Get Complicated!

<aside>Is There a Way to Show All Operands and Results?</aside>

__Yes__.  We'll use __truth tables__ to show what each operator will return.

* a __truth table__ is a concise table of Boolean values that describes the semantics of an operator
* it will go through each possible combination of operands and specify the resulting Boolean value
* each row will represent a combination of operands
* each column will represent a value of one operand
* ...with the exception of the last column, which represents the resulting value
</section>

<section markdown="block">
##  Truth Table - AND

__and__ takes two operands.  Each operand can be True or False (or will evaluate to True or False!).  

__Can you guess how many possible combinations there are for these two operands?__  __What will the Truth Table look like?__ &rarr;

<div class="fragment" markdown="block"> 
<pre><code data-trim contenteditable>
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | q | p and q
----------------
 f | f | f
 f | t | f
 t | f | f
 t | t | t
"""
</code></pre>
</div>
</section>

<section markdown="block">
##  Truth Table - OR

Let's fill out a truth table for __or__! &rarr;

<div class="fragment" markdown="block"> 
<pre><code data-trim contenteditable>
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | q | p and q
----------------
 f | f | f
 f | t | t
 t | f | t
 t | t | t
"""
</code></pre>
</div>
</section>

<section markdown="block">
##  Truth Table - NOT

Let's fill out a truth table for __not__! &rarr;

<div class="fragment" markdown="block"> 
<pre><code data-trim contenteditable>
"""
(using p and q to represent the operands
...and t and f for true and false)
 p | not p
-----------
 t | f 
 f | t 
"""
</code></pre>
</div>
</section>

<section markdown="block">
##  Let's Evaluate Some Simple Boolean Expressions

* True and False &rarr;
* True and not False &rarr;
* True or False &rarr;
* True or not False &rarr;
* False or False &rarr;
* not False and not False &rarr;

</section>

<section markdown="block">
##  Chaining Operators

Boolean, comparison and other operators can be combined to create complex Boolean expressions!  For example:

<pre><code data-trim contenteditable>
100 > 1 and -10 ** 2 <= -100 or "foo" == "foo" + "bar"
</code></pre>

* what order will the operations be evaluated in?
* there is an overall order of operations that exists; [a summary can be found in the official Python 3 documentation](http://docs.python.org/3/reference/expressions.html#operator-precedence)
* __what does the expression above evaluate to?__ &rarr;

<div class="fragment" markdown="block">
True
</div>
</section>


<section markdown="block">
##  Order of Operations / Operator Precedence
The previous summary, but even more _summar-ied_

* parentheses are evaluated first (obv)
* numeric / string operations (in turn, are also ordered)
* comparison operations (==, !=, >, <, >=, >=)
* not
* and
* or
</section>

<section markdown="block">
##  A Quick Note About Boolean Operators and Style
<aside>Because This is Crazy...</aside>
<pre><code data-trim contenteditable>
True and True or False and True and 10 * 10 + 10 == 110 and not False
</code></pre>
* it's usually a good idea to use parentheses, at the very least, for readability 
* ...unless you're chaining the same operator (for example True and True and True)
</section>

<section markdown="block">
##  An Exercise

__Evaluate the following boolean expression.__ &rarr;

<pre><code data-trim contenteditable>
not (8 != 8) or not True  
</code></pre>

<pre><code data-trim contenteditable>
not False or not True  
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
True or False
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
True
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##  Another One

__Evaluate the following boolean expression.__ &rarr;

<pre><code data-trim contenteditable>
"hello" == "world" or 5 + 5 > 8 and 4 * 3 < 16 and 28 != 0
</code></pre>

<pre><code data-trim contenteditable>
"hello" == "world" or 10 > 8 and 12 < 16 and 28 != 0
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
False or True and True and True
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
True
</code></pre>
{:.fragment}

</section>

<section markdown="block">
##  One More Please?

__Evaluate the following boolean expression.__ &rarr;

<pre><code data-trim contenteditable>
((True or False) and not True) and not (False and False)
</code></pre>

<pre><code data-trim contenteditable>
(True and not True) and not (False and False)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
False and True
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
False
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##  Short Circuit Evaluation
* if left hand side of boolean decides the outcome, no need to deal with the remainder of expression
	* saves some processin' time!
	* for example: `(false and (true and true and true or false))`
	* can stop at false!
* can be applied internally to a larger more complex boolean expression
* generally, just language implementation details, right?
	* but it's a concept you should be aware of 
	* (perhaps if there's a function on the right side that doesn't get called!)
</section>

<section markdown="block">
##  Short Circuit Evaluation Continued
__Can you think of some comparison or logical operators where short circuit evaluation wouldn't make sense?__

<div class="fragment" markdown="block"> 
* obv __not__ - nothing to short circuit!
* == equivalence operations - both sides must be evaluated to test equality
</div>
</section>

<section markdown="block">
##  Review
* comparison operators
	* ==, !=, >, <, >=, <=
	* comparing different types
* logical operators
	* and, or, not
	* truth tables
* operator precedence
</section>

