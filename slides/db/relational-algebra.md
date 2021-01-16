---
layout: slides
title: "Relational Algebra"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Relational Databases Revisited

__So... _why_ are they called relational again?__ &rarr;

* {:.fragment} it's _actually not_ because there are relationships between tables
* {:.fragment} it's because relational databases are based on __the relational model__ for managing data 
	* {:.fragment} developed by Edgar F Codd in late 60's / early 70's
	* {:.fragment} all data is represented in terms of __tuples__ (think _rows_)
	* {:.fragment} tuples are grouped into relations (think _tables_)

</section>
<section markdown="block">
## Some Definitions


* {:.fragment} __attribute__
	* {:.fragment} a name and a domain (think _column name_ and _type_)
* {:.fragment} __attribute value__
	* {:.fragment} the attribute name along with a value from it's domain (so: an _instance_ of a type)
* {:.fragment} __tuple__ 
	* {:.fragment} a finite sequence of attribute values (though, for our purposes, does not have to be ordered)
	* {:.fragment} no two attribute values have the same name
* {:.fragment} __relation__
	* {:.fragment} a set of _tuples_ (think _table_)!


</section>

<section markdown="block">
## Also Known As

__An easy way to think about it is:__ &rarr;

* {:.fragment} a __relation__ is _like_ a table
* {:.fragment} a __tuple__ is _like_ a row
* {:.fragment} an __attribute__ is _like_ a column name

([see an image from wikipedia](https://en.wikipedia.org/wiki/Relation_(database)#/media/File:Relational_database_terms.svg))

</section>

<section markdown="block">
## Constraints from the Relational Model

The following constraints come out of the relational model for database management:

* {:.fragment} key constraints - duplicate tuples are not allowed in same relation 
	* {:.fragment} think _primary key_
	* {:.fragment} pk must be unique
	* {:.fragment} pk can't be null
* {:.fragment} domain constraints - data is valid 
	* {:.fragment} think _type_, along with _unique_, _not null_ and _default_
* {:.fragment} foreign key constraint - referential integrity of linked relations



</section>

