---
layout: slides
title: List Methods 
---
<section markdown="block" class="title-slide">
#  List Methods
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  Lists are (Mutable) Objects 

Lists are __objects__, and they have a slew of __methods__ that you can call on them: 

* lists are __mutable__ ... 
* many methods actually __change the list in place__!  __Let's see how this differs from strings__ &rarr;

<pre><code data-trim contenteditable>
>>> s = 'hello'
>>> s.upper()
'HELLO'
>>> print(s)
hello
</code></pre>
<pre><code data-trim contenteditable>
>>> numbers = [5, 3, 4]
>>> numbers.sort()
>>> print(numbers)
[3, 4, 5]
</code></pre>
</section>

<section markdown="block">
##  List Methods Continued

So.... why does this matter?

* most list methods modify the list __in place__
* most list methods __don't return a value__!
* that means... 
	* if you're getting __None__... 
	* you're probably assigning the return result of a list method to a variable

</section>



<section markdown="block">
##  Some methods that you can call on lists

<pre><code data-trim contenteditable>
li = [1, 2, 3]
</code></pre>

* li.append(4) # appends element to end of list
* li.extend([3, 4]) # appends all items of one list to the other...
* li.insert(2, "asdf") # insert object before index
* li.remove(4) # removes first occurrence of...
* li.pop() # returns and removes the last element
* li.sort() # sorts list in place
* li.count(1) # returns number of occurrences of arg in list
* li.index(1) # returns the index of the element supplied
</section>

<section markdown="block">
##  Adding Elements

* __append__(_object_) - append object to end of list, even another list! 
* __extend__(_iterable_) - appends all items of one iterable (list, string, etc.) to the original list
* __insert__(_index_, _object_) - insert object before index

Usage notes: 

* use __append__ when you want the whole object added to the end of a list &rarr;
* use __extend__ when you want every element in another list added as an individual element to the original &rarr;
* use __insert__ when you want to add an element to an arbitrary place in the original list &rarr;
</section>

<section markdown="block">
##  Removing Elements

* __remove__(object) - removes first occurrence of object in list
* __pop__() - __returns and removes__ the last element, takes an optional argument to specify index

Usage notes:

* use __remove__  for finding and removing an element &rarr;
* use __pop__ when you want to delete an element at a specific index (by default, the last element)... you also get the element removed as a return value! &rarr;
</section>

<section markdown="block">
##  Miscellaneous Methods

* __sort__() - sorts a list in place &rarr;
* __count__(object) - counts the number of occurrences of object in the original list &rarr;
* __index__(object) - returns the index of the object supplied; causes an error if the object doesn't exist &rarr;

</section>

<section markdown="block">
##  Some Exercises

* make the last element in a list the first element
* filter a list of strings
* average
</section>

<section markdown="block">
##  Make the First Element Last

* define a function called last_to_first
* it should take a list as an argument
* it should return a new list with the last element as the first element... and every element shifted up one 
	* last_to_first([1, 2, 3, 4] &rarr;
* if there's one element or less in the list, return the list as is
* use at least 3 assertions to test your last_to_first function
* try with just slicing and addition
* or try using pop and insert
</section>

<section markdown="block">
##  Make the First Element Last Solution v1

<pre><code data-trim contenteditable>
{% include classes/19/last_to_first.py %}
</code></pre>
</section>

<section markdown="block">
##  Make the First Element Last Solution v2

<pre><code data-trim contenteditable>
{% include classes/19/last_to_first_pop_insert.py %}
</code></pre>
</section>



<!--

<section markdown="block">
##  [Lists, Strings, and Random ](lists_strings_random.html)
</section>

-->
