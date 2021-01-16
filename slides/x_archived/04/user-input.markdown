---
layout: slides
title: Review 
---

<section markdown="block" class="title-slide">
#  Review (Variables, Strings, Integers, and User Input)
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  So... Let's Start with Variables
</section>

<section markdown="block">
###  Variable

__In Python, what's a variable?&rarr;__

<div class="incremental" markdown="block">
It's a name that refers to a value.
</div>
</section>

<section markdown="block">
###  Declaring Variables

__How do we declare a new variable name and assign it a value?&rarr;__

<div class="incremental" markdown="block">
Using an assignment statement:

1. Start with the variable name
2. Then use the assignment operator (sometimes called token), a single equals sign: (__=__)
3. Finally, the value that you want to assign to the variable

Variable name on the _left_, value on the _right_.

{% highlight python %}
x = 42
{% endhighlight %}

</div>
</section>

<section markdown="block">
###  Naming Variables

__Are there any rules for naming variables?&rarr;__

<div class="incremental" markdown="block">
* consists of letters, digits, and underscores
* must begin with a letter or an underscore
</div>
</section>

<section markdown="block">
###  Naming Variables Continued

__What are some stylistic _conventions_ that we follow when naming variables?&rarr;__

<div class="incremental" markdown="block">
* we usually don't use uppercase letters in variable names
* we usually use underscores to separate words

<del>Word = 'cat'</del>

<del>lotsofwords = 'cabbage, carrots, corn </del>

{% highlight python %}
word = 'cat'
lots_of_words = 'cabbage, carrots, corn'
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Multiple Assignment

__And... what if I want to assign values to multiple variables in just one line? &rarr;__ 

<div class="incremental" markdown="block">
* multiple assignment
* comma separated variable names to the left of the assignment operator
* comma separated values to the right of the assignment operator

{% highlight python %}
word, lots_of_words, x = 'cat', 'cabbage, carrots, corn', 12
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Swapping Values

__What are two ways to swap values? &rarr;__ 

{% highlight python %}
a = 7
b = 21
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
c = a
a = b
b = c
{% endhighlight %}

{% highlight python %}
#  the idiomatic / Pythonic way...
a, b = b, a
{% endhighlight %}
</div>
</section>

<section markdown="block">
##  A Quick Look Back at String Operators
</section>

<section markdown="block">
###  String Concatenation

__What was string concatenation it again? &rarr;__ 

<div class="incremental" markdown="block">
Using the addition operator to add strings together.  For example:

{% highlight pycon %}
>>> "Hi. " + "I'm" + " adding " + "strings!"
"Hi. I'm adding strings!"
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  String Concatenation Continued

Let's use variables!  __What happens when we run the program below? &rarr;__

{% highlight python %}
name = "Joe"
number_of_pets = "314"
pets = "aardvarks"
greeting = "Hi.  My name is " + name 
greeting = greeting + " and I have " + number_of_pets + " " + pets + "."
print(greeting)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight bash %}
Hi.  My name is Joe and I have 314 aardvarks.
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Another Version...

__Let's look at a very similar program.  What's different?  And what happens when we run the program? &rarr;__
{% highlight python %}
name = "Joe"
number_of_pets = 314
pets = "aardvarks"
greeting = "Hi.  My name is " + name 
greeting = greeting + " and I have " + number_of_pets + " " + pets + "."
print(greeting)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight bash %}
#  we tried to add an int to a string!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Type Conversion

__How do we fix this without changing the value of the variable named _number_of_pets_? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
#  use the str function when you add the strings together!
name = "Joe"
number_of_pets = 314
pets = "aardvarks"
greeting = "Hi.  My name is " + name 
greeting = greeting + " and I have " + str(number_of_pets) + " " + pets + "."
print(greeting)
{% endhighlight %}
</div>

</section>


<section markdown="block">
##  Now Let's See How Different Types Affect Numeric Operators
</section>

<section markdown="block">
###  Addition, Subtraction, Division, Integer Division 

<aside>...All Work With Other Numeric Types</aside>

For example: &rarr;

{% highlight python %}
2 + 2    # addition - two ints
24 + 2.2 # addition - int and float
5 // 2   # integer division - int and float
5 // 2.8 # integer division - int and a float
5 / 2    # int and int
{% endhighlight %}
</section>

<section markdown="block">
###  Addition, Subtraction, Division, Integer Division (Fails!)
<aside>Doesn't Work so Well With Non-Numeric Types</aside>

For example: &rarr;

{% highlight python %}
2 + "3"
5 / "3"
5 // "3"
5 - "3"
5 ** "3"
{% endhighlight %}

</section>

<section markdown="block">
###  An Exception: Multiplication

Note that multiplication works with mixed operands: __strings__ and __integers__ 

(This only works for integers; it won't work with floats!).  

For example: &rarr;

{% highlight python %}
2 * "foo"   # k, thx, worx
2.2 * "foo" # fail!
{% endhighlight %}
</section>

<section markdown="block">
###  Some More Type Conversions

__Let's fix the errors in this program without changing the values that are in _slices_ and _people_. &rarr;__

{% highlight python %}
slices = 8
people = "4"
slices_per_person = slices / people
print("Slices per person: " + slices_per_person)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
slices = 8
people = "4"
slices_per_person = slices / int(people)
print("Slices per person: " + str(int(slices_per_person)))
{% endhighlight %}
</div>
</section>

<section markdown="block">
##  Let's Introduce the User Into the Mix!
</section>

<section markdown="block">
###  Functions...

First off, __what's a function? &rarr;__

<div class="incremental" markdown="block">
* a named group of statements / _bunch of code_
* that can optionally take 0 or more values as inputs (_parameters_ or _arguments_)
* and can optionally return/produce a value as an output
</div>

</section>

<section markdown="block">
###  Built-In Functions

__What are some built-in functions that we've seen?__

<div class="incremental" markdown="block">
* print
* str, int, float
* ...
</div>
</section>

<section markdown="block">
###  _Calling_ a Function

__How do we _call_ (execute / run) a function?__

<div class="incremental" markdown="block">
1. function name
2. open parentheses
3. comma separated list of optional arguments 
4. close parentheses

{% highlight python %}
print("one", "two", "three")
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Ask the User!

__What function do we use to ask the user for a value? &rarr;__

<div class="incremental" markdown="block">
input
</div>
</section>

<section markdown="block">
###  The Input Function

__When we call input, what argument(s) does it take, and what is done with it? &rarr;__

<div class="incremental" markdown="block">
Input takes one optional argument: the prompt that's printed out for the user.
</div>
</section>

<section markdown="block">
###  The Input Function Continued

__Does the input function return (that is, _produce_) a value?  If so, what value is produced and what type is it?&rarr;__

<div class="incremental" markdown="block">
* it returns a string
* the string is what the user typed in
</div>
</section>

<section markdown="block">
###  Echo

__Let's write a very simple program together that: &rarr;__ 

* asks the user to _type something_
* the prompt will be "type something", followed by a newline, followed by ">"
* the program will just repeat what is typed in

{% highlight pycon %}
type something
>hi there!
hi there!
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
something_to_echo = input('type something\n>')
print(something_to_echo)
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Repeat

__Try to write a program that: &rarr;__

* asks the user to _type a word_ 
* then, asks the user to enter the number of times they want the word repeated
* finally, the program prints out the word repeated the number of times specified

{% highlight pycon %}
please type word
>hello
please type a number
>5
hellohellohellohellohello
{% endhighlight %}
</section>

<section markdown="block">
###  Repeat (an Implementation)

<aside>Here's One Way of Writing It</aside>
{% highlight python %}
word = input('please type word\n>')
number = input('please type a number\n>')
print(word * int(number))
{% endhighlight %}
</section>

<section markdown="block">
###  A Quick Summary of Input

* the input() function takes an optional argument as a prompt
* and it __always__ returns a __string__
* if you ever want to use input, then...
	* whatever variable that you assign it to, it's a string!
	* if you need to use that input (like as a value in a numeric operation)...
	* make sure _convert_ it if it needs to be changed into a different type 
</section>

<section markdown="block">
##  [Picking up where we left off: functions](functions.html)
</section>
