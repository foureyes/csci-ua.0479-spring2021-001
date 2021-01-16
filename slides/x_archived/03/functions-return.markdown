---
layout: slides
title: Returning Values 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## First, Let's Make Sure We're Speaking the Same Language!
</section>

<section markdown="block">
## A Function (Again)

__What's a function? &rarr;__

<div class="fragment" markdown="block">
* a __function__...
	* is a named sequence of statements that performs some useful operation 
	* may or may not take parameters (produce a value)
	* may or may not produce a result (return a value)
</div>

</section>

<section markdown="block">
## Examples

__What are some examples of built-in functions or functions in modules? &rarr;__

<div class="fragment" markdown="block">
* built-in __functions__
	* print("something")
	* int("5")
	* intput("enter a number)
* __functions__ in modules
	* math.sqrt(5) 
	* sys.exit() 
</div>
</section>

<section markdown="block">
## Calling a Function

__Define what it means to "call" a function.  How do we call a function?  &rarr;__

<div class="fragment" markdown="block">
A __function call__ is the statement that actually executes a function.  It causes the functions code to run.

Syntactically, we call a function by writing &rarr;:

1. the function name 
2. followed by parentheses
3. with zero or more arguments enclosed within those parentheses
4. (no arguments are ok)
</div>
</section>

<section markdown="block">
## Arguments 

Based on the definitions of __function__ and __calling a function__, __how can we define argument? &rarr;__

<div class="fragment" markdown="block">
* an argument is a value provided to a function when the function is __called__
* this value (or values) is used within the function
* the argument can be the result of an expression which may involve operators, operands and calls to other functions!
* or simply, _the input_
</div>
</section>


<section markdown="block">
## Arguments / Parameters
What's the difference between an __argument__ and a __parameter__?

* __argument__: value provided to a function when it's called
* __parameter__: name used inside a function to refer to the value which was passed to it as an argument
* we'll see more about this when we create our own functions!
</section>


<section markdown="block">
## Functions That Return Values

We've used some functions that return values, and we looked at them in an earlier set of slides.  __What type of values do the following functions give back? &rarr;__

* randint(1, 10)
* input("Enter a number")
* float(23)

<div class="fragment" markdown="block">
* int
* str
* float
</div>
</section>

<section markdown="block">
## We Can Define Our Own Functions!
<aside>Yes, Actually.</aside>

<pre><code data-trim contenteditable>
def create_greeting(person):
	return 'hello ' + person
</code></pre>

__What's the name of this function?  How many arguments do you think it takes?  What does the function do?__

<div class="fragment" markdown="block">
* create_greeting
* one argument
* returns a string
</div>
</section>



<section markdown="block">
## Defining a Function - Syntax

__Based on our examples, let's figure out how we define a function:__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
def &lt;function_name&gt;(&lt;zero_or_more_parameters&gt;):
	&lt;statement #1&gt;
	&lt;statement #2&gt;
	.
	.
	&lt;etc.&gt;
	# optional
	return some_value
</code></pre>
</div>
</section>

<section markdown="block">
## The Function Header

1. the keyword, __def__ (this never changes)
2. followed by the function's name
	* (whatever you want, but something meaningful)
	* same rules for variable names apply (alphanumeric and underscores)
3. parentheses surrounding parameters (if any)
	* can just be () if no parameters are required
	* multiple parameters are separated by commas
	* the parameters specify what information must be provided to the function
4. a colon to signify the end of the header line
</section>

<section markdown="block">
## Parameters

A __parameter__ is "a name used inside a function to _refer_ to the value which was passed to it as an argument".

* sometimes we'll use __parameter__ and __argument__ interchangeably
* note that whatever value you pass in to the function, you can now refer to it within the body using the parameter's name
* we'll take a look at this in a little bit...
</section>

<section markdown="block">
## Function Body

The __body__ of a function:

* consists of one or more statements
* the values that were passed in as arguments in the call to the function:
	* can be accessed by the parameter names
	* these names correspond to the position that they were in when the function was called
* an optional __return__ statement that specifies to the function that it should give back a value
* (most of the functions we write will have a return statement)
</section>

<section markdown="block">
## ...And Back to Parameters

Let's see what that means. Whatever values you pass in to the function, you can now refer to it within the body using the parameter's name (based on the position of the argument).

<pre><code data-trim contenteditable>
def greet_more_input(greeting, num):
	s = greeting * num
	return s

greet_more_input("hello", 5)
</code></pre>
</section>

<section markdown="block">
## Parameters Example 1:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

<pre><code data-trim contenteditable>
def greet_more_input(greeting, num):
	s = greeting * num
	return s

greet_more_input("hola", 23)
</code></pre>

<div class="fragment" markdown="block">
* greeting &rarr; "hola"
* num &rarr; 23
</div>
</section>

<section markdown="block">
## Parameters Example 2:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

<pre><code data-trim contenteditable>
def greet_more_input(greeting, num):
	s = greeting * num
	return s

print(greet_more_input("hey " + "there", math.sqrt(25)))
</code></pre>

<div class="fragment" markdown="block">
* greeting &rarr; "hey there"
* num &rarr; 5
</div>
</section>

<section markdown="block">
## Parameters Example 3:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

<pre><code data-trim contenteditable>
def greet_more_input(greeting, num):
	s = greeting * num
	return s

num = "hi"
greeting = 20
greet_more_input(num, greeting)
</code></pre>

<div class="fragment" markdown="block">
* greeting &rarr; "hi"
* num &rarr; 20
</div>
</section>

<section markdown="block">
## Let's Take a Closer Look

<pre><code data-trim contenteditable>
#                    num       greeting
#                      |        |
#                    "hi"      20
#                      |        |
def greet_more_input(greeting, num):
	s = greeting * num
	return s

num = "hi"
greeting = 20
print(greet_more_input(num, greeting))
</code></pre>
</section>

<section markdown="block">
## Function Definition

The entire block of code you wrote, the header and the body of the function, is called the __function definition__.  Here are a few things to note about your function definition:

1. defining a function doesn't call a function
2. you must explicitly call it __after__ it is defined...
3. (and related...) a function must be defined before it's called!
	* if you call it before you define it, you get an error
	* specifcally a NameError 
	* (similar to what happens when using an undeclared variable)
</section>

<section markdown="block">
## Function Definition Example 1:

__If this is the only code in your program, and you run it, what will be printed to the screen?  Something, nothing, or an error? &rarr;__
<pre><code data-trim contenteditable>
def greet():
	return 'hello'

print(greet())
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
hello
</code></pre>
</div>
</section>

<section markdown="block">
## Function Definition Example 2:

__If this is the only code in your program, and you run it, what will be printed to the screen?  Something, nothing, or an error? &rarr;__
<pre><code data-trim contenteditable>
def greet():
	return 'hello'
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
# nothing (the function was never called after it was defined)
</code></pre>
</div>
</section>

<section markdown="block">
## Function Definition Example 3:

__If this is the only code in your program, and you run it, what will be printed to the screen?  Something, nothing, or an error? &rarr;__
<pre><code data-trim contenteditable>
print(greet())

def greet():
	return 'hello'
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
# we called the function before defining it
NameError: name 'greet' is not defined 
</code></pre>
</div>
</section>

<section markdown="block">
## Program Flow

What we've seen so far:

* statements are executed from top to bottom
* each line is executed exactly once


</section>

<section markdown="block">
## Program Flow Coninued

Defining our own functions means:

* still top to bottom, so we have to define the function first
* but once a function is called... 
	1. go to function
	2. execute that code
	3. go back to where function was called
* the body of a function can be executed as many times a function is called
</section>

<section markdown="block">
## Program Flow Example

__Let's walk through this program line-by-line &rarr;__

<pre><code data-trim contenteditable>
def exclaim(word, num):
	punctuation = num * '!'
	s = word + punctuation
	return s

print("hello")
print(exclaim("hi", 1))
print("hey there")
print(exclaim("howdy", 10))
</code></pre>

</section>

<section markdown="block">
## Using a Main Function

Sometimes you'll see a function called main() within a program

* this signifies that this is the _main_ line of execution
* all of the code for the program is written in that function
* the last line of the code calls that function
* the rationale for doing this is to:
	* keep your code organized
	* isolate your function definitions from the actual program (handy when creating modules)
* we'll see this a bit more later...
</section>



<section markdown="block">
## Returning Values

* we can create _fruitful_ functions, that is... functions that return a value
* define a function using __def__, and just use the keyword __return__, followed by the value that you want to give back
* (you might have noticed the keyword, __return__ in previous examples)

<pre><code data-trim contenteditable>
def greet(greeting, num):
	s = greeting * num
	return s
</code></pre>
</section>

<section markdown="block">
## Without Return (None)

In this example, we do not have a return statement. This is still syntactically valid, but...

<pre><code data-trim contenteditable>
def greet(greeting, num):
	s = greeting * num

print(greet('hello', 5)
</code></pre>

If you omit return, you'll get a special value back: __None__. This prints out None to the screen!

__None__ is a value that means the absence of a value!
</section>

<section markdown="block">
## So, Now What?

Now that you have a function that returns a value, you can use that function wherever you would use that value.

<pre><code data-trim contenteditable>
def greet(greeting, num):
	s = greeting * num
	return s

# using the return value of greet as an argument to input!
response = input(greet("hi", 3))
print(response)
</code></pre>
</section>

<section markdown="block">
## The return Statement

* the __return__ immediately stops the execution of a function
* ...and returns the value that follows it
	* the value can be any value!
	* it can even be an expression
</section>

<section markdown="block">
## Some Examples of the Return Statement

These functions are contrived examples of what you can do with return.  __What type and value do they return? &rarr;__

<pre><code data-trim contenteditable>
def foo():
	return "foo"

def bar():
	return "b" + "ar"

def baz():
	return str(math.sqrt(100)) + "!"
</code></pre>

<div class="fragment" markdown="block">
* string, "foo"
* string, "bar"
* string, "10!"
</div>
</section>

<section markdown="block">
## Let's Try Creating a Function That Returns a Value

__Write a function that returns the area of a circle (&pi;r&sup2;)when given a radius, r.&rarr;__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
import math
def area(r):
	a = math.pi * r * r
	return a
</code></pre>
</div>
</section>

<section markdown="block">
## Area, Defined Again

Another way to define our area function:

<pre><code data-trim contenteditable>
import math
def area(r):
	return  math.pi * r * r
</code></pre>

* code is shorter 
* but no intermediary variable (maybe more difficult to debug?) 
</section>

<section markdown="block">
## Print vs Return

__What's the difference between printing in a function and returning a value from a function? &rarr;__

<pre><code data-trim contenteditable>
def greet(greeting, num):
	s = greeting * num
	print(s)

def greet(greeting, num):
	s = greeting * num
	return s
</code></pre>
</section>

<section markdown="block">
## Print vs Return Continued

What's the difference between printing in a function and returning a value from a function?  

* __printing alone will not give you back a value for a function!__  
* however, you can print __and__ return
	* useful for debugging
	* see the example below... where we print out what s is before returning it

<pre><code data-trim contenteditable>
def greet(greeting, num):
	s = greeting * num
	print(s)
	return s
</code></pre>
</section>


<section markdown="block">
## Stopping Execution

The return statement stops execution of your function immediately.  __What gets printed in the following example? &rarr;__

<pre><code data-trim contenteditable>
def foo():
	print("one")
	print("two")
	return "foo"
	print("three")

foo()
</code></pre>
<div class="fragment" markdown="block">
"one" and "two" are printed, but three is not because the function has already returned the value "foo"
</div>
</section>

<section markdown="block">
## Another Example...

Stopping execution again...

<pre><code data-trim contenteditable>
&gt;&gt;&gt; def area(r):
...   a = math.pi * r * r
...   print("before return")
...   return a
...   print("after return")
... 
&gt;&gt;&gt; area(6)
before return
113.09733552923255
</code></pre>
</section>

<section markdown="block">
## Multiple Return Statements

You can have multiple return statements in your function!  __Write a function that calculates absolute value. &rarr;__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
def absolute_value(x):
	if x >= 0:
		return x
	else:
		return x * -1
</code></pre>
</div>
</section>

<section markdown="block">
## Some Exercises

* create a function that returns the largest factor of a number that isn't the number itself
* create two funcions: is_even and is_odd... 
	* each will take one argument (an int)
	* it will use modulo to determine if the number is even or odd
	* it will return True or False
	* (arguably easier to understand than just modulo alone)
* pluralize
	* just add s
	* special case
</section>
