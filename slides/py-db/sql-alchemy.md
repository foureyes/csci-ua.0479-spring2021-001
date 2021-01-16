---
layout: slides
title: "SQLAlchemy"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## SQLAlchemy

Another library for interacting with a relational database (note that it's comis [SQLAlchemy](https://www.sqlalchemy.org/). __It offers multiple ways of working with your database.__ &rarr;

* {:.fragment} it can be used to issue __raw SQL queries__
* {:.fragment} its __expression language__ allows you to skip SQL entirely and use equivalent Python methods
* {:.fragment} it also offers a full-feature __object-relational mapper__ (ORM)  that maps table rows to _actual_ instances of Python objects
* {:.fragment} install with `pip` or `conda`

</section>

<section markdown="block">
## SQLAlchemy Support

👀 __SQLAlchemy supports multiple databases, not just postgres__ &rarr;

* {:.fragment} SQLite
* {:.fragment} MySQL
* {:.fragment} Oracle
* {:.fragment} MS-SQL
* {:.fragment} Postgresql, of course ... and others

Also, check out [this page](https://www.sqlalchemy.org/features.html) for more details on features!
{:.fragment}

</section>
<section markdown="block">
## An Overview...

__SQLAlchemy is pretty large library and it can be a bit daunting to learn__ &rarr;

* we'll check out a quick survey of how it works
* ... in order of increasing abstraction
* (low level SQL queries first... up to using an object-relational mapper)
* [see the diagram in the documentation to get a high-level view of the components that make up SQLAlchemy](https://docs.sqlalchemy.org/en/13/intro.html)... we're mostly interested in:
	* {:.fragment} Engine
	* {:.fragment} Expression Language
	* {:.fragment} Object relational mapper

</section>
<section markdown="block">
## Example

__These slides use [the Museum of Modern Art (MoMA) collection data](https://github.com/MuseumofModernArt/collection)__ for example data.

* the field names have been modified to adhere to naming conventions
* a join table was introduced
* [see `moma-full.sql` for creation and import](../../sql/py/moma-full.sql)

</section>

<section markdown="block">
## Raw SQL

<pre><code data-trim contenteditable>

from sqlalchemy import create_engine

db = create_engine("postgres://localhost/databasename")

artworks = db.execute("""select artwork.title, artwork.artwork_date
from artist
inner join artist_artwork on artist.artist_id = artist_artwork.artist_id
inner join artwork on artist_artwork.artwork_id = artwork.artwork_id
where artist.name ilike '%%marina%%'
""")

for a in artworks:
    print(a)
</code></pre>

</section>

<section markdown="block">
## create_engine

`create_engine` can be called with:

* {:.fragment} ...a database connection string as the first argument:
    * {:.fragment} this connection string is sometimes referred to as a __DSN__ (data source name)
    * {:.fragment} it consists of a protocol, username, password, host and database name:
	* {:.fragment} `postgres://username:password@hostname/databasename`
* {:.fragment} and a keyword argument `echo=True` if you'd like to see the SQL it generates

__`create_engine` returns an `Engine` object, representing the core interface to the database__  
{:.fragment}
</section>

<section markdown="block">
## Engine

__An instance of `Engine`__ &rarr;

* {:.fragment} adapts to the _dialect_ of SQL used (for example, postgres vs MS SQL Server) 
* {:.fragment} ...and handles __connection pooling__ 
    * {:.fragment} from the SQLAlchemy docs: " a standard technique used to maintain long running connections in memory for __efficient re-use__" 
* {:.fragment} `execute` can be called on the `Engine` object directly to issue raw SQL queries... 
    * Note that a connection will be made implicitly when `execute` is called  
    * ...or you can explicitly call `connect` from your `Engine` instance

[See the official docs on SQLAlchemy `Engine`](https://docs.sqlalchemy.org/en/latest/core/engines.html)
{:.fragment}

</section>

<section markdown="block">
## Other Operations

__Of course, because this is just raw SQL, you can modify the database as well. Here is an example of inserting... and then immediately removing an artist__ &rarr;


Note that we parameterize the values here...
{:.fragment}

<pre><code data-trim contenteditable>
q = """insert into artist (artist_id, name, bio) 
values (%s, %s, %s)"""
db.execute(q, 123456, 'joe v', "i'm an artist!?")
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
db.execute('delete from artist where artist_id = 123456')
</code></pre>
{:.fragment}

__Notice that when executing raw SQL inserts, deletes, etc. ... these are treated as _autocommitted_ transactions__
{:.fragment}

(See the docs on [understanding autocommit](https://docs.sqlalchemy.org/en/latest/core/connections.html#understanding-autocommit))
{:.fragment}
</section>

<section markdown="block">
## Expression Language

__SQLAlchemy offers an API that has objects and methods that correspond to relational database structures and SQL statements and clauses__. 

This API is called __the SQLAlchemy Expression Language__

* {:.fragment} it's similar to the _actual_ database operations (for example, names of methods match names of SQL statements)
* {:.fragment} ...but it also serves as a thin layer of abstraction to smooth over any differences in SQL dialects / database backends


</section>

<section markdown="block">
## Expression Language Setup

__In order to use the SQLAlchemy Expression Language, you have to let SQLAlchemy know about your database structures by supplying some metadata__ This database metadata is encapsulated in:

* {:.fragment} `Column` objects that (obvs) represent columns in your database table
* {:.fragment} ...and, of course, these columns are are associated with `Table` objects
* {:.fragment} a collection of `Table` objects are stored in a `MetaData` object

This metadata can be created _by hand_, but it can also be generated automatically from an existing database through __table reflection__. (We'll use the manual way to see how this actually works)
{:.fragment}

</section>

<section markdown="block">
## Expression Language Imports

Start off by bringing in our usual `create_engine` `import`. 

<pre><code data-trim contenteditable>
from sqlalchemy import create_engine
</code></pre>
{:.fragment}

__Now bring in constructors for `Table`, `Column`, and `MetaData`__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
from sqlalchemy import Table, Column, MetaData
</code></pre>
{:.fragment}

__Finally, bring in objects that represent column data types__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
from sqlalchemy import String, Integer
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Table MetaData

__Let's create our database metadata (we'll just do it for `Artist` rn)...__ &rarr;

<pre><code data-trim contenteditable>
# assuming dsn contains our database info
db = create_engine(dsn, echo=True)

meta = MetaData(db)
artist_table = Table('artist', meta,
                       Column('artist_id', Integer),
                       Column('name', String),
                       Column('bio', String))
</code></pre>
{:.fragment}

* {:.fragment} note that we're creating an object that represents the artist table
* {:.fragment} it provides SQLAlchemy with some meta data about `artist`

</section>

<section markdown="block">
## Connecting and Creating

__Now... we explicitly connect (this was done implicitly for us with execute previously) and insert some data__ &rarr;

<pre><code data-trim contenteditable>
with db.connect() as conn:
    s = artist_table.insert().values(artist_id=123456, name="joe v", bio="i'm an artist!?")
    print(s)
    conn.execute(s)
</code></pre>
{:.fragment}

Note that:
{:.fragment}

* {:.fragment} instead of using raw sql, we're using a `Table` object and equivalent methods for `insert`, `values`, etc.
* {:.fragment} we use `with` so that our connection is automatically closed
* {:.fragment} when we print out the result of calling `insert` and `values`, we see the SQL that is generated
* {:.fragment} to run it, use `execute` on the `connection` object

</section>

<section markdown="block">
## Read

__Here's another example where we simply read data__ &rarr;

<pre><code data-trim contenteditable>
    s = artist_table.select().where(artist_table.c.name == 'joe v')
    print(s)
    artists = conn.execute(s)
    for artist in artists:
        print(artist)
</code></pre>
{:.fragment}

* {:.fragment} note the expression `artist_table.c.name` to reference the column, `c`, called `name`
* {:.fragment} instead of iterating over the result set, you can also use the familiar: 
    * {:.fragment} `artists.fetchone`
    * {:.fragment} `artists.fetchall`

</section>

<section markdown="block">
## Result Sets

__We see a tuple representing the row, but, of course, you can index by position... or by column name__ &rarr;

<pre><code data-trim contenteditable>
    # assuming result is returned from query
    for row in result:
        # print the whole tuple
        print(row)

        # just the first two columns (using ints)
        print(row[0], row[1]) 

        # only the name column (using the column name!)
        print(row[artist_table.c.name])
</code></pre>
</section>

<section markdown="block">
## Another Select

__We can also use `select` as regular function... as we can see in this more _complex_ query__ &rarr;

<pre><code data-trim contenteditable>
from sqlalchemy import select
match = '%jack%'
cols = [artist_table.c.artist_id, artist_table.c.name]
name_filter = artist_table.c.name.like('%jack%');
q = select(cols).where(name_filter).limit(5)
</code></pre>
{:.fragment}

Produces...
{:.fragment}

<pre><code data-trim contenteditable>
SELECT artist.artist_id, artist.name 
FROM artist 
WHERE artist.name LIKE %(name_1)s 
 LIMIT %(param_1)s
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Even More!

Check out the [official documentation on the Expression Language](https://docs.sqlalchemy.org/en/latest/core/tutorial.html#selecting). __There are _a lot_ of methods__ ...for example: &rarr;

* {:.fragment} using `table1.join(table2)` for inner joins
* {:.fragment} using methods like `and_`, `or_` etc. for conjunctions
* {:.fragment} issuing updates with `tablename.update().values(col1=val1, col2=val2)`
* {:.fragment} etc.

</section>

<section markdown="block">
## ORM Style!

__Ok... last one: the ultimate abstraction... all 🐍, zero SQL (well at least visible)__ &rarr;

SQLAlchemy offers an __Object Relational Mapper__ (__ORM__) to:

* {:.fragment} create Python classes with associated database tables
* {:.fragment} instances of those classes correspond to rows in the associated table 
* {:.fragment} it allows the synchronization of changes in instances and data in the database
 
 __SQLAlchemy's ORM is built on top of the Expression Language__
 {:.fragment}

 * {:.fragment} however, the Expression Language is tied pretty closely to the underlying database, exposing SQL
 * {:.fragment} whereas the ORM hides away the database


</section>
<section markdown="block">
## ORM Imports

__Setup (so many imports 😅)__

<pre><code data-trim contenteditable>
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer

# base class for our classes
from sqlalchemy.ext.declarative import declarative_base

# database "session"
from sqlalchemy.orm import sessionmaker
</code></pre>
{:.fragment}


Of course... create the engine
{:.fragment}

<pre><code data-trim contenteditable>
db = create_engine("postgres://localhost/scratch")
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Create an Artist Class

__Create a class that represents artists in the database__ &rarr;

(start with retrieving the base class used for SQLAlchemy ORM classes)
{:.fragment}

<pre><code data-trim contenteditable>
# get the base class for all classes that you create
base = declarative_base()

class Artist(base):
    __tablename__ = 'artist'

    artist_id = Column(Integer, primary_key=True)
    name = Column(String)
    bio = Column(String)
</code></pre>
{:.fragment}

* note that these are kind of like _static_ variables (not instance!)
{:.fragment}


</section>

<section markdown="block">
## Let's Make Some Artists

__To insert, create a new instance of `Artist` and `add` it to the session to persist it__ &rarr;

<pre><code data-trim contenteditable>
Session = sessionmaker(db)
session = Session()

a = Artist(artist_id=123456, name="joe v", bio="yes, i'm an artist, ok!?")
# add this new object to our session so we can persist it
session.add(a)
session.commit()
</code></pre>
{:.fragment}

[Note that there are multiple ways to execute queries; using the session is recommended when working with the ORM](https://stackoverflow.com/questions/34322471/sqlalchemy-engine-connection-and-session-difference)
{:.fragment}

</section>

<section markdown="block">
## Reading 

__And, for good measure, let's try a select... this time, `filter` takes the place of `where`__

<pre><code data-trim contenteditable>
artists = session.query(Artist).filter(Artist.name == 'joe v')
for a in artists:
    print(a.name)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Now Remove It!

__Call `session.delete` and `commit` to remove from table__ &rarr;

<pre><code data-trim contenteditable>
session.delete(some_artist_instance)
session.commit()
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Which One to Use?

__Uh... so many ways to get data from the database. Which one should we use and why?__ &rarr;

* {:.fragment} want exact control over how your query is created? __raw sql__ using engine directly
* {:.fragment} vaguely know sql, but can read python documentation well? __expression language__ or __orm__
	* {:.fragment} (that's kind of only _half true_, as expression language uses `select`, `where`, etc.)
* {:.fragment} don't want random sql sprinkled throughout your app? __orm__
	* {:.fragment} also great if not so comfortable with sql
	* {:.fragment} potentially have portable (in terms of db backend) code
	* {:.fragment} most orms prevent common mistakes that lead to security issues (like sql injection)

</section>

<section markdown="block">
## Er Maybe NOT Use?

__What's challenging about using an ORM__  😓 &rarr;

* {:.fragment} what sql is it actually generating? 🤔
* {:.fragment} is the sql efficient? ⏩
* {:.fragment} still "another language" (well, api) 
* {:.fragment} kind of confusing if you already know sql 🤷
* {:.fragment} in the case of SQLAlchemy... many different ways to do the same thing
* {:.fragment} for many ORMs, a lot of boilerplate code / code generation is necessary for mapping

__No ORM, now what?__ &rarr;
{:.fragment}

* {:.fragment} have _some_ sort of abstraction between database and app
* {:.fragment} can be as simple as a library of functions 
* {:.fragment} no raw sql!

</section>
