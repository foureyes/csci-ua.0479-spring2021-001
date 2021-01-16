---
layout: slides
title: "Joins"
---

<script src="../../resources/js/table.js"></script>
<link rel="stylesheet" href="../../resources/css/data-table.css" type="text/css" media="screen" title="no title" charset="utf-8">

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Reviewing Constraints 

__If you were tasked with storing course data in your database, what table name, fields, types, and constraints would you use?__ &rarr;

One potential solution might be:
{:.fragment}

<pre><code data-trim contenteditable>
create table course (
  course_number text,
  section_number text,
  semester text,
  year smallint constraint year_after_found check (year > 1831),
  title text,
  description text,
  primary key (course_number, section_number, semester, year)
);
</code></pre>
{:.fragment}

* note the composite primary key as a table level constraint
* the generic constraint on year 
{:.fragment}


</section>

<section markdown="block">
## Let's Add Some Rows!

__Based on the previous table definition, which of these queries will fail with an error, and which ones will work?__ &rarr;

<pre><code data-trim contenteditable>
insert into course values 
  ('0480', '008', 'spring', 1800, 'ait', 'web stuff');
insert into course values 
  ('0480', '008', 'spring', 2020, 'ait', 'web stuff');
insert into course values 
  ('0480', '001', 'spring', 2020, 'e-sports', 'video games!');
insert into course 
  (course_number, semester, year, title) 
values 
  ('0479', 'spring', 2020, 'dma');
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Foreign Keys Reviewed

__Now let's try to model a user on a web site... and their associated addresses__ &rarr;

<pre><code data-trim contenteditable>
create table web_user (
  web_user_id serial primary key,
  username varchar(8) not null unique,
  email text
);
</code></pre>
{:.fragment}


<pre><code data-trim contenteditable>
insert into web_user (username, email) values ('jversoza', 'jversoza@foo.bar.baz');
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## User and Addresses Continued

__...and the associated address table__ &rarr;

<pre><code data-trim contenteditable>
create table address (
  address_id serial primary key, 
  street text,
  city text,
  state varchar(2),
  zip text, 
  web_user_id integer references web_user(web_user_id)
);
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
insert into address (street, city, state, zip, web_user_id) values ('123 a st', 'brooklyn', 'ny', '11211', 1)
;
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Dropping or Deleting

__What do you think will happen if these queries are run?__ &rarr;

<pre><code data-trim contenteditable>
insert into address 
  (street, city, state, zip, web_user_id) 
values 
  ('123 a st', 'brooklyn', 'ny', '11211', 5);
delete from web_user;
drop table web_user;
delete from address;
drop table address;
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## A Preview...

__How can we view a person and their related addresses__ &rarr;

<pre><code data-trim contenteditable>
select * from web_user u 
	inner join address a on u.web_user_id = a.web_user_id;
</code></pre>
{:.fragment}

</section>
<section markdown="block">
## Joins

__A relational algebra operation implemented in SQL... that combines columns from one or more tables__

</section>

<section markdown="block">
## Genre Table

<pre><code data-trim contenteditable>
CREATE TABLE genre (
	genre_id integer,
	name varchar(20),
	description text,
	PRIMARY KEY (genre_id)
);
</code></pre>
</section>

<section markdown="block">
## Genre Data

<pre><code data-trim contenteditable>
 genre_id |      name       |                description
----------+-----------------+-------------------------------------------
        1 | Comedy          | LOL
        2 | Drama           | Such feels.
        3 | Fantasy         | Swords. And maybe fairies too.
        4 | Horror          | Ghosts, goblins, and other spooky things.
        5 | Science Fiction | Robots and stuff.
        6 | Super Hero      | Mostly capes.
        7 | Thriller        | Close. Your. Eyes.
</code></pre>

</section>

<section markdown="block">
## Movie Table

<pre><code data-trim contenteditable>
CREATE TABLE movie (
	movie_id serial,
	title varchar(50) NOT NULL,
	year smallint NOT NULL,
	runtime smallint NOT NULL, 
	genre_id integer REFERENCES genre (genre_id),
	PRIMARY KEY (movie_id)
);
</code></pre>
</section>

<section markdown="block">
## Movie Data

<pre><code data-trim contenteditable>
 movie_id |                 title                  | year | runtime | genre_id
----------+----------------------------------------+------+---------+----------
        1 | Alphaville                             | 1965 |      99 |
        2 | La Montaña Sagrada (The Holy Mountain) | 1973 |      99 |
        3 | Dune                                   | 1984 |     136 |        5
        4 | Point Break                            | 1991 |     122 |        7
        5 | Strange Days                           | 1995 |     145 |        5
        6 | 2046                                   | 2004 |     122 |        2
        7 | Hellboy                                | 2004 |     122 |        6
        8 | Los Abrazos Rotos (Broken Embraces)    | 2009 |     128 |        7
        9 | Blade Runner 2049                      | 2017 |     163 |        5
       10 | Wonder Woman                           | 2017 |     141 |        6
       11 | Shape of Water                         | 2018 |     123 |        3
</code></pre>
</section>
<section markdown="block">
## Cross Join

__Cartesian product__

* {:.fragment} all rows from one table combined with each row from another table
* {:.fragment} results in n * m rows

<pre><code data-trim contenteditable>
SELECT * FROM movie 
	CROSS JOIN genre;
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Inner Join

__Combines rows from one table and another based on matching column values__ &rarr;

* {:.fragment} condition for matching column is the join predicate
* {:.fragment} _commonly_ used!


<pre><code data-trim contenteditable>
SELECT title, name 
	FROM movie 
	INNER JOIN genre on movie.genre_id = genre.genre_id;
</code></pre>
{:.fragment}

... can also be done with `WHERE` clause (implicit join)
{:.fragment}

<pre><code data-trim contenteditable>
SELECT title, name 
	FROM movie, genre 
	WHERE movie.genre_id = genre.genre_id;
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## ⚠️ Here There Be Nulls! 

__What happened to the `movie` rows that had a `null` `genre_id`__?

* {:.fragment} they weren't included in the results!
* {:.fragment} that implies that when a column that can have a `null` value is used in the join predicate, some rows may be omitted from the query result

</section>
<section markdown="block">
## Other Alternatives

__An `INNER JOIN` where the join predicate involves equality can be written with a `USING` clause__ &rarr;

<pre><code data-trim contenteditable>
SELECT title, name 
	FROM movie 
	INNER JOIN genre USING (genre_id);
</code></pre>
{:.fragment}

A __natural join__ performs an inner join implicitly on matching column names (v risk, tho! ⚠️)
{:.fragment}

<pre><code data-trim contenteditable>
SELECT * FROM movie NATURAL JOIN genre;
</code></pre>
{:.fragment}


</section>

<section markdown="block">
## OUTER JOINS

__Same as inner, but include everything in the first (left) table: `LEFT OUTER JOIN`__ &rarr;

<pre><code data-trim contenteditable>
SELECT * FROM movie LEFT OUTER JOIN genre ON movie.genre_id = genre.genre_id;
</code></pre>

__Same as above, but include everything in second (right) table: `RIGHT OUTER JOIN`__ &rarr;

<pre><code data-trim contenteditable>
SELECT * FROM movie RIGHT OUTER JOIN genre ON movie.genre_id = genre.genre_id;
</code></pre>

__Both! `FULL OUTER JOIN`__ &rarr;

<pre><code data-trim contenteditable>
SELECT * FROM movie FULL OUTER JOIN genre ON movie.genre_id = genre.genre_id;
</code></pre>

</section>

<section markdown="block">
## Self Joins

__Which movies were made in the same year, shown as pairs?__ &rarr;

This is a tough one to answer, as we'd have to compare the table to itself to see if years are equal. __What?__ &rarr;


1. {:.fragment} use the table to join on itself
2. {:.fragment} do this with an inner join
3. {:.fragment} the inner join should be on year...
4. {:.fragment} so that we only get rows with years that match each other

</section>

<section markdown="block">
## Self Join Attempt #1

<pre><code data-trim contenteditable>
SELECT a.title, b.title, a.year, b.year 
FROM movie as a 
INNER JOIN movie as b on a.year = b.year 
ORDER BY a.year, a.title, b.title;
</code></pre>

Uh... there's something weird about the result of this. __What do you think will happend?__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
title           | title          | year | year
---------------------------------+----------------------------------------+------+------
 Alphaville     | Alphaville     | 1965 | 1965
 .
 .
 Strange Days   | Strange Days   | 1995 | 1995
 2046           | 2046           | 2004 | 2004
 2046           | Hellboy        | 2004 | 2004
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Self Join Attempt #2

Well. __That didn't work__ 😞... since we're matching on year, we're getting movies that match themselves on both tables!

__What could we do to fix this?__ &rarr;

* {:.fragment} let's try filtering the rows with a `WHERE` clause
* {:.fragment} this clause should only show rows that don't have the same id 
* {:.fragment} so that we don't the same title in both title columns
* {:.fragment} `WHERE a.movie_id <> b.movie_id`
</section>
<section markdown="block">
##  Self Join Attempt #2 Continued

__OK... so here's what it looks like now...__ &rarr;

<pre><code data-trim contenteditable>
SELECT a.movie_id, a.title, b.movie_id, b.title, a.year
FROM movie as a INNER JOIN movie as b ON a.year = b.year
WHERE a.movie_id < b.movie_id
ORDER BY a.year, a.movie_id, b.movie_id;
</code></pre>

Works _somewhat_ ... we still have a minor problem 😐, though!
{:.fragment}

<pre><code data-trim contenteditable>
 movie_id |       title       | movie_id |       title       | year
----------+-------------------+----------+-------------------+------
        6 | 2046              |        7 | Hellboy           | 2004
        7 | Hellboy           |        6 | 2046              | 2004
        9 | Blade Runner 2049 |       10 | Wonder Woman      | 2017
       10 | Wonder Woman      |        9 | Blade Runner 2049 | 2017
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Self Join Attempt #3 

The previous attempt got rid rows with the same title in both `a` and `b`, but now we have twice as many rows since the duplicate rows have the titles switching columns. __What now?__ 🤔&rarr;

* {:.fragment} because we have pairs of movies, we can use the ordering of `movie_id` to get rid of duplicate, but swapped title, rows
* {:.fragment} so, now we can filter by saying: only give me rows where one movie_id is less than the other (or greater than... just not both)

<pre><code data-trim contenteditable>
SELECT a.movie_id, a.title, b.movie_id, b.title, a.year
FROM movie as a INNER JOIN movie as b ON a.year = b.year
WHERE a.movie_id < b.movie_id
ORDER BY a.year, a.movie_id, b.movie_id;
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## How Are They Related?

__In our `movie` and `genre` example, how are movie and genre related in terms of cardinality?__ 

Based on where the foreign key is (it's placed on `movie`!)...

* {:.fragment} can a movie have multiple genres (can Hellboy be both horror and fantasy)?
* {:.fragment} can a genre have multiple movies (can the sci-fi genre encompass Alphaville, Bladerunner, etc.)
* {:.fragment} ...or maybe both: can movie have multiple genres and a genre have multiple movies?

In this relationship, multiple movies can have the same genre id: for every one genre, there could be many movies (but a movie can't have more than one genre).
{:.fragment}

This is called a __one-to-many__ relationship!
{:.fragment}

</section>
<section markdown="block">
## Table Relationships

The possible cardinalities of rows in related tables are:

1. {:.fragment} one-to-many
2. {:.fragment} many-to-many
3. {:.fragment} one-to-one

(for all these cases, 0 is a possibility on the right hand side; it's trickier to ensure that there's exactly or at least one, though)
{:.fragment}

__Anyway, let's figure out where the foreign keys go to implement all of these relationships...__ &rarr;
{:.fragment}
</section>

<section markdown="block">
## One to Many

If you have a __foreign key__ in your table .... it will be the many side in a __one-to-many__ relationship. &rarr;


* {:.header .colspan} movie
* {:.header} movie_id (pk), title, genre_id (fk)
* 1, Dune, 57
* 2, A Quiet Place, 57
* 3, 2046, 58
{:.fragment}
{:.table}

* {:.header .colspan} genre
* {:.header} genre_id (pk), name
* 57, Sci-Fi
* 58, Drama
{:.fragment}
{:.table}

* {:.fragment} rows in `movie` can reference the same `genre_id` 
* {:.fragment} (both Dune and a Quiet Place have 57 listed as the related genre id) 
* {:.fragment} ... meaning __one__ `genre` can have __many__ `movie`s

</section>


<section markdown="block">
## One to One

__Making sure that there's a one-to-one (or more exactly one to... zero or one) is a bit tricky__ &rarr;


* {:.header .colspan} user
* {:.header} user_id (pk), username, profile_id (fk __unique__)
* 1, alice, 34
* 2, bob, 35
{:.fragment}
{:.table}

* {:.header .colspan} profile
* {:.header} profile_id (pk), avatar_url
* 34, foo.bar/baz.png
* 35, ne.at.io/hi.gif
{:.fragment}
{:.table}

Uh... isn't this the same as one-to-many? 
{:.fragment}

* {:.fragment} if we put a __unique__ constraint on the foreign key, that means a value for genre id can only occur once in `movie` 
* {:.fragment} this means there can be either no associated profile or only associated profile for a __one-to-one__ relationship.
* {:.fragment} if you want exactly one-to-one, you can put an fk in each table and use [deferred constraints in a transaction to insert rows in each table](https://www.postgresql.org/docs/12/sql-set-constraints.html)
</section>

<section markdown="block">
## Many to Many

__What if we wanted movies to have many genres, and genres to have many movies?__

* Dune is both Sci-Fi and Drama,
* Sci-Fi is a genre that both Dune and A Quiet Place have
{:.fragment}


Maybe `movie` could contains `genre_id` and  `genre` can contain `movie_id`
{:.fragment}

🙅‍♀️... nope this __isn't the best solution__! why not?
{:.fragment}

You'd have to put place duplicate rows _somewhere_:
{:.fragment}

* {:.header .colspan} movie
* {:.header} movie_id (pk), title, genre_id
* 1, Dune, 57
* 1, Dune, 58
* 2, A Quiet Place, 57
{:.fragment}
{:.table}

* {:.header .colspan} genre
* {:.header} genre_id (pk), name, movie_id
* 57, Sci-Fi, 1
* 57, Sci-Fi, 2
* 58, Drama, 1
{:.fragment}
{:.table}


</section>


<section markdown="block">
## Many to Many II 


__For many-to-many, create a third table that houses ids of both other tables__ (so only ids are duplicated) &rarr;


* {:.header .colspan} movie
* {:.header} movie_id (pk), title
* 1, Dune
* 2, A Quiet Place
* 3, 2046
{:.fragment}
{:.table}

* {:.header .colspan} movie_genre
* {:.header} movie_id (fk), genre_id (fk)
* 1, 57
* 1, 58
* 2, 58
{:.fragment}
{:.table}

* {:.header .colspan} genre
* {:.header} genre_id (pk), name
* 57, Sci-Fi
* 58, Drama
{:.fragment}
{:.table}

* {:.fragment} now, Dune has 2 genres and Drama has 2 movies
* {:.fragment} why not just set an fk in each table? that would lead to duplicate rows in either table!
* {:.fragment} sometimes this is called a __join table__; other names include __association__ and __junction__ table
* {:.fragment} this __join table__ can have additional columns, but minimally, the pk of both other tables
</section>


{% comment %}
many to many


{% endcomment %}
