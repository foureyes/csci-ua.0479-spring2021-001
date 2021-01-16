---
layout: slides
title: Tuples 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Sequence Types

We know two sequence types.  __What are they?__

<div class="fragment" markdown="block">
* str
* list
</div>
</section>

<section markdown="block">
##  How Are Strings and Lists Similar?

Sequence types support a number of operations... 

* __Name some operations or functions that can be used on both strings and lists.__  
* __What does the operation do, and what does it return for each type?__

</section>

<section markdown="block">
##  Sequence Operations and Functions

* __+__ concatenation - adds all of the elements from one sequence to another; returns a new sequence 
* __*__ multiplication - repeats a sequence for the specified number of times; returns a new sequence
* __[i]__ indexing - retrieves the element at the specified index; returns the value
* __[m:n]__ slicing - retrieves a subsequence; returns a new sequence
* __len()__ length - returns the length of the sequence
* __for... in__ iteration - traverses over every element of sequence
* __in/not in__ membership - tests if values is in sequence
</section>

<section markdown="block">
##  But Strings and Lists Are Different!

How are strings and lists different?

* a string is an ordered sequence of characters... 
* a list is an ordered sequence of values (any values)... 

__But there's also another big difference.__

<div class="fragment" markdown="block">
* strings are immutable
* lists are mutable
</div>
</section>

<section markdown="block">
##  A Third Sequence Type

Surely you must be thinking: _I really wish that my list was not mutable_

(well... probably not... but...)

<div class="img-container" markdown="block">![Shirley](../../resources/img/surely.jpg)
</div>

</section>

<section markdown="block">
##  Tuples

A __tuple__ is an immutable grouping of data.  Think of it as an immutable list.  

* just like a list, it can hold heterogeneous values
* it can hold strs, lists, ints, and even other tuples
* however, it can't be changed!
	* you can't add items (no extend or append)
	* you can't remove items (no remove; del doesn't work)
	* you can't change items (assignment doesn't work)
</section>

<section markdown="block">
##  Tuple Syntax

A tuple is really just a group of comma separated values.  A tuple literal is _just_ values and commas.  Really! (btw, [chugs exist, and are _a thing_](http://www.dogbreedinfo.com/chug.htm))

<pre><code data-trim contenteditable>
&gt;&gt;&gt; dogs = "chihuahua", "pug", "chug"
&gt;&gt;&gt; print(dogs)
('chihuahua', 'pug', 'chug')
</code></pre>



However... it's common to put parentheses around a tuple (in fact, when you print a tuple, parentheses are always placed around it).(apparently [Pelicans is now the name of a professional basketball team](http://www.grantland.com/blog/the-triangle/post/_/id/44376/17-reasons-you-should-support-the-change-to-new-orleans-pelicans)!)

<pre><code data-trim contenteditable>
&gt;&gt;&gt; birds = ("pelican", "owl", "pigeon")
&gt;&gt;&gt; print(birds)
('pelican', 'owl', 'chug')
</code></pre>
</section>


<section markdown="block">
##  Seem Familiar?

We've actually seen and used tuples in the past!  __Does anyone remember where we've seen tuples before?__

<div class="fragment" markdown="block">

<div>
String formatting with the % operator:

<pre><code data-trim contenteditable>
"I've %s this %s before!" % ("seen", "this")
</code></pre>

Multiple assignment

<pre><code data-trim contenteditable>
a, b, c = 1, 2, 3
</code></pre>

</div>

</div>
</section>

<section markdown="block">
##  What About Function Parameters?

Aren't function parameters comma separated?

* Function parameters (both in definitions and when calling functions) are not tuples, even though they're comma separated 
* In order to pass a tuple literal to a function, you have to use parentheses to delimit the tuple to prevent ambiguity

<pre><code data-trim contenteditable>
&gt;&gt;&gt; print(1, 2)
1 2
&gt;&gt;&gt; print((1, 2))
(1, 2)
</code></pre>

</section>

<section markdown="block">
##  Tuple Operations and Built-In Functions

* a tuple is a sequence type, so it has some operations that are similar to strings and lists... 
* but there are some operations that it doesn't support

</section>

<section markdown="block">
##  Tuple Operations and Built-In Functions Continued

__Let's try the following:__

* Supported Operations:
	* multiplication and addition
	* indexing and slicing
	* len
	* for ... in
	* in / not in
* Unsupported Operations:(because it is immutable, these methods will not work) append, extend, remove, etc.
</section>

<section markdown="block">
##  Tuple Operations Examples

Some operations:

<pre><code data-trim contenteditable>
a = (1,2,3)
print(a + (4, 5, 6))
print(a[0])
print(a[:2])
print(len(a))
print(5 in a)
</code></pre>


<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
(1, 2, 3, 4, 5, 6)
1
(1, 2) # note that slicing a tuple returns a tuple!
3
False
</code></pre>
</div>
</section>

<section markdown="block">
##  Iteration

Just like iterating over strings or lists.

<pre><code data-trim contenteditable>
for value in (1, 2, 3):
	print(value)
</code></pre>
</section>

<section markdown="block">
##  Tuple Unpacking / Multiple Assignment

We talked briefly talked about multiple assignment.  This is generally done with tuples, and when it's done with tuples, it's called  __tuple unpacking__. 

* a tuple of variables on the left of an assignment operator
* a tuple of values on the right of an operator 
* both have the same number of elements 
* each value is assigned to each variable in the order that the elements are in

<pre><code data-trim contenteditable>
&gt;&gt;&gt; first_name, last_name = ("Hiro", "Protagonist")
&gt;&gt;&gt; print(first_name)
Hiro
&gt;&gt;&gt; print(last_name)
Protagonist
</code></pre>
</section>

<section markdown="block">
##  Tuple Unpacking Examples

__What does this code output?__

<pre><code data-trim contenteditable>
values = (1, 2, 3)
a, b, c = values
print(a)
print(b)

c, a, b = values
print(a)
print(b)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
1
2
2
3
</code></pre>
</div>
</section>

<section markdown="block">
##  More Info About Multiple Assignment

Tuple unpacking is the most common way of performing multiple assignment... but the assignment operator is actually super flexible:

[More than you ever wanted to know about the assignment operator](http://docs.python.org/3.2/reference/simple_stmts.html#assignment-statements)
</section>

<section markdown="block">
##  List of Tuples

A tuple within a list is retrieved as a single object, as with every other element in a list, when using our regular _for loop_variable in some_list_ syntax: 

<pre><code data-trim contenteditable>
characters = [("Hiro", "Protagonist"), ("Yours", "Truly")]
for character in characters:
	print(character)
</code></pre>

You get each actual tuple, so this prints out:

<pre><code data-trim contenteditable>
('Hiro', 'Protagonist')
('Yours', 'Truly')
</code></pre>
</section>

<section markdown="block">
##  List of Tuples Continued

Unpacking works in for loops as well!  Imagine that each element is retrieved form the outer list.  Each element is a tuple which can be unpacked into multiple loop variables.

<pre><code data-trim contenteditable>
characters = (("Hiro", "Protagonist"), ("Yours", "Truly"))
for first, last in characters:
	print("first name is " + first)
	print("last name is " + last)
</code></pre>
</section>

<section markdown="block">
##  List of Tuples Example 

<pre><code data-trim contenteditable>
pairs_of_numbers = [(1, 2), (2, 3)]
for a, b in pairs_of_numbers:
	print(a + b)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
3
5
</code></pre>
</div>
</section>

<section markdown="block">
##  Returning Tuples

Tuples and tuple unpacking can provide a method of returning multiple values from a function. __What do you think this prints out?__

<pre><code data-trim contenteditable>
def calculate_3d_point():
	result = (2, 4, 0)
	return result

x, y, z = calculate_3d_point()
print("the z coordinate is %s" % (z))
print("the x coordinate is %s" % (2))
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
the z coordinate is 0
the x coordinate is 2
</code></pre>
</div>
</section>

<section markdown="block">
##  Tuples Exercise 

* __What are two ways of programmatically drawing a square in turtle?__
* __What are some ways of representing a series of four x, y coordinates?__

<div class="fragment" markdown="block">
* there are a couple of ways to draw a square with turtle:
	* for loop and a combination of either left or right and forward or back
	* goto
* as literals, as separate variables... or as a tuple of tuples!
</div>
</section>

<section markdown="block">
##  Tuples Exercise 

1. create a tuple of tuple literals that represent x, y coordinates of corners of a square
2. assume that the bottom left corner is at (0, 0) and the upper right is (0, 50)
3. assign that tuple to a variable
4. use a for loop and tuple unpacking to get each x, y value
5. within the for loop, use goto with your loop variables to draw the square

</section>
<section markdown="block">
##  Template

<pre><code data-trim contenteditable>
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
#  your code here!
wn.mainloop()
</code></pre>

</section>




<section markdown="block">
##  Tuples Solution 

<pre><code data-trim contenteditable>
{% include classes/24/turtle_tuple_points.py %}
</code></pre>
</section>

<section markdown="block">

##  That's cool and all... but _why would an immutable list ever be useful?_


</section>

<section markdown="block">
##  When To Use Tuples Continued

* some Python constructs use tuples (interpolation, multiple assignment)
* tuples are _write protected_
	* prevent an object from being changed
	* example: constants - values that never change... like origin = (0, 0)
* tuples are _faster_ than lists for some operations
* returning multiple values from a function
* semantics  
	* treat related data as a whole
	* example: points in a 2-dimensional plane
</section>
