---
layout: slides
title: "More About Classes"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Additional Class Features

In addition to creating classes with __constructors__, __methods__, and __instance variables__ you can also use the following class features: &rarr;

* {:.fragment} __static variables__ - variables that can be accessed without an instance, but still defined in a class
* {:.fragment} __static methods__ - methods that can be called without an instance, but still defined in a class
* {:.fragment} __magic methods__ - special methods that you can implement to add specific functionality to your class (For example, working with the plus operator)

</section>

<section markdown="block">
## Static Variables

__"Static" / class variables__ ... are properties that you can access __with or without an instance__. The value for a static variable __remains the same for all instances__

Defining a static variable &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
class Example:
    # declare a static variable within a class
    some_var = 'I am static'
</code></pre>
{:.fragment}

Accessing a static variable &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
# without instance (use class name)
print(Example.some_var) # I am static

# with instance
obj = Example()
print(obj.some_var) # I am static
</code></pre>
{:.fragment}
</section>    

<section markdown="block">
## Static Methods

__"Static" methods__ ... are methods that you can call __with or without an instance__.  To define a __static method__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
class Example:
    # prefix with @staticmethod and don't use self parameter
    @staticmethod
    def say_hello():
        return 'hello'
</code></pre>
{:.fragment}

Calling a __static method__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
# without instance (use class name)
# (no need to add self as parameter)
print(Example.say_hello())  # hello

# with instance
obj = Example()
print(obj.say_hello()) # hello
</code></pre>
{:.fragment}
</section>    


<section markdown="block">
## Magic Methods

If you name and implement a method with a special name, it'll have the ability to perform magic! (Not really). __Magic methods__ are methods that add defined functionality to your class. 

__Magic methods usually start and end with TWO underscores__ &rarr;

`__method_name__` - "magic method", "dunderscore", etc. 

* {:.fragment} `__init__` - constructor (initializing your object)
* {:.fragment} `__str__` - nicely formatted string representation
* {:.fragment} `__repr__` - actual string representation .... doesn't have to be formatted nicely
* {:.fragment} `__add__` - lets you use + operator
* {:.fragment} `__eq__`, `__gt__`

Note that these are different from:
{:.fragment}

* `__name__` ... built in variable that contains the name of the module
* `'__main__' # a string that names the currently running module`
{:.fragment}

</section>

<section markdown="block">
## A Fraction Class

__Demonstrates use of static methods and magic methods__ &rarr;

First, let's start of with a class definition and constructor:

<pre><code data-trim contenteditable>
class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
</code></pre>
</section>

<section markdown="block">
## A Static Method

`gcf` is __defined as a static method__ because it's possible that we want to call this outside of the context of a fraction object (for example, just passing it two numbers): &rarr;
<pre><code data-trim contenteditable>
    # this means that this method can be called 
    # with/without instance # and consequently, no 
    # self is needed you call it on an instance or 
    # the actual class itself: Fraction.gcf()

    @staticmethod 
    def gcf(a, b):
        # go through every possible factor
        # check if it divides evenly into both
        # return the largest one
        cur_gcf = 1
        for factor in range(1, a + 1):
            if a % factor == 0 and b % factor == 0:
                cur_gcf = factor
        return cur_gcf
</code></pre>


</section>

<section markdown="block">
## Comparison with Regular Methods

__Let's compare with a regular method__ (one that's called on an instance) &rarr;

Compare to a regular method...

<pre><code data-trim contenteditable>
    # regular method, must be called with instance
    def reduce(self):
        # note how gcf is called / used (no instance needed)!
        gcf = Fraction.gcf(self.n, self.d)
        return Fraction(self.n // gcf, self.d // gcf)
</code></pre>

</section>

<section markdown="block">
## Magic Methods for String Representation

Sometimes, it's __useful to have a string version of an instance of your class__. For example &rarr;

1. {:.fragment} calling `str` on your instance: `str(some_variable)`
2. {:.fragment} passing your instance to print: `print(some_variable)

To define what happens in these cases: 
{:.fragment}

* implement `__str__` and `__repr__`
* both should return a string
* `__str__` is for the human readable string, `__repr__` is a string representation of all of the data in the instance:
{:.fragment}


</section>

<section markdown="block">
## Fraction class, __str__ and __repr__

__Using \_\_str\_\_ and \_\_repr\_\_ for string representation__ for our fraction class... &rarr;

<pre><code data-trim contenteditable>
    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    def __repr__(self):
        # we can call methods that already defined
        return self.__str__()
</code></pre>

Which allows us to...

<pre><code data-trim contenteditable>
amt_of_pie = Fraction(1, 2)
print(amt_of_pie) # prints out 1/2
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## More Magic Methods

In addition to `str` and `repr` there are many more __magic methods__ that add functionality to your object: `__add__` allows the `+` operator, `__eq__` allows `==` &rarr;

__Implementing the above methods gives us the following functionality__ &rarr;

<pre><code data-trim contenteditable>
a = Fraction(1, 2)
b = Fraction(1, 3)
print(fractions)
print(a + b)
print(a == b)
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## Equals and Addition

__Here's how == and + can be implemented in the Fraction class__ &rarr;

<pre><code data-trim contenteditable>
    # note the parameters and return values

    def __add__(self, other):
        return self.add(other)

    def __eq__(self, other):
        return self.n == other.n and self.d == other.d

    def add(self, other):
        new_n = (self.n * other.d) + (other.n * self.d)
        new_d = self.d * other.d
        return Fraction(new_n, new_d)
</code></pre>

</section>

<section markdown="block">
## Usage

__Some example usage of the Fraction class__ &rarr;

<pre><code data-trim contenteditable>
a = Fraction(1, 2)
b = Fraction(6, 8)
c = Fraction(1, 3)
fractions = [a, b, c]
</code></pre>

<pre><code data-trim contenteditable>
print(fractions) # [1/2, 6/8, 1/3]
print(a.add(c)) # 5/6
print(a + c) # 5/6
print(a == c) # False
print(a == Fraction(1, 2)) # True
print(Fraction.gcf(9, 12)) # 3
print(Fraction(4, 8).reduce()) # 1/2
</code></pre>

</section>

<section markdown="block">
## Inheritance Overview

__A class can be created based off of another existing class__ &rarr;

* {:.fragment} that is...
* {:.fragment} __methods__ and __instance variables__ from the original (or base/parent class)...
* {:.fragment} will exist in the sub class (or child class)
* {:.fragment} _without_ those methods and instances having to be explicitly defined

For example...
{:.fragment}

1. {:.fragment} we may want a `Student` class that has `first`, `last` and `full name`
2. {:.fragment} ...so we can just __base it off our existing `Person` class__

</section>

<section markdown="block">
## Inheritance: Base Class

Starting with our `Person` class as the __parent / base__: &rarr;

<pre><code data-trim contenteditable>
class Person:
    def __init__(self, title, first, last):
        self.title = title
        self.first = first
        self.last = last
        # self.full_name = first + ' ' + last

    def __str__(self):
        return self.title + ' ' + self.last

    def full_name(self):
        return self.first + ' ' + self.last

    def say_greeting(self, greeting):
        return greeting + self.first
</code></pre>

</section>

<section markdown="block">
## Inheriting from Person

__Now... `Student` can inherit from `Person`__ using the following syntax: `class Student(Person)` &rarr;

<pre><code data-trim contenteditable>
class Student(Person):
    def __init__(self, title, first, last, netid):
        # when we call super, we get access to the super / parent class methods
        # use super when you're in the class
        super().__init__(title, first, last)
        self.netid = netid

    def full_name(self):
        s = 'STUDENT ' 
        return s + self.first + ' ' + self.last
    
    # this method is called only on student objects
    # person objects don't have this
    def do_homework(self):
        return 'done'
</code></pre>
</section>

<section markdown="block">
## Using Student

__Note that `s` still has the `full_name` method even though it was not defined in `Student`__.

<pre><code data-trim contenteditable>
s = Student('Mr', 'Joe', 'Versoza', 'jjv222')
print(s)
print(s.netid)
print(s.say_greeting('hi'))
print(s.full_name())
</code></pre>

</section>
