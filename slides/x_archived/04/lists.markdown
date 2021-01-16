---
layout: slides
title: Lists, List Operators and Built-in Functions 
---
<section markdown="block" class="title-slide">
#  Lists, Lists Operators and Built-in Functions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  Types

What's a __type__?  __What are the types that we've seen so far? &rarr;__

<div class="fragment" markdown="block">
A __type__ is a set of values.  It's a way of classifying them.  __Some examples of types that we've learned include... &rarr;__

* strings (str)
* integers (int)
* floating point numbers (float)
* complex numbers (complex)
* booleans (bool)
</div>
</section>

<section markdown="block">
##  Types of Types

Types can actually be classified as well.  Like types of types!  __How are the following types related, and what do they have in common?__  

* int
* float
* complex

<div class="fragment" markdown="block">
* all of these types are __numeric__
* they support similar operations...
* for example addition, multiplication, subtraction, division

</div>
</section>


<section markdown="block">

##  Sequences

We've seen __numeric__ types, like int, float and complex.  Another kind/classification of type is a __sequence__. A __sequence__:

* consists of an ordered collection of elements
* with each element identified by an index

Sequences support operations like:

* __indexing__ to retrieve an element
* __slicing__ to retrieve a subset of elements
* __concatenation__ and __multiplication__

</section>

{% comment %}
<section markdown="block">
##  We've Seen This Before

__What data type have we seen that supports these operations?__ &rarr; 

<div class="fragment" markdown="block">
A __string__ is an ordered sequence of characters.  It is a __sequence__ type.  It supports:

<pre><code data-trim contenteditable>
"blubbins?"[0] #index, first element -> "b" 
"blubbins?"[-1] #index, last element -> "?"
"blubbins?"[1:4] #slices -> "lub"
"blubbins?"[4:] #slices -> "bins?"
"what the " + "blubbins?" # concatenates -> "what the blubbins?"
"blubbins?" * 2 # repeats -> "blubbins?blubbins?"
</code></pre>
</div>
</section>
{% endcomment %}

<section markdown="block">
##  Lists

A __list__ is a sequence type.  

* instead of characters, it's an ordered collection of __values__
* _any_ values!
* the following is a list that consists of  ints and strings

<pre><code data-trim contenteditable>
#  a list of ints
stuff = [1, "one", 2, "two"]
</code></pre>
</section>

<section markdown="block">
##  List Literals

Constructing a list using a list literal looks like this:
<pre><code data-trim contenteditable>
["some", "stuff", "between", "brackets"]
</code></pre>

* delimited by brackets... [1, 2, 3]
* each value is separated by a comma
* a list with no elements is an __empty list__ 
* an empty list is []
* again, mixed types are allowed (even other lists) - ['pie', 3, 3.14, ['apple', ['cherry']]]
</section>

<section markdown="block">
##  Printing Lists

You can pass lists directly to the built-in print function.  It will output the list as if it were a string literal: 

<pre><code data-trim contenteditable>
&gt;&gt;&gt; a = [2, 3, 5, 7]
&gt;&gt;&gt; print(a)
[2, 3, 5, 7]
</code></pre>

You can also use str() or string formatting to create a string representation of a list:

<pre><code data-trim contenteditable>
&gt;&gt;&gt; a = [2, 3, 5, 7]
&gt;&gt;&gt; print("Some numbers in a list: %s" % a)
Some numbers in a list: [2, 3, 5, 7]
</code></pre>
</section>

<section markdown="block">
##  Built-in List Operators and Functions

Because a __list__ is a __sequence type__, it has these built-in operators and functions:

* indexing operators
* iteration
* slicing
* comparison operators
* multiplication/addition
* len
</section>


<section markdown="block">
##  Indexing Operations

__What will the following code output? &rarr;__

<pre><code data-trim contenteditable>
import math
land_of_ooo = ["jake", "finn", "pb"]
a = -1
print(land_of_ooo[0])
print(land_of_ooo[2])
print(land_of_ooo[a])
print(land_of_ooo[int(math.sqrt(1))])
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
jake
pb
pb
finn
</code></pre>
</div>

</section>


<section markdown="block">
##  Indexing Operations Continued

__What will the following code output? &rarr;__

<pre><code data-trim contenteditable>
import math
land_of_ooo = ["jake", "finn", "pb"]
a = -1
print(land_of_ooo[3])
print(land_of_ooo[1.0])
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
IndexError: list index out of range

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: list indices must be integers, not float
</code></pre>
</div>

</section>

<section markdown="block">
##  Indexing Operations Continued Some More!

Using the list below, __How would you retrieve "homer"... once using a positive index, and another time using a negative index? &rarr;__

<pre><code data-trim contenteditable>
simpsons = ["marge", "homer", "lisa"]
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
simpsons[1]
simpsons[-2]
</code></pre>
</div>
</section>

<section markdown="block">
##  Indexing Operations Summary

* just like characters in a string, elements in a list can be accessed by their index (place)
* indexes start at 0 
* use the value (a variable, a list literial, etc) followed by the square brackets
* ... with the index enclosed: [1, 2, 3][0] &rarr; 1
* negative indexes start at the end of the list: [1, 2, 3][-1] &rarr; 3
</section>

<section markdown="block">
##  Mutability

Unlike strings, however, lists are __mutable__.  That means that you can reassign a value at an index!  __What will the following code print out? &rarr;__

<pre><code data-trim contenteditable>
&gt;&gt;&gt; a = [3, 4, 5]
&gt;&gt;&gt; a[0] = "surprise"
&gt;&gt;&gt; print(a)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
['surprise', 4, 5]
</code></pre>
</div>
</section>

<section markdown="block">
##  Indexing Into a List of Lists

Lists can be composed of any objects, including __other lists__:

<pre><code data-trim contenteditable>
stuff = [['foo', 'bar', 'baz'], [1, 2, 3], [0.25, 0.5, 0.75]]
</code></pre>

* you can index into the outside list as usual... 
	* stuff[0] gives back ['foo', 'bar', 'baz'] &rarr;
* to get into an element in the inner list, you can index again...
	* stuff[0][1] gives back 'bar'! &rarr;
* you can even change an element in the inner list...
	* stuff[0][1] = "I'm in your list" &rarr;
</section>

<section markdown="block">
##  List of Lists Exercises

Using the same list:

<pre><code data-trim contenteditable>
stuff = [['foo', 'bar', 'baz'], [1, 2, 3], [0.25, 0.5, 0.75]]
</code></pre>

* what indexing syntax would I use to get the number 3?
* what line of code would I use to change 0.25 to 0? 

<div class="fragment">
<pre><code data-trim contenteditable>
stuff[1][2]
stuff[2][0] = 0
</code></pre>
</div>
</section>

<section markdown="block">
##  Iterating Over a List

Just like iterating over a sequence of characters...

* you can __use a for loop to iterate over a sequence of values in a list__
* your __loop variable__ contains the __value of a list element__
* that changes to the next element after each iteration
* loop continues until every element of list is exhausted
* if list is empty, there will be no iterations
</section>

<section markdown="block">
##  Iterating Over a List Example

__What will the following for loop print out? &rarr;__

<pre><code data-trim contenteditable>
some_boolean_values = [True, True, False]
for b in some_boolean_values:
	print(b)
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
##  Iterating Over a List of Lists

How do you think we can print out every element in a line of its own in this list of lists?

<pre><code data-trim contenteditable>
stuff = [['foo', 'bar', 'baz'], [1, 2, 3], [0.25, 0.5, 0.75]]
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
"""NESTED LOOPS!"""
stuff = [['foo', 'bar', 'baz'], [1, 2, 3], [0.25, 0.5, 0.75]]
for inner_list in stuff:
	for element in inner_list:
		print(element)
</code></pre>
</div>
</section>

<section markdown="block">
##  Slicing

Slicing also works on lists.  __What will the following code output? &rarr;__

<pre><code data-trim contenteditable>
colors = ["red", "green", "blue", "taupe"]
print(colors[0:2])
print(colors[2:])
print(colors[:3])
print(colors[0:100])
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
['red', 'green']
</code></pre>
<pre><code data-trim contenteditable>
['blue', 'taupe']
</code></pre>
<pre><code data-trim contenteditable>
['red', 'green', 'blue']
</code></pre>
<pre><code data-trim contenteditable>
['red', 'green', 'blue', 'taupe']
</code></pre>
</div>
</section>

<section markdown="block">
##  Slicing Summary

Again... like slicing strings.

* use square brackets
* ...with start index and end index separated by a colon: [2, 3, 5, 7][1:3] &rarr; [3, 5]
* start and end can be omitted: [2, 3, 5, 7][:2] &rarr; [2, 3]
</section>


<section markdown="block">
##  Equality Operators

* lists are compared lexicographically using comparison of corresponding elements 
* to be equal, each element must compare equal and the two sequences must be of the __same type__ and have the __same length__.

__Equal or not equal?__ &rarr;

<pre><code data-trim contenteditable>
print([1, 2, 3] == [1, 2, 3])
print(['a', 'b', 'c'] == [1, 2, 3])
print(['a', 'b', 'c'] != [1, 2, 3])
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
True
False
True
</code></pre>
</div>
</section>

<section markdown="block">
##  Greater Than, Less Than

* sequences are ordered the same as their __first differing elements__. 
* comparing [1,2,'x'] and [1,2,'y'] is essentially just comparing 'x' and 'y'). 
	* example: [1, 2, 3] > [1, 2, 1] &rarr; True
* if the corresponding element does not exist, the shorter sequence is ordered first 
	* example: [1,2] < [1,2,3] &rarr; True

<pre><code data-trim contenteditable>
""" What boolean values do these statements return?"""
['a', 'b', 1, 2] > ['b', 'b', 1, 2]
[5, 2] < [5, 2, 1]
['x', 'y', 'z'] < ['x', 'a', 'z']
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
False
True
False
</code></pre>
</div>
</section>

<section markdown="block">
##  Addition and Multiplication

Multiplication and addition of lists are similar to the same operations on strings.  __What will the following code output? &rarr;__

<pre><code data-trim contenteditable>
toppings = ["mushrooms", "peppers", "onions"]
numbers = [2, 3, 5, 7]
print(toppings + numbers)
print(toppings * 2)
print(numbers * 2)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
["mushrooms", "peppers", "onions", 2, 3, 5, 7]
["mushrooms", "peppers", "onions", "mushrooms", "peppers", "onions"]
[2, 3, 5, 7, 2, 3, 5, 7]
</code></pre>
</div>
</section>

<section markdown="block">
##  Addition and Multiplication Summary

* list concatenation 
	* __+__
	* adds the elements of one list to another list
	* [1, 2] + [3, 4] &rarr; [1, 2, 3, 4]
* list multiplication
	* __*__
	* repeats a list the given number of times
	* [1, 2] * 3 &rarr; [1, 2, 1, 2, 1, 2]
</section>

<section markdown="block">
##  len()

You can still use the built-in function, len, on lists. __What do you think the following code will output? &rarr;__

<pre><code data-trim contenteditable>
a = ["foo", "bar", "baz"]
b = []
c = ["foo", "bar", "baz", [1, 2, 3]]
print(len(a))
print(len(b))
print(len(c))
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
3
0
4
</code></pre>
</div>
</section>


<section markdown="block">
##  Looking for something?

Testing for membership within a list is similar to testing for a character in a string.  Use the __in__ operator.  It returns True if the operand on the left is an element in the list on right.  __What does the following code print out? &rarr;__

<pre><code data-trim contenteditable>
print('c' in ['a','b', 'c'])
print('c' not in ['a', 'b', 'c'])

breakfast = ["oatmeal", "tofu scramble", "ramen"]
if "ramen" in breakfast:
	print("ramen for breakfast")
else:
	print("wise decision")
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
True
False
ramen for breakfast
</code></pre>
</div>
</section>

<section markdown="block">
##  Deleting List Items

You can delete list items using __del__ statement:  

* the __del__ statement is immediately followed by an indexed list or a list slice
* the value or values of the indexed list or list slice are removed from the original list

__What does the following code print out? &rarr;__

<pre><code data-trim contenteditable>
vegetables = ["broccoli", "cauliflower", "brownie sundae", "carrot"]
del vegetables[2]
print(vegetables)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
['broccoli', 'cauliflower', 'carrot']
</code></pre>
</div>
</section>

<section markdown="block">
##  Some Exercises

* using this list: numbers = [1, 2, 3, 4, 11, 12, 13, 14]
	* Part 1: __print__ out number with an exclamation point (no need to define a function)
	* Part 2: only do this for every other element starting with the 2nd element:
	* 2! 
	* 4! 
	* 12! 
	* 14!
* write a function that takes a list and returns the first half of the elements (it's ok to round down)
	* half_a_list([1, 2, 3, 4, 11, 12, 13, 14])
	* &rarr; [1, 2, 3, 4]
</section>

<section markdown="block">
##  Potential Solutions

<pre><code data-trim contenteditable>
numbers = [1, 2, 3, 4, 11, 12, 13, 14]
print_out_number = False
for n in numbers:
	if print_out_number:
		print('%s!' % (n))
	print_out_number = not print_out_number
</code></pre>

<pre><code data-trim contenteditable>
import math
def half_a_list(items):
	half_index = math.floor(len(items) / 2)
	return items[:half_index]
</code></pre>
</section>

<!--
<section markdown="block">
##  [List Methods](list_methods.html)
</section>
-->

