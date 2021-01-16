---
layout: slides
title: "Explain / Analyze, Indexes"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## Y SO SLOW?

__So far, we've been dealing with relatively small data sets (10K rows max, right?), and just a handful of tables at most__ &rarr;

* {:.fragment} as our data increases...
* {:.fragment} as we add more tables...
* {:.fragment} ... and as our queries get more and more complex

Our queries will take longer to complete 😮! Oh, _what to do about performance issues_?...
{:.fragment}

</section>


<section markdown="block">
## Executing a Query

__A given SQL query can _actually_ be executed in different ways, but still result in the same set of rows__ &rarr;

* {:.fragment} for example, inner joins are commutative
* {:.fragment} ...or using different ways to find data (sequentially scanning or using an index)

PostgreSQL's query planner will _try_ to look at each possible execution plan and use the fastest one! 👟
{:.fragment}

(there are some queries, such as ones with several joins,  where it's not possible to examine every plan)
{:.fragment}

</section>
<section markdown="block">
## Plz Explain


__If you'd like to get a peek into what the query planner is going to do, you can use `EXPLAIN`__ &rarr;

* {:.fragment} simply prefix your query with `EXPLAIN`
* {:.fragment} `EXPLAIN SELECT * FROM foo;`

(Note that `EXPLAIN` is not part of standard SQL, so not all platforms may support it, or they may use a different syntax for examining a query plan)
{:.fragment}

</section>

<section markdown="block">
## EXPLAIN Explained

__Using `EXPLAIN` on a query breaks down a the steps that Postgres will use to execute it__ &rarr;


* every step will have a cost (a _relative_ unit) `cost=nnnn..mmmm`
	* the first number is the startup cost (time prior to retrieving data for looking at indexes, joining tables, etc.)
	* for sequential scans, startup is 0
	* the second number is the total cost 
* every line preceded by an arrow is an _actual_ step (other lines are informational)
* explain on its own will not execute the query
* generally, read from innermost to outermost, top to bottom
{:.fragment}

</section>
<section markdown="block">
## EXPLAIN Example

__Example query plan:__

<pre><code data-trim contenteditable>
EXPLAIN SELECT * FROM web_user WHERE first='tegan';
</code></pre>

<pre><code data-trim contenteditable>
                                 QUERY PLAN
----------------------------------------------------------------------------
 Gather  (cost=1000.00..5739.49 rows=124 width=78)
   Workers Planned: 2
   ->  Parallel Seq Scan on web_user  (cost=0.00..4727.09 rows=52 width=78)
         Filter: ((first)::text = 'tegan'::text)
(4 rows)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## WAT?

__What does this tell us?__ &rarr;

<pre><code data-trim contenteditable>
 Gather  (cost=1000.00..5739.49 rows=124 width=78)
   Workers Planned: 2
   ->  Parallel Seq Scan on web_user  (cost=0.00..4727.09 rows=52 width=78)
</code></pre>

...specifies how the postgres will find the data:

* {:.fragment} `Seq Scan` - scan the whole table 
* {:.fragment} `Gather` and `Parallel Seq Scan` - run multiple queries in parallel to execute original query
	* the `Gather` portion shows how many workers are available for parallelization


</section>

<section markdown="block">
## EXPLAIN ANALYZE

__Adding `ANALYZE` will show the query plan AND run the query__  &rarr;

* this shows the number of rows
* ...and execution time
{:.fragment}

Let's see what this may look like....
{:.fragment}

<pre><code data-trim contenteditable>
EXPLAIN ANALYZE SELECT * FROM web_user WHERE first='tegan';
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## EXPLAIN ANALYZE Continued

<pre><code data-trim contenteditable>
 Gather  (cost=1000.00..5739.49 rows=124 width=78) (actual time=10.928..185.362 rows=149 loops=1)
   Workers Planned: 2
   Workers Launched: 2
   ->  Parallel Seq Scan on web_user  (cost=0.00..4727.09 rows=52 width=78) (actual time=8.456..173.988 rows=50 loops=3)
         Filter: ((first)::text = 'tegan'::text)
         Rows Removed by Filter: 83284
 Planning time: 1.319 ms
 Execution time: 187.264 ms
</code></pre>

<pre><code data-trim contenteditable>
(8 rows)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
Time: 192.123 ms
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Making Lots of Data

__Let's see this at work by making a bunch of data__

We'll create a couple of tables and generate data:

* {:.fragment} `web_user`: ~250k rows
* {:.fragment} `session`: ~1m rows

To do this, we'll create a few functions for generating random names and email addresses:
{:.fragment}

* {:.fragment} `generate_names`
* {:.fragment} `generate_domain`

</section>

<section markdown="block">
## web_user and session Tables

<pre><code data-trim contenteditable>
select min(user_id) from web_user;
drop table if exists web_user;
create table web_user (
  user_id integer primary key,
  first varchar(255) not null,
  last varchar(255) not null,
  active boolean not null default FALSE,
  email varchar(255) not null,
  password varchar(255) not null
);
</code></pre>

<pre><code data-trim contenteditable>
create table session (
  session_number integer,
  session_id varchar(255) primary key,
  user_id integer references web_user(user_id) on delete cascade
);
</code></pre>
</section>

<section markdown="block">
## generate_name

<pre><code data-trim contenteditable>
-- hardcode some names for first_names and last_names
create function generate_name() returns varchar[] as $$
declare
	first_names varchar[] := array[...];
	last_names varchar[] := array[...];
begin
  return array[
    first_names[1 + floor(random() * array_length(first_names, 1))],
    last_names[1 + floor(random() * array_length(last_names, 1))]
  ];
end;
$$
language plpgsql;
</code></pre>

</section>

<section markdown="block">
## generate_domain

<pre><code data-trim contenteditable>
create or replace function generate_domain() returns varchar as $$
declare
  tlds varchar[] := array['com', 'com', 'com','net','me','org', 'com','net','me','org','com','net','me','org', 'es', 'us', 'uk', 'ru', 'jp', 'cn', 'eu'];
  domain varchar;
begin
  with syllables as (
      select 0 as label,
	         --TODO hardcode domain name words
             unnest(array[...]) as syllable
      )
  select string_agg(syllable, '') into domain
  from
      (select * from syllables order by random() limit (1 + floor(random() * 4)::int)) as foo
  group by label;
  return domain || '.' || tlds[1 + floor(random() * array_length(tlds, 1))];
end;
$$
language plpgsql;
</code></pre>

</section>

<section markdown="block">
## Let's Add Some Data!

__Create 250K entries for `web_user`:__ &rarr;

<pre><code data-trim contenteditable>
insert into web_user
select user_id,
       name[1] as first,
       name[2] as last,
       case when random() > 0.5 then TRUE else FALSE end as active,
       substring(name[1], '^.') || name[2] || '@' || generate_domain() as email,
       md5(random()::text) as password
from
     (select generate_series(1, 250000) as user_id, generate_name() as name) as name_temp;
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## And for Session

__Add 2m rows for the `session` table__ &rarr;

<pre><code data-trim contenteditable>
insert into session (session_number, session_id, user_id)
  (select generate_series(1, 2000000), 
          md5(random()::text), 
		  1 + floor(random() * 250000))
on conflict do nothing;
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Try Running

__Here are some queries to run against `web_user`__ &rarr;

<pre><code data-trim contenteditable>
select * from web_user where first = 'tegan';
select * from web_user where email = 'use email from above';
</code></pre>
{:.fragment}

__Let's see what `EXPLAIN ANALYZE` says__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
explain analyze select * from web_user where first = 'tegan';
explain analyze select * from web_user where email = 'use email from above';
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## MAKE IT FASTER

__A simple way to get some performance gains is to add indexes to columns__ &rarr;

* {:.fragment} `CREATE INDEX indexname ON tablename (columnname);`
* {:.fragment} __Let's try it!__ &rarr;
	* {:.fragment} `create index email_index on web_user (email);`

__Was it faster?__ &rarr;
{:.fragment}

* {:.fragment} ✅OH YES, it was....
* {:.fragment} but how? _magic_? 🧙✨
	* {:.fragment} (no, B-Trees 🌲🌳)

</section>

<section markdown="block">
## What's an Index

__So really, what's an index then, and how does it make things faster?__ &rarr;

* {:.fragment} it's a structure in your database that contains indexed table data
* {:.fragment} which means that _it takes up space_, so that you can locate data faster
* {:.fragment} it also has to be created (and updated) based on the data in the table and the changes that occur

</section>

<section markdown="block">
## Index Analogy

__Think of a database index as if it were an index in a book 📖__ &rarr;

* {:.fragment} it helps you locate something in the book
* {:.fragment} it takes up space at the end of the book
* {:.fragment} if the contents of the book were changed, you'd have to change the index too

</section>

<section markdown="block">
## How?

The data in a table is not stored sequentially in physical storage...

* {:.fragment} so, one way to deal with this is to use __doubly linked lists__ for logical ordering
* {:.fragment} and a [B-Tree](https://en.wikipedia.org/wiki/B-tree) (binary search tree that can have more than two nodes) to quickly find one these nodes (which are leaf nodes in the tree)

[see Use the Index, Luke](https://use-the-index-luke.com/sql/anatomy/the-tree)
{:.fragment}

</section>


<section markdown="block">
## MOAR Indexes

__PostgreSQL has many different types of indexes__ (though B-Tree is the most common, and is general purpose)

__There are other index types for different columns/queries__ &rarr;

* {:.fragment} `brin` - for large tables where b-tree would take up too much space
* {:.fragment} `gin` - geared towards columns with composite values, like json or arrays
* {:.fragment} `gist` - columns that have data that may overlap (like geospacial data)

</section>

<section markdown="block">
## No Index?

__What are some drawbacks to using indexes?__ &rarr;

* {:.fragment} take up more space
* {:.fragment} operations that change data may take longer (insert, update, delete)
* {:.fragment} query planner might not actually use it (????)
	* {:.fragment} if your queries return large result sets, then sequential scan is actually more efficient
</section>
