---
layout: slides
title: Functions 
---

<section markdown="block" class="title-slide">
#  Making Our Own Functions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Functions

__What's a function (again)?__ &rarr;

<div class="fragment" markdown="block">
A __function__ is a named sequence of statements that performs a specific task or useful operation
</div>
</section>

<section markdown="block">
###  Built-In Functions

__What are some built-in functions that we just learned about?__ &rarr;

<div class="fragment" markdown="block">
* print
* type
* int
* str
* float
* input
</div>
</section>

<section markdown="block">
###  Our Very Own Functions!

* we can actually create our own functions
* that means:
	* we can group a bunch of statements together
	* name that group of statements
	* __execute that group of statements simply by calling its name!__
</section>

<section markdown="block">
###  Motivation for Creating Functions

__Why would the ability to create our own functions be useful?__ &rarr;

<div class="fragment" markdown="block">
* reduce repetitive code (instead of typing in the group of statements multiple times, just call function)
* break down programming problem into discrete tasks
	* complexity of each sub-task or function is more manageable than dealing with program in its entirity
	* easier to test each individual function or component 
* create your own tools for solving a problem
	* it's almost like defining your own __problem domain__ specific language
</div>
</section>

<section markdown="block">
###  Just a Peek

* we'll only cover enough about functions to be able to write some simple ones (they won't return values quite yet!)
* we'll revisit functions _in-depth_ after the first midterm (early March)
</section>

<section markdown="block">
###  Defining a Function

<pre><code data-trim contenteditable>
#  without parameters (inputs)
def the_name_of_your_function():
	# some code
	print("do some useful stuff")

#  with parameters (inputs)
def the_name_of_your_function(parameter_1, paramter_2):
	# some code
	print("do some useful stuff with parameter_1 and parameter_2")
</code></pre>
</section>

<section markdown="block">
###  Defining a Function Continued

1. a function definition always starts with the __reserved__ word, __def__ (__the function header__)
2. ... followed by the name of your function
	* (function names adhere to the same rules as variable names)
3. ... followed by parentheses
4. with an __optional__, comma separated list of inputs enclosed in parentheses (depends on function)
	* if the __parentheses are empty (), then the function is being called without arguments__
	* __end with a colon__
5. lastly, an indented block of code (__the function body__)
	* this is just one level of indentation in &rarr;
</section>

<section markdown="block">
###  What's This About an Indented Block?

* remember - in Python, __whitespace characters__ (such as space, tabs, newlines, etc.) are __significant__
* __consecutive lines of code__ can be grouped together based on __indentation__
* you can tell the start and end of a function body by its level of indentation
* it is indented one level in from the function header
</section>

<section markdown="block">
###  An Indented Block for the Function Body

<pre><code data-trim contenteditable>
def the_name_of_your_function(parameter_1, paramter_2):
	# inside the function
	print("something")
	print("another thing")

#  outside of the function
print("and another thing")
</code></pre>
</section>

<section markdown="block">
###  Let's Try Creating a Function!

__Write a function called say_multilingual_meow:__ &rarr;

* it'll [say meow in two different languages](http://www.eleceng.adelaide.edu.au/personal/dabbott/animal.html)
* it should print out two lines
* one line with "meow", the other line with "nyan"
* use variables to represent the two types of meow ...

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)
</code></pre>
</div>
</section>

<section markdown="block">
###  Some Terminology


__function definition__ - all of the code for a function

__function header__ - the beginning of the function: its name and optional list of parameters

__function body__ - the code that gets executed when a function is called..

__What is the defintion, header and body of the function we defined below?__ &rarr;

<pre><code data-trim contenteditable>
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)
</code></pre>
</section>

<section markdown="block">
###  Calling Your Function

So... now that you have a shiny new function, __how would you call it?__ &rarr;

<pre><code data-trim contenteditable>
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
"""
Once the function is defined in your file, you can call it!
"""

say_multilingual_meow()
</code></pre>
</div>
</section>


<section markdown="block">
###  Let's See How This All Works!

In one file, write the function definition and function call from the previous slides.  

* try running it!  
* print out "done" after your function call
* __what do you think the output will be?__ &rarr;

<pre><code data-trim contenteditable>
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)

say_multilingual_meow()
print("done!")
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
nyan
meow
done!
</code></pre>
</div>
</section>

<section markdown="block">
###  Calling Your Function Continued

So... [what actually happened there](http://www.pythontutor.com/visualize.html#code=def+say_multilingual_meow()%3A%0A%09japanese_meow+%3D+%22nyan%22%0A%09english_meow+%3D+%22meow%22%0A%09print(japanese_meow)%0A%09print(english_meow)%0A%0Asay_multilingual_meow()%0Aprint(%22done!%22)&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)? &rarr;

<pre><code data-trim contenteditable>
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)

say_multilingual_meow()
print("done!")
</code></pre>

* when you call your function...
* imagine that you're jumping back to your function definition
* ...and then executing the body of your function
* once it's done, execution goes back to where you called your function (printed done for clarity)
</section>

<section markdown="block">
###  Before and After the Function Call

__What does this program output?__ &rarr;

<pre><code data-trim contenteditable>
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)

print('cat sounds:') 
say_multilingual_meow()
print('dog sounds:')
print('woof')
</code></pre>

</section>

<section markdown="block">
###  Before and After the Function Call... Output

<pre><code data-trim contenteditable>
cat sounds:
nyan
meow
dog sounds:
woof
</code></pre>
</section>

<section markdown="block">
###  Just the Definitions, Please!

Let's look at the same program, but without the function __call__.  __What do you think the output of this program will be if the function definition is the only code present in your program?__ &rarr;
<pre><code data-trim contenteditable>
def say_multilingual_meow():
	japanese_meow = "nyan"
	english_meow = "meow"
	print(japanese_meow)
	print(english_meow)
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
 
</code></pre>

(That's supposed to be nothing!  A function definition alone won't execute the code in a function.)
</div>
</section>

<section markdown="block">
###  Just the Calls, Please!

What about this version of the program (again, this is the only code in the program)? __What do you think the output will be?__ &rarr;

<pre><code data-trim contenteditable>
say_multilingual_meow()
</code></pre>

<div class="fragment" markdown="block">
We get a NameError!

<pre><code data-trim contenteditable>
Traceback (most recent call last):
  File "/tmp/foo.py", line 1, in &lt;module&gt;
    say_multilingual_meow()
NameError: name 'say_multilingual_meow' is not defined
</code></pre>

__A function has to be defined before it can be used.__
</div>
</section>

<section markdown="block">
###  Multiple Function Definitions

You can define more than one function in your program!

<pre><code data-trim contenteditable>
def my_first_function():
	print("first")

def my_second_function():
	print("second")
</code></pre>
</section>

<section markdown="block">
###  Functions in Functions

In fact, you can use a function that you've already defined in another function that you're creating.  __What do you think the output of this program will be?__ &rarr;

<pre><code data-trim contenteditable>
def say_moo():
	print("moo")

def main():
	say_moo()
	say_moo()

main()
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
moo
moo
</code></pre>
</div>
</section>

<section markdown="block">
###  Functions in Functions Continued

Notice that in the previous code...

<pre><code data-trim contenteditable>
def say_moo():
	print("moo")

def main():
	say_moo()
	say_moo()

main()
</code></pre>

* we defined a function called __say_moo__
* we defined another function called __main__ that uses __say_moo__
</section>

<section markdown="block">
###  "Local" Variables

* a __local__ variable is a variable created inside a function's definition
* another way of saying this is: all of the variables in your function definition are __local__ to that function
* they cannot be used / accessed by statements outside of the current function definition
* different functions can have local variables of the same name, and they will not interfere with each other
* __scope__ is the part of the program where a variable can be accessed
* a __local__ variable's scope is the function in which it was defined

</section>

<section markdown="block">
###  "Local" Variables Continued


<pre><code data-trim contenteditable>
def my_first_function():
	a = 1
	print(a)

def my_second_function():
	b = 2
	print(b)
</code></pre>

The variables __a__ and __b__ are __local__ to __my\_first\_function__ and __my\_second\_function__ respectively.

__a__ is within the __scope__ of my\_first\_function and __b__ is within the __scope__ of my\_second\_function.

</section>

<section markdown="block">
###  "Local" Variables Continued Some More

In fact... because variables defined within a function are local, using the variable name in two different functions doesn't cause any errors, and nothing gets overwritten. __What will this program output?__ &rarr;

<pre><code data-trim contenteditable>
def my_first_function():
	a = 1
	print(a)

def my_second_function():
	a = 200
	print(a)

my_first_function()
my_second_function()
my_first_function()
</code></pre>
<div class="fragment" markdown="block">
1, 200, and then 1 again
</div>
</section>

<section markdown="block">
##  A Main Function... 

<aside>A common use for defining functions is creating a single function, called main,  that contains your program's main line of logic</aside>
</section>

<section markdown="block">
###  Defining a Main Function

* it is common practice to have the entirety of your program in a single function called main
* with other additional functions defined outside as well
* the examples in {{ site.bookq }} use this pattern often
* here's a template:

<pre><code data-trim contenteditable>
def main():
	print("in main function")

main()
</code></pre>
</section>

<section markdown="block">
###  Main Function Continued

For example, these two programs are equivalent:

<pre><code data-trim contenteditable>
#  version 1
print("About to do stuff")
print("Doing stuff")
print("Done")
</code></pre>

<pre><code data-trim contenteditable>
#  version 2
def main():
	print("About to do stuff")
	print("Doing stuff")
	print("Done")

main()
</code></pre>
</section>

<section markdown="block">
###  Passing Data Into a Function

All of the built-in functions that we've seen so far have values passed in to them:

<pre><code data-trim contenteditable>
print("some stuff")
type("some stuff")
input("enter some stuff\n>> ")
</code></pre>

So far, the functions that we've created __don't take any input__...

</section>

<section markdown="block">
###  Passing Data Into a Function Continued

Inputs to a function are defined by specifying the expected inputs between the parentheses 

<pre><code data-trim contenteditable>

#  this function expects 2 inputs when called:
#  parameter_1 and parameter_2
def name_of_function(parameter_1, parameter_2):
	# do stuff with parameter_1 and parameter_2
</code></pre>

Note: parameters, just like __local__ variables, can only be accessed within the function's body.

</section>

<section markdown="block">
###  Parameters and Arguments Definitions

* a __parameter__ - is a variable that receives an argument that is passed into a function
* __argument__ - a piece of data that is passed into a function
* sometimes these are used interchangeably, but there is actually a distinction 
</section>

<section markdown="block">
###  Parameters and Arguments

* the arguments that you pass into a function can be referenced within that function's body using the parameter's name 
* this is __based on the position of the parameter__ and the __order that the arguments are passed in__ to the function call

<pre><code data-trim contenteditable>
#  this function has two parameters: greeting and num
def greet_more_input(greeting, num):
	# that are used in the body
	s = greeting * num
	print(s)

greet_more_input("hello", 5)
</code></pre>
</section>

<section markdown="block">
###  Um.  What?

The __position of the arguments__ in a function call __determine which parameters the arguments are bound to__.  In the [program below](http://www.pythontutor.com/visualize.html#code=%23++++++++++++++++++++++arguments%0A%23++++++++++++++++++++%22hello%22++++5%0A%23++++++++++++++++++++++%7C++++++++%7C%0Adef+greet_more_input(greeting,+num)%3A%0A++++%23+argument+values+are+now+bound+to+the+paramters,+greeting+and+num!%0A++++s+%3D+greeting+*+num%0A++++print(s)%0Agreet_more_input(%22hello%22,+5)&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0):

* the parameter, __greeting__, refers to "hello" 
* the parameter, __num__, refers to 5

("hello" was passed in first, 5 was passed in second)

<pre><code data-trim contenteditable>
#                       arguments
#                     "hello"    5
#                       |        |
def greet_more_input(greeting, num):
	# argument values are now bound to the paramters, greeting and num!
	s = greeting * num
	print(s)
greet_more_input("hello", 5)
</code></pre>
<!--* -->
</section>

<section markdown="block">
###  Parameters Example 1:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

<pre><code data-trim contenteditable>
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

greet_more_input("hola", 23)
</code></pre>

<div class="fragment" markdown="block">
* greeting &rarr; "hola"
* num &rarr; 23
</div>
</section>

<section markdown="block">
###  Parameters Example 2:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

<pre><code data-trim contenteditable>
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

s = "2"
greet_more_input("hey " + "there", int(s))
</code></pre>

<div class="fragment" markdown="block">
* greeting &rarr; "hey there"
* num &rarr; 2
</div>
</section>

<section markdown="block">
###  Parameters Example 3:

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

<pre><code data-trim contenteditable>
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

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
###  Let's Take a Closer Look

<pre><code data-trim contenteditable>
#                     num       greeting
#                       |        |
#                     "hi"      20
#                       |        |
def greet_more_input(greeting, num):
	s = greeting * num
	print(s)

num = "hi"
greeting = 20
greet_more_input(num, greeting)
</code></pre>
</section>


<section markdown="block">
###  Half the Number

Create a function called __half\_the\_number__:

* it should take a single argument
* it will print out 1/2 of the value passed in

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
def half_the_number(n):
	half = n / 2
	print(half)

#  don't forget to call the function!
def main():
	half_the_number(20)

main()
</code></pre>
</div>
</section>

<section markdown="block">
###  Area Square

Create a function called __compute\_area\_square__()

* it should take a single argument, the length of the side of the square
* it will calculate the square's area
* ...and print out the resulting area

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
def compute_area_square(length_of_side):
	area = length_of_side ** 2
	print(area)
</code></pre>
</div>
</section>

<section markdown="block">
###  Area Rectangle

Create a function called __compute\_area\_rectangle__()

* it should take a two arguments, the length and width of a rectangle
* it will calculate the rectangle's area
* ...and print out the resulting area

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
def compute_area_rectangle(length, width):
	area = length * width
	print(area)
</code></pre>
</div>
</section>

<section markdown="block">
###  Let's Combine This With Input!

Use the previous function to __write a program that__: &rarr;

1. asks the user for a length
2. asks the user for a height
3. prints out the resulting area

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
def compute_area_rectangle(length, width):
	area = length * width
	print(area)

def main():
	length_rectangle = int(input("Length of rectangle:\n> "))
	width_rectangle = int(input("Width of rectangle:\n> "))
	compute_area_rectangle(length_rectangle, width_rectangle)

main()
</code></pre>
</div>

</section>

<section markdown="block">
###   Definitions Recap!

Define the following terms:

* function definition
* function header
* function body
* block

</section>

<section markdown="block">
###   Definitions Recap!

* __function definition__ - all of the code for a function
* __function header__ - the beginning of the function: its name and optional list of parameters, followed by a colon
* __function body__ - the code that gets executed when a function is called
* __block__ - a set of statements that belong together as a group; indentation marks the beginning and end of a block
</section>

<section markdown="block">
###   Definitions Recap Continued!

Define the following terms:

* main function
* local variable
* scope
* argument
* parameter

</section>

<section markdown="block">
###   Definitions Recap Continued!

* __main function__ - a function that contains the program's main line of logic
* __local variable__ - variable created inside a function's definition (only accessible within that function)
* __scope__ - the part of the program where a variable can be accessed
* __argument__ - a piece of data that is passed into a function
* a __parameter__ - is a variable that receives an argument that is passed into a function
</section>

<section markdown="block">
##  BTW - the functions that we've created so far don't return anything ...
</section>
