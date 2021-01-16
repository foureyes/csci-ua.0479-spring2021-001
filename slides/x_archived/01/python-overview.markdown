---
layout: slides
title: "Python Overview"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
# Objects and Names


</section>

<section markdown="block">
## Objects

A [hand-wavey](https://en.wiktionary.org/wiki/handwavy) definition:

* __data__ ... 
* aaaand some __actions__ that can be performed with that data 
* (think member variables and methods in Java)

Or simply...

* a _thing_ that a name can refer to
* (um? is that even really an answer?)
* (we'll see why in a bit...)

Or the __official definition__ from Python Docs

* "Objects are Python's abstraction for data"
* __all data in Python is represented by objects__ (_everything's an object, even code!_)
</section>


<section markdown="block">
## Every Object

1. __has an id__ (that never changes)
    * think of the id as the location in memory
    * built in <code>id</code> function... returns id of object passed in
    * <code>is</code> operator ... determines if two objects are the same
2. __has a value...__ (the value may change, though!)
    * objects with values that can change are called __mutable__ (__immutable__ if value can't be changed)
    * an object's type determines mutability
    * mutable objects contained in an immutable object can be changed(!?)
3. __has a type...__ (cannot be changed)
    * determines the operations and actions that you can perform with object
    * (by actions... think _methods_, or functions that can be called on object with dot)
</section>

<section markdown="block">
## Object ids

__Using the <code>id</code> function__

<pre><code data-trim contenteditable>
# 5 is always same object
>>> id(5)
4322167232
>>> id(5)
4322167232
</code></pre>



</section>

<section markdown="block">
## Is vs ==

<pre><code data-trim contenteditable>
# obviously, based on previous slide
>>> 5 is 5
True
</code></pre>
<pre><code data-trim contenteditable>
# slicing creates an entirely new list!
>>> a = [1, 2, 3]
>>> b = a[:]
>>> id(a)
4371626696
>>> id(b)
4371644040
</code></pre>

<pre><code data-trim contenteditable>
# values are same, but id are not...
>>> a == b
True
>>> a is b
False
</code></pre>

</section>

<section markdown="block">
## Literals

A __literal__ is a representation of a specific value in code.

* __5__ is a literal.
* "hello" is a literal.
* x = 7... x is not a literal, but 7 is

The type of a literal value can be distinguished by the syntax used to create it

* quotes mean the value is a <code>str</code>
* a decimal point and numeric values means that the value is a <code>float</code>
</section>

<section markdown="block">
## Names / Variables

If you want to reference an object later (_remember an object_), __you'll have to give it a name__.

* create a variable name
* and assign it to an object / value / literal / expression

<pre><code data-trim contenteditable>
x = 5
words = ["foo", "bar", baz"]
y = 2 + 3
</code></pre>
</section>


<section markdown="block">
## Aliasing

__What happens here?__ &rarr;

<pre><code data-trim contenteditable>
words = ["foo", "bar", "baz"]
words_again = words
words_again.append("qux")
print(words)
</code></pre>

<pre class="fragment"><code class="python" data-trim contenteditable>
# both words and words_again refer to the same object
["foo", "bar", "baz"]
</code></pre>

{:.fragment}
See the example in <a href="http://pythontutor.com/visualize.html#code=words+%3D+%5B%22foo%22,+%22bar%22,+%22baz%22%5D%0Awords_again+%3D+words%0Awords_again.append(%22qux%22%29%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=3">python tutor</a>

</section>


<section markdown="block">
## Name Space, Object Space


<pre class="python"><code class="python" data-trim contenteditable>
words = ["foo", "bar", "baz"]
words_again = words
words_again.append("qux")
print(words)
</code></pre>


<pre><code data-trim contenteditable>
Names         |     Objects
--------------+-------------
words   ______|__\ ["foo", "bar", "baz"]
              |  /   ^ 
              |     /|\
words_again __|______| 
              |
print  _______|__\ <class 'builtin_function_or_method'>
              |  /
</code></pre>
</section>

<section markdown="block">
## Multiple Assignment

__Variables on the left will bind to variables on the right (in the order that they are written)__ &rarr;

<pre><code class="livecodeserver" data-trim contenteditable>
>>> a, b, c = "foo", "bar", "baz"
>>> print(a)
foo
>>> print(b)
bar
</code></pre>

</section>


<section markdown="block">
## types

A __type__ is a classification of values. __A type determines__ &rarr;

* what you can and can't do w/ an object
* an object's mutability and immutability
* the words  __type__ and __class__ are sometimes used interchangebly
* the <code>type</code> function can be used to determine the type of an object
    * it always returns an object of type type! (!?!?)
</section>
<section markdown="block">
## Determining Type

__Using the built-in type function__ &rarr;

Some obvious ones...

<pre><code data-trim contenteditable>
>>> type(5)
<class 'int'>
>>> type(False)
<class 'bool'>
>>> type(5.0)
<class 'float'>
</code></pre>

Maybe a little tricky...

<pre><code data-trim contenteditable>
>>> type("5")
<class 'str'>
>>> type(print)
<class 'builtin_function_or_method'>
>>> type(type(False))
<class 'type'>
</code></pre>


</section>

<section markdown="block">
## Types of Types

* numeric types
* sequence types

</section>

<section markdown="block">
##  numeric types

The following types are __numeric__

* int
* complex
* float

Some examples of operations that they share are:

* +, -, \*, %, \*\*, //, /
* comparison operators
</section>

<section markdown="block">
## sequence types

A sequence types is type composed of an __ordered series of values__, with each element's position represented by an integer (starting from 0).

* __str__ - an immutable, ordered sequence of characters (other strings), delimited by quotes: <code>"a string</code>
* __list__ - a mutable, ordered sequence of any value, delimited by square brackets and comma separated values <code>[1, 2, 3']</code>
* __tuple__ - essentially... an immutable list, just comma separated values: <code>1, 2, 3</code>

Common operations:

\+ (concatenation), \* (repetition), [] (indexing), [:] slicing, in
</section>

<section markdown="block">
## Tuples?

A __tuple__ is an immutable grouping of data.  Think of it as an immutable list.  

* just like a list, it can hold heterogeneous values
* it can hold strs, lists, ints, and even other tuples
* however, it can't be changed!
	* you can't add items (no extend or append)
	* you can't remove items (no remove; del doesn't work)
	* you can't change items (assignment doesn't work)
</section>

<section markdown="block">
## Tuple Syntax

A tuple is really just a group of comma separated values.  A tuple literal is _just_ values and commas.  Really! (btw, [chugs exist, and are _a thing_](http://www.dogbreedinfo.com/chug.htm))

<pre><code data-trim contenteditable>
>>> dogs = "chihuahua", "pug", "chug"
>>> print(dogs)
('chihuahua', 'pug', 'chug')
</code></pre>



However... it's common to put parentheses around a tuple (in fact, when you print a tuple, parentheses are always placed around it).(apparently [Pelicans is now the name of a professional basketball team](http://www.grantland.com/blog/the-triangle/post/_/id/44376/17-reasons-you-should-support-the-change-to-new-orleans-pelicans)!)

<pre><code data-trim contenteditable>
>>> birds = ("pelican", "owl", "pigeon")
>>> print(birds)
('pelican', 'owl', 'chug')
</code></pre>
</section>


<section markdown="block">
## Seem Familiar?

We've actually seen and used tuples in the past!  __Does anyone remember where we've seen tuples before?__ &rarr;

String formatting with the % operator:

<pre class="fragment"><code data-trim contenteditable>
# string formatting with %
"I've %s this %s before!" % ("seen", "this")
</code></pre>


<pre class="fragment"><code data-trim contenteditable>
# Multiple assignment
a, b, c = 1, 2, 3
</code></pre>

</section>

<section markdown="block">
## An Aside on String Formatting

__The <code>%</code> operator can be used to format strings.__ &rarr;

* it takes a string with placeholders on the left (the placeholders used below is <code>%s</code>)
* ...and a tuple of values on the right

String formatting with <code>%</code>:

<pre><code data-trim contenteditable>
>>> "%s and other stuff %s" % ("joe", "i don't know")
"joe and other stuff i don't know"
>>> "%s and other stuff %s" % (42, ["help","what?"])
"42 and other stuff ['help', 'what?']"
</code></pre>

Different types work above... but not with concatenation!

<pre><code data-trim contenteditable>
>>> 42 + "and other stuff"
...
TypeError: unsupported operand type(s) for +: 'int' and 'str' </code></pre>
</section>

<section markdown="block">
## What About Function Parameters?

Um... if tuples are just comma separated values, what's going on with function arguments and parameters?  __Aren't function parameters comma separated too?__ &rarr;

* Function parameters (both in definitions and when calling functions) are not tuples, even though they're comma separated 
* In order to pass a tuple literal to a function, you have to use parentheses to delimit the tuple to prevent ambiguity

<pre><code data-trim contenteditable>
>>> print(1, 2)
1 2
>>> print((1, 2))
(1, 2)
</code></pre>

</section>

<section markdown="block">
## Tuple Operations and Built-In Functions

* a __tuple__ is a __sequence type__, so it has some operations that are similar to strings and lists... 
* but there are some operations that it doesn't support
    * for example, no assignment!
    * no methods that add elements!

</section>

<section markdown="block">
## Tuple Operations and Built-In Functions Continued

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
## Tuple Operations Examples

Some operations:

<pre><code data-trim contenteditable>
a = (1,2,3)
print(a + (4, 5, 6))
print(a[0])
print(a[:2])
print(len(a))
print(5 in a)
</code></pre>

Resulting output...

<pre class="fragment"><code data-trim contenteditable>
(1, 2, 3, 4, 5, 6)
1
(1, 2) # note that slicing a tuple returns a tuple!
3
False
</code></pre>
</section>

<section markdown="block">
## Iteration

Just like iterating over strings or lists.

<pre><code data-trim contenteditable>
for value in (1, 2, 3):
	print(value)
</code></pre>
</section>

<section markdown="block">
## Tuple Unpacking / Multiple Assignment

We talked briefly talked about multiple assignment.  This is generally done with tuples, and when it's done with tuples, it's called  __tuple unpacking__. 

* a tuple of variables on the left of an assignment operator
* a tuple of values on the right of an operator 
* both have the same number of elements 
* each value is assigned to each variable in the order that the elements are in

<pre><code data-trim contenteditable>
>>> first_name, last_name = ("Hiro", "Protagonist")
>>> print(first_name)
Hiro
>>> print(last_name)
Protagonist
</code></pre>
</section>

<section markdown="block">
### Tuple Unpacking Examples

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

<pre class="fragment"><code data-trim contenteditable>
1
2
2
3
</code></pre>
</section>

<section markdown="block">
### More Info About Multiple Assignment

Tuple unpacking is the most common way of performing multiple assignment... but the assignment operator is actually super flexible:

[More than you ever wanted to know about the assignment operator](http://docs.python.org/3.2/reference/simple_stmts.html#assignment-statements)

</section>

<section markdown="block">
### List of Tuples

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

<!--_ -->
</section>

<section markdown="block">
### List of Tuples Continued

Unpacking works in for loops as well!  Imagine that each element is retrieved form the outer list.  Each element is a tuple which can be unpacked into multiple loop variables.

<pre><code data-trim contenteditable>
characters = [("Hiro", "Protagonist"), ("Yours", "Truly")]
for first, last in characters:
	print("first name is " + first)
	print("last name is " + last)
</code></pre>
</section>

<section markdown="block">
### Another List of Tuples Example 

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
pairs_of_numbers = [(1, 2), (2, 3)]
for a, b in pairs_of_numbers:
	print(a + b)
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
3
5
</code></pre>
</section>

<section markdown="block">
### Returning Tuples

Tuples and tuple unpacking can provide a method of returning multiple values from a function. __What do you think this prints out?__

<pre><code data-trim contenteditable>
def calculate_3d_point():
	result = (2, 4, 0)
	return result

x, y, z = calculate_3d_point()
print("the z coordinate is %s" % (z))
print("the x coordinate is %s" % (2))
</code></pre>

<pre><code data-trim contenteditable>
the z coordinate is 0
the x coordinate is 2
</code></pre>
</section>

<section markdown="block">
## Other Types

Additional compound types (objects composed of other objects)

* dictionaries
* sets

Aaaand... some other types:

* __bools__
    * comparison operators
    * logical operators
* __functions__
    * also an object
    * function call _operator_
</section>

<section markdown="block">
## About Logical Operators

Truthy and falsey values:

* <code>[], "", {}, None, 0</code> are all intrinsically <code>False</code>
* almost everything else is <code>True</code>

Sooo... this is a thing:

* __or__ returns the left hand value if it's _truthy_... the right hand value otherwise
* __and__ returns the left hand value if it's _falsey_... the right hand value otherwise

<pre><code data-trim contenteditable>
>>> None or 40
40
>>> 5 or 40
5
>>> [] and "hello"
[]
</code></pre>

</section>


<section markdown="block">
## control structures

* __conditionals__ (no switch, though!)
* __loops__
    * while (with else?)
    * for, with iterable objects
        * range
        * sequence types

</section>

<section markdown="block">
## for loops

__What does for loop _actually_ do? Some examples:__ &rarr;


<pre><code data-trim contenteditable>
for i in range(4):
    print(i)

numbers = [25, 50, 100]
for num in numbers:
    print(num)

for ch in "hello"
    print("ch")

</code></pre>
</section>

<section markdown="block">
## for loops continued

In every case in the previous slide, the <code>for</code> loop was __going over ever element in an iterable object__.

An __iterable__ object is...

* an object that is capable of giving back one element at a time
* (we'll see how later in the semester)
* strings, lists, range objects, tuples, etc. ... are all iterable objects

</section>

<section markdown="block">
## Iterating with Indexes

__What if you want an index with your element?__ &rarr;

<pre><code data-trim contenteditable>
# use enumerate... it gives back a list of tuples
# each tuple has two elements, an index and an element
# [(0, "foo"), (1, "bar") ...]
stuff = ["foo", "bar", "baz", "foo"]
for index, element in enumerate(stuff):
    print(index, element)
</code></pre>
</section>

<section markdown="block">
## while with else

<code>while</code> loops can _actually_ have an <code>else</code> clause!

The code in the else only gets executed if the while loop condition evaluates to False:

<pre><code data-trim contenteditable>
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Done")
</code></pre>
<pre><code data-trim contenteditable>
0
1
2
Done
</code></pre>
</section>

<section markdown="block">
## while with else continued

If the while loop terminates before the condition becomes False, the code in <code>else</code> will not be executed:

<pre><code data-trim contenteditable>
x = 0
while x < 3:
    print(x)
    if x == 1:
        break
    x += 1
else:
    print("Done")
</code></pre>
<pre><code data-trim contenteditable>
0
1
</code></pre>

</section>


