---
layout: slides
title: "Database Design"
---

<script src="../../resources/js/table.js"></script>
<link rel="stylesheet" href="../../resources/css/data-table.css" type="text/css" media="screen" title="no title" charset="utf-8">

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Steps for Writing Software?

__So... u want to write an _awesome_ app..__ &rarr;

What are the high level steps for writing a program (_do you just start coding_)?
{:.fragment}

1. {:.fragment} requirements
2. {:.fragment} implementation
3. {:.fragment} testing
4. {:.fragment} bug fixing, refactoring (go back to 2 or even 1)

(Regardless of software development methodology you use, you'll end up using some variant of the above)
{:.fragment}

</section>

<section markdown="block">
## Makin' a Database

__As with software engineering, you don't want to just jump in and start creating tables haphazardly...__ &rarr;

The database design process may look something like:
{:.fragment}

1. {:.fragment} requirements analysis - specify the problem, work with _domain experts_, explore existing data, etc. ... to: 
	* {:.fragment} determine what data needs to be stored 
	* {:.fragment} how the data is related to each other?
2. {:.fragment} __conceptual design__ - just entities, attributes and relationships
	* {:.fragment} use requirements to formally describe the data, relationships and constraints
	* {:.fragment} says nothing about _actual_ implementation (no details on platform, physical storage, etc.)	
	* {:.fragment} most simple model

</section>

<section markdown="block">
## Continued...

__After conceptual design...__ &rarr;

3. {:.fragment} translate conceptual design to __logical design__ - no database creation yet, but add types, unique identifiers... more complex than conceptual design
4. {:.fragment} translate logical design to actual _objects_ in specific DBMS / db platform

</section>
<section markdown="block">
## Design Rules

What should your database design accomplish? &rarr;

* {:.fragment} ability to solve problem
	* understand problem
	* fulfill _business_ requirements
		* reporting and data analysis
* {:.fragment} can store required data
	* structure can satisfy required queries
	* correct fields and types of fields
* {:.fragment}  models relationships

</section>

<section markdown="block">
## Design Rules Continued 

* {:.fragment}  as we saw previously... data integrity
	* data is correct
	* relationships are correct
	* ... avoid anomalies, inconsistency, and redundancy
*  {:.fragment} flexibility to handle future changes
*  {:.fragment} performance, efficiency
	* indexes, modify queries, etc.
	* typically done after-the-fact
	* design should be influenced by this if efficiency is the first requirement, but typically this leads to compromises in other parts of the design

</section>

<section markdown="block">
## Jargon Again

* {:.fragment} __data model__ - specifies the data and relationships to a DBMS; The actual implementation may vary based on the DBMS, so the data model is independent from the DBMS that is being used.
* {:.fragment} __entity__ - some _thing_ that we store data about, like a student, a dog bite incident, a pizza order, etc (essentially, a table)
* {:.fragment} an __attribute__ is the data that describes an entity, like netid, breed of dog, or type of crust (think: columns)
* {:.fragment} __entity identifier__ - an attribute or attributes that uniquely identify an instance of an entity (u no, like, primary 🔑)
* {:.fragment} an __instance__ of an entity is the actual attribute data of an entity (like a row in a table)
</section>


<section markdown="block">
## Attribute Values

__An attribute _should_ contain a single value__. You could imagine, though, an attribute w/ multiple values... &rarr;

* {:.fragment} a student may have an attribute called `contact_info`, containing phone, multiple email addresses, and an ig username (uh? wat?) 
* {:.fragment} maybe like: `"555-555-5555, pg12@nyu.edu, sql.is.my.life@nyu.edu, @sqlXallXday"`
* {:.fragment} this is a __multi value attribute__ <span class="fragment">and it's not great design. Why?</span>
	* {:.fragment} searching on that particular attribute slower (no longer exact match, but sub)
	* {:.fragment} choosing only that piece of information is more difficult
	* {:.fragment} better to have separate attributes
* {:.fragment} your dbms may support multi value attributes, tho!
</section>

<section markdown="block">
## Attribute Domains

__An attribute's value can be restricted to a set of possible values__ &rarr;

* {:.fragment} this is an attribute's domain
* {:.fragment} for example, a student's gpa should be a floating point number, a pie can be one of: small, medium, large, or [record breaking](https://imgur.com/gallery/YLFomNd)
* {:.fragment} it's essentially _type_

</section>

<section markdown="block">
## Entities Can be Related

__Entities can be related to each other. What are these relationship types again?__ &rarr;

* {:.fragment} one to one
* {:.fragment} one to many
* {:.fragment} many to many
* {:.fragment} it's possible that either side can be zero too... for example:
	* {:.fragment} a student can exist without a related courses
	* {:.fragment} a course can exist without students
</section>

<section markdown="block">
## Weak Entities

A __weak entity__ is an __entity that must be related to another entity__, otherwise, it cannot exist.

Can you think of some examples of weak entities in any domain? &rarr;

1. {:.fragment} a pizza order cannot exist with a customer
2. {:.fragment} an exam can't exist without a course 

In these cases, the relationships are mandatory for one of the entities (the other side can't be zero)
{:.fragment} 

For implementation, what constraints do you think would be necessary for a weak entity field that references the table that it's dependant on?
{:.fragment}

* {:.fragment} foreign key
* {:.fragment} not null

</section>

<section markdown="block">
## Composite Entities

A __composite entity__ models the relationship between other entities.

* {:.fragment} for example... the relationship between a student and a course could be an _enrollment_
* {:.fragment} it's essentially the _join_ table in a many-to-many

</section>

<section markdown="block">
## Documentation, ER diagrams 

We can use an __Entity Relationship Diagram__ to show entities, their attributes and their relationships.

Some are picky about what's a true ER diagram, but for our purposes, it could refer to any style of ER diagram

* [wikipedia has a list of 'em](https://en.wikipedia.org/wiki/Entity–relationship_model)
* however, we'll stick to either:
	1. Chen
	2. _crow's feet_

</section>



<section markdown="block">
## Demo

Please [see the book](https://learning-oreilly-com.proxy.library.nyu.edu/library/view/relational-database-design/9780123747303/B9780123747303000048.xhtml) for a more complete guide on ER diagrams. Let's using the following types of diagrams:

1. {:.fragment} Chen
2. {:.fragment} Crow's Feet

To model...
{:.fragment}

* entities
* attributes
* relationships
* join tables
{:.fragment}


</section>


