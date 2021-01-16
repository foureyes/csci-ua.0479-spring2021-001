---
layout: slides
title: "Strings and Mutability"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Removing Characters from a String

__Wait... strings are immutable. How do we? Whaaaat?__ &rarr;

Let's try to implement the following functions:

* <code>remove_duplicates(s)</code>
    * removes all duplicate letters in the string <code>s</code>
* <code>remove_letters(letters, s)</code>
    * removes all occurrences of every letter in <code>letters</code> from string <code>s</code>

HINT: These functions don't actually remove letters from the original string - instead they return an entirely new string.

</section>

<section markdown="block">
## But First, Removing a Single Character

In the following examples, __we'll _simulate_ removing <code>r</code> from <code>carts</code>. We'll start with... <code>s = 'carts'</code>__ &rarr;

1. __accumulate__ into new string and leave out cahrs to be removed
    <pre><code data-trim contenteditable>
>>> accum = ''
>>> for ch in s:
...   if ch != 'r':
...     accum += ch
>>> s = accum
</code></pre>
2. create and __concatenate slices__ before and after the char to be removed
    <pre><code data-trim contenteditable>
>>> s = s[:2] + s[3"]
</code></pre>
3. use __replace and reassign__
    <pre><code data-trim contenteditable>
>>> s = s.replace('r', '')
</code></pre>
</section>

<section markdown="block">
## Removing Duplicates

__We can implement the following function using the techniques below__ &rarr;

<pre><code data-trim contenteditable>
def remove_duplicates(s):
    """removes all duplicate letters in the string s"""
</code></pre>


1. loop over every letter, __count__ its occurrences (by looping or by count method) and _remove_
2. loop over every letter and __accumulate__ if letter is not already in accumulation
3. some methods don't preserve order:
    * {:.fragment} use set constructor: <code>set('abc') # does not retain ordering though</code> 
    * {:.fragment} add letter and count to dictionary, give back keys (also does not retain ordering)

Chapter 3 in the book and Homework #2 demonstrates method #2.
{:.fragment}
</section>

<section markdown="block">
## Remove Letters

__We can implement the following function using the techniques below__ &rarr;

<pre><code data-trim contenteditable>
def remove_letters(letters, s):
    """removes all occurrences of every letter in letters 
    from string s
    """
</code></pre>

1. create new string, loop over every character in s and accumulate into new string as long as character not in letters
2. loop over every character in letters, and remove from s using slicing technique
3. consecutive calls to replace (as shown below)

<pre><code data-trim contenteditable>
    for letter in letters:
        # why haz assignment
        s = s.replace(letter, '')
    return s
</code></pre>

</section>


