---
layout: slides
title: "Indexes, Hierarchical Indexes, Grouping"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## More About Indexes, Aggregation

__In this set of slides, we'll take a closer look at indexes (_row labels_)... and tie that in to grouping rows together.__ &rarr;

To do this, we'll use data extracted from the US Department of Labor's [Occupational Employment Statistics](https://www.bls.gov/oes/tables.htm).

* it consists of a small amount of data picked out from the data source above
* minor transformations were made:
	* adjusting occupation names, like Database Administrator &rarr; DB Admin
	* adjusting column names, like Occupation Title &rarr; Title
</section>

<section markdown="block">
## Sample Data

```
cols = ["Year", "State", "Title", "Employment", "Salary"]
```

```
data = [[2018, "CA", "Web Dev", 20170, 86160],
        [2018, "CA", "DB Admin", 10970, 100890],
        [2018, "NY", "Web Dev", 12030, 79880],
        [2018, "NY", "DB Admin", 7100, 99000],
        [2017, "CA", "Web Dev", 21150, 84270],
        [2017, "CA", "DB Admin", 12030, 95630],
        [2017, "NY", "Web Dev", 11900, 82360],
        [2017, "NY", "DB Admin", 7170, 94330],
        [2016, "CA", "Web Dev", 22650, 82930],
        [2016, "CA", "DB Admin", 12370, 93960],
        [2016, "NY", "Web Dev", 11410, 81140],
        [2016, "NY", "DB Admin", 6650, 91720]]
```
{:.fragment}

```
df = pd.DataFrame(data, columns=cols)
```
{:.fragment}


</section>
<section markdown="block">
## Setting a New Index

__Let's first start off by modifying the index.__ &rarr;

One way is to set the `.index` explicitly as we've seen before:
{:.fragment}

```
some_df.index = ['new', 'index', 'values']
```
{:.fragment}

There's also `.reindex`... reorder, leave out, etc.
{:.fragment}

```
# reorder indexes, add new indexes, and leave out indexes
some_df.reindex([1, 4, 2, 3])
```
{:.fragment}
</section>

<section markdown="block">
## `.set_index`

An index can also be specified by using the `set_index` method on a frame to convert a column into an index (which returns a new frame)...

__Here's an example of turning a column into an index:__ &rarr;

```
# convert Year to index
tmp = df.set_index('Year')
```
{:.fragment}

Now we can do something like slice based on year as index!
{:.fragment}

```
tmp.loc[2016:2017]
```
{:.fragment}

Note however, that the column `Year`, no longer exists
{:.fragment}

```
tmp['Year] # KeyError 😞
```
{:.fragment}

</section>

<section markdown="block">
## Multiple Indexes!

__`set_index` also allows you to pass in multiple column names... doing so creates more than one index__ 😮

```
df = df.set_index(['Year', 'State'])
```
{:.fragment}

```
		Title		Empl 	Salary
2016	CA	Web Dev		22650	82930
	CA	DB Admin	12370	93960
	NY	Web Dev		11410	81140
	NY	DB Admin	6650	91720
2017	CA	Web Dev		21150	84270
	CA	DB Admin	12030	95630
	NY	Web Dev	11900	82360
...
```
{:.fragment}

Uh... what? This is an example of __hierarchical indexing__....
{:.fragment}
</section>

<section markdown="block">
## Hierarchical Indexing

__Hierarchical Indexing__ allows multiple levels of indexes on an axis. We'll be concentrating mainly on rows, though...

To interpret the previous frame: 

* __you can think of the year as being the same for all rows underneath the row with an actual value for year__
* additionally, each index can be considered a __level__ in the hierarchy of indexes
* the name of a level is the same as that of the index
* `df.index.names`

</section>

<section markdown="block">
## Initial Indexing

__Let's see when we try to use the outermost index:__ &rarr;

```
df.loc[2016]
```
{:.fragment}

We get back get a DataFrame with the outer index removed
{:.fragment}

```
CA	Web Dev		22650	82930
CA	DB Admin	12370	93960
NY	Web Dev		11410	81140
NY	DB Admin	6650	91720
```
{:.fragment}

</section>

<section markdown="block">
## Indexing with Both Outer and Inner

__You can "drill down" by using multiple indexes by using a tuple or comma separated values in `loc`__ &rarr;

```
df.loc[(2016, 'CA')]
```
{:.fragment}

```
df.loc[2016, 'CA']
```
{:.fragment}

both return
{:.fragment}

```
		Title	Employment	Salary
Year	State
2016	CA	Web Dev		22650	82930
	CA	DB Admin	12370	93960
```
{:.fragment}

</section>
<section markdown="block">
## Summary by Level

__Now that we have a MultiIndex, we can group rows by level and run summary statistics (`max`, `min`, `mean`, `count`, etc.) on a specific group__ &rarr;

The DataFrame methods for summary statistics take a keyword argument, `level` to specify which "group" to work on:

```
# mean of all values for each state
df.mean(level='State')

# mean of all values for each year
df.mean(level='Year')
```
{:.fragment}

```
# number of rows per state
df.count(level='State')
```
{:.fragment}
</section>
<section markdown="block">
## Grouping, Aggregation

__Using MultiIndexes to do grouping operations is pretty powerful...__ &rarr;

Secretly, though, it's actually using pandas `GroupBy`.
{:.fragment}

`GroupBy` allows:
{:.fragment}

* {:.fragment} the splitting apart of a data set into separate chunks...
* {:.fragment} and then running operations / working on all of the resulting chunks

</section>
<section markdown="block">
## How GroupBy Works

__The grouping mechanism follows these steps:__ &rarr;


1. {:.fragment} split apart a data set into groups based on some criteria or common value
2. {:.fragment} apply a function on each group that
3. {:.fragment} combine the output of applying the function to each group into a single result

(this is referred to as split-apply-combine; [check out some diagrams](https://www.google.com/search?q=split+combine+apply&rlz=1C5CHFA_enUS775US778&sxsrf=ACYBGNRm7BX2psswlDDNd9TqtON4dA9PPg:1570112757257&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjY75zppYDlAhXxUN8KHXbWCdgQ_AUIEigB&biw=1440&bih=766&dpr=2)!)
{:.fragment}

</section>

<section markdown="block">
## `.groupby` Example

__The `groupby` method on a DataFrame or Series allows this...__


First split apart the data in a column into groups based on a key... in this case, the key is the value in the Year column.

```
grouped = df['Salary'].groupby(df['Year'])
```
{:.fragment}

Then... apply a function and combine the results:
{:.fragment}

```
grouped.mean()
```
{:.fragment}

```
Year
2016    87437.5
2017    89147.5
2018    91482.5
Name: Salary, dtype: float64
```
{:.fragment}

```
# as a one-liner
df['Salary'].groupby(df['Year']).mean()
```
{:.fragment}
</section>

<section markdown="block">
## Grouping and Applying on All Columns

__This can also be done on a DataFrame rather than just a series.__ &rarr;

In this case, we get the function applied to each column, rather than just a single column... but the grouping by key still occurs...

```
df.groupby(df['Year']).mean()
```
{:.fragment}

Notice that some columns are left out... in the case of `mean`, `Title` was not included as it was not numeric.
{:.fragment}
</section>

<section markdown="block">
## Aggregation Functions

__A list of methods that can be used with groupby__ &rarr;

* count
* sum, prod
* mean, median 
* std, var 
* min, max 
* first, last
</section>

