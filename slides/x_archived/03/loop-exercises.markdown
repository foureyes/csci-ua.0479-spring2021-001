---
layout: slides
title: Loop Exercises 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>
{% comment %}
String concatentation. Roll two dice exactly 5 times. Write out the number of each roll, and the sum of each roll.

	while loop, for loop version

Roll it 100 times, is an easy for or a hard four more difficult to get?

	while loop, for loop

How about rolling it until we get a hard four?

	only while loop?

This time, let's control the numbers ask the user how many times they want to roll the dice?

	while and for

How about roll forever until they type stop?

	only while loop

How about building ladder with random... add constructing ...
{% endcomment %}

<section markdown="block">
##  Fours and Roots

__Print out the square root of every multiple of 4 that's less than 65, but greater than 3__ &rarr;

<div class="fragment" markdown="block">

<pre><code data-trim contenteditable>
import math
for n in range(4, 65, 4):
    print(math.sqrt(n))    
</code></pre>
</div>
</section>

<section markdown="block">
##  Odds or Evens

__Create a program that simulates two players playing odds or evens__ &rarr;

* keep track of a score for two players, the evens player and the odds player
* both players present either a 1 or a 2.  if the total is even, the evens player gets a point, otherwise, the odds player gets the point
	* for each player, randomly generate a number: 1 or 2
	* determine the total; allocate the point based on whether the total is odd or even
* once either player scores 2 points, stop
</section>


<section markdown="block">
##  Example Output

<pre><code data-trim contenteditable>

odds play: 1, evens play: 2
total is: 3
-------------
odds score: 1, evens score: 0

odds play: 2, evens play: 2
total is: 4
-------------
odds score: 1, evens score: 1

odds play: 1, evens play: 2
total is: 3
-------------
odds score: 2, evens score: 1
</code></pre>
</section>

<section markdown="block">
##  Example Implementation

<pre><code data-trim contenteditable>
import random

def main():
    evens_score = 0
    odds_score = 0
    max_score = 5

    while evens_score < max_score and odds_score < max_score:
        evens_num = random.randint(1, 2)
        odds_num = random.randint(1, 2)
        total = evens_num + odds_num
        print("odds play: %s, evens play: %s" % (odds_num, evens_num))
        print("total is: %s" % (evens_num + odds_num))
        if total % 2 == 0:
            evens_score += 1
        else:
            odds_score += 1
        print("-------------")
        print("odds score: %s, evens score: %s\n" % (odds_score, evens_score))

main()
</code></pre>
</section>

{% comment %}

<section markdown="block">
##  Reverse Sentence

__Write a program that asks for exactly 5 words.  The program should print the words in reverse order.__ &rarr;

* You must use a __loop__ to do this; don't just create 5 variables &rarr;  
* Hint:  accumulating the words into an emptry string and printing out at the end may help
* Hint:  you can start just by printing out the words in order instead of reverse

</section>

<section markdown="block">
##   Example Output

<pre><code data-trim contenteditable>
Word please!
> program
Word please!
> amazing
Word please!
> my
Word please!
> out
Word please!
> check
check out my amazing program
</code></pre>
</section>

<section markdown="block">
##   Example Implementation

<pre><code data-trim contenteditable>
sentence = ''
for i in range(5):
    word = input("Word please!\n> ")
    sentence = word + ' ' + sentence

print(sentence)
</code></pre>
</section>

{% endcomment %}

<section markdown="block">
##  An ATM Program

__Create a program that simulates an ATM__ &rarr;

* the program displays your current balance, which starts at 5
* it repeatedly asks for one of three commands: deposit, withdraw or quit
	* d or D for deposit
	* w or W for withdraw
	* q or Q to quit
* if the command is withdraw or deposit, the program asks for an amount (that will be added/subtracted)
* if the command is q, the program stops running
* if the command is not recognized, print "huh?"
</section>

<section markdown="block">
##  Example Output 

<pre><code data-trim contenteditable>
Your current balance is 5
(D/d)eposit, (W/w)ithdraw or (Q/q)uit?
> D
how much would you like to deposit?
> 10
Your current balance is 15
(D/d)eposit, (W/w)ithdraw or (Q/q)uit?
> d
how much would you like to deposit?
> 2
Your current balance is 17
(D/d)eposit, (W/w)ithdraw or (Q/q)uit?
> w
how much would you like to withdraw?
> 8
Your current balance is 9
(D/d)eposit, (W/w)ithdraw or (Q/q)uit?
> blah
huh?
Your current balance is 9
(D/d)eposit, (W/w)ithdraw or (Q/q)uit?
> q
k, thx bye
</code></pre>
</section>


<section markdown="block">
##  Example Implementation

<pre><code data-trim contenteditable>
balance = 5
command = ''
while command != 'q' and command != 'Q':
    print("Your current balance is %s" % (balance))
    command = input("(D/d)eposit, (W/w)ithdraw or (Q/q)uit?\n> ")
    if command == 'd' or command == 'D':
        amt = int(input('how much would you like to deposit?\n> '))
        balance += amt
    elif command == 'w' or command == 'W':
        amt = int(input('how much would you like to withdraw?\n> '))
        balance -= amt
    elif command == 'q' or command == 'Q':
        print('k, thx bye')
    else:
        print('huh?')
</code></pre>
</section>

<section markdown="block">
##  Generate Random Bits

__Write the following program__ &rarr;

* ask the user for a number between 4 and 8 inclusive 
* if the number is not between 4 and 8, ask again (continually)
* use the number to create a series of randomly generated bits (4 means 4 bits will be generated)
* print out the bits and their decimal value
* for example, if the program generates 0011, then the resulting base 10 number is 3

<pre><code data-trim contenteditable>
how many bits (between 4 and 8)?
>4
0011 in binary is 3 in decimal
</code></pre>

</section>

<section markdown="block">
##  Random Bits Solution!
 
<pre><code data-trim contenteditable>
import random

bit_length = 0
while bit_length < 4 or bit_length > 8: 
    bit_length = int(input('how many bits (between 4 and 8)?\n>'))
bits = ''
num = 0
for exponent in range(bit_length):
    b = random.randint(0, 1)
    bits = str(b) + bits
    num += b * (2 ** exponent)

print('%s in binary is %s in decimal' % (bits, num))
</code></pre>
</section>
