---
layout: slides
title: "Processing"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>




<section markdown="block">
## Processing

* Processing programs are called __sketches__ 
* (Processing is used for _creative coding_, _graphics experiments_, and education)
* The Processing library is actually written in __Java__ 
    * Java programs are compiled to "bytecode" that is runnable by the Java Virtual Machine (JVM)
    * Other languages can also be compiled to "bytecode" runnable by the JVM
* Python can be turned into Java "bytecode" (the project that does this translation is Jython)
* (Jython is what Python mode for Processing uses so that you can write Python with a library that was meant for Java)

</section>

<section markdown="block">
## Getting Processing

Download the appropriate version of the Processing IDE and libraries from:

[processing.org](https://processing.org/)

To add Python as a language that you can use:

1. go to `Tools` &rarr; Add Tool
2. click on the `Modes` tab
3. find `Python Mode for Processing 3`
4. click on `Install`

</section>

<section markdown="block">
## Setting Up a Processing Sketch

In the Processing IDE's text editor, the minimum amount of code you'll need is two functions:

1. setup
2. draw

Both have no parameters. In the sample below, we write `pass` for the body of each function as way of saying that this function doesn't do anything yet (`pass` essentially means no operation needs to be done here).

<pre><code data-trim contenteditable>
def setup():
    pass

def draw(): 
    pass

</code></pre>
</section>


<section markdown="block">
## Setup and Draw

The two functions that you defined, `setup` and `draw` are special functions that are __automatically called when a Processing sketch is run__ &rarr;

* `setup` - is called exactly once when your program first runs
* `draw` - is called repeatedly at a specific interval after `setup` is called


</section>

<section markdown="block">
## Processing Documentation

For a full reference, check out the Processing site:


* It's a bit nacent, so the documentation for it isn't quite comprehensive
* However you can use the original Processing docs, and usually that'll be quite adequate

[Processing Reference](https://processing.org/reference/)

</section>

<section markdown="block">
## Your Canvas!

You can modify and access attributes of your sketch's window by using the following __built-in__ Processing methods and variables:

* <code>background(r, g, b) // or just background(n) for grayscale</code>
* <code>size(width, height) // window dimensions</code>
* <code>width // width of window</code>
* <code>height // height of window</code>

Note that...

* `size` is usually only called once in the `setup` method
* `background` can be called in `setup`...
* but, if you want to "repaint" the background each time draw is called, you can use it there as well
* __why would you want to do that?__ &rarr;

__Let's try these.__ &rarr;
</section>

<section markdown="block">
## Drawing Shapes

Some methods for drawing shapes:

* <code>ellipse(x, y, width, height)</code>
* <code>rect(x, y, width, height)</code>
* <code>triangle(x1, y1, x2, y2, x3, y3)</code>
* <code>stroke() // all subsequent shapes have an outline</code>
* <code>noStroke() // all subsequent shapes don't have an outline</code>
* <code>strokeWeight(width) // set line and outline width</code>
* <code>line(x1, y1, x2, y2)</code>
* <code>fill(r, g, b) // or fill(n) ... all subsequent shapes are filled in with color</code>
* <code>background(r, g, b) // or background(n) will repaint the entire screen with color</code>

__Let's try a few of these within our setup function.__ &rarr;
</section>

<section markdown="block">
## How About Shapes That Occupy the Same Space?

What happens if we draw two shapes over each other (can they overlap)? __Let's try it out. Describe what happens.__ &rarr;

* {:.fragment} shapes can overlap
* {:.fragment} however, the last shape drawn is rendered over all of the other previous shapes
</section>

<section markdown="block">
## Fill, Background

Both fill and background have 1, 3, and 4 parameter versions:

* with 3 parameters, the colors represent red, green, and blue, each with a value from 0 through 255
	* red: 255, 0, 0
	* yellow: 255, 255, 0
	* want dark blue: 10, 10, 70
* the 4 parameter version's last parameter is alpha (or opacity):
	* also 0-255
	* example: <code>fill(40, 200, 40, 180);</code>
* with 1 parameter, it represents grayscale
</section>


<section markdown="block">
## Drawing a Crescent Moon

__Draw this using two circles:__ &rarr;

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/crescent.png)
</div>

</section>

<section markdown="block">
## A Crescent Continued

<pre><code data-trim contenteditable>
def setup():
    size(400, 400)
    background(0)
    fill(255)
    ellipse(width / 2, height / 2, 100, 100)
    fill(0, 0, 0)
    ellipse(width / 2 + 20, height / 2 - 20, 100, 100)
</code></pre>

</section>

<section markdown="block">
## Perhaps a Function?

Of course, we can also make our crescent drawing a little more generic by creating a function called <code>drawCrescent</code> 

<pre><code data-trim contenteditable>
def drawCrescent(x, y, offset, size):
    fill(255)
    ellipse(x, y, size, size)
    fill(0, 0, 0)
    ellipse(x + offset, y - offset, size, size)

</code></pre>
{:.fragment}
</section>


<section markdown="block">
## Using the Draw Function

__Let's try using the `draw` function to repeatedly draw some shapes__

Our program will repeatedly draw a square

* in a random location
* with a random color
* and a random size

Let's try putting that code in:

1. `setup`
2. then... in `draw`


</section>

<section markdown="block">
## Random Squares

__Here's what our code may look like__ &rarr;

<pre><code data-trim contenteditable>
import random
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# within setup first, then within draw
    fill(
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(100, 200)
    )
    side = random.randint(5, 75)
    rect(
        random.randint(0, width),  # x
        random.randint(0, height), # y
        side, # width
        side  # height
    )
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Changing Global Variables

__In Python, if you create a local variable with the same name as a global, the local doesn't overwrite / change the value in the global .__ &rarr;

* if we want to actually change this behavior...
* use the keyword `global` followed by the variable name that will be modified
* (all within your function)

<pre><code data-trim contenteditable>
x = 0
def changeX():
    global x
    x += 1
</code></pre>

</section>

<section markdown="block">
## Animated... and Loop Back

__Now try animating it:__ &rarr;

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/crescent-animation.gif)
</div>
</section>


<section markdown="block">
## Some Animation

<pre><code data-trim contenteditable>
moonX, moonY, moonSize = 0, 0, 0

def setup():
    global moonX, moonY, moonSize
    size(400, 400)
    moonX = width / 2
    moonY = height / 2
    moonSize = 100
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
def draw():
    global moonX, moonY, moonSize
    background(0)
    drawCrescent(moonX, moonY, 20, moonSize)
    moonY += 2
    if moonY > height + moonSize / 2: 
        moonY = 0 - moonSize / 2
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## A Minor Change...

__In our drawCrescent method, what if we changed:__ &rarr;

<pre><code data-trim contenteditable>
  fill(0, 0, 0)
</code></pre>

to 

<pre><code data-trim contenteditable>
  fill(0, 0, 0, 180)
</code></pre>

<span class="fragment">The second circle would not be entirely black, as it's partially transparent.</span>
</section>

<section markdown="block">
## Mouse Stuffs

A quick aside on interaction:

* <code>mouseX</code> represents the current x coordinate of the mouse cursor
* <code>mouseY</code> represents the current y coordinate of the mouse cursor
* create a method called <code>mousePressed</code> if you want a method to be called every time the user presses a button
    



</section>
<section markdown="block">
## Try These Mouse Exercises

__Let's do these together.__ &rarr;

1. write a program that makes a lot of crescent moons!
    * allows you to click on the screen 
    * on every click, a moon is drawn in a random location
2. write a program that draws a shape based on the location of the mouse
    * clicking on left side of screen draws rectangles where the cursor is
    * clicking on right side of screen draws ellipses where the cursor is
</section>

<section markdown="block">
## Truchet Tiles

Tiles that are decorated with patterns that are not symmetric when rotated.

[Check out the wikipedia article](http://en.wikipedia.org/wiki/Truchet_tiles)

* the black triangle version... has four distinct possible rotations
* you can create various patterns by mixing rotations
</section>

<section markdown="block">
## A Function to Draw a Tile

__Write a function to draw a Truchet tile:__ &rarr;

* it should have x and y as parameters (where the upper left corner of the tile is)
* it should have a size parameter (the width of the tile)
* it should have a rotation parameter (to determine which permutation of the tile to draw)
* it will draw a single black triangle

Call the function a few times to try it out.
</section>


<section markdown="block">
## Example Truchet Tile Method Calls

(note, the second row is to show the upper corner, there shouldn't be any outlines in the actual method)

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/truchet-method.png)
</div>
</section>

<section markdown="block">
## drawTile

<pre><code data-trim contenteditable>
def drawTile(x, y, size, rotation):
	# you can comment out the fill for just an outline
    fill(0, 0, 0)

    if rotation == 0:
        triangle(x, y + size, x + size, y + size, x + size, y)
    elif rotation == 1:
        triangle(x, y + size, x + size, y + size, x, y)
    elif rotation == 2:
        triangle(x, y + size, x + size, y, x, y)
    elif rotation == 3:
        triangle(x, y, x + size, y + size, x + size, y)
</code></pre>
</section>

<section markdown="block">
## How About Tiling the Tiles

Now... __use your drawTile method to create any of these patterns!__ &rarr;

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/truchet.gif)
</div>
</section>


<section markdown="block">
## A Possible Implementation

<pre><code data-trim contenteditable>
cols, rows, counter = 20, 20, 0;
def setup():
    background(255, 255, 255)
    size(600, 600)
    drawPattern()

def draw():
    pass
</code></pre>
<pre><code data-trim contenteditable>
def drawPattern():
    background(255, 255, 255)
    for y in range(0, height, height / rows):
        for x in range(0, width, width / cols):
            drawTile(x, y, height / rows, counter % 4);
</code></pre>
</section>

<section markdown="block">
## Seeing All Patterns

__Let's modify our code so that we see a different pattern when we click the mouse__ &rarr;

<pre><code data-trim contenteditable>
def mousePressed():
    global counter
    counter += 1
    print('clicked')
    drawPattern()  
</code></pre>
</section>

<section markdown="block">
## And Finally... Random

(again, you don't have to implement click - just make sure to get the random pattern first!)

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/truchet-random.gif)
</div>


</section>

<section markdown="block">
## An Implementation of Random!

<pre><code data-trim contenteditable>
def drawPattern():
    background(255, 255, 255)
    print('calling draw pattern')

    for y in range(0, height, height / rows):
      for x in range(0, width, width / cols):
        drawTile(x, y, height / rows, random.randint(0, 3))
</code></pre>
</section>


<section markdown="block">
## Another Truchet Tile

You can create Truchet tiles with a single line diagonal on a tile. __How many unique rotations would there be for this kind of tyle?__ &rarr;

<span class="fragment">Only 2!</span>

</section>

<section markdown="block">
## A Maze

Modify your previous random Truchet Tiling program to create the following:

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/maze-1.png)
</div>

</section>

<section markdown="block">
## Maybe Another Maze?

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/maze-2.png)
</div>
</section>

<section markdown="block">
## Working With Pixels

You can actually edit each pixel of the window!

(these methods and variables are all part of processing)

1. <code>loadPixels()</code> - begin working with pixels
2. use <code>pixels[] // a list of colors </code>
3. <code>color(r, g, b) // gives back an int representation of a color</code>
4. <code>updatePixels();</code> - update screen with new pixels
</section>

<section markdown="block">
## Um. An List of Pixels?

Wait... how does a single array of pixels represent a two-dimensional window?

* {:.fragment} each row is represented end-to-end in the single array
* {:.fragment} sooo... pixels / height = rows
* {:.fragment} row # = index // width (quotient)
* {:.fragment} col # = index % width (remainder)
* {:.fragment} index = row # * width + col #

</section>

<section markdown="block">
## Um What!?

<pre><code data-trim contenteditable>
"""
[0, 1, 2, 3, ....14, 15]

    0  1  2  3
  +------------
0 | 0  1  2  3
1 | 4  5  6  7
2 | 8  9  10 11
3 | 12 13 14 15

i = row * width + col
2 * 4 + 1 = 9
"""
</code></pre>

</section>

<section markdown="block">
## Lines From Pixels

__Let's try drawing this.__ &rarr;

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/pixels.png)
</div>

</section>
<section markdown="block">
## Lines from Pixels

<pre><code data-trim contenteditable>
def setup():
    size(300, 400)
    
def draw(): 
  loadPixels()
  for row in range(height):
    for col in range(width):
      i = row * width + col
      if row % 10 == 0:
        pixels[i] = color(255, 255, 255)
      else:
        pixels[i] = color(0, 0, 0)
  updatePixels()
</code></pre>

</section>

{% comment %}
<section markdown="block">
## 

<div markdown="block" class="img">
![alt](/csci-ga.1120-fall2017-001/resources/img/black-and-white.png)
</div>
<div markdown="block" class="img">
![alt](../../resources/img/edge.png)
</div>
<div markdown="block" class="img">
![alt](../../resources/img/processing-image.png)
</div>
<div markdown="block" class="img">
![alt](../../resources/img/red.png)
</div>
<div markdown="block" class="img">
![alt](../../resources/img/static-color.gif)
</div>
<div markdown="block" class="img">
![alt](../../resources/img/static-gray.gif)
</div>
<div markdown="block" class="img">
![alt](../../resources/img/truchet-rotate.gif)
</div>
</section>


<section markdown="block">
## 

* create new class file
* import <code>PApplet</code>
* extend you class as usual
* import <code>PImage</code>
* create a global <code>PImage</code> variable
* load in setup by using <code>loadImage</code>


</section>
<section markdown="block">
## 

what is it? /data folder?
eclipse wants to manage all your jamz.

So, just let it. Life will be easier.

But just so you know
1. right click source folder &rarr; new &rarr; other ... choose folder
2. in finder or in explorer, copy image to data folder
3. right click on data folder... refresh
4. build
5. if build doesn't work, clean
If you copy stuff in through the finder, eclipse doesn't "realize" you did so. The data/ folder should be created throught the eclipse "Package Explorer" under the src/ folder. Eclipse will then create bin/data/. 

If you want to add and image you will have to make sure it can be seen in the src folder. Add it through eclipse or refresh the folder. If it still does not appear select project->clean in the menu. This will delete your bin/ directory and recreate it from src/.

</section>

<section markdown="block">
## 
Data structure that represents images

</section>

<section markdown="block">
## 

* window pixels represented as a single array
* __how__ &rarr;
loadPixels
* represents pixels in window
updatePixels
* updates the pixels in window
pixels[]
color

</section>
{% endcomment %}
