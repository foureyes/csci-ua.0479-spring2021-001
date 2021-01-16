---
layout: slides
title: "Transposition Cipher"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Transposition Cipher / Rail Cipher

__This is covered in chapter 3, section 3.4 in {{ site.book1 }}__ &rarr;

Some terminology....

* __plain text__: some message (original _readable_ message)
* __ciphertext__: "scrambled" up version of original message
* __encryption__: the process of transforming plain text into ciphertext
* __decryption__: process of transforming ciphertext back to plain text
</section>

<section markdown="block">
## Rail Cipher Encryption Pseudocode

<pre><code data-trim contenteditable>
# for every character
    # if it's even add it to ___
    # if it's odd add it to other ___
# add odd and evens... and return it
</code></pre>
</section>

<section markdown="block">
## Encryption Implementation

<pre><code data-trim contenteditable>
def encrypt(s):
    odds, evens = '', ''
    for i in range(len(s)):
        if i % 2 == 0:
            evens += s[i]
        else:
            odds += s[i]
    return odds + evens
</code></pre>
</section>

<section markdown="block">
## Decryption Psuedocode

(Implementation saved for in-class activity)

<pre><code data-trim contenteditable>

odds = slice from  0 to length / 2
evens = slice from  length / 2 to the end

go from i to range (length / 2)
    add even at i, add odd at i

if original length is odd...
    add the left over evens (last index)
</code></pre>
</section>
