---
layout: slides
title: Conditionals Intro
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Boolean Values

__What are the two possible Boolean values?  How are they represented in Python?__ &rarr;

<div class="fragment" markdown="block"> 
* Boolean values can be either true or false
* In Python, these values are represented by the reserved words, __True__ and __False__ (notice that the initial letter is uppercase)
* In Python, the type of these values is __bool__ &rarr;
</div>
</section>

<section markdown="block">
##  A Quick Aside on bool Types

__If bool is the name of the type, what do you expect the name of the function to convert to this type is?__  &rarr;

<div class="fragment" markdown="block"> 
<pre><code data-trim contenteditable>
>>> bool(0)
False
>>> bool("a string")
True
>>>
</code></pre>
</div>
</section>

<section markdown="block">
##  == And =
__What's the difference between == and =?__ &rarr;

<div class="fragment" markdown="block"> 
* __==__ (double equals) is the equality operator 
	* tests if the operand on left _is equal_ to the operand on the right
	* also called __logical equivalence__
	* "foo" == "bar" &rarr;
* __=__ (equals) is the assignment operator
	* assigns the operand on the right to the variable on the left
	* sometimes called binding
	* a = "foo"
</div>
</section>

<section markdown="block">
##  The Equality Operator 

Some details about how __==__ works:

* two different types (except if they're both numeric), __are never considered equal__  
* two different numeric types can be equal
* when comparing strings, case matters

A few examples:

* "One" == "one"
* 1 = "1.0"
* 1 == "1" 
* 1 == 1.0

</section>

<section markdown="block">
##  If Statements
__How do we construct an if statement?  Why does indentation matter?__

<div class="fragment" markdown="block"> 

<pre><code data-trim contenteditable>
print("before my if statement")
if foo == bar:
	print "they are equal"
print("after my if statement")
</code></pre>

* indentation signifies a block of code
* the indented block of code immediately after the condition and colon will be executed if the condition is true
</div>
</section>

<section markdown="block">
##  On Indentation
__Um, BTW - how do we know when a block of code ends?__ &rarr;

<div class="fragment" markdown="block"> 
* no more lines
* next line is back one level of indentation
</div>
</section>

<section markdown="block">
##  This or That
__What construct (keyword) would you used to execute a block of code only if the condition in the original if-statement is not met?  What is the syntax for using it?__ &rarr;

<div class="fragment" markdown="block"> 
<pre><code data-trim contenteditable>
#  use the keyword, else
if some_boolean_expression:
	print('yes, that\'s true!')
else:
	print('nope, totally false!')
</code></pre>

Note that else will always have a corresponding if statement.
</div>
</section>


<section markdown="block">
##  What's the Output? Part 1!

__What's the output of this program?__ &rarr;

<pre><code data-trim contenteditable>
flag = True
print('one')
if flag:
	print('two')
else:
	print('three')
print('four')
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
one
two
four
</code></pre>
</div>
</section>




<section markdown="block">
##  What's the Output? Part 2!

__What is the output of this program if the user enters 'Yes', 'yes', and 'whatevs'?__ &rarr;

<pre><code data-trim contenteditable>
answer = input("you have 12 doughnuts, would you like another dozen?\n>")
if answer == 'yes':
	print('you have 24 doughnuts')
else:
	print('you have 12 doughnuts')
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
you have 12 doughnuts, would you like another dozen?
>Yes
you have 12 doughnuts

you have 12 doughnuts, would you like another dozen?
>yes
you have 24 doughnuts

you have 12 doughnuts, would you like another dozen?
>whatevs
you have 12 doughnuts
</code></pre>
</div>
</section>

<section markdown="block">
##  What's the Output? Part 3!

__What happens if the user enters 16?__ &rarr;

<pre><code data-trim contenteditable>
answer = input('what is 2 to the 4th power?\n>')
if answer == 2 ** 4:
	print('yup, you got it!')
else:
	print('close, but no cigar!')
</code></pre>

<pre><code data-trim contenteditable>
close, but no cigar!
</code></pre>
{:.fragment}

__...will this ever print 'yup, you got it!'?  why?__ &rarr;
{:.fragment}

no, because it is always comparing a string to an int
{:.fragment}
</section>

<section markdown="block">
##  Number Guessing Game

__Create a game that__ &rarr;

* hardcodes a "secret" number 
* asks the user to guess that secret number
* prints out an appropriate message depending if the guess is correct (see 2 runs below)

<pre><code data-trim contenteditable>
please enter a number
>2
the secret number was 5, not 2
</code></pre>
<pre><code data-trim contenteditable>
please enter a number
>5
yeah, you got it!
</code></pre>
</section>

<section markdown="block">
##  A Possible Solution

<pre><code data-trim contenteditable>
secret = 5
n = int(input('please enter a number\n>'))
if n == secret:
	print('yeah, you got it!')
else:
	print('the secret number was ' + str(secret) + ', not ' + str(n))
</code></pre>

</section>


<section markdown="block">
##  A Few Terms

if statement __header__ line and __body__:

<pre><code data-trim contenteditable>
n = int(input("number plz\n>")

#  if statement header line
if n == 42:

	# if statement body
	print('that's the meaning of life!')
	print('!!!!')

</code></pre>

</section>

<section markdown="block">
##  One Last Pass

You can use the keyword __pass__ to tell Python to do nothing.  __What do you think this prints out?__ &rarr;

<pre><code data-trim contenteditable>
if True:
	pass
</code></pre>
<div class="fragment" markdown="block"> 
nothing!
</div>
</section>

{% comment %}
<section markdown="block">
##  [Boolean Logic](boolean-logic.html)
<aside markdown="block">
[Oh, and a handout](../../resources/handouts/class05/input-types-if.pdf)
</aside>
</section>
{% endcomment %}
