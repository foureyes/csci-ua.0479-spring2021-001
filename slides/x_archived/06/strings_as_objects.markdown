---
layout: slides
title: String Objects, String Methods 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Objects and Methods (Again!)

__What's an object?  What's a method?  Give some examples. &rarr;__

<div class="fragment" markdown="block">
* __object__ - a _thing_ that a variable name can refer to, like a string or integer
* for us that means attributes (data) and methods (functions)... all packed into one thing
* a __method__ is essentially a function that's associated with a particular object
* a __methods__ can be thought of as an action behavior that an object can perform
</div>
</section>

<section markdown="block">
##  Calling Methods

How do you call a method?  For example, if you had a string named food, that contains the value "pizza", __how would you call the upper method on it to tell it to give back an uppercase version of itself? &rarr;__

<pre><code data-trim contenteditable>
food = "pizza"
#  tell food to give back an uppercase version of itself
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
food.upper()
#  use the object name
#  followed by dot
#  and the method (from here, it's like a regular function)
#  notice that upper has no arguments
</code></pre>
</div>
</section>

<section markdown="block">
##  Strings Methods!

Strings are objects. They have methods. Lots of 'em!

1. __upper__() 
2. __lower__()
3. __capitalize__()
4. __title__()
5. __isdigit__()
6. __isnumeric__()
7. __isalpha__()
8. __isspace__()

__to be continued in next slide!__ &rarr;
</section>

<section markdown="block">
##  Even More String Methods!

1. __find__(sub[, start[, end]])
2. __format__(...)
3. __strip__([chars])
4. __isupper__()
5. __islower__()
6. __count__(...)
7. __replace__(...)

<br>
In the interactive shell, you could use the __dir__ with a string in parentheses to show all of the methods of an object:


<pre><code data-trim contenteditable>
dir("some string")
</code></pre>
</section>

<section markdown="block">
##  Casing Methods

__upper__(), __lower__(), __capitilize__(), and __title__() return the string that the method was called on as all uppercase, all lowercase, first letter uppercase, and title-cased (first letter of every word uppercase).  __What would the following print out? &rarr;__

<pre><code data-trim contenteditable>
print("this should be uppercase".upper())
print("THIS SHOULD BE LOWERCASE".lower())
print("this should be uppercase".capitalize())
print("this should be uppercase".title())
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
THIS SHOULD BE UPPERCASE
this should be lowercase
This should be uppercase
This Should Be Uppercase
</code></pre>
</div>
</section>

<section markdown="block">
##  isdigit(), isnumeric() and isalpha()

__isdigit__(), __isnumeric__() and __isalpha__() test whether a string is __only__ composed of all numbers or all letters (all three return False if empty string).  __What would the following print out? &rarr;__

\* __isnumeric__() also returns true for numeric characters other than 0-9, such as '⅕'.

<pre><code data-trim contenteditable>
print("123".isdigit())            # True
print("1.23".isdigit())           # False (. is not 0 - 9)
print("one two three".isdigit())  # False (not 0 - 9)
print("onetwothree".isalpha())    # True
print("one two three".isalpha())  # False (has spaces)
print("one!".isalpha())           # False (has !)
print("1".isalpha())              # False (it's a digit)
print("⅕".isdigit())              # False (not 0 - 9)
print("⅕".isnumeric())  # True (isnumeric allows other numeric chars)
</code></pre>

</section>


<section markdown="block">
##  isspace()

__isspace__() gives back true if all of the characters in the string it's called on is white space - any kind of _white space_. __What is the output of the following?__ &rarr;

<pre><code data-trim contenteditable>
print("             ".isspace())
print("\n".isspace())
print("some    space".isspace())
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
True
True
False
</code></pre>
</div>
</section>

<section markdown="block">
##  find()

__find__() returns the first index where the argument (a character or substring) is found.  It returns -1 if the substring is not in the original string.

<pre><code data-trim contenteditable>
print("hello".find("h"))
print("hello".find("x"))
print("hello".find("lo"))
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
0
-1
3
</code></pre>
</div>
</section>

<section markdown="block">
##  strip()

__strip__() removes leading and trailing whitespace (it can also remove other leading and trailing characters).  What do you think this results 

<pre><code data-trim contenteditable>
print("  spaces all around   ".strip())
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
spaces all around
</code></pre>
</div>
</section>

<section markdown="block">
##  format()

Format is like the string formatting operator, but possibly easier?! 

* instead of %s, use curly braces and the number of the argument as a placeholder {0}, {1}
* numer corrseponds to each argument in the call, 0 being the first
* __What do you think the following returns? &rarr;__

<pre><code data-trim contenteditable>
"{0} elephants".format("twenty")
"{0} elephants".format(20)
"{0} elephants".format(20, 100)
"{1} elephants".format(20, 100)
"{0} elephants and {1} peanuts".format(20, 100)
</code></pre>
</section>

<section markdown="block">
##  format() results

<pre><code data-trim contenteditable>
twenty elephants
20 elephants
20 elephants
100 elephants
20 elephants and 100 peanuts
</code></pre>
</section>

<section markdown="block">
##  isupper() and islower()

__isupper__() and __islower__() return True if the string that is called on is the case specified.  __What does the following output?__ &rarr;

<pre><code data-trim contenteditable>
print("this should be uppercase".isupper())
print("THIS SHOULD BE LOWERCASE".isupper())
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
False
True
</code></pre>
</div>
</section>


<section markdown="block">
##  count(), replace()

__count__(s) ...counts the number of times substring, s, occurs in the original string.

<pre><code data-trim contenteditable>
'aardvark'.count('a') # --> 3
</code></pre>

__replace__(s, new_s) ...replaces all occurrences of substring, s, with new_s. (note that this gives back a __new string__, and it does not change the original)

<pre><code data-trim contenteditable>
'aardvark'.replace('a', '42') # --> 4242rdv42rk
</code></pre>
</section>

<section markdown="block">
##  A Couple of Exercises:

* use upper or lower to check for permutations for input
	* for example, loop forever
	* ask the user if they want the loop to stop
	* accept "Yes", "YES", "yes", etc.
* rewrite get_first_word, but use __find__() instead of a loop
</section>
