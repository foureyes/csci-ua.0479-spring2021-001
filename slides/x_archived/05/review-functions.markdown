---
layout: slides
title: Review Functions 
---

<section markdown="block" class="title-slide">
#  Review - Functions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Greetings

Create a function called __display\_loud\_greeting__ ...

* this function will print out a greeting based on the __arguments__ that are passed to it
* it should have two __parameters__, the name of the person to be greeted, and the number of exclamation points to add
* it will display the greeting, "Hi", followed by the name, and finally some number of exclamation points
* __example usage__:
	* display_loud_greeting("Jasper", 4)
	* ... will print out: Hi __Jasper!!!!__

</section>


<section markdown="block">
###  Greetings Implementation 

Here's a possible implementation.  __If this were the only code in this program, what would the output be if we ran it?__ &rarr;

{% highlight python %}
def display_loud_greeting(name, num_exclamation_points):
	greeting = "Hi " + name + num_exclamation_points * "!"
	print(greeting)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
 
{% endhighlight %}

Yup.  That's nothing.
</div>
</section>

<section markdown="block">
###  Calling Greetings

So.... __how do we call this function (let's use the arguments, Jasper and 4)?__ &rarr;

{% highlight python %}
def display_loud_greeting(name, num_exclamation_points):
	greeting = "Hi " + name + num_exclamation_points * "!"
	print(greeting)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
display_loud_greeting("Jasper", 4)
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Detour - Some Definitions Revisited

The previous slides mentioned function __call__, __parameters__ and __arguments__.  __What does it mean to call a function?  What is a parameter, and what is an argument__? &rarr;
 
<div class="incremental" markdown="block">
* __calling__ a function - running or executing the function
* __argument__ - a piece of data that is passed into a function
* a __parameter__ - is a variable in a function that receives an argument that's passed
	* within a function the values passed in can be referred to by parameter name
</div>
</section>


<section markdown="block">
###  ....And More Definitions

What is a __function definition__, __header__, and __body__?  What is meant by saying a __block__ of code? &rarr;

<div class="incremental" markdown="block">
* __function definition__ - all of the code for a function
* __function header__ - the beginning of the function: its name and optional list of parameters
* __function body__ - the code that gets executed when a function is called..
* __block__ - a set of statements that belong together as a group; indentation marks the beginning and end of a block
</div>
</section>

<section markdown="block">
###  Combined With User Input

* instead of hardcoding arguments, let's ask the user for some input!
* __modify the program below so that it asks the user for a name and a number__ &rarr;

{% highlight python %}
def display_loud_greeting(name, num_exclamation_points):
	greeting = "Hi " + name + num_exclamation_points * "!"
	print(greeting)

display_loud_greeting("Jasper", 4)
{% endhighlight %}

Example output from the new program:

{% highlight python %}
What's your name? 
> Jasper
How many exclamation points? 
> 4
Hi Jasper!!!!
{% endhighlight %}

</section>


<section markdown="block">
###  Combined With User Input - Implementation

{% highlight python %}
def display_loud_greeting(name, num_exclamation_points):
	greeting = "Hi " + name + num_exclamation_points * "!"
	print(greeting)

name = input("What's your name?\n> ")
number = int(input("How many exclamation points?\n> "))

display_loud_greeting(name, number)
{% endhighlight %}
</section>


<section markdown="block">
###  A Main Function

__How do we change the previous program so that all of the logic is contained within functions?__ &rarr;

* the main() function should contain the main line or flow of logic
* display\_loud\_greeting and input can be in the main function's body....

<div class="incremental" markdown="block">
{% highlight python %}
def display_loud_greeting(name, num_exclamation_points):
	greeting = "Hi " + name + num_exclamation_points * "!"
	print(greeting)

def main():
	name = input("What's your name?\n> ")
	number = int(input("How many exclamation points?\n> "))
	display_loud_greeting(name, number)

main()
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Variables Inside a Function 

__What's a local variable?  What's scope?__ &rarr;

<div class="incremental" markdown="block">
* __local variable__ - variable created inside a function's definition 
	* only accessible within that function
	* cannot be changed from outside of the function
	* does not overwrite variables of the same name outside of the function (or in other functions)
* __scope__ - the part of the program where a variable can be accessed
</div>
</section>

<section markdown="block">
###  Local Variables

__What is the output of this program?__ &rarr;

{% highlight python %}
def make_some_noise():
	sound = "pop"
	print(sound)

sound = "fizz"
make_some_noise()
print(sound)
{% endhighlight %}

<div class="incremental">
{% highlight python %}
pop
fizz
{% endhighlight %}
</div>
</section>

<section markdown="block">
##  [Review: Conditionals](review-conditionals.html)
</section>
