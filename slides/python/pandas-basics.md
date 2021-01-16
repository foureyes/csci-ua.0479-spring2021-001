---
layout: slides
title: "Pandas Basics"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

</section>

<section markdown="block">
## numpy + ┬──┬ =🐼 

__Um... sort of. <span class="fragment"><span class="hl">pandas</span> is... &rarr;</span>__
{:.fragment} 

<span class="hl">pandas</span> a python module that has data structures and tools for working with data
{:.fragment} 

You'll find a lot of _numpy-like_ functionality in it: 
{:.fragment} 

* {:.fragment} especially for array based computing and functions 
* {:.fragment} and, of course, a style that __favors vectorized array operations over for loops__

However, unlike numpy, <span class="hl">pandas specializes in dealing with tabular data composed of mixed data types</span>
{:.fragment} 

</section>


<section markdown="block">
## Some Types!

__pandas offers a few types for manipulation of tabular data:__ &rarr;

* {:.fragment} __Series__ 
	* {:.fragment} one-dimensional, labeled, array
* {:.fragment} __DataFrame__
	* {:.fragment} two-dimensional data structure (think of a table with columns and rows)
* {:.fragment} Bonus Type! __Index__
	* {:.fragment} the type that holds the labels for a `Series` and `DataFrame`

Let's check out a `Series` first!
{:.fragment}

</section>

<section markdown="block">
## Series

__You can think of a `Series` as: &rarr;__

* {:.fragment} a numpy `ndarray` with labels for each value
* {:.fragment} ... or a `dict` with ordered key/value pairs and potentially duplicate keys
* {:.fragment} ... but officially (from the docs):
	* {:.fragment} a one-dimensional labeled array 
	* {:.fragment} where the associated labels are collectively referred to as the <span class="hl">index</span>
</section>

<section markdown="block">
## `index` and `value` 

__A `Series` has two properties that show the labels and data it holds__ &rarr;

* {:.fragment} `values` - the _actual_ data in the `Series`
* {:.fragment} `index` - the labels for the data in `Series`

</section>

<section markdown="block">
## Creating a Series

__There are several ways to create a `Series`, each resulting in different labels for the index__ &rarr;

1. {:.fragment} using a single positional argument, `data` (an `ndarray` or sequence type like `list`), to specify `values` in `Series`
2. {:.fragment} two positional (`data` and `index`) arguments with the second specifying the `index` labels
3. {:.fragment} passing keyword arguments for `data` and `index`
4. {:.fragment} passing in a `dict` with dictionary keys as `labels` and values as `values`
	* {:.fragment} (can also be called with a specific `index` value)

Remember, the <span class="hl">index</span> provides a label for each element in a `Series`.
{:.fragment}
</section>

<section markdown="block">
## Implicit Index

__Without and `index` specified, the labels are simply 0 to length of `values` - 1. Check the examples__  &rarr;

<pre><code data-trim contenteditable>
# an ndarray
pd.Series(np.array([7, 8, 9]))
0    7
1    8
2    9
dtype: int64
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# a list
pd.Series(['ant', 'bat', 'cat'])
0    ant
1    bat
2    cat
dtype: object
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## That Looks Like `numpy`! But!

Hey... this _actually_ looks just like an `ndarray`. __Note the `dtype` property!__

However, you'll see that there are a couple of major differences:
{:.fragment}

1. {:.fragment} the obvious difference is that it has `index` labels (that can be repeated)
2. {:.fragment} additionally, it supports different types in its `values`:
	 <pre class="fragment"><code data-trim contenteditable>
pd.Series(['ant', 'bat', 123])
0    ant
1    bat
2    123
dtype: object
</code></pre>
</section>

<section markdown="block">
## Specifying Labels 🏷 

So, um... if `index` labels are just _gonna_ be 0 through length, then that's just the same as an `ndarray`, right? __Let's specify labels by adding a second positional argument__ &rarr;

<pre><code data-trim contenteditable>
pd.Series(['Hoboken', 'Ithaca'], ['NJ', 'NY'])
NJ    Hoboken
NY     Ithaca
</code></pre>
{:.fragment}

Oh yes. Duplicate. Labels. R. Allowed. 👯
{:.fragment}

<pre><code data-trim contenteditable>
pd.Series(['Syracuse', 'Hoboken', 'Ithaca'], 
    ['NY', 'NJ', 'NY']) # (line continuation)
NY    Syracuse
NJ     Hoboken
NY      Ithaca
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## With 🔑 Arguments

__You can also pass these arguments in as keyword arguments `data` and `index` (for labels)__ &rarr;


<pre><code data-trim contenteditable>
pd.Series(data=[7, 8])
0    7
1    8
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
pd.Series(data=[7, 8], index=['A', 'B'])
A    7
B    8
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
pd.Series([7, 8, 9], index=['A', 'B', 'C'])
A    7
B    8
C    9
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## `len(data) == len(index)`

__The lengths of the `data` and `index` passed in must be the same.__

If these lengths are different, you'll get a `ValueError`: 
{:.fragment}

<pre><code data-trim contenteditable>
pd.Series([7, 8, 9], index=['A', 'B'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>ValueError: Length of passed values is 3, index implies 2
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Creating `Series` with `dict` 📖

__Earlier, we described a `Series` as a dictionary that allows duplicate labels.__ 

In fact you can pass a `dict` in to a `Series` constructor:
{:.fragment}

<pre><code data-trim contenteditable>
pd.Series({'B': 'bat', 'A': 'ant'})
B    bat
A    ant
</code></pre>
{:.fragment}

* {:.fragment} `dict` keys become labels
* {:.fragment} `dict` values are the values in the `Series`

</section>

<section markdown="block">
## `dict` with `index`

<pre><code data-trim contenteditable>
pd.Series({'A': 'ant', 'B': 'bat'}, ['A', 'B']) # OK
A    ant
B    bat
</code></pre>
{:.fragment}

If a key from `data` doesn't match an element in `index`, <span class="hl">it's value is not included.</span>
{:.fragment}

<pre><code data-trim contenteditable>
pd.Series({'A': 'ant', 'B': 'bat'}, ['A'])
A    ant
</code></pre>
{:.fragment}

If an `index` label does not have a corresponding key in `data`, <span class="hl">then missing `data` values will be `NaN`</span>
{:.fragment}

<pre><code data-trim contenteditable>
pd.Series({'A': 'ant', 'B': 'bat'}, ['A', 'C'])
A    ant
C    NaN
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## `NaN` Means Missing Data

__In pandas, `NaN` implies that a value is missing or "N/A"__ &rarr;

The `pandas` functions / instance methods, `isnull` and `notnull` can be used to check for missing values:

<pre><code data-trim contenteditable>
s = pd.Series({'x': 100}, ['x', 'y'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
pd.isnull(s) # or s.isnull()
x    False
y     True
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
pd.notnull(s) # or s.notnull()
x     True
y    False
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## `index` and `value` Revisited

__The `index` and `values` properties of a `Series` object can be used to retrieve the labels and data from a `Series`__

(note that this is slightly confusing as the keyword arg is called `data`, while the property is called `values`)
{:.fragment}

<pre><code data-trim contenteditable>
 s = pd.Series([7, 8, 9], ['x', 'y', 'z'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
s.values
array([7, 8, 9])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
s.index
Index(['x', 'y', 'z'], dtype='object')
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## Indexing

__Indexing a `Series` is similar to indexing a 1-dimensional `ndarray`__

<pre><code data-trim contenteditable>
s = pd.Series([7, 8, 9, 10], list('xyxz'))
s['y'] # 8 ... (as expected)
</code></pre>
{:.fragment}

Using a `list` to specify multiple labels:
{:.fragment}

<pre><code data-trim contenteditable>
s[['y', 'z']] #  Series! y     8
              #          z    10
</code></pre>
{:.fragment}

Repeating a label repeats value:
{:.fragment}

<pre><code data-trim contenteditable>
s[['y', 'y', 'z']] #  Series  y     8
                   #          y     8
                   #          z    10
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Duplicate Labels 🔖👯

__If a label specified maps to more than one value, give back all values__ &rarr;

<pre><code data-trim contenteditable>
s = pd.Series([7, 8, 9, 10], list('xyxz'))
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
s['x'] #  Series! x     7
       #          x     9
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Indexing by Position

__Just like a `numpy` `ndarray`, you can still use position for indexing__ &rarr;

<pre><code data-trim contenteditable>
s = pd.Series([2, 3, 4, 5], list('abcd'))
</code></pre>

Both of the following... &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
s['a']
s[0]
</code></pre>
{:.fragment}

...gives us `2`
{:.fragment}

</section>

<section markdown="block">
## Slicing with Labels

__Although indexing by labels and position is similar, there's a pretty big gotcha when slicing ⚠️__ &rarr;

* {:.fragment} slicing by position works as expected
* {:.fragment} slicing with labels is inclusive at the end

<pre><code data-trim contenteditable>
s = pd.Series([2, 3, 4, 5, 6], list('abcde'))
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
s[1:3]
b    3
c    4  #👌
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
s['b':'d']
b    3
c    4
d    5 # WAT!?😮
</code></pre>
{:.fragment}

</section>



<section markdown="block">
## Vectorized Arithmetic

Yup ✅ ... works as you'd expect:

<pre><code data-trim contenteditable>
s = pd.Series([1, 2], ['x', 'y'])
</code></pre>
{:.fragment}


<pre><code data-trim contenteditable>
s - 2
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
x   -1
y    0
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Label Alignment

__If the other operand is a `Series`, operations will be done based on label alignment__ &rarr;

* {:.fragment} values for matching labels will be operated on
* {:.fragment} non-matching labels result in `NaN` (in pandas, this means NA or missing)
* {:.fragment} the union of labels will be the result of the operation

__Let's start off with a straightforward one; what's the result of this operation?__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
s = pd.Series([1, 2], ['x', 'y'])
s + pd.Series([9, 8], ['x', 'y']) # let's add!
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
x    10
y    10
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Tricky Label Alignment

__Now for something a little tricker. What is the result of this operation?__ &rarr;

<pre><code data-trim contenteditable>
s = pd.Series([1, 2], ['x', 'y'])
s + pd.Series([9, 100], ['x', 'z']) # tricky!
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
x    10.0
y     NaN
z     NaN
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Alignment Summary

__`Series` operations align by label rather than position:  &rarr;__

* {:.fragment} if index pairs aren't the same (present in one, missing from the other), then <span class="hl">resulting `index`</span> will be both labels!
* {:.fragment} missing values are inserted where labels to not match 

<pre><code data-trim contenteditable>
s1 = pd.Series([1, 2], ['x', 'y'])
s2 = pd.Series([9, 100], ['x', 'z'])

s1 + s2
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
x    10.0
y     NaN
z     NaN
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Comparison Operations

__Comparison operators work similarly to arithmetic operators, except, of course, they return boolean values... what are the results of the following comparisons?__ &rarr;

<pre><code data-trim contenteditable>
s = pd.Series([1, 2], ['x', 'y'])
</code></pre>

<pre><code data-trim contenteditable>
s == 1
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
x     True # such vectorized!
y    False
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
s  == pd.Series([1, 2], ['x', 'y'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
x    True # compared by value
y    True
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Nothing Compares 2 U 

__One big difference ⚠️ though... if the labels don't align, you get an exception (`ValueError`)!__

<pre><code data-trim contenteditable>
s = pd.Series([1, 2], ['x', 'y'])
</code></pre>

<pre><code data-trim contenteditable>
# try this...
s  == pd.Series([1, 99], ['x', 'z'])

# or this...
s  == pd.Series([1], ['x'])
</code></pre>

<pre><code data-trim contenteditable>
ValueError: Can only compare identically-labeled Series objects
</code></pre>
</section>


<section markdown="block">
## Filtering with Booleans 

__Just like a `numpy` `ndarray`, you can filter a `Series` with a list of booleans:__ &rarr;

<pre><code data-trim contenteditable>
s = pd.Series([2, 3, 4, 5]) #  0    2
                            #  1    3
                            #  2    4
                            #  3    5
</code></pre>
{:.fragment}

What does the following expression give us? &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
s[[True, False, True, False]]	
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
0    2   # keeps 1st and 3rd (index 0 and 2)
2    4   # discards 2nd and 4th (index 1 and 3)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Using Results of Comparison to Filter

__A common pattern is to use a `Series` of booleans returned from a comparison to filter out values:__ 

What is the result of the following? &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
s = pd.Series([5, 6, 7, 8], index=['A', 'B', 'C', 'D'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
s[s % 2 == 1]
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
A    5   # only odds, s % 2 == 1 
C    7   # gives us booleans [T, F, T, F]
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## DataFrames 🖼  

__You can think of a <span class="hl">DataFrame</span> as:__ &rarr;

* {:.fragment} a rectangular table of data
* {:.fragment} or an ordered collection of columns
	* {:.fragment} (where perhaps each column is a `Series`!)
	* {:.fragment} (think a `dict` of `Series` objects!)

</section>
<section markdown="block">
## `index` and `columns`

__In a `DataFrame`, both rows and columns have an `index`. The nomenclature is:__

* {:.fragment} `index` - for row labels
* {:.fragment} `columns` - for column labels
* {:.fragment} `data` - again, the actual values is called `data`

`data`, `index` and `columns` can be specified when creating a new `DataFrame`
{:.fragment}
</section>

<section markdown="block">
## Creating DataFrames

__Like `Series`, there are multiple ways to create `DataFrames`__ &rarr;

* {:.fragment} positional arguments
	* {:.fragment} with an`ndarray` or other sequence types
	* {:.fragment} with a `dict` of `dict` objects
* {:.fragment} using keyword arguments
* {:.fragment} mixing positional and keyword arguments

Each method allows different ways to specify `data`, `index` and `columns`
{:.fragment}

</section>

<section markdown="block">
## Implicit `index` and `columns`

__Without the second or third arguments specified, `index` and `columns` are generated as 0 to length of rows or cols - 1__

<pre><code data-trim contenteditable>
# only data (index and columns generated)
pd.DataFrame([[1, 2, 3], [4, 5, 6]])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   0  1  2
0  1  2  3
1  4  5  6
</code></pre>
{:.fragment}


<pre><code data-trim contenteditable>
# only data and index (columns generated)
pd.DataFrame([[1, 2, 3], [4, 5, 6]], ['r1', 'r2'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    0  1  2
r1  1  2  3
r2  4  5  6
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Creating DataFrames Continued

__Of course, with all three, you can explictly set `data`, `index`, and `columns`__ &rarr;

<pre><code data-trim contenteditable>
pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9 ], # data
    ['r1', 'r2', 'r3'],                # index
    ['A', 'B', 'C'])                   # columns
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    A  B  C
r1  1  2  3
r2  4  5  6
r3  7  8  9
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Nested Dictionaries

__A nested `dict` can be used to explicitly define row labels and column names as well__ &rarr;

* {:.fragment} <span class="hl">outer</span> keys are <span class="hl">column</span> names
* {:.fragment} <span class="hl">inner</span> keys are <span class="hl">row</span> names

<pre><code data-trim contenteditable>
d = pd.DataFrame({
    "colA": {'r1': 6, 'r2': 7},
    "colB": {'r1': 8, 'r2': 9}
})
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    colA  colB
r1     6     8
r2     7     9
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Keyword Arguments

__Like `Series`, you can mix and match with keyword arguments:__ &rarr;

In the following code, notice that:
{:.fragment}

* {:.fragment} `data` is passed in as a positional argument,
* {:.fragment} `index` is left out (to be generated automatically)
* {:.fragment} `columns` is defined as a keyword argument

<pre><code data-trim contenteditable>
pd.DataFrame([[1, 2, 3], [4, 5, 6]], 
    columns=['A', 'B', 'C'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   A  B  C
0  1  2  3
1  4  5  6
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## `values` `index` `columns`

__The data, row labels and columns can all be retrieved by accessing attributes / properties on a `DataFrame` instance__ &rarr;

* {:.fragment} `values` - the data for the table
* {:.fragment} `index` - the row labels
* {:.fragment} `columns` - the column names
* {:.fragment} there's also `dtype`...
	* since a `DataFrame` and `Series` can hold different types...
	*`dtype` will be set to the `type` that can accommodate all the values in the `DataFrame`

</section>

<section markdown="block">
## Retrieving Columns

__Columns can be retrieved by:__

* {:.fragment} indexing with a <span class="hl">single column name</span> 
	* {:.fragment} (which may return a `Series` or `DataFrame`)
* {:.fragment} indexing with a <span class="hl">list</span> of column names to return a `DataFrame`

__Using the following `DataFrame`, let's check out some indexing possibilities__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    columns=['foo', 'bar', 'baz'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   foo  bar  baz
0    4    5    6
1    7    8    9
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Retrieving one Column

__With a single column name, a column is returned as a `Series`__ &rarr; 

<pre><code data-trim contenteditable>
df['foo']
0    4
1    7
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# note that the type and name of the column are usually
# given too:
Name: foo, dtype: int64
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
type(df['foo']) # we get a series back
pandas.core.series.Series
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
df['foo'].name # note the name attribute!
Out[107]: 'foo'
</code></pre>
{:.fragment}



</section>


<section markdown="block">
## Retrieving Multiple Columns pt 1!

__If a label in the `index` occurs more than once, then a `DataFrame` of multiple columns is returned rather than a single `Series`__ &rarr;


<pre><code data-trim contenteditable>
d = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    columns=['a', 'b', 'a'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
d['a']
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   a  a
0  4  6
1  7  9
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Retrieving Multiple Columns pt 2!

__When indexing with a list of column names (even if there's only one name in the list), a `DataFrame` is returned with only the columns matching the names in the list included in the returned `DataFrame`__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
df[['foo', 'bar']]
   foo  bar
0    4    5
1    7    8
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
type(df[['foo', 'bar']])
pandas.core.frame.DataFrame
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
type(df[['foo']])  # list w/ 1 element
pandas.core.frame.DataFrame # (still!)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Rearrange / Repeat

__Indexing can also be used to to retrieve a new `DataFrame` with reordered columns and/or repeated columns__ &rarr;

<pre><code data-trim contenteditable>
pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    columns=['foo', 'bar', 'baz'])
</code></pre>
{:.fragment}

__What `DataFrame` will we get back from:__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
df[['bar', 'bar', 'foo']]
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   bar  bar  foo  # bar is repeated
0    5    5    4  # and placed before
1    8    8    7  # foo
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## If Key Doesn't Exist...

__Regardless of whether or not a list or a single column is used for indexing into a `DataFrame`, a `KeyError` is raised if a key doesn't exist__ &rarr;


<pre><code data-trim contenteditable>
df = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    columns=['foo', 'bar', 'baz'])
</code></pre>

<pre><code data-trim contenteditable>
d['dne']             
df[['foo', 'dne']] # both of these are 🚫
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
KeyError: "['dne'] not in index"
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## `DataFrame` Slices Gives Rows!

__If a `DataFrame` is sliced BY POSITION, it yields rows rather than columns__ &rarr;

<pre><code data-trim contenteditable>
d = pd.DataFrame({"cA": {'r1': 1, 'r2': 2, 'r3': 3},
                  "cB": {'r1': 4, 'r2': 5, 'r3': 6},
                  "cC": {'r1': 7, 'r2': 8, 'r3': 9}})
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
d[:2] # slicing refers to rows here! 
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    cA  cB  cC  # only first two rows!
r1   1   4   7
r2   2   5   8
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Indexing with List of Booleans / Arrays

__Much like `Series` and `ndarray`, we can use a list or array of booleans to select parts of a `DataFrame`__

* {:.fragment} a list/array of booleans filters `DataFrame` rows
* {:.fragment} the length of the booleans must match the number of rows

<pre><code data-trim contenteditable>
d = pd.DataFrame({"cA": {'r1': 1, 'r2': 2, 'r3': 3},
                  "cB": {'r1': 4, 'r2': 5, 'r3': 6},
                  "cC": {'r1': 7, 'r2': 8, 'r3': 9}})
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
d[[False, True, True]] 
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    cA  cB  cC # gimme last two rows!
r2   2   5   8
r3   3   6   9
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Constructing Boolean Selection 

__Again, we don't have to manually create a Boolean `array`; it can be the result of a vectorized boolean comparison__ &rarr;

Let's take this example...
<pre><code data-trim contenteditable>
d = pd.DataFrame({"cA": {'r1': 1, 'r2': 2, 'r3': 3},
                  "cB": {'r1': 4, 'r2': 5, 'r3': 6},
                  "cC": {'r1': 7, 'r2': 8, 'r3': 9}})
</code></pre>

</section>

<section markdown="block">
## Boolean Selection Continued

__Retrieve the rows where column `cA` is more than 1__ 
<pre><code data-trim contenteditable>
# d is       cA  cB  cC
#        r1   1   4   7
#        r2   2   5   8
#        r3   3   6   9
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
d['cA'] > 1  # r1    False
             # r2     True
             # r3     True
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
d[d['cA'] > 1] # 😘
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    cA  cB  cC
r2   2   5   8
r3   3   6   9
</code></pre>
{:.fragment}

</section>




<section markdown="block">
## Setting Values

__Now that we know how to retrieve values with indexing... let's see how we can set values with `Series`__ &rarr;

<pre><code data-trim contenteditable>
s = pd.Series([2, 3, 4, 5, 6], list('abcde'))
</code></pre>

<pre><code data-trim contenteditable>
s['a'] = 100     # assigning with an index
s['b':'d'] = 200 # assigning with a slice
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
a    100
b    200
c    200
d    200
e      6
</code></pre>
{:.fragment}

</section>
<section markdown="block">
## Setting Values, `DataFrame`

Using our usual example:... 
{:.fragment}

<pre><code data-trim contenteditable>
 df = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
     columns=['foo', 'bar', 'baz'])
</code></pre>
{:.fragment}

<span class="hl">Assigning to a scalar sets all values of a column:</span>
{:.fragment}

<pre><code data-trim contenteditable>
df['foo'] = 77
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   foo  bar  baz
0   77    5    6
1   77    8    9
</code></pre>
{:.fragment}




</section>

<section markdown="block">
## Assignment Continued

__Of course, you can set each value in a column to a specific value using a `list` or even a `Series`__ &rarr;

<pre><code data-trim contenteditable>
df['foo'] = [99, 100]
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   foo  bar  baz
0   99    5    6
1  100    8    9
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
df['foo'] = pd.Series([-8, -9])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   foo  bar  baz
0   -8    5    6
1   -9    8    9
</code></pre>
{:.fragment}

</section>
<section markdown="block">
## About That `Series`

__As you might expect, if you assign a `Series` to a `DataFrame` column:__ &rarr;

* {:.fragment} the labels will be aligned to perform assignment
* {:.fragment} with... `DataFrame` labels missing from the `Series` filled with `NaN` 
* {:.fragment} and extra labels in the `Series` (not matching any of the `DataFrame`’s labels) ignored


</section>

<section markdown="block">
## More `DataFrame` / `Series` Assignment

__Pay attention to the mismatched labels...__ &rarr;

<pre><code data-trim contenteditable>
df = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    index=['r1', 'r2'],
    columns=['foo', 'bar', 'baz'])
#     foo  bar  baz
# r1    4    5    6
# r2    7    8    9
</code></pre>

<pre><code data-trim contenteditable>
df['foo'] = pd.Series([100, 200], ['r1', 'r3'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
      foo  bar  baz
r1  100.0    5    6    
r2    NaN    8    9   # r2 is added as NaN
                      # r3 ignored
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Assignment Errors

__When assigning a `list`/`ndarray` or `Series` to a column, the length of the data must match the length of the `DataFrame` column.__ &rarr;
<pre><code data-trim contenteditable>
df['foo'] = [100]
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
ValueError: Length of values does not match length of index
</code></pre>
{:.fragment}


</section>
<section markdown="block">
## Assignment + Boolean Selection

__Note that indexing with an `array`, `Series` or `list` of booleans can be used in assignment as well__ &rarr;

<pre><code data-trim contenteditable>
d = pd.DataFrame({"cA": {'r1': 1, 'r2': 2, 'r3': 3},
                  "cB": {'r1': 4, 'r2': 5, 'r3': 6},
                  "cC": {'r1': 7, 'r2': 8, 'r3': 9}})
d[d['cA'] > 1] = 0
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    cA  cB  cC
r1   1   4   7
r2   0   0   0
r3   0   0   0
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Adding Columns

__If the column name used in assignment does not exist, a new column will be created__ &rarr;

<pre><code data-trim contenteditable>
df = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    columns=['foo', 'bar', 'baz'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
df['qux'] = [20, 30]  # qux is new!
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   foo  bar  baz  qux
0    4    5    6   20
1    7    8    9   30
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Removing Columns: a Mystery ⁉️

__The `.drop` method on a `DataFrame` can be used remove a column. Let's try it:__ &rarr;

<pre><code data-trim contenteditable>
df = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    columns=['foo', 'bar', 'baz'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
df.drop('baz') #  🤔
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
KeyError: "['baz'] not found in axis"
# 😮 what happened!?
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Axis Flashback 

__Remember `numpy`... specifically the significance of `.shape` and axis?__ &rarr;

* {:.fragment} `.shape` describes the length of the dimensions of an `ndarray`
* {:.fragment} a two-dimensional `ndarray` has a `.shape` that's a two-element tuple
* {:.fragment} what does the first element of that tuple represent? and the second?
	* {:.fragment} the first, <span class="hl">axis 0</span>, represents <span class="hl">rows</span>
	* {:.fragment} the second, <span class="hl">axis 1</span>, represents <span class="hl">columns</span>

</section>

<section markdown="block">
## Really Removing Columns 

__`.drop` takes `axis` as a keyword argument__ &rarr;

* {:.fragment} buuuut... it's default value is 0 (rows! 😮)
* {:.fragment} to remove a column, use `axis=1`

<pre><code data-trim contenteditable>
df = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    columns=['foo', 'bar', 'baz'])

df.drop('baz', axis=1)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   foo  bar  # baz column
0    4    5  # was removed!
1    7    8
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Dictionary Life (`del`)

__Similar to deleting keys/values in dictionaries, the `del` keyword cal also be used to drop columns__ &rarr;

<pre><code data-trim contenteditable>
df = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
    columns=['foo', 'bar', 'baz'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
del df['baz']
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
   foo  bar  # again, baz
0    4    5  # is removed!
1    7    8
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Ok, How About Rows?

__Indexing into rows can be done by indexing into the `loc` attribute / property of a `DataFrame` object.__ &rarr;

* {:.fragment} again, a `Series` is returned
* {:.fragment} the labels are the `column` names, though!

<pre><code data-trim contenteditable>
df = pd.DataFrame([[4, 5, 6], [7, 8, 9]],
	columns=['foo', 'bar', 'baz'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
df.loc[1]
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
foo    7  # last row returned
bar    8  # (2nd row is index 1)
baz    9
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Retrieving a Single Value 

__Remember that once you have a row, you can index into that as well.__ &rarr;

* {:.fragment} we can use `.loc` to get a row...
* {:.fragment} and then get a specific element from that row

__What value would this retrieve?__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
# df is      foo  bar  baz
#         0    4    5    6
#         1    7    8    9

df.loc[1]['bar']
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
8
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Transpose

__Rows can be made into columns (and columns to rows) using transpose:__ &rarr;

Imagine that `df` looks like this `DataTable`:

<pre><code data-trim contenteditable>
   foo  bar  baz
0    4    5    6
1    7    8    9
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
df.T      # transpose....
     0  1
foo  4  7
bar  5  8
baz  6  9
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## Index

__The index of a `DataFrame` is actually an object itself (not just a simple `array` of labels... Apropriately, it's called an `Index`:__ &rarr;

* {:.fragment} holds axis labels (row labels and column names)
* {:.fragment} immutable
* {:.fragment} can be shared among objects
* {:.fragment} _like_ a fixed size set
	* {:.fragment} (shares some operations)
	* {:.fragment} (but can contain duplicates)

</section>

<section markdown="block">
## `Index` Objects

__Given this example, data frame, let's take a look at its index__ &rarr;

<pre><code data-trim contenteditable>
d = pd.DataFrame({"colA": {'r1': 6, 'r2': 7},
                  "colB": {'r1': 8, 'r2': 9}})
idx = d.index
</code></pre>

<pre><code data-trim contenteditable>
idx    # Index is its own type!
Index(['r1', 'r2'], dtype='object')
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
idx[0]  # indexing works as you'd expect: 'r1'
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
idx[0] = 'nope!'  # assignment?
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
TypeError: Index does not support mutable operations
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Speaking of Indexes...

__Remember that we can get a new `DataFrame` with rearranged or repeated indexes?__ &rarr;

__Retrieve a new `DataFrame` with the column `bar` from another `DataFrame`, `df`, repeated twice__ &rarr;

<pre><code data-trim contenteditable>
# df is      foo  bar  baz
#         0    4    5    6
#         1    7    8    9
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
df[['bar', 'bar']]
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## More Powerful "Reindexing" 💪

__The method, `.reindex`, can be called on a `Series` or a `DataFrame` to:__ &rarr;

* {:.fragment} reorder columns, rows
* {:.fragment} repeat columns, rows
* {:.fragment} add columns, rows
* {:.fragment} interpolate values

By default, it returns new object, but it can also be done __in place__ (on the actual object itself) using a keyword argument
{:.fragment}

(Note, the `.loc` property on a `DataFrame` can also do some of this...)
{:.fragment}
</section>

<section markdown="block">
## _Real_ Reindexing with `Series`

__To reindex a `Series`, pass in a list of labels__ &rarr;

* {:.fragment} repeated labels are ok (values are simply repeated)
* {:.fragment} if a label is passed in that doesn't exist, it's given a missing value `NaN`

__What will the `Series`, `s`, look like following the `.reindex` operation below?__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
s = pd.Series([1, 2, 3], list('abc'))
s.reindex(['d', 'b', 'b', 'c'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
d    NaN
b    2.0
b    2.0
c    3.0
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Interpolation

__The `method` keyword argument can be used to fill in missing values via interpolation: `method="ffill"` means use the last valid value for next missing value(s)__ &rarr;

<pre><code data-trim contenteditable>
s = pd.Series([5, 7], list('ac'))
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
s.reindex(list('abcde'), method='ffill')
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
a    5
b    5
c    7
d    7
e    7
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Reindexing a `DataFrame`

__Both rows (`index`) and columns (`columns`) can be reindexed in a `DataFrame`__ &rarr;

__Using the following `DataFrame`...__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
d = pd.DataFrame({"cA": {'r1': 1, 'r2': 2, 'r3': 3},
                  "cB": {'r1': 4, 'r2': 5, 'r3': 6},
                  "cC": {'r1': 7, 'r2': 8, 'r3': 9}})
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    cA  cB  cC
r1   1   4   7
r2   2   5   8
r3   3   6   9
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Reindexing Rows

__A single positional argument for `.reindex` works on rows__ &rarr;

<pre><code data-trim contenteditable>
d.reindex(['r2', 'r3', 'r4', 'r1'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
     cA   cB   cC  
r2  2.0  5.0  8.0
r3  3.0  6.0  9.0
r4  NaN  NaN  NaN
r1  1.0  4.0  7.0
</code></pre>
{:.fragment}


Missing values filled with `NaN` by default
{:.fragment}

</section>

<section markdown="block">
## Reindexing Columns

__Using the `columns` keyword, the column names can be manipulated__ &rarr;

<pre><code data-trim contenteditable>
d.reindex(columns=['cD', 'cB', 'cB', 'cC'])
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
    cD  cB  cB  cC  # duplicates 
r1 NaN   4   4   7  # allowed...
r2 NaN   5   5   8
r3 NaN   6   6   9
</code></pre>
{:.fragment}

Again, missing values filled with `NaN` by default
{:.fragment}
</section>

<section markdown="block">
## Last Reindexing!

__Rearranging both rows and columns (and with a fill!)__ &rarr;

<pre><code data-trim contenteditable>
d.reindex(['r2', 'r1', 'r4'], 
    columns=['cB', 'cB', 'cD', 'cC'])
     cB   cB  cD   cC
r2  5.0  5.0 NaN  8.0
r1  4.0  4.0 NaN  7.0
r4  NaN  NaN NaN  NaN
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
d.reindex(['r2', 'r1', 'r4'], 
    columns=['cB', 'cB', 'cD', 'cC'], 
    method="ffill")
    cB  cB  cD  cC
r2   5   5   8   8
r1   4   4   7   7
r4   6   6   9   9
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Selection Using `.loc`

__Using `.loc` allows us to use `numpy` like indexing (whew 😅, good thing we remember _everything_ about, amirite?)__  &rarr;

__What does `.shape` give back for a two dimensional `ndarray`?__ &rarr;
{:.fragment}

A two-element tuple...
{:.fragment}

1. {:.fragment} 1st element, axis 0 is rows
2. {:.fragment} 2nd element, axis 1 is columns
</section>

<section markdown="block">
## `.loc` 

__`.loc` allows axis label indexes to select rows and indexes__ &rarr;

<pre><code data-trim contenteditable>
# d is     cA  cB  cC
#      r1   1   4   7
#      r2   2   5   8
#      r3   3   6   9
</code></pre>

<pre><code data-trim contenteditable>
d.loc['r2', 'cB'] # gives us 5!
</code></pre>
{:.fragment}


<pre><code data-trim contenteditable>
d.loc['r1':'r2', 'cB']
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
r1    4
r2    5
</code></pre>
{:.fragment}




</section>



