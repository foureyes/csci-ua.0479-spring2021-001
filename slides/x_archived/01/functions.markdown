---
layout: slides
title: "Functions"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Defining a Function

Basic template for defining a function:

<pre><code data-trim contenteditable>
def function_name(param1, param2):
    body
</code></pre>

No parameters

<pre><code data-trim contenteditable>
def make_breakfast():
    return 'pancakes and home fries'
</code></pre>

With parameters

<pre><code data-trim contenteditable>
def make_breakfast(sweet, savory)
    return '{} and {}'.format(sweet, savory)
</code></pre>

</section>

<section markdown="block">
## Arbitrary Number of Positional Parameters

Hey... my breakfast consists of more than just 2 things. __How can I change my function so that it accepts any number of arguments (kind of like how <code>print</code> works).__ &rarr;

* prefixing a parameter with \* takes incoming arguments and packs those arguments into a tuple
* a common idiom is to use <code>*args</code> in a function definition to allow for an arbitrary number of arguments to be passed in
* within the body of the function, <code>args</code> (without the \*) will be a tuple of the values passed in...



</section>

<section markdown="block">
## Arbitrary Number of Positional Parameters

__What will this output?__ &rarr;

<pre><code data-trim contenteditable>
def make_breakfast(*args):
    print(type(args))
    print(args)

make_breakfast('pancakes', 'ramen', 'cereal', 'bagel')
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
<class 'tuple'>
('pancakes', 'ramen', 'cereal', 'bagel')
</code></pre>

</section>

<section markdown="block">
## Unpacking in a Function Call

You can also use \* before a list or tuple passed in as an argument to unpack that list or tuple into separate arguments! __What does this output?__ &rarr;

<pre><code data-trim contenteditable>
def small_breakfast(sweet, savory):
    return '{} and {}'.format(sweet, savory)

food = ['ramen', 'bagel']
print(small_breakfast(*food))
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
ramen and bagel
</code></pre>

{:.fragment}
<code>small_breakfast</code> has two parameters, but we pass in only a single argument, a list, that we unpack.

<!--* -->
</section>

<section markdown="block">
## Keyword Arguments

Ok... that's cool and all, but some built-in Python functions have this weird name=value thing passed in as an argument. 

__What is that?__ &rarr;

<pre><code data-trim contenteditable>
print('ramen', 'bagel', 'waffles', sep='yum')
# outputs ramenyumbagelyumwaffles
</code></pre>

* <code>sep='yum'</code> is a __keyword argument__ - an argument that is preceded by an identifier (<code>name=</code>)
* which can then be referenced within the body of the function using that name.
</section>

<section markdown="block">
## Keyword Arguments and Default Values

You can define a function that uses keyword arguments by adding them as parameters to your function definition. __What is the output of the following code?__ &rarr;

<pre><code data-trim contenteditable>
def make_breakfast(savory='ramen', sweet='waffle'):
    return '{} and {}'.format(savory, sweet)
print(make_breakfast())
print(make_breakfast(sweet='pineapple'))
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
ramen and waffle
ramen and pineapple
</code></pre>

{:.fragment}
If keyword arguments aren't passed in, default values are used. You can override the default values by passing in <code>name=value</code> as an argument to the function call.
</section>

<section markdown="block">
## Arbitrary Number of Keyword Arguments

You can use <code>**</code> to turn multiple keyword arguments into a __single dictionary__.

* a common pattern is to use __<code>**kwargs</code>__ in a function definition to accept any number of keyword arguments
* in the body of the function, <code>kwargs</code> will contain a dictionary of all of the names and values passed in

<pre><code data-trim contenteditable>
def make_breakfast(**args):
    print(args)
make_breakfast(beverage='orange juice', food='oatmeal')
# {'food': 'oatmeal', 'beverage': 'orange juice'}
</code></pre>

</section>

<section markdown="block">
## Unpacking a Dictionary into Keyword Arguments

As you might expect, __you can also unpack a dictionary into keyword arguments during a function call__. __What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
def make_breakfast(savory='ramen', sweet='pancake'):
    return '{} and {}'.format(savory, sweet)
d = {'savory':'grits', 'sweet':'pineapple'}

print(make_breakfast(**d))
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
grits and pineapple
</code></pre>

{:.fragment}
A single dictionary is passed in as an argument... and is unpacked into two keyword arguments.
</section>

<section markdown="block">
## \*args, \*\*kwargs

You can define functions that have __positional arguments__, an _arbitrary_ number of __positional arguments__, and __keyword arguments__. To do this, you must define the parameters of the function as follows:

1. positional arguments are first
2. arbitrary number of positional arguments next
3. finally ... keyword arguments

<pre><code data-trim contenteditable>
def super_function(a, b, *im, **sick):
    print(a, b)
    print(im)
    print(sick)

super_function(1, 2, 3, 4, 5, foo=6, bar=7)
</code></pre>
<!--* -->
</section>

<section markdown="block">
## Name of Function vs Calling Function

__What's the output of the following code?__ &rarr;

<pre><code data-trim contenteditable>
def foo():
    return 'bar'

x = foo
y = foo()
print(X)
print(y)
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
<function foo at 0x10f348bf8>
bar
</code></pre>

{:.fragment}
The first assignment binds the name <code>x</code> to the function, <code>foo</code>. __x__ is now a callable function! The second assignment binds the return value of calling <code>foo</code> to the variable, <code>y</code>.

</section>

<section markdown="block">
## A Note on Built-In Names / Identifiers

It turns out that you can overwrite the names of built-in functions! __Dont' do this!__ 

In following program, we're binding the name, <code>print</code> to the string "uh oh!"

__What's the output of this code?__ &rarr;
<pre><code data-trim contenteditable>
print = 'uh oh'
print('will this work?')
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
TypeError: 'str' object is not callable
</code></pre>

{:.fragment}
Of course! ...a str isn't a function, so we can't call it! We've now lost the <code>print</code> function!
</section>

<section markdown="block">
## Functions are Objects Too!

Sooo... all this is to say... that <code>function</code> is a valid type, and __functions are objects__!

* you can bind variable names to function objects: <code>my_print = print</code>
* you can pass functions as arguments to other functions
* you can return functions from functions


</section>
<section markdown="block">
## Passing Functions as Arguments

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
def f():
    print('f')

def g(some_function):
    print('calling...')
    some_function()
    
g(f)
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
calling...
f
</code></pre>

</section>

<section markdown="block">
## Functions as Arguments Continued

Using the same function definitions...

<pre><code data-trim contenteditable>
def f():
    print('f')
def g(some_function):
    print('calling...')
    some_function()
</code></pre>

__How are these two function calls different?__ &rarr;

<pre><code data-trim contenteditable>
g(f)
g(f())
</code></pre>

* {:.fragment} the first one prints out <code>calling...</code> and <code>f</code>
* {:.fragment} the second one results in an error: <code>NoneType is not callable</code> 

</section>

<section markdown="block">
## Nested Functions

You can define functions within functions. __What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
def outer():
    def inner():
        print('inner')
    inner()
    print('outer')

outer()
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
inner
outer
</code></pre>

* {:.fragment} <code>inner</code> is defined within the function, <code>outer</code>
* {:.fragment} it can only be used within the body of the enclosing function (or if it's returned... which we'll see next)

</section>
<section markdown="block">
## Returning Functions

__What's the output of this code?__ &rarr;
<pre><code data-trim contenteditable>
def make_greeter(greeting):

    def greet(person):
        return '{} {}'.format(greeting, person)

    return greet

say_hi = make_greeter('hi')
print(say_hi('joe'))
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
hi joe
</code></pre>

* {:.fragment} calling <code>make_greeter</code> with <code>'hi'</code> gives back a function that constructs a string consisting of 'hi' and the argument passed in to the function
* {:.fragment} the name, <code>say_hi</code> is bound to the new function
</section>

<section markdown="block">
## Global Variables and Function Definitions

__In the following program, will something be printed out, nothing, or an error... and why?__ &rarr;

<pre><code data-trim contenteditable>
s = "hello"

def greet():
	print(s)

greet()
</code></pre>

{:.fragment}
__s is a global variable__.  It is accessible everywhere, including the function body. 
</section>

<section markdown="block">
### Variables Declared Inside a Function

__In the following program, will something be printed out, nothing, or an error... and why?__ &rarr;

<pre><code data-trim contenteditable>
def greet():
	s = "hello"
	print(s)

print(s)
</code></pre>

{:.fragment}
An error occurs because s is inaccessible outside of the function definition.  __s is local to the function that it was defined in.__
</section>

<section markdown="block">
## Parameters

__In the following program, will something be printed out, nothing, or an error... and why?__ &rarr;

<pre><code data-trim contenteditable>
def greet(s):
	s = s + "!"
	print(s)

greet("foo")
print(s)
</code></pre>

{:.fragment}
An error occurs.  You can't access the parameters (by their name) that you passed in to the function from outside of the function.  __Parameters are local to their function.__
</section>

<section markdown="block">
### Precedence / Finding a Name

__In the following program, will something be printed out, nothing, or an error... and why?__ &rarr;

<pre><code data-trim contenteditable>
s = "hello"

def greet():
	s = "something else"
	print(s)

greet()
print(s)
</code></pre>


<div class="incremental" markdown="block">
Variables _created_ within a function are _local_ to that function.  A function will use a __local__ variable before global.  In this case, it will use the _local_ variable, s, instead of the global variable, s.
</div>
</section>


<section markdown="block">
## Scope

A __scope__: 

* determines where a variable is accessible
* a __scope__ is the textual region of a program where names are __directly__ accessible
* it __holds the current set of all available names and the values that they refer to__

</section>

<section markdown="block">
## Global Scope

* anything that we define in the top level of indentation in our program is said to be in the __global scope__
* in the following example, the variables _a_ and _b_ are in the __global scope__
* they can be accessed from anywhere, even within the function

<pre><code data-trim contenteditable>
a, b = 25, "something"

def foo():
	print(a)
	print(b)

foo()
</code></pre>
</section>

<section markdown="block">
## Local Scope

Variables that are defined in your function (one indentation level in), however, are only available within your function.  They are _local_ to that function.  The example below won't work.

<pre><code data-trim contenteditable>
def foo():
	c = "bar"
	return c

print(c)
</code></pre>

</section>

<section markdown="block">
## Local Scope Continued

Variables that __are declared__ (created) within a function that have the same name as a global variable are totally different variables/values! They create a new variable in the local scope that takes precedence over the global variable (they don't overwrite the outer, global variable). __What will this print?__ &rarr;

<pre><code data-trim contenteditable>
c = "on toast"
def foo():
	c = "grape jelly"
	print(c)

foo()
print(c)
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
grape jelly
on toast
</code></pre>

{:.fragment}
[Obligatory Python tutor version](http://www.pythontutor.com/visualize.html#code=c+%3D+%22on+toast%22%0Adef+foo()%3A%0A%09c+%3D+%22grape+jelly%22%0A%09print(c)%0A%0Afoo()%0Aprint(c)&mode=display&cumulative=true&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)
</section>


<section markdown="block">
### Creating Names

* when you create a variable in a function, you're actually creating a name in the local scope
* if there's a global variable that happens to be the same name, it is not affected!

</section>

<section markdown="block">
## Finding Names

If you use a variable name in a function, __it will try to find that name in the following places in order__:

* __local__ scope (variables defined in the function)
* __enclosing functions' locals__ (function can be defined within function definitions; we saw this in previous slides)
* __global scope__ (variables defined in the top-level of your file)
* __built-ins__ (all of the built-in functions and variables that are available when Python starts)



</section>
<section markdown="block">
## Finding Names Continued

__What does the following code print out?__ &rarr;


<pre><code data-trim contenteditable>
foo = 'global foo'
bar = 'global bar'
baz = 'gobal baz'
def f():
    bar = 'enclosing bar'
    def g():
        baz = 'local baz'
        print(foo, bar, baz)
    g()

f()
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
global foo enclosing bar local baz
</code></pre>

</section>

<section markdown="block">
## Global Variables Revisited

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
n = 1

def f():
    n = 200
    print(n)
f()
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
200
</code></pre>

* {:.fragment} easy... we've seen this before
* {:.fragment} n is global, so its value can be read from within the function's body (it's accessible from everywhere!)
</section>

<section markdown="block">
## Global Variables Revisited

__What's the output of this code?__ &rarr;

<pre><code data-trim contenteditable>
n = 1

def f():
    n += 1
    print(n)
f()
</code></pre>

<pre class="fragment"><code data-trim contenteditable>
UnboundLocalError: local variable 'n' referenced before assignment
</code></pre>

{:.fragment}
<code>n += 1</code> is the same as <code>n = n + 1</code>... but Python sees the assignment along with the reference to n in the value... so it thinks that n does not have a value yet!

</section>

<section markdown="block">
## Changing Global Variables within a Local Context

Ok... so what if you wanted to change that global variable (that is... assign a different value to it)? __Use the keyword, <code>global</code>, before the variable name__ so that you can change global variable from within a function body:

<pre><code data-trim contenteditable>
n = 1

def f():
    global n
    n += 1
    print(n)
f()
</code></pre>

</section>

<section markdown="block">
## Global Variables that are Mutable

Note that if a global variable is mutable, __you can _mutate_ it from within a function body__. &rarr;

<pre><code data-trim contenteditable>
numbers = [1, 2, 3]

def change_first():
    numbers[0] = 99

change_first()
print(numbers)
# prints out [99, 2, 3]
</code></pre>

* notice that this is not the same as creating a new variable in the local scope
* instead it's changing a single element in a global list
* no need to use the <code>global</code> keyword in this case
</section>

<section markdown="block">
## Closures

A __closure__ is a function along with its enclosing scope / environment. 

* in Python, __we create closures by defining functions within functions__
* the inner function _remembers_ the variables that the outer, enclosing function has... (even after the outer function returns)

<pre><code data-trim contenteditable>
def gimme_function():
    foo = 'bar'
    def f():
        print(foo)
    return f
g = gimme_function()
g()
</code></pre>

The variable, <code>foo</code>, is available to the function, <code>gimme_function</code>
</section>

<section markdown="block">
## nonlocal

We can use the keyword, <code>nonlocal</code> to change variables in the closure (much like the keyword, <code>global</code>)...

<pre><code data-trim contenteditable>
def make_counter():
    count_calls = 0
    def count():
        nonlocal count_calls
        count_calls = count_calls + 1
        return count_calls
    return count
</code></pre>
<pre><code data-trim contenteditable>
my_counter = make_counter()
my_counter()
another_counter = make_counter()
x = another_counter()
my_counter()
y = my_counter()
print(x)
print(y)
# prints out 1... then 3
</code></pre>
</section>
