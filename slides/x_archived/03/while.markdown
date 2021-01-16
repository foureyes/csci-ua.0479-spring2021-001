---
layout: slides
title: While Loops 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Write a Program to Print out the numbers 1 through 5
</section>

<section markdown="block">
## Motivation for Loops

A program to count from 1 to 5

<pre><code data-trim contenteditable>
n, delta = 1, 1
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
n = n + delta
print(n)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Motivation for Loops Continued

Um.  That was _kind of tedious_.  Can't we just tell the computer to repeat those two lines of code?  

__YES! ...using loops__

<pre><code data-trim contenteditable>
n = 1
end = 5
delta = 1

while n <= end:
	print(n)
	n = n + delta
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Iteration and Loops

Some formal definitions:

* __iteration__ - repeated execution of a set of programming statements.
* __loop__ - the construct that allows us to repeatedly execute a statement or a group of statements until a terminating condition is satisfied.
* sometimes these words are used interchangeably
</section>

<section markdown="block">
## While Loops

Using a __while__ loop allows us to:

* repeat a block of code
* ...as long as a condition is met
* stops as soon as the condition is no longer true
* looks similar to an if statement
</section>

<section markdown="block">
## While Loop Syntax

A template:

<pre><code data-trim contenteditable>
# while &lt;some sort of condition&gt;:
#	&lt;do stuff here&gt;
</code></pre>

Some _real_ code:

<pre><code data-trim contenteditable>
a = 100
while a > -1:
	print(a)
</code></pre>

__What does this output? &rarr;__

<div class="fragment">
<pre><code data-trim contenteditable>
100
100
100
</code></pre>
</div>
</section>

<section markdown="block">
## Trivial Cases, Again

__What do these snippets of code print out?&rarr;__
<pre><code data-trim contenteditable>
while True:
	print("I'm true!")
</code></pre>
<pre><code data-trim contenteditable>
while False:
	print("I'm false!")
</code></pre>

<div class="fragment">
<pre><code data-trim contenteditable>
I'm true!
I'm true!
I'm true!
</code></pre>
<pre><code data-trim contenteditable>
# nothing printed here
</code></pre>
</div>
</section>

<section markdown="block">
## Let's Step Through True
<pre><code data-trim contenteditable>
while True:
	print("I'm true!")
</code></pre>

1. condition is true
2. print "I'm true!"
3. go back to top
4. condition is true
5. print "I'm true!"
6. go back to top
7. you know the _deal_
</section>

<section markdown="block">
## Let's Step Through False
<pre><code data-trim contenteditable>
while False:
	print("I'm false!")
</code></pre>

1. condition is false

We never even get into the body of the loop!
</section>

<section markdown="block">
## Slightly More Complicated
<aside>Well, Not This One Exactly, But You'll See</aside>

__What does this print out? &rarr;__

<pre><code data-trim contenteditable>
keep_on_going = True
while keep_on_going:
	print("I'm going!")
</code></pre>

<div class="fragment">
<pre><code data-trim contenteditable>
I'm going
I'm going
I'm going
.
.
I'm going
</code></pre>
</div>
</section>

<section markdown="block">
## Slightly More Complicated Continued

__Let's add one line.  What does this print out? &rarr;__

<pre><code data-trim contenteditable>
keep_on_going = True
while keep_on_going:
	print("I'm going!")
	keep_on_going = False
</code></pre>

<div class="fragment">
<pre><code data-trim contenteditable>
I'm going
</code></pre>
</div>
</section>

<section markdown="block">
## Slightly More Complicated Continued Continued

Going through each iteration

<pre><code data-trim contenteditable>
keep_on_going = True
while keep_on_going:
	print("I'm going!")
	keep_on_going = False
</code></pre>

* condition (keep_on_going) is true 
* print "I'm going!"
* set keep_on_going to false
* condition (keep_on_going) is false

Loop ends after one iteration.
</section>

<section markdown="block">
## What Happened There?

* we had some state __outside__ of the loop
* __within__ the loop we mutated / changed that state to eventually get out of the condition
* consequently, the loop _terminates_
* sometimes we call these kinds of variables __sentinel__ variables
* they only let certain conditions in!
</section>

<section markdown="block">
## Affecting the Outcome of the Condition

To change the outcome of your conditional:

* maintain state 
	* declare a variable __outside__ of the loop!
* mutate that state on loop iteration 
	* change that variable __inside__ the loop!
	* this will eventually cause the conditional to fail
* examples:
	* using operators to change a variable in your condition
	* using input to change a variable in your condition
</section>

<section markdown="block">
## Figuring Out How to Write a While Loop

Before you write your while loop, __you should probably first determine__...

* if your code needs a while loop _at all_ (is there repeated code)
* if there's data that affects whether or not the loop will continue running
* what condition will make your loop repeat
* how your loop will end
</section>


<section markdown="block">
## Count From 2 Through 8 By 2's

__How would you implement this?&rarr;__

<div class="fragment">
<pre><code data-trim contenteditable>
count = 2
while count <= 8:
	print(count)
	count = count + 2
</code></pre>
</div>
</section>

<section markdown="block">
## Stepping Through Counting By 2's
<pre><code data-trim contenteditable>
count = 2
while count <= 8:
	print(count)
	count = count + 2
</code></pre>
1. count is 2
2. condition is true because count (2) is less than 8
3. print count
4. add 2 to count... count is now 4
5. condition is true because count(4) is less than 8..
6. goes on until count gets to 10, at which point condition is no longer true

[Check out the fancy step through](http://www.pythontutor.com/visualize.html#code=count+%3D+0%0Awhile+count+%3C%3D+8%3A++++%0A++++print(count)%0A++++count+%3D+count+%2B+2&mode=display&cumulative=false&py=2&curInstr=0)
</section>

<section markdown="block">
## Odd Numbers Except 13

__Write a program that... &rarr;__

* prints all of the odd numbers from 1-99
* skips 13

There are a few ways to do this!  __What are some general strategies for solving this problem?&rarr;__

<div markdown="block" class="fragment">

* using modulo
* or incrementing by twos

</div>
</section>

<section markdown="block">
## Possible Solutions for Odd Numbers Except 13
 
[Increment by 2's](http://www.pythontutor.com/visualize.html#code=n+%3D+1%0Awhile+n+%3C%3D+99%3A%0A++++if+n+!%3D+13%3A%0A++++++++print(n)%0A++++n+%3D+n+%2B+2&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)

<pre><code data-trim contenteditable>
n = 1
while n <= 99:
    if n != 13:
        print(n)
    n = n + 2
</code></pre>

[Using modulo to determine odds](http://www.pythontutor.com/visualize.html#code=n+%3D+1%0Awhile+n+%3C%3D+99%3A%0A++++if+n+!%3D+13%3A%0A++++++++print(n)%0A++++n+%3D+n+%2B+2&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)

<pre><code data-trim contenteditable>
n = 1
while n <= 99:
    if n % 2 == 1 and n != 13:
        print(n)
    n = n + 1
</code></pre>
</section>

<section markdown="block">
## Do You Want Cake (Again)

__Repeatedy ask if user wants cake until user says yes or yeah.  How would you implement this?&rarr;__

<pre><code data-trim contenteditable>
Do you want cake?
> no
Do you want cake?
> No
Do you want cake?
> yeah
Have some cake!
</code></pre>

<div class="fragment">
<pre><code data-trim contenteditable>
answer = 'no'
while answer != 'yes' and answer != 'yeah':
	answer = input("Do you want cake?\n> ")
print("Have some cake!")
</code></pre>
</div>
</section>

<section markdown="block">
## Stepping Through Cake

Let's make an assumption that the user enters "no" first, and then "yeah" second.

<pre><code data-trim contenteditable>
answer = 'no'
while answer != 'yes' and answer != 'yeah':
	answer = input("Do you want cake?\n> ")
print("Have some cake!")
</code></pre>

1. answer is set to no by default
2. condition is true, answer (no) is not 'yes' or 'yeah'
3. answer is set to user input of 'no'
4. condition is true, answer (no) is not 'yes' or 'yeah'
5. answer is set to user input of 'yes'
6. condition is false, answer != 'yeah' is now false!
7. have some cake is printed
</section>

<section markdown="block">
## Accumulating Values

__Write a program that will: &rarr;__ 

* continually ask the user for a number (__forever__)
* add that number to a running total
* print out the running total

<pre><code data-trim contenteditable>
Give me a number to add
> 10
Current total is 10
Give me a number to add
> 15
Current total is 25
Give me a number to add
> 5
Current total is 30
Give me a number to add
> 
</code></pre>

</section>

<section markdown="block">
## Potential Solution for Accumulating Values

<pre><code data-trim contenteditable>
total = 0
while True:
    n = int(input("Give me a number to add\n> "))
    total = total + n
    print("Current total is " + str(total))
</code></pre>

</section>

<section markdown="block">
## A Difficult One... 

__Write a program that continually asks the user for numbers, and asks them if they'd like to keep going.  In the end, it should output the average of all of the numbers entered&rarr;__

<pre><code data-trim contenteditable>
I'll calculate the average for you!
Current total: 0
Numbers summed: 0
Please enter a number to add
> 10
Do you want to continue adding numbers (yes/no)?
> yes
Current total: 10
Numbers summed: 1
Please enter a number to add
> 12
Do you want to continue adding numbers (yes/no)?
> no
The average is 11.0
</code></pre>
</section>

<section markdown="block">
## Some Hints, Please?
Let's try keeping track of multiple variables:

* a user's answer to whether or not the program should continue
* the total (sum) of the numbers that a user has entered 
* the count of numbers input
</section>

<section markdown="block">
## An Average Solution

<pre><code data-trim contenteditable>
total = 0
count = 0
answer = 'yes'
print("I'll calculate the average for you!")
while answer == 'yes':
        print("Current total: " + str(total))
        print("Numbers summed: " + str(count))
        total = total + int(input("Please enter a number to add\n> "))
        count = count + 1
        answer = input("Do you want to continue adding numbers (yes/no)?\n> ")
print("The average is "+ str(total / count))
</code></pre>
</section>

<section markdown="block">
## Increment / Decrement

We've used the following syntax to increment or decrement a variable

<pre><code data-trim contenteditable>
n = 0
n = n + 1

n = 100
n = n - 1
</code></pre>

_Slightly_ tedious...
</section>

<section markdown="block">
## Increment / Decrement Continued

There's some _syntactic sugar_ that makes doing this less verbose:  use __+=__ or __-=__

* __n += 1__ is the same as n = n + 1
* __n -= 1__ is the same as n = n - 1

<pre><code data-trim contenteditable>
n = 0
# adds one to n and binds the resulting value to n
n +=  1

n = 100
# subtracts one to n and binds the resulting value to n
n -= 1
</code></pre>

</section>

<section markdown="block">
## More Syntactic Sugar

This works for other operators too.   __What does this code print out? &rarr;__

<pre><code data-trim contenteditable>
n = 2
n *= 2
n *= 2
print(n)

n = 64
n /= 2
n /= 2
print(n)
</code></pre>
<div class="fragment">
<pre><code data-trim contenteditable>
8
16.0
</code></pre>
</div>

</section>

<section markdown="block">
## What About Strings?

Also works with strings....   __What does this code print out? &rarr;__
<pre><code data-trim contenteditable>
s = "h"
s += "e"
s += "y"
s *= 3
print(s)
</code></pre>

<div class="fragment">
<pre><code data-trim contenteditable>
heyheyhey
</code></pre>
</div>

<!-- remove asterisk* -->
</section>

<section markdown="block">
## Other Exercises

* count the number of digits in an int
	* repeatedly use integer division
	* ...until the original number becomes 0
	* keep count of divisions
* continually add exclamation points to a word
	* ask for a word
	* ask for x number of exclamation points
	* print out resulting word and exclamation points
	* continue asking for another word and exclamation points
</section>
