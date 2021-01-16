---
layout: slides
title: "Quick Guide on Combining DataFrames"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## "Joining" DataFrames

`pd.merge` joins data from one DataFrame with another based on common column values. The default result is the intersection of rows with matching column values, with all columns merged:

```
a = pd.DataFrame([[2, 20], [4, 40], [6, 60], [8, 80]],
                 columns=['k', 'col1'])
b = pd.DataFrame([[4, 2], [4, 3], [8, 7]], 
                 columns=['k', 'col2'])
```

```
# take all rows that have a matching value in 
# column k ...  and put data togther!
pd.merge(a, b, on='k')

# result will have col1 and col2, but one row will
# be left out
```
{:.fragment}
</section>

<section markdown="block">
## Merge with Outer


__If a union is desired rather than intersection of values for a column, then pass in a keyword argument, `how`__ &rarr;

```
pd.merge(a, b, on='k', how='outer')
```
{:.fragment}

Those familiar with SQL may notice that:
{:.fragment}

* {:.fragment} regular merge is _like_ an inner join
* {:.fragment} outer is, as the name implies, an outer join
* {:.fragment} (we'll go over these later, of course)
</section>

<section markdown="block">
## Merge how? 🤔

__`merge` has other possible values for `how`__ ... the full list of possible values is &rarr;

* {:.fragment} `'left'`: include all keys from the first (left) DataFrame, even if they don't exist in second
* {:.fragment} `'right'`: include all keys from the second (right) DataFrame, even if they don't exist in first
* {:.fragment} `'outer'`: union of keys from both DataFrames
* {:.fragment} `'inner'`: intersection of keys from both DataFrames (default)


These can be found in the [official pandas docs for `merge`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
{:.fragment}

</section>

<section markdown="block">
## "Stacking"

__To stack DataFrames based on column name, `pd.concat` can be used__ &rarr;

```
d1 = pd.DataFrame(np.arange(9).reshape((3, 3)),
                columns=list('abc'))
d2 = pd.DataFrame(np.arange(10, 19).reshape((3, 3)),
                columns=list('abc'))
```
{:.fragment}

`pd.concat` takes a list of pandas objects, like DataFrames...
{:.fragment}

```
pd.concat([d1, d2]) 

# yields d1 and d2 stacked together by column name
```
{:.fragment}

</section>
