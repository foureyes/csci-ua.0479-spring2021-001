---
layout: slides
title: Values and Types 
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##   Values
</section>

<section markdown="block">
##   What are Values?
* __values__ are just data
	* for now, a __value__ is a number or a string (we'll see more __types__ of values later) 
	* it can be stored in a variable 
	* it can be part of an __expression__ (a combination of values, operators, functions, etc ... that can be evaluated)
	* but it can't be _evaluated_ any further on its own (2 + 3 is not a value, because it can be evaluated further)
* some examples of values:
	* -123456
	* "a string is a value"
</section>

<section markdown="block">
##   A Note on Values in Code
The representation of a bare value in code is called a __literal__.

* "a string " a __string literal__
* 254 - an __integer literal__
* we'll go over these types in the next few slides
</section>

<section markdown="block">
##   Data Types
</section>

<section markdown="block">
##   Values can be Classified by Data Type
A __data type__ is a set of values.  The type of a value determines how it can be used in expressions.  Sometimes __data type__ is also referred to as just __type__... or __class__.  

__Today, we'll go over the following 4 types__

1. __str__ (string)
2. __int__ (integer)
3. __float__ (floating point)
4. __complex__ (complex numbers)

The last 3 are  __numeric types__.
</section>

<section markdown="block">
##   Strings
</section>

<section markdown="block">
##   What's a String Again?
<div class="fragment" markdown="block">
A __string__ is a sequence of characters.

* any characters
* including spaces and punctuation
* must __start and end__ with quotes!
</div>
</section>


<section markdown="block">
##   Unbalanced Quotes
__What do you think will happen if you have an extra quote?__ 

Let's give it a try: &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
>>> "oops " I quoted again"
SyntaxError: invalid syntax
</code></pre>

If you don't have matching start and end quotes (__unbalanced quotes__) you'll get a syntax error.
</div>
</section>

<section markdown="block">
##   Alternate String Syntax
<aside>You Don't Have to Stick to Double Quotes...</aside>
You can use three different types of quotation marks:

* double quotes

<pre><code data-trim contenteditable>
"double quoted string"
</code></pre>

* single quotes 

<pre><code data-trim contenteditable>
'single quoted string'
</code></pre>

* triple double quotes __for multiline strings__

<pre><code data-trim contenteditable>
"""more than
one line.  omg!"""
</code></pre>

</section>

<section markdown="block">
##   Multiline Strings?
* triple double quotes allow you to span multiple lines 
* single or double quotes do not

__What do you think will happen if you try spanning multiple lines with single or double quotes?__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
>>> "spanning multiple
SyntaxError: EOL while scanning string literal
</code></pre>
</div>
</section>

<section markdown="block">
##   A Quick Aside on Comments
A __comment__ is text in a program that is meant for the human reader; it isn't used by the interpreter.  A comment can be:

* prefixed with the # token
* __or__ surrounded by triple double quotes as a bare string literal

These are both comments: &rarr;
<pre><code data-trim contenteditable>
#   this is a comment
"""
so
is
this
"""
</code></pre>
</section>

<section markdown="block">
##  A Hasty Escape
What if I want to put in a character that has special meaning in a string?  Say, for example... a single or double quote?

* you can use the backslash character before the special character
* for quotes, you can use mixed quotes (embed single quotes in a double quoted string)!
* let's give it a try... &rarr;

<div markdown="block">
<pre><code data-trim contenteditable>
print("escaping using \"backslash\"")
print("single  quotes ''''") 
print("""some "double quotes"""")
</code></pre>
</div>
</section>

<section markdown="block">
##  I Heard You Like Backslashes
<aside>So I...</aside>

__What if you want an _actual_ backslash in your string?__ &rarr;

<div class="fragment" markdown="block">
You can use backslashes to escape backslashes 
<pre><code data-trim contenteditable>
print("I heard you like \\'s, So I put a \\ before your \\")
</code></pre>
</div>
</section>

<section markdown="block">
##  New Lines (Again)

You can actually represent a new line as a character by using:

<pre><code data-trim contenteditable>
\n
</code></pre>

* that's __backslash__, then __n__, or the __newline character__
* so... a multiline string can also be created by using __newline characters__:

<pre><code data-trim contenteditable>
print('two\nlines\n')
</code></pre>
</section>

<section markdown="block">
##  On a Tropical Island
<aside>A Quick Activity</aside>

![jake](../../resources/img/jake.jpeg)
</section>
<section markdown="block">
##  On a Tropical Island Lyrics

These are lyrics to a song called ["On a Tropical Island"](http://www.youtube.com/watch?v=E6-HjFQ_Jtg#t=14)... from a _fine_ cartoon named Adventure Time.  It has a bunch of new lines in it, as well as single quotes.

__How would you get Python to print out these lyrics?  Let's find 2 different ways to print this out.__&rarr;

<pre><code data-trim contenteditable>
On a tropical island,
Underneath a molten lava moon.
Hangin' with the hula dancers,
Askin' questions cause' they got all the answers.
</code></pre>
</section>

<section markdown="block">
##  Numeric Types
<aside>Integers, Floating Point Numbers and Complex Numbers</aside>
</section>

<section markdown="block">
##  Three Numeric Types
The following types are all closely related; most of the same operations can be applied to all of them:

1. __int__ (integer)
2. __float__ (floating point)
3. __complex__ (complex numbers)
</section>

<section markdown="block">
##   int (integer)

__What's an integer?__

<div class="fragment" markdown="block">
* __integer__ - whole number, can be negative
* __int__ is the actual name of the integer type
* 24, -25 &rarr;
* no size limit (well, as much as your computer can handle)!
* for example: 1337 ** 20 &rarr;
</div>
</section>

<section markdown="block">
##   __float__ (floating point)

__What's a floating point number?__

<div class="fragment" markdown="block">
__A floating point number__ represents real numbers

__...but what's a real number?__ &rarr;

* a quantity across a continuous line, like fractions or irrational numbers like pi or the square root of two
* floating point numbers are __indicated by a decimal point__: 5.55555, 5.0 &rarr;
</div>
</section>

<section markdown="block">
##   Really Big or Really Small Numbers
Very __large__ or __small__ floating point numbers are expressed in scientific notation

* 5555 ** 5.0 gives back 5.289569361832972e+18 (that is 5.2389 ... times 10 to the 18th power) &rarr;
* the exponent can be + or - 
* a few more examples:
	* 52e+3 = 52 * 10 ^ 3 = 52000
	* 52e-3 = 52 * 10 ^ -3 = 0.052
* __What is the result of 2e+2?__ &rarr;

<div class="fragment" markdown="block">
* 200.0
</div>
</section>

<section markdown="block">
##   Uh-oh - That's Too Much
<aside>Overflow</aside>

* unlike integers, floats have min and max values... if you have a value that's too big or too small
* sys.float_info.max &rarr;
* 5555**55555.0 &rarr;

<pre><code data-trim contenteditable>
&gt;&gt;&gt; 5555**55555.0
Traceback (most recent call last):
  File "&lt;pyshell#93&gt;", line 1, in &lt;module&gt;
    5555**55555.0
OverflowError: (34, 'Result too large')
&gt;&gt;&gt; 
</code></pre>

<!-- _nomd -->
</section>

<section markdown="block">
##  Complex Numbers
<aside>Um - Does anyone remember these?  I don't</aside>

For completeness... __Python supports complex numbers__

* numbers with square root of -1 / imaginary numbers
* 1j * 1j &rarr;
</section>

<section markdown="block">
##  Don't, Use, That, Comma
Clearly, symbols have special meanings in numeric types

* a decimal point signifies a floating point number
* scientific notation is represented by e and a plus or minus
* j is the imaginary part of a complex number

__However - Don't use commas!  They don't mean what you expect.__ &rarr;
<pre><code data-trim contenteditable>
>>> 3,000
(3, 0)
>>> # huh???
>>> # it's something called a tuple
</code></pre>
</section>

<section markdown="block">
##  So You Don't Know What Type You Have
* There's a function called __type__
* Let's look at it in the interactive shell &rarr;
* Notice the arrow... it says it returns the "type" of the parameter passed in...
* Here's how you would use it: &rarr;

<pre><code data-trim contenteditable>
type(1.0)
</code></pre>
</section>

<section markdown="block">
##  A Guessing Game
<aside>What type is it?</aside>

1. __1__
2. __1.0__
3. __"1"__
4. __"""1.0"""__
5. __1.111__
6. __'1,111'__

<div class="fragment" markdown="block">
1 is an __int__. 2 and 5 are __floats__.  Everything else is a string.
</div>
</section>

<section markdown="block">
##   Reeeeeewind
<aside>A Quick Recap</aside>
* What do we call a bare value in code... like "foo" or 5?
* Name three ways to represent a syntactically correct string in Python
* Name two ways to put a double quote in a string
* How about a backslash, or newline?
* Which type can be affected by really large or small numbers - float or int?
* How can I tell if a number is a float?
* What function could I use to determine the type of a value or variable?
* What are two ways of representing comments?
</section>

<section markdown="block">
##   [Next: Operations and Variables](operations-and-variables.html)
</section>
