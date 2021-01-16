---
layout: slides
title: Functions 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  A Quick Review
</section>

<section markdown="block">
##  Write a Function... 

* call it join_three_strings
* it should take three arguments: a, b, c
* it should return a single string composed of a, b, and c __separated__ by a space
* handle non-string arguments (see last example)

Example Usage:

<pre><code data-trim contenteditable>
&gt;&gt;&gt; print(join_three_strings('one', 'two', 'three'))
one two three
&gt;&gt;&gt; print(join_three_strings('1', '2', '3'))
1 2 3
&gt;&gt;&gt; print(join_three_strings(1, 2, 3))
1 2 3
</code></pre>

__Let's write this function together &rarr;__
</section>

<section markdown="block">
##  Join Three Strings Solution
<pre><code data-trim contenteditable>
{% include classes/16/join_three_strings.py %}
</code></pre>
</section>

<section markdown="block">
##  Syntax
A quick summary on syntax:
&lt;pre&gt;&lt;code data-trim contenteditable&gt;
def &lt;function_name&gt;(&lt;zero_or_more_parameters&gt;):
	&lt;statement #1&gt;
	&lt;statement #2&gt;
	.
	.
	&lt;etc.&gt;
</code></pre>
</section>

<section markdown="block">
##  Parameters
<pre><code data-trim contenteditable>
{% include classes/16/join_three_strings.py %}
</code></pre>

__What are the values of a, b and c in the above function when called as below:&rarr;__
<pre><code data-trim contenteditable>
join_three_strings('one', 'two', 'three')
</code></pre>
<pre><code data-trim contenteditable>
join_three_strings('three', 'one', 'two')
</code></pre>
<pre><code data-trim contenteditable>
a = 'three'
b = 'two'
c = 'one'
join_three_strings(c, b, a)
</code></pre>

<div class="fragment" markdown="block">
* a = 'one', b = 'two', c = 'three'
* a = 'three', b = 'one', c = 'two'
* a = 'three', b = 'two', c = 'one'
</div>
</section>

<section markdown="block">
##  Parameters Summary
* __parameters__ 
	* variable names used within a function 
	* reference the values passed in as arguments
* parameters are positional; order determines what names match to what variables
	* def f(p1, p2, p3):
	* p1 will refer to the first value passed in
	* p2 to the second
	* etc.
</section>

<section markdown="block">
##  Return Values
__What's the difference between these two definitions of our function?  What gets printed out for each code sample? &rarr;__

Version #1

<pre><code data-trim contenteditable>
{% include classes/16/join_three_strings.py %}
print(join_three_strings('one', 'two', 'three'))
</code></pre>

Version #2

<pre><code data-trim contenteditable>
{% include classes/16/join_three_strings_no_return.py %}
print(join_three_strings('one', 'two', 'three'))
</code></pre>
</section>

<section markdown="block">
##  Return Values Continued
The first definition (#1) returns a string, while the other (#2) doesn't return a value.  

Printing out the __results__ of both functions gives:

1. Version #1
    * <code class="inline">one two three</code>
    * (this function returns a string, and the caller prints)
2. Version #2
    * <code class="inline">one two three</code>
    * <code class="inline">None</code>
    * (this function prints out the string itself, and then returns no value, or `None`)
</section>

<section markdown="block">
##  The Return Statement
* a function can return a value after it is called
* this is done by using the __return__ statement
* the __return__ statement immediately stops the execution of a function
* ...and returns the value that follows it 
	* the value can be any value! (return True)
	* it can even be an expression (return 1 + 1)
* if a function doesn't explicitly return a value, it gives back __None__, a special value that means the absence of a value
</section>

<section markdown="block">
##  Defining vs Calling 
__What gets printed out for each version of code?__
<pre><code data-trim contenteditable>
#  version 1
{% include classes/16/join_three_strings.py %}
</code></pre>
<pre><code data-trim contenteditable>
#  version 2
{% include classes/16/join_three_strings.py %}
join_three_strings('one', 'two', 'three')
</code></pre>
<pre><code data-trim contenteditable>
#  version 3
{% include classes/16/join_three_strings.py %}
print(join_three_strings('one', 'two', 'three'))
</code></pre>
<div class="fragment" markdown="block">
1: nothing, 2: nothing, 3: `one two three`
</div>
</section>

<section markdown="block">
##  Testing Programs / Functions
__So far, we've tested our programs by:__ &rarr;

<div class="fragment" markdown="block">

* printing things out to the screen
* manually inspecting the output
* ...for every test case that we have
</div>

<div class="fragment" markdown="block">
__Some shortcomings of manual testing__ &rarr;
</div>

<div class="fragment" markdown="block">

* it's tedious!
* it's error prone!
</div>

<div class="fragment" markdown="block">
__What can we do to make testing less tedious and error prone? &rarr;__
</div>
</section>

<section markdown="block">
##  Assertions for Testing

Let's get the computer to test it for us!  Assertions are a way to systematically check the state of our program.

* we can test _expected_ values against the _actual_ values by using an __assert__ statement
* the __assert__ statement will stop program execution if if a specified condition is __not True__
* for testing, that condition is _expected_ value == _actual_ value
</section>

<section markdown="block">
##  Assertions as "Sanity Checks"

* note that assertions are not limited to this type of testing
* they're usually used to check for conditions that _shouldn't_ happen 
* such as the return value of a function not being an expected type
* or the parameters of a function adhering to certain bounds
</section>

<section markdown="block">
##  Assert Syntax

<pre><code data-trim contenteditable>
assert &lt;some condition&gt;, "a string representing a test"
</code></pre>

1. the keyword __assert__
2. followed by any condition - an expression that returns True or False (usually expected == observed)
3. followed by a comma
4. followed by a string that represents the test 
</section>

<section markdown="block">
##  An Assertion Example

__Let's use assertions to test an incorrect implementation of our function - one that doesn't have spaces between the strings. &rarr;__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{% include classes/16/join_three_strings_with_asserts.py %}
</code></pre>

<pre><code data-trim contenteditable>
#  output shows line number and error...
Traceback (most recent call last):
  File "foo.py", line 4, in &lt;module&gt;
    assert "ha ha ha" == join_three_strings("ha", "ha", "ha"), "should have spaces"
AssertionError: joined string should have spaces
</code></pre>
</div>
</section>

<section markdown="block">
##  An Assertion Example That Actually Passes

__Let's fix the program... and see what happens. &rarr;__

<pre><code data-trim contenteditable>
{% include classes/16/join_three_strings_with_asserts_with_fix.py %}
#  results in no output
</code></pre>
</section>

<section markdown="block">
##  Another Assertion Example

__Let's use assertions to test an incorrect implementation of an absolute_value function &rarr;__
<pre><code data-trim contenteditable>
def absolute_value(x):
	if x >= 0:
		return x
	else:
		return -1
</code></pre>
<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
assert 1 == absolute_value(-1), "absolute value of negative # is positive"
assert 1 == absolute_value(1), "absolute value of positive # is same #"
assert 0 == absolute_value(0), "absolute value of 0 is 0"
</code></pre>

</div>
</section>

<section markdown="block">
##  Questions About Assertions
* why use assertions
	* to test specific portions of your program
	* to cut down on manual testing
	* they're almost like inline documentation for your functions
* why use assertions over if statements
	* you can actually _turn off_ assertions when you run your program
	* more concise than if statements
	* specifically meant for checking the internal state of your program
</section>

<section markdown="block">
##  Documentation

* what if someone else is reading your code, but your code is kind of _complex_?
* what if you _forgot_ what your code does!?
* you can write comments to give you a hint
* or you can write __docstrings__ that will show up in Python's documentation tools
</section>

<section markdown="block">
##  Docstrings

* we can document our functions using a __docstring__ 
* it's a string that immediately follows the head of a function definition
* it's in triple quotes
* it describes the function

<pre><code data-trim contenteditable>
def join_three_strings(a, b, c):
	"""returns a string composed of the values passed in separated by spaces""""
	return "%s %s %s" % (a, b, c)
</code></pre>

In later classes, we'll see where this string shows up, but for now just use it as inline documentation for your code.
</section>
