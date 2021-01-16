---
layout: slides
title: "Decorators (and args again)"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>
<section markdown="block">
## Aaaaaaaargs!?

__Anyone remember what \*args is... or maybe what it's used for?__ &rarr;

* we used <code>*args</code> in function definitions to specify that a function can take an arbitrary number of arguments.
* <code>*args</code> goes in the parameter list
* <code>args</code> in the function body to represent the tuple of arguments
{:.fragment}

__Got it? Ok... sooooo__ &rarr;
{:.fragment}

</section>

<section markdown="block">
## \*args Example

What's the output of this code?
<pre><code data-trim contenteditable>
def my_func(*args):
    return (max(args), min(args))
print(my_func(1, 2, 3))
print(my_func(1, 2, 3, 4, -2))
</code></pre>

<pre><code data-trim contenteditable>
# *args represents a tuple of the arguments coming in
# ... so we get the max and min of the args tuple
(3, 1)
(4, -2)
</code></pre>

</section>
<section markdown="block">
## Some More Details on Args

When used outside of the parameter list, prefixing a variable with \* will unpack a list or a tuple into separate arguments for a function call.

__Check iiittt. What does this print out?__ &rarr;

<pre><code data-trim contenteditable>
t = (1, 6, 2)
for i in range(*t):
    print(i)
</code></pre>

<pre><code data-trim contenteditable>
1
3
5
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## So... There's a Difference

There's a slight difference between the two functions below, <code>f</code> and <code>g</code>. __What's going on... what will the output be?__ &rarr;

<pre><code data-trim contenteditable>
def f(*args):
    print(args)
print(f(1, 2))

def g(*args):
    print(*args)
print(g(1, 2))
</code></pre>

<pre><code data-trim contenteditable>
(1, 2)
1 2
# the first one prints out a tuple
# the second prints out each element of the tuple as a separate argument
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## A Bit of Code

Answer questions about the following code:

* __what are the types of its arguments?__ &rarr;
* __what is the type of its return?__ &rarr;
* __what is it doing with its arguments?__ &rarr;

<pre><code data-trim contenteditable>
def call_it(func, n):
    def new_func(x):
        res = x
        for i in range(n):
            res = func(res)
        return(res)
    return new_func
</code></pre>
</section>

<section markdown="block">
## A Closer Look

It takes a function as an argument... and it returns a new function that calls the old function a few times.

In the example usage below... my_func is a new function that calls double a few times.

<pre><code data-trim contenteditable>
def double(num):
    return num * 2

my_func = call_it(double, 3)
print(my_func(2))
</code></pre>

__The function, double, was kind of modified... without actually modifying the actual function definition.__ &rarr;
</section>

<section markdown="block">
## Decorators

Soooo. That thing we just saw... could be called a __decorator__.

A __decorator__ is function that takes a function as an argument and returns a _replacement_ function.
</section>

<section markdown="block">
## A Decorator That Does Nothing

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
def make_replacement(old_func):
    def new_func():
        res = old_func()
        return res
    return new_func
</code></pre>

<pre><code data-trim contenteditable>
def make_some_pizza():
    return 'pizza is made'

f = make_replacement(make_some_pizza)
res = f()
print(res)
</code></pre>

<pre><code data-trim contenteditable>
pizza is made
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## Ok, How About Something More Useful

Hm. That was kind of silly. __The new function that was returned (that was stored in f) is essentially the same as calling the function that was originally passed in (make_some_pizza).__

Let's make a slight modification. __What would the output be if we changed <code>make_replacement</code> to:__ &rarr;
<pre><code data-trim contenteditable>
def make_replacement(old_func):
    def new_func():
        res = old_func()
        res += " with pepperoni"
        return res
    return new_func
</code></pre>

<pre><code data-trim contenteditable>
pizza is made with pepperoni
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Decoratin'

So, basically, __we have a pattern for modifying a pattern for modifying a function regardless of weather or not we have access to the actual function definition!!!__

In fact, a common use of this pattern is __replace a function entirely!__ &rarr;

<pre><code data-trim contenteditable>
make_some_pizza = make_replacement(make_some_pizza)
</code></pre>

We've now replaced <code>make_some_pizza</code> with a decorated version of itself!

</section>

<section markdown="block">
## Decorator Syntax

__Replacing a function with a _decorated_ version of itself is common enough that there's special syntax for it:__ 

`@` followed by name of the function that does the modification... placed above the function definition to be modified
{:.fragment}

<pre><code data-trim contenteditable>
@name_of_function_decorator
def function_to_be_modified():
    return foo
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Decorator Syntax Continued

Sooo.... instead of:

<pre><code data-trim contenteditable>
def make_some_pizza():
    return 'pizza is made'
make_some_pizza = make_replacement(make_some_pizza)
</code></pre>

We have this:
{:.fragment}

<pre><code data-trim contenteditable>
@make_replacement
def make_some_pizza():
    return 'pizza is made'
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## A Slight Modification

__Let's try creating a decorator that gives back a modified function that accepts arguments.__ __What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
def shout(old_f):
    def new_f(some_arg):
        res = old_f(some_arg)
        return res + '!!!!!'
    return new_f
</code></pre>
<pre><code data-trim contenteditable>
str = shout(str)
res = str(12)
print(res)
</code></pre>

<pre><code data-trim contenteditable>
12!!!!!
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Again, With Something Slightly Different

__What's the output here!?__ &rarr;
<pre><code data-trim contenteditable>
@shout
def full_name(first, last):
    return "{} {}".format(first, last)
</code></pre>

<pre><code data-trim contenteditable>
person = full_name('Alice', 'Alvarez')
</code></pre>

We get an error! __Why?__ &rarr;
{:.fragment}

The function that <code>shout</code> returns, <code>new_f</code>, only takes one argument. __How do we fix this?__ &rarr;
{:.fragment}
 
</section>

<section markdown="block">
## Fixin' It (Multiple Args)

__How can we change our shout decorator so that it accepts multiple arguments?__ &rarr;


Use \*args!
{:.fragment}

<pre><code data-trim contenteditable>
def shout(old_f):
    def new_f(*args):
        res = old_f(*args)
        return res + '!!!!!'
    return new_f
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## One Last Thing

`__name__` and `__doc__` get mangled, so....

<pre><code data-trim contenteditable>
from functools import wraps
def my_decorator(f):
     @wraps(f)
     def wrapper(*args, **kwds):
         print('Calling decorated function')
         return f(*args, **kwds)
     return wrapper
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
@my_decorator
def example():
     """Docstring"""
     print('Called example function')
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Why

__I guess that's umm... useful? What are some applications of decorators?__ &rarr;

* decorating functions is actually useful! sometimes we want to:
    * modify arguments going into a function or modify a functions output
    * do _some things_ before or after we call a function
* some examples:
    * timing (use timeit.timeit())...  &rarr;
    * caching... store the result in a dictionary, don't call function...  &rarr;
    * insert additional arguments
    * authentication check
{:.fragment}

</section>

<section markdown="block">
## In Practice

In reality, though...

* it's unlikely we'll be making too many of our _own_ function decorators
* instead, we'll be using them a bunch... for example:
    * python uses decorators to define a method as static
    * one of the libraries will use for web development, flask, uses decorators for http request handling
* __good thing decorators are easy to use!__

</section>


