---
layout: slides
title: "Substitution Cipher, Vigenère Cipher"
---

<section markdown="block">
## Encryption / Decryption Algorithms

__Our book covers the following ciphers in Chapter 3: Codes and Other Secrets__ &rarr;

1. transposition / rail cipher
2. substitution cipher
3. vigenère  cipher

We checked out the __transposition cipher__ last week. In this set of slides we'll:

* discuss how a __substitution cipher__ and the __vigenère cipher__ work
* take a look some partial implementations and helper functions required for both
* (you'll get a more in-depth look through readings and homework)
</section>

<section markdown="block">
## Substitution Cipher

The __substitution cipher__ simply maps one character to another character. For example, the table below contains:

1. the __plain text__ in the first row
2. the __key__ / _translated_ version in the second row
3. and the index for the 2 rows above as the last row

<pre><code data-trim contenteditable>
a  b  c  d  e  f  g  h  i  j  k  l  m  ... y  z
x  y  z  a  b  c  u  v  w  d  e  f  r      j  k
00 01 02 03 04 05 06 07 08 09 10 11 12 ... 24 25
</code></pre>

Encrypting the word <code>ace</code> would give us <code>xzb</code> (the letter of the key at index 0, 2, and 4.


</section>

<section markdown="block">
## Definitions

In the previous slide, the terms __substitution cipher__ and __key__ were used:

* as its name implies, a __substitution cipher__ is:
    * a cipher that substitutes one character... 
    * for another character...
    * for every character in a message
* a __key__ is:
    * a rearranged version of the alphabet (or the set of all characters possible in the plain text message)
    * used as the source for replacement letters in a substitution cipher
</section>

<section markdown="block">
## Substitution Interactive Shell

The following transcript from an interactive shell session:

* generates a string from a - z using our _homegrown_ <code>gen_consecutive_chars</code> function
* uses <code>bcdefghijklmnopqrstuvwxyza</code> as the key
* and encrypts the first letter of the string, <code>hello</code> (<code>h</code>)...

<pre><code data-trim contenteditable>
>>> alpha = spytools.gen_consecutive_chars()
>>> translated = alpha[1:] + alpha[0]
>>> translated
'bcdefghijklmnopqrstuvwxyza'
>>> s = 'hello'
>>> s[0]
'h'
>>> alpha.index(s[0])
7
>>> translated[alpha.index(s[0])]
'i'
</code></pre>
</section>


<section markdown="block">
## About Keys

__Ok... the key that we used...__ &rarr;

* should probably not be as predictable as a simple shift
* maybe it should include an element of randomness
* but that just means that the key will be difficult to remember

One way to balance _easy of use_, but make it a little less predictable than a simple shift... is to use a __password__ to generate a key. __For example...__ &rarr;

<pre><code data-trim contenteditable>
password: topsecret
generated key: topsecruvwxyzabdfghijklmnq
</code></pre>

But how???
</section>

<section markdown="block">
## Generating a Key

__Our book describes the following algorithm.__ &rarr;

0. create string containing alphabet
1. remove duplicates from incoming password
2. partition alphabet - before last letter, after last letter of password
3. for each partition remove letters in password from both parts
4. create key by concatenating password, before last letter of password, and after lass letter of password

For example:

* __alphabet__: <code>abcdefghijklmnopqrstuvwxyz</code>
* __password__: <code>topsecret</code>
* __removed duplicates__: <code>topsecr</code>
* __paritioned alphabet with letters removed__:
    <code>abdfghijklmnq ... and ... uvwxyz</code>
* __concatenated__: topsecruvwxyzabdfghijklmnq
</section>

<section markdown="block">
## Substitution Cipher with Password - Example

Using __topsecret__ as the password, __we generate our key...__ &rarr;

<pre><code data-trim contenteditable>
abcdefghijklmnopqrstuvwxyz 
topsecruvwxyzabdfghijklmnq
</code></pre>

The key can be used to encrypt our message with __the usual substitution cipher__:

<pre><code data-trim contenteditable>
we are discovered. flee at once.
le tge svhpbkeges. cyee ti bape.
</code></pre>
</section>

<section markdown="block">
## Breaking a Substitution Cipher

It turns out that you should probably _not_ use a substitution cipher to hide your secret messages. __It's easily broken... how / why?__ (ignore that we've preserved non-letter characters) &rarr;

* {:.fragment} you can __brute force__ a key
* {:.fragment} you can do some __frequency analysis__ on the letters, and determine the key based on that
    * {:.fragment} for example, e tends to be the most frequently used letter in English
    * {:.fragment} ... soooo, finding the most frequent letter in the ciphertext may reveal that it maps to the plain text letter, e

</section>
<section markdown="block">
## Vigenère Cipher

__The Vigenère attempts to mitigate this issue by using a different key for every letter!__ (see ch 3 in our book) &rarr;

* overlay password over every letter
* find letter in password overlay that corresponds to plain text letter
    * this letter determines which row (shift to use)
    * (letter maps to row, row is new key)... 
    * the example below shows a few different keys based on a letter from the password
    <pre><code data-trim contenteditable>
  0123456789
  abcdefghijklmnopqrstuvwxyz
A abcdefghijklmnopqrstuvwxyz
B bcdefghijklmnopqrstuvwxyza
C cdefghijklmnopqrstuvwxyzab
</code></pre>
* using new key... use index of original letter in plain text in alphabet
* to retrieve the letter from the key

</section>


<section markdown="block">
## An Aside on Modulo

Before we dive into the Vigenère cipher, __we should discuss modulo__.  __How many possible values can be produced from using  % 3 on a number? What are they?__ &rarr;

* {:.fragment} just 3 values
* {:.fragment} 0, 1, or 2

Imagine I have a string of 3 characters: <code>cat</code>. I'd like any indexes above the last (that is, index <code>2</code>) to start again at the beginning. 
{:.fragment}

* {:.fragment} 3 should give back c, 4 should give back a
* {:.fragment} __how could this be implemented?__ &rarr;
* {:.fragment} use modulo len(sequence) on the index, and you're constraining the value to 0 to len(sequence) - 1... with anything greater than the last index looping around
</section>

<section markdown="block">
## Overlay Password to Get Row Letter 

So... armed with our knowledge of using __modulo for looping around__, how do we __overlay the password__ and __get the row letter__ from the password based on the plain text so that we get something like this?

<pre><code data-trim contenteditable>
password:   DAVINCIDAVINCIDAVINI
plain text: the eagle has landed
index:      0123456789..........
</code></pre>

* {:.fragment} using the __index of the plain text letter__ that you'd like to encrypt...
* {:.fragment} __constrain__ the index to an index within the password by using: index modulo length of the password 
* {:.fragment} this will be the __index in the password__ that the plain text letter maps to
* {:.fragment} the letter at this newly calculated index is the row that the key is in

</section>
<section markdown="block">
## Overlay Password to Get Row Letter Code

__An interactive shell session below shows how the password overlay may work in order to get the index of the <code>row_letter</code> from the original password.__ &rarr;

<pre><code data-trim contenteditable>
>>> pw = 'DAVINCI'
>>> s = 'the eagle has landed'
>>> i = 2 # index of e in plaintext
>>> j = 7 # index of l in plaintext
>>> row_letter = pw[i % len(pw)]
>>> row_letter
'V'
>>> row_letter = pw[j % len(pw)]
>>> row_letter
'D'
</code></pre>

</section>
<section markdown="block">
## Vigenère Cipher Table

Now that we have the row letter __we can look up our key based on the letter in the password__. For example, <code>D</code> maps to the key that starts with <code>defgh...</code> &rarr;

<pre><code data-trim contenteditable>
DAVINCIDAVINCIDAVINC
the eagle has landed

  0123456789
  abcdefghijklmnopqrstuvwxyz
A abcdefghijklmnopqrstuvwxyz
B bcdefghijklmnopqrstuvwxyza
C cdefghijklmnopqrstuvwxyzab
D defghijklmnopqrstuvwxyzabc
.
.
.
Y yzabcdefghijklmnopqrstuvwx
Z zabcdefghijklmnopqrstuvwxy
</code></pre>

</section>

<section markdown="block">
## Vigenère Cipher Table Continued

Uh... what about this table thing? __Do we have to create a table of all keys in our code?__ &rarr;

Note that each key is just shifted an additional letter. __To get a _shifted_ alphabet... you don't have to hardcode a table, just figure out an offset to add to the original index to get the newly _shifted_ index__. &rarr;
{:.fragment}

* {:.fragment} __offset__ is index of letter in alphabet
* {:.fragment} B is at index 1, so add 1 to original alpha index: e's are at (4), but in the shifted version, f (5) replaces e
* {:.fragment} C is at index 2, so the letter at position (4) is g instead of c (4 + 2)
* {:.fragment} Z is at index 25, so add 25 to original alpha index (hmmm... let's see how this works)

</section>

<section markdown="block">
## Starting on Other Side

Here's Z again. z is at index 25. __What happens if we want to figure out what position e will have in the newly rotated alphabet?__.

<pre><code data-trim contenteditable>&nbsp;&nbsp;0123456789...
  abcdefghijklmnopqrstuvwxyz
Z zabcdefghijklmnopqrstuvwxy
</code></pre>

* {:.fragment} e is originally at index 4. 
* {:.fragment} we add 25... and it's off the charts (it's index is no longer between 0 and 25)!
* {:.fragment} __what do we do?__ &rarr;
* {:.fragment} modulo! (4 + 25) % 26 = 3 (which is the index of d in the original alphabet)
* {:.fragment} so the letter at position 4 for key at Z would be <code>d</code> instead of <code>e</code>
</section>

<section markdown="block">
## Example of Translating a Single Letter

<pre><code data-trim contenteditable>
password:   DAVINCIDAVINCIDAVINI
plain text: the eagle has landed
</code></pre>

<pre><code data-trim contenteditable>
>>> import spytools
>>> plain_text = 't' # we want to encrypt 't'
>>> row_letter = 'D' # assuming 't' maps to 'D' in our password
>>> alpha = spytools.gen_consecutive_chars()
>>> offset = alpha.index(row_letter.lower()) # what's D's index?
>>> i = (alpha.index(plain_text) + offset) % len(alpha)
>>> print(i) # index in key that our plain text letter maps to
22
>>> print(alpha[i]) # sooo... t maps to w
'w'
</code></pre>
</section>

<section markdown="block">
## Related Readings

{{ site.book1 }} contains an in-depth descriptions of the material covered:

* __3.5__ - Substitution Cipher
* __3.6__ - Generating a Key
* __3.7__ - Vigenère Cipher

</section>
