---
layout: slides
title: "Style"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Have You Read the Book?

Maybe you've shuddered at its __coding style__?

* it kind of looks like Java with all of that camel case!
* don't do that
* follow the [conventions laid out in pep-8](https://www.python.org/dev/peps/pep-0008/) (some of which is described in the next few slides)

<br>
The following slides discuss how you should format your code... that is... _coding style_.

</section>
<section markdown="block">
## Hobgoblins

First off... directly from the PEP-8:

__"A Foolish Consistency is the Hobgoblin of Little Minds"__

What does that mean?


* {:.fragment} "A style guide is about consistency. Consistency with this style guide is important."
* {:.fragment} "Consistency within a project is more important." 
* {:.fragment} "Consistency within one module or function is most important."
* {:.fragment} follow the style set forth in the file that you're working on (if code already exists), otherwise try to use PEP-8
</section>

<section markdown="block">
## Ok. Ok. Valid Variable Names

__You have to have a valid name before you even name anything...__ &rarr;

* starts w/ letter or underscore
* remainder of name is letter, underscore or number

</section>

<section markdown="block">
## Good Variable Names

* all lowercase
* separate words are <code>separated_by_underscore</code>
    * (rather than <code>smushedtogether</code>)
    * (rather than <code>camelCase</code>)
* use descriptive variable names (avoid single letter names)
    * unless single letter is meaningful (for example, x and y for dealing with a point)
    * 
</section>

<section markdown="block">
## Indentation

__Python is whitespace significant, but it kind of doesn't care what _type_ of whitespace you have at the beginning of the line__ &rarr;

* don't mix spaces and tabs (this will inevitably cause an error down the line)!
* use spaces instead of _actual_ tabs
* most editors will expand tabs (key press) into spaces for you 
* use 4 spaces for an indent
* if you use PyCharm you don't have to worry about this

</section>

<section markdown="block">
## Use Whitespace for Visually Separation

We already know that Python is whitespace significant (specifically leading whitespace). __However, you can make liberal use of newlines and internal white space to make things easier to read.__ &rarr;

* surround binary operators with spaces... use <code>x = 5 + 5</code> instead of <code>x=5+5</code>
* surround a function definition with minimally 1 blank line (PEP-8 says 2)
* avoid using whitespace before commas and immediately after or before opening or closing parens, braces, etc. ... don't do this
* avoid extraneous trailing white space 

</section>

<section markdown="block">
## Use Docstrings Where Appropriate

* when you write functions... 
* write a multi-line string
* right after your function header
* it should describe your function (parameters, return type etc.)
    * it is used by Python's help system
    * it's kind of like JavaDoc
</section>

<section markdown="block">
## What? Python's Help?

In the interactive shell, you can use the <code>help()</code> function to get help on any object that you pass to it.

__For example, if we want help on the math module's sin function, we can do this...__ &rarr;

<pre><code data-trim contenteditable>
>>> import math
>>> help(math.sin)
</code></pre>

...aaaaand ...it gives back this:

<pre><code data-trim contenteditable>
sin(...)
    sin(x)

Return the sine of x (measured in radians).
</code></pre>
</section>

<section markdown="block">
## Docstring Example

Here's an example of creating our docstring (this is in the interactive shell, btw)...

<pre><code data-trim contenteditable>
>>> def my_super_function(s):
...     """my function does great stuff; it takes a string as an argument and returns an int"""
...     return 1
...
>>> help(my_super_function)
</code></pre>

Output when asking for help on our custom function!

<pre><code data-trim contenteditable>
Help on function my_super_function in module __main__:

my_super_function(s)
    my function does great stuff; it takes a string as an argument and returns an int
</code></pre>

</section>
