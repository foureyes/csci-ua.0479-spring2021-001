review
=====

* topics
* hw 5 solution / background on normalization


topics
----
* since midterm exam (around sql stuff)
	* cumulative in that: still need to know how to write python
		* classes
		* can i split a comma separated file
		* but focus of questions is not ^^^
	* there won't be specific questions for python only
		* use a list comprehension to do x
	* on the exam
		* bias towards material around class 10 
		* sql
			* basics: types, select, from, where, group by, having, limit, etc.
			* basic/intermediate: joins, subqueries, common table expressions, insert ... from
			* intermediate: (with reference) built-in functions, such as to_char, regexp_split_to_array, etc.
* most coding questions will come from homework / be homework inspired
* won't be in coding questions, but you should know concepts
	* pyscopg2
	* firebase
	* d3
	* making your own sql functions (know how to read, but not write)
* won't be on exam at all
	* anything beyond 3rd normal form will not be on!


review topics
-----
* hw 5
	* database design
	* normalization
		* normal forms
		* practice questions
	* er diagram
	* create statements if u want?
* sql alchemy relationships
* explain / analyze, indexes

db design
------
reduce redundant data
prevent update/insert/delete anomalies
make it easy expand database
models domain appropriately

Sample Data
----
a project portfolio

* can u allocate appropriate resources to projects ????
* with the resources that u have ???
* idk! maybe we need a db to figyer this out????

```
person
----
id | first | last    | role id | role
1  | alice | amin    |       1 | frontend engineer
2  | bob   | basil   |       2 | systems administrator
3  | carol | cortez  |       3 | backend engineer
4  | dan   | dang    |       1 | frontend engineer


project_allocations
id | project id | person_id | name           | hours
1  | 1          | 1         | favs feature   | 10
2  | 1          | 2         | favs feature   |  2
3  | 2          | 2         | analytics      |  7
4  | 3          | 3         | api            | 12
```

update anomaly .... a failed or incorrect update leads to inconsistent data
insert anomaly .... data model is such that some data cannot be inserted
(usually because something is a primary key or not null)
delete anomaly .... inadvertently deleting data because its tied to data that you actually wanted to delete

functional dependency ---> if you have value from one set a values... it maps to only precisely one value from another set of values

marital status has functional dependency on person id

```
person_id| marital status (married, single)
=========+=================================
2        | married
```

in reference
-----
sql types

```
crow's foot (martin)
>| -------- |< one or many
-|| -------- ||-exactly one
>o--------o< zero or many
-|o--------o|- zero or many

o | ... modality
> |... cardinality

-||----|<  eactly one to one/many
```

1NF
====
1. no "repeating groups" - ...really meant that you shouldn't have multiple values in a single col/row intersection, but term has also been used to describe these situations:
	* repeated columns: 
		* name | hours | proj1 | proj2 | proj3
	* atomicity:
		* bob | 7 | favs,analytics  <---- multiple values crammed into single field!
2. sometimes a key is identified 

2NF
=====
1. it's in first normal form
2. either:
	* no partial dependencies - no non key attributes are dependent on only part of a composite key (candidate keys)
	* every non-key attribute is functionally dependent on the ENTIRE/whole key
3. if there's no composite key then it's already 2NF


3NF
=====

1. there no non-key attributes that are functionally dep on another non-key attribute

abt homework 5
=====

many to many relationship through some table



person >|-----|< rental >|-----|< scooter
                  \/
				  --
				  |
				  |
				  extra fees
                  notes

rental
====
date_borrowed
date_returned


person

reference_id fk to person

alternatively: use join table


how do you import data?
i haz database
i haz csv
wat?

* extract 
	* python
		* split
		* csv module
		* pandas
	* copy <--- in sql, \copy <-- psql command
* transform
	* python
		* regular python
		* pandas
	* some combination of inserts, selects, updates
		* (on a staging table)
* load
	* python
		* psycopg2 + insert queries
		* sqlalchemy
			* raw sql
			* expression language
			* sqlalchemy orm
	* sql (already there!)

for firebase visualization

extract
	* same as above (csv module, pandas, etc.)
transform
	* same as above (regular python, whatever)
load
	* python client 


sqlalchemy
=====
in your class
1.define mappings:

__tablename__ = 'actual_table_name'
class_attribute1 = Column('column_name_in_table_1', Type, ...)
class_attributeN = Column('column_name_in_table_N', Type, ForeignKey('table.col'))
specify all the attribute want to map to actual columns, including fk
(you don't have to specify every column)

2. convenience attributes that allow you to refer to related instances from another class
project.... employee

attributes on instances (not actually in table)
employee.project
project.employees

project has many employees
employee will have project id (determined by FK in sql alchemy)

attrib_name = relationship('RelatedClassName', back_populates='refer_to_me_with_this')

Employee
	project = relationship('Project', back_populates='employees')

Project
	employees = relationship('Employee', back_populates='project')


syntax
----
select col1, col2... from table1 inner join....

logical ordering
-----
1. FROM (JOINS go here too)
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

_actual_ order
????

index.... they make ur your query go faster

* compromise is space
* advantage faster lookups

explain
* will try to tell you what the query planner might do

explain with analyze
* will do explain and then execute the query
* and give you timings

* always use begin / commit or rollback
* explain... (don't do analyze)





















































































