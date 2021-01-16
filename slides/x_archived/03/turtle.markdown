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
* it's essentially a Python implementation of another language called [Logo](http://en.wikipedia.org/wiki/Logo_(programming_language))

</section>

<section markdown="block">
## Some History

So, what's this __Logo__ thing about?

* Logo is an __educational__ language
* one of its most well-known features is turtle graphics 
* built on theory of constructionist learning
	* learning by experimentation
	* learning by making tangible things!
* created in the mid 60's(!) by a group of computer scientists: Daniel G. Bobrow, Wally Feurzeig, Seymour Papert and Cynthia Solomon
</section>

<section markdown="block">
## Seymour Papert

* Papert, in particular, is well known for his work in education and computing
* developed an influential theory on learning called _[constructionism](http://en.wikipedia.org/wiki/Constructionist_learning)_
* was the director of the MIT Artificial Intelligence Laboratory
* besides inventing Logo, also collaborated with Lego (it's not confusing that that's one vowel away from Logo) on a robotics kit called [Mindstorms](http://en.wikipedia.org/wiki/Lego_Mindstorms)

</section>

<section markdown="block">
## (And Like Many Great Computer Scientists, He Has a Beard)

<div class="img-container" markdown="block">![Seymour Papert](../../resources/img/papert.jpg)
</div>

</section>

<section markdown="block">
## Great, So... Why Turtle?

Imagine you have a turtle hanging out on the beach...

<div class="img-container" markdown="block">![Turtle](../../resources/img/turtle.jpg) 
</div>
</section>

<section markdown="block">
## Turtles Drawing Stuff

* imagine further that it's a robotic turtle (__AWESOME!__)
* ...that you can give commands to
	* move forward
	* turn around
* as it moves, it leaves tracks on the ground
* turtle graphics _simulates this_ (seriously)
	* your window is a sandy beach
	* the turtle, is... well... um... a turtle (a virtual robotic one)
</section>

<section markdown="block">
## What Does That Mean for Us?

So... in Python, we now have access to our own drawing turtle

* we can draw by writing code
* that code is analogous to the commands that we would give the turtle (or pen, or pointer, or _whatever_)
	* move forward
	* turn around
* but in addition, we can also
	* change colors
	* ask for user input
	* etc.
</section>

<section markdown="block">
## Hello Turtle
<aside>Enough Talk.  What Does This Code Actually Look Like?</aside>

This draws a line (that's exactly 200 pixels).  (exciting).  Let's try running it.
<pre><code data-trim contenteditable>
{% include classes/13/hello.py %}
</code></pre>
</section>

<section markdown="block">
## About the Drawing Environment

* obviously, we're drawing on a two-dimensional plane
* the turtle starts at the center
* the turtle is facing right (imagine that it's looking east)
* __can you guess what the coordinates (x and y values) are at the center__?
* __where are the positive x values... and the positive y values__?

</section>

<section markdown="block">
## About the Drawing Environment Continued

* you can use __leo.forward(200)__ as a clue!
* if that drew a 200 pixel line, then, maybe
* the center is at (0, 0)
* positive x values are to the right of the origin, positive y, above
* (yeah, maybe that's obvious, but some graphics packages have a different coordinate plane)
</section>

<section markdown="block">
## A Few Tips for Running Programs

Running these programs (from IDLE or from Terminal!) cause a new window to pop up.  You may encounter some _minor annoyances_:

* the window usually opens up __behind the interactive shell (or Terminal)__ &rarr;
* sometimes an extra Python process shows up as a __rocket icon on the dock__ &rarr;
	* even after you've closed your actual drawing's window
	* you can get around this by closing the console
	* (btw, you can also exit the shell using __CTRL-d__)
</section>

<section markdown="block">
## More Tips for Running Turtle
* if there's an __error__, the window of your __program may hang__ &rarr;
	* close the interactive shell to get rid of it
	* ...or force quit the window
* output from __print still shows up in the shell__ &rarr;
	* there won't be any ouptut in your drawing's window for print
	* you'll have to juggle two windows
</section>

<section markdown="block">
## Let's Dissect That Code

bring in the turtle module
<pre><code data-trim contenteditable>
import turtle
</code></pre>
create a Screen object (this provides a canvas to draw on, and some window related commands)
<pre><code data-trim contenteditable>
wn = turtle.Screen()
</code></pre>
create a Turtle object to draw with
<pre><code data-trim contenteditable>
leo = turtle.Turtle()
</code></pre>
</section>

<section markdown="block">
## Let's Dissect That Code Continued
tell the turtle to move forward 200 pixels
<pre><code data-trim contenteditable>
leo.forward(200)
</code></pre>
start the program!
<pre><code data-trim contenteditable>
wn.mainloop()
</code></pre>
</section>

<section markdown="block">
## Objects

So... I used the word __object__ there a few times.  What does that actually mean?

* __object__ - a _thing_ that a variable name can refer to, like a screen or a turtle
* ...in fact, all of the values in Python are things
* they're objects too: "hello" is a str object, 42 is an int object
* an __object__ can have __attributes__ ...data associated with an object
* an __object__ can have __methods__ ...which are basically things that the object can do
</section>

<section markdown="block">
## Methods

* a __method__ is essentially a function that's associated with a particular object
* you can _call_ a method just like a function... but you have to use the dot operator
* object.method() - it's similar to using a method in a module!
* for example: leo.forward(200) 
* ...means I'm calling the forward() function on the turtle object called leo
* in fact... we can see some methods on objects that we've used before!

<pre><code data-trim contenteditable>
dir("hello")
</code></pre>
</section>

<section markdown="block">
## Let's Look at That Code Again...
<pre><code data-trim contenteditable>
{% include classes/13/hello.py %}
</code></pre>
</section>

<section markdown="block">
## The Basic Steps Are...

What did we have to do?

1. bring in the __turtle module__
2. create a __Screen object__
3. create at least one __Turtle object__
4. tell the __Screen object__ to start the program
</section>

<section markdown="block">
## So, That's Some Boilerplate Stuff

We should probably convert our hello program into a template.  You'll need to write this stuff every time you create a program with turtle:

<pre><code data-trim contenteditable>
{% include classes/13/template.py %}
</code></pre>
</section>

<section markdown="block">
## A Note On Names

* in the template, I use __t__ as the variable name for my turtle.  
* it's just a variable name; it can be anything you want (same with __wn__, but you have to change wn everywhere you see it)
* in fact, in my previous programs, I called the turtle leo, in honor of one of these guys

<div class="img-container" markdown="block">![Turtle](../../resources/img/tmnt.gif) 
</div>

</section>

<section markdown="block">
## BTW, I Definitely Encourage You to Follow Along When I Code Up Examples!
</section>

<section markdown="block">
## Basic Turtle Methods

These are all methods that you can call on your __Turtle__ object.

* __forward__(_distance_) - move the turtle forward by the specified _distance_
* __right__(_angle_) - turn the turtle right by _angle_ degrees
* __left__(_angle_) - turn the turtle left by _angle_ degrees
* __back__(_distance_) - move the turtle back by the specified _distance_

<pre><code data-trim contenteditable>
t.forward(200)
t.right(45)
</code></pre>
</section>

<section markdown="block">
## Forward, Right, Left, Back - Code

__BTW... what do you think this draws? &rarr;__

<pre><code data-trim contenteditable>
{% include classes/13/basic.py %}
</code></pre>
</section>

<section markdown="block">
## Screen and Pen Drawing Attributes

Methods you can call on your __Turtle__ object:

* __color__(_colorstring_) - change the color of your _pen_ to _colorstring_, which can be "red", "green", etc.
* __pensize__(_size_) - change the size of your pen to _size_

<pre><code data-trim contenteditable>
t.color("blue")
</code></pre>

Methods you can call on your __Screen__ object

* __setup__(width, height) - window dimensions (default is 50% and 75% of screen)
* __bgcolor__(_colorstring_) - change the background color of your window to _colorstring_

<pre><code data-trim contenteditable>
wn.bgcolor("pink")
</code></pre>
</section>

<section markdown="block">
## Color, Background and Pen Size
<pre><code data-trim contenteditable>
{% include classes/13/color.py %}
</code></pre>
</section>

<section markdown="block">
## Moving Without Drawing

Methods you can call on your __Turtle__ object:

* __up__() - pick the pen up so that the turtle object doesn't draw when it moves
* __down__() - put the pen down so that the turtle object draws when it moves
<pre><code data-trim contenteditable>
t.up()  # picks the pen up, doesn't draw when the turtle moves
</code></pre>
</section>


<section markdown="block">
## Pen Up, Pen Down

__BTW... what do you think this draws? &rarr;__

<pre><code data-trim contenteditable>
{% include classes/13/pen.py %}
</code></pre>
</section>

<section markdown="block">
## Going Somewhere?

A method you can call on your __Turtle__ object:

__goto__(_x_, _y_) - move the turtle to the specified coordinates ..._x_ and _y_.  Note that if the pen is down, it will draw up to that coordinate.

<pre><code data-trim contenteditable>
t.goto(200, 200)  # picks the pen up, doesn't draw when the turtle moves
</code></pre>
</section>

<section markdown="block">
## Goto

__BTW... what do you think this draws? &rarr;__

<pre><code data-trim contenteditable>
{% include classes/13/goto.py %}
</code></pre>
</section>

<section markdown="block">
## A Confused Turtle

A quick demo using goto: __let's try incorporating random elements to our drawings!__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{% include classes/13/confused.py %}
</code></pre>
</div>
</section>
<section markdown="block">
##  Let's Use What We Know to Create a Square!

__How would we tell the turtle to create a square with the upper left corner at the origin? Each side should be 200px long.  We just learned goto, so let's try that.&rarr;__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{% include classes/13/square_goto.py %}
</code></pre>
</div>
</section>

<section markdown="block">
## Another Square!

__Same thing, but this time, just use forward or back and either left or right.  &rarr;__

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
{% include classes/13/square_basic.py %}
</code></pre>
</div>
</section>

<section markdown="block">
## For a Square....

__How can we simplify the previous version?  There was a lot of repeated code! &rarr;__

<div class="fragment" markdown="block">
Clearly, this calls for a __for loop__!

<pre><code data-trim contenteditable>
{% include classes/13/square_with_loops.py %}
</code></pre>
</div>
</section>

<section markdown="block">
## Loops for Squares?

Ugh... so, every time we want a square, we have to write another loop? That seems a bit cumbersome. 

__What can we do to package up a drawing of a square so that we we don't have to explicitly worry about looping?__ &rarr;


<div class="fragment" markdown="block">
How about we write a function?

* every time we want a square, we just call draw_square()
* all of the implementation details of drawing a square are hidden within that function
* __easy enough__ &rarr;
</div>


</section>

<section markdown="block">
## draw_square Function

__Write a function to draw a square with a side of length 200.__ &rarr;

* parameters: 0 (no parameters)
* processing: draws a square with side of length 200
* return value: None (does not return anything)

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
# turtle setup

function draw_square():
	for i in range(4):
    	t.forward(200)
    	t.right(90)

draw_quare()

wn.mainloop()

</code></pre>
</div>

</section>

<section markdown="block">
## Cool Function, Bro... But...

So, our function worked pretty well for drawing a square, but there's a major shortcoming. __What's not so great about the draw_square function that we created?__ &rarr;

<div class="fragment" markdown="block">
For every different sized square, we'd have to create another function. __How do we get around this?__ &rarr;

Parameterize the side length!

<pre><code data-trim contenteditable>
def draw_square(side_length):
	for i in range(4):
    	t.forward(side_length)
    	t.right(90)
</code></pre>
</div>
</section>

<section markdown="block">
## Ok, Now What? Using draw_square(...)

Eh? That was a lot of work, but for what. __Let's try our new draw square_function by drawing _a lot_ of squares!__ &rarr;

<div class="fragment" markdown="block">

<pre><code data-trim contenteditable>
for size in range(10, 501, 10):
    draw_square(size)
    t.up()
    t.back(5)
    #t.forward(5)
    t.down()
    #t.left(10)
</code></pre>
</div>
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
</section>



<section markdown="block">
## Enough With Squares

__Long live pentagons!__ More sides equals _more_ better, right!?

But first. Some geometry

* __sum of interior angles__ of a polygon are: 
	* (number of sides - 2) × 180°
* to get each __interior angle__ of a polygon, divide the sum of interior angles by number of sides:
	* sum of interior angles / sides
* so, the turtle has to turn 180 - the interior angle

</section>

<section markdown="block">
## Planning for a Pentagon

So, for a pentagon, __when we apply the calculations from the previous slide...__ &rarr;

* sum_interior_angles = (5 - 2) * 180 = 540
* interior_angle = 540 / 5 = 108
* turtle_angle = 180 -108 = 72
</section>


<section markdown="block">
## Pentagons

Ok, so that means we have 5 sides, and the turtle has to turn 72 degrees. __Let's create a draw_pentagon function__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
def draw_pentagon(side_length):
    for i in range(5):
        t.forward(side_length)
        t.right(72)

draw_pentagon(200)
</code></pre>
</div>
</section>

<section markdown="block">
## Same but Different

Let's check out our draw_square and draw_pentagon functions. __Can anyone find another _thing_ to parameterize?__ &rarr;

<pre><code data-trim contenteditable>
def draw_square(side_length):
    for i in range(4):
        t.forward(side_length)
        t.right(90)

def draw_pentagon(side_length):
    for i in range(5):
        t.forward(side_length)
        t.right(72)

</code></pre>

<div class="fragment" markdown="block">
The number of sides!
</div>
</section>

<section markdown="block">
## Why. Stop. At. Squares and Pentagons. Polygonz!

So many shapes. __Let's create one function that could draw a square, pentagon or even a tetradecagon__. &rarr;

Create a function called __draw_poly__ that has two parameters: 

* number of sides
* length of a side...

Remember the following calculations:

* __sum interior angles__ = (num sides - 2) × 180°
* __interior angle__ = sum interior angles / num sides
* __turtle's turn angle__ = 180 - interior angle

</section>

<section markdown="block">
## draw_poly

<pre><code data-trim contenteditable>
def draw_poly(sides, side_length):
    sum_interior_angles = (sides - 2) * 180
    interior_angle = sum_interior_angles / sides
    a = 180 - interior_angle
    for i in range(sides):
        t.forward(side_length)
        t.right(a)
</code></pre>
</section>


<section markdown="block">
## Polygonz!

__Let's draw a bunch of polgons, starting with a rectangle, going up to and including a 10-gon.__ &rarr;

<div class="fragment" markdown="block">
<pre><code data-trim contenteditable>
t.up()
t.back(300)
t.down()
for sides in range(3, 11):
    draw_poly(sides, 1 / sides * 175)
    t.setheading(0)
    t.up()
    t.forward(70)
    t.down()
</code></pre>
</div>
</section>


<section markdown="block">
## Circle

We were kind of approaching a circle at the end there. __This is a pretty decent approximation.__ &rarr;

<pre><code data-trim contenteditable>
draw_poly(60, 30)
</code></pre>

Buuuut... of course there's also a __circle(radius__ method:

<pre><code data-trim contenteditable>
t.circle(50)
</code></pre>
</section>


<section markdown="block">
## ontimer

__Let's bring time into the mix!__ &rarr;

The Screen object function, __ontimer__, allows a function to be executed some specified time (in milliseconds) later. For example, the following code would call a function called my_draw 500 milliseconds later.

<pre><code data-trim contenteditable>
wn.ontimer(my_draw, 500)
</code></pre>

Notice that the function name is passed in as you would any other variable name.

__On to an example...__ &rarr;
</section>

<section markdown="block">
## ontimer Example

__What will happen when this program is run?__ &rarr;

<pre><code data-trim contenteditable>
# usual turtle set up above is omitted
t.hideturtle()
wn.tracer(0)

# assuming draw_square function was defined above
def draw_stuff():
    draw_square(20)
    t.up()
    t.forward(22)
    t.down()
    wn.update()

wn.ontimer(draw_stuff, 2000)
wn.ontimer(draw_stuff, 4000)
wn.ontimer(draw_stuff, 6000)
wn.ontimer(draw_stuff, 8000)

wn.mainloop()
</code></pre>
</section>

<section markdown="block">
## ontimer Example Continued

Let's modify our __draw_stuff__ method ever so slightly. __What will happen when this program is run?__ &rarr;

<pre><code data-trim contenteditable>
def draw_stuff():
    draw_square(20)
    t.up()
    t.forward(22)
    t.down()
    wn.update()
    # move ontimer into the function body
    wn.ontimer(draw_stuff, 500)

# now call draw_stuff once...
draw_stuff()
</code></pre>
</section>

<section markdown="block">
## clear

To __reset the drawings on the screen__, just call __clear__ on your turtle object!

<pre><code data-trim contenteditable>
t.clear()
</code></pre>

This is actually kind of handy because... __we can do clear the screen before drawing each square__ (which essentially has the effect of... ???) &rarr;
</section>

<section markdown="block">
## Animation!

Clearing the screen before we draw a square at a new position __has the effect of animation!__ &rarr;

<pre><code data-trim contenteditable>
def draw_stuff():
    # clear the screen
    t.clear()
    draw_square(20)
    t.up()

    # descrease the forward movement 
    t.forward(22)
    t.down()
    wn.update()
    wn.ontimer(draw_stuff, 500)
</code></pre>
</section>


<section markdown="block">
## Putting Everything Together

Ok ... so this is a bit ambitious. Let's try creating a bouncing circle. __Starting with some setup code:__ &rarr;

<pre><code data-trim contenteditable>
import turtle

t, wn = turtle.Turtle(), turtle.Screen()

turtle_x, turtle_y, turtle_dx, turtle_dy = [0], [0], [0], [-0.1]

# store acceleration
acc = -0.5

# turn animation of turtles off
wn.tracer(0)
t.hideturtle()

# draw function goes here

draw()
wn.mainloop()
</code></pre>
</section>


<section markdown="block">
## Putting Everything Together

Aaaand... __filling in our draw function__ &rarr;

<pre><code data-trim contenteditable>
def draw():
    t.clear()
    t.penup()
    t.goto(turtle_x[0], turtle_y[0])
    t.pendown()
    turtle_y[0] += turtle_dy[0]

    # change velocity based on acceleration
    turtle_dy[0] += acc
    t.circle(15)

    wn.update()
    wn.ontimer(draw, 30)
    
    # bounce!
    if turtle_y[0] <= -250:
        turtle_dy[0] *= -1
</code></pre>
</section>

<section markdown="block">
## Reviewing Objects and Methods

__What's an object and what's a method? &rarr;__

* __object__ - a _thing_ that a variable name can refer to, like a Screen, Turtle, int or str
* an __object__ can have __methods__ ... things that the object can do
* a __method__ is a function that you can call from a particular object
</section>

<section markdown="block">
## Again a Few Tips for Running Programs

Running these programs (from IDLE or from Terminal!) cause a new window to pop up.

* the window usually opens up behind the interactive shell (or Terminal)
* if there's an error, the window of your program may hang. __demo &rarr;__
	* close the interactive shell to get rid of it
	* ...or force quit the window
* your prints still show up in the shell, but you'll have to juggle two windows. __demo &rarr;__
</section>

