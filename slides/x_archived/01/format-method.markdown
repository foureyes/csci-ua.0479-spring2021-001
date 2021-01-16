---
layout: slides
title: "format Method"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Constructing Strings

Although Python prides itself in having _"only one obvious way to do things"_ ... there's actually quite a few ways to put together a string. __Here are two of them.__ &rarr;

<pre><code data-trim contenteditable>
greeting, name = 'hi', 'joe'
print(greeting + ' my name is ' + name)
print("%s my name is %s" % (greeting, name))
</code></pre>

We're using...

* __string concatenation__ for the first
* __string formatting with the % operator__ for the second

</section>

<section markdown="block">
## The format Method

There's a third, more _modern_ way to put together strings, and that's __the <code>format</code> method found in the <code>str</code> object__. &rarr;

* start with a string with placeholders (curly braces)
* call the <code>format</code> method...
* with values that you want to go into the placeholders
* the format method __always returns a string!__

<br>

__Let's see this in action.__ &rarr;

</section>

<section markdown="block">
## The format Method

Using curly braces as a placeholder...

<pre><code data-trim contenteditable>
>>> 'blah {}'.format('bloop')
'blah bloop'
</code></pre>

The argument, 'bloop' is placed where the curly braces are located.

</section>

<section markdown="block">
## Multiple Arguments

__You can have more than one placeholder...__ &rarr;

* pass in more than one argument
* arguments are put into the placeholders in the order that they occur

<pre><code data-trim contenteditable>
>>> 'blah {} {}'.format('bloop', 'bleep')
'blah bloop bleep'
</code></pre>

</section>

<section markdown="block">
## Doubled Curly Braces

Um. __What happense here?__ &rarr;

* doubling curly braces is valid syntax
* it's used as a way to _escape_ a curly brace (so... if you want an actual curly brace in your string, double it!)
{% raw %}
<pre><code data-trim contenteditable>
>>> 'blah {} {{}}'.format('bloop')
'blah bloop {}'
</code></pre>
{% endraw %}
</section>

<section markdown="block">
## More Placeholders Than Arguments

You can actually have more placeholders than arguments... and you can specify which argument is placed in the placeholder.

__Simply add the position of the argument within curly braces.__ &rarr;

<pre><code data-trim contenteditable>
>>> 'blah {0} {1} {0}'.format('bloop', 'bleep')
'blah bloop bleep bloop'
</code></pre>
</section>

<section markdown="block">
## Keyword Arguments

Finally, __you can actually place names in your placeholders... and pass in values using keyword args__ &rarr;

<pre><code data-trim contenteditable>
>>> '{greeting} {name}!'.format(greeting='hey', name='joe')
'hey joe!'
</code></pre>
</section>
