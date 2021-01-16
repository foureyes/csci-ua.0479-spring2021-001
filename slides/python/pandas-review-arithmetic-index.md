---
layout: slides
title: "Pandas Indexing, Operations Review"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## 🐼🐼🐼🐼🐼

__Whew. That was _a lot_ of pandas we've been through.__

The material was a little _dry_ (😴), so to review, let's try put a little context around it:

* {:.fragment} [Wikipedia - List of the largest information technology companies](https://en.wikipedia.org/wiki/List_of_the_largest_information_technology_companies#cite_note-5)
* {:.fragment} (which in turn sourced its data from official earnings reports, other stats sites, etc.)
* {:.fragment} (we're just using it to practice some 🐼)
* {:.fragment} some interesting data that It contains includes:
	* {:.fragment} company name
	* {:.fragment} revenue from 2017 
	* {:.fragment} number of employees
	* {:.fragment} location



</section>
<section markdown="block">
## All The Data

__Copy and paste the following into your notebook / interactive shell.__ &rarr;

* this will create a `DataFrame`
* ...containing some slightly modified (to compact) data from the Wikipedia article mentioned previously

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
## 👀

__It should look like this__ &rarr;

<pre><code data-trim contenteditable>
         revenue    fy  employees   mcap                 location
apple     $229.2  2017     123000  $1100            Cupertino, US
samsung   $211.9  2017     320671   $284       Suwon, South Korea
amazon    $177.8  2017     566000   $985              Seattle, US
foxconn   $154.7  2017    1300000    $66  New Taipei City, Taiwan
alphabet  $110.8  2017      80110   $834        Mountain View, US
</code></pre>
</section>

<section markdown="block">
## Removing Columns

__Looking at the data, `fy` (fiscal year), is the same throughout. We're also not going to use the `mcap` (market cap) column__ &rarr;

Name two ways to remove these two (`fy`, `mcap`) columns <span class="hl">in place</span>:

* {:.fragment} use the `del` operator
* {:.fragment} use the `.drop` method

<pre><code data-trim contenteditable>
del c['mcap']
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
c.drop('fy', axis=1, inplace=True)
# ... (default is to make a copy, so 
# use keyword argument, inplace)
# btw, can also use axis='columns'
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Retrieving Values

__Now let's try getting some values out of this `DataFrame`.__ &rarr;


1. {:.fragment} Only show me the employees column
	<pre class="fragment"><code data-trim contenteditable>
c['employees']	
</code></pre>
2. {:.fragment} What was Amazon's revenue in 2017?
	<pre class="fragment"><code data-trim contenteditable>
c['revenue']['amazon']
c.loc['amazon', 'revenue']
</code></pre>

</section>

<section markdown="block">
## Retrieving Values Continued

1. {:.fragment} Show the revenue and location of rows apple through amazon
	<pre class="fragment"><code data-trim contenteditable>
c[:3][['revenue', 'location']] 
c.loc['apple':'amazon', ['revenue', 'employees']]
# inclusive when using labels for slicing!
</code></pre>
	* {:.fragment} note that `.iloc` can do the same thing by position:
	* {:.fragment} `c.iloc[:3, [0, 2]]`
2. {:.fragment} Only get the names of the companies... (or rather, how do you get the row labels?)
	<pre class="fragment"><code data-trim contenteditable>
c.index
</code></pre>

</section>

<section markdown="block">
## Adding Columns!?

__Hm. It looks like we're missing some location data for the US based companies. Let's add a `state` column__ &rarr;

* {:.fragment} it's ok to have missing values for companies that don't have a `state` associated with it
* {:.fragment} google and apple in `CA`, and amazon in `WA`
* {:.fragment} _hint_: think about label alignment...

<pre><code data-trim contenteditable>
c['state'] = pd.Series({'apple': 'CA', 'amazon': 'WA', 'alphabet': 'CA'})
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Arithmetic and Comparisons/Selections

1. {:.fragment} Only show the `employees` column... but do it so that the amount is in hundreds of thousands (for example 200000 should be 2... any precision is ok)
	<pre class="fragment"><code data-trim contenteditable>
c['employees'] / 100000	
</code></pre>
{:.fragment}
2. {:.fragment} Show the companies that have less than 200,000 employees:
	<pre class="fragment"><code data-trim contenteditable>
c[c['employees'] < 200000]	
</code></pre>

</section>

<section markdown="block">
## One Last Selection

__Now that we've added state... maybe we want to show only the companies that have a state associated with it__ &rarr;

Show all the companies that have a _missing/NA/NaN_ value
{:.fragment} 

<pre class="fragment"><code data-trim contenteditable>
c[c['state'].isnull()]	
</code></pre>
{:.fragment}


</section>
<section markdown="block">
## Speaking of NaN

__If you have missing values, then it may make sense to fill them in with another default value__ &rarr;

Use the `.fillna` method to do this (first argument is value to use to replace `NaN` with):
{:.fragment}


<pre><code data-trim contenteditable>
c['state'] = c['state'].fillna('')
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Vectorized String Methods

__In addition to the arithmetic operators we've used, we can also use [vectorized string operations on `Series`](http://pandas.pydata.org/pandas-docs/stable/text.html#text-string-methods)__ &rarr;

* {:.fragment} methods are called off of `str` attribute
* {:.fragment} some examples include:
	* {:.fragment} `str.upper`: c['location'] = c['location'].str.upper()
	* {:.fragment} `str.split` returns a `Series` of lists for each value it works on
	* {:.fragment} the result of each split can be accessed through `.str`
	* {:.fragment} `c['country'] = c['location'].str.split(',').str[-1]`

</section>

<section markdown="block">
## Rearranging

__I'd like to rearrange the the table a little bit:__ &rarr;

* {:.fragment} move apple to the end of the list
* {:.fragment} swap location and state
* {:.fragment} while we're at it, why don't we add another row for microsoft (with NaN values filled in) (ok if it's at the end, after apple)

<pre><code data-trim contenteditable>
c.reindex(index=[*(list(c.index)[1:]), 'apple', 'microsoft'],
        columns=['revenue', 'employees', 'state', 'location'])
</code></pre>
{:.fragment}

</section>
<!--* -->


