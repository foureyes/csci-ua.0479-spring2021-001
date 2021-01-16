"""
translate_passage.py 
=====

Use your to_pig_latin function to translate an entire passage of text. Do this
by importing your pig_latin module, and calling your to_pig_latin function.

You can use any source text that you want! 

For example: Mary Shelley's Frankenstein from Project Gutenberg:
http://www.gutenberg.org/cache/epub/84/pg84.txt

Or... the Hacker Manifesto from phrack
http://phrack.org/issues/7/3.html

Here's an example of using Mary Shelley's Frankenstein. Taking The second 
paragraph in "Letter 1"...
-----
I am already far north of London, and as I walk in the streets of
Petersburgh, I feel a cold northern breeze play upon my cheeks, which
braces my nerves and fills me with delight. ...

Would be translated to...
-----
i amway alreadyway arfay orthnay ofway ondonlay, andway asway i alkway inway 
ethay treetssay ofway etersburghpay, i eelfay a oldcay orthernnay reezebay 
laypay uponway ymay eekschay, hichway racesbay ymay ervesnay andway illsfay 
emay ithway elightday.

This program can be implemented two ways:

    1. (easy) using a built string method called split to break up the
       passage into individual words only using space as a word boundary
    2. (medium) manually break apart the passage by looping and accumulating
       characters, using space non-letter characters as word boundaries

Step-by-step instructions:

1. Bring in your pig_latin module using import
2. Copy a large paragraph  as a triple quoted string and assign this string to 
   a variable name.
3. Write a function that will:
   a. one parameter, a string, the entire passage to be translated.
   b. return a translated version of the string by using the pig latin 
      function (that only translates single words)
4. To do this treat all consecutive letters as words.  Note that numbers, 
   punctuation and white space do not count as "letters".  Translate each word 
   and create a string that represents the translation of the full text.
   * ALTERNATIVELY, an easy way to deal with breaking up a string is by using
     the string method called split:
   * s = 'the hacker manifesto'
   * words = s.split(' ') # words is ['the', 'hacker', 'manifesto']
7. Print out the result of calling your translate_passage function on a 
   paragraph from Frankenstein

HINT for the standard version (don't read this until you've tried writing the 
pseudocode for the above specifications on your own)
1. Accumulate two strings... your current word, and the actual translation.
2. Go through every character, collecting them into a word. 
3. When you encounter a non letter character (use islpha), take what you
   currently have as a word, translate it, and add it to the translation
4. Add the non letter character to the translation
5. Reset your current word to empty string and go on with the loop

(This is just one possible implementation; there are other ways to do this!)
"""
