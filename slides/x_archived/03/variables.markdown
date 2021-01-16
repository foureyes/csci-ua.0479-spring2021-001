---
layout: slides
title: Variables 
---

<section markdown="block" class="title-slide">
#  Variables
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Variables

* a __variable__ is a _name_ that refers to a _value_:
* once a variable is declared and assigned a value, __you can use that variable where you would use any other values &rarr;__
	* my_variable + "!"
	* print(my_variable)
	* (a + b) / c

</section>

<section markdown="block">
###  Assignment 

<aside>Assigning values to a variable</aside>

* use the assignment operator: __=__
	* a single equals sign
	* note - does not test for equality, performs __assignment__!
* variable name goes on the left 
* value goes on the right
</section>

<section markdown="block">
###  Using Variables

When do you use variables?

* when you want your program to _remember_ a value
* if you have a value that will _vary_ 
* some examples include:
	* a player's score
	* a count of repetitions
	* user input
	* sensor input
* additionally, using variables will help make your code more maintainable / less brittle
	* (let's talk about this...)

</section>

<section markdown="block">
###  Here's an Example of Improving Maintainability

__Let's say you have a program that adds x number of exclamation points to some words.  &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
print("foo" + "!" * 5)
print("bar" + "!" * 5)
{% endhighlight %}
__OR...__
{% highlight python %}
my_exclamation_constant = 5
print("foo" + "!" * my_exclamation_constant)
print("bar" + "!" * my_exclamation_constant)
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  "Hardcoding"
* assume everything will vary / change
* avoid using a bare __literal__
	* you remember what that is, right?
	* "a string", 58.3
* sometimes this is called __hardcoding__
* cleaning this stuff up helps code reuse / __DRY__
	* not having to write the same thing multiple times
	* don't repeat yourself
* we saw that in the previous slide
</section>

<section markdown="block">
###  Multiple Assignment

You can also assign __multiple values to multiple variable names simultaneously__.  &rarr;

This is done by:

* using the assignment operator: __=__
* a comma separated group of variables on the left-hand side
* a comma separated group of values on the right hand side

{% highlight python %}
a, b, c = 3, 21, 7
{% endhighlight %}

Each variable/value is bound in the order that they appear.
</section>

<section markdown="block">
###  Multiple Assignment Continued

{% highlight python %}
a, b, c = 3, 21, 7
{% endhighlight %}

__What values are referred to by a, b, and c? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
a -> 3
b -> 21
c -> 7
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Here's a Quick Exercise on a Tiny Algorithm
<aside>And Idioms, as Well!</aside>
__If I have two variables, a and b, and they are set to 3 and 21 respectively, how would I swap their values in code? (Try this on your own!) &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
a = 3
b = 21
print("a:", a, "b:", b)
c = b
b = a
a = c
print("a:", a, "b:", b)
{% endhighlight %}
[See the Python Tutor version](http://www.pythontutor.com/visualize.html#code=a+%3D+3%0Ab+%3D+21%0Aprint(%22a%3A%22,+a,+%22b%3A%22,+b)%0Ac+%3D+b%0Ab+%3D+a%0Aa+%3D+c%0Aprint(%22a%3A%22,+a,+%22b%3A%22,+b)&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&curInstr=0)
</div>
</section>

<section markdown="block">
###  An Idiomatic Way to Do It
<aside>(read: easier)</aside>
Here's another, more _idiomatic_ way to do it
{% highlight python %}
a = 3
b = 21
a, b = b, a
{% endhighlight %}
</section>

<section markdown="block">
###  ...And, Some BTWs

* in Python, if something is _idiomatic_, it's called _Pythonic_
* someone that codes in Python is sometimes called a _Pythonista_
* (yes, _really_)

</section>

<section markdown="block">
##  [Greeaaat.  Maybe we can use them to help us create our own functions!](functions.html)
</section>

