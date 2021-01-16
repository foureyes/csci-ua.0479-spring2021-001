---
layout: slides
title: Strings 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
##  String Delimiters
__How do we know we have a string?  What are the ways we can create a _string literal_? &rarr;__

<div class="fragment" markdown="block">
* 'single quotes'
* "double quotes"
* """triple double quotes!!!"""
</div>
</section>

<section markdown="block">
##  Strings vs Variables

__What's the difference between lines two and three of the following code? &rarr;__

<pre><code data-trim contenteditable>
foo = "bar"
print(foo)   # line 2
print("foo") # line 3
</code></pre>
<div class="fragment" markdown="block">
* the first line prints the variable foo, resulting output is "bar"
* the second line prints the string "foo", resulting output is "foo"
</div>
</section>

<section markdown="block">
##  String Operations
__Name some operations that we can perform on strings &rarr;__ 

<div class="fragment" markdown="block">
* addition / concatenation: __+__
* multiplication: __*__
* string formatting: __%__
</div>
</section>

<section markdown="block">
##  Strings Revisited
* we've been looking at strings as single things (single objects)
* but really, they're made of a bunch of smaller pieces
* __what are strings made of?&rarr;__

<div class="fragment" markdown="block">
zero or more characters!

__what's special about the characters in a string?  are they jumbled or in a specific order? &rarr;__  

* strings are specifically a __sequence__ of characters
* that is, they're ordered - "cat"... c is first, a is second, t is third
</div>
</section>

<section markdown="block">
##  Strings Revisited Continued
* a string is a __compound data type__
* a __compound data type__ is a type in which the values are composed of zero or more other values.
* strings are the first data type that we'll see that's made of other types... 
* (we'll see lists in the next class)
* we've been using strings as a whole... (and we'll explore that further)
* but, next we'll treat strings as a collection of characters... 
</section>

<section markdown="block">
##  [Strings as a List of Characters](strings_as_list.html)
</section>
