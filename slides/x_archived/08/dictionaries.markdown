---
layout: slides
title: Dictionaries 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##   Counting Frequency of Dice Rolls

* roll two thee sided dice simultaneously 1000 times
* (they exist!  what do you think they [look like](http://suptg.thisisnotatrueending.com/archive/14752803/images/1304091112226.jpg)? 
* count the frequency of the results... 2 through 6
* __let's code that up really quickly__
	* generate two random numbers
	* do this 1000 times
	* keep track of the number of times a two is rolled... a three... up through six
	* use multiple assignment for initializing your counts!
</section>

<section markdown="block">
##  Dice Rolls Solution 
<pre><code data-trim contenteditable>
import random
twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	if roll == 2:
		twos += 1
	if roll == 3:
		threes += 1
	if roll == 4:
		fours += 1
	if roll == 5:
		fives += 1
	if roll == 6:
		sixes += 1

print("twos: %s, threes: %s, fours: %s, fives: %s, sixes %s" % (twos, threes, fours, fives, sixes)) 
</code></pre>
</section>


<section markdown="block">
##  Dice Rolls 

Whew!

That was a long if-else.  What if we had to write one for two twenty-sided dice?  

* that would be pretty lengthy
* and consequently error prone

If there were only a way to dynamically create names and associate values to them.

We'll get to that in a second.  First: __compound types, mapping types and dictionaries__...
</section>

<section markdown="block">
##   Revisiting Compound Types

__Compound types__: values that are made up of other values.  

Sequence types are compound types.  We know three sequence types.  __What are they?__

<div class="fragment" markdown="block">
1. string
2. list
3. tuple
</div>
</section>

<section markdown="block">
##   Mapping Types

Another kind of compound type is a mapping type.  

A __mapping type__ is a data type that is made of a collection of keys (think of names) and their associated values.  The only mapping type in Python is a __dictionary__.
</section>

<section markdown="block">
##   Dictionaries

A __dictionary__ is an __unordered__ collection of key/value pairs.  

* __key__ is an item that is used to _look up_ values in a dictionary; think of keys as names or labels.
* keys must be immutable objects (they're usually strings or ints)
* the values that are associated with keys can be any type!
* in other languages dictionaries are called associative arrays or hash tables 
</section>

<section markdown="block">
##   Dictionaries Syntax

Let's take a look at some examples

<pre><code data-trim contenteditable>
{"first_name":"joe", "fav_candy":"cleo's"}
{28:"foo", 6:"bar", "entirely different":["baz"]}
{}
</code></pre>

* dictionaries are delimited by curly braces - { and }
* an empty dictionary is {}
* each key value pair in a dictionary is separated by a comma
* keys and values are linked together by a colon, the key before and the value after

(btw, [cleo's are pretty good](http://www.godairyfree.org/wp-content/uploads/2012/11/gomaxgocleo.jpg))
</section>

<section markdown="block">
##   Dictionaries Syntax Continued

__What are the keys and what type are they? What are the values and what type are they?__
<pre><code data-trim contenteditable>
d1 = {"first_name":"joe", "fav_candy":"cleo's"}
d2 = {28:"foo", 6:"bar", "entirely different":["baz"]}
</code></pre>

<div class="fragment" markdown="block">
* d1
	* keys - the strings "first_name" and "fav_food"
	* values - the strings "joe" and "cleo's"
* d2
	* keys - the ints 28 and 6 ...and the string "entirely different" 
	* values - the strings "foo" and "bar" ... and the list ["baz"]
</div>
</section>

<section markdown="block">
##  Retrieving Values at Keys 

You can use the key like a list index to retrieve a value at that key.  __What does this code print out?__

<pre><code data-trim contenteditable>
d = {"first_name":"joe", "fav_candy":"cleo's"}
print(d["first_name"])
print(d["fav_candy"])
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
joe
cleo's
</code></pre>
</div>

</section>

<section markdown="block">
##  Keys That Don't Exist!

Let's try that again... but with a key that doesn't exist.  __What do you think will happen here?__

<pre><code data-trim contenteditable>
d = {"first_name":"joe", "fav_candy":"cleo's"}
print(d["height"])
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
KeyError: 'height'
</code></pre>
</div>
</section>

<section markdown="block">
##  Retrieval Using the get Method

You can also retrieve a value from a dictionary by calling the __get__ method.  __get__ takes two arguments:

* the key of the element you want to retrieve
* an optional default value in case that key doesn't exist yet

__What do you think this code outputs?__

<pre><code data-trim contenteditable>
d = {"first_name":"joe", "fav_candy":"cleo's"}
print(d.get("height", None))
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
None
</code></pre>
</div>
</section>

<section markdown="block">
##  Key/Value Pairs 

So... things are a bit different when adding keys and values to a dictionary.  There is __no error__ if you use a key that doesn't exist in order to assign a value to it (that is... to create a new key/value pair).

<pre><code data-trim contenteditable>
#  look ma, no keys!
d = {}
#  but I can assign with no probz
d["problems"] = None
d["another key"] = "another value"
</code></pre>
</section>

<section markdown="block">
##  Key/Value Pairs Continued

If the key already exists... and you use the assignment operator, you are just associating a new value with an existing key.

__What does this code output?__

<pre><code data-trim contenteditable>
d = {}
d["another key"] = "another value"
d["problems"] = None
d["another key"] = "something"
print(d["another key"])
print(d["problems"])
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
something
None
</code></pre>
</div>
</section>

<section markdown="block">
##  Dictionaries and Mutability

Based on what we've seen so far... __are dictionaries mutable or immutable?__

<div class="fragment" markdown="block">
Dictionaries are __mutable__!

<pre><code data-trim contenteditable>
d = {}
d["did not exist before"] = "some value"
#  ok!
</code></pre>
</div>
</section>

<section markdown="block">
##  We Can Iterate Over Dictionaries

__Let's run this code.  What would you expect this to print?  Does it match what actually happens?__

<pre><code data-trim contenteditable>
d = {"first_name":"joe", "fav_candy":"cleo's"}
for item in d:
  print(item)
</code></pre>
<div class="fragment" markdown="block">

<pre><code data-trim contenteditable>
#  we only get the keys!
fav_candy
first_name
</code></pre>
</div>
</section>

<section markdown="block">
##  Dictionary Views

Another way to iterate over a dictionary is to convert it to a special sequence called a __dictionary view__.

* the __items__() method returns a __dictionary view__ (another _iterable_ object)
* __each element in the view is a tuple__  
* the first element in each tuple the key, and the second, the value

__What type is the type of variable, i?  How many iterations are there?  What is the value of i at each iteration?__

<pre><code data-trim contenteditable>
d = {"first_name":"joe", "fav_candy":"cleo's"}
items = d.items()
for t in items:
	print(t)
</code></pre>

</section>

<section markdown="block">
##  Converting a Dictionary to a Bunch of Tuples 

<pre><code data-trim contenteditable>
d = {"first_name":"joe", "fav_candy":"cleo's"}
items = d.items()
for t in items:
	print(t)
</code></pre>

A few notes....

* items is a _list like_ value that contains tuples
* in the for loop, __t__ is always a __tuple__
* __2 iterations__, with t being a tuple that represents a name value pair 

</section>

<section markdown="block">
##  Iterating over a Dictionary Using items()

Now... we have a tuple... __how do we print out each key and value individually (how do we unpack again?)__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
d = {"first_name":"joe", "fav_candy":"cleo's"}
for k, v in d.items():
  print(k, v)
</code></pre>
</div>
</section>

<section markdown="block">
##  Dictionaries Are Unordered

Unlike sequence types like string, list or tuple, dictionaries are __unordered__.  That means that the order of the key value pairs cannot be guaranteed!  __Let's take a look.  Intuitively, what's the first thing that we think will be printed out?__

<pre><code data-trim contenteditable>
d = {"one":"foo", "two":"bar", 3:"baz"}
for k, v in d.items():
  print(k, v)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
#  this is actually just one possible ordering!
3 baz
two bar
one foo
</code></pre>
</div>
</section>

<section markdown="block">
##  in and len()

__The in and not in operators work with dictionary keys; len() gives back the number of key/value pairs__ &rarr;

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}
print(len(pizza))
#  prints out 4

result = 'crust' in pizza
print(result)
#  prints out True
</code></pre>
</section>


<section markdown="block">
##  Summary Questions

* how do we construct a dictionary literal?
* how do we create an empty dictionary?
* are dictionaries mutable or immutable?
* are dictionaries ordered or unordered
* how do we access a value at a key... what happens if they key doesn't exist?
* what's the exception to the above?
* what's another way of accessing a value?


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
##  Summary Answers

* dictionaries are delimited by curly braces, key value pairs are separated by commas, with each key and value joined by a colon
* {}
* they're mutable
* order cannot be guaranteed
* d["some key"], exception
* assignment
* get method

</section>


<section markdown="block">
##  Back to Dice!

__Try reimplementing our dice program so that it uses a dictionary to store the frequency of rolls (each roll as a key, each value as a count).__  (hint: use in, the get method or a try-except to deal with keys that don't exist).
<pre><code data-trim contenteditable>
import random
twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	if roll == 2:
		twos += 1
	if roll == 3:
		threes += 1
	if roll == 4:
		fours += 1
	if roll == 5:
		fives += 1
	if roll == 6:
		sixes += 1

print("twos: %s, threes: %s, fours: %s, fives: %s, sixes %s" % (twos, threes, fours, fives, sixes)) 
</code></pre>
</section>


<section markdown="block">
##  Dice Rolls Solution 
<pre><code data-trim contenteditable>
import random
freq_dice_rolls = {}
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	freq_dice_rolls[roll] = freq_dice_rolls.get(roll, 0) + 1
print(freq_dice_rolls)
</code></pre>
</section>

<section markdown="block">
##  Further Exercises

* counting letters
* counting letters, sorted keys
* run-length encoding
* storing inventory
</section>

