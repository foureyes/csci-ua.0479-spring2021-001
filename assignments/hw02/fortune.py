""" 
fortune.py (5 points)
=====
Write a program that generates a random fortune.
You'll be using the random module.

1. Ask the user for their name: 
    What's your name?
    > Joe
2. Ask the user if they want to see the future: 
    Hi Joe, would you like to see your future?
    > YES
3. If the answer isn't any of the permutation of "yes" specified in (4) say "I didn't want to tell you anyway"
4. Otherwise, if the answer YES, yes, or Yes, then:
    a. Ask the user how their future should be predicted:
        Should I use my (c)rystal ball or should I use (t)ea leaves?
        > c
    b. If the user enters "t" in any case, then output:
        You will drink some tea!
    c. If the user enters "c" in any case, use the randint function from the random module to generate a random number from 1 up-to and including 4.
    d. Create 4 fortunes... and based on the number that is generated, output one of the fortunes that you created.
    f. If the user did not enter a "t" or a "c" then say:
        I'm sorry, (Name), I can't tell your fortune today

Example Output (consider text after the ">" user input):

Run 1:
-----
What's your name? 
> Joe
Hi Joe, would you like to see your future? 
> YES
Should I use my (c)rystal ball or should I use (t)ea leaves?
> c
There are many quotation marks in your future!

Run 2:
-----
What's your name? 
> Joe
Hi Joe, would you like to see your future? 
> yes
Should I use my (c)rystal ball or should I use (t)ea leaves?
> neither!
I'm sorry, Joe, I can't tell your fortune today

Run 3:
-----
What's your name? 
> Joe
Hi Joe, would you like to see your future? 
> noooope
I didn't want to tell you anyway
"""
