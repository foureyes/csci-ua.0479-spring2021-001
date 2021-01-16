---
layout: slides
title: Conditionals 
---

<section markdown="block" class="title-slide">
#  Conditionals
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Controlling Program Flow w/ Conditionals
A __conditional__ allows a decision to be made about which code path to take.  

* allows for __conditional__ execution of code.
* it uses __boolean values__ and __boolean expressions__ to evaluate a condition


What do you think the two possible values are for __boolean values__?

<div class="incremental" markdown="block">
* true
* false
</div>

</section>


<section markdown="block">
###  The bool Type
Python represents these boolean values using the __bool type__.  The __bool type__ has two possible values:

* True
* False 

Some things to pay attention to...

* both values start with an uppercase letter (you'll know you're doing it right in IDLE when they're highlighted appropriately &rarr;)
* these values are reserved words (keywords); they can't be used as variable names 
</section>

<section markdown="block">
###  Boolean Expressions / The Equality Operator
A __boolean expression__ is just an expression that eventually evaluates to a boolean value.  

* True evaluates to True
* False evaluates to False

The __equality operator__, __==__ (double equals), will test the left and right hand sides for equality and evaluate to the appropriate boolean value

* 1 == 1 evaluate to True
* "foo" == "foo" evaluates to True
* "foo" == "bar" evaluates to False

</section>

<section markdown="block">
###  if Statements
We use __if__ statements to conditionally execute code.  

* they start with the __keyword__ __if__
* ...followed by a __boolean expression__ and a colon
* the code that is to be executed if the condition is met is placed in an __indented code block__.

For example:

{% highlight python %}
if True:
	print("this is")
	print("true")
{% endhighlight %}

</section>

<section markdown="block">
###  if Statements continued
This will also work with equality operators and variables
{% highlight python %}
x = 5
y = 5
if x == y:
	print("x and y are equal")
{% endhighlight %}
</section>

<section markdown="block">
###   Let's Make a Game!
Let's try making a number guessing game.  Here's the expected output:
{% highlight python %}
Guess the number that I'm thinking of
>5
you got it!
{% endhighlight %}
</section>

<section markdown="block">
###  Review
* What's the equality operator in Python?
* What are the two possible values for the bool type?
* How do we write an if statement?
</section>

<section markdown="block">
##  [Next... a Quick Note on Statements, Expressions, Values](expressions.html)
</section>
