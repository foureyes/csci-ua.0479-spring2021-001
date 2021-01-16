---
layout: slides
title: "Lists - References, Comprehensions, Built-in Functions"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Creating Lists

__What are some ways to create new lists?__ '&rarr;

1. {:.fragment} list literals
2. {:.fragment} list comprehensions
3. {:.fragment} slicing and concatenation (both produce an entirely new list)
4. {:.fragment} <code>list</code> function / constructor (we sort of saw this briefly when talking about range)
5. {:.fragment} various methods and functions  that we haven't gone over yet(<code>sorted()</code>, <code>str.split()</code>)

Check out [the documentation on constructing lists](https://docs.python.org/3.5/library/stdtypes.html#list)
{:.fragment}
</section>

<section markdown="block">
## List Literal

You can create __list literals__ by using square brackets: <code>[]</code>  &rarr;

<pre><code data-trim contenteditable>
[] # an empty list
</code></pre>

A list with values (note that the values don't have to be the same type)

<pre><code data-trim contenteditable>
[1, 2, 3, 4, 'foo', 'bar', 'baz']
</code></pre>

You can even nest lists within lists, and index into the inner list:

<pre><code data-trim contenteditable>
>>> nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> nested[-1][0] 
7
</code></pre>

{% comment %}
You can even nest other compound data types (like <code>tuples</code> or <code>dicts</code>):

<pre><code data-trim contenteditable>
[(1, 2, 3), {"number": 4}, "five"]
</code></pre>
{% endcomment %}

</section>

<section markdown="block">
## Accessing Nested Items in Lists

__It's possible to continually index into a list to retrieve nested elements__ &rarr;

Nested lists

<pre><code data-trim contenteditable>
>>> stuff = [[], [1, 2, 3], None]
>>> stuff[0]
[]
>>> stuff[1]
[1, 2, 3]
>>> stuff[2]
>>> stuff[1][2]
3
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## More Examples of Indexing

__As long as the inner element is indexable, it'll work just fine!__ &rarr;

Strings in lists

<pre><code data-trim contenteditable>
>>> stuff = ['foo', 'bar', 'baz']
>>> stuff[-1][-1]
'z'
</code></pre>

{% comment %}
Tuples in lists

<pre><code data-trim contenteditable>
>>> points = [(1, 2), (3, 4), (5, 6)]
>>> points
[(1, 2), (3, 4), (5, 6)]
>>> points[0][0]
1
</code></pre>
{% endcomment %}

</section>

<section markdown="block">
## List Constructor

As with other types and their corresponding constructors, __you can call <code>list()</code> to create a new (of course) list__ &rarr; 

<pre><code data-trim contenteditable>
>>> list() # ----> [] an empty list
</code></pre>

Or, create a list from an __iterable object__ (an object that's capable of returning its items one at a time... like a string, range, tuple, etc.):

<pre><code data-trim contenteditable>
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
>>> list(range(1, 4)) # range gives back a range object, which can be converted to a list
[1, 2, 3]
</code></pre>

{% comment %}
>>> list((1, 2, 3)) # a tuple
[1, 2, 3]
{% endcomment %}

For now, think of an _iterable object_  as anything that can be looped over 

{% comment %}
(like sequences, files, ranges, etc.).
{% endcomment %}
</section>


<section markdown="block">
## An Aside on Strings

__Using the list function on a string, each character of a string becomes an individual element in the new list.__ &rarr;

<pre><code data-trim contenteditable>
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
</code></pre>

There's also a <code>split</code> method on strings (we'll see this later in full detail): 

<pre><code data-trim contenteditable>
>>> "hw01,hw02,hw03".split(",")
['hw01', 'hw02', 'hw03']
</code></pre>

However, you <code>split</code> can't mimic the behavior of <code>list</code>:

<pre><code data-trim contenteditable>
'hello'.split() # causes an error instead of a list of characters)
</code></pre>

</section>
<section markdown="block">
## List Comprehensions

A __list comprehension__ is a compact way of creating lists from other _iterable_ objects. Some common applications include:

1. _mapping_ 
    * map each element in an existing __sequence__ or __iterable__ 
    * ... to a new list by performing some operation(s) on each original elements
2. _filtering_ 
    * filter elements in an existing __sequence__ or __iterable__ 
    * ... so that a new list is created composed of only the elements from the original iterable that satisfy some sort of condition (pass a test)


Check out [the official Python 3 documentation on list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).
</section>


<section markdown="block">
##  List Comprehension Syntax

__The syntax of a list comprehension is an expression, a for clause and an if clause wrapped in square brackets:__ &rarr;

<pre><code data-trim contenteditable>
[expression ... for clause ... if clause]
</code></pre>

* __expression__ represents what the value in the new list will be based on a loop variable introcued in the _for clause_
* the __for clause__ is a compact for __loop__; it can be any loop (like iterating over characters in a string or numbers in a range)
* an __if clause__ that specifies a __condition__ for an element to be included in the new list

</section>


<section markdown="block">
## List Comprehension Syntax Explained

Or... another way to put it is:

<pre><code data-trim contenteditable>
[expression ... for clause ... if clause]
 |                      |              |
 what value goes        |    should this value
 in the new list?       |    be included in the
                        |    new list?
         what to loop over?
</code></pre>

For example... the list comprehension below creates a new list composed of the uppercase version of every word in the original list that has more than 2 characters.

<pre><code data-trim contenteditable>
>>> words = ['this', 'is', 'a', 'list'] 
>>> [w.upper() for w in words if len(w) > 2]
['THIS', 'LIST']
</code></pre>
</section>
<section markdown="block">
##  List Comprehension Examples

In this first example, a list comprehension is used to simply make a copy of an existing list. Note that the result of a list comprehension __is a new list__ ... so __to save that value, assign it to a variable__ &rarr;

<pre><code data-trim contenteditable>
>>> a = [1, 2, 3]
>>> [n for n in a]
[1, 2, 3]
>>> b = [n for n in a]
>>> b # (just like a!)
[1, 2, 3]
</code></pre>

A minor modification of the expression will __double the value of every element in the original list.__ &rarr;

<pre><code data-trim contenteditable>
>>> [n * 2 for n in a]
[2, 4, 6]
</code></pre>

</section>

<section markdown="block">
## More Examples

The for loop is not limited to lists of numbers. 


__Getting every character in a string, adding an exclamation to it... and making a new list out of each character/exclamation combo.__ &rarr;

<pre><code data-trim contenteditable>
>>> [ch + '!' for ch in "hello"]
['h!', 'e!', 'l!', 'l!', 'o!']
>>> [name.upper() for name in names]
['ALICE', 'BOB', 'CAROL']
</code></pre>

And with a range, powers of 16:

<pre><code data-trim contenteditable>
>>> [16 ** i for i in range(7)]
[1, 16, 256, 4096, 65536, 1048576, 16777216]
</code></pre>

</section>

<section markdown="block">
## Even More Examples

__Iterating over a list of strings changing them all to uppercase__ &rarr;

<pre><code data-trim contenteditable>
>>> names = ['alice', 'bob', 'carol']
>>> upper_names = [name.upper() for name in names]
>>> upper_names
['ALICE', 'BOB', 'CAROL']
</code></pre>

__Only do this for the names that don't start with 'c'__ &rarr;
<pre><code data-trim contenteditable>
>>> [name.upper() for name in names if name[0] != 'c']
['ALICE', 'BOB']
</code></pre>
</section>

<section markdown="block">
## How to Make Your Code Unreadable

(Or, to fulfill a compulsion to put things into one line).

__There's a one line if/else statement (someimtes called _ternary_ operator in other languages)__ &rarr;

<pre><code data-trim contenteditable>
value1 if condition else value2
</code></pre>

* evaluates to <code>value1</code> (left side) if condition is <code>True</code>
* evaluates to <code>value2</code> (right side / second value) if condition is <code>False</code>


<pre><code data-trim contenteditable>
>>> 'first' if True else 'second'
'first'
>>> 'first' if False else 'second'
'second'
</code></pre>

__Why?__ &rarr;
</section>

<section markdown="block">
## To Make a Monstrosity

__Stuffing more logic into our list comprehension, we can choose to include names that begin with c, but change how they're transformed in the expression.__ &rarr;

<pre><code data-trim contenteditable>
>>> [name.upper() if name[0] != 'c' else name for name in names]
['ALICE', 'BOB', 'carol']
</code></pre>

Probably avoid this, as readability counts more than minimizing number of lines (but... interesting to see it all work together).
</section>

<section markdown="block">
## Looping Over Lists


You can go over every element in a list a few different ways. __What are they? (they all involve a for loop, of course)__ &rarr;

1. {:.fragment} __go over every element__ 
    * (the regular <code>for element in sequence</code> loop)
2. {:.fragment} __go over every index__
    * ...and index into the list to retrieve an element 
    * (using <code>range</code> - <code>for i in range(len(sequence))</code>
2. {:.fragment} __go over every element along with the index__ 
    * (using the built-in function <code>enumerate</code> - <code>for i, element in enumerate(sequence)</code>

</section>

<section markdown="block">
## Every Element, The "Regular Way"

Retrieve every element in a list using a for loop; the __loop variable__ __represents each element...__ &rarr;

<pre><code data-trim contenteditable>
>>> stuff = ['foo', 'bar', 'baz']
>>> for word in stuff:
...   print(word)
...
foo
bar
baz
</code></pre>
</section>

<section markdown="block">
## With Indexes

Generate every possible index in the list; the __loop variable represents each index...__ &rarr;

<pre><code data-trim contenteditable>
>>> for i in range(len(stuff)):
...   print(i, stuff[i])
...
0 foo
1 bar
2 baz
</code></pre>

</section>

<section markdown="block">
## Every Element, With Index 

Get every element and index using the built-in function, <code>enumerate</code>. <code>enumerate</code> actually gives back an <code>enumerate object</code>, __which behaves like a list of tuples__ ... &rarr;

<pre><code data-trim contenteditable>
>>> for i, the_thing in enumerate(stuff):
...   print(i, the_thing)
...
0 foo
1 bar
2 baz
</code></pre>

Every tuple contains 2 elements:

1. the index
2. the element

</section>

<section markdown="block">
## Enumerate

Again, <code>enumerate</code> gives back an <code>enumerate object</code>, which acts like a list of tuples.

__It gives back a list-like object of tuples.__ &rarr;

<pre><code data-trim contenteditable>
>>> print(enumerate(stuff))
<enumerate object at 0x110076870>
</code></pre>

__You can even use it in a list comprehension!__ &rarr;

<pre><code data-trim contenteditable>
>>> [t for t in enumerate(stuff)]
[(0, 'foo'), (1, 'bar'), (2, 'baz')]
</code></pre>

__Which is the same as just calling <code>list</code> with the enumerate object as the argument.__ &rarr;

<pre><code data-trim contenteditable>
>>> list(enumerate(stuff))
[(0, 'foo'), (1, 'bar'), (2, 'baz')]
</code></pre>
</section>

<section markdown="block">
## Which One to Use?

__How do you choose which method of iteration to use?__ &rarr;

1. {:.fragment} if you just care about the __elements__, prefer the _regular_ for loop
2. {:.fragment} if you want the __index__, use <code>enumerate</code> or <code>range</code>
    * this begs the question... __why would you need the index?__ &rarr;
    * {:.fragment} if you want to __change__ the original list at specific indexes
        * remember, to change an element in a list... 
        * swapping, assignment, etc.
        * <code>some_list[index] = 'new value'</code>
    * {:.fragment} or if you care about the position of an element
        * every nth element
</section>

<section markdown="block">
## Creating a List from Another List

When working with lists, you'll find that common task is to produce a list from an existing list by:

1. initializing an empty list as an accumulator
2. then... performing operations on elements of the original list
3. ... and adding those transformed elements to the new list

__The code below creates a new with 10 added to every number in the original list. The original list, <code>numbers</code>, is unchanged.__ &rarr;

<pre><code data-trim contenteditable>
numbers = [10, 12, 5, 18, 3]
new_numbers = []
for number in numbers:
    new_numbers.append(number + 10)
print(numbers, new_numbers)
</code></pre>

Of course, this can be done in a single line list comprehension. __How?__ &rarr;

<pre><code data-trim contenteditable>
new_numbers = [n + 10 for n in number]
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Changing a List's Elements

Instead of creating a new list, you may need to _actually_ change the original list. __Again, if we want to change a list, we'll have to work with indexes.__ &rarr;

The following code increments every number in the list, <code>numbers</code>, by 10. (Same as the previous, but changing the original instead making a new list).

<pre><code data-trim contenteditable>
numbers = [10, 12, 5, 18, 3]
for i, number in enumerate(numbers):
  numbers[i] = number + 10
print(numbers)
</code></pre>
</section>

<section markdown="block">
## Reverse a List by Creating a New List

A quick exercise. Reverse the following list by creating a new list with the original elements in reverse order.

<pre><code data-trim contenteditable>
numbers = [10, 12, 5, 18, 3]
#TODO: create a new list, with element order reversed
</code></pre>

<pre><code data-trim contenteditable>
new_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    new_numbers.append(numbers[i])
print(new_numbers, numbers)
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Reverse a List by Changing the Original List

Same as the previous... reverse the following list, __but this time, change the original list rather than accumulate__.  &rarr;

<pre><code data-trim contenteditable>
numbers = [10, 12, 5, 18, 3]
# TODO: reverse the above list in place!
</code></pre>

<pre><code data-trim contenteditable>
print('before', numbers)
for i in range(len(numbers) // 2):
    j = len(numbers) - (i + 1)
    numbers[i], numbers[j] = numbers[j], numbers[i]
print('after', numbers)
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Changing Elements While Looping

Be careful when adding or removing elements in a list while looping over it using a _regular_ for loop. __It may yield unexpected results!__ &rarr;

The code below attempts to remove every instance of the string, <code>"foo"</code> from the list, <code>words</code>. It doesn't quite work! __Why?__ &rarr;

<pre><code data-trim contenteditable>
words = ['foo', 'foo', 'bar', 'baz', 'foo']

# maybe this removes every occurrence of foo?
for i, word in enumerate(words):
    print(i, word)
    if word == 'foo':
        words.remove(word)
print(words)
</code></pre>

The list is shortened on some iterations, so the loop stops prematurely. <a href="http://pythontutor.com/visualize.html#code=words+%3D+%5B'foo',+'foo',+'bar',+'baz',+'foo'%5D%0A%0A%23+maybe+this+removes+every+occurrence+of+foo%3F%0Afor+i,+word+in+enumerate(words%29%3A%0A++++print(i,+word%29%0A++++if+word+%3D%3D+'foo'%3A%0A++++++++words.remove(word%29%0Aprint(words%29&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0">(Check out the  pythontutor version to see what happens!)</a>
{:.fragment}

</section>

<section markdown="block">
## Aliasing / References 

Remember that names are just references to objects. __We can create an alias by assignming one name to another... so that both names point to the same object.__ &rarr;

<pre><code data-trim contenteditable>
>>> a = [1, 2, 3]
>>> b = a
>>> b.append(4)
>>> a
[1, 2, 3, 4]
</code></pre>

<a href="http://pythontutor.com/visualize.html#code=a+%3D+%5B1,+2,+3%5D%0Ab+%3D+a%0Ab.append(4%29%0Aa%0A%5B1,+2,+3,+4%5D%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0">(See the reference diagram on pythontutor)</a>

</section>

<section markdown="block">
## Elements in an Array are References 

You can actually think of lists as a collection of references. __Here, we have two lists that are elements in another list.__ &rarr;

<pre><code data-trim contenteditable>
>>> a = [1, 2, 3]
>>> a = [1, 2]
>>> b = [3, 4]
>>> c = [a, b]
>>> a.append(100)
>>> a
[1, 2, 100]
</code></pre>

<a href="http://pythontutor.com/visualize.html#code=a+%3D+%5B1,+2,+3%5D%0Aa+%3D+%5B1,+2%5D%0Ab+%3D+%5B3,+4%5D%0Ac+%3D+%5Ba,+b%5D%0Aa.append(100%29%0Aa%0A%5B1,+2,+100%5D%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0">(See the reference diagram on pythontutor)</a>

</section>
<section markdown="block">
## Elements in an Array are References Continued

__Multiplying a list of lists just repeats existing references.__ &rarr;

<pre><code data-trim contenteditable>
>>> a = [1, 2, 3]
>>> multi_a = [a] * 3 # put the list a in another list
>>> multi_a
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
>>> del a[0]
>>> multi_a
[[2, 3], [2, 3], [2, 3]]
</code></pre>

<a href="http://pythontutor.com/visualize.html#code=a+%3D+%5B1,+2,+3%5D%0Amulti_a+%3D+%5Ba%5D+*+3%0Amulti_a%0A%5B%5B1,+2,+3%5D,+%5B1,+2,+3%5D,+%5B1,+2,+3%5D%5D%0Adel+a%5B0%5D%0Amulti_a%0A%5B%5B2,+3%5D,+%5B2,+3%5D,+%5B2,+3%5D%5D%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0">(See the reference diagram on pythontutor)</a>
</section>
<section markdown="block">
## Functions and References

Parameters in function definitions reference the original object passed in as an argument. __What is the output of the following code?__ &rarr;

<pre><code data-trim contenteditable>
def make_first_none(some_list):
    if len(some_list) >= 1:
        some_list[0] = None
    # else don't do anything
</code></pre>

<pre><code data-trim contenteditable>
words = ['foo', 'bar', 'baz']
make_first_none(words)
print(words)
</code></pre>

<code>words</code>, outside of the function, is changed to <code>[None, 'bar', 'baz']</code> <a href="http://pythontutor.com/visualize.html#code=def+make_first_none(some_list%29%3A%0A++++try%3A%0A++++++++some_list%5B0%5D+%3D+None%0A++++except+IndexError%3A%0A++++++++pass%0A%0Awords+%3D+%5B'foo',+'bar',+'baz'%5D%0Amake_first_none(words%29%0Aprint(words%29%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0">(See the pythontutor version to go through the program step-by-step)</a>
</section>

<section markdown="block">
## Globals that are Mutable Objects

You can't change what object a global variable name refers to (without the <code>global</code> keyword, which you may encounter in other code), but you __can change mutable global objects from within a function__!

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
instruments = []
def add_cow_bell():
    instruments.append("cow bell")
add_cow_bell()
print(instruments)
</code></pre>

<pre><code data-trim contenteditable>
['cow bell']
# the outer list instruments is mutated
# by the function, add_cow_bell
</code></pre>
{:.fragment}

<a class="fragment" href="http://pythontutor.com/visualize.html#code=instruments+%3D+%5B%5D%0Adef+add_cow_bell(%29%3A%0A++++instruments.append(%22cow+bell%22%29%0Aadd_cow_bell(%29%0Aprint(instruments%29%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0">(See python tutor to view the reference diagram)</a>

</section>

<section markdown="block">
## Masking / Scope

Note that global variables and parameters can be masked (functions will look for names locally first, enclosing next, then global)! 

<pre><code data-trim contenteditable>
instruments = []
def add_cow_bell():
    instruments = ['kazoo', 'theremin']
    instruments.append("cow bell")
add_cow_bell()
print(instruments)
</code></pre>

<pre><code data-trim contenteditable>
[]
# the global, instruments, remains empty
# the local variable, instruments, masks
# the global variable
</code></pre>
{:.fragment}

<a class="fragment" href="http://pythontutor.com/visualize.html#code=instruments+%3D+%5B%5D%0Adef+add_cow_bell(%29%3A%0A++++instruments+%3D+%5B'kazoo',+'theremin'%5D%0A++++instruments.append(%22cow+bell%22%29%0Aadd_cow_bell(%29%0Aprint(instruments%29%0A&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0">(See python tutor to view the reference diagram)</a>
</section>

<section markdown="block">
## Built-in Functions

__A lot of common list operations that can be done manually with loops and list comprehensions are actually bundled up into handy built-in functions.__ &rarr;

* __len__ - returns the number of elements in a list
* __sum__ - returns the sum of all numbers in an _iterable_ containing numbers
* __max__ - gives back the max value in a list
* __min__ - gives back the min value in a list
* __sorted__ - returns a new sorted list
* __map__ - returns a new list with values mapped from old list
* __filter__ - returns a new list with values from the original that pass a teset
</section>

<section markdown="block">
## len, sum

__len__ and __sum__ are pretty self explanatory. Note that sum will only work with a list of all numeric types (ints, floats, complex)

<pre><code data-trim contenteditable>
>>> numbers = [1.5, 2, 4.5]
>>> len(numbers)
3
>>> sum(numbers)
8.0
</code></pre>

</section>
<section markdown="block">
## max, min

The built-in functions, __max__ and __min__ can be used two ways:

1. with a __single positional argument__ as an __iterable__
    * <code>max</code> and <code>min</code> will return the largest and smallest element in the iterable respectively
2. with an __arbitrary number of positional argumenents__
    * <code>max</code> and <code>min</code> will return the largest and smallest argument passed in respectively
    
<pre><code data-trim contenteditable>
>>> max([2, 3, 1])
3
>>> max(4, 5, 1)
5
</code></pre>
</section>

<section markdown="block">
## Defining a Key

__Both <code>max</code> and <code>min</code> have an optional keyword argument, <code>key</code>__ &rarr; 

* <code>key</code> can be used to specify what value to use when comparing elements
* the <code>key</code> that you pass in must:
    1. {:.fragment} be a __function__
    2. {:.fragment} ...that has __one parameter__ 
    3. {:.fragment} ... and __returns a value__

For example, you can pass in <code>key=math.sqrt</code>, and <code>max</code> will:
{:.fragment}

* {:.fragment} take the square roots of the elements of the list passed in...
* {:.fragment} and use that value as the basis of ordering
</section>

<section markdown="block">
## Defining a Key Continued

__In the code below, we define key as the absolute value of the element (<code>abs</code> is a built-in function that returns the absolute value of the argument passed in).__ &rarr;

<pre><code data-trim contenteditable>
>>> a = [-100, 5, 2]
>>> max(a, key=abs)
-100
</code></pre>

Consequently, -100 is the largest element because abs(-100) gives us 100 - the value used for the comparisons).

Compare this with using <code>max</code> without a key...

<pre><code data-trim contenteditable>
>>> a = [-100, 5, 2]
>>> max(a)
5
</code></pre>
</section>

<section markdown="block">
## Defining a Custom Function for Key

The <code>key</code> doesn't have to be a built-in function. __The key can be a custom function as shown below.__ &rarr;
<pre><code data-trim contenteditable>

>>> a = [-100, 5, 2]
>>> def convert2to1000(x):
...   return 1000 if x == 2 else x
...
>>> convert2to1000(2)
1000
>>> convert2to1000(100)
100
>>> max(a, key=convert2to1000)
2
</code></pre>
</section>

<section markdown="block">
## Another Example of Custom Function for Key

In the following code, the key is the custom function, <code>f</code>

<pre><code data-trim contenteditable>
>>> def f(x):
...   return 1 / x;
...
>>> max(5, 10, 2, 1, key=f)
1
</code></pre>

Again, instead of comparing the values outright, <code>max</code> applies the function <code>f</code> before comparing elements.

__(1 is returned because 1/1 is the highest value)__
</section>

<section markdown="block">
## A Quick Note on Functions

By the way... remember, __a function that doesn't return a value gives back <code>None</code>__ &rarr;

<pre><code data-trim contenteditable>
>>> def im_selfish():
...   pass
...
>>> result = im_selfish()
>>> print(result)
None
</code></pre>
</section>

<section markdown="block">
## Sort vs Sorted

The list method, __sort()__ (called on a list object) __sorts the original list that it was called on and doesn't return a value__ ... &rarr;

<pre><code data-trim contenteditable>
>>> a = [-100, 5, 2]
>>> result = a.sort()
>>> print(result)
None
>>> print(a)
[-100, 2, 5]
</code></pre>

Again, sort:

1. sorts the original list in place
2. __does not return a value__; it gives back <code>None</code> (like the previous slide)
</section>



<section markdown="block">
## Sort vs Sorted Continued

On the other hand, __the built-in function <code>sorted</code> gives back an entirely new sorted version of the list passed in as an argument to it__ &rarr;

<pre><code data-trim contenteditable>
>>> a = [-100, 7, 2, 1, 5]
>>> sorted(a)
[-100, 1, 2, 5, 7]
</code></pre>

Just like <code>max</code> and <code>min</code>, __a <code>key</code> can be passed in as a keyword argument to specify a function to be used to determine the values for ordering__ &rarr;

<pre><code data-trim contenteditable>
>>> sorted(a, key=abs)
>>> a = [-100, 7, 2, 1, 5]
[1, 2, 5, 7, -100]
</code></pre>
</section>



<section markdown="block">
## selection sort

Maybe you're into writing your own sort. You'd have to take advantage of looping with indexes so that you can swap. 

One algorithm that we can use to sort is called __selection sort__ &rarr;

1. {:.fragment} split the list into two parts; the left part is sorted, the right part is unsorted
2. {:.fragment} start with no sorted elements
3. {:.fragment} find the smallest element in the unsorted part and swap with the first unsorted value from the left

</section>


<section markdown="block">
## selection sort

__In this animation from wikipedia, red is the current min, blue is the current item, and everything in yellow is already sorted.__ &rarr;

![selection sort](../../resources/img/wikipedia-selection-sort-cc.gif)

Check out the [Khan Acadamy animation](https://www.khanacademy.org/computing/computer-science/algorithms/sorting-algorithms/a/selection-sort-pseudocode) too!
</section>

<section markdown="block">
## selection sort pseudocode

<pre><code data-trim contenteditable>
"""
for every position in the array
    assume that the current position is the smallest (it's not yet sorted)
    for every position after that
        determine which position has the smallest element
    if the current position is not the smallest
        swap the current with the smallest
"""
</code></pre>
</section>
<section markdown="block">
## selection sort implementation

__Here's an implementation of selection sort__ &rarr;

<pre><code data-trim contenteditable>
def selection_sort(li):
    for outer_index, ele in enumerate(li):
        min_index = outer_index
        for inner_index in range(outer_index + 1, len(li)):
            if li[inner_index] < li[min_index]:
                min_index = inner_index
        if min_index != outer_index:
            li[min_index], li[outer_index] = li[outer_index], li[min_index]
</code></pre>

<pre><code data-trim contenteditable>
numbers = [64,25,12,22,11]
selection_sort(numbers)
print(numbers)
</code></pre>
</section>

<section markdown="block">
## map

__map takes a function and a list and applies that function to every element in the list to create a new list__ &rarr; 

<pre><code data-trim contenteditable>
>>> def double(x):
...   return x * 2
...
>>> list(map(double, [1, 2, 3, 4]))
[2, 4, 6, 8]
</code></pre>

Note that map _actually_ gives back a mack object (which is why we needed to use list above)

<pre><code data-trim contenteditable>
>>> map(double, [1, 2, 3, 4])
<map object at 0x1100790b8>
</code></pre>


</section>

<section markdown="block">
## Looping Over a Map Object

Instead of converting to a list, we can simply loop over a map object immediately because it's iterable. &rarr;

<pre><code data-trim contenteditable>
>>> for item in map(double, [1, 2, 3, 4]):
...   print(item)
...
2
4
6
8
</code></pre>
</section>

<section markdown="block">
## Map / Equivalent list comprehensions

__Of course, why use map when you can just use a list comprehension.__ &rarr;

<pre><code data-trim contenteditable>
>>> [n * 2 for n in [1, 2, 3, 4]]
[2, 4, 6, 8]
</code></pre>
</section>

<section markdown="block">
## lambda

Maybe defining a whole lambda function was too much for you? So. Much. Code. __Can't we just inline an anonymous function.__ &rarr;

Um, sure, I guess... with <code>lambdas</code>
{:.fragment}

* {:.fragment} <code>lambda parameter: return_value</code>
* {:.fragment} <code>lambda x: x * 2</code> is equivalent to:

<pre><code data-trim contenteditable>
def double(x):
    return x * 2
</code></pre>
{:.fragment}

Sooo... a lambda can be passed in as an argument when a function has another function as a parameter:
{:.fragment}

<pre><code data-trim contenteditable>
>>> list(map(lambda x: x * 2, [1, 2, 3, 4]))
[2, 4, 6, 8]
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##  filter

__Filter also produces a new list:__ &rarr;

* It applies the function in the first argument to every element in the second argument... 
* and if the function returns True, it adds that element ot the new list.

<pre><code data-trim contenteditable>
>>> numbers = [5, 6, 7, 8, 9]
>>> def isOdd(x):
...   return x % 2 == 1
...
>>> list(filter(isOdd, numbers))
[5, 7, 9]
</code></pre>

With lambda

<pre><code data-trim contenteditable>
>>> list(filter(lambda x: x % 2 != 0, numbers))
[5, 7, 9]
</code></pre>

With a list comprehension

<pre><code data-trim contenteditable>
>>> [n for n in numbers if n % 2 == 1]
</code></pre>

</section>

<section markdown="block">
## Reduce

__Typically, with filter and map... there's another function called <code>reduce</code>.__ 

* __reduce__ will take a list and whittle it down to a single value
* like summing a bunch of numbers in a list (eh... there's actually already a <code>sum</code> function)
* it takes a function as a first argument, a list as a second, and an initial value as the third
* the function has two arguments a previous (accumulator) and the current element
* it'll return the new value of the accumulator
* it pretty much simulates an accumulator and a for loop, with the body of the for loop tucked away in the supplied function


__But reduce doesn't exist (sort of, at least not right away)__ &rarr;


</section>

<section markdown="block">
## Reduce Example

It goes something like this:

<pre><code data-trim contenteditable>
def add(accum, value):
    return accum + value

reduce(add, [5, 2, 3], 0) 
# -->10
</code></pre>

Which is equivalent to:

<pre><code data-trim contenteditable>
accum = 0
for value in [5, 2, 3]:
    accum = accum + value
</code></pre>
</section>
<section markdown="block">
## WHY U NO REDUCE

__However It's a little more difficult to find in Python 3. Why?__ &rarr;

* {:.fragment} because it's tucked away in a module called <code>functools</code>...
* {:.fragment} and the [BDFL](https://en.wikipedia.org/wiki/Guido_van_Rossum) wants the community to avoid its usage 
* {:.fragment} [because it's bad (see this SO article)](http://stackoverflow.com/questions/181543/what-is-the-problem-with-reduce)
* {:.fragment} TL;DR <code>reduce</code> is confusing, better to just be explicit and use an accumulator with a loop
* {:.fragment} like what do these _even do_???

<pre><code data-trim contenteditable>
functools.reduce(lambda accum, ele: accum + [ele * 2], [1, 2, 3, 4], [])
functools.reduce(lambda accum, ele: accum + "!" + ele, ["foo", "bar", "baz"], "")
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
[2, 4, 6, 7] # (doubles every value)
!foo!bar!baz # (concatenates strings)
</code></pre>
{:.fragment}
</section>


{% comment %} 
 
## map and filter

* function then list
* loop over
* turn to list to see



## selection sort

<pre><code data-trim contenteditable>
def selection_sort(li):
    for outer_index, ele in enumerate(li):
        min_index = outer_index
        for inner_index in range(outer_index + 1, len(li)):
            if li[inner_index] < li[min_index]:
                min_index = inner_index
        if min_index != outer_index:
            li[min_index], li[outer_index] = li[outer_index], li[min_index]


numbers = [64,25,12,22,11]
selection_sort(numbers)
print(numbers)
</code></pre>
 
## map and filter

* function then list
* loop over
* turn to list to see

## dictionaries

* syntax
* name value pairs
* key / index, value
    * key - immutable
    * value - any
* retrieving
    * key error
* adding a key/value pair
* removing

## looping

## methods

* keys
* values
* get
* update
* pop

## counting letters

* d[key] = d.get(key, 0) + 1
"""






















































































{% endcomment %}





