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

The typical workflow for imports is to:

1. create a table based on the data that you'll import
2. potentially clean the data so that the import works well
3. import a file with a `COPY` query or generate `INSERT` statements in a `.sql` file
</section>

<section markdown="block">
## Running SQL Scripts

__Two ways to run `.sql` scripts:__ &rarr;

* in the `psql` client, use the `\i` command:
	* `\i /path/to/stuff-to-import.sql`
* when starting psql, a file that contains sql commands can be redirected to the client so that statements within it are run:
	* `psql someDatabaseName < /path/to/stuff-to-import.sql`

In both cases, the `.sql` file can contain any number of valid sql commands.
</section>

<section markdown="block">
## A Sample .sql Script

__In songs.sql__ &rarr;
col_name
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
psql class11 < songs.sql
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

A list of specific columns can be added after `table_name` in parentheses (for example: `song (title, artist, danceability)`)

`options` can be replaced by some combination of additional options that control how file should be imported (see next slide).

The [`COPY` documentation shows more details on usage](https://www.postgresql.org/docs/current/static/sql-copy.html)
</section>

<section markdown="block">
## `COPY` options

__Options can be__ &rarr;

* format of file: `text`, `csv` or `binary` 
* `DELIMITER AS 'some char'` - specify delimiter (default is comma for csv)
* `NULL AS 'null_string'` - determines what string to treat as null (default for csv is empty string)
* `HEADER` - presence specifies that header is included in file
* `QUOTE AS 'quote_character'` - specify quote character

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

__Assuming that a table exist with appropriate types__ &rarr;

<pre><code data-trim contenteditable>
id serial PRIMARY KEY,
title varchar(100),
artist varchar(100),
danceability numeric
</code></pre>

* a file with a comma delimiter can be imported 
* the fields to be filled are `title`, `artist`, `danceability`
* this allows a `serial` primary key to not have to be specified in the csv (id will be generated!)

<pre><code data-trim contenteditable>
-- 4 columns, but only 3 in csv
COPY song (title, artist, danceability) 
	FROM '/tmp/songs.csv' 
	csv HEADER NULL AS 'N/A';
</code></pre>

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

</section>
