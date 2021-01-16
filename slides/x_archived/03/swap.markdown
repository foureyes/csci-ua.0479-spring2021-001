---
layout: slides
title: Swapping Values 
---

<section markdown="block" class="title-slide">
#  Swapping Values
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Here's a Quick Exercise on a Tiny Algorithm
<aside>And Idioms, as Well!</aside>
__If I have two variables, a and b, and they are set to 3 and 21 respectively, how would I swap their values in code? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
a = 3
b = 21
print("a:", a, "b:", b)
c = b
b = a
a = c
print("a:", a, "b:", b)
{% endhighlight %}
</div>
</section>

<section markdown="block">
###  An Idiomatic Way to Do It
<aside>(read: easier)</aside>
Here's another, more idiomatic way to do it
{% highlight python %}
a = 3
b = 21
a, b = b, a
{% endhighlight %}
You can use the same construct to assign multiple values (these features are not common in other languages). &rarr;
{% highlight python %}
a, b = 3, 21
{% endhighlight %}
</section>

<section markdown="block">
###  Some BTWs
* in Python, if something is idiomatic, it's called Pythonic
* this swap example brings up a trickier part of programming: references and values
	* if you're eager, or like being confused here's a link about references and values in Python:
	* http://od-eon.com/blogs/bogdan/python-assignment-value-or-reference/
	* we'll revisit this later!
</section>

<section markdown="block">
##  [Greeaaat.  Now, what do we do with all of these variables and assignments?](user-input.html)
</section>
