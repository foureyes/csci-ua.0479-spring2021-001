---
layout: slides
title: Built-in String Functions 
---
<section markdown="block" class="title-slide">
#  Built-in String Functions
{% include title-slide-footer.html %}
</section>

<section markdown="block">
##  A Few String Related Built-In Functions

Strings have methods that you can call on them.  However, there are also __built-in__ functions that are relevant to strings.  A few that we'll use include:


* __len__(s) - the length of a string
* __ord__(s) - the _code point_ of the character supplied
* __chr__(i) - the character represented by the supplied _code point_

</section>

<section markdown="block">
##  The Built-In len() Function

__len__ is a built-in function that returns the length of a __sequence__

* it is __not a method__, so you do not call it on an object
* however, you can pass a value to it, and it will return its length
* for strings, it will return the number of characters

<pre><code data-trim contenteditable>
s = "cat"

#  returns 3
print(len(s))

</code></pre>
</section>

<section markdown="block">
##  Index of the Last Character in a String

__What's the formula for getting the last character in a string?__ &rarr;

<div class="fragment" markdown="block">
length of string - 1
</div>
</section>

<section markdown="block">
##  Index of the Last Character in a String Continued

__What values / expressions would you use if you wanted to index into the string below to get the last character?__ &rarr;

<pre><code data-trim contenteditable>
s = "cat"
print(s[?])
</code></pre>

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
print(s[2])
print(s[-1])
print(s[len(s) - 1])
</code></pre>
</div>
</section>

<section markdown="block">
##  Representing Strings

There's a __standard__ for consistently representing text through different character sets and encodings. 

* this system is called __unicode__
* in __unicode__, __code points__ are numbers (specifically integers) that represents a _character_ or _glyph_
* here's a table of [code points](http://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec)
* here's a [unicode snowman](http://unicodesnowmanforyou.com)
</section>

<section markdown="block">
##  Unicode Table

[Let's see that table again.](http://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec)

* note that 65-90 are uppercase latin letters; 97-122 are lowercase
* this matches an older method of encoding characters called ASCII
	* ASCII accomodated 128 characters
	* what are some shortcomings of this? &rarr;
</section>


<section markdown="block">
##  chr() and ord()

Python has a couple of functions that translate code points to characters and characters back to code points.

* __ord__(c) - gives back the integer value of the code point of the supplied character 
* __chr__(i) - gives back the character corresponding to the supplied integer (code point) 
</section>

{% comment %}
<section markdown="block">
##  Caesar Cipher

* simple encryption technique
* shifts letter over by x number of letters
* for example, shifting by one maps letters 1 to the right
	* A &rarr; B
	* B &rarr; C
* Julius Caesar "used it with a shift of three to protect messages of military significance"

See... [Caesar Cipher](http://en.wikipedia.org/wiki/Caesar_cipher)
</section>

<section markdown="block">
##  Caesar Cipher Encryption Function

__Write a function that takes a string as an argument and returns an encrypted string using Caesar's Cipher.  Shift by 23.__ &rarr;

* takes one argument, example call: caesar_encrypt("ABCD")
* should return an encrypted string &rarr; caesar_encrypt("ABCD") &rarr; "XYZA" 
* if the characters is not a letter, don't shift: "Hello!!!"  &rarr; "Ebiil!!!"
* write assertions (use the examples above for test cases)
</section>

<section markdown="block">
##  Some General Strategies

__What are some approaches / algorithms we can use?__ &rarr;

<div class="fragment" markdown="block">
* maintain two sets of letters: 
	* untranslated and translated
	* the index of the translated letter should match the untranslated
* unicode code points for uppercase and lowercase letters are consecutive; use addition and/or subtraction to alter the code point to shift letters
	* bound upper, lower, and loop back by using a series of boolean expressions and conditionals
	* calculate new offset using mod 26 to simulate circle
	
</div>

</section>

<section markdown="block">
##  Caesar Cipher Encrypt Version 1

<pre><code data-trim contenteditable>
{% include classes/18/caesar_encrypt_v1.py %}
</code></pre>
</section>

<section markdown="block">
##  Caesar Cipher Encrypt Version 2

<pre><code data-trim contenteditable>
{% include classes/18/caesar_encrypt_v2.py %}
</code></pre>
</section>

<section markdown="block">
##  Caesar Cipher Encrypt Version 3

<pre><code data-trim contenteditable>
{% include classes/18/caesar_encrypt_v3.py %}
</code></pre>
</section>

<section markdown="block">
##  Caesar Cipher Decryption Function

__Write a function that takes an encrypted string as an argument and returns the original message.  Assume that Caesar's Cipher, with a shift of 23, was used to encrypt it.__ &rarr;

* example call: caesar_decrypt("XYZA") &rarr; "ABCD"
* (should be similar to casear_encrypt)
* write assertions (use the examples above for test cases)
</section>

<section markdown="block">
##  Caesar Cipher Decrypt Version 1

<pre><code data-trim contenteditable>
{% include classes/18/caesar_decrypt_v1.py %}
</code></pre>
</section>

<section markdown="block">
##  Caesar Cipher Decrypt Version 2

<pre><code data-trim contenteditable>
{% include classes/18/caesar_decrypt_v2.py %}
</code></pre>
</section>

<section markdown="block">
##  Caesar Cipher Decrypt Version 3

<pre><code data-trim contenteditable>
{% include classes/18/caesar_decrypt_v3.py %}
</code></pre>
</section>
<section markdown="block">

##  Interactive Caesar Cipher

Let's try using our new function(s).  __Create a program that encrypts and decrypts a message using the Caesar Cipher__ &rarr;

* _continually_ ask the user for a command:
	* __e__ to encrypt
	* __d__ to decrypt
	* __q__ to quit (stop asking)
* for encryption or decryption:
	* ask for a shift number
	* ask for a message
</section>


<section markdown="block">
##  Example Output

<pre><code data-trim contenteditable>
Caesar Cipher
==========
(e)ncrypt, (d)ecrypt or (q)uit)?
> e
How many places should each letter be shifted?
> 23
What is the message?
> hello
ebiil
(e)ncrypt, (d)ecrypt or (q)uit)?
> d
How many places was each letter shifted?
> 23
What was the message?
> ebiil
hello
(e)ncrypt, (d)ecrypt or (q)uit)?
> q
Bye!
</code></pre>
</section>

<section markdown="block">
##  Something to Consider Before Implementation

* to make this work, we can no longer hardcode offset
* we can use two functions for encrypt and decrypt...
	* however, they're pretty similar
	* can we just have one function that does both?
</section>

<section markdown="block">
##  Interactive Caesar Cipher Implementation Part 1

(added shift parameter to previous implementation)

<pre><code data-trim contenteditable>
def shift_letters(shift, s):
	uppercase_start, lowercase_start = 65, 97
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	translation = ''
	for c in s:
		letter_pos = alphabet.find(c.upper())
		offset = (letter_pos + shift) % len(alphabet)
		if c.isupper():
			translation += chr(uppercase_start + offset)
		elif c.islower():
			translation += chr(lowercase_start + offset)
		else:
			translation += c
	return translation
</code></pre>
</section>

<section markdown="block">
##  Interactive Caesar Cipher Implementation Part 2

(used shift_letters function from previous slide))

<pre><code data-trim contenteditable>
print('Caesar Cipher\n==========\n')
action = ''
while action != 'q':
	action = input('(e)ncrypt, (d)ecrypt or (q)uit)?\n> ')
	if action == 'q':
		print('Bye!')
	elif action == 'e':
		shift = int(input('How many places should each letter be shifted?\n> '))
		message = input('What is the message?\n> ')
		print(shift_letters(shift, message))
	elif action == 'd':
		shift = int(input('How many places was each letter shifted?\n> '))
		message = input('What was the message?\n> ')
		print(shift_letters(-shift, message))
	else:
		print('Sorry, I can only encrypt, decrypt or quit...')
</code></pre>
</section>


<section markdown="block">
##  Breaking a Caesar Cipher 

If you find a message that's encrypted, __how can you tell that it was encrypted using Caesar's Cipher, and how can you figure out the right number of letters to shift?__ &rarr;
 
<div class="fragment" markdown="block">
* look at letter frequency to deduce that it's a simple _substitution_ scheme, like Caesar's Cipher
* since there are only a finite number of shifts, _trial and error_ can easily break the encryption
* again, letter frequency can help
* see the [wikipedia article on Caesar's Cipher](http://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher)
* (pretty simple to break, but probably worked because most of Caesar's enemies would have been illiterate!)
</div>

</section>

<section markdown="block">
##  [Lists](lists_intro.html)
</section>
{% endcomment %}
