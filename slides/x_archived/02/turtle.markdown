---
layout: slides
title: Turtle Graphics 
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Turtle

__turtle__ is a Python module...

* that allows you to draw programmatically
	* think of a virtual [pen plotter](https://www.youtube.com/watch?v=iziP0cQhOFY&feature=youtu.be&t=20s)
	* commands are given to a movable pen
	* that pen can move and draw on a two dimensional plane
	* the pen is called a turtle!
* it's essentially a Python implementation of another language (created by Seymour Papert) called [Logo](http://en.wikipedia.org/wiki/Logo_(programming_language))

</section>



<section markdown="block">
## Objects

Before we get into using the <code>turtle</code> module for drawing, __let's talk about objects and methods__ &rarr;

* __object__ - a _thing_ that a variable name can refer to, like a screen or a turtle
* _Everything_ in Python is an object (ints, strs, lists, functions, etc.)
* an __object__ can have __attributes__ ...data associated with an object
* an __object__ can have __methods__ ...which are basically things that the object can do
</section>

<section markdown="block">
## Methods

* a __method__ is essentially a function that's associated with a particular object
* you can _call_ a method just like a function... but you have to use the dot operator
* object.method() - it's similar to using a method in a module!
* for example: leo.forward(200) 
* ...means I'm calling the forward() function on object named leo
</section>

<section markdown="block">
## Screens and Turtles

When drawing with the <code>turtle</code> module, we'll be doing most our work with the following objects:

* a __Screen__ object
* one or more __Turtle__ objects

The <code>Turtle</code> object represents our pen... and the <code>Screen</code> object represents the window that we're drawing on.

</section>

<section markdown="block">
## Boilerplate

__A program that uses the <code>turtle</code> usually starts with the following boilerplate code__ &rarr;

<pre><code data-trim contenteditable>
import turtle
wn = turtle.Screen()
leo = turtle.Turtle()

// draw stuff here

wn.mainloop()
</code></pre>

1. bring in the __turtle module__
2. create a __Screen object__
3. create at least one __Turtle object__
4. prevent the window from closing (use <code>wn.mainloop</code>)
</section>


<section markdown="block">
## Basic Turtle Methods

These are some methods that you can call on your __Turtle__ object for drawing and moving.

* __forward__(_distance_) - move turtle forward by specified _distance_
* __back__(_distance_) - move turtle back by specified _distance_
* __circle__(_radius_) - draw a circle with radius, _radius_
* __clear__() - clears all of the turtle's drawings
* __right__(_angle_) - turn the turtle right by _angle_ degrees
* __left__(_angle_) - turn the turtle left by _angle_ degrees
* __setheading__(_angle_)- turn turtle so that it faces a heading:
    * 0 - right
    * 90 - down
    * 180 - left
    * 270 - up
* __goto__(_x_, _y_) - move the turtle to the specified coordinates ..._x_ and _y_.  Note that if the pen is down, it will draw to that coordinate.


</section>

<section markdown="block">
## Examples of Basic Turtle Methods

<pre><code data-trim contenteditable>
t.clear()       # remove's all of this turtle's drawings
t.setheading(0) # rotates turtle so that it's facing right
t.left(45)      # turns the turtle left 45 degrees
t.goto(200, 200)# moves the turtle to 200, 200
t.forward(100)  # moves the turtle forward 100 pixels
</code></pre>
</section>

<section markdown="block">
## Screen and Pen Drawing Attributes

Methods you can call on your __Turtle__ object:

* __color__(_colorstring_) - change the color of your _pen_ to _colorstring_, which can be "red", "green", etc.
* __pensize__(_size_) - change the size of your pen to _size_

<pre><code data-trim contenteditable>
t.color("blue")
t.pensize(5)
</code></pre>

Methods you can call on your __Screen__ object

* __setup__(width, height) - window dimensions (default is 50% and 75% of screen)
* __bgcolor__(_colorstring_) - change the background color of your window to _colorstring_

<pre><code data-trim contenteditable>
wn.setup(500, 500)
wn.bgcolor("pink")
</code></pre>
</section>


<section markdown="block">
## Moving Without Drawing

Methods you can call on your __Turtle__ object:

* __up__() - pick the pen up so that the turtle object doesn't draw when it moves
* __down__() - put the pen down so that the turtle object draws when it moves

<pre><code data-trim contenteditable>
t.up()  # picks the pen up, doesn't draw when the turtle moves
t.forward(100)
t.down()
</code></pre>
</section>


<section markdown="block">
## Drawing Two Lines 

(without having a line connect them!). Use <code>up</code> and <code>down</code>. __This draws a line starting at 0, 0... and another starting at 150, 150__.

<pre><code data-trim contenteditable>
t.up()
t.goto(0, 0)
t.down()
t.forward(100)
t.up()
t.goto(150, 150)
t.down()
t.forward(100)
</code></pre>


</section>

<section markdown="block">
## A Little Help Please

That was a lot of calls to up and down! We can use what we know about functions as objects to shorten our code a bit. __<code>up_then_down</code> will call whatever function that's passed in to it between calls to t.up and t.down__ &rarr;

<pre><code data-trim contenteditable>
def up_then_down(t, f, *args):
    t.up()
    f(*args)
    t.down()
</code></pre>

<pre><code data-trim contenteditable>
up_then_down(t, t.goto, 0, 0)
t.forward(100)
up_then_down(t, t.goto, 150, 150)
t.forward(100)
</code></pre>

</section>

<section markdown="block">
##  Let's Use What We Know to Create a Square!

Ok... just go forward, then turn 90 degrees. Do this four times... aaaand:

<pre><code data-trim contenteditable>
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
</code></pre>
</section>

<section markdown="block">
## Square Continued

That was kind of silly. _Soooo much repeated code_. Let's put that into a loop.

<pre><code data-trim contenteditable>
for i in range(4):
    t.forward(100)
    t.right(90)
</code></pre>

</section>

<section markdown="block">
## Square Function 

Wellll... this looks like a good candidate for a function.


<pre><code data-trim contenteditable>
def draw_square():
    for i in range(4):
        t.forward(100)
        t.right(90)
</code></pre>
</section>

<section markdown="block">
## Square Function with Parameters

But... what if we want a square that's a different size? __We should parameterize our function.__ &rarr;

<pre><code data-trim contenteditable>
def draw_square(side):
    for i in range(4):
        t.forward(side)
        t.right(90)
</code></pre>

</section>

<section markdown="block">
## Square Function, turtle Object as Parameter

We might as well make the turtle object a parameter too... so that we don't rely on a global variable named, t.

<pre><code data-trim contenteditable>
# note that we pass in a turtle object, t
# ... so that our function doesn't rely on a global
def draw_square(t, side):
    for i in range(4):
        t.forward(side)
        t.right(90)
</code></pre>
</section>

<section markdown="block">
## Square Function, Heading

Depending on the direction that your turtle is headed, the turtle may start at different corners. __To make your turtle start consistently from the upper left corner, set the turtle's heading so that it faces right.__ &rarr;

<pre><code data-trim contenteditable>
def draw_square(t, side):
    # make sure we consistently start at the upper left corner
    t.setheading(0)
    for i in range(4):
        t.forward(side)
        t.right(90)
</code></pre>
</section>


<section markdown="block">
## Why Limit Ourselves to Squares?

We can parameterize the number of sides so that we can draw any polygon.

* we'll have to calculate the interior angles though...
    * for a square, it's 90
    * for a triangle, it's 180
    * what's the pattern?
* {:.fragment} 360 / number_of_sides ... gives the interior angle

<pre><code data-trim contenteditable>
def draw_poly(t, num_sides, side):
    t.setheading(0)
    a = 360 / num_sides
    for i in range(num_sides):
        t.forward(side)
        t.right(a)
</code></pre>

</section>

<section markdown="block">
## Coloring the Polygon

To fill the interior of our shape with a color, we'll use the following methods:

* __t.color(color)__ - sets the color that will be used to fill the shape... a string representing a hex color code or a text color can be used as the argument ('red' or '#ff0000')
* __t.begin_fill()__ - start the shape to be filled
* __t.end_fill()__ - end the shape to be filled


<pre><code data-trim contenteditable>
# we'll have a default color set via a keyword argument...
def draw_poly(t, num_sides, side, color='#888888'):
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    a = 360 / num_sides
    for i in range(num_sides):
        t.forward(side)
        t.right(a)
    t.end_fill()
</code></pre>
</section>

<section markdown="block">
## Using draw_poly

A triangle...

<pre><code data-trim contenteditable>
draw_poly(t, 3, 100, color='#993355')
</code></pre>

An octagon...

<pre><code data-trim contenteditable>
draw_poly(t, 8, 50, color='#225599')
</code></pre>

What happens if we have a very large number of sides?

<pre><code data-trim contenteditable>
draw_poly(t, 90, 5, color='#227744')
</code></pre>

{:.fragment}
We're kind of approaching a circle! 

{:.fragment}
Buuuut... of course there's also a __circle(radius)__ method:

<pre class="fragment"><code data-trim contenteditable>
t.circle(50)
</code></pre>
</section>

<section markdown="block">
## Y So Slow?

It's fun watching the turtle draw stuff for the first couple of times you work on your program, but it gets _super annoying_ immediately after that. 

Just like cooking shows where the food magically appears all cooked, __we can get to the drawing results faster by adding these two lines of code__: &rarr;

<pre><code data-trim contenteditable>
# after creating a turtle and a screen...

t.hideturtle()
wn.tracer(0)

# after drawing stuff...
wn.update()
</code></pre>
</section>

<section markdown="block">
## hideturtle, tracer, update

Ok... so those two special methods for drawing more quickly were:

* t.__hideturtle()__ - makes the turtle invisible (this _actually_ speeds up drawing, somehow!?)
* wn.__tracer(0)__ - turns animation off
* wn.__update()__ - to remind Python to _actually_ refresh the window with the new drawing
    * use this whenever you want the screen to update with the _latest_ version of your drawing!
</section>






<section markdown="block">
## ontimer

__Let's bring time into the mix!__ &rarr;

The Screen object function, __ontimer__, allows a function to be executed some specified time (in milliseconds) later. For example, the following code would call a function called my_draw 500 milliseconds later.

<pre><code data-trim contenteditable>
wn.ontimer(my_draw, 500)
</code></pre>

Notice that the function name is passed in as you would any other variable name.</section>

__On to an example...__ &rarr;
</section>

<section markdown="block">
## ontimer Example

__What will happen when this program is run?__ &rarr;

<pre><code data-trim contenteditable>
def f():
    print('called')

wn.ontimer(f, 2000)
wn.ontimer(f, 4000)
wn.ontimer(f, 6000)
wn.ontimer(f, 8000)
</code></pre>

{:.fragment}
<code>called</code> gets printed out 4 times, with each being printed in 2 second intervals (the first one 2 seconds into the program running, the second 4 seconds, etc.).
</section>

<section markdown="block">
## ontimer Example Continued

Let's use <code>ontimer</code> to continually draw a bunch of circles.

<pre><code data-trim contenteditable>
# setup, turning off animation
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)
t.hideturtle()
</code></pre>
<pre><code data-trim contenteditable>
# set some global variables for the
x, y = 0, 0

def next_frame():
    # use global keyword so that x can be modified
    global x
    t.up()
    t.goto(x, y)
    t.down()
    t.circle(100)
    x += 5 
    # this will cause next_frame to be called again!
    wn.ontimer(next_frame, 50)
    # don't forget to force a window update!
    wn.update()

# call function once
next_frame()
wn.mainloop()
</code></pre>

Using the exact code above, you should get a bunch of circles drawn, with each new circle popping up after 50 milliseconds.
</section>

<section markdown="block">
## Animation

We only need to make a minor modification to our previous code to create an animation! Simply clear the window before drawing the circle.

Change <code>next_frame</code> so that it calls clear at the beginning:

<pre><code data-trim contenteditable>
def next_frame():
    global x
    # clear everything out before drawing circle
    t.clear()
    t.up()
    t.goto(x, y)
    t.down()
    t.circle(100)
    x += 5 
    wn.ontimer(next_frame, 50)
    wn.update()
</code></pre>
</section>

<section markdown="block">
## Sample Program with Naive Collision Detection

Setup

<pre><code data-trim contenteditable>
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.hideturtle()
wn.tracer(0)
</code></pre>

Globals

<pre><code data-trim contenteditable>
# attributes of one square...
# x, y, width, height, velocity
x, y, w, h, v = -300, 0, 50, 50, 2
</code></pre>

</section>

<section markdown="block">
## Sample Program Continued

Draw rectangle function...

<pre><code data-trim contenteditable>
def draw_rect(t, x, y, w, h, color='#777799'):
    t.color(color)
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(0)
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()
</code></pre>

Determine if a point is in a rectangle
<pre><code data-trim contenteditable>
def point_in_rectangle(x, y, x1, y1, x2, y2):
    print(x, y, x1, y1, x2, y2)
    return x >= x1 and x <= x2 and y >= y2 and y <= y1
</code></pre>


wn.ontimer(next_frame, 50)

wn.mainloop()
</section>

<section markdown="block">
## Sample Program Continued

<pre><code data-trim contenteditable>
def next_frame():
    t.clear()
    global x
    color = 'green'
    # check each corner of our rectangle to see if it's inside the other rectangle
    for p in [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]:
        if point_in_rectangle(p[0], p[1], 0, 0, 100, -100):
            color = 'blue'
    draw_rect(t, 0, 0, 100, 100)
    draw_rect(t, x, y, w, h, color=color)
    x += v
    wn.ontimer(next_frame, 10)
</code></pre>

<pre><code data-trim contenteditable>
next_frame, 50
wn.mainloop()
</code></pre>
</section>

<section markdown="block">
## Listening for Key Presses

To listen for keypresses, use the following methods:

* __wn.onkeypress(function, key)__ - call function when key is pressed
* __wn.listen()__ - listen for keypresses

</section>

<section markdown="block">
## Key Press Example

Usual setup stuff...
<pre><code data-trim contenteditable>
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.tracer(0)
t.hideturtle()
</code></pre>

global

<pre><code data-trim contenteditable>
x, y, v = 0, 0, 2
</code></pre>
</section>

<section markdown="block">
## Key Press Example Continued

Our function that repeatedly draws a circle... to create an animation.
<pre><code data-trim contenteditable>
def next_frame():
    t.clear()
    global x, v
    t.up()
    t.goto(x, y)
    t.down()
    t.circle(50)
    x += v 
    wn.ontimer(next_frame, 50)
    wn.update()
</code></pre>
</section>

<section markdown="block">
## Key Press Example Continued

Key press event handlers

<pre><code data-trim contenteditable>
def handle_left():
    global v
    print('left pressed')
    v = -2

def handle_right():
    global v
    print('right pressed')
    v = 2
</code></pre>

_Attaching_ handlers to specific keys...

<pre><code data-trim contenteditable>
wn.onkeypress(handle_left, 'Left')
wn.onkeypress(handle_right, 'Right')
</code></pre>

Finishing up...

<pre><code data-trim contenteditable>
next_frame()
wn.listen()
wn.mainloop()
</code></pre>
</section>
