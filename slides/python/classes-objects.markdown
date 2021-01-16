---
layout: slides
title: "Named Tuples, Classes, and Objects"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>



</section>

<section markdown="block">
## Storing a 2-Dimensional Point

__What are some options for storing point on a 2D plane?__ (Imagine we had a point, (4, 2)... how would we represent it in our program?) &rarr;

* {:.fragment} two separate ints: 
    <pre><code data-trim contenteditable>x, y = 4, 2</code></pre>
* {:.fragment} a 2-element list or a 2-element tuple: 
    <pre><code data-trim contenteditable>p = [4, 2] 
p = (4, 2)
</code></pre>
* {:.fragment} a dictionary:
    <pre><code data-trim contenteditable> p = {'x':4, 'y':2] </code></pre>


</section>

<section markdown="block">
## Storing a Point...

All of the methods in the previous slide are usable depending on the situation. __However, there are definitely some drawbacks. ...What are they?__ &rarr;

* {:.fragment} dealing with entirely separate variables only really works for a handful of coordinates
* {:.fragment} ...and the bracket syntax for using dictionaries, lists and tuples is a bit cumbersome. 

__Let's check out another way of creating a point.__ &rarr;
{:.fragment}
</section>

<section markdown="block">
## Named Tuples

From [the official Python 3 docs](https://docs.python.org/2/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields)...

* "Named tuples assign meaning to each position in a tuple" 
* "...allow for more readable, self-documenting code" 
* "can be used wherever regular tuples are used"
* "... add the ability to access fields by name instead of position index"

Sounds pretty good. __Let's see this work.__ &rarr;

</section>
<section markdown="block">
## Defining Named Tuples


So... using __namedtuple__ in the __collections__ module, you can define a tuple with each position named based on your own specifications. The arguments that you pass to __namedtuple__ are:

1. __typename__  
2. __field_names__ 


<pre><code data-trim contenteditable>
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
</code></pre>

From here, you can use <code>Point</code> to create named tuples that have x and y values.
</section>

<section markdown="block">
## Creating Named Tuples

Creating a named tuple with keyword arguments.

<pre><code data-trim contenteditable>
>>> p = Point(x=0,y=0)
>>> p.x
0
>>> p.y
0
</code></pre>

Another way of creating a named tuple with positional arguments.

<pre><code data-trim contenteditable>
>>> q = Point(14, 16)
>>> q
Point(x=14, y=16)
</code></pre>

</section>

<section markdown="block">
## Named Tuples Continued

Accessing items

<pre><code data-trim contenteditable>
>>> q.x
14
>>> q[0]
14
</code></pre>

Unpacking

<pre><code data-trim contenteditable>
>>> x, y = q
>>> x
14
</code></pre>

Immutable!
<pre><code data-trim contenteditable>
>>> q[0] = 100
>>> // exception!
</code></pre>

</section>

<section markdown="block">
## What is Point _Exactly_?

__Let's see...__ &rarr;

<pre><code data-trim contenteditable>
>>> type(Point)
<class 'type'>
</code></pre>

It looks like we made our own type! Just like there are ints, floats, etc... now there's a Point type too...

<pre><code data-trim contenteditable>
>>> type(str)
<class 'type'>
>>> p = Point(2, 2)
>>> type(p)
<class '__main__.Point'>
</code></pre>

__SO MUCH POWER.__
</section>

<section markdown="block">
## More Detail

__Let's break down what happened when we created Point.__ &rarr;

<pre><code data-trim contenteditable>
>>> Point = namedtuple('Point', ['x', 'y'])
</code></pre>

* <code>namedtuple</code> actually returns a __new type__! (like <code>str</code>, <code>int</code>, etc.)
* the __type's name__ is the argument that's passed in, <code>'Point'</code>
* the __variable name__, <code>Point</code>, is bound to the new type that we create... so we can use it to create <code>Point</code> objects (just like we can use <code>list</code> to create lists or <code>str</code> to create strings)

Note that it doesn't matter what we name the variable; the type still remains <code>'Point'</code> (the first argument)

<pre><code data-trim contenteditable>
>>> Foo = namedtuple('Point', ['x', 'y'])
>>> q = Foo(9, 10)
>>> type(q)
<class '__main__.Point'>
</code></pre>
</section>

<section markdown="block">
## If You Liked Named Tuples...

Ok... so named tuples are pretty nice tool. Buuuuut: 

* they're still just tuples, so they're immutable
* and you're stuck with the methods (functions) that are already defined on tuples

Another option that we have is to use __classes__, which are basically a fancier way of saying type.

</section>

<section markdown="block">
## First... about Types and Objects

__What's an object?__ &rarr;

* {:.fragment} an object is just some data or _state_...
* {:.fragment} along with the actions that can be performed with that data
* {:.fragment} for example, <code>"hello"</code> is a string object (the data is a sequence of characters), and ask that object to give you an uppercase version of itself, an action: <code>"hello".upper()</code>

__Great... so why do we care about what the type of an object is?__ &rarr;
{:.fragment}

* {:.fragment} type determines what we can and can't do with an object
* {:.fragment} ...such as what operations are valid
* {:.fragment} ...and what methods you can call on it

</section>
<section markdown="block">
## Classes and Objects

In Python, the words __type__ and __class__ can be used synonymously. We just saw one way to declare a new type by using a named tuple.

__Another way to declare a new type is to declare a new class.__

* start with the keyword <code>class</code>
* followed by the name of your new type
* and an indented block of code that outlines the actions / behaviors / methods (as well as data) that can be used by objects created from your new type

<pre><code data-trim contenteditable>
# we're creating a new type, a Cat!
class Cat:
    # methods (actions) go here
    pass
</code></pre>
</section>


<section markdown="block">
## Using a Class

With this simple class definition, __we can already start creating objects__ (they won't _do much_, but their type exists!)...

<pre><code data-trim contenteditable>
class Cat:
    pass

obj = Cat()
print(type(obj))
# <class '__main__.Cat'>
</code></pre>

As you can see, using the class name as we were calling a function creates a new _Cat_ object.

The creation of new objects from a class is __instantiation__. (We're creating an instance of class <code>Cat</code>)
</section>

<section markdown="block">
## Where's the Data? 

So, our <code>Cat</code> class is pretty bare bones. __Maybe we want to specify that every new <code>Cat</code> that we create should have a name and a cuteness factor__. We can do this by explicitly creating a __constructor__ method.

A __constructor__ method determines what happens when an object is created. Define a constructor by making a function called <code>__init__</code> that takes a single argument, self. You can define additional arguments as well.

<pre><code data-trim contenteditable>
&nbsp;   def __init__(self, other_argument):
</code></pre>

__self__ refers to the new object that the constructor will create. You can add data to the __self__ object by using the dot operator and assignment.

<pre><code data-trim contenteditable>
&nbsp;       self.some_data = other_argument
        self.foo = "bar"
</code></pre>
</section>

<section markdown="block">
## Constructors

Here's a version of our <code>Cat</code> class with a constructor that requires specifying a cat name and a cuteness factor when creating a new cat:

<pre><code data-trim contenteditable>
class Cat:
    def __init__(self, name, cuteness_factor):
        self.name = name
        self.cuteness_factor = cuteness_factor

# create a new cat named Paw Newman, with cuteness factor, 10
c = Cat('Paw Newman', 10)
</code></pre>

This means that we __always__ have to pass in the same number of arguments as the constructor (minus self). Consequently, this would not work with our constructor:

<pre><code data-trim contenteditable>
c = Cat('Bill Furry') # ERROR!
</code></pre>

</section>

<section markdown="block">
## Accessing an Object's Data

Once you have an object, you can access it's data / _state_ by using the dot operator and the name of the data you'd like access.

In our previous example, we had a new <code>Cat</code> object.

<pre><code data-trim contenteditable>
c = Cat('Paw Newman', 10)
</code></pre>

We can check out our cat's name and cuteness factor by:

<pre><code data-trim contenteditable>
print(c.name)
print(c.cuteness_factor)
</code></pre>

</section>

<section markdown="block">
## Defining Methods

__We can also define actions that our cat can perform.__ It's essentially like defining a function, but within a class... aaaand __the first argument should be self if you want to be able to call it on an instance__:


<pre><code data-trim contenteditable>
class Cat:
    def __init__(self, name, cuteness_factor):
        self.name = name
        self.cuteness_factor = cuteness_factor
    def meow(self, how_loudly):
        print("{} meows{}".format(self.name, how_loudly * '!'))

c = Cat('Paw Newman', 10)
c.meow(5)
# Paw Newman meows!!!!!
</code></pre>
</section>

<section markdown="block">
## Defining Methods Continued

__Let's take a closer look at defining methods...__ &rarr;

* again, to define a method, create it within the class definition you'd like to add it to
* __the first argument is always self__ if you want to be able to call the method on an _instance_ of your class (which is typically what you want to do)
* note that self refers to the _instance_ that the method is being called on... so for our cat, <code>Paw Newman</code>... <code>self.name</code> is <code>Paw Newman</code>

<pre><code data-trim contenteditable>
&nbsp;    def meow(self, how_loudly):
        print("{} meows{}".format(self.name, how_loudly * '!'))
</code></pre>

</section>

<section markdown="block">
## Getters / Setters

Although we can access data in our objects using the dot operator, a __typical pattern__ when creating classes is to __mediate access__ to this data using __"accessor and mutator" methods__, or methods that get and set an object's data.

For example, __instead of accessing data directly, we can use the following getters__ &rarr;

<pre><code data-trim contenteditable>
&nbsp;   def get_name(self):
        return self.name

    def get_cuteness_factor(self):
        return self.cuteness_factor
</code></pre>
</section>

<section markdown="block">
## Why Getters and Setters

__Um. Why go through all of that trouble when we can just use the dot operator?__ &rarr;

* {:.fragment} some of your object's data may need rules or processing applied to them before they are retrieved or written
* {:.fragment} for example, when you read data, you may want to format it a certain way rather than reading the data directly
* {:.fragment} or... you may want to have some validation that occurs before you set data

</section>

<section markdown="block">
## Printing Out an Object

__Let's try printing out one of our <code>Cat</code> objects. What do we get?__ &rarr;
<pre><code data-trim contenteditable>
c = Cat('Paw Newman', 10)
print(c)
</code></pre>

<pre><code data-trim contenteditable>
# prints out ??? <__main__.Cat object at 0x10dfab470>
</code></pre>
{:.fragment}

What? How did this happen? <code>Paw Newman's</code> name is <code>"Paw Newman</code>, not <code>0x10dfab470</code>.
{:.fragment}
</section>

<section markdown="block">
## String Representation of Objects


In Python, by default, __an object's string representation is its class name followed by its id (for some implementations, this is just the object's address in memory)__.

If we want to override this string representation, we can create a _special method_ called <code>__str__</code>. The value that <code>__str__</code> returns will be used as the string representation of objects created from your class.


<pre><code data-trim contenteditable>
&nbsp;   def __str__(self):
        return "the cat named {}".format(self.name)
</code></pre>
</section>

<section markdown="block">
## Types / Validation

__A few notes about data validation:__ &rarr;

* In our constructors, getters and setters, and other methods, we can add any validation that we want to incoming arguments... __if there's an issue, our code can__
    * let the exception bubble up (let an error happen)
    * raise our own custom exception (acknowledge an issue and raise an error)
    * handle the issue (perhaps set a default value)
* __Types are not automatically enforced, though!__



</section>

<section markdown="block">
## Using Custom Exception Classes

<pre><code data-trim contenteditable>
class CutenessError(Exception):
    pass

class Cat:
    def __init__(self, name, cuteness_factor):
        self.name = name
        if cuteness_factor > 10:
            raise CutenessError("{} is too cute".format(cuteness_factor))
        self.cuteness_factor = cuteness_factor

try:
    cat = Cat('Chairman Meow', 88888)
except CutenessError as e:
    print('uh oh, your cat is too cute: {}'.format(e))
</code></pre>
</section>
