---
layout: slides
title: Statements, Expressions, Values 
---

<section markdown="block" class="title-slide">
#  Statements, Expressions, Values
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  Now That We've Seen Some Code...
<aside>Let's revisit some terminology.</aside>
</section>

<section markdown="block">
###  Statements

A __statement__ is:

* an instruction that the interpreter can execute
* think of a line of code
* some examples of statements that we've seen are:
	* assignment statement
	* if statement
* statements can contain __expressions__
</section>

<section markdown="block">
###  Expressions

An __expression__ is:

* a combination of __values__, __variables__, __operators__, __function calls__
* when __evaluated__, produces a result (a __value__)
* some examples of expressions:
	* 5 + 5
	* int("24")
	* input(">")

__When evaluated, what values do the above expressions produce?&rarr;__

<div class="incremental" markdown="block">
{% highlight bash %}
10, 24, "whatever string is typed in"
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Evaluating Expressions
<aside>Let's Take a Closer Look...</aside>

{% highlight pycon %}
>>> # values can't be evaluated further, the value just produces the value!
... 25
25
>>> # values with operators produce values
... 25 / 5
5.0
>>> # some function calls produce (return) values
... float("3")
3.0
{% endhighlight %}

</section>

<section markdown="block">
###  Expressions and Values

Because expressions can be reduced to values, we can use expressions where we would require values.

{% highlight pycon %}
>>> # in an assignment statement
... n = 2 ** 2
'24 hours'
>>> # using a function call as an operand
... str(24) + " hours"
'24 hours'
>>> # nesting function calls
... n = int(input("Please enter a number\n>"))
Please enter a number
>5
>>> # a variable by itself just produces its value
... v = "a value"
>>> v
'a value'
{% endhighlight %}

</section>
