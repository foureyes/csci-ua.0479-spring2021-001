---
layout: slides
title: "Lists"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Lists Methods vs String Methods

Hey. Did you know that __lists are mutable__? Of course you did!

Why do we care? __It turns out that mutability influences how list methods work.__ &rarr;

* {:.fragment} when we use a method on a __string__... we _always_ get a new value back
* {:.fragment} however, when we use a method on a list...
    * {:.fragment} it may change the actual list (most of the time)
    * {:.fragment} or it could give back a value (some of the time)
    * {:.fragment} or maybe it could change __and__ give back a value (maybe once)

</section>

<section markdown="block">
## Methods That Mutate the Original List

__The following methods change the original list that they're called on. All of them return None, except for one weirdo method, pop.__ &rarr;

Methods for __adding__ elements:
{:.fragment}

* {:.fragment} <code>append</code> 
* {:.fragment} <code>extend</code> 
* {:.fragment} <code>insert</code> 

Methods for __removing__ elements:
{:.fragment}

* {:.fragment} <code>remove</code>
* {:.fragment} <code>pop</code> (also returns a value!)

Miscellaneous methods
{:.fragment}

* {:.fragment} <code>reverse</code>
* {:.fragment} <code>sort</code>

</section>
<section markdown="block">
## Append

__Adds a single element to end of list__ (think push?) &rarr;


<pre><code data-trim contenteditable>
>>> numbers = [1, 2, 3]
>>> numbers.append(4)
>>> numbers
[1, 2, 3, 4]
>>> result = numbers.append(4) # I return None!
>>> print(result)
None
</code></pre>

</section>

<section markdown="block">
## Extend

__Adds every element in a sequence as an individual element in the original list.__ (continuing session from previous slide)... &rarr;

<pre><code data-trim contenteditable>
>>> numbers.extend('bye')
>>> numbers
[1, 2, 3, 4, 4, 'b', 'y', 'e']
>>> numbers.extend([9, 8, 7])
>>> numbers
[1, 2, 3, 4, 4, 'b', 'y', 'e', 9, 8, 7]
</code></pre>

Notice how this differs from <code>append</code>

<pre><code data-trim contenteditable>
>>> numbers.append([9,8,7])
>>> numbers
[1, 2, 3, 4, 4, 'b', 'y', 'e', 9, 8, 7, [9, 8, 7]]
</code></pre>
</section>

<section markdown="block">
## Concatenation and Insert

Oh yeah... __concatenation doesn't actually change the original list__. 

Aaand, if you want to add an element elsewhere in the list __use insert to insert before an index.__ (again, continuing from the previous session) &rarr;

<pre><code data-trim contenteditable>
>>> numbers + [1, 2] # + doesn't change original list!
[1, 2, 3, 4, 4, 'b', 'y', 'e', 9, 8, 7, [9, 8, 7], 1, 2]
>>> numbers # see? ^^^^
[1, 2, 3, 4, 4, 'b', 'y', 'e', 9, 8, 7, [9, 8, 7]]
>>> numbers.insert(0, 'hello') # insert before element at 0
>>> numbers
['hello', 1, 2, 3, 4, 4, 'b', 'y', 'e', 9, 8, 7, [9, 8, 7]]
</code></pre>
</section>


<section markdown="block">
## Remove, Append and Extend Revisited

__remove__ removes the first occurrence of an object in a list. __Let's check it out, along with additional examples of append and extend.__ &rarr;

<pre><code data-trim contenteditable>
>>> numbers = [1, 2, 3, 2, 2, 2]
>>> numbers.remove(2) # removes first 2!
>>> numbers
[1, 3, 2, 2, 2]
>>> numbers.append([987]) 
>>> numbers # btw, appending single element list is still a list
[1, 3, 2, 2, 2, [987]]
>>> numbers.extend(['thing1', 'thing2'])
>>> numbers # again, extend adds every element in a sequence...
[1, 3, 2, 2, 2, [987], 'thing1', 'thing2']
</code></pre>
</section>

<section markdown="block">
## Remove Continued

__Remove, just like append, extend and insert... return None.__ (continued from previous session) &rarr;

<pre><code data-trim contenteditable>
>>> numbers.remove(2)
>>> numbers # ok, makes sense, removed 1 item
[1, 3, 2, 2, [987], 'thing1', 'thing2']
>>> ret = numbers.remove(2) 
>>> print(ret) # note, however, we get None back as the return value!
None
>>> numbers
[1, 3, 2, [987], 'thing1', 'thing2']
</code></pre>
</section>

<section markdown="block">
## Ah, Pop

Continuing from the last session, we can use __pop__ to __remove and return the last element (or, if we specify an argument, the element at a specific index)__ &rarr;

<pre><code data-trim contenteditable>
>>> ret = numbers.pop()
>>> print(ret)
thing2
>>> numbers
[1, 3, 2, [987], 'thing1']
>>> numbers
[1, 3, 2, [987], 'thing1']
>>> ret = numbers.pop(3)
>>> ret
[987]
>>> numbers
[1, 3, 2, 'thing1']
</code></pre>
</section>

<section markdown="block">
## Sort and Reverse

__They do what you expect, in place (they also both return None)__ &rarr;

<pre><code data-trim contenteditable>
>>> numbers = [4, 5, 1, 2]
>>> numbers.sort()
>>> numbers
[1, 2, 4, 5]
>>> numbers.reverse()
[5, 4, 2, 1]
</code></pre>
</section>

<section markdown="block">
## Ok... So What About Those Other List Methods?

__count__ and __index__ don't change the list, they return a new value....

* __count__ - returns the number of occurrences of an element in a list
* __index__ - gives back the index of the first occurrence of an element in a list
    * (it throws an exception otherwise)
    * if you just want a boolean value, use <code>in</code> operator instead

</section>

<section markdown="block">
## Count, Index and In Examples

Again... __these all return a value, but none of them change the original list__ (because... _why would they_?) &rarr;

<pre><code data-trim contenteditable>
>>> numbers = [1, 2, 4, 5]
>>> numbers.count(1) # there's one 1
1
>>> numbers.index(5) # 5 is at index 3
3
>>> numbers.index('surprise')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: 'surprise' is not in list
>>> 2 in numbers # use in if you want a bool
True
</code></pre>

</section>

<section markdown="block">
## An Error with Index!

Ack. __index__ is tricky because it could cause a runtime error. __How do we get around it?__ &rarr;

* {:.fragment} defensive programming... <code>if my_element in my_list: # then use index</code>
* {:.fragment} exception handling... <code>try: # use index in try body</code>
* {:.fragment} exception handling is _usually_ preferred (easier to ask for forgiveness than permission), __and we'll see this later__

</section>

<section markdown="block">
## Using the built-in List function / constructor

Just like <code>int(obj)</code>, <code>str(obj)</code>, etc. converts to the type of the same name ... __you can use the <code>list</code> function to create (of course!) lists__ &rarr;

<pre><code data-trim contenteditable>
>>> list()
[]
>>> list(range(10)) # range to a string...
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list('asdf') # list to a string....
['a', 's', 'd', 'f']
>>> 'asdf'.split('') # split won't work though!
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: empty separator
</code></pre>

</section>

<section markdown="block">
##  List Comprehension Preview

__A common pattern for creating a new list by transforming every element in another list (mapping) is to use an accumulator__. (Here... we're doubling every element).

<pre><code data-trim contenteditable>
>>> new_numbers = []
>>> for n in numbers:
...   new_numbers.append(n * 2)
...
>>> new_numbers
[2, 4, 8, 10]
</code></pre>

A list comprehension version:

<pre><code data-trim contenteditable>
>>> new_numbers = [n * 2 for n in numbers]
>>> new_numbers
[2, 4, 8, 10]
</code></pre>


</section>

<section markdown="block">
##  And Another

__Same pattern... but here we're filtering elements.__ (only keep even numbers) &rarr;

<pre><code data-trim contenteditable>
>>> numbers = [1, 2, 3, 4, 5]
>>> new_numbers = []
>>> for n in numbers:
...   if n % 2 == 0:
...     new_numbers.append(n)
...
>>> new_numbers
[2, 4]
</code></pre>

List comprehension version:

<pre><code data-trim contenteditable>
>>> new_numbers = [n for n in numbers if n % 2 == 0]
>>> new_numbers
[2, 4]
>>> numbers
[1, 2, 3, 4, 5]

</code></pre>

</section>

{% comment %}
{% endcomment %}

