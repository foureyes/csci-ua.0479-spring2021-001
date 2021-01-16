---
layout: slides
title: "Notes"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

{% comment %}

## functions
* function definition
* keyword args and default values
* arbitrary num of args with \*args
* arbitrary num of keword args with \*\* kwargs
* calling a function vs a function name
* passing a function in as an argument
* declaring a function within a function
* returning a function
* closure
* scope 
    * global, local, built-in
    * name resolution
    * can you change globals / assignment?
        * maybe
        * mutable vs immutable?
    * why doesn't += work in function def?
* global / nonlocal (you can change, tho)

## Using Built-in Modules
* what are modules?
* how do you bring them in?
* from package import module_name
* from package import \*
* import package as alias
* math
    * sqrt
    * trig functions (sin, cos, etc.)
* random
    * random
    * randint
    * randrange
    * choice
    * shuffle
* turtle
    * creating canvas and pen 
        * <code>t = turtle.Turtle()</code>
        * <code>wn = turtle.Screen()</code>
    * setup
        * <code>wn.bgcolor('')</code>
        * <code>wn.setup(w, h)</code>
        * <code>wn.mainloop</code>
    * drawing
        * <code>t.forward(l)</code>
        * <code>t.left(a)</code>
        * <code>t.right(a)</code>
        * <code>t.heading(a)</code>
        * <code>t.circle(r)</code>
        * <code>t.color(c)</code>
        * <code>t.begin_fill()</code>
        * <code>t.end_fill()</code>
        * <code>t.clear()</code>
    * projects
        * create triangle 180
        * square 90
        * poly ... angle = 360 / num sides
        * approximate a circle?
    * turning off drawing animation
        * <code>wn.tracer(0)</code>
        * <code>t.hideturtle</code>
        * <code>wn.update()</code>
    * timer events
        * <code>wn.ontimer(f, t)</code>
    * key events
        * <code>wn.onkeypress(f, k)</code>
        * <code>wn.listen()</code>
    * animation
        * turn off drawing
        * ontimer
        * ontimer f must call ontimer again
    * more projects
        * animate a circle
        * make it bounce back?
        * control w/ key
        * intersection w/ rects
            * x1, y1, x2, y2

## creating and installing modules
    * what's a module again?
    * um... then it should be in our file system?
    * where does python look?
        * cur dir
        * PYTHON PATH
        * system wide
    * create a module
        * same path
        * drop into Python path?
    * try to use matplotlib
    * but it's not built in!
    * install a module
        * site-packages
        * easy_install
        * pip
        * (diff versions per version of python)
        * use pycharm PyCharm &rarr; preferences &rarr; Porject Interpreter &rarr; +
    * what's a virutalenv?
        * why?
        * how does it work in pycharm
* matplotlib
    * <code>import matplotlib.pyplot as plt</code>
    * <code>http://matplotlib.org/api/markers_api.html</code>
    * <code>plt.plot(x, y, marker='o', color="blue")</code>
    * [markers](http://matplotlib.org/api/markers_api.html)

<pre><code data-trim contenteditable>
import matplotlib.pyplot as plt
axis = plt.gca()
axis.xaxis.set_ticks_position('bottom')
axis.spines['bottom'].set_position(('data', 0))
axis.yaxis.set_ticks_position('left')
axis.spines['left'].set_position(('data', 0))
for i in range(-100, 100, 5):
    plt.plot(i, i, marker='o', color="blue")
        plt.plot(i, 100 - i, marker='o', color="red")

        #plt.plot([-4, 1,2,3,4], [-10, 1,4,9,16], 'ro', color='blue')
        plt.show()

</code></pre>
{% endcomment %}

