---
layout: slides
title: "Graphing with Matplotlib"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Data Visualization with matplotlib

`matplotlib` is Python module for creating data visualizations, such as charts, graphs and even interactive / animated diagrams!

1. It's a large library with a lot of functionality, so __we'll focus on creating some simple line graphs and bar charts__.
2. We'll cover the following:
    * {:.fragment} overview / background
    * {:.fragment} example plots for line graphs, bar charts and histograms
    * {:.fragment} simple formatting
</section>


<section markdown="block">
## What Can we Do With It?

__Um, ok... so excel has me covered for charts and graphs. What can we do with matplotlib???__ &rarr;

A lot. Check out the [gallery page](https://matplotlib.org/gallery/index.html) in the documentation. We can make...
{:.fragment}

1. {:.fragment} [simple scatter plots, bar graphs, and the usual](https://matplotlib.org/gallery/style_sheets/ggplot.html#sphx-glr-gallery-style-sheets-ggplot-py)
2. {:.fragment} [or some sophisticated visualizations, like a pie chart on a polar axis](https://matplotlib.org/gallery/pie_and_polar_charts/polar_bar.html#sphx-glr-gallery-pie-and-polar-charts-polar-bar-py)
3. {:.fragment} [and we can even add some interaction (check out the hover states)](https://matplotlib.org/gallery/event_handling/trifinder_event_demo.html#sphx-glr-gallery-event-handling-trifinder-event-demo-py)
4. {:.fragment} [...and some animation too!](https://matplotlib.org/gallery/animation/unchained.html#sphx-glr-gallery-animation-unchained-py)

We'll just be concerned with the basics for now, like plotting lines and creating histograms...
{:.fragment}



</section>


<section markdown="block">
## Background

__matplotlib is HUGE__. There are a lot of parts to it, and it provides a _a lot_ of functionality through exposing classes and functions. This functionality can be broken down into three areas:

1. {:.fragment} the __backend__, which is responsible for _actually_ displaying a figure on the screen or rendering it to to a _hardcopy_ / file, such as an image (png), document (pdf), or other format
2. {:.fragment} the __artist layer__ is responsible for providing all the tools necessary for plotting and drawing - creating figures, axes, ticks, primitive shapes (lines, polygons), etc.
3. {:.fragment} the __scripting layer__ which provides simple commands for quickly plotting graphs; the commands are similar to the commands that you would find in MATLAB


</section>


<section markdown="block">
## Rendering

__We'll be working with the scripting layer__; it's a quick way to get started with `matplotlib`

However, it's nice to see __how everything comes together to render a plot...__ &rarr;

1. the __scripting layer__ is essentially used to load data
2. the data is then transformed into various objects representing graphical elements in the __artist layer__
3. these objects are then rendered by the __backend__ - to a canvas on the screen, to a pdf, etc.

</section>

<section markdown="block">
## pyplot vs Object Oriented

You'll find that some tutorials go through manipulating graphical elements directly in the __artist layer__. Sometimes this is called the __Object-Oriented Interface__.

When going through tutorials for `matplotlib` you'll find that they will usually use:
{:.fragment}

1. {:.fragment} a bunch of functions from `matplotlib.pylot` (the scripting layer) 
2. {:.fragment} or classes directly from `matplotlib` (the artistic layer... or the object oriented interface)

</section>

<section markdown="block">
## Some Terms

I ❤️ definitions: &rarr;

These are actually the names of classes that exist in `matplotlib`...
{:.fragment}

* {:.fragment} __Canvas__ - the object that _actually_ draws everything to screen (you won't usually be working on this directly)
* {:.fragment} __Figure__ - you can think of this as your entire visualization / diagram, including the axes, its title, etc.
* {:.fragment} __Axes__ - basically your plotted data; there can be more than one Axes object in a figure (so you can a figure with multiple bar charts on it, for example)
* {:.fragment} __Axis__ - the lines in your graph that specify the graph boundaries / limits, its tick marks, etc.


[We can see how all of these are related in this diagram](https://matplotlib.org/tutorials/introductory/usage.html#parts-of-a-figure)
{:.fragment}
</section>

<section markdown="block">
## The Scripting Interface / Layer

Again, there are a few different ways to work with `matplotlib`. We'll work with the __scripting layer__. To work with the scripting layer: &rarr;

1. start off by `import matplotlib.pyplot as plt` 
2. this gives you a bunch of functions that can be called off of `pyplot` (`plt` in our import above)
3. each `pyplot` function creates or modifies a figure (adding text to tick marks, creating an entirely new figure, plotting some points, etc.)
4. these functions are similar to functions that you can find in MATLAB, a programming language that specializes in numerical computing

</section>


<section markdown="block">
## Basic pyplot functions 


__The following two functions will be enough to create some simple charts and graphs:__ &rarr;

These are all called on `pyplot` (or `plt` if you imported it as `plt`)...

1. `plot`: plots points / lines on current figure's axes
2. `show`: draw and display plot

__And for some basic formatting...__ &rarr;

* `xlabel`: adds a label to the x-axis
* `ylabel`: adds a label to the y-axis
* `title`: the title of the current figure's axes
* `title`: the title of the current figure's axes
* `title`: the title of the current figure's axes
</section>

<section markdown="block">
## plot

The `plot` function will plot lines and/or markers to the axes. __There are many different ways to use it__, and consequently, the number and types of the arguments are important in __determining how it will function__. From the docs: &rarr;

<pre><code data-trim contenteditable>
plot(x, y)        # plot x and y with default style
plot(x, y, 'bo')  # plot using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+')     # same, but with red +'s
</code></pre>
{:.fragment}


Note that the `x` and `y` arguments are _like_ lists of values; in reality, they're converted to a special type, `numpy` `arrays`, which we'll take a quick detour on later...
{:.fragment}

</section>

<section markdown="block">
## plot With One Argument

__If you call plot with a single list, it will treat those points as y values, and x will be automatically created as a sequence from 0 to the number of elements in list - 1__

<pre><code data-trim contenteditable>
from matplotlib import pyplot as plt
import numpy as np
plt.plot([1, 2, 3, 4, 5]) # treated as y values
# x's will be 0, 1, 2, 3, 4
plt.show()
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## plot With Two Arguments 

With two arguments, __the first argument will be the x values and the second argument will be the y values__

<pre><code data-trim contenteditable>
from matplotlib import pyplot as plt
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [0, 0, 5, 5, 10, 10, 5, 5, 0, 0])
plt.show()
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## plotting With Three Arguments 

With three arguments, the first argument will be the x values and the second argument will be the y values ... __the third argument is a format string that specifies the style and color of the plot__ &rarr;

<pre><code data-trim contenteditable>
from matplotlib import pyplot as plt
plt.plot([0, 2, 2, 3, 5, 8, 9, 10], 'r--')
plt.show()
</code></pre>
{:.fragment}

In the example above, `r--` means a red dashed line. __Um... where are these specified?__
{:.fragment}


</section>

<section markdown="block">
## The Format String

The format string is composed of a __style and / or a color__, where the style and color are:

<pre><code data-trim contenteditable>
'-'  solid line style  '--'  dashed line style
':'  dotted line style '.'  point marker
'o'  circle marker     'v'  triangle_down marker
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
'b'  blue     'c'  cyan       'k'  black
'g'  green    'm'  magenta    'w'  white
'r'  red      'y'  yellow
</code></pre>
{:.fragment}

You can find these string specified [in the documentation](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib-axes-axes-plot)
{:.fragment}
</section>

<section markdown="block">
## A Note on Multiple Plots

__Your axes can have multiple plots!__ &rarr;

* this means that you can call `.plot` multiple times before showing the graph... 
* and all of your plots will appear in the axes in your figure

For example:

<pre><code data-trim contenteditable>
plt.plot([0, 2, 2, 3, 5, 8, 9, 10])
plt.plot([0, 4, 5, 5, 4, 5, 7, 9])
plt.show()

</code></pre>

</section>
<section markdown="block">
## Multiple Plots Continued

__You can also have multiple lots by using a single call to `plot` by adding more arguments!__

<pre><code data-trim contenteditable>
plt.plot([0, 2, 2, 3, 5, 8, 9, 10], 
        'r-', 
        [0, 4, 5, 5, 4, 5, 7, 9],
        'b:')
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Format Examples

__Now let's combine multiple calls to plot, each formatted__ &rarr;

<pre><code data-trim contenteditable>
# dashed green
plt.plot([0, 2, 2, 3, 5, 8, 9, 10], 'g--')
# dotted black
plt.plot([0, 4, 5, 5, 2, 5, 7, 9], ':k')
# solid red
plt.plot([0, 1, 2, 3, 4, 5, 6, 7], 'r-')
</code></pre>
{:.fragment}

Note that order of style and color doesn't matter
{:.fragment}
</section>

<section markdown="block">
## Keyword Arguments

__In addition to the format string, you can use keyword arguments to control plot style and color)__ &rarr;

Again, check out [the docs](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib-axes-axes-plot) for the properties, but some examples include...

* `color='#ff0000'` - color as a hex string (red)
* `linestyle='dotted'` - linestyle is dashed
* `marker='o'` - marker is a circle

<pre><code data-trim contenteditable>
plt.plot([0, 4, 5, 5, 2, 5, 7, 9], 
        color='#ff0000',
        linestyle='dotted',
        marker='o')
</code></pre>

</section>


<section markdown="block">
## Aside on Numpy Arrays

Oh yeah... about `numpy`. __It's a library for working with vectors and matrixes__:

* `matplotlib` makes heavy use of a type defined in `numpy`: `array`
* an `array` is a lot like a list, but it's much faster... and its operations are a bit different
    *
* try this out to get an idea of `numpy` and arrays can do:

<pre><code data-trim contenteditable>
arr = array([5, 7, 9])  # convert a list to an array
print(arr)
arr = np.arange(10, 20) # 10 up through and including 19
print(arr)
print(arr[0])           # index
print(arr + 100)        # add
print(arr > 15)         # compare (you can an array back!)
# new array of elements where index expression is true!?
print(arr[arr > 15])     
</code></pre>

</section>


<section markdown="block">
## Some Other Ways to Create numpy Arrays

__Besides using an `array` constructor and `arange`, you can also use these functions to create arrays__ &rarr;

<pre><code data-trim contenteditable>
np.zeros(5)          # 5 0's
np.zeros(3, 3)       # 3 x 3 matrix of 0's
# 6 values evenly distributed between 0 and 1
np.linspace(0, 1, 6) 
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# 100 random nums btwn 0 and 1 
# (uniform distribution)
np.random.rand(100)  

# 100 random nums btwn 0 and 1 
# (normal / gaussian distribution)
np.random.randn(100) </code></pre>
{:.fragment}
</section>

<section markdown="block">
## numpy with matplotlib

Here's a quick example of using `numpy` arrays and `matplotlib`:

<pre><code data-trim contenteditable>
import numpy as np
x = np.random.rand(10)
plt.plot(x, 'g--')
plt.show()
</code></pre>
{:.fragment}

__Note that when lists are passed in as arguments, they're really just being converted to numpy arrays!__
{:.fragment}
</section>

<section markdown="block">
## Titles and Labels

In addition to simple plots, we can __set the x and y labels and the title of a plot__ &rarr;

Using `title`, `xlabel`, and `ylabel`...

<pre><code data-trim contenteditable>
import numpy as np
x = np.arange(1, 10)
y = x ** 2
plt.plot(x, y, 'k--')
plt.title('I am a stress eater')
plt.ylabel('No. of desserts')
plt.xlabel('Amt. of stress')
plt.show()

</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Boundaries / Limits

__What's difficult to see about this graph?__ &rarr;

<pre><code data-trim contenteditable>
plt.plot([1, 2, 3, 4, 5, 5, 5], 
        [3, 4, 4, 2, 1, 2, 3])
plt.show()
</code></pre>

* {:.fragment} It's tough to see the parts of the graph that are at the boundaries of the figure.
* {:.fragment} The boundaries are dynamically determined by min and max values, so...
    * {:.fragment} 5 is the boundary on the right
    * {:.fragment} 4 is the boundary on the left


</section>

<section markdown="block">
## Setting the Limits on Axes

__Rather than let the limits on the axes be set for us, we can set them explicitly using the following functions:__ &rarr;

* {:.fragment} `xlim(min, max)`
* {:.fragment} `xlim(min, max)`

Here's how you might use it:
{:.fragment}

<pre><code data-trim contenteditable>
plt.plot([1, 2, 3, 4, 5, 5, 5], 
        [3, 4, 4, 2, 1, 2, 3])
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Ticks!

😮... Not the bug, but the labels on the ticks of the axes. __You can use the following functions to set the ticks as well as their actual labels__ &rarr;

* {:.fragment} functions for setting ticks:
    * {:.fragment} `xticks` - [set ticks on x axis](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xticks.html)
    * {:.fragment} `yticks` - [set ticks on the y axis](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.yticks.html)
* {:.fragment} usage...
    * {:.fragment} Call these with __one argument, a sequence, to set the ticks to those values__.
    * {:.fragment} Call these with __two arguments to include labels for ticks__.

</section>

<section markdown="block">
## Ticks Examples

Here's an example where the __x-axis ticks are set to increments of 25__, and the __y-axis ticks are given the labels smol and extra__ &rarr;

<pre><code data-trim contenteditable>
import numpy as np
x = np.arange(1, 101)
y = x ** 3
plt.plot(x, y, 'k-')
plt.xticks([0, 25, 50, 75, 100])
plt.yticks([0, 1000000], ['smol', 'extra'])
plt.show()
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Bar Charts

To __create a bar chart, use the `.bar`__ function...

Here's [the documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html)... the arguments are &rarr;

1. {:.fragment} the x coordinates of the left sides of the bars
2. {:.fragment} the heights of the bars
3. {:.fragment} the widths of the bars
4. {:.fragment} the keyword argument, `align` will allow you to align the bars to the  right (`edge`) or center
</section>


<section markdown="block">
## Bar Chart Example 

__An example of a bar chart with labels:__ &rarr;

<pre><code data-trim contenteditable>
import numpy as np

# our data
# ====

# some animals
animals = ('Snake', 'Human','Octopus')

# their arms (the y values)
num_arms = [0, 2, 8]

# the x values (0, 1, or 2)
x = np.arange(len(animals))
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# plotting
# =====
plt.bar(x, num_arms, align='right')
plt.xticks(x, animals)
plt.ylim(0, 10)
plt.ylabel('Arms')
plt.xlabel('Animal')
plt.title('Number of Arms')
plt.show()
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## Pride and Prejudice

__Let's try to create a bar chart of the top 10 proper nouns in pride and prejudice!__ &rarr;

</section>







