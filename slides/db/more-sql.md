---
layout: slides
title: "More SQL: Joins, Subqueries, Functions"
---


<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Selecting with a Subquery

__The columsn in a `SELECT` statement can be an expression... even a  subquery!__ &rarr;

<pre><code data-trim contenteditable>
SELECT 5 + 5;
-- 10

SELECT (SELECT 5 + 5) = (SELECT 7 + 3);
-- t (true)
</code></pre>

</section>
<section markdown="block">
## Inserting with a Subquery

__A subquery can be used in an `INSERT` to create data without hardcoding values__ &rarr;

Syntax:

<pre><code data-trim contenteditable>
INSERT INTO table_name (column_name,...)
subquery;
</code></pre>

* note that values can be omitted!
* subquery columns must match column list!

[see docs on insert](https://www.postgresql.org/docs/current/sql-insert.html)
</section>


<section markdown="block">
## FK and Deletes

__What happens when an object referenced by a foreign key is deleted?__ &rarr;

What might be some options that a database could give us?

* {:.fragment} prevent the delete from happening (because this object still references it)
* {:.fragment} delete this object too! (cascade)
* {:.fragment} set the reference to some other value (like `NULL`)

</section>

<section markdown="block">
## FK and Deletes Continued

__Postgres provides multiple options__ &rarr;


* {:.fragment} `ON DELETE RESTRICT` - immediately raise an error
* {:.fragment} `ON DELETE CASCADE` - any row referencing the deleted object will also be deleted
* {:.fragment} `ON DELETE NO ACTION` - __default__ (that is, if `ON DELETE` is not explicitly set): raise an error, but wait until end of transaction to do it
* {:.fragment} `ON DELETE SET NULL` and `ON DELETE SET DEFAULT`

See docs:
{:.fragment}

* [ON DELETE from docs (see paragraph with restricting and cascading delete)](https://www.postgresql.org/docs/9.5/ddl-constraints.html)
* [also, postgresqltutorial shows how this works when creating fk](http://www.postgresqltutorial.com/postgresql-foreign-key/)
{:.fragment}

</section>

<section markdown="block">
## Strings


* `length(text)` 
* `substring(text, pattern)`
	* regexp: greedy vs lazy

<pre><code data-trim contenteditable>
select length('foo');
select substring('Directed by Foo Bar. With Baz Qux starring as Corge', E'Directed by (.+?)\\. With')
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Arrays

__Postgres has an Array type:__ &rarr;

* {:.fragment} Array literal: 
	* `Array[1, 2, 3]`
	* also ...
	* `'{1, 2, 3}'` (as string, when setting values!)
* {:.fragment} WATCH OUT: array indexes start at 1
	* {:.fragment} `arr[1]` (first element)
* {:.fragment} they can be sliced with : syntax
	* {:.fragment} `arr[2:5]` (bounds are inclusive)
* {:.fragment} get the length with `array_length(arr, dimension)`
</section>


<section markdown="block">
## Splitting

* `regexp_split_to_array`
* `regexp_split_table`


select * from (select regexp_split_to_table('1,2,3', ',')) as foo;
</section>
