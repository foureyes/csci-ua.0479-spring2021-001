---
layout: slides
title: Exceptions 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Exceptions

Errors that occur during runtime are called __exceptions__.
</section>

<section markdown="block">
##  Exceptions in the Wild

__What are some exceptions that we've seen?  That is, what errors have occurred during runtime?__ 

<div class="fragment" markdown="block">
* using an out of range index on a list or string that's
* dividing by zero
* using an undefined variable
* using an operator on incompatible types
* converting a value to a type that it can't be converted to
* __Let's try to cause some exceptions!__
</div>
</section>

<section markdown="block">
##  Exception Examples

<pre><code data-trim contenteditable>
Traceback (most recent call last):
  File "/tmp/exceptions.py", line 1, in &lt;module&gt;
    5 / 0
ZeroDivisionError: integer division or modulo by zero

Traceback (most recent call last):
  File "/tmp/exceptions.py", line 1, in &lt;module&gt;
    int("foo")
ValueError: invalid literal for int() with base 10: 'foo'

Traceback (most recent call last):
  File "/tmp/exceptions.py", line 2, in &lt;module&gt;
    print(a[3])
IndexError: list index out of range

Traceback (most recent call last):
  File "/tmp/exceptions.py", line 1, in &lt;module&gt;
    "foo" + 5
TypeError: cannot concatenate 'str' and 'int' objects
</code></pre>
</section>

<section markdown="block">
##   A Closer Look at a Runtime Error
<pre><code data-trim contenteditable>
Traceback (most recent call last):
  File "/tmp/exceptions.py", line 1, in &lt;module&gt;
    "foo" + 5
TypeError: cannot concatenate 'str' and 'int' objects
</code></pre>

We see the following details:

* which file caused the exception
* the line number
* the actual code that caused it
* the kind of exception / error plus some additional details
</section>

<section markdown="block">
##  Types of Exceptions 

A list of [all exception types](http://docs.python.org/3.2/library/exceptions.html) can be found at: [http://docs.python.org/3.2/library/exceptions.html](http://docs.python.org/3.2/library/exceptions.html)

The base exception is just Exception, but there are specific ones after that.  From the previous slides, and our past experience programming, some exceptions we've seen include:

* ZeroDivisionError
* IndexError
* TypeError
* NameError
* ValueError
</section>

<section markdown="block">
##  What do all of These Errors Mean!?

* ZeroDivisionError
* IndexError
* TypeError
* NameError
* ValueError


<div class="fragment" markdown="block">
* ZeroDivisionError - divide by zero
* IndexError - index out of range
* TypeError - function or operation applied to inappropriate type
* NameError - name (variable, function, etc) doesn't exist / not yet declared
* ValueError - function or operation gets right type, but inappropriate value
</div>
</section>

<section markdown="block">
##  So Many Exceptions

The root Exception, and the other exception types that follow from it is called an __exception hierarchy__
</section>

<section markdown="block">
##  Great, so Now What?

We can gracefully recover from exceptions!

For example, a common source of runtime errors is user input...
</section>

<section markdown="block">
##  A Short Program

Let's write a simple  __interactive program__ that converts inches to feet:

* __ask for numeric input__ - some number of inches
* __accept decimal values as well__, such as 1.5 inches
* __divide that number by 12__ to get feet
* print out the result

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
inches = input("inches\n>")
print(float(inches)/12)
</code></pre>
</div>
</section>

<section markdown="block">
##  Soooo... That Works Great

Let's try running the program...

Everything works fine until?  __Is there a certain kind of input that will cause an error in this program?__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
inches
>asdf
Traceback (most recent call last):
  File "foo.py", line 2, in &lt;module&gt;
    print(float(inches)/23)
ValueError: invalid literal for int() with base 10: 'asdf'
</code></pre>
</div>
</section>

<section markdown="block">
##  Can We Prevent This Error from Happening?

__...Maybe!  Let's try a couple of things.__ &rarr;

<div class="fragment" markdown="block">
How about isdigit and isnumeric?

<pre><code data-trim contenteditable>
s = 'asdf'
print(s.isdigit())
print(s.isnumeric())
</code></pre>

But they don't let legitimate input through!

<pre><code data-trim contenteditable>
s = '3.2'
print(s.isdigit())
print(s.isnumeric())
</code></pre>

</div>
</section>

<section markdown="block">
##  "Defensive Programming" Continued

__Any other ways to allow strings like 3.2 in, but still prevent strings that are not composed numbers and a decimal point?__ &rarr;

<div class="fragment" markdown="block">
* loop through every character, and make sure that it's only a number or a decimal point!?
* use find to check for decimal; create another string without that and check if it's a digit
* _ughhhh_ ... nevermind, these all seem a bit clunky
</div>
</section>

<section markdown="block">
##  EAFP

Sometimes it's...

<strong>E</strong>asier to <strong>A</strong>sk <strong>F</strong>orgiveness than <strong>P</strong>ermission

* instead of defensive programming...
* let's just try it
* and ask for forgiveness if we made a mistake
</section>

<section markdown="block">
##  Exception Handling

There's a construct in most programming languages that lets you handle exceptions.  In python, that construct is a __try-except__ block.  It's similar to an if-else:

<pre><code data-trim contenteditable>
try:
	# stuff that I want to do
except:
	# stuff to do if an error occurs
</code></pre>
</section>

<section markdown="block">
##  try-except

* The __try__ block watches out for any statements within that block that causes errors.
* If there is an error, the code in the __except__ block will be run. 
* Otherwise, the code will execute normally (ignoring the except block)

</section>

<section markdown="block">
##  try-except Example 1

__What is the output of this code?__

<pre><code data-trim contenteditable>
a = [1, 2, 3]
try:
	print(a[100])
except:
	print("sorry, try another!")
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
sorry, try another!
</code></pre>
</div>
</section>

<section markdown="block">
##  try-except Example 2

__What is the output of this code?__

<pre><code data-trim contenteditable>
a = [1, 2, 3]
try:
	print(a[0])
except:
	print("sorry, try another!")
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
1
</code></pre>
</div>
</section>

<section markdown="block">
##  Let's Take Another Look at Our Conversion Program

__Let's modify our program so that it behaves in a similar way, but uses try-except instead of testing with an if statement first.__

<pre><code data-trim contenteditable>
inches = input("inches\n>")
print(float(inches)/12)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
inches = input("inches\n>")
try:
    print(float(inches)/12)
except:
    print("don't do that")
</code></pre>
</div>
</section>

<section markdown="block">
##   Other Exceptions

We saw that we could handle a ValueError in our program.  __Can that exception happen in the following program?  Are there any other exceptions (that we just talked about in an earlier slide) that can happen?__ &rarr;

<pre><code data-trim contenteditable>
#  of slices in a pie
people = input("how many people are eating pizza?\n>")
print("Each person can have %s slices" % (8/int(people)))
</code></pre>
<div class="fragment" markdown="block">
* ValueError - for non numeric input
* ZeroDivisionError - for 0 as input
</div>
</section>

<section markdown="block">
##  Fixing the Pizza Pie Problems 

__How do we fix it (original code below)?__ &rarr;

<pre><code data-trim contenteditable>
#  of slices in a pie
people = input("how many people are eating pizza?\n>")
print("Each person can have %s slices" % (8/int(people)))
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
#  of slizes in a pie
people = input("how many people are eating pizza?\n>")
try:
    print("Each person can have %s slices" % (8/int(people)))
except:
    print("No one's gettin' nuthin'")
</code></pre>
</div>
</section>

<section markdown="block">
##  Fixing the Pizza Pie Problems Continued

What if we want to deal with ValueErrors and ZeroDivisionError differently?

Say either:

1. That's not a number! (ValueError)
2. More for me! (ZeroDivisionError)
</section>

<section markdown="block">
##  Specific Exceptions, Multiple Except Blocks

You can catch specific exception types, and add an arbitrary number of except blocks for every exception type that may occur.

<pre><code data-trim contenteditable>
try:
	# some tricky stuff
except NameOfErrorType1:
	# handle it gracefully
except NameOfErrorType2:
	# handle it gracefully too
</code></pre>
</section>

<section markdown="block">
##  Back to Pizza

__So... let's apply that to our pizza program__ &rarr;

<pre><code data-trim contenteditable>
people = input("how many people are eating pizza?\n>")
try:
    print("Each person can have %s slices" % (8/int(people)))
except:
    print("No one's gettin' nuthin'")
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
people = input("how many people are eating pizza?\n>")
try:
    print("Each person can have %s slices" % (8/int(people)))
except ZeroDivisionError:
    print("More for me!")
except ValueError:
    print("That's not a number!")
</code></pre>
</div>
</section>


<section markdown="block">
##  Implement Three Card Monte

Here's a text version of [three card monte](http://en.wikipedia.org/wiki/Three-card_Monte).

<pre><code data-trim contenteditable>
pick a cup: 0, 1, or 2
>0
['.', 'o', 'o']
you win

pick a cup: 0, 1, or 2
>0
['o', '.', 'o']
you lose

pick a cup: 0, 1, or 2
>asdf
['.', 'o', 'o']
not a number
you lose

pick a cup: 0, 1, or 2
>400
['o', '.', 'o']
that cup doesn't exist
you lose
</code></pre>
</section>

<section markdown="block">
##  Three Card Monte Requirements

* in our version, we're using "cups"
* keep a penny under 1 cup
* represent the three cups as a list
* 'o' for empty '.' for a penny
* "shuffle" the list
* ask for input... a number that's 0, 1, or 2
* if the program gets non-numeric input, say that it's not a number
* if the number causes an IndexError, say that the cup doesn't exist
* if either exception occurs, the player loses
* if the user finds the penny, the player wins
</section>

<section markdown="block">
##   A Potential Solution

<pre><code data-trim contenteditable>
import random
cups = ['o', '.', 'o']
random.shuffle(cups)
n = input("pick a cup: 0, 1, or 2\n>")
result = None

print(cups)
try:
    result = cups[int(n)]
except IndexError:
    print("that cup doesn't exist")
except ValueError:
    print("not a number")

if result == ".":
    print("you win")
else:
    print("you lose")
</code></pre>
</section>
