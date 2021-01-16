---
layout: slides
title: "Missing Data and Basic Transformations"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Missing Data

__The special value, `np.nan`, means missing data.__ &rarr;

* {:.fragment} btw, that's a floating point value!?
* {:.fragment} is seen through pandas to represent
	* {:.fragment} missing data
	* {:.fragment} also referred to as NA
	* {:.fragment} __sentinal__ value - easily distinguished from valid values
* {:.fragment} (btw, the reason for missing data should be investigated before determining _what to do with missing data_)

</section>

<section markdown="block">
## WAT Can be Done?

__If we have a bunch of `np.nan` values, what should be done with those values (if anything)?__ &rarr;

It depends on the context, right? ...  ok, well, what are the options then, regardless of context
{:.fragment}

First, two extremes:
{:.fragment}

1. {:.fragment} revisit data collection
2. {:.fragment} ignore

But also:
{:.fragment}

1. {:.fragment} set to some default value
2. {:.fragment} interpolate based on surrounding data

</section>

<section markdown="block">
## Ignoring It 🙈🙉

For a DataFrame, use `dropna`

* drops all rows containing NA value
* can pass `axis=1` to drop columns

```
df = pd.DataFrame(np.arange(12).reshape((3, 4)), 
	columns=list('abcd'))
df.loc[1, 'd'] = np.nan
df.loc[2, 'c'] = np.nan
df.dropna(axis=1)
```
{:.fragment}

Columns (`axis=1`) c and d are dropped, since they have missing values.
{:.fragment}
</section>

<section markdown="block">
## Ignoring More Precisely  🎯


__Remember: on a Series, `.isnull` or `.notnull` produces a boolean Series__ &rarr;

1. {:.fragment} use  `.isnull` or `.notnull` on a column
2. {:.fragment} then filter by using the resulting Series


```
# (df is dataframe from previous slides)
df[df['d'].notnull()]
```
{:.fragment}
</section>

<section markdown="block">
##  Set to Value

__Maybe you just want to fill those pesky missing values with some default value 🔨
.__ 
&rarr;

* {:.fragment} use `fillna` on DataFrame
* {:.fragment} will fill with value passed in 
* {:.fragment} if `dict`, keys will match column names, and values will be used on those columns
* {:.fragment} (also, interpolation w/ keyword args same as reindex, like `method='ffill'`)

```
# using df from previous slides
df.fillna(0)
df.fillna({'c': 100, 'd': 123})
df.fillna({'c': 100, 'd': df['d'].mean()}) # 💪
df.fillna(method='ffill')
```
{:.fragment}

</section>

<section markdown="block">
## Transformation

The following can be used to a call function on: 

* `map` - every element in a Series
* `applymap` - every element in a DataFrame
* `apply` - go across an axis and call function on collection of values


</section>

<section markdown="block">
## `str` Accessor

__Using `.str` on a `Series` allows you to perform vectorized string operations__ &rarr;

* `lower` / `upper`
* `strip`
* `split`
* `replace`
* ...etc. (much like regular string methods)
{:.fragment}

These methods are similar to a `str`'s built-in string methods: 
{:.fragment} 

* {:.fragment} but it's done on every element
* {:.fragment} ...and automatically skips missing / `nan` values
* {:.fragment} check out the pandas [working with text docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)

</section>

<section markdown="block">
## `str` Functions

__In the dataframe below, convert the values in column 1 so that:__ &rarr;

* each element is uppercased
* and the . is replaced with an exclamation point

```
df = pd.DataFrame([['a.', 'b.'], ['c.', 'd.']])
```

```
    0   1
0   a.  b.
1   c.  d.
```

Chaining `str.upper` and `str.replace`:
{:.fragment}

```
df[1] = df[1].str.upper().str.replace('.', '!')
```
{:.fragment}

```
    0   1
0   a.  B!
1   c.  D!
```
{:.fragment}
</section>

<section markdown="block">
## `str.split` Example 

__In the following example, break apart a string in a column... and create two new columns.__ &rarr;

```
df = pd.DataFrame([['BAZCO', 'https://baz.edu' ],
                   ['Foo Inc', 'http://foo.com']],
              columns=['Name', 'URL'])
```

```
	Name	URL
0	BAZCO	https://baz.edu
1	Foo Inc	http://foo.com
0	BAZCO	https://baz.edu
1	Foo Inc	http://foo.com
```

Let's take URL, and split it into protocol and domain...
</section>

<section markdown="block">
## `str.split` Continued

__Using `str.split` w/ `expand=True`, we can create a new DataFrame with the values from the split placed into two columns__ &rarr;

```
tmp = df['URL'].str.split('://', expand=True)
```
{:.fragment}

```
	0	1
0	https	baz.edu
1	http	foo.com
```
{:.fragment}

Finally, to assign back to original DataFrame as new columns:
{:.fragment}

```
# just the domain
df['domain'] = tmp[1]

# add both protocol and domain
df[['protocol', 'domain']] = tmp
```
{:.fragment}

</section>

<section markdown="block">
## Replace Entire Value

__The `str` accessor property allows for replacing parts of a string... but what if you want to replace an entire value -- any value?__ &rarr;

The `.replace(old_val, new_val)` method on a DataFrame will do this for you!
{:.fragment}

```
df = pd.DataFrame([['foo', -1],
                   ['foo', 12],
                   ['bar', 3]], columns=['a', 'b'])
```
{:.fragment}

```
df = df.replace('foo', 'qux')
df = df.replace(-1, 100)
```
{:.fragment}

...replaces all values `'foo'` with `'qux'`, and -1 with 100
{:.fragment}
</section>

<section markdown="block">
## "Binning" Values

__Perhaps you have _a lot_ of _continuous_ data. It may be useful to categorize that data into bins for easier reporting.__ &rarr;

* {:.fragment} use `pd.cut(data, bins, labels=labels)`
* {:.fragment} `bins` represents boundaries of bins as a list: 
	* `[82, 86, 89, 92, 100]`
	* the bins are pairs of each number, and the number next to it
	* the first number in the pair is exclusive, the second is inclusive
	* consequently, groups are: 83-86, 87-89, 90-92, 93-100
* {:.fragment} `labels` can be used to specify text labels for each bin 
* {:.fragment} the result of `pd.cut` is a categories object
* {:.fragment} the values of a categories object can be counted by using:
	* `pd.value_counts(category_object)`

</section>

<section markdown="block">
## Binning Example

__In this example, we'll map exam scores to letter grades__ &rarr;

```
scores = [83, 86, 87, 89, 90]
bins = [82, 86, 89, 92, 100]
labels = ['B', 'B+', 'A-', 'A']
```

```
# use cut to bin the scores into bins
# using labels as the text labels
grades = pd.cut(scores, bins, labels=labels)
```
{:.fragment}

```
# now lets count the values that fall into each bin
pd.value_counts(grades) 
```
{:.fragment}

```
# we get back the Series:
B+    2
B     2
A-    1
A     0
dtype: int64
```
{:.fragment}

</section>
<section markdown="block">
## Renaming Columns and Rows

__We've been dealing mostly with values / data in the DataFrame, but what about column and row names?__

```
df = pd.DataFrame(np.arange(9).reshape((3, 3)),
                 columns = ['a', 'b', 'c'])
```

Use a  DataFrame's `.rename` method to return a new DataFrame with transformed column or row names:
{:.fragment}

```
# change all columns with a transform function
df.rename(columns=str.upper)

# change individual column names with a dict
df.rename(columns={'a': 'x', 'c': 'z'})
```
{:.fragment}

</section>
<section markdown="block">
## Changing Column / Row Names Continued

This can also be done "in place" by explicitly setting `index` or `columns`... (we can even use `map` to transform!): 

This changes all of the column names to uppercase:
{:.fragment}

```
df.columns = df.columns.map(str.upper)
```
{:.fragment}

This replaces all row names with values from a list:
{:.fragment}

```
df.index = [5, 7, 9]
```
{:.fragment}

Remember, however, that an Index object is immutable ⚠️, so you cannot use assignment to change single column or row names (use `.rename` with a `dict` instead): `df.columns[1] = 'Z'` will cause an error 🚫.
{:.fragment}

</section>

<section markdown="block">
## Constraining Values

__To show rows where any column has a value that meets a criteria, use `.any` (note that these operations are on an entire DataFrame__ &rarr;

```
df = pd.DataFrame([[2, 3], [1, 50], [20, 4], [3, 45]])
```

```
# show all rows with a value > 10
df[(df > 10).any(1)]
```
{:.fragment}

__To find values in a column that exceed a certain threshold, we can index with booleans (we've seen this before!)__ &rarr;
{:.fragment}

```
# find all rows w/ values in column 1 that's > 10
df[df[1] >  10]
```
{:.fragment}

We can replace / cap those values by using reassignment
{:.fragment}

```
df[1][df[1] >  10] = 10
```
{:.fragment}

</section>

<section markdown="block">
## Type Conversion

__Data frame columns have types (they're Series after all!)__

Use `df.dtype`, `df.count()`, and `df.info()` to see type info!
{:.fragment}

To convert from one type to another:
{:.fragment}

* {:.fragment} `astype(newType)`
* {:.fragment} `pd.to_numeric(colName)`
* {:.fragment} `pd.to_datetime(colName)`
* {:.fragment} (the last two allow ignoring type errors)
</section>

<section markdown="block">
## to_numeric vs astype

Note that `astype` will result in a __runtime exception__ if one the values in the DataFrame __cannot be converted to a number__.

```
astype(newType)
```

Adding an `errors` keyword argument to `to_numeric`, and setting it to `'coerce'`: 
{:.fragment}

* {:.fragment} will take values that would cause errors...
* {:.fragment} and give back `NaN`

```
pd.to_numeric(df['Column Name'], errors='coerce')
```
{:.fragment}

</section>

<section markdown="block">
## to_numeric Example

__Here's an example of using `to_numeric`__ &rarr;

```
data = [['2009', '$500'],
        ['2010', '$1,234'],
        ['2011', 'WAT!'],
        ['2012', '$2,507']]
df = pd.DataFrame(data , columns=['date', 'total'])
```

The `total` column is type `object`. Let's convert it to a numeric type by:

* {:.fragment} removing non numeric values from the string using chained calls to `replace`
* {:.fragment} ...and converting with `pd.to_numeric`

```
t = df['total'].str.replace('$', '').str.replace(',', '') # 🚫💰,
df['total'] = pd.to_numeric(t, errors='coerce') #👍
```
{:.fragment}

</section>


<section markdown="block">
## Quick Primer on datetime

To convert a column into a datetime object 📅⏰, use `pd.to_datetime(col)` (where col is a DataFrame column, a Series).

```
s = pd.Series(['Jan 7, 2014', 'May 29, 1993'])
```

```
pd.to_datetime(s)
```
{:.fragment}

```
0   2014-01-07
1   1993-05-29
dtype: datetime64[ns]
```
{:.fragment}

Note that conversion will autodetect format, but you can specify your own with a keyword argument [see official docs](https://pandas.pydata.org/pandas-docs/version/0.19/generated/pandas.to_datetime.html)
{:.fragment} 

```
pd.to_datetime('2017-02-03', format='%Y %m %d')
# Timestamp('2017-02-03 00:00:00')
```
{:.fragment}

</section>

<section markdown="block">
##  datetime Continued

__From here, you can use the `dt` accessor property to manipulate datetime objects in a Series:__ &rarr;
{:.fragment}

```
# using the dataframe in the previous slide...
# show month numbers
pd.to_datetime(s).dt.month
```
{:.fragment}

```
0    1
1    5
```
{:.fragment}

```
# show month names
pd.to_datetime(s).dt.month_name()
```
{:.fragment}

```
0    January
1        May
```
{:.fragment}

</section>

