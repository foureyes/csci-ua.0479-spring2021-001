---
layout: slides
title: Dictionaries Review 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##   Data Structures

Python has a few types of data or data structures that we've seen in the past.  Name some types...

<div class="fragment" markdown="block">
* int
* float
* str
* list
* tuple
</div>
</section>

<section markdown="block">
##  Which Data Structure do I Use? 

__What data structure would I use for the following scenarios?__

1. I have to store lyrics to a song (a bunch of text)
2. I have a coordinate that has two values: 0 for x,  0 for y. I want to keep the two values related, and I want to make sure it can't be modified.
3. I have bunch of todos that I have to keep track of.  I'd like to be able to add and remove items from it. 

<div class="fragment" markdown="block">
1. str
2. tuple
3. list
</div>
</section>

<section markdown="block">
##  Another Data Type

We have another data structure to add to our tool set - a __dictionary__  

* great if you have to associate a piece of data with a name
* or if you don't know how many or what kind of variables you'll need
* or if you need to be able to quickly 'look up' values using arbitrary keys
</section>

<section markdown="block">
##   Dictionaries

__In Python, what's a dictionary?  Describe some characteristics of a dictionary.__ &rarr;

<div class="fragment" markdown="block">
* a __dictionary__ is another kind of __compound data structure__ in Python (much like lists, strings and tuples)!
* it's an __unordered__ collection of __key__/__value__ pairs
* it's a __mutable__ object
</div>
</section>

<section markdown="block">
##   Dictionary Syntax

* __What delimits dictionaries?__ &rarr;  
* __What separates each key/value pair?__ &rarr;  
* __What separates a key from a value?__ &rarr;

<div class="fragment" markdown="block">
* dictionaries are delimited by curly braces - __{__ and __}__
* each key value pair in a dictionary is separated by a __comma__
* keys and values are linked together by a __colon__, the key before and the value after
* {"key":"value"}
</div>
</section>

<section markdown="block">
##   Dictionary Syntax

In the following dictionary: 

* __What are the two keys - and their types?__ &rarr;
* __What are the two values - and their types?--__ &rarr;

<pre><code data-trim contenteditable>
{(1, 2):"hello", 100:['other', 'types']}
</code></pre>

<div class="fragment" markdown="block">
* keys
	* (1, 2) - tuple
	* 100 - int
* values
	* "hello" - str
	* ['other', 'types'] - list
</div>
</section>

<section markdown="block">
##  Keys and Values

* List indexes can only be ints  __What kind of values can dictionary keys be?__ &rarr;
* __What about dictionary values?__ &rarr;

<div class="fragment" markdown="block">
* __keys__ - any immutable type, such as strings or tuples (or even ints)
* __values__ - can be any value... including other dictionaries!
</div>
</section>

<section markdown="block">
##  Retrieving Values at Keys 

How do you retrieve a value at a key from a dictionary? __Here's a dictionary; get the value 4__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"car", "wheels":4}
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
vehicle['wheels']
</code></pre>
</div>
</section>

<section markdown="block">
##  Non-Existent Keys

What happens if the key doesn't exist? __What happens in the following code?__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"car", "wheels":4}
vehicle['can fly']
</code></pre>

<div class="fragment" markdown="block">
A __KeyError__ occurs!

<pre><code data-trim contenteditable>
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
KeyError: 'can fly'
</code></pre>
</div>
</section>

<section markdown="block">
##  However!  Non-Existent Keys Continued...

How do you add a new key/value pair to an existing dictionary? __Add the key 'can fly' to this dictionary, and set its value to the boolean value, False__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"car", "wheels":4}
</code></pre>
<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
vehicle['can fly'] = True
</code></pre>
</div>
</section>

<section markdown="block">
##  If the Key Does Exist

If the key already exists, using the assignment operator overwrites the existing value at that key. 

__What does this code output?__&rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"car", "wheels":4}
vehicle['name'] = 'wagon'
print(vehicle)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{'wheels': 4, 'name': 'wagon'}
</code></pre>
</div>
</section>

<section markdown="block">
##  A Quick Summary on Keys

* dictionary __keys__ must be immutable
* you can use __indexing__ to retrieve values with keys - d['key']
* __retrieving__ an element at a key that doesn't exist __causes an error__
* __assigning__ a value to an element that doesn't exist __creates a new key/value pair__
</section>

<section markdown="block">
##  Some Other Dictionary Operations

There are some familiar operations and functions that we can use on dictionaries:

* __del__ - removes a key value pair
<pre><code data-trim contenteditable>
del d['some key']
</code></pre>

* __in__ - checks if a key exists in a dictionary
<pre><code data-trim contenteditable>
if 'some key' in d:
</code></pre>

* __len__ - finds the number of key/value pairs in a dictionary 
<pre><code data-trim contenteditable>
len(d)
</code></pre>
</section>

<section markdown="block">
##  Dictionary Methods

__Name the two dictionary methods that we learned, and describe what they do__ &rarr;

<div class="fragment" markdown="block">
* __get__(key, default) - retrieves an element at key; returns default if key doesn't exist
* __items__() - returns key/value pairs as list of tuples
</div>
</section>

<section markdown="block">
##  get

Soooo... __what does the get method do again, what are its arguments, and what does it return?__ &rarr;

<div class="fragment" markdown="block">
* __key__ - the key that you're trying to retrieve
* __default__ - the default value that you get if the key doesn't exist
* __get__ either returns the value at __key__ or returns __default__ if key doesn't exist
* useful for avoiding a __KeyError__ 
</div>

</section>

<section markdown="block">
##  Using the get Method

__What does this output?__

<pre><code data-trim contenteditable>
vehicle = {"name":"hovercraft"}
number_of_wheels = vehicle.get('wheels', 0)
name_of_vehicle = vehicle.get('name', 'bathysphere') 
print(number_of_wheels)
print(name_of_vehicle)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
0
hovercraft
</code></pre>
</div>
</section>

<section markdown="block">
##  More Dictionary Methods

By the way, here are a few more dictionary methods:

* __values__() - get all values as a list-like structure
* __keys__() - get all keys as a list-like structure (
* __pop__(k, [d]) - removes element at key, _k_, and returns it (returns _d_ if _k_ doesn't exist)
* __popitem__() - removes and returns _some_ name/value pair as tuple
* __update__(dictionary) - overwrites all values at keys in original with values at keys from dictionary passed in
</section>

<section markdown="block">
##  values, keys

__values__ and __keys__ give back _dictionary views_ (they essentially act like lists) of either all values or all keys of the dictionary that they're called on.  __What does this output?__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
print(vehicle.keys())
print(vehicle.values())
</code></pre>

<div class="fragment" markdown="block">
Note that the __order of the keys and values cannot be guaranteed!__
<pre><code data-trim contenteditable>
dict_keys(['can fly', 'wheels', 'name'])
dict_values([False, 0, 'bathysphere'])
</code></pre>
</div>
</section>

<section markdown="block">
##  pop

__pop__ removes and returns the item at the key specified.  __What does this output?__&rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
result1 = vehicle.pop('can fly')
result2 = vehicle.pop('floats', False)
print(result1)
print(result2) 
print(vehicle)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
False
False
{'wheels': 0, 'name': 'bathysphere'}
</code></pre>
</div>
</section>

<section markdown="block">
##  popitem

__popitem__ removes and returns an _arbitrary_ key/value pair.  __What does this output?__&rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
result1 = vehicle.popitem()
print(result1)
print(vehicle)
</code></pre>

<div class="fragment" markdown="block">
Note that the key/value pair removed and returned __will not always be the same!__

<pre><code data-trim contenteditable>
('can fly', False)
{'wheels': 0, 'name': 'bathysphere'}
</code></pre>
</div>
</section>

<section markdown="block">
##  update

__update__ adds key/value pairs (or updates values if keys already exist) from another dictionary to the dictionary that update is called on.  __What does this output?__&rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
another_vehicle = {'can float':True, 'name':'boat'}
vehicle.update(another_vehicle)
print(vehicle)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{'can fly': False, 'wheels': 0, 'name': 'boat', 'can float': True}
</code></pre>
</div>
</section>


<section markdown="block">
##  Changing a Value Based on the Existing Value

To change a value base on an existing value, such as incrementing a number, you can simply do something like this (adds one to the current value at fga):

<pre><code data-trim contenteditable>
d = {'fgm':1, 'fga':2}
d['fga'] = d['fga'] + 1
</code></pre>

</section>

<section markdown="block">
##  Changing a Value Based on the Existing Value

But what if it doesn't exist yet?  __What happens here?__ &rarr;

<pre><code data-trim contenteditable>
d = {'fgm':1 }
d['fga'] = d['fga'] + 1
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
KeyError: 'fga'
</code></pre>
</div>
</section>

<section markdown="block">
##  Avoiding KeyError

__What are a couple of ways of working around incrementing a value at a key when there may be keys that don't exist?__ &rarr;

<div class="fragment" markdown="block">
Use __exception handling__ or use __get__ and take advantage of assignment using keys that don't exist.

<pre><code data-trim contenteditable>
try:
	d['a'] += 1
except KeyError:
	d['a'] = 1

d['a'] = d.get('a', 0) + 1
</code></pre>
</div>
</section>

<section markdown="block">
##  Dictionaries and Mutability

__Dictionaries are mutable!__

* assignment works for changing values at keys
* keys/values can be added and removed
* note that many dictionary methods actually change the dictionary in place

__What are some dictionary methods that change the dictionary in place?__ &rarr;

<div class="fragment" markdown="block">

* pop
* popitem
* update
</div>
</section>

<section markdown="block">
##  Iterating Over Dictionaries

__What does this code print out?__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
for attribute in vehicle:
  print(attribute)
</code></pre>
<div class="fragment" markdown="block">

Note that __same order cannot be guaranteed__
<pre><code data-trim contenteditable>
can fly
wheels
name
</code></pre>
</div>
</section>

<section markdown="block">
##  Iterating Over Dictionaries Continued

We can see that iterating over a dictionary gives back keys.  Additionally, the keys are unordered. __How would be get every key *and* value using the dictionary below?__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
</code></pre>

<div class="fragment" markdown="block">
Use the key that you get from looping key to index into the dictionary, or use get.

<pre><code data-trim contenteditable>
for attribute in vehicle:
  print('%s, %s' % (attribute, vehicle[attribute]))
</code></pre>
</div>
</section>

<section markdown="block">
##  Back to the items Method!

A dictionary can be converted to a list of tuples using the __items__() method.  

* it returns a list like object of tuples 
* each tuple has two elements
* the first element is the key, and the second, the value  

__What does the code below output?__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"hovercraft", "wheels":0}
pairs = vehicle.items()
for pair in pairs:
	print(pair)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
('wheels', 0)
('name', 'hovercraft')
</code></pre>
</div>
</section>

<section markdown="block">
##  Iterating Over Dictionaries Continued

__What's another way of looping over a dictionary to get keys and values without having to index into the original dictionary?__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"hovercraft", "wheels":0}
</code></pre>

<div class="fragment" markdown="block">
Use __tuple unpacking__! within your for-loop.

<pre><code data-trim contenteditable>
pairs = vehicle.items()
for k, v in pairs:
	print('%s, %s' % (k, v))
</code></pre>
</div>
</section>

<section markdown="block">
##  Some Quick Questions

* name as many dictionary methods as you can!
* name two ways of accessing a value at a key
* how do you create an empty dictionary?
* are dictionaries mutable or immutable?
* are dictionaries ordered or unordered
* how do you add a new key/value pair to an existing dictionary?
* name 3 ways of removing items from a dictionary
</section>

<section markdown="block">
##  And Their Answers

* pop, popitem, get, keys, values, update, etc.
* __indexing__ with a __key__ or using __get__
* and empty dictionary is __{}__
* dictionaries are __mutable__
* dictionaries are __unordered__
* use assignment on key that doesn't exist
* use __del__, __pop__ or __popitem__
</section>
