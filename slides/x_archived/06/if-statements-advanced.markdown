---
layout: slides
title: If Statements - Advanced 
---
<section markdown="block" class="title-slide">
#  How to (Un)Complicate Things With If Statements
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  if Statements

__if__ statements allow for the conditional execution of code:

* {{ site.bookq }} refers to this as a __single alternative decision structure__
* there is only one _alternative_ path of execution that the code could veer off to

{% highlight python %}
if some_boolean_expression:
	print("do something")
{% endhighlight %}
</section>

<section markdown="block">
###  if-else Statements

__if-else__ statements will execute one block of code if the condition is true... or another block if it's false:

* {{ site.bookq }} refers to this as a __dual alternative decision structure__
* two possible paths of execution
* note that the if and else clause are part of the same structure

{% highlight python %}
if some_boolean_expression:
	print("do something")
else:
	print("do another thing")
{% endhighlight %}
</section>

<section markdown="block">
##  elif
<aside>Like Smashing Together Your Two Favorite Keywords</aside>
</section>

<section markdown="block">
###  elif Is the New _Else If_

We can use __elif__ to chain together a series of conditions.  This allows us to create multiple flows of execution (more than two), but - at most - only one path will be executed (__even if more than one condition is true__). 

* each condition is checked in order
* if the first is false, the next condition is checked
* this continues until the first true condition
* the body of code associated with that condition is executed
* the statement ends even if there are more conditions left
</section>

<section markdown="block">
###  elif Syntax

Let's see what it looks like...

{% highlight python %}
if condition_1:
	print("do something")
elif condition_2:
	print("do another thing")
elif condition_3:
	print("...and another thing")
elif condition_n:
	print("actually, any artibtrary number of things!")
else:
	print("else clause is optional")
	print("for conditions not caught above")
{% endhighlight %}
</section>

<section markdown="block">
###  elif Syntax Explained

* __if__ statement like usual
* go back one level of indentation to mark that the previous code block has ended
* keyword __elif__
* condition
* colon
* body - indented, body ends when indentation goes back one level
* not required obv
* __even if more than one true, only the first true executes!__
* can still add an __else__ at the end
</section>

<section markdown="block">
###  A Trivial elif Example

__Translate an athlete's finishing placement (1st, 2nd and 3rd) into its Olympic medal value: 1 for gold, 2 for silver, 3 for bronze and anything else means no medal &rarr;__.  Do this by asking for user input.  For example:

{% highlight python %}
What number should I translate into a medal?
>1
gold

What number should I translate into a medal?
>3
bronze

What number should I translate into a medal?
>23
no medal for you!
{% endhighlight %}
</section>

<section markdown="block">
###  Medals... Solution!

{% highlight python %}
{% include classes/06/medals_elif.py %}
{% endhighlight %}

</section>

<section markdown="block">
###  Another elif Example
<aside>Let's have some more cake...</aside>
__Let's do the cake exercise again using elif...__ &rarr;

{% highlight pycon %}
Do you want cake?
> yes
Here, have some cake.
#  > no ... no cake for you
#  > bleargh ... i don't understand
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/cake_elif.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  And How Did That Compare To Consecutive If Statements?

__We could have impemented this using consecutive if statements.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/cake_consecutive_ifs.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  An if in Your if

You can actually nest if statements within each other:

{% highlight python %}
if condition_1:
	print("condition 1 is true!")

	# nested if!
	if condition_2:
		print("in 2")

else:
	print("condition 1 is not true!")
{% endhighlight %}
</section>

<section markdown="block">
###  Let's See Cake With Nested If Statements

__We could have impemented this using nested if statements.__ &rarr;

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/06/cake_nested_ifs.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  And How Did That Compare To Consecutive Nested If Statements?

__What do you think the decision trees look like?.__ &rarr; (Oh, and BTW, what's a decision tree? ...It's a graph that shows all possible decisions and the outcomes of those decisions.)

<div class="incremental" markdown="block">
<div class="img-container" markdown="block">
![trees](../../resources/img/cake-decision-trees.png)
</div>
</div>
</section>

<section markdown="block">
###  And How About Speed?

__We could make an educated guess.__ &rarr;

<div class="incremental" markdown="block">
* elif skips conditions if one of the early conditions is true!
* that means, best case, there are less instructions for the computer to execute when using elif
	* compared to nested ifs
	* or consecutive ifs
* not sure what the interpreter/compiler does behind the scenes when it translates, though
	* could optimize things 
	* produce similar machine code for both kinds of code
</div>
</section>

<section markdown="block">
###  We're Not Finished Yet...
<aside>I'm bad at making decisions...</aside>

* __Add "maybe" as a potential answer?__ &rarr;  
* __Handle different ways of saying yes (like "yeah")?__ &rarr;

{% highlight python %}
Do you want cake?
> maybe
So, call me.

Do you want cake?
> yes
Here, have some cake.

Do you want cake?
> yeah
Here, have some cake.

{% endhighlight %}
</section>

<section markdown="block">
###  Adding 'yeah' and 'maybe'...

{% highlight python %}
{% include classes/06/cake_yeah_maybe.py %}
{% endhighlight %}
</section>

<section markdown="block">
###  Lastly, Everything Together

__Write a program that names the rolls of two dice in a dice game called craps...__ &rarr;

* ask the user for the values of two dice rolls.  
* output the [name of the roll](http://en.wikipedia.org/wiki/Craps#Rolling) using Wikipedia's article on Craps
* only check for the following rolls:
	* _Snake Eyes_
	* _Hard Four_ 
	* _Easy Four_  
* print out "I don't know yet" for any other rolls.  Example output:
* example interaction on next page
</section>

<section markdown="block">
###  Craps - Example Interaction

{% highlight python %}
What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 1
Snake Eyes!

What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 3
Easy Four
{% endhighlight %}
</section>

<section markdown="block">
###  Name That Craps Roll

{% highlight python %}
{% include classes/06/craps.py %}
{% endhighlight %}
</section>

<section markdown="block">
###  Nesting If Statements

* we saw this above to motivate our __elif__ example
* it behaves as you'd expect
* remember to get indentation right
* if there are multiple elif's or else's,  you can use indentation to see which initial if statement they belong to
* this works for any combination of if, elif and else
* note that sometimes nested if statements are equivalent to and
* best to simplify - that is, less nesting, better
</section>

<section markdown="block">
###  Nesting If Statements Example

The coffee shop has a special for half price pastries on Fridays after 4 (16:00... or 16).  __Ask for day and time, and make a recommendation (buy now, wait x hours or don't buy).__ &rarr;

{% highlight python %}
What day is it (ex Thursday, Friday, etc.)?
> Friday
What time is it (in 24 hour time)?
> 17
Go ahead, you deserve a treat

What day is it (ex Thursday, Friday, etc.)?
> Friday
What time is it (in 24 hour time)?
> 12
Just wait 4 more hours
{% endhighlight %}

</section>

<section markdown="block">
###  Pastry Buying Guide

{% highlight python %}
{% include classes/06/pastry_buying_guide.py %}
{% endhighlight %}
</section>


<section markdown="block">
###  How to Order Conditions

* if more than one condition in a series of elif's is true 
	* only the first true condition is executed!
	* other are skipped, including else
* be careful of conditions that never get evaluated 
	* an above condition may already account for it
	* here's an example...
</section>

<section markdown="block">
###  Ordering Conditions Continued!

The intention of the following code is to:

* determine if a number is 101 or greater than 100
* if it's 101, it should only print out "exactly 101" (it should not print out greater than 100)

__What gets printed if n = 200?  What if n = 101?__   &rarr;

{% highlight python %}
if n > 100:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}

<div class="incremental" markdown="block">
200 &rarr; more than 100, 101 &rarr; more than 100
</div>

</section>

<section markdown="block">
###  How to Order Conditions Continued Some More!

__Of course, we could fix this.  There are a few ways...__ &rarr;

<div class="incremental" markdown="block">
* reordering
* using and
{% highlight python %}
if n == 101:
	print("exactly 101")
elif n > 100:
	print("more than 100")

if n > 100 and n != 101:
	print("more than 100")
elif n == 101:
	print("exactly 101")
{% endhighlight %}
</div>
</section>

<section markdown="block">
##  Equivalent Conditions
</section>

<section markdown="block">
###  Logical Opposites 
A way to get rid of not operators is to use the opposite logical operator:

[Logical Opposites from {{ site.bookt }} ](http://openbookproject.net/thinkcs/python/english3e/conditionals.html)

Examples of logical opposites:

* the logical opposite of &gt; is &lt;=
* the logical opposite of &lt; is &gt;=

Consequently

* not &gt; is the same as &lt;=
* not &lt; is the same as &gt;=

</section>

<section markdown="block">
###  Logical Opposites Continued
__How can we rewrite this without the not?__&rarr;

{% highlight python %}
#  Example from {{ site.bookt }}
if not (age >= 17):
    print("Hey, you're too young to get a driving licence!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
if age < 17:
    print("Hey, you're too young to get a driving licence!")
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  De Morgan's Law
* not (x and y)  ==  (not x) or (not y)
* not (x or y)   ==  (not x) and (not y)
* {{ site.bookt }} example
	* uses combination of logical opposites and De Morgan's Law
	* clarity / closeness to original 

__Let's try truth tables for these!__ &rarr;
</section>

<section markdown="block">
###  De Morgan's Law Truth Tables

{% highlight bash %}
x | y | not (x and y)   x | y | (not x) or (not y)
=====================   =========================
t | t | f               t | t | f
t | f | t               t | f | t
f | t | t               f | t | t
f | f | t               f | f | t

x | y | not (x or y)   x | y | (not x) and (not y)
====================   ===========================
t | t | f              t | t | f
t | f | f              t | f | f
f | t | f              f | t | f
f | f | t              f | f | t
{% endhighlight %}
</section>

<section markdown="block">
###  De Morgan's Law 
__How can we rewrite this fragment of code from {{ site.bookt }}?__&rarr; 

{% highlight python %}
#  "suppose we can slay the dragon only if our magic lightsabre sword 
#  is charged to 90% or higher, and we have 100 or more energy units 
#  in our protective shield." 

if not ((sword_charge >= 0.90) and (shield_energy >= 100)):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
#  first... demorgan's: 
if not (sword_charge >= 0.90) or not (shield_energy >= 100):
	# ...
{% endhighlight %}

{% highlight python %}
#  next... logical opposites:
if (sword_charge < 0.90) or (shield_energy < 100):
	# ...
{% endhighlight %}
</div>
</section>

<section markdown="block">
##  Truthiness and Style
</section>

<section markdown="block">
###  Truthiness

See this [crazy chart](http://docs.python.org/py3k/library/stdtypes.html#truth-value-testing) on the _intrinsic_ boolean value of various types.  The following values are considered false:

* None
* False
* 0 of any numeric type (0.0, 0)
* empty mapping or sequence type (We'll look at these later) - this includes the empty string '', "", etc.
</section>

<section markdown="block">
###  Truthiness Examples

{% highlight python %}
a = ""
if a:
	print("true!")

a = 0
if a:
	print("true!")

a = "foo"
if a:
	print("true!")
{% endhighlight %}

</section>

<section markdown="block">
###  Using Logical Operators

__What's the difference between the following two code samples?__&rarr;
{% highlight python %}
#  sample 1
answer = 'no'
if answer == 'yes' or answer == 'YES' or answer == 'Yes':
	print('you said yes')
else:
	print('you said no')

#  sample 2
if answer == 'yes' or 'YES' or 'Yes':
	print('you said yes')
else:
	print('you said no')
answer = 'no'
{% endhighlight %}
</section>

<section markdown="block">
###  Using Logical Operators Continued

{% highlight python %}
#  boolean expression in sample 1
answer == 'yes' or answer == 'YES' or answer == 'Yes':

#  boolean expression in sample 2
answer == 'yes' or 'YES' or 'Yes':
{% endhighlight %}

* the second one always ends up being True (the other values in the boolean expression are treated as true)
	* __or 'YES'__ can be translated as __or True__!
	* which means you always get back True!
* you should have the full comparison operator along with operands to prevent this from happening
</section>

<section markdown="block">
###  Another Note About Style
* remember idioms?
* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#testing-for-truth-values
* more elegant to test intrinsic truth values than using equality operator
{% highlight python %}
b = True
#  instead of if b == True
if b:
	print("b")

s = "catz!"
#  to test if the value is not empty string 
#  (rather than s != "")
if s:
	print(s)

{% endhighlight %}

</section>

<section markdown="block">
###  Let's Write a Mini Quiz Game!

__Write a program to ask a couple of questions about the book, Dune.__ &rarr;

{% highlight python %}
#   ______            _        _______ 
#  (  __  \ |\     /|( (    /|(  ____ \
#  | (  \  )| )   ( ||  \  ( || (    \/
#  | |   ) || |   | ||   \ | || (__    
#  | |   | || |   | || (\ \) ||  __)   
#  | |   ) || |   | || | \   || (      
#  | (__/  )| (___) || )  \  || (____/\
#  (______/ (_______)|/    )_)(_______/
#  
#  What is the name of the desert planet that's informally called Dune?
#  > Arrakis
#  You got it right!
#  What valuable resource is only found on Dune?
#  > cheese?
#  Nope, the answer is: spice
#  You got 1 questions right! 
{% endhighlight %}
</section>

<section markdown="block">
###  Let's Write a Mini Quiz Game (Continued)!

Let's get some requirements down:

* ask two questions sequentially
* keep track of the number of questions that the player got right
* output the number of questions right
* (optional) keep track of the number of questions wrong, and output that as well
* (optional) ask for the player's name and greet the player

</section>

<section markdown="block">
###  We Don't Have To Jump Right Into Code!

__So, first, what's our plan?__ &rarr;

* flow chart?
* pseudocode?
</section>

<section markdown="block">
###  Let's Write a Mini Quiz Game! (Continued Some More)!

What are some ways that we can be more tolerant about capitalization?  That is... what if we wanted to accept these answers:

1. Arrakis / arrakis
2. spice / the spice / the spice melange

Another wrinkle might be to have different output based on which version of the _right_ answer was chosen.  For example, if someone puts in spice, it might say, "oh, you mean, _the spice melange_".
</section>

<section markdown="block">
##  [Built-In Modules Are Up Next!](built-in-modules.html)
</section>
