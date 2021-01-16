---
layout: slides
title: Recursion 
---
<section markdown="block" class="title-slide">
# A Very Brief Look at Recursion (We'll See More Later)
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Recursion

__Recursion__ is a process of repeating something in a self similar way.  When we define a __recursive function__, we define a function in terms of itself.  That is, it can call itself to define itself!

A couple of examples where we'll use recursion are:

* an approach to generating a mathematical sequence or computing a mathematical operation 
* generating a fractal

</section>

<section markdown="block">
### Fractals

You know... fractals!

* [Pizza Fractal](http://urbanhonking.com/kmikeym/2010/12/07/fractal-pizza/)
* [The Largest Island in a Lake...](http://www.elbruz.org/islands/Islands%20and%20Lakes.htm)
</section>

<section markdown="block">
### Back to Recursion

So... to create a recursive function definition:

* you'll need to create a function that calls itself
* a way for the function to stop calling itself (sometimes called a base case)
* otherwise... __what do you think will happen here?__

{% highlight python %}
def is_this_forever():
	print("yes")
	is_this_forever()

is_this_forever()
{% endhighlight %}

<div class="incremental" markdown="block">
RuntimeError: maximum recursion depth exceeded while calling a Python object
</div>
</section>

<section markdown="block">
### Factorial Revisited

If we look at factorial again....

* 5! = 5 * 4 * 3 * 2 * 1
* can be rewritten as: 5 * 4!
* we can define factorial in terms of itself!
* (note that 0! is 1)

</section>

<section markdown="block">
### Factorial Using Recursion

__Let's try to reimplement factorial using recursion rather than a loop. &rarr;__

* we'll need to call the function within its definition
* we may need an end condition

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/15/fact.py %}
{% endhighlight %}
</div>
</section>
<section markdown="block">
### Asking Using Recursion

__Let's try to reimplement a program that continues to ask a question until the user says no by using recursion rather than a loop (how does the loop version go again?). &rarr;__

{% highlight python %}
Type "no" to stop
> yup
Type "no" to stop
> no
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
def ask_for_input():
    if input("Type \"no\" to stop\n> ") != "no":
        ask_for_input()
    else:
        # else is not necessary, but left in for clarity
        return

ask_for_input()
{% endhighlight %}
</div>
</section>


<section markdown="block">
### A Tree

__Let's try to draw a tree using recursion. &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
{% include classes/15/tree.py %}
{% endhighlight %}
</div>
</section>

<section markdown="block">
### More Trees

{% highlight python %}
import random
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)

t.left(90)

"""
add functions here
draw_tree
forest
"""

forest()
wn.mainloop()

{% endhighlight %}



</section>

<section markdown="block">
### draw_tree

{% highlight python %}
def draw_tree(s, w):
    if s <= 5:
        return
    else:
        new_w = w if w <= 1 else w - 1
        t.pensize(w)
        a1 = random.randint(20, 50)
        t.forward(s)
        t.left(a1)
        draw_tree(s - random.randint(2, s // 2), new_w)
        a2 = random.randint(20, 50)
        t.right(a1 + a2)
        draw_tree(s - random.randint(2, s // 2), new_w)
        t.left(a2)
        t.back(s)
{% endhighlight %}

</section>

<section markdown="block">
### forest

{% highlight python %}
def forest():
	for x in range(-300, 301, 200):
    	print(x)
    	t.up()
    	t.goto(x, -100)
    	t.down()
    	t.color("#{}".format(str(random.randint(0, 6)) * 3))
    	draw_tree(random.randint(30, 100), random.randint(4, 10))
{% endhighlight %}
</section>
<!--
<section markdown="block">
### Why Recursion?

* Recursive programs 
</section>
-->
