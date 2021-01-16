---
layout: slides
title: Nested Loops Review 
---
<section markdown="block" class="title-slide">
#  Nested Loops
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  Nested Loops

A __nested loop__ is just a loop inside the body of another loop.  

* every iteration of the outer loop, the inner loop runs through all of its iterations
* in a nested loop, the inner most loop must finish...
* before another iteration of the outer loop is executed
</section>

<section markdown="block">
##  A Simple Case

__How many times does the outer loop run?  For each run of the outer loop, how many times does the inner loop run?  How many times is "You're driving me loopy!" printed out?__ &rarr;

<pre><code data-trim contenteditable>
for i in range(5):
	print('Run number: %s' %(i))
	for j in range(10):
		print("You're driving me loopy!")
</code></pre>
<div class="fragment" markdown="block">
* the __outer__ loop runs 5 times
* the __inner__ loop runs 10 times
* "You're driving me loopy" is printed out 50 times
* (between each set of 10 prints, the iteration of the outer loops printed out)
</div>
</section>


<section markdown="block">
##  Cheers!

Write a program that asks for how many cheers, and then prints out the appropriate number of cheers. 

* continually ask for number of cheers
* print out that many cheers, each prefixed with the count of the cheer
* if the input is zero, stop asking

<pre><code data-trim contenteditable>
How many cheers shall we give?
> 2
Cheer #1: Hip hip hooray!
Cheer #2: Hip hip hooray!
How many cheers shall we give?
> 1
Cheer #1: Hip hip hooray!
How many cheers shall we give?
> 0
</code></pre>
</section>

<section markdown="block">
##  Some Questions to Ask...

Based on this output...  __What parts are repeated and what kind of loops would you use for each part?__ &rarr;

<pre><code data-trim contenteditable>
How many cheers shall we give?
> 2
Cheer #1: Hip hip hooray!
Cheer #2: Hip hip hooray!
How many cheers shall we give?
> 1
Cheer #1: Hip hip hooray!
How many cheers shall we give?
> 0
</code></pre>

<div class="fragment" markdown="block">
* asking for input and cheering are repeated
* a while loop might make sense for input (the outer loop) and a for loop for cheering (the inner loop)
</div>
</section>

<section markdown="block">
##  Some Pseudocode

__In pseudocode, how might we describe this program?__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
"""
assume number of cheers is not zero
as long as the number of cheers isn't zero
	ask for number of cheers
	for every cheer 
		display the number and display "Hip hip hooray!"
"""
</code></pre>
</div>
</section>

<section markdown="block">
##  A Cheers Implementation

__Using the output we've seen, implement the cheers program.__ &rarr;

<pre><code data-trim contenteditable>
How many cheers shall we give?
> 2
Cheer #1: Hip hip hooray!
Cheer #2: Hip hip hooray!
How many cheers shall we give?
> 0
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
number_of_cheers = 1
while number_of_cheers > 0:
	number_of_cheers = int(input('How many cheers shall we give?\n> '))
	for num in range(1, number_of_cheers + 1):
		print('Cheer #' + str(num) + ': Hip hip hooray!')
</code></pre>
</div>
</section>

<section markdown="block">
##  Password Generator

Below is the output of a program that generates passwords based on a number that is input by the user. It's similar to the cheers example.

<pre><code data-trim contenteditable>
Please enter a pasword length (0 to exit)
>10
2402991612
Please enter a pasword length (0 to exit)
>5
60773
Please enter a pasword length (0 to exit)
>2
72
Please enter a pasword length (0 to exit)
>0
</code></pre>
</section>

<section markdown="block">
##  Password Generator

Create a program that generates passwords! The passwords only consist of digits, though...

* continually ask the user for a number
* if the number is 0, stop asking
* if the number is not 0, generate a password:
	* the number entered will specify how many characters are in the password
	* each character is a randomly generated digit from 0 through 9
* for example, if the user enters 4, a password that may be generated is: 3084
</section>

<section markdown="block">
##  Password Generator Solution

<pre><code data-trim contenteditable>
{% include classes/09/pwgen.py  %}
</code></pre>
</section>

<section markdown="block">
##  Triangle 

Draw a triangle made of stars by using __nested loops__ to accumulate single characters.  Don't use string multiplication or string formatting. Here's the expected output:

<pre><code data-trim contenteditable>
"""
*
**
***
****
*****
"""
</code></pre>

* what's the relation between rows and stars?
* note that the first row has 1 star, the second has 2 stars, etc.
* try accumulating strings into a row using the inner loop
* start with an empty string
</section>

<section markdown="block">
##  Potential Solution for Triangle

<pre><code data-trim contenteditable>
{% include classes/09/triangle.py %}
</code></pre>

* note that multiplication could have also been a possible implementation 
* another alternative is to print out each line instead of accumulating strings

</section>

