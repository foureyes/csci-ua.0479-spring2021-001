---
layout: slides
title: "Matplotlib Extras"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.course_number}}-{{ site.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## MOAR matplotlib!

__Some additional features to enhance our plot__

* specifying colors
* styling
* legend / label
* pie charts
* multiple subplots
* disjoint plots, nan

{% comment %}
* using dictionaries for data
* interactivity
* historgram?
{% endcomment %}

</section>

<section markdown="block">
## Colors

__Specifying colors in matplotlib__

* {:.fragment} color string: `green`, `blue`, `cyan`
* {:.fragment} short color string: `k` (black), `b` (blue), etc.
* {:.fragment} tuple of red green and blue: `(0.5, 0.5, 0.5)` (gray), `(1, 0, 0)` (red)
* {:.fragment} hex code: `#00ff00` (green), `#ffff00` (yellow)

<pre><code data-trim contenteditable>
# using a tuple to create a light blue-green color
plt.plot([0, 2, 4, 9, 16], color=(0.5, 0.75, 1))
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Styles

__matplotlib plots are kind of ugly, tbh__ &rarr;

Fortunately, there are pre-defined styles that you can use simply by calling: 
{:.fragment}

<pre><code data-trim contenteditable>
plt.style.use('name-of-prebuilt-style')
# where name-of-prebuilt-style is one
# of the following...
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## Style Values

__Some possible values for style include:__

<pre><code data-trim contenteditable>
ggplot                  bmh
fivethirtyeight         grayscale
seaborn-dark            seaborn-notebook 
</code></pre>
{:.fragment}

You can also see a listing of available styles:
{:.fragment}

<pre><code data-trim contenteditable>
plt.style.available
</code></pre>
{:.fragment}

Finally, the [docs on style sheets](https://matplotlib.org/users/style_sheets.html) also describe how to create your own styles.
{:.fragment}

</section>

<section markdown="block">
## Style Example

Call `style.use` before using `plot` and `show` &rarr;

<pre><code data-trim contenteditable>
x = np.arange(0, 25)
y = [(n * 4) ** 2 for n in x]
x2 = np.arange(0, 25)
y2 = [n ** 3 for n in x2]

plt.style.use('ggplot')
plt.plot(x, y, 'r-', x2, y2, 'b:')
plt.show()
</code></pre>

</section>

<section markdown="block">
## Legend

To add a __legend__ to your plot:

1. {:.fragment} add a keyword argument, `label`, for each plot
2. {:.fragment} call `plt.legend`

<pre><code data-trim contenteditable>

plt.plot(x, y, 'r-', label='text in legend')
plt.legend() # loc keyword arg for positioning
# upper right, lower right, upper center, etc.
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Legend Example

__The follow plot places a legend in the upper center of the plot__ &rarr;

<pre><code data-trim contenteditable>
x = np.arange(0, 25)
y = np.array([(n * 4) ** 2 for n in x])
x2 = np.arange(0, 25)
y2 = np.array([n ** 3 for n in x2])
</code></pre>

<pre><code data-trim contenteditable>
plt.style.use('seaborn-dark')
plt.plot(x, y, 'r-', label='tears of joy')
plt.plot(x2, y2, 'b:', label='face with no good gesture')
plt.legend(loc="upper center")
plt.show()
</code></pre>


</section>

<section markdown="block">
## Pie Charts

__Create a pie chart using the `pie` function.__

<pre><code data-trim contenteditable>
plt.pie(sizes, explode=None, labels=None, autopct=None)

plt.axis('equal')
</code></pre>

* `sizes` - the sizes of the slices
* `explode` - offset for the slice 
* `labels` - labels for each slice
* `autopct` - format of value in slice
</section>

<section markdown="block">
## Pie Example 

Data ....

<pre><code data-trim contenteditable>
edible_pies = ['Strawberry', 'Apple', 'Chocolate', 'Humble']
numbers = [2, 3, 4, 1]
</code></pre>

Calling `pie`: 
{:.fragment}

<pre><code data-trim contenteditable>
plt.style.use('ggplot')
plt.pie(numbers, labels=edible_pies, 
    autopct='%.2f%%', explode=[0, 0, 0, 0.1])
plt.title('number of pies eaten')
plt.axis('equal')
plt.show()
</code></pre>
{:.fragment}

Want to specify colors?
{:.fragment}

<pre><code data-trim contenteditable>
# using a variety of ways to specify color!
colors=['#ffff00', (1, 0, 0), 'b', 'green']
</code></pre>
{:.fragment}

</section>

<section markdown="block">
##  Pie Example with Dictionary

__Using data from previous dictionary example:__ &rarr;

* {:.fragment} values are sizes (the slices!)
* {:.fragment} keys are the labels

<pre><code data-trim contenteditable>
feels = {'👍': 5, '😒':3, '🍠':12}
plt.style.use('ggplot')
plt.pie(list(feels.values()), 
    labels=list(feels.keys()), 
    autopct='%.2f%%')
plt.axis('equal')
</code></pre>
{:.fragment}
</section>

<section markdown="block">
##  Multiple Subplots

The `subplot()` takes `numrows`, `numcols`, and `plot number`as arguments. The rows and columns split up the current figure into subplots, and the last number specifies which subplot to "switch" to.

<pre><code data-trim contenteditable>
y1 = np.arange(0, 10);
y2 = np.arange(15, 5, -1)
plt.style.use('ggplot')

# switch to subplot 1 in subplot with 2 rows
plt.subplot(2, 1, 1)
plt.plot(y1, 'bo')

# switch to subplot 2 in subplot with 2 rows
plt.subplot(2, 1, 2)
plt.plot(y2, 'k')
plt.show()
</code></pre>

</section>

<section markdown="block">
## More Subplots!

A 2 x 2 grid of charts and graphs &rarr;

<pre><code data-trim contenteditable>
y1 = np.arange(0, 10);
y2 = np.arange(15, 5, -1)
plt.style.use('ggplot')

plt.subplot(2, 2, 1)
plt.plot(y1, 'bo')

plt.subplot(2, 2, 2)
plt.plot(y2, 'k')

plt.subplot(2, 2, 3)
plt.bar([0, 1, 2], [5, 2, 7])

plt.subplot(2, 2, 4)
plt.pie([70, 10, 30], explode=[0, 1, 0])
plt.axis('equal')

plt.show()
</code></pre>
</section>

<section markdown="block">
## Disjoint Plots

You can use the special type, `numpy.nan` to represent a value __that will not be plotted__:


<pre><code data-trim contenteditable>
y = [3, 2, 2, 2, 2, np.nan, np.nan, 2, 2, 2, 1]
plt.style.use('seaborn-dark')
plt.plot(y, 'b-')
plt.show()
</code></pre>
{:.fragment}

__Note that the middle of the graph is missing.__
{:.fragment}
</section>
