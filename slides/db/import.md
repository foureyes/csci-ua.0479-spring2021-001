---
layout: slides
title: "Importing Data"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Importing Data

__Issuing a series of manual `INSERT` statements to bring in data can be quite tedious!__ &rarr;

Fortunately, <span class="hl">data can also be imported by running .sql scripts or importing files</span> (csv, tab delimited).
{:.fragment}

The typical workflow for imports is to:
{:.fragment}

1. {:.fragment} create a table based on the data that you'll import
2. {:.fragment} potentially clean the data so that the import works well
3. {:.fragment}import a file with a `COPY` query or generate `INSERT` statements in a `.sql` file
</section>

<section markdown="block">
## Running SQL Scripts

__Two ways to run `.sql` scripts:__ &rarr;

* {:.fragment} in the `psql` client, use the `\i` command:
	* `\i /path/to/stuff-to-import.sql`
* {:.fragment} when starting psql, a file that contains sql commands can be redirected to the client so that statements within it are run:
	* `psql someDatabaseName < /path/to/stuff-to-import.sql`

In both cases, the `.sql` file can contain any number of valid sql commands.
{:.fragment}
</section>

<section markdown="block">
## A Sample .sql Script

__In songs.sql__ &rarr;

<pre><code data-trim contenteditable>
DROP TABLE IF EXISTS song;
CREATE TABLE song (
	id serial PRIMARY KEY,
	title varchar(100),
	artist varchar(100),
	danceability numeric
);

INSERT INTO song (title, artist, danceability)
	VALUES
		('Heartbeats', 'Jose Gonzalez', 0.01),
		('Heartbeats', 'The Knife', 0.9),
		('Lucid Dreams', 'Juice WRLD', 0.9);
</code></pre>

</section>
<section markdown="block">
## Running Sample SQL Script

__Before running psql:__ &rarr;

<pre><code data-trim contenteditable>
psql dbname < songs.sql
</code></pre>

__Or, while in psql:__ &rarr;

<pre><code data-trim contenteditable>
\i songs.sql
</code></pre>
</section>
<section markdown="block">
## `COPY` from csv

__`COPY` can be used to import data from a csv__ &rarr;

(note that `COPY` is not standard SQL)

<pre><code data-trim contenteditable>
COPY table_name 
    FROM filename
    options
</code></pre>


`options` can be replaced by some combination of additional options that control how file should be imported (see next slide).

The [`COPY` documentation shows more details on usage](https://www.postgresql.org/docs/current/static/sql-copy.html)
</section>

<section markdown="block">
## Specifying a Column List

__If you want to import only specific columns, you can do so with parentheses after the table name__ &rarr;

<pre><code data-trim contenteditable>
COPY table_name (col1, col2, col3)
    FROM filename
    options
</code></pre>

* {:.fragment} for example: `song (title, artist, danceability)`.
* {:.fragment} columns not specified in the column list will receive default values


</section>
<section markdown="block">
## `COPY` options

__Options can be__ &rarr;

* {:.fragment} format of file: `text`, `csv` or `binary` 
* {:.fragment} `DELIMITER AS 'some char'` - specify delimiter (default is comma for csv)
* {:.fragment} `NULL AS 'null_string'` - determines what string to treat as null (default for csv is empty string)
* {:.fragment} `HEADER` - presence specifies that header is included in file
* {:.fragment} `ENCODING 'ENCODING_NAME'` - specify encoding of file being imported (`ENCODING 'LATING'`), if not specified, client encoding is used (`psql` will auto detect based on your _locale_ settings, likely 'UTF8')
* {:.fragment} `QUOTE AS 'quote_character'` - specify quote character

</section>

<section markdown="block">
## Example csv File for `COPY`

__Here's an example csv - note that there's no whitespace before or after the delimiter (otherwise, it'll be included in value!)__ &rarr;

<pre><code data-trim contenteditable>
title,artist,danceability
Heartbeats,Jose Gonzalez,0.01
Heartbeats,The Knife,0.9
Lucid Dreams,Juice WRLD,0.9
Happy Birthday,N/A,0.9
</code></pre>

</section>

<section markdown="block">
## `COPY` Examples

__Assuming that a table exists with appropriate types__ &rarr;

<pre><code data-trim contenteditable>
id serial PRIMARY KEY,
title varchar(100),
artist varchar(100),
danceability numeric
</code></pre>

* {:.fragment} a file with a comma delimiter can be imported 
* {:.fragment} the fields to be filled are `title`, `artist`, `danceability`
* {:.fragment} this allows a `serial` primary key to not have to be specified in the csv (id will be generated!)

<pre><code data-trim contenteditable>
-- 4 columns, but only 3 in csv
COPY song (title, artist, danceability) 
	FROM '/tmp/songs.csv' 
	csv HEADER NULL AS 'N/A';
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Another Example, w/ Tabs

__Assuming a tab delimited file that contains all the columns needed (for example, primary key is not artificial, but a _natural_ key instead)__ &rarr;

<pre><code data-trim contenteditable>
COPY student 
	FROM '/tmp/students.txt' 
	csv HEADER DELIMITER AS E'\t';
</code></pre>

In this case: 

* every column in table exist in csv
* the delimiter is specified as `E'\t'` ... 
* E means use backslash to escape (and, consequently, specifies tab as the delimiter)
{:.fragment}

</section>

<section markdown="block">
## COPY vs \copy

__When using `COPY` to source data from a file, note that__ &rarr;

* {:.fragment} the file specified must be accessible by the `postgres` user (the user that the database server runs under, which is _actually_ `postgres`)
* {:.fragment} the file path should either be absolute or relative to where the server's working directory is (typically, *not* the directory that you started `psql` in)

If you want to copy relative to the client, you can use a `psql` command rather than an SQL `COPY`:
{:.fragment}

```
\copy table_name
from file_name
options
```
{:.fragment}


</section>

<section markdown="block">
## Which to Use?

The behavior of `\copy` seems much more intuitive than `COPY` when it comes to finding files / determining paths.

__However, why might it be useful to prefer `COPY` over `\copy`?__ &rarr;

* {:.fragment} the overhead of using the client and sending data to the server makes `\copy` slower than `COPY`
* {:.fragment} `\copy` is a client specific command; that is, it's available on `psql`, but perhaps not on some other client

</section>
<section markdown="block">
## What About JSON?

__It's possible to import JSON data as well__ &rarr;

* {:.fragment} it's not as straightforward as csv
* {:.fragment} the target column of the import should be type `jsonb` [see the docs](https://www.postgresql.org/docs/current/datatype-json.html)
* {:.fragment} `jsonb` allows a column to store JSON data that can be keyed/indexed into using arrow syntax `->` (`col->'field_name'`)
* {:.fragment} the format of the data file being brought in should be a JSON object per line 

</section>

<section markdown="block">
## A Quick JSON Example

Create a table:

```
CREATE TABLE foo(
	id serial PRIMARY KEY,
	data jsonb
);
```

File to import

```
{"name": "bar", "a": 12, "b": 14}
{"name": "qux", "a": 100, "b": 101}
{"name": "corge", "a": 98, "b": 99}
```

Copying and selecting

```
\copy foo (data) from 'data.json';
select data->'a' from foo;
```

[for more information on querying using `jsonb`, see this tutorial](https://www.postgresqltutorial.com/postgresql-json/)
</section>
