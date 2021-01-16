---
layout: slides
title: "Classes, Examples"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Classes

* creating properties on the fly
* more about static methods
* finish off fraction class
* using more magic methods
* draw a face, make creating a class that represents a face
* what am i?

</section>

<section markdown="block">
## We're Not Limited by the Constructor / Class Definition

__We can create instance properties / attributes whenever we want!__ &rarr;

<pre><code data-trim contenteditable>
class Whatever:
    pass

w1 = Whatever()
w2 = Whatever()
w1.hi = "hello"

print(w1.hi)

try:
    print(w2.hi)
except:
    print("not gonna say it")

</code></pre>

</section>

<section markdown="block">
## Fraction

(From last class) Initial setup... __write a class that represents a fraction.__

* create a constructor
* create a special method, <code>__str__</code> so that the string representation of a Fraction object is <code>numerator / denominator</code> (when calling print or str, for example)

<pre><code data-trim contenteditable>
class Fraction:

    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return '{} / {}'.format(self.numerator, self.denominator)
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Multiply

__Write a method called multiply... that takes another fraction as an argument... uses the argument's numerator and denominator to multiply the numerator and denominator of the object that multiply was originally called on.__ &rarr;

<pre><code data-trim contenteditable>
a = Fraction(1, 4)
b = Fraction(2, 3)
a.multiply(b) # multiply changes fraction a!
print(a)
# prints out 2/12
</code></pre>
</section>

<section markdown="block">
## Wait a Second, 2/12?

__Sooo... the result of that multiplication was 2/12. That looks off? What do we do with a fraction that looks like that?__ &rarr;

* {:.fragment} we should reduce! __how do we do that?__
* {:.fragment} find the greatest common factor between the numerator and denominator, and divide both by that factor... which means we have to implement 2 functions/methods!
* {:.fragment} greatest common factor... aaaand reduce
</section>

<section markdown="block">
## Greatest Common Factor

__What's a naive algorithm for calculating the greatest common factor?__ &rarr;

* {:.fragment} go through every _possible_ factor of the smallest number, n (that is, 1 through n)
* {:.fragment} if the numerator and denominator are both divisible by the factor... the factor _could_ be the greateset common factor
* {:.fragment} continue on to the next factor
* {:.fragment} give back the last potential gcf

</section>

<section markdown="block">
## Greatest Common Factor Method

We can create the greatest common factor as a __static method__. 

* a __static method__ is a method that can be called on the class itself (as well as on instances)
* this can be used when you think that your method could / should be used without an instance of your class 
* __to create a static method__ &rarr;
    * add a __decorator__ <code>@staticmethod<code> before your method
    * omit self from the parameter list 

__Let's see our static method version of greatest common factor__ &rarr;
</section>

<section markdown="block">
## Greatest Common Factor Method Continued

__What should our gcf method do? Should it have parameters? Should it return a value?__ &rarr;

<pre><code data-trim contenteditable>
class Fraction:
    # ...

    @staticmethod
    def gcf(a, b):
        factor = 1
        for n in range(1, min(a, b) + 1):
            if a % n == 0 and b % n == 0:
                factor = n
        return factor
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## A WUT? Static Method

A little more detail on static methods... 

* [check out the docs](https://docs.python.org/3.5/library/functions.html#staticmethod)
* [why you would use them?](http://stackoverflow.com/questions/2438473/what-is-the-advantage-of-using-static-methods-in-python)
    * {:.fragment} limited use since they don't have access to instance data
    * {:.fragment} but, it may make sense from an organizational point of view to lump together some functionality with a class
* check out this example, where the method, <code>bar</code> can be called on the class itself... or on an instance:

<pre><code data-trim contenteditable>
class Foo:

    @staticmethod
    def bar():
        return 'bar'

# call on class
print(Foo.bar())

# or on instance!
f = Foo()
print(f.bar())
</code></pre>
</section>

<section markdown="block">
## Reduce

__Now that we have greatest common factor, we can reduce. What should reduce do... any parameters? Should it return a new value or mutate the object its called on?__ &rarr;

<pre><code data-trim contenteditable>
class Fraction:
    # ...

    def reduce(self):
        # notice that we don't have to call gcf
        # on an instance!
        factor = Fraction.gcf(self.numerator, self.denominator)
        self.numerator = self.numerator // factor
        self.denominator = self.denominator // factor
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Using Reduce

We could make calling reduce up to the user of our class:

<pre><code data-trim contenteditable>
a = Fraction(1, 4)
b = Fraction(2, 3)
a.multiply(b)
a.reduce()
print(a)
</code></pre>

And / or we can combine it with multiply so that we automatically reduce:

<pre><code data-trim contenteditable>
class Fraction:
    # ...
    def multiply(self, other):
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        self.reduce()
</code></pre>
</section>


<section markdown="block">
## How About Add?

__Let's specify what an add method should do... how do we implement it?__ &rarr;

<pre><code data-trim contenteditable>
class Fraction:
    # ...

    def add(self, other):
        old_other = Fraction(other.numerator, other.denominator)
        other.multiply(Fraction(self.denominator, self.denominator))
        self.multiply(Fraction(old_other.denominator, old_other.denominator))
        self.numerator += other.numerator
        self.reduce()
</code></pre>
{:.fragment}

</section>
<section markdown="block">
## Special Methods

We can also redesign our <code>Fraction</code> type to make use of some special methods that allow the use of common operators, like addition and multiplication. 

The methods, called __magic__ methods start and begin with two underscores... and when they're defined, they have some special functionality (like behaving like a constructor or allowing the use the addition symbol...etc.)

[Check out this article on special methods](http://www.rafekettler.com/magicmethods.html)

We could use these special methods to create a new version of our fraction class that utilizes regular operators, like + and \*.

<pre><code data-trim contenteditable>
a = Fraction(1, 2) 
b = Fraction(2, 4)
c = a * b
print(c)
# would give us an entirely new Fraction!
</code></pre>
</section>

<section markdown="block">
##  Let's Implement the Following Special Methods


* \_\_add\_\_
* \_\_mul\_\_
* \_\_eq\_\_

</section>

<section markdown="block">
## Multiply

__Implement \_\_mul\_\_ so that \* returns a new value__ &rarr;
<pre><code data-trim contenteditable>
def __mul__(self, other):
    n = self.numerator * other.numerator
    d = self.denominator * other.denominator
    return Fraction.reduce(Fraction(n, d))
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Add

__Implement \_\_add\_\_ so that + returns a new value__ &rarr;

<pre><code data-trim contenteditable>
def __add__(self, other):
    d = other.denominator * self.denominator
    n = self.numerator * other.denominator + self.denominator * other.numerator 
    return Fraction.reduce(Fraction(n, d))
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Hey... Wait... A Pattern

Notice how we're calling reduce at the end of both of the methods that we just created? __We just learned something that could modify functions__ &rarr;

We can create a reduce decorator!
{:.fragment}

<pre><code data-trim contenteditable>
def reduced(old_f):
    def new_f(*args):
        res = old_f(*args)
        return Fraction.reduce(res)
    return new_f
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## What Am I?

__What are some ways of determining what the class or type of something is?__ &rarr;

We know two... and there's a 3rd:

<pre><code data-trim contenteditable>
type("hello")
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
"hello".__class__
</code></pre>
{:.fragment}
<pre><code data-trim contenteditable>
isinstance("hello", str)
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Additional Exercise

* \_\_eq\_\_
* create a turtle drawing
* use functions for abstraction
* use a class for abstraction

</section>
