import wordsy
"""
Using your wordsy module, write an iteractive program that:

1. continually asks the user for a word
2. when the user presses enter without entering a word, stop
   asking for a word (in this case, the result of input will
   be an empty string: '' ... so your condition will basically
   check if the user entered empty string or not)
3. print out all of the words, along with the position that
   the word is in (for example, word 1, word 2, etc.), and
   a scrambled version of the word.
4. (OPTIONAL) if you implemented sort_by_length in wordsy,
   sort the words by length first before printing them out

Example output:
=====

WORD SCRAMBLER!
I'll ask you for a series of words
When you stop giving words, I'll print out every word with its letters mixed up!
-----
Give me a word, or just press <Return> without typing to stop
>brown
Give me a word, or just press <Return> without typing to stop
>the
Give me a word, or just press <Return> without typing to stop
>belched
Give me a word, or just press <Return> without typing to stop
>rabbit
Give me a word, or just press <Return> without typing to stop
>dark
Give me a word, or just press <Return> without typing to stop
>
Word 1: brown - rownb
Word 2: the - het
Word 3: belched - elbecdh
Word 4: rabbit - itrbab
Word 5: dark - rdka

Example output at end for optional part (note that it is
sorted):
=====
Word 1: the - eth
Word 2: dark - krda
Word 3: brown - nwrbo
Word 4: rabbit - biabtr
Word 5: belched - edebchl
"""
