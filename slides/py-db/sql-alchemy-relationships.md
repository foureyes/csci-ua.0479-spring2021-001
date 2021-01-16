---
layout: slides
title: "SQLAlchemy ORM"
---
<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## SQLAlchemy ORM

__Some more details about SQLAlchemy__ &rarr;

* {:.fragment} overview
* {:.fragment} building classes
* {:.fragment} columns and types 
* {:.fragment} creating tables
* {:.fragment} relationships

</section>

<section markdown="block">
## Object Relational Mapper

An __Object Relational Mapper__ translates tables and their relationships into objects and object composition

__SQLAlchemy__ features an __ORM__ that:
{:.fragment}

1. {:.fragment} associates _user-defined_ defined Python classes with tables
2. {:.fragment} ... and instances correspond to _actual_ rows in the associated table 
3. {:.fragment} it also includes mechanisms to:
    * {:.fragment} to __synchronizes changes__ between objects and their related rows
    * {:.fragment} __express queries__ through user defined classes 
</section>

<section markdown="block">
## ORM vs Expression Language

__SQLAlchemy's ORM provides a high-level abstraction to interact with a relational database through objects and classes__ &rarr;

* {:.fragment} otoh, the Expression Language provides a lower level abstraction
* {:.fragment} in doesn't try to hide the underlying relational database and sql behind objects and classes
* {:.fragment} (instead it has functions and methods that directly correspond to to the structure and constructs of a relational database)

Note that the __ORM__ is actually _built_ on top the Expression Language (and in fact, is a sophisticated example of how the Expression Language can be used!)
{:.fragment}
</section>

<section markdown="block">
# ORM vs Expression Language

Another way to __view these two approaches is...__ &rarr;

1. {:.fragment} use the __ORM__ to:
   * {:.fragment} model the problem domain through classes and relationships (for example: composition, aggregation, etc.)
   * {:.fragment} ...persist instances through _some_ mechanism, such as a relational database
   * {:.fragment} ORM DON'T CARE what your backend is 🤷
2. {:.fragment} use the __Expression language__ to: 
   * {:.fragment} construct literal representations of database tables and SQL
   * {:.fragment} which are then issued to the database directly

An application may use both methods simultaneously, especially when some parts of an application require more control over the resulting SQL.
{:.fragment}
</section>

<section markdown="block">
## Mapping

__Two steps are required to map table to classes:__ &rarr;

1. {:.fragment} describe database tables 
2. {:.fragment} define classes that correspond to these tables

Both of these can be done through __SQLAlchemy's Declarative API__:
{:.fragment}

* {:.fragment} create a base class (called __declarative base__) to keep track of all other classes and their related tables
* {:.fragment} have other classes inherit from that base class

</section>

<section markdown="block">
## Declarative Base

__To create a base class that all of your classes will inherit from:__

<pre><code data-trim contenteditable>
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
</code></pre>

* {:.fragment} define all other classes based on this class
* {:.fragment} again, the base class itself catalogs information about all other classes and their corresponding tables
* {:.fragment} for example, check: `Base.metadata.tables`
* {:.fragment} note the use of `MetaData` and `Table` objects: both from the Expression Language!
</section>


<section markdown="block">
## Classes

__When declaring a class that uses the Declarative API...__ &rarr;

* {:.fragment} minimally, define a class variable called `__tablename__`
* {:.fragment} set it equal to the actual database table name (as a string)
* {:.fragment} ... have at least one class variable of type `Column`
 * {:.fragment} `Column` objects are constructed from the database column name, the type, and a boolean keyword argument specifying whether or not the column is a primary key

<pre><code data-trim contenteditable>
class Foo(Base):
    __tablename__ = 'foo'
    bar = Column('bar', String(50), primary_key=True)
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## `MetaData`

__Using the `Declarative` system to create our classes, we automatically create a `MetaData` object on our base class that__ &rarr;

* {:.fragment} stores a collection of metadata about tables (think: a registry of `Table` objects)
* {:.fragment} has the ability to generate some SQL statements relevant to these tables (such as `CREATE`)

Check the `metadata` attribute:
{:.fragment}

* {:.fragment} `Base.metadata`, `Base.metadata.tables` - _registry_ of tables
* {:.fragment} `Base.metadata.tables['foo']` and `Foo.__table__`
* {:.fragment} <pre><code data-trim contenteditable>Table('foo', 
    MetaData(bind=None), 
    Column('bar', String(length=50), table=&lt;foo&gt; primary_key=True, nullable=False), 
    schema=None)
</code></pre>



</section>

<section markdown="block">
## Columns to Attributes

__When a class is constructed, SQLAlchemy's `Declarative` API transforms `Column` objects into getters and setters that look like class and instance variables ([Python descriptors](https://docs.sqlalchemy.org/en/latest/glossary.html#term-descriptors))__


* {:.fragment} this mapped class is referred to as an __instrumented__ class
* {:.fragment} this class is mostly a regular Python class (so you can define your usual methods like `__repr__` and `__str__`)
* {:.fragment} ...with the exception of the special getters and setters 
</section>

<section markdown="block">
## Attributes / Descriptors

__The attributes generated from the `Column` objects provide the following functionality to deal with SQL and persist / load data to and from the database__ &rarr; 

* {:.fragment} at the class level: generate a SQL expression (you've seen this before)
    <pre><code data-trim contenteditable>print(Foo.bar == 'hello')</code></pre>
* {:.fragment} at the instance level: tracks changes to values... and loads / unloads values from the database (_lazily_... doesn't work with the database until it _needs_ to!) 
    <pre><code data-trim contenteditable>f = Foo()
f.bar = 'hello'
</code></pre>
</section>

<section markdown="block">
## Columns

__The `Column` constructor contains information about a column in a database__ &rarr;

Some positional arguments:
{:.fragment}

* {:.fragment} `name` (`str`) - name of the table column
* {:.fragment} `type` - `Integer`, `String`, `DateTime` ([See full list of types](https://docs.sqlalchemy.org/en/latest/core/type_basics.html#generic-types))
    * `from sqlalchemy import Column, Integer, String, DateTime`

Some keyword arguments:
{:.fragment}

* {:.fragment} `default` - a scalar value... or function
* {:.fragment} `nullable` – `False` is `NOT NULL` 
* {:.fragment} `primary_key`

[See the full column and types documentation](https://docs.sqlalchemy.org/en/latest/core/type_basics.html)
{:.fragment}

</section>

<section markdown="block">
## Creating Tables

__Again, the `MetaData` object can generate some SQL relevant to table creation.__ &rarr;

* {:.fragment} use the `create_all` method by passing in an `Engine` object to create all tables in the _registry_ of tables in the `MetaData` object
* {:.fragment} assuming that we access a `MetaData` object via a Declarative API base class:
    <pre><code data-trim contenteditable>
Base.metadata.create_all(engine)
</code></pre>

</section>

<section markdown="block">
## sessionmaker


SQLAlchemy provides a __`Session` class (bound to the engine)__ that the ORM uses to work with the database. __We can create this class by using `sessionmaker()`__ &rarr;

<pre><code data-trim contenteditable>
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
</code></pre>
{:.fragment}



</section>

<section markdown="block">
## Session

__This resulting `Session` class allows us to construct database sessions__ &rarr;

* {:.fragment} a `Session` is "a workspace for your objects, local to a particular database connection" ([see "Creating a Session"](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#creating-a-session))
* {:.fragment} sessions operate by beginning a transaction, which is then either committed or rolled back
* {:.fragment} a session can be reused for a new transaction
* {:.fragment} alternatively, a session can be closed at the same time the transaction ends (which removes the complexity of dealing with separate session and transaction scopes)
* {:.fragment} you can call `commit` and `rollback` on a session object
* {:.fragment} if there's an error in your transaction, you must `rollback` before issuing more queries

</section>

<section markdown="block">
## `INSERT` Example

__Here's an example of how using a session to add a new object may work:__ &rarr;

<pre><code data-trim contenteditable>
session = Session()
</code></pre>

<pre><code data-trim contenteditable>
# (assuming that table exists by using
# Base.metadata.create_all(engine))
f = Foo()
f.bar = 'qux'
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
session.add(f)
session.commit()
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Default Values, Primary Key

__When creating instances, you may notice some values are missing!__ 😮 &rarr;

* {:.fragment} `primary key`
* {:.fragment} `default` values for some properties

These are filled in when the transaction is committed.
{:.fragment}

</section>

<section markdown="block">
## Retrieving Data

__A `Query` object represents a `SELECT` statement__ &rarr;

* {:.fragment} `Query` objects are created by using a session's `query` method: `session.query`
* {:.fragment} the `query` method takes a class representing a table (an entity) or a list of classes as its first argument
* {:.fragment} `filter` can be called on the resulting `Query` object to apply a filter on the returned objects via _some expression_

<pre><code data-trim contenteditable>
result = session.query(Foo).filter(Foo.bar == 'qux')
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Query Object

`session.query` returns a query object. __Some methods that you can call on it include__ &rarr;

* {:.fragment} `filter(expression)` - only return objects that meet criteria, expression
* {:.fragment} `get(primary_key)` - retrieve one object by unique identifier
* {:.fragment} `first()`, `one()` and `one_or_none()` - retrieve only the first element of many, one element from result set of one... or one or none!
* {:.fragment} `limit(num)` - constrain number of objects to num

</section>


<section markdown="block">
## One to Many: Convenience

__Ideally, our objects would abstract away joins and make multiple tables seem like a single object composed/aggregated of other objects__ &rarr;

* {:.fragment} imagine a situation where you keep track of scooter rentals... and each scooter rental can have many notes associated with it.
* {:.fragment} it would be convenient to have access to the notes of a rental through an attribute of a rental object
* {:.fragment} (even if rentals and notes are separate table in our database)

<pre><code data-trim contenteditable>
rentals = session.query(Rental).filter(Rental.rental_id == 1)
print(rentals[0].notes)
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## One to Many Implementation

__To specify relationships in the ORM, you can use the `relationship` function and the `ForeignKey` `Column` type:__

<pre><code data-trim contenteditable>
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
</code></pre>
{:.fragment}

In the table that has one (that is the table that is referenced by a foreign key):
{:.fragment}

<pre><code data-trim contenteditable>
field_name = relationship(OtherTableClassName)
</code></pre>
{:.fragment}

In the table that has many (the table with the foreign key):
{:.fragment}

<pre><code data-trim contenteditable>
field_name_for_fk = Column(Integer, ForeignKey('other_table.other_table_id'))
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## An Example...

__Assuming that we have `rental` and `note`__ &rarr;

`rental`

* rental_id
* rental_date
* return_date
* email
* scooter_number

`note`

* note_id
* note_text
* note_date

</section>
<section markdown="block">
## Imports

__Lots o' imports__ &rarr;

<pre><code data-trim contenteditable>
import sqlalchemy
from sqlalchemy import create_engine
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# columns and their types, including fk relationships
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# declarative base, session, and datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Setup

__Create base class for ORM classes, `Engine` and `session`__ &rarr;

<pre><code data-trim contenteditable>
username, password = 'joe', 'data0480'
host, database = 'localhost', 'scratch'
dsn = f'postgres://{username}:{password}@{host}/{database}'
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
engine = create_engine(dsn, echo=True)
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()
</code></pre>
{:.fragment}
</section>


<section markdown="block">
## A Note

<pre><code data-trim contenteditable>
class Note(Base):
    __tablename__ = 'note'
    
    note_id = Column('note_id', Integer, primary_key=True)
    note_text = Column('note_text', String)
    note_date = Column('note_date', 
                       DateTime(timezone=True), 
                       default=datetime.utcnow)
    
    # match this up with primary key in parent table
    rental_id = Column(Integer, ForeignKey('rental.rental_id'))

    def __repr__(self):
        return f'{self.note_date} - {self.note_text}'
    
    def __str__(self):
        return self.__repr__() 
</code></pre>

</section>

<section markdown="block">
## A Rental

<pre><code data-trim contenteditable>
class Rental(Base):
    __tablename__ = 'rental'
    
    rental_id = Column('rental_id', Integer, primary_key=True)
    email = Column('email', String)
    scooter_number = Column('scooter_number', Integer)
    rental_date = Column('rental_date', 
                         DateTime(timezone=True), 
                         default=datetime.utcnow)
    return_date = Column('return_date', DateTime(timezone=True))
    
    notes = relationship(Note) # match w/ Note for one-to-many 
    
    def __repr__(self):
        return f'{self.rental_id}: {self.rental_date} to {self.return_date} - {self.email} - {self.scooter_number}'
    
    def __str__(self):
        return self.__repr__()
</code></pre>
</section>

<section markdown="block">
## CREATE and INSERT

<pre><code data-trim contenteditable>
# create tables
Base.metadata.create_all(engine)
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# create a rental
r = Rental()
r.scooter_number = 123
r.email = 'foo@foo.foo'
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
# add some notes
n1 = Note(note_text="not yet returned, but renter said scooter was damaged")
n2 = Note(note_text="also, spilled coffee on the controls")
r.notes = [n1, n2]
</code></pre>
{:.fragment}

<pre><code data-trim contenteditable>
session.add(r)
session.commit()
</code></pre>
{:.fragment}
</section>

<section markdown="block">
## Ask for the Scooter Back

__Use query to get single scooter__ &rarr;

<pre><code data-trim contenteditable>
result = session.query(Rental)
    .filter(Rental.rental_id == 1)
    .one()
</code></pre>
{:.fragment}

__Use `.notes` to get associated `Note` objects__ &rarr;
{:.fragment}

<pre><code data-trim contenteditable>
print(result.notes)
</code></pre>
{:.fragment}

</section>

<section markdown="block">
## Modeling Other Relationships


[See the official SQLAlchemy docs on basic relationships](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html) for implementations of:

* one-to-one
* many-to-many
* ...and others!
</section>
