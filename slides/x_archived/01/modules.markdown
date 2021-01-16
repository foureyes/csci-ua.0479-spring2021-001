---
layout: slides
title: "Modules"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## What's a Module

A __module__ is just a file that contains Python code!

* that means that __all modules that you import are somewhere in your file system__
* all of the functions and variables you use from a module are defined in that file

For example, if you <code>import random</code>... that means you're bringing in all of the code from a file called <code>random.py</code>

(You can actually search your file system for <code>random.py</code>, and you'll see that it has definitions for <code>randint</code>, <code>shuffle</code>i, etc.)

</section>

<section markdown="block">
## Bringing in a Module

The recommended way of bringing in a module is to simply use <code>import modulename</code>

<pre><code data-trim contenteditable>
import random
</code></pre>

Whenever you want to access a name of something in that module, you'll have to prefix the name with the module name.  &rarr;

<pre><code data-trim contenteditable>
random.randint(1, 100)
</code></pre>
</section>

<section markdown="block">
## Alias

You can create an alias for a module name by using the keyword, <code>as</code>.


<pre><code data-trim contenteditable>
import random as r
</code></pre>

In this case, instead of prefixing <code>randint</code> with <code>random</code>, you can use <code>r</code> instead...

<pre><code data-trim contenteditable>
import random as r
r.randing(0, 100)
</code></pre>
</section>

<section markdown="block">
## Bringing in Names into Your Global Namespace

Sooo... you probably shouldn't do this, as it _pollutes_ your global name space, but you can also bring in names individually or all names within a module at once using the keyword <code>from</code>...

<pre><code data-trim contenteditable>
from random import randint
randint(0, 100)
</code></pre>

That's kind of ok. However, this should be avoided:

<pre><code data-trim contenteditable>
from random import *
randint(0, 100)
</code></pre>

In this version, __all__ names from the <code>random</code> modules are brought in.
</section>

