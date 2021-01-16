---
layout: slides
title: "Postgres and SQL Basics"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}


### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>


<section markdown="block">
## PostgreSQL Background

__Database category:__

* relational
* __AND__ "object oriented"
	* allows overloaded functions
	* table inheritance 
	* extensible type system!

(We'll only be using the relational features, though)

</section>

<section markdown="block">
## Installation

__For all platforms, you can use the [installer](https://www.postgresql.org/download/)__

* it _should_ prompt you for a username and password
* make sure you remember it (username is postgres)

__If you're on MacOS:__

* preferred installation is to use [homebrew](https://brew.sh/)
	* `brew install postgresql`
	* watch output of install, and copy command given
	* (`pg_ctl -D /usr/local/var/postgres start` # start server!)
	* super user is your username, no password if connect locally
* Linux or Windows 10 - WSL 
	* Linux - apt / pacman / etc. (super user is `postgres`)


</section>

<section markdown="block">
## Server / Client

__Installation installs both server and client:__

* server must be running in order for it to be queried
	* server will run in background when using `pg_ctl`
	* (you can close tab, and it'll still be running)
* client can be commandline or graphical (rn only use commandline)
	* `psql` - commandline client
	* pgAdmin - graphical
	* DataGrip - graphical (free with educational license)
* currently both server and client local (on same machine)
* eventually, server on remote machine!


</section>

<section markdown="block">
## Start, Stop, Restart

* `pg_ctl start` 
	* `-D datadir` - directory where postgres stores data
	* `-l filename` - where to log output
	* (on MacOS) `pg_ctl -D /usr/local/var/postgres start`
	* add `-l /usr/local/var/postgres/server.log`
* `pg_ctl stop`
* `pg_ctl restart` - stop and then start
* `pg_ctl reload` - reread config, but no need to completely stop and start again

Want to stop specifying the `-D` when starting?  ...use `export PGDATA=/foo/bar`, add export to`.bashrc` or add export to `bash_profile` ... or modify `postgresql.conf`
{:.fragment}

<span class="hl">If `pg_ctl` isn't available, then the instance installed must be managed with different tools, like `launchctl` on MacOS, the Services app on Windows, etc.!</span>
{:.fragment}

</section>

<section markdown="block">
## Configuration

* `pg_hba.conf`
	* who can access / where they can access from
	* more about permissions, roles, security in next few classes
* `postgreql.conf` (logging, data dir, etc.)
* locations:
	* `/usr/local/var/postgres/pg_hba.conf`
	* `/usr/local/var/postgres/postgresql.conf`

Or... when connected to any database through `psql`:

`SELECT name, setting FROM pg_settings WHERE category = 'File Locations';`


</section>

<section markdown="block">
## Postgres Object Hierarchy

* __templates__ - base template(s) to copy database from
* __databases__ - multiple databases allowed in one postgres instance / "cluster" 
* __schemas__ - (ANSI SQL standard) next level of organization in database
	* database -> schema -> table
	* name spacing - useful for organizing many tables
	* default schema is `public`
	* we will stick to the public schema
* __tables__
* __views__ - abstraction of table / multiple tables: merge tables and perform calculations and present data as if it were a table; typically read only
* other - languages, functions, triggers, types, sequences

</section>

<section markdown="block">
## psql

__Commandline client: `psql` (should be installed when postgres is installed)__ &rarr;

Usage `psql db_name`: where `dbName` is name of database to connect to.

Optional flags include:

* `-U`  / `--username`
* `-W` / `--password`  prompt for password
* no `db_name` uses user name as db name



</section>

<section markdown="block">
## psql Commands 

__Change database__

* `\c db_name` - connect to different database

__Informational__ (append an `S` to most of these to show system objects)

* `\l` - list databases
* `\dt` - list tables
* `\dv` list views
* `\d` - list tables and views
* `\dn` - list schemas
* `\d table_name` - describe table
* `\du` - list users


</section>

<section markdown="block">
## HALP PLZ

__The `psql` client has a lot of built-in help!__

Use `\?` to show available `psql` commands

`\h` shows help for SQL statements

* `\h STATMENT` will show documentation for _that_ statement
* for example: `\h ALTER TABLE` shows help for the `ALTER TABLE` statement
* syntax and options will be shown
* type `q` to leave help / space to go to next page

</section>

<section markdown="block">
## Naming Conventions

* double quoted table names are case sensitive
* unquoted normalizes to lowercase (maybe bad depending on your table names)
* ...so make table names and column names:
	* {:.fragment} lowercase
	* {:.fragment} avoid double quoting table names
	* {:.fragment} words separated by underscore
	* {:.fragment} descriptive
	* {:.fragment} underscore id (foo_id) for foreign keys (more on this later)
	* {:.fragment} be consistent with pluralization (always either use singular or always use plural)


</section>

<section markdown="block">
## Types

__PostgreSQL has _a lot_ of types (you can even create your own!)__. These are some high level categories where these types can fit in:

* {:.fragment} numeric
* {:.fragment} strings
* {:.fragment} date and time
* {:.fragment} _other_

Note that as we examine types, we'll use:
{:.fragment}

* {:.fragment} `SELECT` statements to run operations and functions without tables (!?)
* {:.fragment} the `pg_typeof` function to determine the type of a value
* {:.fragment} `value::type` to coerce to a type


</section>

<section markdown="block">
## Number Types 

__Check the docs on [numeric data types](https://www.postgresql.org/docs/current/static/datatype-numeric.html)__ &rarr;

* {:.fragment} `serial` (auto incrementing, pk if no "natural pk" apparent, called artificial / surrogate)
* {:.fragment} `integer` - typical choice for integer, 4 bytes
* {:.fragment} `smallint` - 2 bytes, signed
* {:.fragment} `bigint` - 8 bytes, signed
* {:.fragment} `decimal` / `numeric` - user specified precision numbers
* {:.fragment} `real` / `double precision` - variable-precision numbers

</section>

<section markdown="block">
## Precision and Scale of Numeric / Decimal

__`numeric` and `decimal` types can be used to store values that contain a _very large number_ of digits.__ &rarr; 

* {:.fragment} calculations (such as addition, subtraction and multiplication) with these types <span class="hl">give back exact results</span>, but slower than using floating point types! 
* {:.fragment} the __precision__ and __scale__ of these types can be set
	* {:.fragment} __precision__: total count of significant digits
	* {:.fragment} __scale__: the number of decimal digits
	* {:.fragment} specified when declaring type: `numeric(4, 2)`
	* {:.fragment} precision first, then scale (alternatively, only precision)
	* {:.fragment} without precision or scale, precision and scale only limited by current implementation

</section>


<section markdown="block">
## Floating Point Numbers

__`real` and `double precision` are floating point types__ &rarr;

* {:.fragment} these types are <span class="hl">inexact</span>
* {:.fragment} you may be familiar with this already ... try this with regular floating point or number types in Python, Java or JavaScript:
	* {:.fragment} `0.1 + 0.2` 
	* {:.fragment} yields `0.30000000000000004`
* {:.fragment} if exact storage and calculations is necessary, use numeric 
* {:.fragment} `SELECT 0.15::numeric < 0.15::real -- WAT!?`

</section>


<section markdown="block">
## Strings

__See docs on [character data types](https://www.postgresql.org/docs/current/static/datatype-character.html)__ &rarr;

* {:.fragment} `text` - unlimited length
* {:.fragment} `varchar(n)` - where `n` is num of characters (character varying)

⚠️If casting to lesser length, string will be truncated to fit!
{:.fragment}

</section>

<section markdown="block">
## Dates and Times

See [docs on Date/Time types](https://www.postgresql.org/docs/current/static/datatype-datetime.html)

* {:.fragment} `timestamptz` (timestamp __with timezone__, __use this__!)
	* {:.fragment} stored as UTC (universal coordinated time, sometimes GMT is synonym), queried, shown in local time zone
* {:.fragment} `timestamp` (no timezone)
* {:.fragment} `date`
* {:.fragment} `time`

It's sometimes useful to store date or time date in a regular `integer` field. For example, year can be represented by:
{:.fragment}

* {:.fragment} a `timestamptz` or `date` but with consistent values for month, day etc.
* {:.fragment} ...as an `integer` (or even `smallint`) 

</section>

<section markdown="block">
## Booleans

__Boolean literals can be represented multiple ways!__ &rarr;

* {:.fragment} `true`
* {:.fragment} `'t'`
* {:.fragment} even `'yes'`, `'y'`, quoted true, etc...

However, when querying, the representation can depend on the client - for example, psql shows `t` or `f`, but datagrip shows a check box
{:.fragment}

</section>
<section markdown="block">
## Many Others!

__Check out this [table of all data types](https://www.postgresql.org/docs/10/static/datatype.html#DATATYPE-TABLE)!__ &rarr;

* {:.fragment} currency (`money` 💰)
	* will use the currency based on os-level localization settings
	* will format appropriately (commas, currency symbol, dots, etc.)
	* internally stores as `int` (think: cents)
* {:.fragment} shapes (`circle`, `polygon`)
* {:.fragment} documents (`xml`, `json` / `jsonb`)
* {:.fragment} networking (`inet` for ipv4 and ipv6, `cidr` for ip ranges)


</section>

<section markdown="block">
## Aside on Storing Money

__Some considerations when storing currency:__  &rarr;

* __exactness__ and rounding
* multi-currency support
* performance
{:.fragment}

</section>

<section markdown="block">
## Storing Money Continued

__What are some potential options for storing money?__:
{:.fragment}

* {:.fragment} `integer` - store cents manually, convert in application code (how to handle fractional cents, though!)
* {:.fragment} `numeric` - exact, but slow... (choose `scale` carefully; 2 likely not adequate!)
* {:.fragment} `money` - stores as cents, so exact for addition, subtraction, multiplication... but converts to floating point type for division 
	* handles input in different formats, but does not deal with conversion / multi-currency
	* _fast_ (basically int operations since dealing with cents)

Any rounding, conversion logic for either should be handled by application code
{:.fragment}

</section>

<section markdown="block">
## About SQL Syntax

__Whitespace (newlines, tabs) is ok within a statement, so formatting code with line breaks and indentation for readibility is encouraged!__

* {:.fragment} end statements with `;`
* {:.fragment} comments start with `--`
* {:.fragment} SQL keywords can be written in upper or lower case
	* but it's common practice to uppercase keywords 
	* (or at least remain consistent)

Note that in postgres:
{:.fragment}

* when writing SQL, names of objects are lowered
* (double quote if you don't want this behavior) 
* so - in postgres - __avoid uppercase letters in names of objects so that quoting isn't required__
{:.fragment}


</section>

<section markdown="block">
## Strings, Numbers, NULL 

__Delimit strings with single quotes `'`__ &rarr;

* escape with extra `'` (`'` --> `''`)
* or use double $ as quotes `$$what's this$$`
* `E'\t'` - prefix with E to use \ as escape character

__Numbers are just numeric literals: `5`, `1.23`__

__`NULL` means no value or missing value__

</section>
<section markdown="block">
## Creating a Database

__A database can have the following attributes__

* {:.fragment} character encoding
	* default is based on locale
	* (or how database is initialized)
* {:.fragment} collation (sort order of characters)
* {:.fragment} it can also have added features like languages (perl, Python, etc. for scripting), custom functions, etc.

When a database is created, it clones the template database `template1`. 
{:.fragment}

* {:.fragment} `template1` can be modified so you can have a customized template (for example, add objects like languages, functions,etc.). 
* {:.fragment} (there's also `template0`, which is meant to be kept as an unmodified copy of `template1`'s initially configuration)


</section>

<section markdown="block">
## CREATE Statement

__To create a database based off of the template `template1`__ &rarr;

<pre><code data-trim contenteditable>
CREATE DATABASE some_database_name;
--uses same encoding and collation as template1
</code></pre>
{:.fragment}

There are a bunch of options that you can set... for example:
{:.fragment}

<pre><code data-trim contenteditable>
-- use utf8 as encoding, "copy" template0
-- instead of template1
CREATE DATABASE some_database_name
    ENCODING 'UTF8';
    TEMPLATE template0;
</code></pre>
{:.fragment}

See [CREATE DATABASE](https://www.postgresql.org/docs/10/static/sql-createdatabase.html) docs
{:.fragment}


</section>

<section markdown="block">
## Creating a Table Background Info

See [CREATE TABLE](https://www.postgresql.org/docs/10/static/sql-createtable.html) doc

* `CREATE TABLE`
* followed by table name
* in parens...
	* comma separated list of column names and their type separated by space:
	* `first_name` varchar(255)
* can specify some constraints after type, such as:
	* `NOT NULL`
	* `UNIQUE`
	* `PRIMARY KEY`
* default value specified with:
	* `DEFAULT value_to_default_to`
</section>

<section markdown="block">
## Creating a Table Example

__Create a student table with 5 fields: netid first, last, midterm and registered__ &rarr;

<pre><code data-trim contenteditable>
CREATE TABLE student(
	 netid varchar(20) PRIMARY KEY,
	 first varchar(255) NOT NULL,
	 last varchar(255) NOT NULL,
	 midterm numeric,
	 registered timestamptz DEFAULT NOW()
);
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Create (INSERT)

__To add a new row to a table, use an <span class="hl">INSERT</span> statement__ &rarr;

<pre><code data-trim contenteditable>
-- values in order of field names (registered
-- left out, as it has a default value)
INSERT INTO student 
	VALUES ('fb123', 'foo', 'bar', 90);
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
-- specify columns and matching values (does not have 
-- to follow same order of columns in CREATE TABLE)
INSERT INTO student 
	(first, last, midterm, netid) 
	VALUES ('baz', 'qux', 70, 'bq789');
</code></pre>
{:.fragment}

* {:.fragment} insert multiple rows: add commas to after each "tuple" of values
* {:.fragment} [See docs on INSERT](https://www.postgresql.org/docs/current/static/sql-insert.html)

</section>

<section markdown="block">
## Read (SELECT)

__Use a <span class="hl">SELECT</span> statement to _read_ data__ &rarr;

1. {:.fragment} start with `SELECT`
2. {:.fragment}  followed by a comma separated list of columns or calculated values you'd like to see (the `SELECT list`)
	* {:.fragment} you can use `AS some_alias` to alias column names or name calculations
	* {:.fragment} `*` means all columns
	* {:.fragment} arithmetic operators and functions / expressions can be used here 
	* {:.fragment} `DISTINCT` for only unique values
3. {:.fragment} then, optionally, keyword `FROM tablename` ...to specify which table to query 
4. {:.fragment} optionally `WHERE cond` to specify how to filter rows
5. {:.fragment} optionally `ORDER BY ordering` for sorting
6. {:.fragment} optionally `LIMIT num` to restrict the number of rows returned

</section>

<section markdown="block">
## An Example SELECT Query

<pre><code data-trim contenteditable>
-- give me col1, col2, and new_col only
-- new_col is a calculated field
-- this is the 'SELECT list'
SELECT col1, col2, col3 * 2 as new_col    

	-- from table, some_Table
	FROM some_table

	-- the value in col1 must be > 1
	-- for the row to be returned
	WHERE col1 > 1

	-- sort by col2 ascending
	ORDER BY col2

	-- only give back, at most, 5 rows
	LIMIT 5;
</code></pre>

</section>
<section markdown="block">
## SELECT Background

(From [the official docs](https://www.postgresql.org/docs/12/sql-select.html)) __SELECT retrieves rows from <span class="hl">zero or more</span> tables.__ &rarr;

Using the parts of a `SELECT` statement from the previous slide, what order might the parts of a `SELECT` query be processed in? 
{:.fragment}

1. {:.fragment} `FROM` to determine set of all possible rows to return!
2. {:.fragment} `WHERE` to filter out rows that don't match criteria
3. {:.fragment} `SELECT list` to determine the  actual values of the resulting rows by evaluating expressions, resolving column names, etc.
4. {:.fragment} `DISTINCT` to eliminate duplicate rows in the output
5. {:.fragment} `ORDER BY` to sort the output rows
6. {:.fragment} `LIMIT` to restrict the output rows to a specific number
</section>

<section markdown="block">
## Operators and Functions

__Operators__ &rarr;
{:.fragment}

* {:.fragment} arithmetic: `+`, `-`, `*`, `/`
* {:.fragment} string concatenation: `||` (`'HI' || 'THERE'`)
* {:.fragment} logical operators: `AND`, `OR`, `NOT`
* {:.fragment} check for NULL: `IS NULL` and `IS NOT NULL`
* {:.fragment} pattern matching, case sensitive and insensitive: `LIKE`, `ILIKE`

__Functions__ &rarr;
{:.fragment}

* {:.fragment} `NOW()` (current date / time), `ROUND(val)`, etc.

See [documentation on operators and functions](https://www.postgresql.org/docs/9.1/static/functions.html)
{:.fragment}
</section>

<section markdown="block">
## More `SELECT` Examples

__Using the student table created earlier__ &rarr; 

* {:.fragment} get all students
	<pre class="fragment"><code data-trim contenteditable>
SELECT * FROM student;
</code></pre>
* {:.fragment} get all students, just netid, first, and name last name ... and alias first as fn
	<pre class="fragment"><code data-trim contenteditable>
SELECT netid, first as fn FROM student;
</code></pre>
* {:.fragment} get all students, show net id and midterm grade divided by 100
	<pre class="fragment"><code data-trim contenteditable>
SELECT netid, midterm / 100 FROM student;
</code></pre>

</section>

<section markdown="block">
## `SELECT` + `DISTINCT`

__Only show the distinct rows (remove duplicate rows) by using `DISTINCT` with `SELECT`__ &rarr;

Show the distinct first names of students:

<pre><code data-trim contenteditable>
SELECT DISTINCT first 
	FROM student;
</code></pre>

</section>


<section markdown="block">
## `SELECT` with `WHERE` Clause

__Optionally, add a `WHERE` clause to specify _conditions_ (think filtering)__ &rarr;

* conditions can use operators like `=`, `<>` (not equal), `>`, `<`
* you can also use `LIKE` and `ILIKE` with `%` representing _wildcards_ to match on substrings (`ILIKE` is case insensitive)
* use `col_name IS NULL` to check for a `NULL` value
* multiple conditions can be put together with `AND`, `OR`, `NOT`
* parentheses can be added to specify precedence
</section>

<section markdown="block">
## `SELECT` + `WHERE`

__Filter your `SELECT` statement results with a `WHERE` clause__ &rarr;

* {:.fragment} only students with midterm > 80
	<pre class="fragment"><code data-trim contenteditable>
SELECT * FROM student WHERE midterm > 80;
</code></pre>
* {:.fragment} only students with between 70 and 90
	<pre class="fragment"><code data-trim contenteditable>
SELECT * FROM student 
	WHERE midterm > 70	
	AND midterm < 90;
</code></pre>
* {:.fragment} btw, also `BETWEEN 71 and 89`
	* (inclusive)

</section>

<section markdown="block">
## `SELECT` + `WHERE` Continued

* {:.fragment} students that have no midterm score
	<pre class="fragment"><code data-trim contenteditable>
SELECT * FROM student WHERE midterm IS NULL;
</code></pre>
* {:.fragment} get the netid and first name of students with that have a netid that has `jv` in it or starts with `Jo`, case insensitive
	<pre class="fragment"><code data-trim contenteditable>
SELECT netid, first FROM student 
	WHERE netid LIKE '%jv%'	
	OR first ILIKE 'Jo%';
</code></pre>

</section>

<section markdown="block">
## Ordering

__Add an `ORDER BY` clause at the end of your `SELECT` to specify ascending ordering__ &rarr;

<pre><code data-trim contenteditable>
SELECT * FROM student 
	WHERE midterm < 60
	ORDER BY registered;
</code></pre>
{:.fragment}

__Add `DESC` to order in descending order__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
SELECT netid FROM student 
	ORDER BY registered desc;
</code></pre>
{:.fragment}

__Separate multiple column names to order by multiple columns__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
SELECT * FROM student ORDER BY last, first;
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## `LIMIT`

__A <span class="hl">LIMIT</span> clause can be added at the end of a `SELECT` statement (after `ORDER BY`) to contrain the number of results of the query__ &rarr;

Only show 10 results:

<pre><code data-trim contenteditable>
SELECT netid, first, last
	FROM student
	ORDER BY netid
	LIMIT 10;
</code></pre>

</section>

<section markdown="block">
## Update (`UPDATE`)

__Use an `UPDATE` statement to set the value of a column for a row / rows__ &rarr;

* start with keyword, `UPDATE`
* then name of table to update
* followed by keyword `SET`
* finally column name = some value
* (see [docs on `UPDATE`](https://www.postgresql.org/docs/current/static/sql-update.html)

<pre><code data-trim contenteditable>
-- set all students' registered field to 1/1/2018
UPDATE student SET registered = '2018-01-01';
</code></pre>
</section>

<section markdown="block">
## `UPDATE`, Expressions, and `WHERE`

__Add a `WHERE` clause to `UPDATE` (after `SET`) to specify which rows to change__ &rarr;

<pre><code data-trim contenteditable>
-- only set midterm score for rows that
-- have netid fb123
UPDATE student 
	SET midterm = 80 
	WHERE netid = 'fb123';
</code></pre>

__Remember the value in `SET` can be an expression__ &rarr;

<pre><code data-trim contenteditable>
UPDATE student SET registered = NOW();
</code></pre>

<pre><code data-trim contenteditable>
-- probz a bad idea to set pk to this, but...
-- set netid to concatenation of first and last
UPDATE student SET netid = first || last;
</code></pre>

</section>

<section markdown="block">
## Delete / Remove Rows (`DELETE`) 

__To remove rows from a table use the `DELETE` statement__ &rarr;

<pre><code data-trim contenteditable>
DELETE FROM student WHERE midterm > 90;
</code></pre>

Again, note the `WHERE` clause specifying which rows to take action on.

(See the [documentation on `DELETE`](https://www.postgresql.org/docs/current/static/sql-delete.html))
</section>

<section markdown="block">
## Add / Remove Column 

__Use `ALTER TABLE` to add / remove columns__ &rarr;

* {:.fragment} add a new column
	<pre class="fragment"><code data-trim contenteditable>
ALTER TABLE student 
	ADD COLUMN final_exam_score;
</code></pre>
* {:.fragment} add a new column with a default value
	<pre class="fragment"><code data-trim contenteditable>
ALTER TABLE student 
	ADD COLUMN final_exam_score numeric DEFAULT 80;
</code></pre>
* {:.fragment} remove a column
	<pre class="fragment"><code data-trim contenteditable>
ALTER TABLE student DROP COLUMN final_exam_score;
</code></pre>
</section>

<section markdown="block">
## Modifying Columns

__`ALTER TABLE` can also be used to modify columns__ &rarr;

<pre><code data-trim contenteditable>
-- change data type of column
ALTER TABLE student 
	ALTER COLUMN netid 
	SET DATA TYPE varchar(200);
</code></pre>

<pre><code data-trim contenteditable>
-- rename column
ALTER TABLE student 
	RENAME COLUMN midterm TO midterm_score;
</code></pre>

See [full documentation on `ALTER TABLE`](https://www.postgresql.org/docs/10/static/sql-altertable.html)
</section>


<section markdown="block">
## Casting

__To cast a value from one type to another in a SQL statement, use either of the two expressions__ &rarr;

* `CAST (colname as newType)`
* `val::newType`

<pre><code data-trim contenteditable>
SELECT netid, 
	CAST (midterm AS smallint) AS smol_mid
	FROM student;
</code></pre>

<pre><code data-trim contenteditable>
-- assume that midterm is integer
-- cast to numeric
SELECT * FROM student 
	ORDER BY ROUND(midterm::numeric, 2);
</code></pre>
</section>

<section markdown="block">
## `ROUND` / formating

__`ROUND` rounds a numeric value to a specified number of decimal places__

There's a one argument version that rounds to an integer.

Used in conjunction with casting, some simple formatting can be done:

<pre><code data-trim contenteditable>
-- assuming midterm is now an integer
-- cast to numeric
-- so that we can round to two places
SELECT netid, ROUND(CAST(midterm AS numeric), 2)
	FROM student;
</code></pre>

</section>

<section markdown="block">
## Removing Tables / Databases

__Use the `DROP` command to remove databases or tables__ &rarr;

* `DROP TABLE table_name;`
* `DROP DATABASE database_name;`

Notes on usage:

* you must connect to another database if you are planning on dropping the database that you're currently connected to
* use `IF EXISTS` to suppress errors if the table you are dropping doesn't exist
	* DROP TABLE IF EXISTS table_name;


{% comment %}
<section markdown="block">
## Running SQL Scripts

</section>
<section markdown="block">
## import


```
DROP TABLE IF EXISTS sd;
CREATE TABLE sd (
	sd_state text,
	sd_geoid text,
	sd_name text,
	sd_lowestGrade text,
	sd_highestGrade text,
	sd_pop_2010 integer,
	sd_hu_2010 integer,
	sd_aland real,
	sd_awater real,
	sd_aland_sqmi real,
	sd_awater_sqmi real,
	sd_intptlat real,
	sd_intptlong real,
	PRIMARY KEY(sd_geoid)
);
```
```
copy sd from '/tmp/Gaz_elsd_national.txt' delimiter E'\t' CSV header;
```
</section>



<section markdown="block">
## 

<pre><code data-trim contenteditable>

select count(*) as movie_count, director, round(avg(budget::numeric), 2)::money as avg_budget 
	from movie 
	group by director 
	having count(*) > 1 
	order by movie_count desc;

</code></pre>

</section>

{% endcomment %}








