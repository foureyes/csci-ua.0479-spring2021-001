---
layout: slides
title: "Functions, Operations"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>
<section markdown="block">
## Numpy Functions, Apply, and Map

__In addition to basic arithmetic and comparison operators, there are some methods and functions that allow for operations across all elements, row, or columns in a `DataFrame`:__ &rarr;

* {:.fragment} `apply` to use a function for every element in a row or column or `applymap` to use a function for every element
* {:.fragment} `numpy` universal functions (`ufuncs`) - a function that operates on every element in an `ndarray`
	* {:.fragment} such as `floor`, `abs`, `add`, etc. (see [the numpy docs for more](https://docs.scipy.org/doc/numpy/reference/ufuncs.html))
</section>
<section markdown="block">
## Sample Data 

__To go over `apply` and `applymap`, we'll use two very small sample data sets__ &rarr;


* {:.fragment} [Precipitation by month from www.usclimeatedata.com](https://www.usclimatedata.com/)
	* {:.fragment} (data sourced from NOAA)
* {:.fragment} [Wikipedia - List of the largest information technology companies](https://en.wikipedia.org/wiki/List_of_the_largest_information_technology_companies#cite_note-5)
	* {:.fragment} (data sourced from official earnings reports, stats sites, etc.)



</section>

<section markdown="block">
## Precipitation Data

__Copy and paste the following into your notebook / interactive shell.__ &rarr;

<pre><code data-trim contenteditable>
import pandas as pd
rain = pd.DataFrame([[3.50, 4.53, 4.13, 3.98],
                     [7.91, 5.98, 6.10, 5.12],
                     [3.94, 5.28, 3.90, 4.49],
                     [1.42, 0.63, 0.75, 1.65]],
    index=['New York', 'New Orleans', 'Atlanta', 'Seattle'],
    columns=['Jun', 'Jul', 'Aug', 'Sept'])
</code></pre>

</section>
<section markdown="block">
## Technology Companies Data

__Copy and paste the following into your notebook / interactive shell.__ &rarr;

<pre><code data-trim contenteditable>
import pandas as pd
d = [["$229.2", 2017, 123000, "$1100", "Cupertino, US"],
     ["$211.9", 2017, 320671, "$284", "Suwon, South Korea"],
     ["$177.8", 2017, 566000, "$985",  "Seattle, US"],
     ["$154.7", 2017, 1300000, "$66", "New Taipei City, Taiwan"],
     ["$110.8", 2017, 80110, "$834", "Mountain View, US"]]

comps = ["apple", "samsung", "amazon", "foxconn", "alphabet"]
cols = ["revenue", "fy", "employees", "mcap", "location"]

c = pd.DataFrame(d, index=comps, columns=cols)

</code></pre>
</section>

<section markdown="block">
## `apply`

__`apply` allows a function to be called  on one-dimensional arrays by row or by column__ &rarr;

<pre><code data-trim contenteditable>
d.apply(fn, axis=a)
</code></pre>
{:.fragment}

* {:.fragment} `fn` is the function to be applied to every element in the one-dimensional array
* {:.fragment} `axis` is a keyword argument specifying which axis to work <span class="hl">across</span>
	* {:.fragment} if `axis` is 0 or `index`, it will work across rows (and consequently, the results will be per column)
	* {:.fragment} if `axis` is 1 or `columns`, it will work across columns (results will be per row)
* {:.fragment} the function passed in should take a single argument, a `Series`

</section>

<section markdown="block">
## Wait, What?

<span class="hl">The function passed in to `apply` is called with a `Series` representing a row or col</span>

__Let's see__  &rarr;

<pre><code data-trim contenteditable>
rain.apply(lambda arg: type(arg))
</code></pre>
{:.fragment}

(remember that lamdas return the expression after the `:`)
{:.fragment}

<pre><code data-trim contenteditable>
Jun     <class 'pandas.core.series.Series'>
Jul     <class 'pandas.core.series.Series'>
Aug     <class 'pandas.core.series.Series'>
Sept    <class 'pandas.core.series.Series'>
</code></pre>
{:.fragment}

</section>
<section markdown="block">
## `apply` Continued

__Using our rain data... let's try to calculate the following:__ &rarr;

* {:.fragment} what is the total rainfall for each month for all cities combined?
	<pre class="fragment"><code data-trim contenteditable>
rain.apply(lambda month: sum(month), axis=0)
# or axis='index'
# default is 0 anyway, so axis can be omitted
</code></pre>
* {:.fragment} what is the total rainfall for each city during the summer (all 4 months)?
	<pre><code data-trim contenteditable>
rain.apply(lambda city: sum(city), axis=1)
# or axis='columns'
</code></pre>

</section>

<section markdown="block">
## DataFrame and Series Methods

__HOLD ON! There are built in methods that work on rows / columns already! 🤭__ &rarr; 


Let's take a look at a few common ones that work on both `DataFrames` and `Series` (see [DataFrames](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) and [Series](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html) docs for more):

* {:.fragment} `sum` (we just did this with apply)
	* {:.fragment} reimplementing the solutions from the previous slide:
	* {:.fragment} `rain.sum(axis=0)`, `rain.sum(axis=1)`
* {:.fragment} `mean` - find the average rainfall for each city for all of the months in the `DataFrame`
	* {:.fragment} `rain.mean(axis="columns")`
* {:.fragment} `max` and `min` -  how much rainfall was there for each city during the _least rainy_  month
	* {:.fragment} `rain.min(axis='columns')`
* {:.fragment} of course, there are others, like `median`, `mode`, etc.

</section>

<section markdown="block">
## So, Uh, Apply Again?

__Where does that leave us with apply? Well, we can perform even more complicated row/column calculations.__ &rarr;


For each city, show the difference between the rainiest and least rainy summer month (that is, what's the difference between the max rain and the min rain?)
{:.fragment}

<pre><code data-trim contenteditable>
rain.apply(lambda city: city.max() - city.min(), axis="columns")	
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## `map`, `applymap`

__`map` and `applymap` call a function on every element in a `Series` and `DataFrame` respectively__ What `Series` will this give back?

<pre><code data-trim contenteditable>
pd.Series(['ant', 'cat', 'bat']).map(lambda word: word + 's')
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
0    ants
1    cats
2    bats
</code></pre>
{:.fragment}

...and using a named function on every element in a `DataFrame`:
{:.fragment}
<pre><code data-trim contenteditable>
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
nums = pd.DataFrame(np.arange(9).reshape((3, 3)))
nums.applymap(factorial)
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## `map` and `applymap` Practice

* {:.fragment} using our rainfall data, convert every number from inches to centimeters (1 inch is about 2.5 cm) and add cm as a label (it's ok if all values are converted to strings)
	<pre class="fragment"><code data-trim contenteditable>
rain.applymap(lambda inches: f'{inches * 2.5:.2f} cm')
</code></pre>
* {:.fragment} using our tech company data, show the revenue column such that each dollar amount is converted to an actual number (remove the dollar sign and convert to a numeric type)
	<pre class="fragment"><code data-trim contenteditable>
c['revenue'].map(lambda revenue: float(revenue[1:]))
# note the use of map instead of applymap 
# since this is a Series
</code></pre>
* {:.fragment} (btw, if you want to actually set that conversion, you can use assignment: `c['revenue'] = c['revenue'].map(lambda revenue: float(revenue[1:]))`)
</section>

<section markdown="block">
## Built-In Methods Again

__As you may have guessed, there are built in methods that apply to all elements as well__ &rarr;

* {:.fragment} `add`
	* {:.fragment} in some ways, same as using `+`
	* {:.fragment} but you can also pass in a `Series` and broadcast across rows or columns
* {:.fragment} `round`
	* {:.fragment} for our rain data, let's try to round all of the values to one decimal place
	* {:.fragment} `rain.round(1)`
</section>

<section markdown="block">
## Sorting

__A dataframe can be sorted by `index` or by `values`__ &rarr;

* {:.fragment} `sort_index` - sorts by row label lexicographically
* {:.fragment} `sort_values` - using the `by` keyword argument, sorts by a specific column
* {:.fragment} `asecending=False` - sorts in descending order for both methods above

</section>
<section markdown="block">

## Sorting Practice

__Using our Tech Company data...__ &rarr;

1. {:.fragment} show the data in ascending order based on revenue
	<pre class="fragment"><code data-trim contenteditable>
c.sort_values(by='revenue')
</code></pre>
2. {:.fragment} add a column that shows revenue per employee, then show the company that has most revenue per employee (you can do this in multiple steps)
	<pre class="fragment"><code data-trim contenteditable>
# convert revenue to float again
c['revenue'] = c['revenue'].map(lambda rev: float(rev[1:]))
</code></pre>
	<pre class="fragment"><code data-trim contenteditable>
# create a new column for revenue per employee
c['rev_emp'] = c['revenue'] * 1000000000 / c['employees'
</code></pre>
	<pre class="fragment"><code data-trim contenteditable>
# sort descending by rev_emp
c.sort_values(by='rev_emp', ascending=False)
</code></pre>

</section>

<section markdown="block">
## Summary Statistics, Unique, Counts

__Calling `describe` on your `DataFrame` yields some descriptive statistics for__ &rarr;

* {:.fragment} count (number of rows), min, max, mean, etc.
* {:.fragment} `rain.describe()` ... `c.describe()`
* {:.fragment} note that depending on types, output will vary

__To help get an overview of the values and labels you have, use `unique` and `value_counts` on a `Series`__
{:.fragment}

* {:.fragment} the `unique` method will give back an array of the unique values in a `Series`
* {:.fragment} `value_counts` is a top-level function that will count the values

</section>

