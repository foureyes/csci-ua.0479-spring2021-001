---
layout: slides
title: "Motivation for Database Design"
---

<script src="../../resources/js/table.js"></script>
<link rel="stylesheet" href="../../resources/css/data-table.css" type="text/css" media="screen" title="no title" charset="utf-8">


<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Definitions

__Let's get some jargon out of the way 🤓__ &rarr;

* {:.fragment} __entity__ <span class="fragment">- some _thing_ that we store data about (the sale of a property, an incident of a dog bite, a movie)</span>
* {:.fragment} __relation__ <span class="fragment">- a two-dimensional table consisting of columns and rows, with only one value at the intersection of a column and row</span>
* {:.fragment} __composite key__ <span class="fragment">- two or more columns in a table that uniquely identify a row in that table; no part of a composite key may be null</span>
* {:.fragment} we'll also take a look at some strange 👻 things that occur when working with a poorly designed database, which includes: __insertion__, __deletion__, and __update__ __anomalies__.

</section>

<section markdown="block">
## An Example Table


__Imagine that we store all information about courses and students in the following table__ &rarr;

* {:.header} netid, first, last, course_num, name, room, semester, year
* abc123, alice, cho, 0480-003, DMA, 101, fa, 2019
* abc123, alice, cho, 0380-001, E-Sports, 317, fa, 2019
* bcd456, bob, davis, 0380-001, E-Sports, 317, sp, 2017
* cd78, carol, diaz, 0480-007, How 2 Troll, 202, fa, 2019
* cde901, carol, evans, 0380-001, E-Sports, 317, fa, 2019
* efg456, eva, gu, 0480-003, DMA, 101, fa, 2019
{:.fragment}
{:.table}

BTW, what might be a good primary 🔑 for this table? <span class="fragment"> Would `netid` work?</span> <span class="fragment">`netid`  and `course_num`?</span> <span class="fragment">or... how about `netid`, `course_num`, `semester`, and `year`?</span>
{:.fragment}

</section>

<section markdown="block">
## Is This Possible?

__Can we...__ &rarr;

* {:.fragment} show all students enrolled in a particular course? <span class="fragment">✅</span>
* {:.fragment} how about all courses in fall 2019 that have students _enrolled in it_? <span class="fragment">✅</span>

OK! 👌... this looks like a good table. Let's move on. ⏩
{:.fragment}


</section>

<section markdown="block">
## But Wait 🛑


__Can we show _all courses_ in fall 2019?__ <span class="fragment">🤔 er... not without some strange things going on</span> &rarr;

* {:.fragment} this table tangles courses, students and enrollment
* {:.fragment} a course can't exist unless someone enrolls in it (inserting only course data would cause `netid`, a part of the composite primary key, to be `null`! 😕)
* {:.fragment} this is an __insertion anomaly__

</section>
<section markdown="block">
## Insertion Anomaly

An __insertion anomaly__ is an issue that occurs when data cannot be inserted because of incomplete primary key (no part of a composite primary key can be null)

In our example... &rarr;

* {:.fragment} we can't a student to our database unless they enroll in a course
* {:.fragment} we can't add a course unless one student enrolls in it

Typically, insertion anomalies arise from having data from more than one _entity_ in a table... 
{:.fragment}

Consequently, inserting data about one entity forces the insertion of data from another entity even when that extra data is not needed.
{:.fragment}


</section>

<section markdown="block">
## Another Question

__Can we have a student withdraw from a course or leave the school?__ <span class="fragment">sort of... we can delete a row</span> &rarr;

* {:.fragment} but what happens if all students withdraw from a course? <span class="fragment">the course data ceases to exist!</span>
* {:.fragment} deleting only the student data would, again, result in a partially null composite key
* {:.fragment} this is a __deletion anomaly__


</section>

<section markdown="block">
## Deletion Anomaly

A __deletion anomaly__ occurs when the deletion of data about one entity in a row causes a part of the composite primary key for that row to be null. 

The only recourse is to delete the _entire row_, but that could cause unintended data loss! 😮

In our example... &rarr;

* {:.fragment} if a student is the last student in a course, that student can't be removed without removing the course too!
* {:.fragment} or... if a course were canceled, and one student is only enrolled in that course, then we will no longer have that student's data

Like insertion anomalies, deletion anomalies arise from having data from more than one _entity_ in a table.
{:.fragment}
</section>

<section markdown="block">
## MOAR Questions!

__OK, let's say that student decides to legally change their name to `Robert'); DROP TABLE--` ([y not, amirite 🤷‍♀️?](https://xkcd.com/327/))__ &rarr;

Is it possible to change the name of the student (sql injection aside)? <span class="fragment">✅, of course! ...But &rarr;</span>

* {:.fragment} you'll have to change it in multiple places
* {:.fragment} if care isn't taken, only a subset of the duplicate data may change causing inconsistent data!
* {:.fragment} __This is an update anomaly__

</section>

<section markdown="block">
## Update Anomaly

An __update anomaly__ occurs when a subset of duplicate data is updated leading to inconsistent data (that is, when all instances of the same data are not changed at the same time).

* {:.fragment} this is mainly due to redundant data
* {:.fragment} of course, redundant data also means unnecessary usage of space
</section>


<section markdown="block">
## Why Take the Time to Design Your Database?

__Lack of planning and design will lead to ...__ &rarr;


* {:.fragment} redundant (and as consequence, potentially inconsistent data)
* {:.fragment} difficulty adding data (__insert anomalies__)
* {:.fragment} difficulty removing data (__deletion anomalies__)
* {:.fragment} data prone to inconsistencies  (__update anomalies__)

Good database design also allows for:
{:.fragment}

* {:.fragment} the enforcing of constraints and referential integrity (given the mechanisms available in a relational database)
* {:.fragment} growth / expandability
* {:.fragment} overall ease of conceptual understanding
</section>
