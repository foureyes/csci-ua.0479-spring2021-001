---
layout: slides
title: "Constraints and Conventions"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Postgres Casing

__Postgres is a little tricky when comes to casing:__ &rarr;

* {:.fragment} postgres lowercases unquoted names in statement
* {:.fragment} to enforce casing, a name must be surrounded in quotes
* {:.fragment} given the following table definition...

<pre><code data-trim contenteditable>
create table NaMiNg ("QUOTED" varchar(255), UNQUOTED varchar(255))
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
select * from table NaMiNg; -- ok!
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
select * from naming;       -- also ok
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
select * from naming where QUOTED = 'foo';
-- problem! QUOTED is lowered, but the
-- table name is actually upper; use
-- double quotes: "QUOTED"
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Identifiers / Names

__Based on how postgres handles casing, sometimes the following rules are used for naming tables, columns, etc.__ &rarr;

1. {:.fragment} always use __unquoted identifiers__
2. {:.fragment} consequently, all table names, column names, etc. should be __lowercase__
3. {:.fragment} lastly, if there are multiple words in a name, separate with __underscore__ (I guess this is called [snake case](https://en.wikipedia.org/wiki/Snake_case) 🐍!?)

</section>

<section class="danger" markdown="block">
## Quoting

__Please _just don't_ double quote names; it'll be a headache later on!__

* {:.fragment} first.. the obvious is once you quote a name, it'll be case sensitive, 
	* and consequently, if there are uppercase letters
	* ...you'll have to quote that name _forever_
* {:.fragment} also, quoting allows you to use wacky things for names
	* like special characters (such as space) in names 🤢
	* or even SQL keywords 🤮
</section>
<section markdown="block">
## Don't Get Caught Up in the Feels

__Sometimes people feel very strongly about naming conventions (🤷)__ &rarr;

1. don't get too passionate about a particular style
2. more important is remain consistent
3. ...and, if working in an organization, go with the organization's standards!

</section>

<section markdown="block">
## Other Naming Considerations

__This goes without saying, but....__

1. make sure names are descriptive 
	* sometimes being verbose is better to enhance readability
	* most client allow tab completion anyway!
2. as mentioned in an earlier set of slides, be consistent with pluralization for table names 
	* the book uses plurals for table names
	* I tend to use singular

</section>

<section markdown="block">
## Types

__We've already learned about types as we've worked with single tables__ &rarr;

Types dictate:

* {:.fragment} the kind of data that we can put in a column
* {:.fragment} what kind of operations we can perform

Specifying type allows us to declare rules about what the __acceptable values and operations__ are for a particular column
{:.fragment}

</section>
<section markdown="block">
## Aside on Types and Implicit Casting


__Have you tried inserting an incorrect value into a column? ...what happens?__ &rarr;  

* {:.fragment} maybe an error 🙅
* {:.fragment} or maybe it just works
* {:.fragment} (WAIT, BUT I THOUGHT TYPES VALIDATE DATA)

Although SQL is strongly typed (in that functions, operators and data storage with compatible types causes errors), implicit casting does exist.
{:.fragment}

* {:.fragment} inserting an `integer` into a `text` field is ok!
* {:.fragment} ...but inserting a "non-numeric" string into a `integer` won't
* {:.fragment} the specifics of this can be found in some system catalogs (kind of like system tables): `pg_cast` and `pg_type`
</section>

<section markdown="block">
## Constraints

__Sometimes we want more find-grained control over what's considered valid data__ &rarr;

We can add additional rules for valid values by creating __constraints__. Constraints limit the kind of data that can go into:
{:.fragment}

1. {:.fragment} individual columns (column constraint)
2. {:.fragment} or the entire table (table constraint)


Constraints help ensure data integrity (consistency, accuracy, and general quality) in our tables (and even _across_ tables). 👍
{:.fragment}
</section>

<section markdown="block">
## List of Constraints

Some constraints include:

* {:.fragment} Check Constraints
* {:.fragment} Not-Null Constraints
* {:.fragment} Unique Constraints
* {:.fragment} Primary Keys
* {:.fragment} Foreign Keys

We'll go over these in the next few slides, but check out [the official docs for full details](https://www.postgresql.org/docs/12/ddl-constraints.html).
{:.fragment}
</section>

<section markdown="block">
## Check Constraints

__A check constraint is a generic constraint type.__ &rarr;

* {:.fragment} you can specify that the value in a column yields true for a specific boolean expression 
* {:.fragment} as a table level constraint: `CONSTRAINT check_enrollment_cap_not_zero CHECK (enrollment_cap > 0)`
* {:.fragment} note that you can have arbitrarily complex expressions using logical operators (`AND`, `OR`)
* {:.fragment} [see more details in the docs](https://www.postgresql.org/docs/12/ddl-constraints.html#DDL-CONSTRAINTS-CHECK-CONSTRAINTS)

</section>

<section markdown="block">
## Not Null and Unique

__These work as you'd expect__ &rarr;

As column constraints...

* `NOT NULL` - no missing values in this column
* `UNIQUE` - all values in this column are unique
</section>

<section markdown="block">
## Primary Keys

A table's __primary key__ 🔑 is a column (or columns) that uniquely identify a row in that table.  

As a constraint, it provides the following guarantees:
{:.fragment}

1. {:.fragment} the column or columns are unique in the table
2. {:.fragment} the column or columns will always have a value (not null)

__We've already seen primary keys , but let's look into some more details about:__ &rarr;
{:.fragment}

* {:.fragment} primary key syntax
* {:.fragment} strategies for choosing a primary key
</section>


<section markdown="block">
## Primary Key Syntax (Column Constraint)

__Here's how we've declared primary keys so far__ &rarr;

<pre><code data-trim contenteditable>
CREATE TABLE widget (
	id serial PRIMARY KEY,
	-- altenatively
	-- CONSTRAINT id PRIMARY KEY
	name text
);

</code></pre>

Where... `id` is an automatically incrementing integer.
{:.fragment}

The above is __column constraint__ syntax as it refers to the individual column `id`.  Use `\d widget` to see that the primary key constraint has been placed on the table, manifested as an _index_ in the output.
{:.fragment}
</section>

<section markdown="block">
## Primary Key Syntax (Table Constraint) 

__Alternatively a primary key can be declared on the table level:__ &rarr;

(Why might this be useful? <span class="fragment">...a primary key may depend on more than just one column</span>)
{:.fragment}

Yes, that's right, primary key can consist of multiple columns! This is called a __composite primary key__.
{:.fragment}

<pre><code data-trim contenteditable>
CREATE TABLE course (
	course_num varchar(10),
	section varchar(3),
	name text,
	CONSTRAINT course_pkey PRIMARY KEY (course_num, section)
);
</code></pre>
{:.fragment}

</section>
<section markdown="block">
##  Primary Key Syntax (Table Constraint) Continued

__Note the syntax from the previous slide__ &rarr;

* {:.fragment} `CONSTRAINT name PRIMARY KEY (column_1, column_2)`
* {:.fragment}  we give the primary key a name after the `CONSTRAINT` keyword.
* {:.fragment} (we mimic the naming convention when using a column constraint `table_pkey`)

__Let's try inserting some values__ What happens if one of the columns in our composite primary key is null? How about if two rows have the same values? &rarr;
{:.fragment}

* {:.fragment} `ERROR`!
* {:.fragment} (in both cases, the values inserted violate the primary key constraint)

</section>

<section markdown="block">
## Choosing a Primary Key

__A primary key can be created by using existing column(s) (natural) or creating a new column (articial)__ &rarr;

A __natural key__ is an existing column that is used as a primary key
{:.fragment}

* {:.fragment} __if this column exists and already has data in it, what are some characteristics about it that make it a valid candidate for a primary key?__ &rarr;
	* {:.fragment} the existing column cannot have any null values
	* {:.fragment} the existing column must be unique
	* {:.fragment} the key should probably be mostly _stable_ (that is, it shouldn't change!)
* {:.fragment} example: course number and section columns
* {:.fragment} can you think of other examples of _naturally_ potential occurring keys in other domains?
	* {:.fragment} netid, isbn, ssn (but _should_ you use this?), etc.


</section>

<section markdown="block">
## Primary Keys for People

__Values like ssn, license number, or even email address may seem like good primary keys at first... but they do introduce some problems__ &rarr;

* {:.fragment} these values can _actually_ change
* {:.fragment} some of this data, like ssn, is sensitive information, and should not be used as an id
	* that id will be seen by those that have access to the database (even if not intentional)
* {:.fragment} an artificial key is _likely_ the best solution for a unique identifier for a person
</section>

<section markdown="block">
##  Primary Key Continued

A __surrogate key__ or __artifical key__, on the other hand, is a new column added with the purpose of serving as a primary key. 

* {:.fragment} __What type is this typically implemented as?__ &rarr; <span class="fragment">`serial` or `bigserial`</span>
* {:.fragment} if a sequential number is not desired, then [the UUID type in postgres](https://www.postgresql.org/docs/9.1/datatype-uuid.html) can be a good choice for type as well
	* {:.fragment} it's 128 bits of hex characters
	* {:.fragment} for example `a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11`
	* {:.fragment} this can be generated by postgres
	* {:.fragment} the docs have this amazing claim: _"very unlikely that the same identifier will be generated by anyone else in the known universe using the same algorithm"_ 👽🚀🛰

</section>

<section markdown="block">
## Natural Key vs Surrogate/Artificial Key

__What are some reasons to use/not use one key type over another?__ &rarr;

Natural keys
{:.fragment}

* {:.fragment} no extra column needs to be added
* {:.fragment} column is _meaningful_

Surrogate / Artificial Keys
{:.fragment}

* {:.fragment} _real world_, natural keys typically can change... (for example, someone may want to change their `netid` or a course number and section may be modified)!
* {:.fragment} natural keys may take up more space
{:.fragment}
</section>

<section markdown="block">
## Foreign Keys

__Foreign keys__ ensure integrity between related tables. For example, if could guarantee that a column in the first table that references a column in the second table actually has matching value in the second table.

We'll look at related table and foreign keys in more detail later, but as a quick overview, the column constraint syntax for a Foreign Key is as follows:

<pre><code data-trim contenteditable>
column_name column_type REFERENCES other_table (other_column_name)
</code></pre>
{:.fragment}

And an actual example in a movie table that reference a column in a genre table:
{:.fragment}

<pre><code data-trim contenteditable>
genre_id integer REFERENCES genre (genre_id),
</code></pre>
{:.fragment}



</section>
<section markdown="block">
## Foreign Keys Continued

__So what does this get you?__

* {:.fragment} sticking with our genre and movie tables
* {:.fragment} if movie has a column, `genre_id`, related to the genre table column also called `genre_id`... __what do you think a foreign key constraint gaurantees__ &rarr;
* {:.fragment} if a genre id is set in a row in the `movie` table, it is guaranteed to exist in `genre` (otherwise an error will occur due to violation of this constraint)
* {:.fragment} this affects operations like `INSERT`, `DELETE`, and `UPDATE`
* {:.fragment} (btw, you can add `ON DELETE CASCADE` to the end of your constraint to delete rows in a related table)
* {:.fragment} (there could still be errors though if other rows are related to the same row in the related table)

</section>

<section markdown="block">
## Foreign Keys with Multiple Columns

__Also, I'm _sure_ you wanted to know, but this syntax does support multi-column foreign keys by using a table constraint.__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
FOREIGN KEY (b, c) REFERENCES other_table (c1, c2)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Where Does Your "Business Logic" Live

__This sounds a lot like app logic?__ &rarr;

This logic can be implemented in the database...

* more likely to change application stack or have multiple application stacks
* but _no one knows_ database programming anymore (less trendy, smaller pool, not a common skillset)
* database migrations happen, but definitely less common than other parts of a technology stack

</section>








