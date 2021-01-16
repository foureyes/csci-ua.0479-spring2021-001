---
layout: homework
title: "Assignment #8 (Optional / Make-up)"
---

<style>

.warning {
    background-color: yellow;
    color: #aa1122;
    font-weight: bold;
}

.highlight {
    background-color: yellow;
    font-weight: bold;
}
</style>

# Assignment #8 (Optional, Make-up) - Due Friday, May 6th, 2016

<span class="warning">This assignment is optional and there is no late submission</span>. It can be used to make-up/__replace__ a very low or missing assignment score. It's worth 45 points; the majority the assignments are worth 60 (with one worth 35 and another worth 40). In this  assignment, you'll use the following concepts:

* inheritance
* iterators (it's essentially the in-class activity that we missed!)

* __Part 1__ - Readings
* __Part 2__ - Object Oriented Pig!
* __Part 3__ - Primerator

We'll go over solutions during Monday's (May 9th) review!

## Part 1 - Readings

#### Book

Chapter 12  (Your Father Was a Rectangle)

#### Online Resources

* [inheritance from the official Python docs](https://docs.python.org/3/tutorial/classes.html#inheritance)
* [iterators from the official Python docs](https://docs.python.org/3/tutorial/classes.html#iterators)
* [from sample code in class](https://github.com/jversoza/p4a-spring-16-examples/blob/master/p4a-class22/scratch/iterators.py)


## Part 2 - Object Oriented Pig

You'll be creating an object-oriented version of a dice game called Pig. The game is played as follows:

* each turn, a player repeatedly rolls a die until they roll a 1 or choose to "hold"
    * if a 1 is rolled, the player scores nothing for that turn and the next player goes...
    * if the player rolls any other number, that numbers is added to their turn total and the player's turn continues
    * if the player chooses to "hold" their turn total is added to their score, and it becomes the next player's turn
* the player that reaches 100 or more points first wins (__in our version, we'll have the win total be 30 so games won't last so long__)

[Read the wikipedia article on it!](http://en.wikipedia.org/wiki/Pig_%28dice_game%29)


#### Setup

Create a file called <code>oopig.py</code>.

#### Technical Requirements

* there are two players, the user and the computer
* the game continues until either player scores 30
* the game proceeds with the user taking their turn first, followed by the computer
* the score for both players is displayed after both take their turns
* during a turn, a player can (note that the computer player will automatically choose):
    * (r)oll to continue rolling
        * this rolls a six sided die, with the roll displayed
        * if the roll is not 1 
            * the roll is added to their turn total
            * the current turn total is displayed if the player is the user (not the computer)
        * if the roll is 1, then their turn total is 0, and their turn ends
    * (h)old to end their turn
        * the player's turn ends
* at the end of each player's turn
    * the player's new turn total should be added to their score
    * the player's roll total should be displayed
    * the player's new score should be displayed

__The game must be implemented with minimally 3 classes that fit these requirements__

1. a <code>Player</code> class
    * should hold common data like <code>score</code> 
    * and common methods like <code>roll</code>
2. a <code>ComputerPlayer</code> class
    * __must inherit from the Player class above__
    * however, it should also have methods that allow it to automatically determine whether it should roll or hold based on the opponent's score
    * you can use any heuristic for the computer player (for example, if the other player's score is close to winning, continue to pick roll)
3. a <code>Game</code> class
    * should contain your main game logic
    * should contain one <code>Player</code> object and one <code>ComputerPlayer</code> object

Here's an example of how it may work (<span class="warning">Notice that the player zeros out on their 2nd turn!</span>):

<pre><code data-trim contenteditable>Player's turn
=====
(r)oll or (h)old
> r
| Player | roll: 2, turn total: 2
(r)oll or (h)old
> r
| Player | roll: 4, turn total: 6
(r)oll or (h)old
> r
| Player | roll: 2, turn total: 8
(r)oll or (h)old
> r
| Player | roll: 6, turn total: 14
(r)oll or (h)old
> r
| Player | roll: 4, turn total: 18
(r)oll or (h)old
> r
| Player | roll: 2, turn total: 20
(r)oll or (h)old
> h
Turn Total: 20, Current Total: 20
----------
SCORE... Player: 20, Computer: 0
----------

Computer's turn
=====
| Computer | roll: 3, turn total: 3
| Computer | roll: 4, turn total: 7
| Computer | roll: 6, turn total: 13
Compy FTW!
Turn Total: 13, Current Total: 13
----------
SCORE... Player: 20, Computer: 13
----------

Player's turn
=====
(r)oll or (h)old
> r
| Player | roll: 5, turn total: 5
(r)oll or (h)old
> r
| Player | roll: 4, turn total: 9
(r)oll or (h)old
> r
| Player | roll: 1, turn total: 0
Rolled a zero; NO POINTS 4 U
Turn Total: 0, Current Total: 20
----------
SCORE... Player: 20, Computer: 13
----------

Computer's turn
=====
| Computer | roll: 2, turn total: 2
| Computer | roll: 3, turn total: 5
| Computer | roll: 1, turn total: 0
Rolled a zero; NO POINTS 4 U
Turn Total: 0, Current Total: 13
----------
SCORE... Player: 20, Computer: 13
----------

Player's turn
=====
(r)oll or (h)old
> r
| Player | roll: 5, turn total: 5
(r)oll or (h)old
> r
| Player | roll: 2, turn total: 7
(r)oll or (h)old
> r
| Player | roll: 6, turn total: 13
(r)oll or (h)old
> h
Turn Total: 13, Current Total: 33
----------
SCORE... Player: 33, Computer: 13
----------

PLAYER WON!!!!


</code></pre>

## Part 3 - Primerator

Create an iterator that continually produces the _next_ prime number

#### Setup

Create a file called <code>primerator.py</code>.

#### Technical Requirements

Create an iterator called <code>PrimeGenerator</code> that generates prime numbers. A prime number is a number that is only divisible by 1 and itself. You can consider 1 not prime... and 2 prime.

A simple algorithm for determining if a number is prime is by trying all factors that are not 1 or the number itself. If one of the factors divides evenly into the original number, then you know it's not prime (composite). If you've exhausted all of the factors, then you know it's prime.

For example, if your iterator is called PrimeGenerator...

<pre><code data-trim contenteditable>p = PrimeGenerator()
print(next(p))
print(next(p))
print(next(p))
</code></pre>

Would give:

<pre><code data-trim contenteditable>2
3
5
</code></pre>

And, if you use a for loop:

<pre><code data-trim contenteditable>for p in PrimeGenerator():
    print(p)
</code></pre>

Your program will continually try to print out prime numbers!

{% comment %}

1. player scores 11 and holds
2. computer scores 0 (rolls a 1 on third roll)
3. player scores 3
4. computer scores 23

<pre><code data-trim contenteditable>Shuffling the deck!
Player: 0 Computer: 0
=====
Your turn.
Your current turn total is 0
(r)oll, (h)old or (q)uit?
> r
You rolled a 6
Your current turn total is 6
(r)oll, (h)old or (q)uit?
> r
You rolled a 5
Your current turn total is 11
(r)oll, (h)old or (q)uit?
> h
Adding your turn total, 11, to your score...
Your score is now 11
Computer's Turn
Computer rolled 5
Computer rolled 4
Computer rolled 1
Uh oh! Your computer total is 0, and computer's turn has ended.
Adding computer's turn total, 0, to score...
Computer's score is now 0

Player: 11 Computer: 0
=====
Your turn.
Your current turn total is 0
(r)oll, (h)old or (q)uit?
> r
You rolled a 3
Your current turn total is 3
(r)oll, (h)old or (q)uit?
> h
Adding your turn total, 3, to your score...
Your score is now 14
Computer's Turn
Computer rolled 2
Computer rolled 5
Computer rolled 2
Computer rolled 5
Computer rolled 3
Computer rolled 6
Adding computer's turn total, 23, to score...
Computer's score is now 23

Player: 14 Computer: 23
=====
Your turn.
Your current turn total is 0
(r)oll, (h)old or (q)uit?

{% endcomment %}

