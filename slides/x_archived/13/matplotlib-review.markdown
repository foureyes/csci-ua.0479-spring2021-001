---
layout: slides
title: "Matplotlib Review"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Review

__Matplotlib Basics__ &rarr;

* installation
* background
* plot
* bar
* xticks, xlabel, title

</section>


<section markdown="block">
## Installation

__Recommended installation__ &rarr;

* {:.fragment} use `pip` (`easy_install pip`) to manage Python packages
* {:.fragment} create a `virtualenv` to bundle and isolate bundled packages (`easy_install virtualenv virtualenvwrapper`)
* {:.fragment} install matplotlib with `pip` in `virtualenv`

__uh... or just use PyCharm's package installation ui__ &rarr;
{:.fragment}

[(See the screencast in the help section)](/help.html)
{:.fragment}


</section>

<section markdown="block">
## Matplotlib

__matplotlib__ is a Python package / module for __creating data visualizations__. It can be used for...  &rarr;

* {:.fragment} creating charts and graphs
* {:.fragment} animations
* {:.fragment} interactivity

It has two main modes
{:.fragment}

* {:.fragment} `scripting` mode - similar to giving commands to turtle
* {:.fragment} `object oriented` - build figures using objects
* {:.fragment} scripting mode is easier to start off with, object oriented mode is more powerful / flexible

</section>

<section markdown="block">
## Matplotlib Vocabulary

Jargon makes matplotlib a little intimidating, [but this visual aid helps explain commonly used terms](https://matplotlib.org/tutorials/introductory/usage.html#parts-of-a-figurea). Additionally, here are some definitions: &rarr;

* {:.fragment} __Canvas__ - the object that _actually_ draws everything to screen (you won't usually be working on this directly)
* {:.fragment} __Figure__ - you can think of this as your entire visualization / diagram, including the axes, its title, etc.
* {:.fragment} __Axes__ - basically your plotted data; there can be more than one Axes object in a figure (so you can a figure with multiple bar charts on it, for example)
* {:.fragment} __Axis__ - the lines in your graph that specify the graph boundaries / limits, its tick marks, etc.
</section>


<section markdown="block">
## Basic Boilerplate Code 

Using scripting mode (__pyplot__) all you have to do is:

1. {:.fragment} `import` matplotlib
2. {:.fragment} plot _something_
3. {:.fragment} then show it...

<pre><code data-trim contenteditable>
import matplotlib.pyplot as plt

# your code goes here

plt.show()
</code></pre>

</section>

<section markdown="block">
## plot

`plot` plots points or a line. __It's flexible in terms of arguments passed in__, but a common way of calling it is `plt.plot(x, y, format)`:

* {:.fragment} `x` and `y` - list or numpy array 
* {:.fragment} `format` - a string representing the color and line/marker style

`plot` can also be called with more or less arguments: 
{:.fragment}

* {:.fragment} with 2 arguments, first y values (x is generated automatically), and second format
* {:.fragment} more than 3 arguments, multiple plots
* {:.fragment} with keyword arguments, like `color='#ff0000'`



</section>

<section markdown="block">
## lim, ticks, label, titles

You can use the following functions __to format and style the entire figure__:

* `xticks`, `yticks` - the values shown and associated with the x and y ticks
* `xlim`, `ylim` - the boundaries of the figure, the length of the x and y axis
* `xlabel`, `ylabel` - the label for the x and y axis
* `title` - set the title of the figure

</section>

<section markdown="block">
## An Entire Example

Setup...

<pre><code data-trim contenteditable>
import matplotlib.pyplot as plt
import numpy as np
</code></pre>

Some data...

<pre><code data-trim contenteditable>
x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 9, 16]
x2 = [0, 1, 2, 3, 4]
y2 = [4, 5, 6, 7, 8]
</code></pre>

</section>

<section markdown="block">
## plot Example Continued

Plot a dashed red line and a solid blue line

<pre><code data-trim contenteditable>
plt.plot(x, y, 'r--', x2, y2, 'b-')
</code></pre>

Formatting...

<pre><code data-trim contenteditable>
plt.xticks([0, 2, 4], ['small', 'medium', 'large'])
plt.yticks([0, 16], ['not much', 'a lot'])

plt.xlabel('pizza size')
plt.ylabel('amount of toppings')

plt.xlim(-1, 5)
plt.ylim(0, 20)
</code></pre>

Finally, display the figure...

<pre><code data-trim contenteditable>
plt.show()
</code></pre>
</section>

<section markdown="block">
## bar

[Documentation for the bar function](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html)... and a quick summary of its arguments `plt.bar(x, h, w, align='center')`: &rarr;

1. {:.fragment} the x coordinates of the left sides of the bars
2. {:.fragment} the heights of the bars
3. {:.fragment} the widths of the bars
4. {:.fragment} the keyword argument, `align` will allow you to align the bars to the  right (`edge`) or center
</section>


<section markdown="block">
## Bar Chart Example 

__An example of a bar chart with labels:__ &rarr;

Start off with some data...

<pre><code data-trim contenteditable>
# labels
feels = ('👍', '😒', '🍠')

# y values
num_votes = [5, 3, 12]

# the x values (based on number of labels)
x = np.arange(len(feels))

</code></pre>
{:.fragment}

</section>


<section markdown="block">
## Bar Chart Example Continued

Using data from previous slide...

<pre><code data-trim contenteditable>
plt.bar(x, num_votes, align='center', color='#aaddff')
plt.xticks(x, feels)
plt.ylim(0, 14)
plt.ylabel('Votes')
plt.xlabel('Feels')
plt.title('How U Feel Abt This Graph?')
plt.show()
</code></pre>

</section>

<section markdown="block">
## Using a Dictionary

__If your data were in a dictionary... here's how the previous program may look__ &rarr;

<pre><code data-trim contenteditable>
feels = {'👍': 5, '😒':3, '🍠':12}
plt.bar(np.arange(len(feels)), list(feels.values()), align='center', color='#aaddff')
plt.xticks(np.arange(len(feels)), list(feels.keys()))

plt.ylim(0, 14)
plt.ylabel('Votes')
plt.xlabel('Feels')
plt.title('How U Feel Abt This Graph?')
plt.show()
</code></pre>
</section>
