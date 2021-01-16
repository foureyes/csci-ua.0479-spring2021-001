---
layout: slides
title: Tuples 
---
<section markdown="block" class="title-slide">
#  Tuples Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Sequence Types

We know two sequence types.  __What are they?__

<div class="incremental" markdown="block">
* str
* list
</div>
</section>

<section markdown="block">
###  How Are Strings and Lists Similar?

Sequence types support a number of operations... 

* __Name some operations or functions that can be used on both strings and lists.__  
* __What does the operation do, and what does it return for each type?__

</section>

<section markdown="block">
###  Sequence Operations and Functions

* __+__ concatenation - adds all of the elements from one sequence to another; returns a new sequence 
* __*__ multiplication - repeats a sequence for the specified number of times; returns a new sequence
* __[i]__ indexing - retrieves the element at the specified index; returns the value
* __[m:n]__ slicing - retrieves a subsequence; returns a new sequence
* __len()__ length - returns the length of the sequence
* __for... in__ iteration - traverses over every element of sequence
* __in/not in__ membership - tests if values is in sequence
</section>

<section markdown="block">
###  Strings vs Lists

__How are strings and lists different?__ &rarr;


<div class="incremental" markdown="block">
* syntax ([]'s and ""'s)
* a string is an ordered sequence of characters... 
* a list is an ordered sequence of values (any values)... 
* __strings are immutable__
* __lists are mutable__
</div>
</section>

<section markdown="block">
###  A Third Sequence Type

Last week, we learned about a third sequence type.  __What is it called... what is it, and how is different from lists and strings?__ &rarr;

<div class="incremental" markdown="block">
* a __tuple__ is another sequence type
* __it's basically an immutable list__
* it can hold strs, lists, ints, and even other tuples
* because it is immutable:
	* you can't add items (no extend or append)
	* you can't remove items (no remove; del doesn't work)
	* you can't change items (assignment doesn't work)
</div>

</section>

<section markdown="block">
###  Tuple Syntax

__Write out the code that creates a tuple with three elements: "python", "java",  and "php"__ &rarr;

<div class="incremental" markdown="block">
A tuple is just a group of comma separated values.  A tuple literal is _just_ values and commas. 

{% highlight python %}
t = "python", "java", "php"
{% endhighlight %}

It's common to put parentheses around a tuple (printing a tuple always displays the parentheses)

{% highlight python %}
t = ("python", "java", "php")
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  We've Used Tuples...

__Name two places where we've seen tuples before__ &rarr;

<div class="incremental" markdown="block">

String formatting

{% highlight python %}
"I've %s this %s before!" % ("seen", "this")
{% endhighlight %}

Multiple assignment

{% highlight python %}
a, b, c = 1, 2, 3
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Not a Tuple

__What's a case where comma separated values ARE NOT a tuple?__ &rarr;

<div class="incremental" markdown="block">
* __Function parameters (both in definitions and when calling functions) are not tuples__, even though they're comma separated 
* In order to pass a tuple literal to a function, you have to use parentheses to delimit the tuple to prevent ambiguity

{% highlight pycon %}
>>> print(1, 2)
1 2
>>> print((1, 2))
(1, 2)
{% endhighlight %}
</div>

</section>


<section markdown="block">
###  Tuple Operations and Built-In Functions 

__Based on what we know about other sequence types, guess what operations, function and/or methods are supported by tuples?  How about ones that aren't?__&rarr;

<div class="incremental" markdown="block">
* Supported Operations:
	* multiplication and addition
	* indexing and slicing
	* len
	* for ... in
	* in / not in
* Unsupported Operations:(because it is immutable, these methods will not work) assignment, append, extend, remove, etc.
</div>
</section>

<section markdown="block">
###  Tuple Operations Examples

Some operations:

{% highlight python %}
a = (1,2,3)
print(a + (4, 5, 6))
print(a[0])
print(a[:2])
print(len(a))
print(5 in a)
{% endhighlight %}


<div class="incremental" markdown="block">
{% highlight python %}
(1, 2, 3, 4, 5, 6)
1
(1, 2) # note that slicing a tuple returns a tuple!
3
False
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Iteration

Just like iterating over strings or lists.

{% highlight python %}
for value in (1, 2, 3):
	print(value)
{% endhighlight %}
</section>

<section markdown="block">
###  Tuple Unpacking / Multiple Assignment

Multiple assignment is achieved by __tuple unpacking__. 

* a tuple of variables on the left of an assignment operator
* a tuple of values on the right of an operator 
* both have the same number of elements 
* each value is assigned to each variable in the order that the elements are in

{% highlight python %}
c = ("UA2", "Intro to Programming")
number, name = c
print(number, name)
{% endhighlight %}
</section>

<section markdown="block">
###  Tuple Unpacking 

__What does this code output?__

{% highlight python %}
values = ("python", "java", "php")
a, b, c = values
print(a)
print(b)

c, a, b = values
print(a)
print(b)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
python
java
java
php
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  List of Tuples

A tuple within a list is retrieved as a single object, as with every other element in a list, when using our regular _for loop_variable in some_list_ syntax: 

{% highlight python %}
characters = [("Mabel", "Pines"), ("Dipper", "Pines")]
for character in characters:
	print(character)
{% endhighlight %}

You get each actual tuple, so this prints out:
{% highlight python %}
('Mabel', 'Pines')
('Dipper', 'Pines')
{% endhighlight %}
</section>

<section markdown="block">
###  List of Tuples Continued

Unpacking works in for loops as well!  

* each element is retrieved from the outer list
* each element is a tuple which can be unpacked into multiple loop variables

{% highlight python %}
characters = [("Mabel", "Pines"), ("Dipper", "Pines")]
for first, last in characters:
	print("first name is " + first)
	print("last name is " + last)
{% endhighlight %}
</section>

<section markdown="block">
###  List of Tuples Example 

__What does the following code print out?__ &rarr;

{% highlight python %}
pairs_of_numbers = [("hello", 2), ("hi", 1)]
for greeting, n in pairs_of_numbers:
	print(greeting * n)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
hellohello
hi
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Returning Tuples

Tuple unpacking can provide a method of returning multiple values from a function. __What does the follwing code output?__

{% highlight python %}
def plus_or_minus(num, interval):
	start = num - interval
	end = num + interval
	result = (start, num, end)
	return result

low, original, high = plus_or_minus(0, 5)
print(low)
print(original)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
-5
0
{% endhighlight %}
</div>
</section>


<section markdown="block">
###  Turtle / Tuples Exercise 

1. create a list of tuples that represent x, y coordinates of corners of a square
2. assume that the bottom left corner is at (0, 0), the upper left is (0, 50), upper right (50, 50), lower right (50, 0)
3. use a for loop and tuple unpacking to get each x, y value
4. within the for loop, use a turtle object and goto with your loop variables to draw a square

{% highlight python %}
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
#  your code here!
wn.mainloop()
{% endhighlight %}
</section>

<section markdown="block">
###  Tuples Solution 

{% highlight python %}
{% include classes/24/turtle_tuple_points.py %}
{% endhighlight %}
</section>

<section markdown="block">
###  When To Use Tuples

__In what situations would a tuple be useful?__ &rarr;

<div class="incremental" markdown="block">
* some Python constructs use tuples (string formatting, multiple assignment)
* tuples are _write protected_
	* prevent an object from being changed
	* example: constants - values that never change... like origin = (0, 0)
* tuples are _faster_ than lists for some operations
* returning multiple values from a function
* semantics  
	* treat related data as a whole
	* example: points in a 2-dimensional plane
</div>
</section>
