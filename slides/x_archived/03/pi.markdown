---
layout: slides
title: "Approximating Pi (math module, Control Structures)"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## draw_poly

Heeeyyyy. So remember our draw_poly function?

* we could pass it any number of sides
* and it would draw a polygon with (you guessed it) that number of sides

__What happens when we draw a polygon with a _large_ number of sides? What shape does it start to look like?__ &rarr;

A circle!
{:.fragment}

</section>

<section markdown="block">
## Approximating Pi

It turns out that we can use a closed polygon to approximate the value of pi. (This is the first part of our book's 2nd chapter... on Archimedes method for approximating pi).

* consider that C = 2&pi;r
* we can get pi by ... &pi; = C / 2r or &pi; = C / 2 (if unit circle, or circle with radius 1)
* our polygon is almost a circle
* ...soooo &pi; = perimeter / 2
* __but how do we get the perimeter?__ &rarr;
* {:.fragment} we have to figure out the length of a side

</section>

<section markdown="block">
## Circle

![cirlce](../../resources/img/circle.png)

* a = 360 / number of sides.
* we can get half of the length of side, s, by taking the sin of half of the angle, a.
* check out chapter 2 in {{ site.book1 }}

</section>


<section markdown="block">
## Our Plan of Attack!

To find the perimeter of the polygon...

1. create right triangle
2. use half interior angle to get half length of side
3. interior angle is 360 / num sides
4. use math module
    * <code>math.sin(a)</code> (a is angle in radians)
    * <code>math.radians(a)</code> convert degrees a to radians

__Let's see a sample program...__ &rarr;
</section>


<section markdown="block">
## Using Archimedes Method

<pre><code data-trim contenteditable>
import math
num_sides = int(input('how many sides?'))
inner_angle = 360 / num_sides

# half of inner angle (so that we have a right triangle)
half_angle = inner_angle / 2

# ... we'll have half the length of side (sin A = opposite / hypotenuse)
half_s = math.sin(math.radians(half_angle))

# actual side length and perimeter
s = 2 * half_s
perimeter = num_sides * s

# pi = C / 2
pi = perimeter / 2
print(pi)
</code></pre>

</section>

<section markdown="block">
## Homework #01 / Approximating Pi Again

__In section 2.6 of the book, there's...__ &rarr;

* a __monte carlo__ simulation is introduced to approximate pi
* as well as a few parts dedicated to __conditionals__
    * (if you're already familiar with Python's if statements, it's safe to skip those parts)

__Part 3 of the first homework is meant to be a simple way to practice some basic control structures:__

1. for loops
2. if statements

</section>
<section markdown="block">
## Monte Carlo simulation

A __Monte Carlo simulation__ is a method of using random numbers to solve mathematical problems

* _usually_, an analytical method of solving the problem may not exist or may be too time consuming / complex / etc.
* these methods weren't so practical until the development of computers __why__? &rarr;
* {:.fragment} roulette wheels and dice aren't that efficient at generating random numbers, but computers are
* {:.fragment} __we can use a monte carlo approximation to approximate pi...__
* {:.fragment} (btw, where did it get its name from?)
* {:.fragment} Monte Carlo... a city famous for games of chance (read: gambling)
</section>

<section markdown="block">
## Plotting with turtle

__The book uses turtle to create a monte carlo simulation.__. It introduces a few turtle and screen methods that allow us to plot points on a 2D plane:

* __<code>wn.setworldcoordinates(llx, lly, urx, ury)</code>__ 
    * (lower left x and y, upper right x and y)
    * sets coordinate system (regardless of actual width and height of window)
* __<code>t.dot(size)</code>__  
    * plots a point
    * (pen can be up, it's ok!)
* __<code>wn.exitonclick()</code>__ 
    * use instead of mainloop to keep window open
    * clicking on window closes it
</section>

<section markdown="block">
## Homework #01, Approximating Pi

Sooo... in homework #01, there's a partial implementation of the Monte Carlo simulation presented in the book. 

* read through chapter 2 (specifically 2.6)
* finish the implementation 
* you'll just need to add ...
    * a repetition structure
    * and a conditional
</section>

