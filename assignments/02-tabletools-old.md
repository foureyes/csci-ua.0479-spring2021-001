---
layout: homework
title: "Assignment #2"
---
<style>
img {
    border: 1px solid #000;
}

.warning {
    background-color: yellow;
    color: #aa1122;
    font-weight: bold;
}

.hidden {
    display: none;
}

.hintButton {
    color: #7788ff;
    cursor: pointer;
}
</style>
<script>
document.addEventListener('DOMContentLoaded', hideHints);

function hideHints(evt) {
    document.querySelectorAll('.hint').forEach((ele, i) => {
        const div = document.createElement('div');
        div.id = 'hint' + i + 'Button';
        ele.id = 'hint' + i;
        ele.classList.add('hidden');
        div.addEventListener('click', onClick);
        div.textContent = 'Show Hint';
        div.className = 'hintButton';
        ele.parentNode.insertBefore(div, ele);
    });

}

function onClick(evt) {
    const hintId = this.id.replace('Button', '');
    const hint = document.getElementById(hintId);
    hint.classList.toggle('hidden');
    this.textContent = this.textConent === 'Show Hint' ? 'Hide Hint' : 'Show Hint';
}
</script>

# Assignment #2 - List Comprehensions, Classes, CSV, Tabular Data - Due Wed, Sep 26th (extended from Mon, Sep 24th) at 11pm


This assignment consists of two parts:

1. `tabletools.py`
2. Candy!

Clone the homework #2 repository when it is created for you.

## Goals

* create classes
	* implement magic methods
	* create an iterator
* use list comprehensions
* work with csvs
* use a lambda function
* preview working with tabular data in Python

## Part 1 - `tabletools.py`

Working with tabular data as a two-dimensional `Array` is pretty common, but as soon as you try to do some simple operations like filtering based on column name, things get complicated quickly unless you throw in some additional libraries or tools. 

In this homework, we'll being creating (a _maybe over-engineered_) module for reading in csvs and filtering rows based on column values. You'll have to use some Python features in your implementation, like `__iter__`, list comprehensions, etc.

For example, imagine we had a csv containing people's names, the number of fruits they eat weekly, and their favorite color (um... idk?). This data is in a csv called `fruitarians.csv`, and can be visualized as a table (note that row # is not in the csv):

```
 row #    first        last   weekly_fruits_eaten  fav_color
     0      abe       apple                     0        red
     1      bob      banana                     4     yellow
     2    carol     coconut                   100      white
     3      bob   blueberry                     9       blue
     4      eve      endive                    20      green
     5  frances       fruit                     5          ?
     6      ann       apple                    23      green
```

What if we'd like to run some reports on this? For example:

* read in the csv...
* what do the first three columns look like?
* how many people have the last name, apple?
* what is the first name and number of fruits eaten / week of everyone that eats more than 10 fruits a week
* how many people have a first name less than 4 letters eat less than 10 fruit / week?

We'll create an api to do this... and it'll look something like this:

```
import tabletools as tt

# read in the csv
t = tt.read_csv('fruitarians.csv')

# what do the first three columns look like?
t.head(3)

"""
                first                last weekly_fruits_eaten           fav_color
0                 abe               apple                 0.0                 red
1                 bob              banana                 4.0              yellow
2               carol             coconut               100.0               white
"""

# how many people have the last name, apple?
t[t['last'] == 'apple'].shape()[0]

"""
2
"""

# what is the first name and number of fruits eaten / week of everyone that eats more than 10 fruits a week
t[t['weekly_fruits_eaten'] > 10][['first', 'weekly_fruits_eaten']]

"""
                first weekly_fruits_eaten
2               carol               100.0
4                 eve                20.0
6                 ann                23.0
"""

# how many people have a first name less than 4 letters eat less than 10 fruit / week?
def length_less_than(n):
    def is_length_less_than_n(s):
        return len(s) < n
    return is_length_less_than_n
first_name_three = t[t['first'].map(length_less_than(4))]
first_name_three[first_name_three['weekly_fruits_eaten'] < 10]

"""
                first                last weekly_fruits_eaten           fav_color
0                 abe               apple                 0.0                 red
1                 bob              banana                 4.0              yellow
3                 bob           blueberry                 9.0                blue
"""
```


1. You'll be writing two classes:
	* `LabeledList` - kind of like a `dict`, but ordered, allows _vectorized_ operations, and iterates over values instead of keys
	* `Table` - a table of data with column labels
2. Open `tabletools.py` in a text editor of your choice
3. Write the classes mentioned above...
	* __YOU MUST USE AT LEAST 4 LIST COMPREHENSIONS!__
	* __YOU CANNOT USE THE FOLLOWING MODULES__: `numpy`, `pandas`, `csv`
4. Using your previously implemented `tablestools.py` as a module, import it and use it in a notebook to do some very simple analysis on candy data!

<hr>

### `LabeledList`

A `LabeledList` acts like a dictionary... but:

* it's ordered (note that 3.7 has ordered dictionaries by default, though)
* when you loop over it, you get values instead of keys
* if you use a comparison operator with it... and a scalar value (a number, for example), that comparison is done on each value, yielding a new `LabeledList` composed of only `bool` values
* duplicate 'keys' are allowed

Here's how you might use it:

```
ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
ll['A'] # gives back value at label 'A'
ll['BB'] # gives back new LabeledList composed of labels 'BB' and their values
ll[['A', 'D', 'BB', 'BB']] # gives back new LabeledList composed of the labels specified in list... along with their values
ll > 2 # gives back a new LabeledList composed of labels in original, along with boolean results of comparison
```

<hr>

#### Properties:

* `self.values` - contains the values in this `LabeledList` as a `list`
	* ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	* ll.values # [1, 2, 3, 4, 5]
* `self.index` - contains the labels in this `LabeledList` as a `list`
	* ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
	* ll.index # ['A', 'BB', 'BB', 'CCC', 'D']

<hr>

#### `__init__(self, data=None, index=None)`

Creates a new `LabeledList`. 

* `data` - the values stored in `self.values`; represents all of the values in this `LabeledList`
* `index` - the labels associated with each value

`data` and `index` are assumed to be the same length (no error checking is necessary) and the order of the elements in each list determines which values are associated with which labels (if data is `[0, 1]` and values are `['foo', 'bar']`, then the label `0` is associated with the value `'foo'`

You can assume that the labels and values are only `str`, `int`, `float`, and `bool` (no type checking is needed in the constructor). Duplicate labels are allowed.

Note that if `index` is `None` then the labels should be from 0 to the length of the data - 1:
```
list_with_default_labels = tt.LabeledList(['foo', 'bar', 'baz'])

"""
0 foo
1 bar
2 baz
"""

list.index # [0, 1, 2]
```

However, if `index` is provided...

```
ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
"""
  A 1
 BB 2
 BB 3
CCC 4
  D 5
"""
```

<hr>

#### `__str__(self)` and `__repr__(self)`

These two methods will give the string representation of a `Labeled List`. `__str__` is used for human readable format (such as when printing) and `__repr__` is used for displaying _what the object actually is_ (for example, debugging by just typing the object name in the interactive shell). 

For our purposes, these will return the same string (in fact, one can call the other).

The string should be a tabular format where labels are on the left and values on the right. You can space this out any way you like, as long as it's very clear what the labels and columns are.

Using the earlier example, here's a nicely formatted `LabeledList`:

```
ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])
"""
  A 1
 BB 2
 BB 3
CCC 4
  D 5
"""
```

It will be useful to use dynamically padded strings to maintain consistent widths for columns. This can be done with format strings and [the format specification mini language](https://docs.python.org/3/library/string.html#format-specification-mini-language). For example: 

```
s = 'foo'

# print out 'foo' so that it's padded with spaces and tis total length is 10
print(f'{s:>10})

# results in:
#       foo
```

The `:` signals that a format specifier is coming up. The `>` aligns right. Finally, the `10` is the total width of the new string (spaces will pad the left side).

Of course, you may want the `10` to be variable...

```
vals_max_len = m # imagine that this is the length of the longest label
label = s # imagine that this is a label whose length is shorter than the longest label
# we want to pad this thing ^^^^

# create a format specifier that right justifies and pads
format_spec = '>{vals_max_len}' 

# now add that format specifier to another formatted string by nesting curly braces!?
f'{label:{format_spec}}'
```

Note that if the variable in the format string is a boolean and a format specifier is given, then the boolean will either be a 0 or 1 rather than `True` or `False` which is ok for our purposes (a work-around is to convert the boolean to a string first... then format with `f''`)

<hr>

#### `__getitem__(self, key_list)`

`__getitem__` allows our object to be indexed / 'keyed' into as if it were a `dict`. In `LabeledList` the label is the key. Our implementation's key behavior depends on the type of the key:

1. if the key is another `LabeledList` then the key is the `values` property of that labeled list (which is, of course a `list`... see below for how to handle `list` and a `list` of only `bool` values)
2. if the key is a `list`, then that means that we're retrieving multiple labels and values, so a new `LabeledList` is returned with each label specified and its associated value (if a label occurs more than once, add all occurrences)
3. if the key is specifically a list of `bool` values, then give back a new `LabeledList` where the only label and value pairs given are the ones where the position matches the position of a `True` in the incoming key list (you can assume that the list of `bool` values must be the same length as the `index` of labels... you can error handling if it makes it easier to debug your code, though!)
4. given any single value as the label (such as `str`, `int`)... you will get back:
	a. the value associated with that exact label if the label occurs only once
	b. a new `LabeledList` composed of that label repeated, along with its values

Ok. So that's pretty confusing. Here are some examples:

```
ll = tt.LabeledList([1, 2, 3, 4, 5], ['A', 'BB', 'BB', 'CCC', 'D'])

# 1 (values are taken from LabeledList as a list...
# more than one label yields all label and value pairs)
ll[tt.LabeledList(['A', 'BB'])]

"""
 A 1
BB 2
BB 3
"""

# 2 (same as above, but with plain list)
ll[['A', 'BB']] 

"""
 A 1
BB 2
BB 3
"""

# 3 (only the last two label value pairs have the same positions as True
ll[[False, False, False, True, True]]

"""
CCC 4
  D 5
"""

# 4a (value is returned as is... just like a dict)
ll['A']

"""
1
"""

# 4b (new LabeledList is returned even though only single value key)
ll['BB'] #

"""
BB 2
BB 3
"""
```

Use the built-in function, [`isinstance`](https://docs.python.org/3/library/functions.html#isinstance) to check if a value is a particular type:

```
isinstance(key_list, LabeledList)
isinstance(key_list, list)
```

<hr>

<!--

#### `__setitem__(self, key, value)`

Like assignment for `dict`, but if duplicate keys exist all of those values change:

```
# using ll from previous examples where BB was associated with 2... then 3
ll['BB'] = 100
"""
  A   1
 BB 100
 BB 100
CCC   4
  D   5
"""
```
-->

<hr>

#### `__iter__(self)` 

Implement `__iter__` so that it returns a new object that has a `__next__` method... for this, simple return `self.values` so that iterating over a `LabeledList` gives back values instead of keys:


```
# using the previous version of ll
for val in ll:
    print(val)
"""
1
100
100
4
5
"""
```

<hr>

#### `__eq__(self, scalar)`, `__ne__(self, scalar)`, `__gt__(self, scalar)`, `__lt__(self, scalar)`

These methods all correspond to an associated comparison operator (`==`, `>`, etc.). Each makes an assumption that the only thing passed in is a numeric type (that is, the other operand is numeric when using the associated comparison operator). They should return a new `LabeledList` of `bool` values corresponding to the operation specified for every value compared to the `scalar` passed in.

__If there is an index present, keep that index__

__This might be a good place to get in your four list comprehensions!__

```
tt.LabeledList([0, 1, 2, 3, 4]) > 2
0 False
1 False
2 False
3  True
4  True
```

```
ll = tt.LabeledList([1, 2], ['x', 'y'])
ll == 1
x  True
y False
```

<hr>

#### `map(self, f)`

Gives back a new `LabeledList` with all of the values transformed to the result of calling `f` on that value.

```
def squared(n):
    return n ** 2
tt.LabeledList([5, 6, 7]).map(squared)
0 25
1 36
2 49
```

<hr>

### `Table` 

A `Table` represents tabular data with row labels (`index`) and column names (`columns`)... along with 2 dimensional grid of data (`data`).

It supports operations for filtering by values in a column... as well as selecting specific columns.


#### Properties

* `self.values` - contains the values in this `Table` as a `list`
    * `t = Table([[1, 2, 3],[4, 5, 6]],['a', 'b'], ['x', 'y', 'z'])`
	* `.values # [[1, 2, 3],[4, 5, 6]]`
* `self.index` - contains the row labels in this `Table` as a `list`
    * `t = Table([[1, 2, 3],[4, 5, 6]],['a', 'b'], ['x', 'y', 'z'])`
	* `t.index # ['a', 'b']`
* `self.columns` - contains the column names  in this `Tabled` as a `list`
    * `t = Table([[1, 2, 3],[4, 5, 6]],['a', 'b'], ['x', 'y', 'z'])`
	* `t.index # ['x', 'y', 'z']`

#### `__init__(self, data, index=None, columns=None)`

If either `index` or `columns` are not included, then default to numeric values from 0 up to length of `index` - 1 or `columns` - 1

```
t = Table([['foo', 'bar', 'baz'],['qux', 'quxx', 'corge']])

      0     1     2
0   foo   bar   baz
1   qux  quxx corge
```

Otherwise, adding the `index` and `columns` as arguments will explicitly set the row labels and column names

```
t = Table(d, ['foo', 'bar', 'bazzy', 'qux', 'quxx'], ['a', 'b', 'c', 'd', 'e'])

         a    b    c    d    e
  foo 1000   10  100    1  1.0
  bar  200    2  2.0 2000   20
bazzy    3  300 3000  3.0   30
  qux   40 4000  4.0  400    4
 quxx    7    8    6    3   41
```
#### `__str__(self)` and `__repr__(self)`

Again, these two methods will give the string representation of an object. `__str__` is used for a human readable format (for example, used with `print`), and `__repr__` is used for displaying _what the object actually is_ (for example, typing the object name Jupyter). Both of these methods return strings, and for our purposes, these can be the same string.

For a `Table` object, create a string representation in any way such that rows and columns can be clearly distinguished. See the example below for a potential format (it's ultimately up to you how you'd like to format it, though... as long as the grader can read it and determine which rows and columns are aligned). 

Please read the notes for the `LabeledList` `__str__` and `__reper__` methods for info on setting a consistent width for cells using string formatting (`f'{foo:{format_spec}}'`).

```
t = Table([['foo', 'bar', 'baz'],['qux', 'quxx', 'corge']])

      0     1     2
0   foo   bar   baz
1   qux  quxx corge
```

#### `__getitem__(self, col_list)`

`__getitem__` allows our `Table`  to be indexed / 'keyed' into as if it were a `dict`. The behavior of indexing or retrieving by key depends on the type of the value used as a key!

Essentially, most keys result in selecting all rows, but specifying which columns to include in a new `Table` (for example `t['a'] selects column a from all rows, and t[['a', 'b']] selects column a and b from all rows. The main exception is a list or `LabeledList` of `bool` values... which specifies which rows to include based on position of the `bool` value and the position of the row (for example, if `t` has 2 rows, then t[[True, False]] will only give back the first row as a new `Table`. 

If there's ever only one column returned, give back a `LabeledList`. Otherwise, give back a `Table`.

For exact details, see below:

1. if the key is a `LabeledList`, then the key is the `values` property of that labeled list (which is a `list`)... and a `Table` consisting of __only__ the columns contained in the `LabeledList` is returned (note that all rows are returned) ... note that if the `LabeledList` `values` are all `bool`, then follow the procedure for dealing with a list of `bool` values as shown below
2. if the key is a `list`, then that means that we're retrieving multiple columns, so a new `Table` is returned including only the columns specified by the elements in the key list passed in. If a key list has repeated column names, duplicate the column. If a column name matches more than one column, add both columns in the resulting Table.
3. if the key is specifically a list of `bool` values, then give back a new `Table` where the only rows given are the ones where the position matches the position of a `True` in the incoming key list (you can assume that the list of `bool` values must be the same length as the total number of rows in the `Table` object)
4. given any single value as the label (such as `str`, `int`)... you will get back:
	a. _that_ column for all rows as a `LabeledList` if there is only one occurrence of that column name
	b. a new `Table` composed of that column repeated if there are duplicate column names

Once again, the behavior is complex enough to warrant examples:

```
#####
# Remember... if only one column is given back, return a LabeledList
# ...but if there's more than one column, give back a Table
#####

# 1 (using a LabeledList to select columns)
t = Table(d, ['foo', 'bar', 'bazzy', 'qux', 'quxx'], ['a', 'b', 'c', 'd', 'e'])
t[LabeledList(['a', 'b'])]
"""
         a    b
  foo 1000   10
  bar  200    2
bazzy    3  300
  qux   40 4000
 quxx    7    8
"""

# 2 (the first two columns are selected using a list of columns...
# notice that repeat columns are allowed)
t = Table([[15, 17, 19], [14, 16, 18]], columns=['x', 'y', 'z'])
t[['x', 'x', 'y']]

"""
   x  x  y
0 15 15 17
1 14 14 16
"""

# 3 (select only the first and third rows by using a list of booleans)
t = Table([[1, 2, 3], [4, 5, 6], [7, 8 , 9]], columns=['x', 'y', 'z'])
t[[True, False, True]]

"""
  x y z
0 1 2 3
2 7 8 9
"""

# 4a (using a column name that matches only a single column gives
# back a LabeledList... note no column names, but there are labels!)

t = Table([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'a'])
t['b']

"""
0 2
1 5
"""

# 4b (however, if more than one column matches column name, include
# all matched columns in the resulting Table object)
t = Table([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'a'])
t['a']

"""
  a a
0 1 3
1 4 6
"""
```


<!--
#### `__eq__(self, other)` and `__ne__(self, other)`

Only implement for `other` as a `Table` (you do not have to implement this for vectorized comparisons / arithmetic). Determines if two `Table` objects are equal by comparing the values in `values`, `index` and `columns`:

```
t1 = Table([[4, 5], [6, 7]])
t2 = Table([[4, 5], [6, 7]])
t1 == t2
True
```

```
t3 = Table([[4, 5], [6, 7]], columns=['a', 'b'])
t1 == t3
False
```

```
t4 = Table([[4, 5], [6, 7]], index=['r1', 'r2'])
t1 == t4
False
```
(Note return value is _just_ a single boolean)
-->

#### `head(self, n)` and `tail(self, n)`

Returns a `Table` showing the first or last `n` row respectively.

```
t = Table([[1, 2], [3, 4], [5, 6], [7, 8]], columns=['x', 'y'])

print(t.head(2))

"""
  x y
0 1 2
1 3 4
"""

print(t.tail(2))

"""
  x y
2 5 6
3 7 8
"""
```
#### `shape(self)`

Gives back a tuple containing the number of rows and columns:

```
t = Table([[1, 2], [3, 4], [5, 6], [7, 8]], columns=['x', 'y'])
t.shape()

"""
(4, 2)
"""
```

### `read_csv(fn)`

Finally, in `tabletools.py`, write a function that reads in a `csv` file and gives back a `Table` object:

1. assume that the first row is the header (it can be treated as column names)
2. assume that there is no need to escape commas (a simple `split` will suffice)
3. beware of leading and trailing whitespace (`strip` may be helpful)
4. __convert numeric values to `floats`__ (use `try`/`except`... and look for `ValueError` specifically)

To test your code, you can try to open a csv from your `tabletools.py` module. Once you're finished testing, you can comment out the code (or alternatively, you can wrap your test code in `if __name__ == '__main__':
` to only run it when the module isn't being imported) 

<hr>

## Part 2 - Candy!

[Using the `candy-power-ranking` data set](https://data.fivethirtyeight.com/), explore the data using a notebook and your `LabeledList` and `Table` classes.

* display the last 4 rows of the data set
* show the candy name, if it's chocolate, if it's peanuty/almondy, and its win percentage for all candy that is chocolate
* using the results above, add another criteria: only candies that are peanuty/almondy (that is... at the end, you'll only have a listing of chocolate and peanut candies!)
* using the previous results... let's see how many chocolate and peanut candies lost (their win percentage is < than 50)
* now... show the candies whose name starts with "Reese"
* finally... show all the candies whose name is less than 10 characters long
* __YOU MUST USE LAMBDAS FOR THE LAST TWO__

## Annotations

Add a `README.md` that [links to the lines of code (see this link for instructions how)](https://help.github.com/articles/creating-a-permanent-link-to-a-code-snippet/) where you have:

* 4 list comprehensions
* 2 lambdas

Use this exact markdown format in your `README.md` to add links (including []'s and ()'s):

```
* List Comprehensions
	1. [short description 1](https://path.copied/for/permalink/to/code)
	2. [short description 2](https://path.copied/for/permalink/to/code)
	3. [short description 3](https://path.copied/for/permalink/to/code)
	4. [short description 4](https://path.copied/for/permalink/to/code)
* Lambdas
	1. [short description 1](https://path.copied/for/permalink/to/code)
	2. [short description 2](https://path.copied/for/permalink/to/code)
```

