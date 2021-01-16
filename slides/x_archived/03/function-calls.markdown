---
layout: slides
title: Calling Built-In Functions 
---

<section markdown="block" class="title-slide">
#  Calling Built-In Functions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Built-In Functions

Based on the previous slides, __name some functions that we've learned so far__ &rarr;

<div class="incremental" markdown="block">
(Remember, a __function__ is a named sequence of statements that performs a specific task or useful operation)

1. print
2. type
3. int
4. float
5. str

</div>
</section>

<section markdown="block">
###  Using Built-In Functions

How do you use (_call_) built-in functions in your code?  __How would you call the function, str, on a value, 300 (that is, convert 300 to a string)?__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
"""
1. start with the function name, str
2. use parentheses to signify that you're calling a function
3. within those parentheses, put in the value that you're passing in, 300
"""
str(300)
{% endhighlight %}
</div>
</section>

<section markdown="block">
##  Parentheses after a function name signify that you're calling (executing) that function!
</section>

<section markdown="block">
###  Using Built-In Functions with Multiple Input Values

1. again start with the function name
2. use parentheses to signify that you're calling a function
3. within those parentheses, put in the values, __separated by commas__, that you're passing in

{% highlight python %}
"""
print can take multiple values as inputs
this contrived example shows two strings as inputs to print
"""

print("Hi ", "there")
{% endhighlight %}
</section>


<section markdown="block">
###  Some Terminology

* __call__ - using a function in your code, executing a function
* __arguments__ - the actual literal values that a function is called with; 25 is the argument in _print(25)_
* __parameters__ - within the function itself, the names given to the values passed in (we'll see more about this when we create our own functions)
* __passing__ arguments into a function - providing input values to a function 
* __return__ value - the value that's given back to your program after _calling_ a function (returning a value __doesn't mean printing out a value__)

</section>

<section markdown="block">
###  Talkin' the Talk

Using this code as an example:

{% highlight python %}
num = "5"
x = int(num)
{% endhighlight %}

1. __what is the name of the function being called?__ &rarr;
2. __what are the arguments passed in to the function?__ &rarr;
3. __what value is returned from this function call?__ &rarr;

<div class="incremental" markdown="block">
1. int
2. num, or the string, "5"
3. the integer, 5
</div>
</section>

<section markdown="block">
###  Talkin' the Talk 2


{% highlight python %}
length = 10
width = 7
print(length, width)
{% endhighlight %}

1. __what is the name of the function being called?__ &rarr;
2. __what are the arguments passed in to the function?__ &rarr;

<div class="incremental" markdown="block">
1. print
2. the integers, length and width (10 and 7 respectively)

Note that __print does not return a value to your program; rather it _prints_ values to the screen__.
</div>
</section>


<section markdown="block">
###  Composing Functions

* you can call functions within functions
* the value returned by the inner function calls are what's used as arguments to the outer function call

{% highlight python %}
t = type(str(5 + 5))
print(t)
{% endhighlight %}

__What is printed out by this program?__ &rarr;

<div class="incremental" markdown="block">
The type of the result of calling str(5 + 5), which __turns out to be?__ &rarr;

{% highlight python %}
<class 'str'>
{% endhighlight %}
</div>
</section>

<section markdown="block">
##  [A Closer Look At a Built-In Function Called Input](input-review.html)
</section>
