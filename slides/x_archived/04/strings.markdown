---
layout: slides
title: "Strings"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Strings

Chapter 3 in {{site.book1}} covers strings pretty thoroughly, so the following slides just contain very short notes on what was covered in class.

* __what are they?__
* __how are they delimited?__
* __mutability?__

Some answers...
{:.fragment}

* {:.fragment} collection of characters
* {:.fragment} ordered sequence of characters
* {:.fragment} python doesn't have characters... just has strings
* {:.fragment} it's a sequence type...
* {:.fragment} immutable


</section>

<section markdown="block">
## how are they represented

Strings are represented by numbers. The mapping of numbers to characters is an encoding. In the encoding that Python 3 uses, these numbers are integers called __unicode code points__. For example...

* __65__ - A 
* __66__ - B
* __90__ - Z
* __97__ - a
* __98__ - b
* etc.

</section>

<section markdown="block">
## built-in functions...

There are some built-in functions that we can use to work with strings. A few that we'll use for encryption and decryption algorithms in the next class include:

* __chr__ - character of a unicode code point
* __ord__ - unicode code point of a character
* __len__ - # chars in a string

<pre><code data-trim contenteditable>
chr(65) # --> A
ord('A') # --> 65
</code></pre>
</section>

<section markdown="block">
## operators

* concatenation + 
* index []
* repetition * 
* slicing [:]
* in / not in
* string formatting operator %
</section>

<section markdown="block">
## comparisons

You can compare strings with relational / ordering operators like &lt;, &gt;, etc. ... __They're compared__ &rarr;

* lexicographically 
* start on left, compare code point of each
* basically alphabetically

<pre><code data-trim contenteditable>
'azc' > 'abc' # True
'ab' < 'abc' # True
</code></pre>

</section>
<section markdown="block">
## operators continued

__Using indexes and slices...__ &rarr;

* what's an index?
    * an int that represents position of character in string
    * starts at 0
    * last index is -1 (or len(some_string) - 1)
* index... again []
    * if index is larger than length of string, <code>IndexError</code>
    * <code>'joe'[100] #--> error!</code>
* slice... substring (returns new string, doesn't change original) 
    * ...[start:end], but doesn't include end
    * leave out start to start at beginning
    * leave out end to go to last char

<pre><code data-trim contenteditable>
'pizza'[:] # --> pizza
'pizza'[:2] # --> pi
'pizza'[3:] # --> za
</code></pre>
</section>

<section markdown="block">
## iteration

__There are a few ways to go over every character in a string__ &rarr;

<pre><code data-trim contenteditable>
s = "Yes, I'm a string"
</code></pre>

Every _character_

<pre><code data-trim contenteditable>
for letter in s:
    print(letter)
</code></pre>

Indexes...

<pre><code data-trim contenteditable>
for i in range(len(s)):
    print(s[i])
</code></pre>

Enumerate (best of both!)
<pre><code data-trim contenteditable>
for i, ch in enumerate(s):
    print(i, ch)
</code></pre>
</section>

<section markdown="block">
## Retrieving a substring?

__To determine if a string is a substring... or to find a substring's index...__ &rarr;

* <code>in</code> and <code>not in</code>
* also <code>index</code> and <code>find</code> methods...
* wait what? why two?
    * index causes an exception if substring not found
    * find returns -1

<pre><code data-trim contenteditable>
'ace' in 'racecar' # --> True
'racecar'.index('ace') # --> 1
'racecar'.find('ace') # --> 1
'racecar'.index('joe') # --> ValueError
'racecar'.find('joe') # --> -1 (negative one!)
</code></pre>
</section>
<section markdown="block"> 
## speaking of... methods

__The book mentions__ &rarr;

* center
* count
* ljust
* rjust
* upper lower index
* f ind replace

__Some others__ &rarr;

* is\_\_\_\_ (numeric, digit, alpha, alnum, lower, upper, space, etc.)
* format (as a method) - replaces placeholders with arguments
* strip - returns new string with leading and trailing whitespace removed
</section>
