---
layout: slides
title: "Having and Between"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}


### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## GROUP BY 

Some additional notes on GROUP BY.

* `GROUP BY` can be added after `FROM` or `WHERE`
* it's used to group the rows return from a `SELECT` (after `WHERE` filters)
* an aggregate function (`COUNT`, `SUM`, `MAX`, `MIN`, `AVG`) may be applied to each group
* it is not the same as `DISTINCT` (which only gives back unique values, no aggregation)

Check out the [official docs on GROUP BY](https://www.postgresql.org/docs/current/static/sql-select.html#SQL-GROUPBY) as well as [some examples](http://www.postgresqltutorial.com/postgresql-group-by/).

</section>


<section markdown="block">
## GROUP BY Example

<pre><code data-trim contenteditable>
-- group by country name
-- show the highest concentration for each group
SELECT country, MAX(concentration) AS c 
    FROM product 
    GROUP BY country 
    ORDER BY c desc;
</code></pre>
</section>

<section markdown="block">
## GROUP BY Errors

__(from the docs) when using GROUP BY__ &rarr;

* it's invalid for the `SELECT` list to reference ungrouped columns 
* ... unless the ungrouped column appears as an argument to an aggregate functions
* (otherwise, there would be more than one possible value to return for an ungrouped column)
* (note that an ungrouped column can also appear when the `GROUP BY` column is a primary key)

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
## HAVING

[official postgres docs on HAVING](https://www.postgresql.org/docs/current/static/sql-select.html#SQL-HAVING)
HAVING eliminates group rows that do not satisfy the condition. HAVING is different from WHERE: WHERE filters individual rows before the application of GROUP BY, while HAVING filters group rows created by GROUP BY. Each column referenced in condition must unambiguously reference a grouping column, unless the reference appears within an aggregate function or the ungrouped column is functionally dependent on the grouping columns.

The presence of HAVING turns a query into a grouped query even if there is no GROUP BY clause. This is the same as what happens when the query contains aggregate functions but no GROUP BY clause. All the selected rows are considered to form a single group, and the SELECT list and HAVING clause can only reference table columns from within aggregate functions. Such a query will emit a single row if the HAVING condition is true, zero rows if it is not true.

Currently, FOR NO KEY UPDATE, FOR UPDATE, FOR SHARE and FOR KEY SHARE cannot be specified with HAVING.
</section>

<section markdown="block">
## BETWEEN
[official postgres docs on BETWEEN](https://www.postgresql.org/docs/9.1/static/functions-comparison.html)
</section>