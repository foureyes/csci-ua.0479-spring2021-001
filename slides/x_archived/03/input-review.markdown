---
layout: slides
title: User Input 
---

<section markdown="block" class="title-slide">
#  User Input, a Closer Look
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Getting Data From the User

__What function allows our program to retrieve data from the user?__ &rarr;

<div class="incremental" markdown="block">
The built-in function, __input__, reads in a line of input from the user.  Input returns this as a value in your program.  __What type is the value that is returned by input?__ &rarr;

Input __always__ returns a string.
</div>
</section>

<section markdown="block">
##  Input Always Gives Back a String

<aside>(even if the user types in a number &rarr;)</aside>

</section>

<section markdown="block">
###   Input Example 1

{% highlight python %}
animal = "aardvark"
adjective = input("Give me an adjective that starts with an 'a' please!\n> ")
print(adjective + " " + animal)
{% endhighlight %}

__What will this program output to the screen if the user types in 'apprehensive'?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
apprehensive aardvark
{% endhighlight %}
</div>
</section>

<section markdown="block">
###   Input Example 2

{% highlight python %}
number_of_cheers = input("How many cheers?\n> ")
print("hip " * number_of_cheers + "hooray")
{% endhighlight %}

__What will this program output to the screen if the user types in 20?__ &rarr;

<div class="incremental" markdown="block">
We get a run-time error! (TypeError: can't multiply sequence by non-int of type 'str')
</div>
</section>

<section markdown="block">
###   Fixing Input Example 2

__How would we fix this program?__ &rarr;

{% highlight python %}
number_of_cheers = input("How many cheers?\n> ")
print("hip " * number_of_cheers + "hooray")
{% endhighlight %}

<div class="incremental" markdown="block">

We can __convert__ the __string__ that we get __from input__ into an __int__ by using the __int__ function...

{% highlight python %}
number_of_cheers = input("How many cheers?\n> ")
print("hip " * int(number_of_cheers) + "hooray")
{% endhighlight %}
</div>

</section>

<section markdown="block">
###   Another Way to Fix Example 2

Using __function composition__, we could also call __int__ on the return value of __input__:

{% highlight python %}
number_of_cheers = int(input("How many cheers?\n> "))
print("hip " * number_of_cheers + "hooray")
{% endhighlight %}

</section>


<section markdown="block">
###  Definitions

* __value__ - just data!  
	* a string, number ...
* __type__ - a kind or category of data/values
	* int, float ...
* __literal__ - the literal representation of a value
	* "a string", 25.0 ...
</section>

<section markdown="block">
###  Definitions Continued

* __function__ - a named sequence of statements that performs a specific task or useful operation
* __function call__ / __calling__ a function - executing or using a function
	* str(25.0)
* __arguments__ - the values that you pass in to a function
	* in _print('hello')_, "hello" is the argument passed in to the function, print 
* __returns__ a value - the result of calling a function, the value that the function gives back
	* float("2") returns 2.0
</section>

<section markdown="block">
###  Finishing up the Review...

Let's take a look at [that handout](../../resources/handouts/class03/types-variables-operators-comments.pdf) again.
</section>

