---
layout: slides
title: "🐍 + 🐼 + 🐘"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Pyscopg2

__A quick review of a psycopg2__ &rarr;

<pre><code data-trim contenteditable>
conn = psycopg2.connect(user='joe', password='data0480', database='scratch')
cur = conn.cursor()
cur.execute('select * from artist limit 10')
result = cur.fetchall()
print(result)
</code></pre>
{:.fragment}

__What type does this give back?__ &rarr;
{:.fragment}

* {:.fragment} a list of tuples

</section>

<section markdown="block">
## Query Description

__In addition to the _actual_ query results, a description of the query can be found with by using the `.description` attribute__ &rarr;

<pre><code data-trim contenteditable>
print(cur.description)
</code></pre>
{:.fragment}

From this attribute, you can grab all of the column names from the query result:
{:.fragment}

<pre><code data-trim contenteditable>
print([col[0] for col in cur.description])
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Pandas and psycopg2

__What are some arguments to pandas DataFrames?__ &rarr;

* data in the column
* columns
* index
{:.fragment}

The query result and description from psycopg2 can be used to create a DataFrame:
{:.fragment}

<pre><code data-trim contenteditable>
import pandas as pd
df = pd.DataFrame(result, columns=[col[0] for col in cur.description])
</code></pre>
{:.fragment}

</section>



<section markdown="block">
## SQLAlchemy + pandas

__Some setup to create an `Engine` object:__ &rarr;

<pre><code data-trim contenteditable>
from sqlalchemy import create_engine
password = 'data0480'
user = "joe"
database = "scratch"
dsn = f'postgres://{user}:{password}@localhost/{database}'
engine = create_engine(dsn, echo=True)
</code></pre>
{:.fragment}

__Issuing queries and loading the result set into a `DataFrame`__ &rarr;
{:.fragment}

* {:.fragment} `pd.read_sql` - a sql query as the first argument and a SQLAlchemy `Engine` as the second
* {:.fragment} <pre><code data-trim contenteditable>
df = pd.read_sql('select * from artwork limit 3', engine)
</code></pre>

</section>

<section markdown="block">
## DataFrame to SQL

__The `df.to_sql` method can be used to insert data into a database through SQLAlchemy__ &rarr; 

First... create a `DataFrame` &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
df = pd.DataFrame([(123456, 'joe v', 'an artist'), (123457, 'foo b', 'also an artist')], columns=['artist_id', 'name', 'bio'])
</code></pre>
{:.fragment}

Then use the `DataFrame` `to_sql` method:
{:.fragment}

<pre><code data-trim contenteditable>
df.to_sql('artist', con=engine, if_exists='append', index=False)
</code></pre>
{:.fragment}

Note the keyword arguments to specify the connection, what to do if table already exists, and finally, whether or not to include the index.
{:.fragment}

</section>


{% comment %}

<section markdown="block">
## Hierarchical Indexing

With a feature called __Hierarchical Indexing__, pandas allows `DataFrames` and `Series` to have __multiple "nested" indexes__. Hierarchical Indexing is useful for:

* {:.fragment} grouping and reshaping algorithms
* {:.fragment} working with higher-dimensional data in a lower dimensional form
* {:.fragment} instead of a regular `Index` object representing a `DataFrame` or `Series` index, a Hierarchical Index is represented by a `MultiIndex` object

We won't go in-depth with `MultiIndex`; we'll just look at enough to do some basic _SQL-like_ grouping and reshaping
{:.fragment}

</section>
<section markdown="block">
## MultiIndex Example

__A quick way to create a `MultiIndex` is to use a multidimensional list as the `index`__ &rarr;
<pre><code data-trim contenteditable>
s = pd.Series(np.arange(9), 
	index=[list('aabbbcaaa'), [9, 8, 8, 7, 6, 5, 8, 1, 2]])
</code></pre>
{:.fragment}


<pre><code data-trim contenteditable>
a  3    0
   3    1
b  3    2
   2    3
   1    4
c  2    5
a  2    6
   1    7
   1    8
dtype: int64
</code></pre>
{:.fragment}



</section>

<section markdown="block">
## 

</section>
{% endcomment %}
