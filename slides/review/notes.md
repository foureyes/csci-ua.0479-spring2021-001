---
layout: slides
title: "Final Review"
---

<section markdown="block" class="intro-slide">
# {{ page.title }}

### {{ site.vars.course_number}}-{{ site.vars.course_section }}

<p><small></small></p>
</section>

<section markdown="block">
## Using the Following Tables

<pre><code data-trim contenteditable>
person
-----
id |first|last    |role id | role
---+-----+--------+--------+------------------
1   alice amin            1 frontend engineer
2   bob   bautista        2 systems administrator
3   carol carlin          3 backend engineer
4   dave  dang            1 frontend engineer
project_allocation
------------------
id|person_id|name        | hours
--+---------+------------+--------
1          1 favorites        12 
3          2 analytics         2 
3          3 analytics        12
4          2 new servers    10.5
</code></pre>

</section>

<section markdown="block">
## Update Anomaly

Repeated information in multiple rows.

Failure or missed update for name of a project allocation may lead to inconsistent project names.

<pre><code data-trim contenteditable>
id|person_id|name        | hours
--+---------+------------+--------
1          1 favorites        12 
3          2 analytics         2 
3          3 analytics        12
4          2 new servers    10.5
</code></pre>
</section>

<section markdown="block">
## Insertion Anomaly

There are some scenarios where data _can't_ be inserted...

What column or columns can be used for a primary key?

<pre><code data-trim contenteditable>
id|person_id|name        | hours
--+---------+------------+--------
1          1 favorites        12 
3          2 analytics         2 
3          3 analytics        12
4          2 new servers    10.5
</code></pre>

id and person id

</section>
<section markdown="block">
## Insertion Anomaly

A project that doesn't have anyone working in it can't be inserted (even though composite key, part of composite key still can't be null)!

<pre><code data-trim contenteditable>
id|person_id|name        | hours
--+---------+------------+--------
1          1 favorites        12 
3          2 analytics         2 
3          3 analytics        12
4          2 new servers    10.5
</code></pre>

Other scenarios, many involving keys / columns that are set to not null (ex: students and courses in same table... what if course related fields are not null, but student not in any courses for a semester).
</section>

<section markdown="block">
##  Deletion Anomaly

Removing data may inadvertently remove data that should not be deleted

* removing only person working in project...
* makes project go away!

</section>

<section markdown="block">
## Functional Dependency

functional dependency. Functional dependencies are a way of describing the interdependence of attributes or fields in our tables

when an attribute is dependent on the unique value of another attribute (so... if you know the value of one, you can infer the other)
when one attribute uniquely determines another attribute

* every value x is associated with precisely one y
* for example... person could have marital status: married or single... can only be associated with one value (not both)... marital status is functionaly dependent on person
* or with a person's id, you can retrieve their last name
* (otoh, with a person's id, you can't derive which project they're on... it can map to more than one project!)
* all other attributes in table have functional dependency on primary key 
</section>


<section markdown="block">
## 1NF

1. no repeating groups (address1, address2, address3)
2. atomicity (one column with multiple values: person + their projects as analytics,new servers,etc.
3. usually primary key is determined at this point


</section>

<section markdown="block">
## 2NF

1. already in 1NF
2. two ways to look at it:
	* not partial dependencies
	* all non-key attributes have functional dependency on ENTIRE key
3. (if one key, then already in 2NF)

</section>
