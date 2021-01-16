---
layout: slides
title: For Loops 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  Loops, In General

Does anyone remember the two broad  __categories__ of loops?  __What are they, and how are they different?__ &rarr;

<div class="fragment" markdown="block">
* __condition-controlled__ - repeats as long as a condition is true
* __count-controlled__ - repeats a specific number of times
</div>
</section>

<section markdown="block">
##  Condition Controlled Loops in Python

__What programming construct (repetition structure) do we use in Python to create a condition-controlled loop?__ &rarr;

<div class="fragment" markdown="block">
A __while__ loop is a repetition structure in Python that repeats a block of code as long as a check for a particular condition is true.
</div>
</section>

<section markdown="block">
##  Count-Controlled Loops

<aside>In Python, <em>for loops</em> are count-controlled loops.</aside>

</section>

<section markdown="block">
##  For Loops

An Example

<pre><code data-trim contenteditable>
for i in range(5):
    print(i)
</code></pre>

Its output:

<pre><code data-trim contenteditable>
0
1
2
3
4
</code></pre>
</section>


<section markdown="block">
##  For Loop Syntax

__for loops__ repeat code by iterating over every item in some group / collection of items:

<pre><code data-trim contenteditable>
"""
for &lt;loop variable&gt; in &lt;iterable object&gt;:
    (&lt;loop variable&gt; can be used here)
"""

</code></pre>

Again, the same example:

<pre><code data-trim contenteditable>
"""
 keyword    loop    an iterable object,
     for  variable  like range
       |     |      |
       |     |      |
        for i in range(5):
              print(i)
"""
</code></pre>
</section>

<section markdown="block">
##  Let's Break That Down a Bit

A __for__ loop:

* consists of the keyword __for__ (obvs!)
* followed by a __loop variable__ (this could be named anything you like)
* followed by some __iterable object__ (some sequence of values)
* followed by a colon
* in this case, the iterable object is returned by the __range__ function
* the range function returns an arithmetic sequence of numbers
* in this case, that sequence is [0, 1, 2, 3, 4]
</section>


<section markdown="block">
##  For Loops - Details, Details, Details
</section>

<section markdown="block">
##  What Does It Do?

A __for__ loop:

* repeats a block of code for a specific number of times
* it does this by running through all of the elements in a sequence, one at a time
* the current element can be accessed in the body of the for loop using the __loop variable__
* (note that the __loop variable__ is called __target variable__ in {{ site.bookq }})
* that is... for each element in your sequence, the __loop variable__ is set to that element
</section>

<section markdown="block">
##  For Loops

A more technical explanation is: __for loops__ iterate over every item in an __iterable object__.  

An _iterable object_:

* is a _thing_ (_object_) that contains other values / _members_
* is capable of returning each of its members __one at a time__
* examples of iterable objects include: 
	* strings (we know these)
	* __range objects__ (we'll learn these today)
	* lists (for the future!)
* so... let's see about these __range objects__
</section>

<section markdown="block">
##  Range and Range Objects

A __range__ object is another data type!  It represents an _arithmetic sequence_, such as 0, 1, 2, 3, 4.

* a __range__ object is created by calling the range() function.
* with one argument, it creates an arithmetic sequence from 0 up to but __not including__ that argument
* consequently, range(5) produces 0, 1, 2, 3, 4
* to see the elements in a range, you can use the __list()__ function
* (we'll learn more about lists later!)
</section>

<section markdown="block">
##  Showing the Results of Range

__Let's see if we can make sense of this:__ &rarr;

<pre><code data-trim contenteditable>
#  make a range object - an arithmetic sequence from 0 through 5
numbers = range(5)

#  let's look at that object
print(numbers)

#  what type is it?
print(type(numbers))

#  can we actually see the sequence?  yes, but we have to use list.
print(list(numbers))
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
range(0, 5)
<class 'range'>
[0, 1, 2, 3, 4]
</code></pre>
</div>
</section>

<section markdown="block">
##  So... All of That Meant...

* there's a type called __range__
* the string representation of a range shows you the original arguments that you passed in
* you can call the built-in __list__ function (used to convert value into a list) to show the exact ints in the list
</section>

<section markdown="block">
##  Quick Summary So Far...

We've learned two new built in functions

* __range__ returns a range _object_, a representation of an arithmetic sequence
* __list__ returns a list _object_
	* for now, we use list in combination with print  to show each number in a range object
	* we'll learn more about lists later
</section>

<section markdown="block">
##  Range Life...

<aside>The built-in function, range(), creates range objects - convenient, eh?</aside>
</section>

<section markdown="block">
##  Range 

__range()__ returns a __range object__, an arithmetic sequence of numbers.  

* one argument: __range__(stop) 
	* returns a series of numbers starting with 0, up to, but not including _stop_ by ones
	* range(3) &rarr; 0, 1, 2
* two arguments: __range__(start, stop) 
	* returns a series of numbers starting with _start_ , up to, but not including _stop_ by ones
	* range(5, 10) &rarr; 5, 6, 7, 8, 9
* three arguments: so many arguments, you'll have to go to the next slide &rarr;
</section>

<section markdown="block">
##  Range (Continued)

(continued from previous slide)

* three arguments: __range__(start, stop, step)
	* returns a series of numbers starting with _start_ , up to, but not including _stop_ by _step_
	* range(4, 9, 2) &rarr; 4, 6, 8
</section>

<section markdown="block">
##  Some Other Things You Should Know About Range

* negative _step_ goes backwards
	* range(8, 3, -2) &rarr; 8, 6, 4
* printing the result of a range object just gives you the original arguments that you used to call range
	* print(range(8, 3, -2)) &rarr; range(8, 3, -2)
* use the list function to show the elements in a range
	* print(__list__(range(8, 3, -2)))
</section>

<section markdown="block">
##  Guess That Series of Numbers

__Given the following calls range , what is the start, stop, and step?  What is the resulting arithmetic sequence? &rarr;__

<pre><code data-trim contenteditable>
range(3)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
#  start:0, end:3, step:1
0, 1, 2
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
range(10, 16)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
#  start:10, end:16, step:1
10, 11, 12, 13, 14, 15
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
range(-2, 3)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
#  start:-2, end:3, step:1
-2, -1, 0, 1, 2
</code></pre>
{:.fragment}

</section>

<section markdown="block">
##  Guess That Series of Numbers

__What is the start, stop, and step... and the sequence? &rarr;__


<pre><code data-trim contenteditable>
range(200, 501, 100)
</code></pre>

<pre><code data-trim contenteditable>
#  start:200, end:501, step:100
200, 300, 400, 500
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
range(0, 10, 5)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
#  start:0, end:10, step: 5
0, 5
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
range(5, -11, -5)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
#  start:5, end:-11, step:-5
5, 0, -5, -10
</code></pre>
{:.fragment}
</section>


<section markdown="block">
##  For Loop Examples
</section>

<section markdown="block">
##  And Now, Back to For Loops
<aside>A Slightly Different Example</aside>

<pre><code data-trim contenteditable>
for whatevs in range(1, 4):
    print(str(whatevs) + " Mississippi")
</code></pre>

* notice the different loop variable name, _whatevs_?
* __What does this snippet of code output?__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
1 Mississippi
2 Mississippi
3 Mississippi
</code></pre>
</div>
</section>

<section markdown="block">
##  Let's Take a Closer Look

<pre><code data-trim contenteditable>
for whatevs in range(1, 4):
   	print(str(whatevs) + " Mississippi")
</code></pre>

__Going over this step-by-step, what is the value of whatevs, and what is printed? &rarr;__

<div class="fragment" markdown="block">
* range(4) gives a sequence of 1, 2, 3
* first iteration, the loop variable, whatevs, is 1
* "1 Mississippi" is printed
* next iteration, the loop variable, whatevs, is 2
* "2 Mississippi" is printed
* next iteration, the loop variable, whatevs is 3
* "3 Mississippi" is printed
</div>
</section>

<section markdown="block">
##  Another For Loop Example
<pre><code data-trim contenteditable>
for num in range(6, 13, 3):
    result = num * num
    print(str(num) + " squared is " + str(result))
</code></pre>

__And... step-by-step, that's: &rarr;__

<div class="fragment" markdown="block">
* the sequence is 6, 9, 12
* __num__: 6, __result__: 36, 6 squared is 36
* __num__: 9, __result__: 81, 9 squared is 81
* __num__: 12,__result__: 144, 12 squared is 144

[And by using pythontutor.com](http://www.pythontutor.com/visualize.html#code=for+num+in+range(6,+13,+3)%3A%0A++++result+%3D+num+*+num%0A++++print(str(num)+%2B+%22+squared+is+%22+%2B+str(result))&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)
<!-- stop it* -->
</div>
</section>

<section markdown="block">
##  How About Another?

__What is the output of this code? Let's read through it line-by-line to figure it out. &rarr;__

<pre><code data-trim contenteditable>
for whatevs in range(1, 4):
    if whatevs == 2:
        print("let's skip this one")
    else:
        print(str(whatevs) + " Mississippi")
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
1 Mississippi
let's skip this one
3 Mississippi
</code></pre>
[And again, step-by-step](http://www.pythontutor.com/visualize.html#code=for+whatevs+in+range(1,+4)%3A%0A++++if+whatevs+%3D%3D+2%3A%0A++++++++print(%22let's+skip+this+one%22)%0A++++else%3A%0A++++++++print(str(whatevs)+%2B+%22+Mississippi%22)&mode=display&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&py=3&curInstr=0)
</div>
</section>


<section markdown="block">
##  For Loop Exercises
</section>

<section markdown="block">
##  Some Quick Excercises

__Let's do these together &rarr;__

* count to 100 starting from 1
* count to 100 by twos from 0
* count backwards starting from 100 down to and including 0
</section>

<section markdown="block">
##  Fizz Buzz
* [fizz buzz](http://c2.com/cgi/wiki?FizzBuzzTest)
* print out 1 to 100 ...with the following exceptions:
* for multiples of three, print out "Fizz" instead of the number 
* for multiples of five, print out "Buzz" instead of the number
* for multiples of both three and five print “FizzBuzz”
* example output, next slide, plz!
</section>

<section markdown="block">
##  FizzBuzz Output
<pre><code data-trim contenteditable>
1
2
Fizz
4
Buzz
Fizz
.
.
14
FizzBuzz
16
.
.
98
Fizz
Buzz
</code></pre>
</section>

<section markdown="block">
##  FizzBuzz Solution
<pre><code data-trim contenteditable>
{% include classes/09/fizzbuzz.py %}
</code></pre>
</section>

<section markdown="block">
##  Using an Accumulator Variable
</section>

<section markdown="block">
##  Accumulator Variable

An __accumulator__ variable is a variable used to keep the running total of a repeated calculation or operation that's within a loop:  

* a variable is declared outside of the loop
* it is added to within the loop

Some examples include:

* counting the number of times a while loop runs (count += 1)
* fragmently building a string within a loop (s += word)
</section>

<section markdown="block">
##  Summing Numbers
* sum the first 1-100 numbers, print out the resulting the sum 
* (which, of course, [doesn't need a loop](http://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/))
* (and there's [this story](http://en.wikipedia.org/wiki/Carl_Friedrich_Gauss#Anecdotes))
* (and [the list of things named after him!?](http://en.wikipedia.org/wiki/List_of_things_named_after_Carl_Friedrich_Gauss))

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{% include classes/09/sum.py %}
</code></pre>
</div>
</section>

<section markdown="block">
##  Counting Dice For Loop

__Roll a die 1000 times; count how many times a one is rolled!  Print out the result.  Use a for loop.&rarr;__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{% include classes/09/roll_for.py %}
</code></pre>
</div>
</section>

<section markdown="block">
##  Counting Dice While Loop

__Roll a die 1000 times; count how many times a one is rolled!  Print out the result.  Use a while loop.&rarr;__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{% include classes/09/roll_while.py %}
</code></pre>
</div>
<!--_ -->
</section>

<section markdown="block">
##  Using User Input to Influence Number of Repetitions
</section>

<section markdown="block">
##  Controlling a For Loop With User Input

We can base the number of repetitions that a for loop goes through by asking the user to enter a value.

__Let's check out a programming problem where this idea might come in handy...__ &rarr;

<!--
<pre><code data-trim contenteditable>
highest_number = int(input("How high should I count?\n> "))
for n in range(1, highest_number + 1):
	print(n)
</code></pre>
-->

</section>

<section markdown="block">
##  A Ladder

__Make me a ladder!__ &rarr;

* ask for a height, make a ladder with that many rungs
* can you do this using a for loop?
* or how about just string multiplication?

<pre><code data-trim contenteditable>
How tall do you want this ladder to be?
> 3

 ========
 |      |
 ========
 |      |
 ========
 |      |
</code></pre>
</section>

<section markdown="block">
##  A Ladder Implementation

(Or... two implementations, really)
<pre><code data-trim contenteditable>
height = int(input('How tall do you want this ladder to be?'))

for i in range(height):
    print('========\n|      |')

#  or... just multiply instead of using the for loop
#  print(height * '========\n|      |')
</code></pre>
</section>
