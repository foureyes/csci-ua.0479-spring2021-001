---
layout: slides
title: "NumPy Arrays!"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

</section>

<section markdown="block">
## Creating Arrays

__`numpy` provides a multidimensional container for homogeneous (same type and size in memory) types: `ndarray` (n-dimenional array__ 

You can create an array by &rarr;

* {:.fragment} `array` called with a sequence (like a `list`, `tuple`, etc.)
* {:.fragment} `ones`, `zeros` called with an integer or tuple of ints (dimensions )
* {:.fragment} `arange` called with a start, stop and step
* {:.fragment} `random.randn` called with arbitrary number of args as dimensions

</section>

<section markdown="block">
## Creating Arrays Examples

<pre><code data-trim contenteditable>
# both of these sequences results equivalent arrays
np.array([[1, 1], [2, 2]])
np.array(((1, 1), (2, 2)))
# array([[1, 1],
#        [2, 2]])
</code></pre>

<pre><code data-trim contenteditable>
np.zeros((2, 5)) # array([[0., 0., 0., 0., 0.],
                          [0., 0., 0., 0., 0.]])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
np.arange(4, 12, 2) # array([ 4,  6,  8, 10])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
np.random.randn(2, 3)
# array([[-0.41478999, -0.87304136, -0.23290474],
#       [ 0.30277282,  0.44985592,  1.06013982]])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Describing an Array

__The following properties can be used to get some information about _your shiny, new array_...__ &rarr;

* {:.fragment} `ndim` - number of dimensions
* {:.fragment} `shape` - a tuple containing the size of each dimension
	* {:.fragment} think of this like nested lists... 
	* {:.fragment} 1st element is outermost dimension 
	* {:.fragment} last element is the innermost: `[[77], [88]]` &rarr; `(2, 1)`
	* {:.fragment} (can also be assigned a value to reshape)
* {:.fragment} `dtype` - the data type of the array 
	* (inferred from values, or set explicitly via keyword arg, `dtype="type name")
	* {:.fragment} ex: `int64` (signed 64-bit int), `float64` (a "double"), `unicode_`, etc.
	* {:.fragment} can convert type with `astype`
</section>

{% comment %}
end_
{% endcomment %}

<section markdown="block">
## Describing an Array Examples

__Given the following array, what will the `ndim`, `shape` and `dtype` properties be?__ &rarr;

<pre><code data-trim contenteditable>
arr = np.array([[[1, 1], [2, 2], [3, 3]],
                [[4, 4], [5, 5], [6, 6]],
                [[7, 7], [8, 8], [9, 9]]])
</code></pre>

* {:.fragment} `arr.ndim` &rarr; `3`
* {:.fragment} `arr.shape` &rarr; `(3, 3, 2)`
* {:.fragment} `arr.dtype` &rarr; `dtype('int64')`
</section>

<section markdown="block">
## Shape Again

__Remember, shape 🔺🔵■ gives us the size of each dimension as a tuple, starting from the outermost dimension__ 

What is the resulting `.shape` `tuple` for the following; describe what the `tuple` represents in _natural language_ 🤷 &rarr;

* {:.fragment} `np.array([1, 2, 3])` 
	* {:.fragment} `(3,)` - 3 columns
* {:.fragment} `np.array([[1, 2, 3], [1, 2, 3]])`
	* {:.fragment} `(2, 3)` - 2 rows, 3 columns
* {:.fragment} ...lastly
	```
np.array([
	[[1, 2], [3, 4],  [5, 6]], 
	[[7, 8], [9, 10], [11, 12]]
])
```
	* {:.fragment} `(2, 3, 2)` - 2 "tables", each with 3 rows, and 2 columns

</section>

<section markdown="block">
## Axis

__You'll often see the term <span class="hl">axis</span>, followed by a number, to address a specific dimension__ &rarr;

* {:.fragment} __axis 0__, __axis 1__, etc.
* {:.fragment} this describes the position of the dimension as given by `.shape`
* {:.fragment} for example, `[[1, 2, 3], [4, 5, 6]]`
	* {:.fragment} `.shape` is `(2, 3)`, so....
	* {:.fragment} __axis 0__, rows, is 2
	* {:.fragment} __axis 1__, columns,  is 3

In higher dimensions, row and column is not going to be 0 and 1 (likely last 2, instead!)
{:.fragment}

In lower dimension, only columns, so __axis 0__ is columns, not rows! 😮
{:.fragment}
</section>

<section markdown="block">
## 2D-4-ME 📈

Yeah, so with that said.... __We'll be working with tabular data, so we'll be sticking to <span class="hl">2 dimensions</span> mostly.__ 

__When might higher dimensional data be needed, though (lets think through some scenarios)?__ &rarr;
{:.fragment}

* {:.fragment} keeping track of <span class="hl">historical tabular data</span> (for example, people responding to the same survey questions over time)
* {:.fragment} <span class="hl">image data as separate channels</span> (a grid of red, grid for green, blue ...)
* {:.fragment} ...and of course, <span class="hl">video</span> (several images over time)
* {:.fragment} dealing with a <span class="hl">large feature set for machine learning </span>
</section>

<section markdown="block">
## About That Reshaping

__You can change the dimensions and shape of an array by:__ &rarr;

* {:.fragment} assigning a tuple to the `shape` property
	* {:.fragment} changes `ndarray` in place
* {:.fragment} ...or calling `reshape`
	* {:.fragment} accepts tuple as argument 
	* {:.fragment} returns new `ndarray` with specified shape

<pre><code data-trim contenteditable>
a = np.arange(9)
a.reshape((3, 3))
# gives back:
# array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# (but a stays the same)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
a.shape = (3, 3)
# changes a itself!
</code></pre>
{:.fragment}

</section>
<section markdown="block">

## Array Arithmetic 

__Arithmetic operations behave differently based on the type of the _other_ operand. For example.__

If the other operand is a scalar (_single value types_ like `int`, `float`, `boolean`, `string`, etc.), then the operation is performed on every element using the same scalar as the second operand (<span class="hl">vectorization</span>):

<pre><code data-trim contenteditable>
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr * 10)
</code></pre>

<pre><code data-trim contenteditable>
[[10 20 30]
 [40 50 60]]
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Broadcasting

Multiplying an `ndarray` with a scalar is the most simple case of <span class="hl">broadcasting</span>.

* {:.fragment} __Broadcasting__ is a _fancy_ term for __how `numpy` deals with arrays with different shapes.__
* {:.fragment} only works when the arrays being used are _compatible_ (more on that later)
* {:.fragment} provides a mechanism for <span class="hl">vectorizing</span> array operations by...
* {:.fragment} _stretching_ out dimensions / shapes to make two arrays the same shape
	* {:.fragment} <span class="hl">no loops</span> have to be written to <span class="hl">apply operations to every array element</span> 👍
	* {:.fragment} looping occurs in C instead of Python ⏩
	* {:.fragment} no extra copies 👯 of data have to made to do this
</section>

<section markdown="block">
## Simple Broadcasting

__Same `shape` or w/ scalar.__ What are the resulting arrays? &rarr;

<pre><code data-trim contenteditable>
# same shape: perform operation on elements in same positions
np.ones((2, 3)) + np.array([[1, 2, 3], [4, 5, 6]])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
array([[2., 3., 4.],
       [5., 6., 7.]])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# stretch scalar value out over all dimensions needed to
# to create array of same dimensions ([[5, 5, 5], [5, 5, 5]])
np.ones((2, 3)) * 5
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
array([[5., 5., 5.],
       [5., 5., 5.]])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Not So Simple Broadcasting

That was easy.😎 __...but what about different shapes? 😅__ &rarr;

__Broadcasting can only be performed if the dimensions, starting from the end, either__ &rarr;

* {:.fragment} equal
* {:.fragment} or... one of them is 1

<span class="hl">If different dimensions, left pad with 1, and follow rules above</span>
{:.fragment}

__Can the following shapes be made compatible?__ &rarr;
{:.fragment}

* {:.fragment} `(2, 3, 2)`, `(2, 1, 2)`<span class="fragment">✅</span>
* {:.fragment} `(2, 2, 3)` and `(3, 2)` <span class="fragment">🙅</span>
* {:.fragment} `(3,)` and `(4, 3)` <span class="fragment">✅</span> 

</section>
<section markdown="block">
## Compatible ❤️, Now What?

__If two Arrays are compatible, how do we make the `shape` of both arrays match__? &rarr;

* {:.fragment} left pad with 1 to make equal `ndim`
* {:.fragment} stretch out dimensions with size 1 by repeating elements

<pre><code data-trim contenteditable>
a1 = np.ones((3, 3)); a2 = np.array([1, 2, 3])
</code></pre>
{:.fragment}

* {:.fragment} change shape of `a2` from `(3, )` to `(1, 3)`: `[[1, 2, 3]]`
* {:.fragment} repeat along new axis / dimension until size matches (repeat 3 times)
	* {:.fragment} `[[1, 2, 3], [1, 2, 3], [1, 2, 3]]`
* {:.fragment} `a1 + a2` &rarr; `[[2, 3, 4], [2, 3, 4], [2, 3, 4]]`
</section>

<section markdown="block">
## And Another One 🔑

__What are the `shape` properties of `a1` and `a2`? How is `a2` stretched?__

<pre><code data-trim contenteditable>
a1 = np.ones((2, 3, 2)) 
a2 = np.array([[[8, 9]], [[88, 99]]])
a1 + a2 # ????
</code></pre>

<pre><code data-trim contenteditable>
a1.shape # 2, 3, 2
a2.shape # 2, 1, 2
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# stretching a2 along axis 1
np.array([[[8, 9],     [8, 9],   [8, 9]],
          [[88, 99], [88, 99], [88, 99]]])
</code></pre>
{:.fragment}

</section>
<section markdown="block">
## Some More Examples

__Want some more practice...?__ &rarr;

<pre><code data-trim contenteditable>
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr + arr
</code></pre>

<pre><code data-trim contenteditable>
array([[ 2,  4,  6],
       [ 8, 10, 12]])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
arr + np.array([1, 2, 3])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
array([[2, 4, 6],
       [5, 7, 9]])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Now for Some Indexing 👆

Works like you'd expect (again, think of nested lists):

<pre><code data-trim contenteditable>
a =  np.array([[10, 11, 12], [13, 14, 15]])
</code></pre>

Get the first element of `a`:

<pre><code data-trim contenteditable>
a[0] # array([10, 11, 12])
</code></pre>
{:.fragment}

Now get the last item of the first sub array of `a` 
{:.fragment}

<pre><code data-trim contenteditable>
a[0][2] # 12 (also a[0][-1]
</code></pre>
{:.fragment}

Alternatively, use tuple `a[0, 2]` or `a[(0, 2)]`:
{:.fragment}

</section>

<section markdown="block">
## Reduced Dimensions

__Note that when you index with a value containing less dimensions, you get an array with less dimensions consisting of only the data in the higher dimensions__ &rarr;

<pre><code data-trim contenteditable>
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
</code></pre>

* {:.fragment} `a[1]`<span class="fragment"> - only axis 0 is given, so resulting array is data from axis 1 and 2 `array([[5, 6], [7, 8]])`</span>
* {:.fragment} `a[1, 0]`<span class="fragment"> - both axis 0 and 1 are given, so resulting array is data from axis 2 only  `array([5, 6])` </span>

(we already _sort of do this intuitively_)
{:.fragment}

</section>

<section markdown="block">
## Assignment 

__We can use indexing to perform assignment, as with regular lists... but with some magic!__✨  &rarr;
<pre><code data-trim contenteditable>
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
</code></pre>


* {:.fragment} `a[0][0][0] = 135` - 🆗 
* {:.fragment} `a[0][0] = 135` <span class="fragment"></span>
	* {:.fragment} `[[[135, 135], [3, 4]], [[4, 6], [5, 8]]]`
	* {:.fragment} both elements in `a[0][0]` set to 135
	* {:.fragment} (repeat `135` along axis 2 at `a[0][0]`)
* {:.fragment} `a[0][0] = [99, 135]` - 🆗 `[[[ 99, 135], [3, 4]], ...]`
* {:.fragment} `a[0] = [987, 987]`
	* {:.fragment}  `[[[987, 987], [987, 987]], [[ 4, 6], ...]`
	* {:.fragment}  (repeat `[987, 987]` along axis 1 at `a[0]`)

</section>

<section markdown="block">
## Views 👀

__Again, _kind of_ like working with lists... indexing into an array gives you a <span class="hl">view</span> into the array, not a new sub array__ &rarr;

* {:.fragment} consequently, you're not getting a copy back if you index
* {:.fragment} so if you perform assignment on the value that you get back after indexing, it <span class="hl">changes the original array</span>

<pre><code data-trim contenteditable>
a = np.ones((2, 3))
last_row = a[-1]
last_row[-1] = 456
#...what does a look like???
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# a is now... array([[  1.,   1.,   1.],
#                    [  1.,   1., 456.]])
</code></pre>
{:.fragment}
</section>
<section markdown="block">
## Slicing 🔪

__Same, but different... _as usual_.__ This should be familiar... `np.ones(5)[:2]` &rarr; <span class="hl">`[1., 1.]`</span>

* {:.fragment} slices grab a range of elements along an axis
* {:.fragment} ...but the _crazy_ 🙃 part is that you can have multiple slices in a single expression
<pre><code data-trim contenteditable>
a = np.arange(36).reshape((4, 3, 3))
a[1:3,:2,1:]
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
array([[[10, 11], [13, 14]],
       [[19, 20], [22, 23]]])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## For Reference

__Here's a view of our array, `a`__ &rarr;

<pre><code data-trim contenteditable>
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]],

       [[27, 28, 29],
        [30, 31, 32],
        [33, 34, 35]]])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## And `:`

__What are the rules for slicing syntax again?__ &rarr;

* {:.fragment} leave out value before colon `:m`
	* {:.fragment} <span class="hl">start at beginning</span> (`0`)
* {:.fragment} leave out value after colon `n:`
	* {:.fragment} <span class="hl">end at end</span> 
* {:.fragment} leave out both `:`
	* {:.fragment} <span class="hl">beginning to end</span> 

</section>
<section markdown="block">
## How'd We Slice That?

__Let's take a look at the slice in more detail.__

<pre><code data-trim contenteditable>
a = np.arange(36).reshape((4, 3, 3))
a[1:3,:2,1:]
</code></pre>
{:.fragment}

* {:.fragment} first...we can think of axis 0 as "table/panel", axis 1 as row and axis 2 as col
* {:.fragment} so this says, only give me <span class="hl">tables 1 and 2</span>
* {:.fragment} and from those tables, I want the <span class="hl">first 2 rows, and the last 2 columns</span>

<pre><code data-trim contenteditable>
array([[[10, 11],
        [13, 14]],

       [[19, 20],
        [22, 23]]])
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Slice and Assign

__Based on what we've seen before, what will happen here?__ &rarr;

<pre><code data-trim contenteditable>
a = np.arange(36).reshape((4, 3, 3))
a[1:3,:2,1:] = 0
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
array([[[ 0,  1,  2],...

       [[ 9,  0,  0],
        [12,  0,  0],
        [15, 16, 17]],

       [[18,  0,  0],
        [21,  0,  0],
        [24, 25, 26]], ...]])
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## Slicing Also a View

🔪🔭 ... __ok, so here's where `numpy` `ndarray` differs from `list` and other sequence types.__

* unlike sequences, `ndarray` slices give a view (rather than a new `array`)
* so assignment changes the original array!

</section>

<section markdown="block">
## Slicing / Indexing Practice

__Give me multiple ways to retrieve the X's form the following `3, 3` arrays__ &rarr;

<pre><code data-trim contenteditable>
 1. X X _    2. _ _ X     3. _ _ _     4. _ _ _
    X X _       _ _ X        X X X        _ X X
    _ _ _       _ _ X        X X X        _ _ _
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
a[:2, :2] # 1
a[:, 2:]  # 2
a[1:, :]  # 3
a[1, 1:]  # 4
</code></pre>
{:.fragment}

(there are multiple ways to do each, and dimensions of the returned array may differ)
{:.fragment}
</section>

<section markdown="block">
## Boolean Selections

__You can use a boolean list / array as an index as well!__

* {:.fragment} for the axis that it's used as an index on, it will include, positionally, everything that's `True`, and exclude `False`
* {:.fragment} given `a = np.arange(15).reshape(5, 3)`...
* {:.fragment} and `rows = [False, True, False, True, False]`
* {:.fragment} using `rows` as the index for axis 0, only the rows in positions where there is a `True` value will be included

<pre><code data-trim contenteditable>
a[rows]
array([[ 3,  4,  5],
       [ 9, 10, 11]])
</code></pre>
{:.fragment}

<span class="hl">The number of elements in the boolean list / array must be the same as the size of the axis you're indexing</span>
{:.fragment}
</section>

<section markdown="block">
## Mix 🌀 and Match 🔷🔷

__Given this monstrosity 🙈 (what's it look like?)__ ... &rarr;

<pre><code data-trim contenteditable>
a = np.arange(24).reshape((3, 4, 2))
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
array([[[ 0,  1],
        [ 2,  3],
        [ 4,  5],
        [ 6,  7]],

       [[ 8,  9],
        [10, 11],
        [12, 13],
        [14, 15]],

       [[16, 17],
        [18, 19],
        [20, 21],
        [22, 23]]])
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## Slicing and Boolean Selection 

__Using the previous slide and at least one boolean list to index, give back ...__ &rarr;

* {:.fragment} the first two tables, 
* {:.fragment} the 2nd and last row of both of those tables
* {:.fragment} the last element of each row

<pre><code data-trim contenteditable>
a[:2, [False, True, False, True], 1:]
a[:2, [False, True, False, True], -1] # (less dims)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Fancier 💃

__Not only can you use booleans, you can also use a list of integers as an index__ &rarr;

* {:.fragment} the integers specify which elements to include
* {:.fragment} and their order specifies the order to include the elements n
* {:.fragment} passing in multiple lists allows you to essentially pick and choose specific elements!

For example, given a single column, `a` as `[[0], [1], [2], [3]]` ... to select just the last row twice, then the first row:
{:.fragment}

<pre><code data-trim contenteditable>
a[[-1, -1, 0]]
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## 💃[[0, 0], [1, 1]]

__Try these examples of fancy indexing...__ &rarr;

<pre><code data-trim contenteditable>
a = np.arange(9).reshape(3, 3) # [[0, 1, 2],
                               #  [3, 4, 5],
                               #  [6, 7, 8]]

</code></pre>

<pre><code data-trim contenteditable>
# what do we get with these indexes????
a[[2, 1]]
a[[0, 1, 2], [2, 1, 0]]
</code></pre>
{:.fragment}


<pre><code data-trim contenteditable>
array([[6, 7, 8],
       [3, 4, 5]])

array([2, 4, 6])
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Transpose / Matrix Operations

__Turn columns into rows or find the dot product__ &rarr;


<pre><code data-trim contenteditable>
a = np.arange(12).reshape((3, 4))
a.T # rows into columns (transpose)
</code></pre>
{:.fragment}


<pre><code data-trim contenteditable>
m1 = np.arange(6).reshape(2, 3)
m2 = np.arange(6, 12).reshape(3, 2)
m1.dot(m2) # matrix dot product
# (sum or products of elements of rows from m1
# ...and columns of m2)
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## Functions on Array Elements

__`numpy` comes with built-in functions that work on every element in an `array` ... some examples include:__ &rarr;

* {:.fragment} unary functions 
	* {:.fragment} `sqrt` and `square`
	* {:.fragment} `floor` and `ceil`
	* {:.fragment} `sum` and `mean` \*
	* {:.fragment} etc.
* {:.fragment} binary functions
	* {:.fragment} `add`
	* {:.fragment} `floor_divide`
	* {:.fragment} etc.

Check out the table in the book for others...
{:.fragment}

Note that <span class="hl">these are all functions called from the `numpy` module</span> ... and they either take on or two arguments.
</section>


<section markdown="block">
## `sum`, `mean`, `std`

__These functions are a little different from the other functions in the previous slides__ &rarr;

* {:.fragment} these functions can be called on instance of `array` as well as`numpy`
* {:.fragment} they'll give back a single value
* {:.fragment} OR... they can take an `axis` keyword argument specifying which column to aggregate on


<pre><code data-trim contenteditable>
a = np.arange(9).reshape(3, 3)
a.mean()
a.mean(axis=0)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
4.0
array([3., 4., 5.])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Ternary With `where`

__Remember the ternary / one-line if-else?__ &rarr;

<pre><code data-trim contenteditable>
val1 if cond else val2
# in other languages cond ? val1 : val2
</code></pre>
{:.fragment}

<span class="hl">The `numpy` equivalent of a ternary operator is a function called `where`</span>
{:.fragment}

* {:.fragment} argument 1 is `condition`
* {:.fragment} argument 2 is value to return if `condition` is `True`
* {:.fragment} argument 3 is value to return if `condition` is `False`

__It gives back a new array with the values specified above.__
{:.fragment}

</section>

<section markdown="block">
## Where⁉️

__What do you think this will give back__ &rarr;

<pre><code data-trim contenteditable>
a = np.arange(9).reshape(3, 3)
np.where(a < 5, 'YAS', 'OH NO')
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
array([['YAS', 'YAS', 'YAS'],
       ['YAS', 'YAS', 'OH NO'],
       ['OH NO', 'OH NO', 'OH NO']], dtype='<U5')
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## Miscellaneous Methods and Functions

__Methods on boolean arrays__ 
{:.fragment}

* {:.fragment} `any` - `True` if any element is `True`
* {:.fragment} `all` - `True` if all elements are `True`

__Sorting (method),  Unique (function) and Membership (function__
{:.fragment}

* {:.fragment} `sort` - sort (along an optional axis) 📶
* {:.fragment} `unique` - `numpy` function that gives back unique elements in array as an array 
* {:.fragment} `in1d` - `numpy` function that gives back booleans based on whether or not values in first array exist in values in second array

</section>


