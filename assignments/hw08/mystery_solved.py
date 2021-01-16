"""
myster_solved.py
=====

Given the coded (encrypted) text in secret.py, find out what book and 
author the text comes from. It is encoded by substituting one letter for 
another.

Consequently, it's possible to decode some of the text by using letter 
frequency analaysis.

First, read the following for some background material:
-----
1. Sorting using sorted: https://docs.python.org/3/library/functions.html#sorted
2. An explanation of using sorted: test_ordering.py (on the course site)
3. Letter frequencies: http://norvig.com/mayzner.html

To decode the text in secret.py:
-----
1. in this file, import secret... the variable, secret.text, will 
   contain the encoded text; feel free to print it out to view it!
2. calculate the number of times each letter occurs in the encrypted 
   text; there are some tricky things that might have to be dealt with:
    * what should you do with non-letter characters?
    * how should casing be handled?
3. print out the letters and their counts in descending order based on 
   count
4. using your calculations and the freqency of letters given by the site 
   above (http://norvig.com/mayzner.html gives us these letters in order
   of descending frequency... 'etaoinsrhldcumfpgwybvkxjqz')
5. ...come up with a mapping: for example, your most frequently occurring 
   letter will map to 'e', the 2nd most frequently occurring will map to 
   't'
6. print out the mapping
7. go through the original encoded text, and substitute the letters 
   appropriately based on frequency
8. finally, display a semi-translated version of the text!

Requirements
-----
1. print out letters and their counts from the encoded text
2. print out your mapping of what letters should be substituted (for 
   example if all x's in the original text should be substituted with e, 
   then print out something like: x -> e)
3. print out a semi-decoded version of the encoded text
4. you must use a dictionary or dictionaries somewhere in your code
5. lastly, in a comment above your code, write a short description of 
   the process that you used and your guess for the source book and author

You can create any functions or modules you want to do this.
"""

