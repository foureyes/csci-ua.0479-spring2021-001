---
layout: slides
title: If Statements 
---

<section markdown="block" class="title-slide">
#  If Statements / Conditionals
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Controlling Program Flow w/ Conditionals

__What does an if statement allow you to do? &rarr;__

<div class="incremental" markdown="block">
* allows for __conditional__ execution of code.
* the condition that is used to determine which code path to take is:
	* either a __boolean value__ 
	* or some sort of __boolean expression__ (an expression that evaluates to a boolean value)
</div>
</section>

<section markdown="block">
###  Boolean Values

__What are the two possible boolean values, and how are they represented in Python? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
#  note the uppercase!

True
False
{% endhighlight %}
</div>
</section>


<section markdown="block">
###  Boolean Expressions / The Equality Operator

Again, a  __boolean expression__ is just an expression that eventually evaluates to a boolean value.  Let's look a boolean expression that uses the __equality operator__.

The __equality operator__, __==__ (double equals), will test the left and right hand sides for equality and evaluate to the appropriate boolean value

* 1 == 1 evaluates to True
* "foo" == "foo" evaluates to True
* "foo" == "bar" evaluates to False


</section>

<section markdown="block">
###  The Equality Operator Continued

When two values are compared, and they are of different types (except if they're both numeric), they are never considered equal.  For example, all of the following comparisons evaluate to False:

* 1 == "one"
* 1 = "1.0"
* 1 == "1" 

However, this gives us True (different types, but both types are numeric):

* 1 == 1.0

</section>

<section markdown="block">
###  if Statement Syntax
Again, __if__ statements allow conditional code execution.

1. start with the __keyword__ __if__
2. ...followed by a __boolean expression__ 
3. which ends with a __colon__
4. the code that is to be executed if the condition is met is placed in an __indented code block__.
5. once the indentation goes back one level, the __body__ of the if-statement ends

{% highlight python %}
if 1 == 1:
	print("this is")
	print("true")

#  now we're out of the if statement
print("outta here")
{% endhighlight %}

</section>

<section markdown="block">
###  if Statements continued

The equality operator also works with variables:

{% highlight python %}
x = 5
y = 5
if x == y:
	print("x and y are equal")
{% endhighlight %}
</section>


<section markdown="block">
###  A Quick Exercise

__Let's try writing an if statement that checks if the variables a and b are equal.  If they're equal, print the sum of a and b, and then print out the product of both a and b. &rarr;__
{% highlight python %}
a, b = 2, 2 
{% endhighlight %}
</section>

<section markdown="block">
###  A Potential Solution 

* begin with keyword __if__
* condition
* colon - ends the condition / marks that a block of code is about to come up
* if + condition + colon usually is considered the __if-statement header__
* indented block of code is the body of the if-statement

<div class="incremental" markdown="block">
{% highlight python %}
a, b = 2, 2 
if a == b:
	print(a + b)
	print(a * b)
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Let's See That Again
<aside>Now With More Blank Lines</aside>

* the body of an if statement ends when indentation goes back one level
* blank lines don't count as ending a block of code!

{% highlight python %}
a, b = 2, 2 
if a == b:
	# totally ok?  yes!
	print a + b


	print a * b

{% endhighlight %}
</section>

<section markdown="block">
###  Oh Yeah, Else What?

We can use __else__ to execute code if the original condition was not met.  After the body of an if-statement, add the following:

* go back one level of indentation to mark that the previous code block has ended
* keyword __else__, immediately followed by a colon
* body - indented, body ends when indentation goes back one level
* (this whole __else clause__ is totally optional; it's not required)
</section>

<section markdown="block">
###  An if/else Example

__What does this code print out?__

{% highlight python %}
a, b = 2, 2 
if a == b:
	print("they're the same!")
else:
	print("they're different")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight bash %}
they're the same!
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  An if/else Example

__What does this code print out?__

{% highlight python %}
a, b = 2, 20 
if a == b:
	print("they're the same!")
else:
	print("they're different")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight bash %}
they're different
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  An if Example

__What does this code print out?__

{% highlight python %}
a, b = "foo", 20 
if a == b:
	print("they're the same!")

print("hello!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight bash %}
hello!
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  Another if Example

__What does this code print out?__

{% highlight python %}
a, b = "foo", "foo" 
if a == b:
	print("they're the same!")

print("hello!")
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight bash %}
they're the same!
hello!
{% endhighlight %}
</div>
</section>

<section markdown="block">
###   Let's Make a Game!
__Try writing a number guessing game. &rarr;__  

* keep track of a _secret number_ (choose whatever int value you'd like)
* ask the user for a number
* if the number entered matches the secret number, print "you got it!"
* if it doesn't match, print "nope, I was thinking of ..." and the secret number
</section>

<section markdown="block">
###  Example Interaction
{% highlight bash %}
Guess the number that I'm thinking of
>4
Nope, I was thinking of 10
{% endhighlight %}

{% highlight bash %}
Guess the number that I'm thinking of
>10
You got it!
{% endhighlight %}
</section>

<section markdown="block">
###   A Potential Solution

{% highlight python %}
secret = 10
guess = input('Guess the number that I\'m thinking of\n>')
if int(guess) == 10:
    print('You got it!')
else:
    print('Nope, I was thinking of ' + str(secret))
{% endhighlight %}

</section>

<section markdown="block">
###  Review
* What's the equality operator in Python?
* What happens if I compare two different types using the equality operator?
* What are the two possible values for the bool type?
* What's the syntax for an if statement?
* What statements do I use if I want either one branch of code to execute or another?
</section>

<section markdown="block">
##  [Next... a Quick Note on Statements, Expressions, Values](expressions.html)
</section>
