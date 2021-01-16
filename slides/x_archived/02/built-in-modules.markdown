---
layout: slides
title: Built-in Modules
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>
<section markdown="block">
##  Built-In Functions

So... again, we learned a few built-in functions.  These are all available by default.

* print
* type
* int
* str
* float
* bool
* input
</section>

<section markdown="block">
##  Modules

__module__ (as defined in THINKSCI):

* a file containing Python definitions and statements intended for use in other Python programs
* the contents of a module are made available to the other program by using the import statement.
</section>

<section markdown="block">
##  Modules Continued

So... what does that actually mean?

* there are other functions that are not automatically loaded when you run python
* these functions (and other definitions, such as variables and constants like pi) are grouped together in files called modules
* you can bring them in to your program by using the __import__ statement
* simply use the keyword __import__ followed by the module name (with no quotes)

<pre><code data-trim contenteditable>
import math
import random
</code></pre>
</section>

<section markdown="block">
##  So... What Can These Modules Do?

* math
	* __pi__ &rarr;
	* __floor__ &rarr;
	* __sqrt__ &rarr;
* random
	* __random__ &rarr;
	* __randint__ &rarr;

</section>

<section markdown="block">
##  We Know How to Call Functions
<aside>But How Do You Do It From Modules?</aside>

Call or use these definitions by using the module name as the prefix and dot (__.__)... and then the function name

* math.pi()
* math.sqrt(25)
</section>

<section markdown="block">
##  Let's See math and random in Use

<pre><code data-trim contenteditable>
import math
a = math.cos(math.pi)
print(a)
b = math.sqrt(4)
print(b)

import random
a = random.randint(10)
print(a)
b = random.randint(5,10)
print(b)
</code></pre>
</section>

<section markdown="block">
##  Let's Simulate Rolling a Six Sided Die Twice

__Use random to "roll" dice; print out the two die rolls__&rarr;

<div class="fragment" markdown="block"> 
<pre><code data-trim contenteditable>
d1 = random.randint(1,6)
print(d1)
d2 = random.randint(1,6)
print(d2)
</code></pre>
</div>
</section>
