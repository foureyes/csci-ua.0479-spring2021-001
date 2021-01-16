---
layout: slides
title: "Aggregation / Group By"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

	

<section markdown="block">
## `GROUP BY` and Aggregate Functions

__Adding a `GROUP BY` clause allows the grouping of rows and the application of aggregate functions on each groups__ &rarr;

* {:.fragment} the `GROUP BY` clause goes after `FROM` and `WHERE`, and must be followed by the column name(s) to form groups with
* {:.fragment} it's used to group the rows __after__ rows are filtered out by `WHERE`
* {:.fragment} an aggregate function can be applied to each group
* {:.fragment} not the same as `DISTINCT` (which only gives back unique values, no aggregation)


See the [documentation for `GROUP BY`](https://www.postgresql.org/docs/10/static/sql-select.html#SQL-GROUPBY)
{:.fragment}
</section>

<section markdown="block">
## Aggregate Functions

__When grouping rows with `GROUP BY`, an aggregate function can be be applied to each group (in other parts of the query such as the `SELECT` list or `ORDER BY` clause)__ &rarr;

* {:.fragment} `AVG`
* {:.fragment} `SUM`
* {:.fragment} `MAX`
* {:.fragment} `MIN`
* {:.fragment} `COUNT`

</section>

<section markdown="block">
## When Does Group By Happen?

__Reviewing the processing order of a `SELECT`, let's see where `GROUP BY` fits in__ &rarr;

1. {:.fragment} `FROM` to determine set of all possible rows to return!
2. {:.fragment} `WHERE` to filter out rows that don't match criteria
3. {:.fragment} <span class="hl">GROUP BY</span> combines rows into groups, and results of aggregate functions are computed (`HAVING` can be used to filter out groups)
4. {:.fragment} `SELECT list` to determine the  actual values of the resulting rows by evaluating expressions, resolving column names, etc.
5. {:.fragment} `DISTINCT` to eliminate duplicate rows in the output
6. {:.fragment} `ORDER BY` to sort the output rows
7. {:.fragment} `LIMIT` to restrict the output rows to a specific number

</section>

<section markdown="block">
## Example Table

__The following slides assume the following table is present with some data__ &rarr;

<pre><code data-trim contenteditable>
CREATE TABLE student(
	 netid varchar(20) PRIMARY KEY,
	 first varchar(255) NOT NULL,
	 last varchar(255) NOT NULL,
	 midterm numeric,
	 registered timestamptz DEFAULT NOW()
);
</code></pre>
</section>

<section markdown="block">
## `GROUP BY` Examples

__Group by first name, show counts for each group (for example, 5 students named alice, 3 students named bob, etc.)__ &rarr;

<pre class="fragment"><code data-trim contenteditable>
SELECT FIRST, COUNT(*) FROM student GROUP BY first;
</code></pre>

Note that it doesn't matter what column name is passed to count (and `*` works too), since we're simply counting
{:.fragment}

__Again, group by first name, but this time show the midterm average for students with same first name__ &rarr;
{:.fragment}

<pre class="fragment"><code data-trim contenteditable>
SELECT FIRST, AVG(midterm) FROM student GROUP BY first;
</code></pre>

In this case, the `midterm` column is the argument used for `AVG`
{:.fragment}
</section>

{% comment %} ` {% endcomment %}

<section markdown="block">
## Using Aggregations

__Depending on when a particular clause is processed, a group may be available to use!__ &rarr; 

For example, since `ORDER BY` is processed last, both the `GROUP BY` and `SELECT` list have already been processed, so the aliased column `c` is available in `ORDER BY`...
{:.fragment}

<pre><code data-trim contenteditable>
-- group by country name
-- show the highest concentration for each group
SELECT country, MAX(concentration) AS c 
    FROM product 
    GROUP BY country 
    ORDER BY c desc;
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## Multiple Group By Columns

__It's possible to specify multiple columns to group by.__

* groups are formed where values for __both__ columns are equal
* for example, the following query counts the number of students that have the same first name and same midterm score
	<pre class="fragment"><code data-trim contenteditable>
SELECT first, midterm, COUNT(*) FROM student GROUP BY first, midterm;
</code></pre>

* output may look something like (two people named alice scored a 90 on their midterm):
	<pre><code data-trim contenteditable>
 Alice | 90 | 2
 Alice | 71 | 1
 Bob   | 84 | 1
</code></pre>

</section>

{% comment %} comment* {% endcomment %}

<section markdown="block">
## Just Aggregates Plz!?

__No `GROUP BY`, no problem! (sort of)__ &rarr;

* {:.fragment} if an aggregate function is used, but no `GROUP BY` is present...
* {:.fragment} all selected rows form a single group... 
* {:.fragment} the aggregate function is applied to that single group

Knowing this, it's possible to to run query that applies an aggregate function on a group that includes all rows:
{:.fragment}

<pre><code data-trim contenteditable>
SELECT MAX(score) FROM student;
</code></pre>
{:.fragment}


</section>

<section markdown="block">

## Filtering Groups

__Add a `HAVING` clause after `GROUP BY` to eliminate groups that do not satisfy a condtion__ &rarr;

From the [documentation on `HAVING`](https://www.postgresql.org/docs/10/static/sql-select.html#SQL-HAVING):

* {:.fragment} "`HAVING` is different from `WHERE`:" 
* {:.fragment} "`WHERE` filters individual rows before the application of `GROUP BY`
* {:.fragment} "while `HAVING` filters group rows created by `GROUP BY`
* {:.fragment} "Each column referenced in condition must unambiguously reference a grouping column"

Only include groups that have an average score greater than 70:
{:.fragment}

<pre><code data-trim contenteditable>
SELECT FIRST, AVG(midterm) 
	FROM student 
	GROUP BY first
	HAVING AVG(midterm) > 70;
</code></pre>
{:.fragment}

</section>


<section markdown="block">
## GROUP BY Errors

__(from the docs) when using GROUP BY__ &rarr;

* {:.fragment} it's invalid for the `SELECT` list to reference ungrouped columns (columns that don't appear in `GROUP BY`)
* {:.fragment} ... unless the ungrouped column name appears as an argument to an aggregate function
* {:.fragment} otherwise, there could be more than one possible value to return for an ungrouped column... 
	* {:.fragment} what value would be the same for every member of the group!?
	* {:.fragment} there is an exception though!
	* {:.fragment} an ungrouped column can appear in the `SELECT` when the `GROUP BY` column is a primary key, since that means each group will only have 1 row in it! 😮 (but then, why even 🤔)

{% comment %}
From the actual docs
When GROUP BY is present, or any aggregate functions are present, it is not valid for the SELECT list expressions to refer to ungrouped columns except within aggregate functions or when the ungrouped column is functionally dependent on the grouped columns, since there would otherwise be more than one possible value to return for an ungrouped column. A functional dependency exists if the grouped columns (or a subset thereof) are the primary key of the table containing the ungrouped column.
{% endcomment %}
</section>

<section markdown="block">
## GROUP BY Error Example

<pre><code data-trim contenteditable>
-- group by country 
-- note that name doesn't appear in GROUP BY
-- and it's not in an aggregate
SELECT country, name, MAX(concentration) AS c 
    FROM product 
    GROUP BY country 
    ORDER BY c desc;
</code></pre>
</section>


<section markdown="block">
## Foreshadowing

Sometimes we really want ungrouped columns to appear in our query result. __One way to do this is__ &rarr;

* run the `GROUP BY` and aggregation in one query
* use that query as a subquery ...
* and join it with another query (perhaps itself!) to get the other columns
* of course, we'd have to learn joins and subqueries first... which we'll get to in a few classes


</section>


