---
layout: slides
title: "Dictionaries"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Dictionaries

__What's a dictionary?__

* {:.fragment} a __dictionary__ is an __unordered__ collection of key/value pairs.  
* {:.fragment} it's a __mapping type__ - a data type that made of a collection of keys (think of names) and their associated values
</section>

<section markdown="block">
##  Dictionaries Syntax

__What's the syntax for a dictionary literal?  What delimits dictionaries?  What separates each name value pair?  What joins each name to a value?__

* dictionaries are delimited by curly braces - { and }
* an empty dictionary is {}
* each key value pair in a dictionary is separated by a comma
* keys and values are linked together by a colon, the key before and the value after
* an example: 
{:.fragment}

<pre><code data-trim contenteditable>
{"a":"value one", "b":2}
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Retrieving Values at Keys 

__How do you retrieve a value at a key from a dictionary?  What happens if the key doesn't exist?__

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms"}
print(pizza["topping"])
print(pizza["extra topping"])
</code></pre>

<pre><code data-trim contenteditable>
mushrooms
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
KeyError: 'extra topping'
</code></pre>
{:.fragment}

[btw, pizza!](http://www.pizzabrain.org/about-pizza-brain/)
{:.fragment}
</section>


<section markdown="block">
## Using the get Method

You can also retrieve a value from a dictionary without having to worry about KeyErrors by calling the __get__ method with two arguments:

* the key of the element you want to retrieve
* an optional default value in case that key doesn't exist yet

__What does this output?__

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms"}
print(pizza.get("extra topping", "peppers")
</code></pre>

<pre><code data-trim contenteditable>
peppers
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Key/Value Pairs 

So... things are a bit different when _adding_ keys and values to a dictionary.  There is __no error__ if you use a key that doesn't exist in order to assign a value to it (that is... to create a new key/value pair).

<pre><code data-trim contenteditable>
# look ma, no keys!
d = {}
# but I can assign with no probz
d["problems"] = None
d["another key"] = "another value"
</code></pre>
</section>

<section markdown="block">
## Key/Value Pairs Continued

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


<pre><code data-trim contenteditable>
something
None
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Creating New Keys/Values

__So.... how do you create a new key/value pair in a dictionary?__ &rarr;


* {:.fragment} you can assign a new value to a new key simply by indexing into a key that doesn't exist!
* {:.fragment} this is different from reading from a key that doesn't exist (which gives us a KeyError)
* {:.fragment} __for example...__ &rarr;

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms"}
pizza['sauce'] = 'tomato'
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## Setting a New Key or Incrementing an Existing

If you're storing numbers as key values, and you want to increment a value at key or initialize it to 1 if it doesn't exist...

<pre><code data-trim contenteditable>
d['a'] += 1
# ...but I don't know if a exists
</code></pre>

You can catch an exception, or use get

<pre><code data-trim contenteditable>
try:
	d['a'] += 1
except KeyError:
	d['a'] = 1

d['a'] = d.get('a', 0) + 1
</code></pre>
</section>

<section markdown="block">
## Dictionaries and Mutability

__Are dictionaries mutable or immutable?__

Dictionaries are __mutable__!
{:.fragment}

<pre><code data-trim contenteditable>
d = {}
d["did not exist before"] = "some value"
# ok!
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## We Can Iterate Over Dictionaries

__Let's run this code.  What would you expect this to print?  Does it match what actually happens?__

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}
for topping in pizza:
  print(topping)
</code></pre>

<pre><code data-trim contenteditable>
sauce
topping
crust
size
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Iterating Over Dictionaries Continued

__What can we conclude about dictionaries and iteration bsed on the output from the previous slides?__ &rarr;

* {:.fragment} iterating over a dictionary yields __keys only__
* {:.fragment} again, dictionaries are __unordered__!
</section>

<section markdown="block">
## Iterating Over Every Key and Value

Another common way of iterating over a dictionary is to convert it to a list of tuples using the __items__() method.  It returns a list like object of tuples w/ the first element in each tuple the key, and the second, the value.  __What does the code below output?__

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms"}
t = pizza.items()
for i in t:
	print(i)
</code></pre>

<pre><code data-trim contenteditable>
('topping', 'mushrooms')
('crust', 'thin')
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Iterating Over Dictionaries Continued

__Of course, we can unpack those tuples.  How do we rewrite this using tuple unpacking?__

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms"}
t = pizza.items()
for i in t:
	print(i)
</code></pre>

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms"}
t = pizza.items()
for k, v in t:
	print(k, v)
</code></pre>
</section>

<section markdown="block">
## Order!

__Remember that the dictionaries are _unorderd_...__

That means that when you iterate over elements, order isn't guaranteed

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms", "sauce":"tomato"}
t = pizza.items()
for k, v in t:
	print(k, v)
</code></pre>

<pre><code data-trim contenteditable>
# sometimes it'll be in the original order... or not!
sauce tomato
topping mushrooms
crust thin
</code></pre>
</section>

<section markdown="block">
## sorted

So... we saw a built-in function before called __sorted__...

* it takes an iterable as an argument (dictionary, list, string, tuple)
* and it returns a sorted list version of the original argument
* there's an optional second argument which is the _actual function_ to use on each element for sorting, the keyword argument, <code>key</code> (just like <code>max</code> and <code>min</code>)

</section>

<section markdown="block">
## sorted on Dictionary Values

We can use __sorted__ to iterate over a dictionary (which is inherently unordered) by value. 

* __sorted__ will look at a dictionaries keys only
* sooo <code>sorted(d)</code> will give back a sorted list of keys
* and <code>sorted(d, key=d.get)</code> will give back a list of keys sorted by their corresponding value!

<pre><code data-trim contenteditable>
pg = {"Ricky Rubio":12, "Derrick Rose":9, "Steve Nash":15}
for name in sorted(pg, key=pg.get):
	print(name, pg[name])
</code></pre>

Notice that the key is actually the get method in the dictionary! __This means that the value used for sorting is the value returned by retrieving the element at each key of the dictionary__.
</section>

<section markdown="block">
## BTW, in and len()

__The in and not in operators work with dictionary keys; len() gives back the number of key/value pairs__ &rarr;

<pre><code data-trim contenteditable>
pizza = {"crust":"thin", "topping":"mushrooms", 'size':'large', 'sauce':'tomato'}
print(len(pizza))
# prints out 4

result = 'crust' in pizza
print(result)
# prints out True
</code></pre>
</section>

<section markdown="block">
## Dictionary Methods

__Besides <code>get()</code> and <code>items()</code>, there are a bunch of other dictionary methods... here are some of them:__ &rarr;

* __values__() - get all values as a list-like structure
* __keys__() - get all keys as a list-like structure (
* __pop__(k, [d]) - removes element at key, _k_, and returns it (returns _d_ if _k_ doesn't exist)
* __popitem__() - removes and returns _some_ name/value pair as tuple
* __update__(dictionary) - overwrites all values at keys in original with values at keys from dictionary passed in
</section>

<section markdown="block">
## values, keys

__values__ and __keys__ give back _dictionary views_ (they essentially act like lists) of either all values or all keys of the dictionary that they're called on.  __What does this output?__ &rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
print(vehicle.keys())
print(vehicle.values())
</code></pre>

Note that the __order of the keys and values cannot be guaranteed!__
{:.fragment}

<pre><code data-trim contenteditable>
dict_keys(['can fly', 'wheels', 'name'])
dict_values([False, 0, 'bathysphere'])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## pop

__pop__ removes and returns the item at the key specified.  __What does this output?__&rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
result1 = vehicle.pop('can fly')
result2 = vehicle.pop('floats', False)
print(result1)
print(result2) 
print(vehicle)
</code></pre>

<pre><code data-trim contenteditable>
False
False
{'wheels': 0, 'name': 'bathysphere'}
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## popitem

__popitem__ removes and returns an _arbitrary_ key/value pair.  __What does this output?__&rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
result1 = vehicle.popitem()
print(result1)
print(vehicle)
</code></pre>

Note that the key/value pair removed and returned __will not always be the same!__
{:.fragment}

<pre><code data-trim contenteditable>
('can fly', False)
{'wheels': 0, 'name': 'bathysphere'}
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## update

__update__ adds key/value pairs (or updates values if keys already exist) from another dictionary to the dictionary that update is called on.  __What does this output?__&rarr;

<pre><code data-trim contenteditable>
vehicle = {"name":"bathysphere", "wheels":0, "can fly":False}
another_vehicle = {'can float':True, 'name':'boat'}
vehicle.update(another_vehicle)
print(vehicle)
</code></pre>


<pre><code data-trim contenteditable>
{'can fly': False, 'wheels': 0, 'name': 'boat', 'can float': True}
</code></pre>
{:.fragment}
</section>



<section markdown="block">
## Some Questions

* how do we construct a dictionary literal?
* how do we create an empty dictionary?
* are dictionaries mutable or immutable?
* are dictionaries ordered or unordered
* how do we access a value at a key... what happens if they key doesn't exist?
* what's the exception to the above?
* what's another way of accessing a value?
* when we us a regular for loop with a dictionary, what value is in the for loop variable?
* how do we get both keys and values when iterating?
</section>

<section markdown="block">
## Aaand Answers

* dictionaries are delimited by curly braces, key value pairs are separated by commas, with each key and value joined by a colon
* {}
* they're __mutable__
* __unordered__ - order cannot be guaranteed
* d["some key"], exception
* assignment
* get method
* the current key
* convert to a list of tuples using __items__()
</section>


<section markdown="block">
## Dictionaries Exercise

* write a program that asks the user for a word
* the program should output the total number of times each character in the word appears in the word
* example output:

<pre><code data-trim contenteditable>
>hello
h 1
e 1
l 2
o 1
</code></pre>
</section>

<section markdown="block">
## Counting Letters By Checking for Key

__Check to see if the key exists first (using <code>in</code>; if it does, increment... otherwise, create a new key value pair!__ &Rarr;

<pre><code data-trim contenteditable>
word = input("Enter a word\n>")
d = {}
for c in word:
    if c in d:
        d[c] += 1
    else::
        d[c] = 1
for k,v in d.items():
    print(k, v)
</code></pre>
</section>

<section markdown="block">
## Counting Letters Using Try/Except

__Use try/except ... similar to the previous version, but here, we rely on a KeyError to determine whether or not we should increment at a key or create a new key value pair.__ &rarr;

<pre><code data-trim contenteditable>
word = input("Enter a word\n>")
d = {}
for c in word:
    try:
        d[c] += 1
    except KeyError:
        d[c] = 1
for k,v in d.items():
    print(k, v)
</code></pre>
</section>
<section markdown="block">
## Counting Letters Using Get

__If the key doesn't exist, create a new key value pair with the value as 0... otherwise set the value at the key to the current value + 1)__ &rarr;

<pre><code data-trim contenteditable>
word = input("Enter a word\n>")
d = {}
for c in word:
	d[c] = d.get(c, 0) + 1
for k,v in d.items():
	print(k, v)
</code></pre>

</section>
<section markdown="block">
## Counting Letters Without a Dictionary

Of course, you don't _really_ need a dictionary to do this, but it's a bit inefficient, right?

<pre><code data-trim contenteditable>
word = input("Enter a word\n>")
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
    count = word.count(c)
    if count > 0:
        print(c, count)
</code></pre>
</section>


<section markdown="block">
## Counting Dice Rolls 

* roll two thee sided dice simultaneously 1000 times
* count the frequency of the results... 2 through 6
* pseudocode
	* generate two random numbers
	* do this 1000 times
	* keep track of the number of times a two is rolled... a three... up through six
	* use multiple assignment for initializing your counts!
</section>

<section markdown="block">
## Dice Rolls Solution 

Using a dictionary...and taking advantage of get:

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
## A Visualization with Matplotlib

__We can whip up a quick visualization with matplotlib using the following functions.__ &rarr;

* <code>plt.bar(left, height)</code>
    * <code>left</code> - sequence of x coordinates of left side of bars
    * <code>height</code> - heights of bars

* <code>plt.hist(inputarray, bins=bins)</code>
    * <code>inputarray</code> - sequence of data
    * <code>bins=bins</code> - number of bins or sequence of edges of bins

__To add some handy labels...__ &rarr;

* <code>plt.title("Dice Rolls")</code>
* <code>plt.xlabel("Roll")</code>
* <code>plt.ylabel("Frequency")</code>

</section>

<section markdown="block">
## Bar

__For a bar chart, we can pass in the keys (the possible roll numbers) as the x coordinates and the values as the height__ &rarr;

<pre><code data-trim contenteditable>
import matplotlib.pyplot as plt
import random
freq_dice_rolls = {}
for i in range(1000):
    roll = random.randint(1,3) + random.randint(1,3)
    freq_dice_rolls[roll] = freq_dice_rolls.get(roll, 0) + 1

plt.bar(freq_dice_rolls.keys(), freq_dice_rolls.values() )
plt.title("Dice Rolls")
plt.xlabel("Roll")
plt.ylabel("Frequency")
plt.show()
</code></pre>
</section>

<section markdown="block">
## Histogram

__The histogram will calculate the totals for each roll for us, so just pass it all of the actual list of all elements.__ &rarr;

<pre><code data-trim contenteditable>
import matplotlib.pyplot as plt
import random
rolls = []
for i in range(1000):
    rolls.append(random.randint(1,3) + random.randint(1,3))

plt.hist(rolls, bins=[2, 3, 4, 5, 6, 7])
plt.title("Dice Rolls")
plt.xlabel("Roll")
plt.ylabel("Frequency")
plt.show()
</code></pre>
</section>

<section markdown="block">
## Max

You can actually use max with a dictionary to find the key/value pair that has the highest value.

__Specify the key as d.get to tell Python that the values to compare are the values at a particular key.__ &rarr;

<pre><code data-trim contenteditable>
>>> d = {'b':24, 'c':1, 'z':15, 'h':21, 'm':100, 'y':50}
>>> d
{'y': 50, 'z': 15, 'h': 21, 'b': 24, 'c': 1, 'm': 100}
>>> max(d)
'z'
>>> max(d, key=d.get)
'm'
>>> max(5, -10, 24)
24
>>> max(5, -10, 24, key=abs)
24
>>> max(5, -10, 24, -50, key=abs)
-50
>>> def f(x):
...   return 1 / x;
...
>>> max(5, 10, 2, 1, key=f)
</code></pre>
</section>

{% comment %}
<section markdown="block">
## Dictionary Transcript

<pre><code data-trim contenteditable>
>>> d = {}
>>> d = {'name': 'joe'}
>>> d['name']
'joe'
>>> d = {'name': 'joe', 'last':'versoza'}
>>> d['last']
'versoza'
>>> d['middle']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'middle'
>>> d['middle'] = 'j'
>>> d
{'name': 'joe', 'middle': 'j', 'last': 'versoza'}
>>> 'is_hungry' in d
False
>>> result = d.get('is_hungry')
>>> print(result)
None
>>> result = d.get('name')
>>> result
'joe'
>>> result = d.get('is_hungry', True)
>>> result
True
>>> d
{'name': 'joe', 'middle': 'j', 'last': 'versoza'}
>>> d.keys()
dict_keys(['name', 'middle', 'last'])
>>> list(d.keys())
['name', 'middle', 'last']
>>> list(d.values())
['joe', 'j', 'versoza']
>>> list(d.items())
[('name', 'joe'), ('middle', 'j'), ('last', 'versoza')]
>>> for thing in d:
...   print(thing)
...
name
middle
last
>>> for thing in d:
...   print(d[thing])
...
joe
j
versoza
>>> for thing in d:
...   print(thing, d[thing])
...
name joe
middle j
last versoza
>>> for k, v in d.items():
...   print(k, v)
...
name joe
middle j
last versoza
>>> d.popitem()
('name', 'joe')
>>> d
{'middle': 'j', 'last': 'versoza'}
>>> d.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop expected at least 1 arguments, got 0
>>> d.pop('middle')
'j'
>>> d
{'last': 'versoza'}
>>> del d['last']
>>> d
{}
>>> d = {'foo': 'bar'}
>>> d['foo'] = 'qux'
>>> d
{'foo': 'qux'}
>>>
</code></pre>

</section>
{% endcomment %}
